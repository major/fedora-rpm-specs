%global gitdate 20230829.232718
%global cmakever 5.240.0
%global commit0 8260e304c367377c16bf564cee43ee13479e66d5

%undefine __cmake_in_source_build

%global framework karchive

Name:           kf6-%{framework}
Version:        %{cmakever}^%{gitdate}.%{commit0}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with archive functions
License:        LGPL-2.0-or-later AND BSD-2-Clause
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{commit0}.tar.gz

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
Requires:       kf6-filesystem
BuildRequires:  kf6-rpm-macros

# KDE Frameworks
BuildRequires:  extra-cmake-modules

# Qt
BuildRequires:  cmake(Qt6Core)

# Compression
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

%description
KDE Frameworks 6 Tier 1 addon with archive functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%{cmake_kf6}
%cmake_build

%install
%cmake_install
%find_lang_kf6 karchive6_qt

%files -f karchive6_qt.lang
%doc AUTHORS README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Archive.so.5.240.0
%{_kf6_libdir}/libKF6Archive.so.6

%files devel
%{_kf6_archdatadir}/mkspecs/modules/qt_KArchive.pri
%{_kf6_includedir}/KArchive/
%{_kf6_libdir}/cmake/KF6Archive/
%{_kf6_libdir}/libKF6Archive.so

%changelog
* Fri Sep 22 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.232718.8260e304c367377c16bf564cee43ee13479e66d5-1
- Initial Package
