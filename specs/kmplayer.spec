%global branch 0.12

Name:    kmplayer
Summary: A simple front-end for MPlayer/FFMpeg/Phonon
Version: 0.12.0b
Release: 15%{?dist}
# The documentation is GFDL.
# The files under src/moz-sdk are MPLv1.1 or GPLv2+ or LGPLv2+
# except src/moz-sdk/npruntime.h is BSD.
# The other source files carry GPL and LGPL licenses
# For instance:
# src/kmplayer.h is GPLv2+
# src/kmplayer_asx.cpp is LGPLv2
# src/kmplayer_atom.h is LGPLv2+
# and each of the other source files carry one of the above 3 licenses. So
#License: GFDL and (MPLv1.1 or GPLv2+ or LGPLv2+) and BSD and GPLv2+ and LGPLv2 and LGPLv2+
# Automatically converted from old format: GFDL and GPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-GFDL AND GPL-2.0-or-later
URL:     https://kmplayer.kde.org
Source0: https://download.kde.org/stable/kmplayer/%{branch}/kmplayer-%{version}.tar.bz2

## upstream patches

BuildRequires: kf5-kdelibs4support-devel 
BuildRequires: kf5-kmediaplayer-devel
BuildRequires: desktop-file-utils
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: gettext
BuildRequires: extra-cmake-modules
BuildRequires: xcb-util-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: phonon-qt5-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-renderutil-devel
BuildRequires: libxcb-devel
BuildRequires: cmake-data
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: qt5-qtspeech-devel
BuildRequires: polkit-qt5-1-devel


%description
KMPlayer, a simple front-end for MPlayer/FFMpeg/Phonon.
It can play DVD/VCD movies, from file or URL and from a video device.
KMPlayer can embed inside Konqueror. Which means if you click
on a movie file, the movie is played inside Konqueror.


%prep
%setup -q -n %{name}-%{version}

#Set Phonon as default
sed -i  "s:Show Toolbar=true:Show Toolbar=true\nurlsource=phonon:g" src/kmplayerrc
#Fix building issue
sed -i 's:Q_PLUGIN_METADATA(IID "org.kde.KPluginFactory" FILE ""):Q_PLUGIN_METADATA(IID "org.kde.KPluginFactory" ""):g' src/kmplayer_part.h
#Fix desktop entry
sed -i "s:Exec=kmplayer -caption %c %i %U:Exec=kmplayer %U:g" src/kmplayer.desktop

%build
%{cmake}
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING* README TODO
%{_bindir}/*
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/qt5/plugins/kmplayerpart.so
%{_libdir}/libkdeinit5_kmplayer.so
%{_libdir}/libkmplayercommon.so
%{_sysconfdir}/xdg/kmplayerrc
%{_docdir}/HTML/*
%{_datadir}/%{name}/*
%{_datadir}/applications/kmplayer.desktop
%{_datadir}/kxmlgui5/%{name}/*
%{_datadir}/kservices5/*.desktop



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.12.0b-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 26 2023 Mosaab Alzoubi <moceap[AT]fedoraproject[DOT]org> - 0.12.0b-9 
- PR #1 BY Yaakov Selkowitz to FIX #2045770

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Mosaab Alzoubi <moceap[AT]hotmail[DOT]com> - 0.12.0b-1
- Update to 0.12.0b
- Clean up SPEC
- Remove patches
- Use sed for make Phonon default
- Use KF5 instead of KDE4
- Renew URLs

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3c-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3c-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3c-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3c-15
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3c-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3c-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3c-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3c-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3c-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Rex Dieter <rdieter@fedoraproject.org> 0.11.3c-9
- fix FTBFS wrt symbol visibility

* Wed Jun 03 2015 Rex Dieter <rdieter@fedoraproject.org> 0.11.3c-8
- update URL: (#1227976)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3c-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.11.3c-6
- Fix FTBFS on aarch64 (#1113337)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.3c-1
- kmplayer-0.11.3c
- Drop all upstreamed patches

* Wed Feb 15 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.3b-2
- gcc-4.7 build fix

* Sat Feb 11 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.3b-1
- kmplayer-0.11.3b

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 25 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.3a-1
- kmplayer-0.11.3a

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.11.2c-6
- Rebuild for new libpng

* Mon Apr 25 2011 Rex Dieter <rdieter@fedoraproject.org> 0.11.2c-5
- s/uri/x-scheme-handler/ (#587573)

* Mon Mar 21 2011 Rex Dieter <rdieter@fedoraproject.org> 0.11.2c-4
- drop executable_script.patch (not needed, kde#269075)

* Mon Mar 21 2011 Rex Dieter <rdieter@fedoraproject.org> 0.11.2c-3
- use %%find_lang ... --with-kde
- broken or deprecated mime type (#587573)
- (upstreamable) fix for executable script

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 05 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.2c-1
- kmplayer-0.11.2c

* Tue May 11 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.2b-1
- kmplayer-0.11.2b

* Tue Mar 23 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.2a-1
- kmplayer-0.11.2a

* Fri Mar 05 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.2-1
- kmplayer-0.11.2
- Drop upstreamed dso linking patch

* Sat Feb 13 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.1b-4
- Fix DSO linking RHBZ#564937

* Thu Aug 06 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.1b-3
- Update the .desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.1b-1
- kmplayer-0.11.1b
- drop upstreamed patches

* Mon May 18 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.1a-1
- kmplayer-0.11.1a

* Mon May 11 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.1-1
- kmplayer-0.11.1
- drop upstreamed patches

* Tue Mar 24 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.11.0a-2
- default to using phonon engine (instead of mplayer)

* Tue Mar 24 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.11.0a-1
- kmplayer-0.11.0a (KDE4)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.10.0c-4
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 0.10.0c-3
- really include/use -icon patch

* Tue Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 0.10.0c-2
- patch kmplayer.desktop: Icon=kmplayer

* Mon Jan 07 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 0.10.0c-1
- kmplayer-0.10.0c

* Wed Nov 21 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.10.0a-1
- kmplayer-0.10.0a

* Wed Oct 03 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.10.0-1
- kmplayer-0.10.0

* Wed Apr 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.4a-1
- kmplayer-0.9.4a
- +cairo support

* Wed Jan 03 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.3a-1
- kmplayer-0.9.3a

* Fri Sep 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.3-1
- 0.9.3

* Fri Jul 07 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.2-2.a
- 0.9.2a

* Mon Apr 24 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.2-1
- 0.9.2(final)

* Fri Apr 14 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.2-0.1.rc1
- 0.9.2-rc1

* Fri Nov 11 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.9.1-0.lvn.1
- 0.9.1

* Wed Mar 09 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.4-0.2.a.kde
- 0.8.4a

* Sat Jan 01 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.3-0.2.a.kde
- touchup x-mplayer2.deskop

* Fri Nov 19 2004 Rex Dieter <rexdieter[AT]users.sf.net> 0.8.3-0.1.a.kde
- 0.8.3a
