%global gitdate 20231009.021332
%global cmakever 5.240.0
%global commit0 6933aaec278dd9cb61591b2a3b806416df5b36b8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    kglobalacceld
Summary: Daemon providing Global Keyboard Shortcut functionality
Version: 5.27.80^%{gitdate}.%{shortcommit0}
Release: 1%{?dist}

License: CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/plasma/%{name}

Source0:  https://invent.kde.org/plasma/%{name}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules >= %{cmakever}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-gui
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xtest)
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
%autosetup -n %{name}-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*.txt
%{_sysconfdir}/xdg/autostart/kglobalacceld.desktop
/usr/lib/systemd/user/plasma-kglobalaccel.service
%{_libdir}/libKGlobalAccelD.so.*
%{_qt6_plugindir}/org.kde.kglobalacceld.platforms/KGlobalAccelDXcb.so
%{_libexecdir}/kglobalacceld

%files devel
%{_includedir}/KGlobalAccelD/
%{_libdir}/cmake/KGlobalAccelD/

%changelog
* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.27.80^20231009.021332.6933aae-1
- Initial release
