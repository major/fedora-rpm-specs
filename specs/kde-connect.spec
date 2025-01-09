%global base_name kdeconnect-kde

Name:    kde-connect
Version: 24.12.1
Release: 1%{?dist}
License: GPL-2.0-or-later
Summary: KDE Connect client for communication with smartphones

Url:     https://community.kde.org/KDEConnect
	
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
	
 
## upstream patches (lookaside cache)

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  firewalld-filesystem
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(openssl)

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6ModemManagerQt)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6Crash)

BuildRequires:  cmake(Qt6Bluetooth)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Core5Compat)
# wayland/clipboard deps
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  wayland-protocols-devel
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(Qca-qt6)

BuildRequires:  cmake(KF6PulseAudioQt)

BuildRequires:  libXtst-devel
BuildRequires:  pkgconfig(libfakekey)

Obsoletes: kde-connect-kde4-ioslave < %{version}-%{release}
Obsoletes: kde-connect-kde4-libs < %{version}-%{release}

# upstream name
Provides:       kdeconnect-kde = %{version}-%{release}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kdeconnectd = %{version}-%{release}

Requires:       fuse-sshfs
Requires:       qca-qt6-ossl%{?_isa}
# /usr/bin/plasmawindowed (make optional at least until this is split out for bug #1286431)
#Recommends:     plasma-workspace
# /usr/bin/kcmshell5
Requires:       kde-cli-tools
# /usr/bin/kdeconnect-app
Requires:       kf6-kirigami2%{?_isa}
Requires:       kf6-kirigami2-addons
# Required for contact synchronization with kde connect
Recommends:     kf6-kpeople

%description
KDE Connect adds communication between KDE and your smartphone.

Currently, you can pair with your Android devices over Wifi using the
KDE Connect 1.0 app from Albert Vaka which you can obtain via Google Play, F-Droid
or the project website.

%package -n kdeconnectd
Summary: KDE Connect service
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description -n kdeconnectd
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
# I think we may want to drop this, forces kdeconnectd to pull in main pkg indirectly -- rex
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package nautilus
Summary: KDEConnect extention for nautilus
Requires: kdeconnectd = %{version}-%{release}
Requires: nautilus-python
Supplements: (kdeconnectd and nautilus)
%description nautilus
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html

# https://bugzilla.redhat.com/show_bug.cgi?id=1296523
desktop-file-edit --remove-key=OnlyShowIn %{buildroot}%{_sysconfdir}/xdg/autostart/org.kde.kdeconnect.daemon.desktop
	
## unpackaged files
# this is a static version of the shared lib dropped in the beta
rm -fv %{buildroot}%{_kf6_libdir}/libkdeconnectinterfaces.a

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kdeconnect.appdata.xml ||:
for i in %{buildroot}%{_kf6_datadir}/applications/org.kde.kdeconnect*.desktop ; do
desktop-file-validate $i
done


