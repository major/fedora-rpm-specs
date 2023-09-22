%global pretty_name HighFive

%global _description %{expand:
HighFive is a modern header-only C++11 friendly interface for libhdf5.

HighFive supports STL vector/string, Boost::UBLAS, Boost::Multi-array, Eigen
and Xtensor. It handles C++ from/to HDF5 with automatic type mapping. HighFive
does not require additional libraries (see dependencies) and supports both HDF5
thread safety and Parallel HDF5 (contrary to the official hdf5 cpp)

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
  etc... (see ChangeLog)
}

%bcond_without tests
%bcond_without docs

# Header only, so no debuginfo is generated
%global debug_package %{nil}

Name:           highfive
Version:        2.7.1
Release:        %autorelease
Summary:        Header-only C++ HDF5 interface

License:        Boost
URL:            https://bluebrain.github.io/HighFive/
Source0:        https://github.com/BlueBrain/HighFive/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  hdf5-devel
BuildRequires:  catch-devel
# Technically optional, enabled by default
BuildRequires:  boost-devel
# Our choice vs. make
BuildRequires:  ninja-build

# Optional but included in Fedora, so we use these
BuildRequires:  cmake(eigen3)
BuildRequires:  cmake(xtensor)
%ifnarch %{arm32}
BuildRequires:  cmake(opencv)
%endif
# The -static versions are required by guidelines for tracking header-only
# libraries
BuildRequires:  eigen3-static
BuildRequires:  xtensor-static

%if %{with docs}
BuildRequires:  doxygen
%endif

%description %_description


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
# Unarched version is needed since arched BuildRequires must not be used
Provides:       %{name}-static = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with docs}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}
%endif


%prep
%autosetup -n %{pretty_name}-%{version} -S git -p1


%build
# With g++13, warnings are generated from xtl side, e.g.
# /usr/include/xtl/xsequence.hpp:132:24: error: 'ret' may be used uninitialized
# [-Werror=maybe-uninitialized]
# Disabling -Werror
sed -i CMake/config/CompilerFlagsHelpers.cmake -e 's|-Werror ||'

%if %{with tests}
%set_build_flags
# The unit tests intentionally test deprecated APIs; silence these warnings so
# we are more likely to notice any real problems.
CXXFLAGS="${CXXFLAGS} -Wno-deprecated-declarations"
%endif
%cmake \
    -DHIGHFIVE_USE_BOOST:BOOL=TRUE \
    -DHIGHFIVE_USE_XTENSOR:BOOL=TRUE \
    -DHIGHFIVE_USE_EIGEN:BOOL=TRUE \
%ifnarch %{arm32}
    -DHIGHFIVE_USE_OPENCV:BOOL=TRUE \
%endif
    -DHIGHFIVE_EXAMPLES:BOOL=TRUE \
    -DHIGHFIVE_UNIT_TESTS:BOOL=%{?with_tests:TRUE}%{?!with_tests:FALSE} \
    -DHIGHFIVE_BUILD_DOCS:BOOL=%{?with_docs:TRUE}%{?!with_docs:FALSE} \
    -GNinja
%cmake_build
%if %{with docs}
%cmake_build --target doc
%endif


%install
%cmake_install
# Move the CMake configurations to the correct location
[ ! -d '%{buildroot}/%{_libdir}/cmake/%{pretty_name}' ]
install -d '%{buildroot}/%{_libdir}/cmake'
mv -v '%{buildroot}/%{_datadir}/%{pretty_name}/CMake' \
    '%{buildroot}/%{_libdir}/cmake/%{pretty_name}'


%check
%if %{with tests}
# Run tests sequentially: https://github.com/BlueBrain/HighFive/issues/825
%ctest -VV -j 1
%endif


%files devel
%license LICENSE
%doc README.md AUTHORS.txt CHANGELOG.md
%{_includedir}/%{name}
%{_libdir}/cmake/%{pretty_name}


%if %{with docs}
%files doc
%license LICENSE
%doc %{_vpath_builddir}/doc/html
%endif


%changelog
%autochangelog
