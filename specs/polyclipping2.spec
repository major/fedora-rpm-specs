# The Clipper C++ crystallographic library already uses the name "clipper".
# The developer is fine with the choosen name polyclipping for the previous version
# of the library. This rpm packages the "clipper2" polygon clipping library

%global _vpath_srcdir CPP

Name:           polyclipping2
Version:        1.4.0
Release:        2%{?dist}
Summary:        Polygon Clipping and Offsetting Library v2
License:        BSL-1.0
URL:            https://angusj.com/clipper2/Docs/Overview.htm
Source:         https://github.com/AngusJohnson/Clipper2/archive/refs/tags/Clipper2_%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtest-devel

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


%prep
%autosetup -n Clipper2-Clipper2_%{version} -p0
rm -rf CPP/Tests/googletest


%build
%cmake -DUSE_EXTERNAL_GTEST=ON
%cmake_build


%install
%cmake_install


%check
pushd %{_vpath_builddir}
./ClipperTests
./ClipperTestsZ
popd


%files
%license LICENSE
%doc README.md
%{_libdir}/libClipper2.so.1
%{_libdir}/libClipper2.so.%{version}
%{_libdir}/libClipper2Z.so.1
%{_libdir}/libClipper2Z.so.%{version}


%files devel
%{_libdir}/pkgconfig/Clipper2.pc
%{_libdir}/pkgconfig/Clipper2Z.pc
%{_includedir}/clipper2/
%{_libdir}/libClipper2.so
%{_libdir}/libClipper2Z.so
%{_libdir}/cmake


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Thomas Sailer <fedora@tsailer.ch> - 1.4.0-1
- Update to 1.4.0
- Package cmake files
- Reviewer comments

* Wed Jun 05 2024 Thomas Sailer <fedora@tsailer.ch> - 1.3.0-1
- Initial package based on polyclipping
