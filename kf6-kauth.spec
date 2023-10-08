%global gitdate 20231003.060844
%global cmakever 5.240.0
%global commit0 0b37b029eaa4a32ae82da13d69ba2b7e07c1495a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global framework kauth

Name:    kf6-%{framework}
Version: %{cmakever}^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}
Summary: KDE Frameworks 6 module to perform actions as privileged user

# LGPL-2.0-or-later is also in the project's LICENSES, but is unused according to reuse.
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://invent.kde.org/frameworks/%{framework}/-/archive/%{commit0}/%{framework}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  polkit-qt6-1-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(KF6CoreAddons)

Requires:  kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kauth6_qt

%files -f kauth6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/dbus-1/system.d/org.kde.kf6auth.conf
%{_kf6_datadir}/kf6/kauth/
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6AuthCore.so.5*
%{_kf6_libdir}/libKF6AuthCore.so.6
%{_kf6_qtplugindir}/kf6/kauth/

%files devel
%{_kf6_includedir}/KAuth/
%{_kf6_includedir}/KAuthCore/
%{_kf6_libdir}/cmake/KF6Auth/
%{_kf6_libdir}/libKF6AuthCore.so
%{_kf6_libexecdir}/kauth/

%changelog
* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.060844.0b37b02-1
- Initial Release
