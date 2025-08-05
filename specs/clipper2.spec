# Conditionals for optional features
%bcond_without tests  # Enable tests by default
%bcond_without docs   # Enable docs by default

%global forgeurl https://github.com/AngusJohnson/Clipper2
%global libname clipper2

Version:        1.5.4
%forgemeta
Name:           %{libname}

Release:        %autorelease
Summary:        Polygon Clipping and Offsetting Library

License:        BSL-1.0
URL:            %{forgeurl}
# Standardized source URL format with proper tarball naming
Source0:        %{forgeurl}/archive/Clipper2_%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Build dependencies
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel

%description
Clipper2 is a modern rewrite of the original Clipper library
with improved performance, support for multiple fill rules,
robust self-intersecting polygon handling, and high precision offsetting.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for Clipper2, including headers, CMake config,
and pkg-config files.

%package static
Summary:        Static files for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Static libraries for Clipper2.

%if %{with docs}
%package doc
Summary:        Documentation for %{name}
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildArch:      noarch
%description doc
Documentation for Clipper2 library.
%endif

%prep
%autosetup -n Clipper2-Clipper2_%{version}

%build
%cmake -S CPP \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DCLIPPER2_BUILD_EXAMPLES=OFF \
    -DCLIPPER2_BUILD_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
    -DCLIPPER2_DOCS=%{?with_docs:ON}%{!?with_docs:OFF} \
    -DCLIPPER2_PKGCONFIG=ON \
    -DUSE_EXTERNAL_GTEST=ON \
    -DCLIPPER2_HI_PRECISION=ON

%cmake_build

%install
%cmake_install

%if %{with tests}
%check
# Skip failing test
# https://github.com/AngusJohnson/Clipper2/issues/1001
%ctest -E  "TestMultiplePolygons" \
   --test-dir %{_vpath_builddir}  # Out-of-source test directory
%endif

# Main package contains runtime components
%files
%license LICENSE
%doc README.md
%{_libdir}/libClipper2.so.1{,.*}
%{_libdir}/libClipper2Z.so.1{,.*}

# Development package contains static assets
%files devel
%license LICENSE
%{_includedir}/clipper2/
%{_libdir}/libClipper2.so
%{_libdir}/libClipper2Z.so
%{_libdir}/pkgconfig/Clipper2.pc
%{_libdir}/pkgconfig/Clipper2Z.pc
%{_libdir}/cmake/clipper2/

%files static
%{_libdir}/libClipper2utils.a
%{_libdir}/libClipper2Zutils.a

# Documentation
%if %{with docs}
%files doc
%doc %{_docdir}/%{name}
%endif

%changelog
%autochangelog
