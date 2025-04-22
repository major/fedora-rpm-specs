%global _description %{expand:
HighFive is a modern header-only C++11 friendly interface for libhdf5.

HighFive supports STL vector/string, Boost::UBLAS, Boost::Multi-array and
Xtensor. It handles C++ from/to HDF5 with automatic type mapping. HighFive does
not require additional libraries (see dependencies).

It integrates nicely with other CMake projects by defining (and exporting) a
HighFive target.

Design:
- Simple C++-ish minimalist interface
- No other dependency than libhdf5
- Zero overhead
- Support C++11

Feature support:
- create/read/write files, datasets, attributes, groups, dataspaces.
- automatic memory management / ref counting
- automatic conversion of std::vector and nested std::vector from/to any
  dataset with basic types
- automatic conversion of std::string to/from variable length string dataset
- selection() / slice support
- parallel Read/Write operations from several nodes with Parallel HDF5
- Advanced types: Compound, Enum, Arrays of Fixed-length strings, References
  etc… (see ChangeLog)

Known flaws:
- HighFive is not thread-safe. At best it has the same limitations as the HDF5
  library. However, HighFive objects modify their members without protecting
  these writes. Users have reported that HighFive is not thread-safe even when
  using the threadsafe HDF5 library, e.g.,
  https://github.com/BlueBrain/HighFive/discussions/675.
- Eigen support in core HighFive is broken. See
  https://github.com/BlueBrain/HighFive/issues/532. H5Easy is not affected.
- The support of fixed length strings isn’t ideal.}

%bcond tests 1

# Header only, so no debuginfo is generated
%global debug_package %{nil}

Name:           highfive
Version:        2.10.1
Release:        %autorelease
Summary:        Header-only C++ HDF5 interface

# SPDX
License:        BSL-1.0
URL:            https://highfive-devs.github.io/highfive/
Source:         https://github.com/highfive-devs/highfive/archive/v%{version}/highfive-%{version}.tar.gz

# Downstream-only: Patch all cmake_minimum_required from 3.1 to 3.5
#
# This fixes compatibility with CMake 4. It does not make sense to offer
# this upstream because a larger CMake modernization effort was already
# implemented for the upcoming 3.0.0 release.
Patch:          0001-Downstream-only-Patch-all-cmake_minimum_required-fro.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  catch-devel
# Technically optional, enabled by default
# Our choice vs. make
BuildRequires:  ninja-build

BuildRequires:  hdf5-devel
# Optional but included in Fedora, so we use these. The -static versions are
# required by guidelines for tracking header-only libraries
BuildRequires:  boost-devel
BuildRequires:  (cmake(eigen3) with eigen3-static)
BuildRequires:  (cmake(xtensor) with xtensor-static)
BuildRequires:  cmake(opencv)

%description %_description


%package        devel
Summary:        Development files for HighFive
Provides:       highfive%{?_isa} = %{version}-%{release}
Provides:       highfive-static%{?_isa} = %{version}-%{release}
# Unarched version is needed since arched BuildRequires must not be used
Provides:       highfive-static = %{version}-%{release}

Requires:       hdf5-devel
# Optional, but we want -devel package users to have all features available.
Requires:       boost-devel
Requires:       (cmake(eigen3) with eigen3-static)
Requires:       (cmake(xtensor) with xtensor-static)
Requires:       cmake(opencv)

%description    devel
The highfive-devel package contains libraries and header files for
developing applications that use HighFive.


%prep
%autosetup -p1


%build
%if %{with tests}
# The unit tests intentionally test deprecated APIs; silence these warnings so
# we are more likely to notice any real problems.
CXXFLAGS="${CXXFLAGS} -Wno-deprecated-declarations"
%endif
%cmake \
    -DHIGHFIVE_USE_BOOST:BOOL=TRUE \
    -DHIGHFIVE_USE_XTENSOR:BOOL=TRUE \
    -DHIGHFIVE_USE_EIGEN:BOOL=TRUE \
    -DHIGHFIVE_USE_OPENCV:BOOL=TRUE \
    -DHIGHFIVE_EXAMPLES:BOOL=TRUE \
    -DHIGHFIVE_UNIT_TESTS:BOOL=%{?with_tests:TRUE}%{?!with_tests:FALSE} \
    -DHIGHFIVE_BUILD_DOCS:BOOL=FALSE \
    -GNinja
%cmake_build


%install
%cmake_install
# Move the CMake configurations to the correct location
[ ! -d '%{buildroot}/%{_libdir}/cmake/HighFive' ]
install -d '%{buildroot}/%{_libdir}/cmake'
mv -v '%{buildroot}/%{_datadir}/HighFive/CMake' \
    '%{buildroot}/%{_libdir}/cmake/HighFive'


%check
%if %{with tests}
%ctest -VV
%endif


%files devel
%license LICENSE
%doc README.md AUTHORS.txt CHANGELOG.md
%{_includedir}/highfive/
%{_libdir}/cmake/HighFive/


%changelog
%autochangelog
