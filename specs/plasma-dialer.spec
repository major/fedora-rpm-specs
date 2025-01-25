%global kde_name org.kde.plasma.dialer

Name:           plasma-dialer
Epoch:          1
Version:        6.2.91
Release:        1%{?dist}
License:        BSD and CC0 and GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and LGPLv2+ and LGPLv2.1 and LGPLv2.1+ and LGPLv3 and LGPLv3
Summary:        Convergent Plasma Mobile dialer application
Url:            https://invent.kde.org/plasma-mobile/plasma-dialer
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

## patches

ExclusiveArch:  %{java_arches}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6ModemManagerQt)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6KIO)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(libphonenumber)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  wayland-devel
BuildRequires:  callaudiod-devel
BuildRequires:  pkgconfig(protobuf)

%if 0%{?fedora}
BuildRequires:  reuse
%endif
BuildRequires:  wayland-devel



%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{epoch}:%{version}-%{release}

Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libphonenumber-devel
Requires:       protobuf-devel
Provides:       %{name}-static = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n plasma-dialer-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_datadir}/metainfo/%{kde_name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{kde_name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/plasma-dialer
%{_kf6_metainfodir}/%{kde_name}.appdata.xml
%{_kf6_datadir}/applications/%{kde_name}.desktop
%{_kf6_sysconfdir}/xdg/autostart/org.kde.modem.daemon.desktop
%{_kf6_sysconfdir}/xdg/autostart/org.kde.telephony.daemon.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/dialer.svg
%{_kf6_datadir}/knotifications6/plasma-dialer.notifyrc
%{_kf6_datadir}/dbus-1/interfaces/org.kde.telephony.*
%{_kf6_datadir}/dbus-1/services/org.kde.telephony.service
%{_kf6_datadir}/dbus-1/services/org.kde.modemdaemon.service
%{_kf6_qmldir}/org/kde/telephony
%{_libexecdir}/kde-telephony-daemon
%{_libexecdir}/modem-daemon

%files devel
%{_includedir}/KF6/kTelephonyMetaTypes
%{_kf6_libdir}/libktelephonymetatypes.a

%changelog
* Thu Jan 23 2025 Steve Cossette <farchord@gmail.com> - 1:6.2.91-1
- 6.2.91

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.2.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Steve Cossette <farchord@gmail.com> - 1:6.2.90-1
- Beta 6.2.90

* Tue Dec 31 2024 Steve Cossette <farchord@gmail.com> - 1:6.2.5-1
- 6.2.5

* Sat Dec 14 2024 Adam Williamson <awilliam@redhat.com> - 1:6.2.4-2
- Rebuild for new libphonenumber

* Tue Nov 26 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:6.2.4-1
- 6.2.4

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 1:6.2.3-1
- 6.2.3

* Tue Oct 22 2024 Steve Cossette <farchord@gmail.com> - 1:6.2.2-1
- 6.2.2

* Tue Oct 15 2024 Steve Cossette <farchord@gmail.com> - 1:6.2.1-1
- 6.2.1

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 1:6.2.0-2
- Rebuild (qt6)

* Thu Oct 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:6.2.0-1
- 6.2.0

* Mon Sep 23 2024 Alessandro Astone <ales.astone@gmail.com> - 6.1.90-1
- 6.1.90
- Bump epoch

* Sun Aug 25 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 24.08.0-2
- Rebuilt for abseil-cpp-20240722.0

* Thu Aug 15 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0 (+ Conversion to Qt6)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 23.01.0-9
- Rebuilt for abseil-cpp-20240116.0

* Sun Jan 28 2024 Alessandro Astone <ales.astone@gmail.com> - 23.01.0-8
- Remove phony and nonexistent cmake(KWinEffects) build requires

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

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
