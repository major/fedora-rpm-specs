Name:           plasma-settings 
Version:        23.01.0
Release:        5%{?dist}
License:        BSD and CC0 and GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and LGPLv2 and LGPLv2+
Summary:        Convergent Plasma Mobile settings application
Url:            https://invent.kde.org/plasma-mobile/plasma-settings
Source0:        https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib


BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Solid)

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  pkgconfig(gobject-2.0)

Requires:       ((pulseaudio-module-gsettings and sound-theme-freedesktop) if pulseaudio)
Requires:       polkit-kde
Requires:       accountsservice

%description
Convergent settings application for Plasma Mobile.
Notice that Wi-Fi, mobile broadband and hotspot KConfig
modules are provided separately, by plasma-nm.

%prep
%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%check
desktop-file-validate %{buildroot}/%{_kf5_datadir}/applications/org.kde.mobile.plasmasettings.desktop

%files -f %{name}.lang
%doc README.md

%license LICENSES/*

%{_kf5_bindir}/plasma-settings

%{_kf5_datadir}/applications/org.kde.mobile.plasmasettings.desktop
%{_kf5_datadir}/kpackage/

%{_qt5_plugindir}/kcms/*.so
 
%changelog
* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 27 2022 Justin Zobel <justin@1707.io> - 22.04-1
- Update to 22.04

* Sat Feb 26 2022 Justin Zobel <justin@1707.io> - 22.02
- Verison bump to 22.02

* Sun Feb 6 2022 Justin <justin@1707.io> - 21.12-1
- Initial Inclusion
