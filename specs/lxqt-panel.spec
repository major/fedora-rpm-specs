Name:          lxqt-panel
Summary:       Main panel bar for LXQt desktop suite
Version:       2.1.4
Release:       1%{?dist}
License:       LGPL-2.1-or-later
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Xdg)
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(lxqt-globalkeys)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-damage)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libstatgrab)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(sysstat-qt6)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Solid)
BuildRequires: pkgconfig(dbusmenu-lxqt)
BuildRequires: desktop-file-utils
BuildRequires: lm_sensors-devel
BuildRequires: libXdamage-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: cmake(LayerShellQt)
BuildRequires: pkgconfig(xtst)
BuildRequires: xcb-util-image-devel
BuildRequires: lxqt-menu-data
BuildRequires: perl
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: wayland-devel
BuildRequires: qt6-qtbase-private-devel
Requires: lxqt-menu-data

Requires: xscreensaver-base
Requires: lxmenu-data

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-panel
Requires:       lxqt-panel
%description l10n
This package provides translations for the lxqt-panel package.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

for desktop in %{buildroot}/%{_datadir}/lxqt/lxqt-panel/*.desktop; do
    # Exclude category as been Service 
    desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt --add-only-show-in=X-LXQt ${desktop}
done
desktop-file-validate %{buildroot}/%{_datadir}/applications/lxqt-panel.desktop ||:

%find_lang lxqt-panel --with-qt
%find_lang cpuload --with-qt
%find_lang desktopswitch --with-qt
%find_lang directorymenu --with-qt
%find_lang mainmenu --with-qt
%find_lang mount --with-qt
%find_lang networkmonitor --with-qt
%find_lang quicklaunch --with-qt
%find_lang sensors --with-qt
%find_lang showdesktop --with-qt
%find_lang spacer --with-qt
%find_lang statusnotifier --with-qt
%find_lang sysstat --with-qt
%find_lang taskbar --with-qt
%find_lang volume --with-qt
%find_lang worldclock --with-qt

%files
%{_bindir}/lxqt-panel
%dir %{_libdir}/lxqt-panel
%{_libdir}/lxqt-panel/
%{_datadir}/lxqt
%{_mandir}/man1/lxqt-panel*
%{_sysconfdir}/xdg/autostart/lxqt-panel.desktop
%{_datadir}/applications/lxqt-panel.desktop

%files devel
%dir %{_includedir}/lxqt
%{_includedir}/lxqt/*

%files l10n -f lxqt-panel.lang -f cpuload.lang -f desktopswitch.lang -f directorymenu.lang  -f mainmenu.lang -f mount.lang -f networkmonitor.lang -f quicklaunch.lang -f sensors.lang -f showdesktop.lang -f spacer.lang -f statusnotifier.lang -f sysstat.lang -f taskbar.lang -f volume.lang -f worldclock.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-panel

%changelog
* Sat Jan 11 2025 Steve Cossette <farchord@gmail.com> - 2.1.4-1
- 2.1.4

* Sun Nov 24 2024 Steve Cossette <farchord@gmail.com> - 2.1.2-1
- 2.1.2

* Sun Nov 10 2024 Steve Cossette <farchord@gmail.com> - 2.1.1-1
- 2.1.1

* Tue Jul 16 2024 Steve Cossette <farchord@gmail.com> - 2.0.1-1
- 2.0.1

* Fri Apr 19 2024 Steve Cossette <farchord@gmail.com> - 2.0.0-1
- 2.0.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Zamir SUN <sztsian@gmail.com> - 1.4.0-1
- Update version to 1.4.0

* Fri Jul 28 2023 Zamir SUN <sztsian@gmail.com> - 1.3.0-1
- Update version to 1.3.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 12 2023 Tim Orling <ticotimo@gmail.com> - 1.2.0-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Zamir SUN <sztsian@gmail.com> - 1.2.0-1
- Update version to 1.2.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Zamir SUN <sztsian@gmail.com> - 1.1.0-1
- new version

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 25 2021 Zamir SUN <sztsian@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Sat Aug 07 2021 Zamir SUN <sztsian@gmail.com> - 0.17.1-1
- Update to 0.17.1

* Thu Aug 05 2021 Zamir SUN <sztsian@gmail.com> - 0.16.0-4
- Fix FTBFS
- Fixes RHBZ#1987695

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Mon Feb 17 2020 Than Ngo <than@redhat.com> - 0.14.1-4
- Added BR on libXdamage-devel

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-1
- Update to version 0.14.1

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-3
- Fix RHBZ 1624474 by adding requires lxmenu-data

* Sat Aug 04 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-2
- Bump to build against libsysstat-0.4.1-1

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-7
- Fix FTBFS: https://github.com/lxde/lxqt/issues/1251

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Thu Sep 29 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-2
- Fix some rpmlint issues

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream version 0.11.0

* Mon Sep 12 2016 Than Ngo <than@redhat.com> - 0.10.0-7
- requires on xscreensaver-base for the case only lxqt desktop is installed

* Tue May 24 2016 Than Ngo <than@redhat.com> 0.10.0-6
- add rhel support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-4
- Nor obsoletes razorqt anymore

* Sun Dec 13 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-3
- Disable kbindicator under epel

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-2
- Use new cmake_lxqt infra

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New upstream version

* Thu Sep 17 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-8
- Rebuild due new libstatgrab soname.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-5
- Rebuild (gcc5)

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-4
- Obsoletes typo

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Obsoletes razorqt-autosuspend and razorqt-appswitcher

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Obsoletes razorqt-panel as migrated to LXQt

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-1
- New upstream release 0.9.0

* Tue Feb 03 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Preparing 0.9.0 release

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-8
- Rebuild against new Qt 5.4.0

* Sat Dec 20 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-7
- Unify naming as discussed on Fedora IRC

* Tue Dec 16 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-6
- Wrong requires of xscreensaver-base. Should be handled but xdg-utils

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-5
- Fix missing item on  https://bugzilla.redhat.com/show_bug.cgi?id=1159873 - dir ownership

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-4
- New update to match requests on https://bugzilla.redhat.com/show_bug.cgi?id=1159873

* Tue Nov 04 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Update to match requests on review https://bugzilla.redhat.com/show_bug.cgi?id=1159873

* Mon Nov 03 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Update to review on Fedora bugzilla
- Added upstream patch #288 # https://github.com/lxde/lxde-qt/issues/288

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base
