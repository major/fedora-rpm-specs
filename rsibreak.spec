Name:           rsibreak
Summary:        A small utility which bothers you at certain intervals
Version:        0.12.15
Release:        5%{?dist}

License:        GPLv2+
URL:            https://userbase.kde.org/RSIBreak
%global majmin   %(echo %{version} | cut -d. -f1,2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/rsibreak/%{majmin}/rsibreak-%{version}.tar.xz

## upstream patches

BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib

%description
RSIBreak is a small utility which bothers you at certain intervals. The
interval and duration of two different timers can be configured. You can
use the breaks to stretch out or do the dishes. The aim of this utility
is to let you know when it is time to have a break from your computer.
This can help people to prevent Repetive Strain Injury.


%prep
%autosetup -p1


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang rsibreak --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.rsibreak.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.rsibreak.desktop


%if 0%{?rhel} && 0%{?rhel} < 8
%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi
%endif

%files -f rsibreak.lang
%license LICENSES/*
%doc AUTHORS ChangeLog NEWS TODO
%{_kf5_bindir}/rsibreak
%{_kf5_datadir}/applications/org.kde.rsibreak.desktop
%{_kf5_metainfodir}/org.kde.rsibreak.appdata.xml
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/knotifications5/rsibreak.notifyrc
%{_sysconfdir}/xdg/autostart/rsibreak_autostart.desktop
%{_datadir}/dbus-1/interfaces/org.rsibreak.rsiwidget.xml


%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Justin Zobel <justin@1707.io> - 0.12.15-1
- Update to 0.12.15

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 0.12.14-1
- Update to 0.12.14

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 02 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.12.13-4
- use new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.12.13-1
- 0.12.13
- renamed .desktop, +appdata

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.12.9-1
- 0.12.9, updated macros/scriptlets

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.12.8-1
- 0.12.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.12.7-2
- fix reported version

* Sat Jan 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.12.7-1
- 0.12.7 (#1534138)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.12.6-1
- rsibreak-0.12.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.12.5-1
- 0.12.5, update URL

* Tue May 31 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.12.3-1
- rsibreak-0.12.3 (kf5 port)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.11-12
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.11-7
- fix/update url (#896176)
- fix/update icon scriptlets
- .spec cosmetics

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Tom Albers <toma@kde.org> - 0.11-1
- New upstream version

* Thu Feb 25 2010 Roland Wolters <wolters.liste@gmx.net> - 0.10-3
- Fixed DSO errors

* Wed Jul 29 2009 Roland Wolters <wolters.liste@gmx.net> - 0.10-1
- Update to upstream version 0.10

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Artem S. Tashkinov <t.artem@mailcity.com> 0.9.0-10
- trunk fix for memory leak

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 06 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.9.0-6
- fix build against KDE 4.2 (patch from Kubuntu)

* Wed Jan 21 2009 Roland Wolters <wolters.liste@gmx.net> 0.9.0-5
- added doc/HTML dir

* Wed Jan 14 2009 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-3
- fix %%find_lang usage
- BR: kdelibs4-devel plasma-devel

* Fri Nov 28 2008 Roland Wolters <wolters.liste@gmx.net> 0.9.0-2
- update to version 0.9 featuring a KDE 4 version

* Fri Feb 22 2008 Roland Wolters <wolters.liste@gmx.net> 0.8.0-5
- rebuild after dbug bug has been fixed in devel branch

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.0-4
- Autorebuild for GCC 4.3

* Sat Dec 01 2007 Roland Wolters <wolters.liste@gmx.net> - 0.8.0-3
- changed build require from kdelibs-devel to kdelibs3-devel
- removed qt-devel dependency, kdelibs3-devel dep should be enough

* Thu Aug 16 2007 Roland Wolters <wolters.liste@gmx.net> - 0.8.0-2
- licence tag corrected

* Fri Oct 13 2006 Roland Wolters <wolters.liste@gmx.net> 0.8.0-1
- update to version 0.8

* Tue Jun 20 2006 Roland Wolters <wolters.liste@gmx.net> 0.7.1-3
- mass rebuild of devel branch

* Tue Jun 20 2006 Roland Wolters <wolters.liste@gmx.net> 0.7.1-1
- update to version 0.7.1
- e-mail-address of packager corrected

* Tue Apr 11 2006 Roland Wolters <rolandwolters@web.de> 0.6.0-1
- initial build
