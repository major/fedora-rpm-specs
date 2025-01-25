Name:           spacebar
Epoch:          1
Version:        6.2.91
Release:        1%{?dist}
License:        GPLv2+ and GPLv3 and GPLv2
Summary:        Messaging app for Plasma Mobile
Url:            https://invent.kde.org/plasma-mobile/spacebar
Source:         https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

ExclusiveArch:  %{java_arches}

BuildRequires:  abseil-cpp-devel
BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libphonenumber-devel
BuildRequires:  protobuf-devel

BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Sql)

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6ModemManagerQt)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(libphonenumber)

BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  cmake(FutureSQL6)

Requires:       hicolor-icon-theme
Requires:       kf6-kirigami
Requires:       telepathy-mission-control

%description
Spacebar is a telepathy-qt based SMS application that primarily targets Plasma Mobile.

%prep
%autosetup -n spacebar-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/{GPL-2.0-or-later,LicenseRef-KDE-Accepted-GPL}.txt
%{_kf6_bindir}/%{name}
%{_kf6_bindir}/spacebar-fakeserver
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_datadir}/knotifications6/%{name}.notifyrc

%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_libexecdir}/%{name}-daemon
%{_sysconfdir}/xdg/autostart/org.kde.%{name}.daemon.desktop

%changelog
* Thu Jan 23 2025 Steve Cossette <farchord@gmail.com> - 1:6.2.91-1
- 6.2.91

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.2.90-2
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

* Thu Oct 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:6.2.0-1
- 6.2.0

* Mon Sep 23 2024 Alessandro Astone <ales.astone@gmail.com> - 6.1.90-1
- 6.1.90
- Bump epoch

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.02.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 02 2024 Steve Cossette <farchord@gmail.com> - 24.02.0-1
- 24.02.0

* Sun Feb 04 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 23.01.0-8
- Rebuilt for abseil-cpp-20240116.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 23.01.0-6
- Remove spurious TelepathQt5 BuldRequires; fix FTBFS

* Wed Aug 30 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 23.01.0-5
- Rebuilt for abseil-cpp 20230802.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 17 2023 Sérgio Basto <sergio@serjux.com> - 23.01.0-3
- Rebuild for libphonenumber-8.13.x

* Mon Mar 27 2023 Rich Mattes <richmattes@gmail.com> - 23.01.0-2
- Rebuild for abseil-cpp-20230125.1

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Mon Sep 26 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.06-1
- initial version spacebar
