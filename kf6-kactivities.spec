%global gitdate 20231009.214418
%global cmakever 5.240.0
%global commit0 330a3e248842caa50a77c19d6a6821ce0b4321b9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kactivities

Name:    kf6-%{framework}
Summary: A KDE Frameworks 6 Tier 3 to organize user work into separate activities
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:  https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(xkbcommon)
Requires:  kf6-filesystem

%description
A KDE Frameworks 6 Tier 3 API for using and interacting with Activities as a
consumer, application adding information to them or as an activity manager.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
%{summary}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kactivities-cli6
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Activities.so.*
%{_kf6_qmldir}/org/kde/activities/

%files devel
%{_kf6_includedir}/KActivities/
%{_kf6_libdir}/cmake/KF6Activities/
%{_kf6_libdir}/libKF6Activities.so
%{_kf6_libdir}/pkgconfig/KF6Activities.pc


%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231009.214418.330a3e2-1
- Initial release
