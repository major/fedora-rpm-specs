%global gitdate 20231011.222045
%global cmakever 5.240.0
%global commit0 245b3ddae46a0b395334e65dc63ee3cc5370c4f4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework plasma5support

Name:    kf6-%{framework}
Summary: Support components for porting from KF5/Qt5 to KF6/Qt6
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 2%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{framework}

Source0:  https://invent.kde.org/plasma/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  pkgconfig(xkbcommon)
Requires:  kf6-filesystem

%description
%{summary}.

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
%find_lang lib%{framework}

%files -f lib%{framework}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Plasma5Support.so.*
%{_qt6_qmldir}/org/kde/plasma/plasma5support/
%{_datadir}/plasma5support/
%{_datadir}/qlogging-categories6/plasma5support.categories
%{_datadir}/qlogging-categories6/plasma5support.renamecategories

%files devel
%{_kf6_includedir}/Plasma5Support/
%{_kf6_libdir}/cmake/KF6Plasma5Support/
%{_kf6_libdir}/libKF6Plasma5Support.so
%{_kf6_includedir}/plasma5support/
%{_kf6_includedir}/plasma5support_version.h

%changelog
* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231011.222045.245b3dd-2
- Rebuild (qt6)

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.222045.245b3dd-1
- Initial release
