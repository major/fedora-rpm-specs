Name:           plasma-mobile
Version:        5.27.80
Release:        1%{?dist}
License:        CC0 and GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and LGPLv2+ and LGPLv2.1 and LGPLv2.1+ and LGPLv3 and LGPLv3 and MIT
Summary:        General UI components for Plasma Phone including shell, containment and applets
Url:            https://invent.kde.org/plasma/plasma-mobile
Source:         https://download.kde.org/%{stable_kf6}/plasma/%{version}/plasma-mobile-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kwin-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

BuildRequires: cmake(KF6Activities)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6ModemManagerQt)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6People)
BuildRequires: cmake(KF6Plasma)
BuildRequires: cmake(KF6PlasmaQuick)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Wayland)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Screen)
BuildRequires: cmake(KPipeWire)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Sensors)
BuildRequires: cmake(libkworkspace)
BuildRequires: libepoxy-devel
BuildRequires: wayland-devel

Requires: kf6-bluez-qt
Requires: kf6-kactivities
Requires: kf6-kdeclarative
Requires: kf6-kirigami2
Requires: kpipewire
# Plasma Mobile uses kscreen to automatically set a logical scaling factor based on hardware
Requires: kscreen
Requires: kwin
Requires: plasma-milou
Requires: plasma-nano
Requires: plasma-nm
Requires: plasma-pa
Requires: plasma-workspace >= %{version}
Requires: qqc2-breeze-style
Requires: qt6-qtwayland

# This package now integrates what was plasma-nm-mobile
Obsoletes: plasma-nm-mobile < 5.27.81


%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang plasma_applet_org.kde.phone.homescreen --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml ||:
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_{cellular_network,mobile_hotspot,mobile_info,mobile_onscreenkeyboard,mobile_power,mobile_time,mobile_wifi}.desktop

%files -f plasma_applet_org.kde.phone.homescreen.lang
%license LICENSES/*

%{_kf6_bindir}/startplasmamobile
%{_kf6_bindir}/plasma-mobile-envmanager
%{_kf6_bindir}/plasma-mobile-initial-start
%{_kf6_datadir}/plasma/quicksettings
%{_kf6_datadir}/plasma/shells/org.kde.plasma.phoneshell
%{_kf6_datadir}/wayland-sessions/plasma-mobile.desktop

#%{_kf6_metainfodir}/org.kde.plasma.phone*
%{_kf6_metainfodir}/org.kde.plasma.*
%{_kf6_metainfodir}/org.kde.breeze.*
%{_kf6_datadir}/plasma/look-and-feel/org.kde.breeze.mobile
%{_kf6_datadir}/plasma/mobileinitialstart
%{_kf6_datadir}/applications/*.desktop
%{_kf6_datadir}/dbus-1/interfaces/org.kde.plasmashell.Mobile.xml
%{_kf6_datadir}/knotifications6/plasma_mobile_quicksetting*.notifyrc
%{_kf6_datadir}/kwin/effects/mobiletaskswitcher
%{_kf6_datadir}/kwin/scripts/convergentwindows/contents/ui/main.qml
%{_kf6_datadir}/kwin/scripts/convergentwindows/metadata.json
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.mobile.panel
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.mobile.taskpanel
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon

%{_kf6_qmldir}/org/kde/plasma/mm/*
%{_kf6_qmldir}/org/kde/plasma/private/mobileshell
%{_kf6_qmldir}/org/kde/plasma/quicksetting
%{_kf6_qmldir}/org/kde/plasma/mobileinitialstart
%{_kf6_qmldir}/org/kde/private/mobile

%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_mobileshell.so
%{_kf6_qtplugindir}/plasma/applets/*.so
%{_kf6_qtplugindir}/kf6/kded/kded_plasma_mobile_start.so
%{_kf6_qtplugindir}/kwin/effects/plugins/mobiletaskswitcher.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_mobile_*.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_cellular_network.so

%changelog
* Fri Nov 24 2023 Steve Cossette <farchord@gmail.com> - 5.27.80-1
- 5.27.80

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
