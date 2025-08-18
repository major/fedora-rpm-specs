%global base_name elisa

Name:       elisa-player
Version:    25.08.0
Release:    2%{?dist}
Summary:    Elisa music player

# Main program LGPLv3+
# Background image CC-BY-SA
# Automatically converted from old format: LGPLv3+ and CC-BY-SA - review is highly recommended.
License:    LGPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:        https://community.kde.org/Elisa

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/elisa-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6QQC2DesktopStyle)

Requires:       hicolor-icon-theme
Requires:       dbus-common
# QML module dependencies
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-qqc2-desktop-style%{?_isa}
Requires:       qt6-qt5compat%{?_isa}


%description
Elisa is a simple music player aiming to provide a nice experience for its
users.

%prep
%autosetup -n elisa-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang elisa --all-name --with-kde --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.elisa.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.elisa.appdata.xml

%files -f elisa.lang
%license COPYING
%{_kf6_bindir}/elisa
%{_kf6_datadir}/applications/org.kde.elisa.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.elisa.service
%{_kf6_datadir}/icons/hicolor/*/apps/elisa*
%{_kf6_datadir}/qlogging-categories6/elisa.categories
%{_kf6_metainfodir}/org.kde.elisa.appdata.xml
%{_kf6_libdir}/elisa/

%changelog
* Sat Aug 16 2025 Neal Gompa <ngompa@fedoraproject.org> - 25.08.0-2
- Undo autorelease/autochangelog conversion

* Sat Aug 09 2025 Steve Cossette <farchord@gmail.com> - 25.08.0-1
- 25.08.0

* Sat Jul 26 2025 Steve Cossette <farchord@gmail.com> - 25.07.90-1
- 25.07.90

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 14 2025 Steve Cossette <farchord@gmail.com> - 25.07.80-1
- 25.07.80

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 25.04.3-2
- 25.04.3

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 25.04.3-1
- 25.04.3

* Thu Jun 05 2025 Steve Cossette <farchord@gmail.com> - 25.04.2-1
- 25.04.2

* Wed May 14 2025 Steve Cossette <farchord@gmail.com> - 25.04.1-1
- 25.04.1

* Mon Apr 14 2025 Jan Grulich <jgrulich@redhat.com> - 25.04.0-2
- Rebuild (qt6)

* Sat Apr 12 2025 Steve Cossette <farchord@gmail.com> - 25.04.0-1
- 25.04.0

* Tue Mar 25 2025 Jan Grulich <jgrulich@redhat.com> - 25.03.80-2
- Rebuild (qt6)

* Sun Mar 23 2025 Steve Cossette <farchord@gmail.com> - 25.03.80-1
- 25.03.80

* Wed Mar 05 2025 Steve Cossette <farchord@gmail.com> - 24.12.3-1
- 24.12.3

* Fri Feb 21 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-2
- Rebuild for ppc64le enablement

* Thu Feb 06 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-1
- 24.12.2

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Wed Nov 20 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Wed Nov 06 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 24.08.2-2
- Rebuild (qt6)

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Thu Sep 26 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 24.08.0-2
- convert license to SPDX

* Fri Aug 23 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Mon Jun 24 2024 Timothée Ravier <tim@siosm.fr> - 24.05.1-2
- Remove dependency on Baloo

* Sat Jun 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 24.05.0-3
- Rebuild (qt6)

* Sun May 19 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-2
- fix: adjust BuildRequires and files section

* Sun May 19 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Sat Apr 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 24.02.1-3
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 24.02.1-2
- Rebuild (qt6)

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Fri Feb 23 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 24.01.95-2
- Rebuild (qt6)

* Thu Feb 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.85-1
- 24.01.85

* Sun Dec 03 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.80-1
- 24.01.80

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 24.01.75-2
- Rebuild (qt6)

* Thu Nov 23 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 24.01.75-1
- 24.01.75

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Tue Aug 29 2023 Sergi Jimenez <tripledes@fedoraproject.org> - 23.08.0-1
- 23.80.0

* Thu Aug 17 2023 Sergi Jimenez <tripledes@fedoraproject.org> - 23.07.90-1
- 23.07.90

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sun May 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 27 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- feat: 22.12.3

* Tue Jan 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.08.3-1
- 22.08.3

* Sat Oct 15 2022 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.08.2-1
- fix: update spec file

* Sat Oct 15 2022 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.08.1-2
- 22.08.2

* Thu Sep 08 2022 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Sun Aug 21 2022 Vasiliy Glazov <vascom2@gmail.com> - 22.08.0-2
- Add source file.

* Sun Aug 21 2022 Vasiliy Glazov <vascom2@gmail.com> - 22.08.0-1
- Update to 22.08.0.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Robert-André Mauchin <zebob.m@gmail.com> - 22.04.3-1
- Update to 22.04.3 - Close: rhbz#2104887

* Tue Jun 21 2022 Robert-André Mauchin <zebob.m@gmail.com> - 22.04.2-1
- Update to 22.04.2 Close: rhbz#2095219

* Sun May 15 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Tue Apr 26 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.04.0-1
- Update to 22.04.0

* Thu Mar 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.2-1
- Update to 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Mon Dec 13 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.0-1
- Update to 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Thu Oct 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Fri Sep 24 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.08.1-1
- Update to 21.08.1

* Mon Aug 23 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.08.0-1
- Update to 21.08.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.3-1
- Update to 21.04.3

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Mon Apr 19 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Fri Mar  5 08:47:17 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 20.12.3-1
- Update to 20.12.3
- Close: rhbz#1935395

* Mon Feb 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.2-1
- Update to 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 14:18:41 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 20.12.1-1
- Update to 20.12.1
- Close: rhbz#1913967

* Fri Dec 11 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.0-1
- Update to 20.12.0

* Sat Nov 07 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.3-1
- Update to 20.08.3

* Wed Oct 21 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.2-1
- Update to 20.08.2

* Wed Sep 23 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.1-1
- Update to 20.08.1

* Wed Aug 19 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.0-1
- Update to 20.08.0

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-4
- drop unused dep on qt5-qtbase-private-devel
- tighten qt5-qtquickcontrols runtime dep
- drop kde-filesystem dep (not needed, pulled in elsewhere)
- drop __cmake_in_source_build reference, enforced by %%cmake_kf5 now

* Tue Jul 28 16:05:29 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 20.04.3-3
- Fix FTBFS

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.3-1
- Update to 20.04.3

* Fri Jun 12 2020 Marie Loise Nolden <loise@kde.org> - 20.04.2-1
- Update to 20.04.2

* Sun May 24 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.1-1
- Update to 20.04.1

* Fri Apr 24 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.0-1
- Update to 20.04.0

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.03.90-2
- rebuild (qt5)

* Sat Apr 04 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.03.90-1
- Update to 20.03.90

* Thu Apr 02 19:31:23 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 20.03.80-1
- Update to 20.03.80 (#1800330)
- Update translations (#1820139)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 15:32:31 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 19.12.1-1
- Update to 19.12.1 (#1789485)
- Fix desktop file (#1790040)

* Sat Dec 14 05:41:09 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 19.12.0-1
- Release 19.12.0 (#1773785)

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 0.4.2-4
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.4.2-3
- rebuild (qt5)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 00:24:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.2-1
- Release 0.4.2 (#1722265)

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.4.0-2
- rebuild (qt5)

* Mon May 20 23:45:59 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Release 0.4.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-2
- Add qt5-qtquickcontrols

* Sun Sep 30 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Release 0.3.0

* Mon Jul 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Release 0.2.0

* Tue Apr 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.1-1
- Release 0.1.1

* Sat Apr 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1-1
- Release 0.1

* Fri Feb 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.81-0.2.alpha2
- Rebuild with missing translations

* Thu Feb 01 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.81-0.1.alpha2
- Release 0.0.81

* Fri Dec 08 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.80-0.1.alpha1
- First RPM release
