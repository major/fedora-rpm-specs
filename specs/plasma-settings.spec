Name:           plasma-settings
Version:        24.02.0
Release:        4%{?dist}
# Automatically converted from old format: BSD and CC0 and GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and LGPLv2 and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-LGPLv2+
Summary:        Convergent Plasma Mobile settings application
Url:            https://invent.kde.org/plasma-mobile/plasma-settings
Source0:        https://download.kde.org/stable/plasma-settings/%{name}-%{version}.tar.xz

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiAddons)

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
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%check
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.mobile.plasmasettings.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.mobile.plasmasettings.svg
%{_kf6_bindir}/plasma-settings
%{_kf6_datadir}/applications/org.kde.mobile.plasmasettings.desktop

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.02.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 24.02.0-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.02.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 02 2024 Steve Cossette <farchord@gmail.com> - 24.02.0-1
- 24.02.0

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
