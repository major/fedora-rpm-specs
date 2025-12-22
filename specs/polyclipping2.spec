# The Clipper C++ crystallographic library already uses the name "clipper".
# The developer is fine with the chosen name polyclipping for the previous version
# of the library. This rpm packages the "clipper2" polygon clipping library

# Conditionals for optional features
%bcond_without tests  # Disable tests by default
%bcond_without docs   # Enable docs by default

Name:           polyclipping2
Version:        2.0.1
Release:        %autorelease
Summary:        Polygon Clipping and Offsetting Library v2
License:        BSL-1.0
URL:            https://angusj.com/clipper2/Docs/Overview.htm
Source:         https://github.com/AngusJohnson/Clipper2/archive/refs/tags/Clipper2_%{version}.tar.gz

# Build dependencies
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtest-devel

# Obsolete the redundant clipper2 only for Rawhide
# https://bugzilla.redhat.com/show_bug.cgi?id=2386078
Obsoletes:      clipper2 < %{version}
Provides:       clipper2 = %{version}

%description
This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

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
    -DCLIPPER2_HI_PRECISION=ON \
    -DCLIPPER2_PKGCONFIG=ON \
    -DUSE_EXTERNAL_GTEST=ON
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

%files
%license LICENSE
%doc README.md
%{_libdir}/libClipper2.so.2
%{_libdir}/libClipper2.so.%{version}
%{_libdir}/libClipper2Z.so.2
%{_libdir}/libClipper2Z.so.%{version}

%files devel
%license LICENSE
%{_libdir}/pkgconfig/Clipper2.pc
%{_libdir}/pkgconfig/Clipper2Z.pc
%{_includedir}/clipper2/
%{_libdir}/libClipper2.so
%{_libdir}/libClipper2Z.so
%{_libdir}/cmake/clipper2/

# Documentation
%if %{with docs}
%files doc
%doc %{_docdir}/%{name}
%endif

%changelog
%autochangelog