%files -f %{name}.lang
%dir %{_kf6_datadir}/kdeconnect/
%license LICENSES/*
%{_datadir}/Thunar/
%{_datadir}/contractor/
%{_datadir}/deepin/
%{_datadir}/zsh/
%{_kf6_datadir}/applications/org.kde.kdeconnect*.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/kdeconnect*
%{_kf6_datadir}/icons/hicolor/*/status/*
%{_kf6_bindir}/kdeconnect-*
%{_kf6_datadir}/kdeconnect/kdeconnect_*.qml
%{_kf6_datadir}/knotifications6/*
%{_kf6_datadir}/plasma/plasmoids/org.kde.kdeconnect/
%{_kf6_datadir}/qlogging-categories6/kdeconnect*
%{_kf6_datadir}/applications/kcm_kdeconnect.desktop
%{_kf6_metainfodir}/org.kde.kdeconnect.appdata.xml
%{_kf6_metainfodir}/org.kde.kdeconnect.metainfo.xml
%{_kf6_plugindir}/kfileitemaction/kdeconnectfileitemaction.so
%{_kf6_plugindir}/kio/kdeconnect.so
%{_qt6_archdatadir}/qml/org/kde/kdeconnect/
%{_qt6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kdeconnect.so

%files -n kdeconnectd
%{_sysconfdir}/xdg/autostart/org.kde.kdeconnect.daemon.desktop
%{_datadir}/applications/org.kde.kdeconnect.daemon.desktop
%{_kf6_bindir}/kdeconnectd
%{_datadir}/dbus-1/services/org.kde.kdeconnect.service

%ldconfig_scriptlets libs

%files libs
%{_kf6_libdir}/libkdeconnectpluginkcm.so.*
%{_kf6_libdir}/libkdeconnectcore.so.*
%{_qt6_plugindir}/kdeconnect/

%files nautilus
%{_datadir}/nautilus-python/extensions/kdeconnect-share.py*


%changelog
* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 24.08.2-2
- Rebuild (qt6)

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Sun May 26 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-3
- Rebuild (pulseaudio-qt)

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 24.05.0-2
- Rebuild (qt6)

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 24.02.1-2
- Rebuild (qt6)

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 24.01.95-2
- Rebuild (qt6)

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 30 2023 Marie Loise Nolden <loise@kde.org> - 24.01.85-1
- 24.01.85

* Thu Nov 23 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-2
- Rebuild for new pulseaudio-qt version

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Tue Jan 24 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.1-3
- Add upstream patch

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Thu Nov 03 2022 Than Ngo <than@redhat.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 22.04.3-2
- Rebuild (qt5)

* Thu Jul 07 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 22.04.1-3
- Rebuild (qt5)

* Sun May 15 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Fri Mar 25 2022 Jan Grulich <jgrulich@redhat.com> - 21.12.3-2
- Rebuild (qt5)

* Thu Mar 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Tue Feb 15 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 21.12.2-2
- rebuild (pulseaudio-qt)

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Mon Dec 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.12.0-1
- 21.12.0

* Fri Nov 05 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-2
- rebuild (pulseaudio-qt)

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Thu Oct 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Mon Apr 19 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 15:17:14 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Wed Oct 14 14:46:50 CDT 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.2-1
- 20.08.2

* Wed Oct 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-2
- pull in upstream fixes
- .spec cleanup

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Tue Sep 08 2020 Troy Dawson <tdawson@redhat.com> - 20.08.0-2
- Requires: kf5-kirigami2 (#1877110)

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Thu Apr 23 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0, part of release-service now
- add .desktop/appstream validation (permissive for now)

* Mon Mar 30 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.4-2
- f31+ firewalld already supports kdeconnect

* Sun Mar 01 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.4-1
- 1.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jul 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.3.5-1
- 1.3.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.3.4-1
- 1.3.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3.3-1
- 1.3.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3.1-1
- 1.3.1

* Mon Apr 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-1
- 1.3.0
- -nautilus subpkg (extention for nautilus)

* Sun Mar 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.2.1-3
- use %%make_build %%ldconfig_scriptlets
- BR: gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.2.1-1
- 1.2.1, update url

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org>
- Remove obsolete scriptlets

* Sat Oct 07 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.2-2
- fix typo in Obsoletes

* Fri Oct 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.2-1
- 1.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Rex Dieter <rdieter@math.unl.edu> - 1.0.3-1
- kdeconnect-1.0.3 (#1408570), drop kde4 (compat) kioslave 

* Wed Oct 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-2
- fix _with_kde4 conditional

* Wed Oct 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-1.1
- -kde4-libs: inflate soname to avoid collisions (#1374869)
- fix Obsoletes

* Wed Sep 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-1
- 1.0.1

* Thu Sep 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1.0-2
- update URL (#1325177)

* Sun Aug 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0-1
- kde-connect-1.0

* Sun Jun 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9-7
- prep git snapshot (for 1.0 compatibility), but don't use yet
- kdeconnectd subpkg (#1324214)
- kdeconnectd does not autostart on MATE (#1296523)

* Fri Feb 19 2016 Rex Dieter <rdieter@fedoraproject.org> 0.9-6
- drop kde4 support (f24+)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Rex Dieter <rdieter@fedoraproject.org> 0.9-4
- kde-connect-0.9g

* Tue Dec 01 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9-3
- make plasma-workspace a soft dependency (#1286431)

* Thu Nov 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9-2
- respin kde-connect-0.9f, includes translations

* Mon Nov 16 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9-1
- kde-connect-0.9 (missing translations?)

* Tue Nov 10 2015 Rex Dieter <rdieter@fedoraproject.org> 0.8-10
- Requires: plasma-workspace kde-cli-tools (#1280078)

* Wed Sep 23 2015 Rex Dieter <rdieter@fedoraproject.org> 0.8-9
- include kde-connect firewalld service (#1115547)

* Thu Aug 27 2015 Helio Chissini de Castro <helio@kde.org> - 0.8-8
- Added buildreq for specific qca version that has proper headers

* Wed Aug 26 2015 Rex Dieter <rdieter@fedoraproject.org> - 0.8-7
- fresh snapshot, use releaseme to include translations
- tighten subpkg deps
- .spec cosmetics

* Fri Aug 07 2015 Helio Chissini de Castro <helio@kde.org> - 0.8-6
- Added missing requires, qca-qt5-ossl. Thanks to Stefano Cavallari <spiky.kiwi@gmail.com>

* Wed Aug 05 2015 Helio Chissini de Castro <helio@kde.org> - 0.8-5
- Update the KF5 snapshot.
- Added b revision for 0.8 KDE 4
- Added requires for fuse-ssh ( thanks to Sudhir Khanger )

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Helio Chissini de Castro <helio@kde.org> - 0.8.3
- Added some missing buildrequires for rawhide

* Mon Apr 20 2015 Helio Chissini de Castro <helio@kde.org> - 0.8-2
- KDE Connect KF5 snapshot based on 0.8 and kioslave for KDE 4

* Sun Feb 22 2015 Rex Dieter <rdieter@fedoraproject.org> 0.8-1
- KDE Connect 0.8 available (#1195011)
- use %%{?_kde_runtime_requires} (instead of %%_kf5_version macro)

* Thu Oct 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.7.3-1
- kde-connect-0.7.3
- BR: libfakekey-devel (and switch other BR's to pkgconfig style)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 06 2014 Rex Dieter <rdieter@fedoraproject.org> 0.7.2-1
- kde-connect-0.7.2 (#1116448)

* Sun Jun 29 2014 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-1
- 0.7.1

* Sat Jun 28 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.7-1
- kde-connect-0.7 (#1114196)
- Requires: fuse-sshfs (#1114197)
- Requires: qca-ossl
- -libs, -devel subpkgs

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.3.20140305git52901898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Martin Briza <mbriza@redhat.com> - 0.6-0.2.20140305git52901898
- Include the translations too

* Wed Mar 05 2014 Martin Briza <mbriza@redhat.com> - 0.6-0.1.20140305git52901898
- Updated to the latest upstream git to match the mobile app release

* Mon Feb 24 2014 Martin Briza <mbriza@redhat.com> - 0.5-1
- New release

* Thu Jan 02 2014 Martin Briza <mbriza@redhat.com> - 0.4.2-1
- Initial package
