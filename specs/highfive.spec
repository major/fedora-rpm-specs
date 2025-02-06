%global pretty_name HighFive

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
# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# We could enable the Doxygen PDF documentation as a substitute, but beginning
# with 2.8.0 we encounter:
#
#   ! LaTeX Error: File `topics.tex' not found.
#
# This seems like a Doxygen bug, but it’s not clear exactly what kind of bug,
# or what can be done about it.
%bcond docs 0

# Header only, so no debuginfo is generated
%global debug_package %{nil}

Name:           highfive
Version:        2.10.0
Release:        %autorelease
Summary:        Header-only C++ HDF5 interface

# SPDX
License:        BSL-1.0
URL:            https://bluebrain.github.io/HighFive/
Source:         https://github.com/BlueBrain/HighFive/archive/v%{version}/%{name}-%{version}.tar.gz

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

%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  doxygen-latex
BuildRequires:  make
%endif

%description %_description


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
# Unarched version is needed since arched BuildRequires must not be used
Provides:       %{name}-static = %{version}-%{release}

Requires:       hdf5-devel
# Optional, but we want -devel package users to have all features available.
Requires:       boost-devel
Requires:       (cmake(eigen3) with eigen3-static)
Requires:       (cmake(xtensor) with xtensor-static)
Requires:       cmake(opencv)

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
%autosetup -n %{pretty_name}-%{version}

%if %{with docs}
# We enable the Doxygen PDF documentation as a substitute. We must enable
# GENERATE_LATEX and LATEX_BATCHMODE; the rest are precautionary and should
# already be set as we like them. We also disable GENERATE_HTML, since we will
# not use it.
sed -r -i \
    -e "s/^([[:blank:]]*(GENERATE_LATEX|LATEX_BATCHMODE|USE_PDFLATEX|\
PDF_HYPERLINKS)[[:blank:]]*=[[:blank:]]*)NO[[:blank:]]*/\1YES/" \
    -e "s/^([[:blank:]]*(LATEX_TIMESTAMP|GENERATE_HTML)\
[[:blank:]]*=[[:blank:]]*)YES[[:blank:]]*/\1NO/" \
    doc/Doxyfile
%endif


%build
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
    -DHIGHFIVE_USE_OPENCV:BOOL=TRUE \
    -DHIGHFIVE_EXAMPLES:BOOL=TRUE \
    -DHIGHFIVE_UNIT_TESTS:BOOL=%{?with_tests:TRUE}%{?!with_tests:FALSE} \
    -DHIGHFIVE_BUILD_DOCS:BOOL=%{?with_docs:TRUE}%{?!with_docs:FALSE} \
    -GNinja
%cmake_build
%if %{with docs}
%cmake_build --target doc
%make_build -C %{_vpath_builddir}/doc/latex
mv %{_vpath_builddir}/doc/latex/refman.pdf \
    %{_vpath_builddir}/doc/latex/%{pretty_name}.pdf
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
%doc %{_vpath_builddir}/doc/latex/%{pretty_name}.pdf
%endif


%changelog
%autochangelog
