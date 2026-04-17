Name:          kwin-zones
Version:       1.0.12
Release:       1%{?dist}
Summary:       Wayland ext-zones for KWin

License:       BSD-3-Clause AND GPL-2.0-or-later AND CC0-1.0 AND MIT
URL:           https://invent.kde.org/automotive/%{name}

Source:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(qt6waylandscannertools)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(libdrm)
BuildRequires: cmake(Qt6GuiPrivate)

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KWin)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-client)

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%doc README.md
%{_kf6_qtplugindir}/kwin/plugins/KWinZones.so
%{_kf6_qmldir}/org/kde/zones/

%changelog
* Wed Apr 15 2026 Steve Cossette <farchord@gmail.com> - 1.0.12-1
- 1.0.12

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Sep 2 2025 Steve Cossette <farchord@gmail.com> - 1.0.11-1
- 1.0.11
