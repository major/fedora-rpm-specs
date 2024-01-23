%global kde_name org.kde.phone.dialer

Name:           plasma-dialer
Version:        23.01.0
Release:        6%{?dist}
License:        BSD and CC0 and GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and LGPLv2+ and LGPLv2.1 and LGPLv2.1+ and LGPLv3 and LGPLv3
Summary:        Convergent Plasma Mobile dialer application
Url:            https://invent.kde.org/plasma-mobile/plasma-dialer
Source0:        https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz

ExclusiveArch:  %{java_arches}

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  abseil-cpp-devel

BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5People)
BuildRequires:  cmake(KF5PulseAudioQt) >= 1.3
BuildRequires:  cmake(KF5WindowSystem)

BuildRequires:  cmake(KWinEffects)
BuildRequires:  cmake(PlasmaWaylandProtocols)

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Feedback)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5WaylandClient)

BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpulse)

BuildRequires:  callaudiod-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  libmpris-qt5-devel
BuildRequires:  libphonenumber-devel
BuildRequires:  protobuf-devel
BuildRequires:  qt5-qtbase-private-devel
%if 0%{?fedora}
BuildRequires:  reuse
%endif
BuildRequires:  wayland-devel

Requires:       kf5-kcontacts
Requires:       kf5-kcoreaddons
Requires:       kf5-modemmanager-qt
Requires:       oxygen-sound-theme

Requires:       google-noto-sans-cjk-ttc-fonts
Requires:       qt5-qtfeedback

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libphonenumber-devel
Requires:       protobuf-devel
Requires:       cmake(KF5ModemManagerQt)
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n plasma-dialer-%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_datadir}/metainfo/%{kde_name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/%{kde_name}.desktop

%files -f %{name}.lang
%license LICENSES/*

%{_kf5_bindir}/plasmaphonedialer

%{_kf5_metainfodir}/%{kde_name}.appdata.xml
%{_kf5_datadir}/applications/%{kde_name}.desktop
%{_kf5_sysconfdir}/xdg/autostart/org.kde.modem.daemon.desktop
%{_kf5_sysconfdir}/xdg/autostart/org.kde.telephony.daemon.desktop
%{_kf5_datadir}/icons/hicolor/scalable/apps/dialer.svg
%{_kf5_datadir}/knotifications5/plasma_dialer.notifyrc

%{_kf5_datadir}/dbus-1/interfaces/org.kde.telephony.*
%{_kf5_datadir}/dbus-1/services/org.kde.telephony.service
%{_kf5_datadir}/dbus-1/services/org.kde.modemdaemon.service
%{_kf5_qmldir}/org/kde/telephony
%{_libexecdir}/kde-telephony-daemon
%{_libexecdir}/modem-daemon

%files devel
%{_includedir}/KF5/kTelephonyMetaTypes
%{_kf5_libdir}/libktelephonymetatypes.a

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 30 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 23.01.0-5
- Rebuilt for abseil-cpp 20230802.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 17 2023 Sérgio Basto <sergio@serjux.com> - 23.01.0-3
- Rebuild for libphonenumber-8.13.x

* Mon Mar 27 2023 Rich Mattes <richmattes@gmail.com> - 23.01.0-2
- Rebuild for abseil-cpp-20230125.1

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Mon Sep 26 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.06-1
- initial version plasma-dialer
