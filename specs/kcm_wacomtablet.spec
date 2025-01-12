Name:    kcm_wacomtablet
Summary: KDE Control module for Wacom Graphictablets
Version: 6.2.90
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/system/wacomtablet
Source0: http://download.kde.org/%{stable_kf6}/plasma/%{version}/wacomtablet-%{version}.tar.xz

## upstream patches

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(Plasma5Support)
BuildRequires: cmake(Plasma) 
BuildRequires: kf6-rpm-macros

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtdeclarative-devel

BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(xcb-xinput)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xorg-wacom)
BuildRequires: pkgconfig(xrandr)

ExcludeArch: s390 s390x

Obsoletes: kcm-wacomtablet < 1.3.7-2
Provides:  kcm-wacomtablet = %{version}-%{release}

%description
This module implements a GUI for the Wacom Linux Drivers and extends it
with profile support to handle different button/pen layouts per profile.


%prep
%autosetup -n wacomtablet-%{version} 


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%doc AUTHORS
%license COPYING*
%{_datadir}/dbus-1/interfaces/org.kde.Wacom*.xml
%{_kf6_bindir}/kde_wacom_tabletfinder
%{_kf6_datadir}/applications/kcm_wacomtablet.desktop
%{_kf6_datadir}/applications/kde_wacom_tabletfinder.desktop
%{_kf6_datadir}/knotifications6/wacomtablet.notifyrc
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.wacomtablet/
%{_kf6_datadir}/plasma5support/services/wacomtablet.operations
%{_kf6_datadir}/wacomtablet/
%{_kf6_datadir}/qlogging-categories6/wacomtablet.categories
%{_kf6_metainfodir}/org.kde.plasma.wacomtablet.appdata.xml
%{_kf6_metainfodir}/org.kde.wacomtablet.metainfo.xml
%{_qt6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_wacomtablet.so
%{_kf6_plugindir}/kded/wacomtablet.so
%{_qt6_plugindir}/plasma5support/dataengine/plasma_engine_wacomtablet.so


%changelog
* Thu Jan 09 2025 Steve Cossette <farchord@gmail.com> - 6.2.90-1
- Beta 6.2.90

* Tue Dec 31 2024 Steve Cossette <farchord@gmail.com> - 6.2.5-1
- 6.2.5

* Tue Nov 26 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.4-1
- 6.2.4

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 6.2.3-1
- 6.2.3

* Tue Oct 22 2024 Steve Cossette <farchord@gmail.com> - 6.2.2-1
- 6.2.2

* Tue Oct 15 2024 Steve Cossette <farchord@gmail.com> - 6.2.1-1
- 6.2.1

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 6.2.0-2
- Rebuild (qt6)

* Thu Oct 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Thu Sep 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.90-1
- 6.1.90

* Tue Sep 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.5-1
- 6.1.5

* Fri Aug 09 2024 Steve Cossette <farchord@gmail.com> - 6.1.4-1
- 6.1.4

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 6.1.3-4
- convert license to SPDX

* Wed Jul 24 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.3-3
- rebuilt

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.3-1
- 6.1.3

* Wed Jul 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.2-1
- 6.1.2

* Tue Jun 25 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.1-1
- 6.1.1

* Thu Jun 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Fri May 24 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.90-1
- 6.0.90

* Wed May 22 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.5-1
- 6.0.5

* Tue Apr 16 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.4-1
- 6.0.4

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 6.0.3-2
- Rebuild (qt6)

* Tue Mar 26 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.3-1
- 6.0.3

* Tue Mar 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.2-1
- 6.0.2

* Wed Mar 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.1-1
- 6.0.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 5.93.0-2
- Rebuild (qt6)

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.93.0-1
- 5.93.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.92.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.92.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 28 2023 Marie Loise Nolden <loise@kde.org> - 5.92.0-1
- 5.92.0

* Thu Dec 28 2023 Marie Loise Nolden <loise@kde.org> - 5.91.0-1
- update to Plasma 6

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Peter Hutterer <peter.hutterer@redhat.com> - 3.2.0-6
- Rebuild for libwacom soname bump

* Sun Aug 29 2021 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-5
- .spec cosmetics (URL)
- backport upstream fixes

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-1
- 3.2.0, pull in Qt 5.15 fix

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.1.1-2
- update deps, fix/workaround FindX11.cmake issue

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Sun Sep 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-1
- 3.1.0 (#1624665)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.7.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.6.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.0-0.5.beta2
- 3.0.0-beta2 (aka 2.9.82), +translations

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.4.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-0.1.beta1
- 3.0.0-beta1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3.20150702gitg8ad842e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 02 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.0-2.20150702gitg8ad842e
- New snapshot.

* Thu Jul 02 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.1.0-1.20150702gitde80d02
- Update to latest kf5-port HEAD.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.3.20141123.ede16d1git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-0.2.20141123.ede16d1git
- 2.1.0 20141123 snapshot

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Oct 15 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-1
- 2.0.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Rex Dieter <rdieter@fedoraproject.org>  2.0.1-1
- kcm_wacomtablet-2.0.1 (#1114238)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Dan Horák <dan[at]danny.cz> - 1.3.7-3
- no wacom on s390(x)

* Thu Nov 29 2012 Mario Santagiuliana <fedora@marionline.it> - 1.3.7-2
- Rename to kcm_wacomtablet

* Mon Nov 19 2012 Mario Santagiuliana <fedora@marionline.it> - 1.3.7-1
- Initial build
- spec file created by rdieter
