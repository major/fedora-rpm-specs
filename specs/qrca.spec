Name:          qrca
Version:       25.08.0
Release:       1%{?dist}
License:       CC0-1.0 AND BSD-3-Clause AND BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later
Summary:       QR code scanner for KDE Plasma
URL:           https://apps.kde.org/%{name}/

Source0:       https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Multimedia)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6DBusAddons)

# Qml Imports
Requires: qt6qml(org.kde.config)
Requires: qt6qml(org.kde.kirigami)
Requires: qt6qml(org.kde.kirigamiaddons.formcard)
Requires: qt6qml(org.kde.prison)

%description
Qrca is a simple application for Plasma Desktop
and Plasma Mobile that lets you scan many barcode
formats and create your own QR code images.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/qrca
%{_kf6_datadir}/applications/org.kde.qrca*.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.qrca.svg
%{_kf6_metainfodir}/org.kde.qrca.appdata.xml

%changelog
* Fri Aug 08 2025 Steve Cossette <farchord@gmail.com> - 25.08.0-1
- 25.08.0

* Fri Jul 25 2025 Steve Cossette <farchord@gmail.com> - 25.07.90-1
- 25.07.90

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 11 2025 Steve Cossette <farchord@gmail.com> - 25.07.80-1
- 25.07.80

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 25.04.3-1
- 25.04.3

* Wed Jun 04 2025 Steve Cossette <farchord@gmail.com> - 25.04.2-1
- 25.04.2

* Wed May 14 2025 Steve Cossette <farchord@gmail.com> - 25.04.1-1
- 25.04.1

* Sat Apr 12 2025 Steve Cossette <farchord@gmail.com> - 25.04.0-1
- 25.04.0

* Mon Mar 24 2025 Yaakov Selkowitz <yselkowi@redhat.com> - 25.03.80-1
- 25.03.80

* Fri Feb 21 2025 Steve Cossette <farchord@gmail.com> - 0.1~20241206.203647.da129cc-3
- Rebuild for ppc64le enablement

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~20241206.203647.da129cc-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Steve Cossette <farchord@gmail.com> - 0.1~20241206.203647.da129cc-1
- Initial Release
