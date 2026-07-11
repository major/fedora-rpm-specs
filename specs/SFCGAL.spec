Summary: C++ wrapper library around CGAL for PostGIS
Name: SFCGAL
Version: 2.3.0
Release: %autorelease
License: LGPL-2.0-or-later
URL: https://gitlab.com/sfcgal/SFCGAL/
Source: https://gitlab.com/sfcgal/SFCGAL/-/archive/v%{version}/SFCGAL-v%{version}.tar.bz2

BuildRequires: CGAL-devel >= 5.6
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: boost-devel
BuildRequires: mpfr-devel
BuildRequires: gmp-devel
BuildRequires: json-devel

%description
SFCGAL is a C++ wrapper library around CGAL with the aim of supporting
ISO 19107:2013 and OGC Simple Features Access 1.2 for 3D operations.

SFCGAL provides standard compliant geometry types and operations, that
can be accessed from its C or C++ APIs. PostGIS uses the C API, to
expose some SFCGAL's functions in spatial databases (cf. PostGIS
manual).

Geometry coordinates have an exact rational number representation and
can be either 2D or 3D.

%package devel
Summary: The development files for SFCGAL
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake-devel

%description devel
Development headers and libraries for SFCGAL.

%prep
%autosetup -p0 -n SFCGAL-v%{version}

%build
%cmake -D LIB_INSTALL_DIR=%{_lib} -DBoost_NO_BOOST_CMAKE=BOOL:ON -DCMAKE_SKIP_RPATH:BOOL=YES -DSFCGAL_BUILD_DOC:BOOL=YES
%cmake_build
(cd doc; doxygen)

%install
%cmake_install

%files
%doc AUTHORS README.md NEWS
%license LICENSE
%{_libdir}/libSFCGAL.so.2*

%files devel
%{_includedir}/SFCGAL
%{_libdir}/libSFCGAL.so
%{_libdir}/pkgconfig/sfcgal.pc
%{_libdir}/cmake/SFCGAL
%{_bindir}/sfcgal-config
%doc example/ doc/html

%changelog
%autochangelog
