%global forgeurl https://github.com/KDE/choqok/
%global commit de3801bb52f4d4ee3ad3cbaa7f8704d0013881f3

Name:    choqok
Version: 1.7.0
Summary: KDE Micro-Blogging Client
License: GPLv3

%{forgemeta}

Release: 9%{?dist}
URL:     %{forgeurl}
Source0: %{forgesource}
Source1: %{name}.rpmlintrc

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets)

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Emoticons)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)

BuildRequires: cmake(Qca-qt5)
BuildRequires: qt5-qtnetworkauth-devel
BuildRequires: kf5-purpose-devel
BuildRequires: extra-cmake-modules

# optional features
BuildRequires: cmake(TelepathyQt5)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5WebKit)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
A Free/Open Source micro-blogging client for K Desktop Environment.
The name comes from an ancient Persian word, which means Sparrow!
Choqok currently supports:
Twitter, Friendica, Mastodon social, Pump.io network, GNU social
and Open Collaboration Services.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}

%package devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%prep
%{forgesetup}
%autosetup -p1 -n %{archivename}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.choqok.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.choqok.desktop

%files -f %{name}.lang
%doc README AUTHORS changelog
%{_kf5_bindir}/choqok
%{_kf5_qtplugindir}/choqok_*.so
%{_kf5_qtplugindir}/kcm_choqok_*.so
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/applications/org.kde.choqok.desktop
%{_kf5_metainfodir}/org.kde.choqok.appdata.xml
%{_datadir}/dbus-1/services/org.kde.choqok.service
%{_kf5_datadir}/config.kcfg/*.kcfg
%{_kf5_datadir}/kservices5/choqok_*.desktop
%{_kf5_datadir}/choqok/
%{_kf5_datadir}/knotifications5/choqok.notifyrc
%{_kf5_datadir}/kxmlgui5/*choqok*/
%{_kf5_datadir}/qlogging-categories5/choqok.categories
%{_kf5_plugindir}/parts/konqchoqokplugin.so
%{_kf5_plugindir}/purpose/choqokplugin.so
%{_kf5_datadir}/kservices5/ServiceMenus/choqok_*.desktop
%{_kf5_datadir}/kservices5/konqchoqok.desktop
%{_kf5_datadir}/kservicetypes5/choqok*.desktop

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libchoqok.so.*
%{_kf5_libdir}/libgnusocialapihelper.so.*
%{_kf5_libdir}/libtwitterapihelper.so.*

%files devel
%{_includedir}/choqok/
%{_kf5_libdir}/libchoqok.so
%{_kf5_datadir}/cmake/modules/FindChoqok.cmake
%{_kf5_libdir}/libgnusocialapihelper.so
%{_kf5_libdir}/libtwitterapihelper.so

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Gerald Cox <gbcox@fedoraproject.org> - 1.7.0-7
- Crash upon exit rhbz#1861171

* Sun Jun 19 2022 Gerald Cox <gbcox@fedoraproject.org> - 1.7.0-6
- Crash upon exit rhbz#1861171

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Gerald Cox <gbcox@fedoraproject.org> - 1.7.0-1
- Upstream release rhbz#1851805

* Mon Feb 17 2020 Than Ngo <than@redhat.com> - 1.6.0-12
- Fixed FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-8
- validate appdata (#1551266)
- backport upstream fixes

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-6
- use %%make_build,%%find_lang --with html, %%ldconfig_scriptlets
- use %%_kf5_metainfodir

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.0-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.6.0-1
- choqok-1.6.0 (#1403458), drop -devel subpkg for now

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Jan 24 2015 Rex Dieter <rdieter@fedoraproject.org> 1.5-1
- 1.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 04 2013 Rex Dieter <rdieter@fedoraproject.org> 1.4-1
- 1.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-0.4.20130711
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-0.3.20130711
- 1.3.1 20130711 snapshot

* Mon Jun 24 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-0.2.20130624
- 1.3.1 20130624git snapshot
- fix/prune %%changelog
- .spec cosmetics

* Fri Jun 21 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-0.1.20130621
- 1.3.1 20130621git snapshot (uses new twitter 1.1 api)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3-5
- rebuild (qjson)

* Fri Nov 23 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3-4
- rebuild (qjson)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3-2
- rebuild (attica)

* Sun Apr 22 2012 Sven Lankes <sven@lank.es> - 1.3-1
- new upstream release

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 31 2011 Rex Dieter <rdieter@fedoraproject.org> 1.2-3
- BR: pkgconfig(libattica)

* Sat Dec 31 2011 Sven Lankes <sven@lank.es> - 1.2-2
- rebuild for new libattica

* Wed Nov 23 2011 Sven Lankes <sven@lank.es> - 1.2-1
- new upstream release

* Tue Aug 09 2011 Sven Lankes <sven@lank.es> - 1.1-4
- fix bug on friendlist update (rhbz #729464)

* Tue Jul 26 2011 Rex Dieter <rdieter@fedoraproject.org> 1.1-3
- drop kwebkitpart support

* Tue Jun 21 2011 Rex Dieter <rdieter@fedoraproject.org> 1.1-2
- simplify %%files, use %%_kde4_appsdir macro
- use %%?_isa to tighten subpkg deps

* Sun Apr 03 2011 Sven Lankes <sven@lank.es> - 1.1-1
- new upstream release

* Sat Mar 26 2011 Sven Lankes <sven@lank.es> - 1.0-3
- apply upstream patch for rhbz #691237

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Sven Lankes <sven@lank.es> - 1.0-1
- new upstream release
