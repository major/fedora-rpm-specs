# define to allow khtml to remain the default
%ifarch ppc ppc64 s390 s390x
%global khtml 1
%endif

%if 0%{?rhel}
%global khtml 1
%endif

%global snap 20190110

Name:    kwebkitpart
Summary: A KPart based on QtWebKit
Version: 1.4.0
Release: 0.19.%{snap}%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://cgit.kde.org/kwebkitpart.git/
# use releaseme script (kdelibs4 branch) to generate
# with tweaks to CMakeLists.txt to properly handle translations
Source0: kwebkitpart-%{version}-%{snap}.tar.xz

## upstreamable patches

## upstream patches

BuildRequires: gettext

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5WebKit)
BuildRequires: cmake(KF5I18n)

BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt5PrintSupport)

Obsoletes: kwebkitpart-devel < 1.1
Obsoletes: webkitpart < 0.0.6
Provides:  webkitpart = %{version}-%{release}

%description
KWebKitPart is a web browser component for KDE (KPart)
based on (Qt)WebKit. You can use it for example for
browsing the web in Konqueror.


%prep
%autosetup


%if 0
# revert commit that gives kwebkitpart higher priority than khtml
# https://projects.kde.org/projects/extragear/base/kwebkitpart/repository/revisions/49ea6284cc46e8a24d04a564d4c8680ebd2b0f74
sed -i.InitialPreference \
  -e 's|^InitialPreference=.*|-InitialPreference=9|g' \
  src/kwebkitpart.desktop
%endif


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang kwebkitpart


%if 0%{?rhel} && 0%{?rhel} < 8
%post
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:

%posttrans
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null ||:
  gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null ||:
fi
%endif

%files -f kwebkitpart.lang
%doc README TODO
%license COPYING.LIB
%{_kf5_sysconfdir}/xdg/kwebkitpart.categories
%dir %{_kf5_plugindir}/parts/
%{_kf5_plugindir}/parts/kwebkitpart.so
%{_kf5_datadir}/icons/hicolor/*/apps/webkit.*
%{_kf5_datadir}/kservices5/kwebkitpart.desktop
%{_kf5_datadir}/kwebkitpart/
%{_kf5_datadir}/kxmlgui5/kwebkitpart/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.19.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.0-0.18.20190110
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.17.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.16.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.15.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.14.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.13.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.12.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.11.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.10.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.9.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.4.0-0.8.20190110
- minor cosmetics

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.7.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.6.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.5.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.4.20190110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.4.0-0.3.20190110
- 20190110 snapshot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.2.20180320
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.4.0-0.1.20180320
- kf5-based kwebkitpart-1.4.0 (#1474170)

* Tue Mar 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.3.4-13
- .spec cosmetics, update URL, use %%make_build %%license

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.4-6
- Rebuilt for GCC 5 C++11 ABI change

* Fri Nov 14 2014 Rex Dieter <rdieter@fedoraproject.org> 1.3.4-5
- CVE-2014-8600 Insufficient Input Validation (#1164293)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Rex Dieter <rdieter@fedoraproject.org> 1.3.4-3
- keep khtml default on rhel

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 1.3.4-2
- BR: kdelibs4-webkit-devel

* Thu Jun 12 2014 Rex Dieter <rdieter@fedoraproject.org> 1.3.4-1
- 1.3.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 29 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.3-2
- respin tarball

* Wed Dec 04 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.3-1
- 1.3.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Than Ngo <than@redhat.com> 1.3.2-3
- khtml engine default on s390(x) and ppc(64) 

* Fri May 17 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-2
- revert workaround for kde bug#313005

* Sat Mar 09 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-1
- 1.3.2

* Tue Jan 29 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-2
- Translations are not included in the kwebkitpart package (#905627)

* Thu Jan 03 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.1-1
- 1.3.1

* Thu Oct 04 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.0-1
- generate tarball from v1.3.0 tag
- include a few post v1.3.0 patches
- default web browsing KPart unexpectedly changed to WebKitPart (#862601)
- BR: pkgconfig(QtWebKit)
- .spec cosmetics

* Thu Jul 26 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3-0.1.20120726git
- 1.3 branch 20120726 snapshot

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.5.20120715
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Rex Dieter <rdieter@fedoraproject.org> 1.2-0.4.20120715
- 20120715 snapshot (master branch, 1.2 is broken atm)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.3.20111030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 30 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.2-0.2.20111030
- kwebkitpart 1.2 20111030 snapshot

* Thu Jul 21 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.2-0.1.20110720
- kwebkitpart 1.2 20110720 snapshot
- drop kwebkitpart-devel

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.9.6-2
- Rebuilt for gcc bug 634757

* Sun Jul 25 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.9.6-1
- kwebkitpart 0.9.6

* Sat May 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.0.5-0.4.svn1088283
- revert BR: qt4-webkit-devel, rebuild against newer kdelibs-devel that includes it

* Sat May 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.0.5-0.3.svn1088283
- BR: qt4-webkit-devel

* Wed Mar 24 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.5-0.2.svn1088283
- drop webkitkde package
- removed Requires: webkitkde from webkitpart

* Wed Feb 10 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.5-0.1.svn1088283
- update to kwebkitpart snapshot from kdereview

* Wed Feb 10 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.4-0.3.svn1079265
- build only for kdelibs >= 4.4.0

* Sun Jan 24 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.4-0.2.svn1079265
- svn 1079265. Fixed the library and header file names.

* Sat Jan 23 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.4-0.1.svn1078162
- svn 1078162

* Thu Dec  3 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.3-0.2.svn1057318
- svn 1057318

* Tue Nov 24 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.3-0.1.svn1049337
- version changed to 0.0.3 (kdewebkit moved to kdelibs 4.4)
- drop webkitkde-devel subpackage for KDE 4.4

* Wed Nov 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.0.2-0.2.20091109svn
- rebuild (qt-4.6.0-rc1, fc13+)

* Mon Nov  9 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.2-0.1.20091109svn
- version changed to 0.0.2 for new API

* Mon Nov  9 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.1-0.6.20091109svn
- removed kdelauncher from CMakeLists because it not installs

* Mon Nov  9 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.1-0.5.20091109svn
- snapshot 1046552 with new API

* Sun Sep 27 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.1-0.2.20090924svn
- webkitpart should owns kpartplugins in webkitpart apps dir

* Thu Sep 24 2009 Alexey Kurov <nucleo@fedoraproject.org> - 0.0.1-0.1.20090924svn
- Initial RPM release
