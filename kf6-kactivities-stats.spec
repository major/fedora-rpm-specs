%global gitdate 20231007.105021
%global cmakever 5.240.0
%global commit0 eae8543498e3fe988903c0889ee2fcc193f0d779
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kactivities-stats

Name:    kf6-%{framework}
Summary: A KDE Frameworks 6 Tier 3 library for accessing the usage data collected by the activities system
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}

License: CC0-1.0, GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Activities)
BuildRequires:  cmake(KF6Config)
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig

BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtbase-devel

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
%description devel
%{summary}.


%prep
%autosetup -n %{framework}-%{commit0} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc MAINTAINER README.developers TODO
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6ActivitiesStats.so.*

%files devel
%{_kf6_includedir}/KActivitiesStats/
%{_kf6_libdir}/cmake/KF6ActivitiesStats/
%{_kf6_libdir}/libKF6ActivitiesStats.so
%{_kf6_libdir}/pkgconfig/KF6ActivitiesStats.pc

%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231007.105021.eae8543-1
- Initial release
