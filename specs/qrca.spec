%global gitcommit da129ccadc519317051cfbf98acd02b1befa42a6
%global gitdate 20241206.203647
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:          qrca
Version:       0.1~%{gitdate}.%{shortcommit}
Release:       2%{?dist}
License:       CC0-1.0 AND BSD-3-Clause AND BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later
Summary:       QR code scanner for KDE Plasma
URL:           https://apps.kde.org/%{name}/

Source0:       https://invent.kde.org/utilities/%{name}/-/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz

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
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6NetworkManagerQt)

# Qml Imports
Requires: qt6qml(org.kde.config)
Requires: qt6qml(org.kde.kirigami)
Requires: qt6qml(org.kde.kirigamiaddons.formcard)
Requires: qt6qml(org.kde.prison)
Requires: qt6qml(org.kde.purpose)

%description
Qrca is a simple application for Plasma Desktop
and Plasma Mobile that lets you scan many barcode
formats and create your own QR code images.

%prep
%autosetup -p1 -n %{name}-%{gitcommit}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.qrca.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/qrca
%{_kf6_datadir}/applications/org.kde.qrca.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.qrca.svg
%{_kf6_metainfodir}/org.kde.qrca.appdata.xml

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~20241206.203647.da129cc-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Steve Cossette <farchord@gmail.com> - 0.1~20241206.203647.da129cc-1
- Initial Release
