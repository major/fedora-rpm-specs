%undefine __cmake_in_source_build

Name:             knemo
Version:          0.7.7
Release:          24.20170520git%{?dist}
Summary:          A KDE network monitoring tool
License:          GPLv2+
URL:              http://extragear.kde.org/apps/knemo/
# git clone -b frameworks git://anongit.kde.org/knemo.git
Source0:          knemo-20170520git.tar.xz
# Source0:          http://kde-apps.org/CONTENT/content-files/12956-%{name}-%{version}.tar.xz
Patch0:           knemo-FTBFS-qmap.patch
BuildRequires:    desktop-file-utils
BuildRequires:    extra-cmake-modules
BuildRequires:    gettext
BuildRequires:    libnl3-devel
BuildRequires:    cmake(KF5KCMUtils)
BuildRequires:    cmake(KF5KDELibs4Support)
BuildRequires:    cmake(KF5NotifyConfig)
BuildRequires:    cmake(KF5Notifications)
BuildRequires:    cmake(KF5GlobalAccel)
BuildRequires:    cmake(KF5Plasma)
BuildRequires:    cmake(KF5SysGuard)

%description
KNemo displays for every network interface an icon in the systray. Tooltips
and an info dialog provide further information about the interface. Passive
popups inform about interface changes. A traffic plotter is also integrated.
It polls the network interface status every second using the ifconfig, route
and iwconfig tools.

%prep
%setup -q -n knemo-20170520git
%patch0 -p1

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

#find_lang %{name}
#find_lang kcm_%{name}
#cat kcm_%{name}.lang >> %{name}.lang

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/%{name}.desktop



#files -f %{name}.lang
%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_kf5_bindir}/%{name}
%{_qt5_plugindir}/kcm_knemo.so
%{_kf5_sysconfdir}/xdg/autostart/knemo.desktop
%{_kf5_datadir}/%{name}
%{_kf5_datadir}/plasma/desktoptheme/*/icons/knemo.svgz
%{_kf5_datadir}/applications/%{name}.desktop
%{_kf5_datadir}/kservices5/kcm_knemo.desktop
%{_kf5_datadir}/knotifications5/knemo.notifyrc
%{_kf5_datadir}/kconf_update/knemo*
%{_kf5_datadir}/icons/hicolor/*/apps/%{name}*
%{_kf5_datadir}/icons/hicolor/*/status/%{name}*
%{_kf5_datadir}/icons/breeze-dark/status/panel/%{name}*
%{_kf5_datadir}/icons/breeze/status/panel/%{name}*
%{_kf5_datadir}/icons/oxygen/scalable/status/%{name}*

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-24.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-23.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-22.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-21.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-20.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-19.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-18.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-17.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 29 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.7.7-16.20170520git
- Drop wireless-tools, functionality superseeded by libnl3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-15.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Alexey Kurov <nucleo@fedoraproject.org> - 0.7.7-14.20170520git
- Rebuilt for libksysguard 5.19

* Mon Feb 17 2020 Than Ngo <than@redhat.com> - 0.7.7-13.20170520git
- Fixed FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-12.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-11.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-10.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-9.20170520git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Alexey Kurov <nucleo@fedoraproject.org> - 0.7.7-8.20170520git
- frameworks git 20170520 snapshot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.7-6
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Alexey Kurov <nucleo@fedoraproject.org> - 0.7.7-1
- KNemo 0.7.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 28 2013 Alexey Kurov <nucleo@fedoraproject.org> - 0.7.6-1
- KNemo 0.7.6
- switch to libnl3 (#1035831)
- spec file cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.7.3-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan  6 2012 Alexey Kurov <nucleo@fedoraproject.org> - 0.7.3-1
- KNemo 0.7.3

* Thu Mar 31 2011 Alexey Kurov <nucleo@fedoraproject.org> - 0.7.1-1
- KNemo 0.7.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.7.0-1
- KNemo 0.7.0

* Fri Sep  3 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.6.80-1
- KNemo 0.7.0 beta1
- Requires: kdelibs4

* Tue Jun 15 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.6.3-1
- update to 0.6.3

* Sat Apr 10 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.6.2-2
- disabled new KStatusNotifierItem for now (kde#226650)

* Fri Apr  9 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.6.2-1
- update to 0.6.2

* Mon Jan 18 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.6.1-2
- update to 0.6.1

* Fri Dec  4 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.6.0-1
- update to 0.6.0

* Thu Nov 19 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.5.80-2
- rebuild (qt-4.6.0-rc1, fc13+)

* Fri Nov  6 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.5.80-1
- update to 0.5.80 (0.6.0 beta1)
- drop xdg-utils references
- removed Requires net-tools wireless-tools

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  1 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.5.2-1
- Update to version 0.5.2
- Fixed spec License and URL fields

* Tue Mar 17 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.5.1-5
- Upstream update from git.mehercule.net

* Thu Mar  5 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.5.1-1
- Update to version 0.5.1

* Wed Feb 25 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.5.0-3
- Update to version 0.5.0 for KDE4

* Tue Apr 17 2007 Francois Aucamp <faucamp@csir.co.za> - 0.4.7-1
- Update to version 0.4.7
- Removed unnecessary desktop-file-install statements (KDE-specific desktop
  files)
- Removed desktop file patch - desktop file "Keywords" keys used internally
  by KDE
- Added "OnlyShowIn=KDE" to kcm desktop file
- Removed unnecessary BuildRequires: qt-devel desktop-file-utils
- Simplified %%post and %%postun scriplets
- Use RPM_BUILD_ROOT variable format consistently

* Wed Sep 13 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.3-2
- Rebuilt for FC6

* Sun Aug  6 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.3-1
- New upstream version

* Mon Jun 26 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.2-1
- Upstream update
- Fixes crashing when you click in panel icon (bz #196576)
- ifconfig and iwconfig are now in both Requires and
  BuildRequires (it checks while building too)

* Tue Jun 13 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.1-2
- ifconfig and iwconfig are now in Requires section instead
  of BuildRequires. They are runtime dependencies. Thanks to
  Kevin Kofler for pointing this.

* Mon Jun 12 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.1-1
- Upstream update

* Tue May 30 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.0-4
- Created BuildRequires for the ifconfig and iwconfig commands,
  as knemo utilizes it for monitoring.
- Removed addition of categories in desktop-file-install command

* Thu May 25 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.0-3
- Removed vendor option from desktop-file-install (no renaming)

* Sat May 20 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.0-2
- Installed .desktop files now use desktop-file-install

* Sat May 20 2006 Hugo Cisneiros <hugo@devin.com.br> 0.4.0-1
- Initial RPM release.
