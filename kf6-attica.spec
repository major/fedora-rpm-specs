%global		gitdate 20230829.232558
%global		cmakever 5.240.0
%global		commit0 4e09a15b47bc901af5c0839715aa6d7d3c331343
%global		shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global		framework attica

Name:		kf6-%{framework}
Version:	%{cmakever}^%{gitdate}.%{shortcommit0}
Release:	1%{?dist}
Summary:	KDE Frameworks Tier 1 Addon with Open Collaboration Services API
License:	CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL.txt
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{cmakever}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	reuse

Requires:	kf6-filesystem

%description
Attica is a Qt library that implements the Open Collaboration Services
API version 1.4.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
%{summary}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS ChangeLog README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Attica.so.*

%files devel
%{_kf6_libdir}/cmake/KF6Attica/
%{_kf6_includedir}/Attica/
%{_kf6_libdir}/libKF6Attica.so
%{_kf6_archdatadir}/mkspecs/modules/qt_Attica.pri
%{_kf6_libdir}/pkgconfig/KF6Attica.pc

%changelog
* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232558.4e09a15-1
- Initial Release
