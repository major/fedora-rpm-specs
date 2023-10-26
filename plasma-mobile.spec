Name:           plasma-mobile
Version:        5.27.9
Release:        1%{?dist}
License:        CC0 and GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and LGPLv2+ and LGPLv2.1 and LGPLv2.1+ and LGPLv3 and LGPLv3 and MIT
Summary:        General UI components for Plasma Phone including shell, containment and applets
Url:            https://invent.kde.org/plasma/plasma-mobile
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source:         https://download.kde.org/%{stable}/plasma/%{version}/plasma-mobile-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kwin-devel
BuildRequires: qt5-qtdeclarative-devel

BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Auth)
BuildRequires: cmake(KF5Bookmarks)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5KirigamiAddons)
BuildRequires: cmake(KF5ModemManagerQt)
BuildRequires: cmake(KF5NetworkManagerQt)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Package)
BuildRequires: cmake(KF5People)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5PlasmaQuick)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KPipeWire)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(libkworkspace)

Requires: kf5-bluez-qt
Requires: kf5-kactivities
Requires: kf5-kdeclarative
Requires: kf5-kirigami2
Requires: kpipewire
# Plasma Mobile uses kscreen to automatically set a logical scaling factor based on hardware
Requires: kscreen
Requires: kwin
Requires: plasma-milou
Requires: plasma-nano
Requires: plasma-nm
Requires: plasma-nm-mobile
Requires: plasma-pa
Requires: plasma-workspace >= %{version}
Requires: qqc2-breeze-style
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtquickcontrols
Requires: qt5-qtquickcontrols2
Requires: qt5-qtwayland

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang plasma_applet_org.kde.phone.homescreen --all-name

%files -f plasma_applet_org.kde.phone.homescreen.lang
%license LICENSES/*

%{_kf5_bindir}/startplasmamobile
%{_kf5_datadir}/knotifications5/plasma_phone_components.notifyrc
%{_kf5_datadir}/kpackage/kcms/kcm_mobileshell
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.*.desktop
%{_kf5_datadir}/applications/kcm_mobileshell.desktop
%{_kf5_datadir}/plasma/look-and-feel/org.kde.plasma.phone
%{_kf5_datadir}/plasma/plasmoids/org.kde.phone.*
%{_kf5_datadir}/plasma/quicksettings
%{_kf5_datadir}/plasma/shells/org.kde.plasma.phoneshell
%{_kf5_datadir}/wayland-sessions/plasma-mobile.desktop

%{_kf5_metainfodir}/org.kde.plasma.phone*
%{_kf5_metainfodir}/org.kde.plasma.quicksetting.*
%{_kf5_metainfodir}/org.kde.phone.*

%{_kf5_qmldir}/org/kde/plasma/mm/*
%{_kf5_qmldir}/org/kde/plasma/private/mobileshell
%{_kf5_qmldir}/org/kde/plasma/quicksetting

%{_kf5_qtplugindir}/plasma/kcms/systemsettings/kcm_mobileshell.so
%{_kf5_qtplugindir}/plasma/applets/*.so

%changelog
* Tue Oct 24 2023 Steve Cossette <farchord@gmail.com> - 5.27.9-1
- 5.27.9

* Tue Sep 12 2023 justin.zobel@gmail.com - 5.27.8-1
- 5.27.8

* Tue Aug 01 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.7-1
- 5.27.7

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.6-1
- 5.27.6

* Tue May 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.5-1
- 5.27.5

* Tue Apr 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.4-1
- 5.27.4

* Tue Mar 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.3-1
- 5.27.3

* Tue Feb 28 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-1
- 5.27.2

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.1-1
- 5.27.1

* Thu Feb 09 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 19 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- 5.26.90

* Sat Jan 07 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.5-1
- 5.26.5

* Tue Nov 29 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.4-1
- 5.26.4

* Wed Nov 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.3-1
- 5.26.3

* Wed Oct 26 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.2-1
- 5.26.2

* Tue Oct 18 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.1-1
- 5.26.1

* Thu Oct 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.0-1
- 5.26.0

* Sat Sep 17 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.90-1
- 5.25.90

* Wed Sep 07 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.5-1
- 5.25.5

* Sat Mar 19 2022 Justin Zobel <justin@1707.io> - 5.24.3
- Update to 5.24.3

* Fri Feb 18 2022 Justin Zobel <justin@1707.io> - 5.24.1
- Initial version of package
