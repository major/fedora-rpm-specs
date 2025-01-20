Name:           psi
Version:        1.5
Release:        16%{?dist}

# GPL-2.0-or-later - core project.
# LGPL-2.1-or-later - iris library, widgets, several tools.
# Zlib - bundled minizip library.
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND Zlib
Summary:        Jabber client based on Qt
URL:            https://psi-im.org

Source0:        https://github.com/%{name}-im/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/%{name}-im/%{name}-l10n/archive/%{version}/%{name}-l10n-%{version}.tar.gz
Source2:        https://github.com/%{name}-im/plugins/archive/%{version}/%{name}-plugins-%{version}.tar.gz

# https://github.com/psi-im/psi/commit/2212aeb8412ef790fba62e3cf96c36e6a8bd7b8e
Patch100:       hunspell-1.7.patch
# https://github.com/psi-im/plugins/commit/77d213dfd57df8658eae0266dcbc224323c6f5e8
Patch101:       %{name}-screenshot-plugin-qt515.patch

BuildRequires:  cmake(QJDns-qt5)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebKit)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libotr)
BuildRequires:  pkgconfig(tidy)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(zlib)

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libgcrypt-devel
BuildRequires:  ninja-build

Requires:       %{name}-common = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugins%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:       hicolor-icon-theme
Requires:       qca-qt5-gnupg%{?_isa}
Requires:       qca-qt5-ossl%{?_isa}

Provides:       bundled(iris) = 0~git
Provides:       bundled(minizip) = 1.2.11

%description
%{name} is the premiere Instant Messaging application designed for Microsoft
Windows, Apple Mac OS X and GNU/Linux.

Built upon an open protocol named Jabber, %{name} is a fast and lightweight
messaging client that utilises the best in open source technologies.

%{name} contains all the features necessary to chat, with no bloated extras
that slow your computer down. The Jabber protocol provides gateways to other
protocols as AIM, ICQ, MSN and Yahoo!.

Attention! This package is an old-stable branch of the Psi Instant Messenger.
If you want modern features, including voice and video calls, OMEMO end-to-end
encryption support, consider switching to the %{name}-plus package.

%package common
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Common assets for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-i18n = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-i18n < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-icons = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-icons < %{?epoch:%{epoch}:}%{version}-%{release}

%description common
This package contains architecture-agnostic common assets (language packs,
icons, themes, skins, etc.) for %{name}.

%package plugins
# GPLv2+ is used for the most plugins.
# BSD - screenshot plugin.
License:        GPLv2+ and BSD
Summary:        Additional plugins for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugins
This package adds additional plugins to %{name}.

%prep
# Unpacking main tarball...
%setup -q

# Unpacking tarball with additional locales...
tar -xf %{SOURCE1} %{name}-l10n-%{version}/translations --strip=1

# Unpacking tarball with additional plugins...
tar -C src/plugins -xf %{SOURCE2} plugins-%{version}/generic --strip=1

# Applying patches...
%patch -P100 -p1
%patch -P101 -p1

# Removing bundled libraries...
rm -rf iris/src/jdns

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_PLUGINS:BOOL=ON \
    -DENABLE_WEBKIT:BOOL=ON \
    -DPLUGINS_PATH:PATH="%{_lib}/%{name}/plugins" \
    -DSEPARATE_QJDNS:BOOL=ON \
    -DUSE_ENCHANT:BOOL=OFF \
    -DUSE_HUNSPELL:BOOL=ON \
    -DUSE_QJDNS:BOOL=ON \
    -DUSE_QT5:BOOL=ON
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt
install -m 0644 -p -D %{name}.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%files common -f %{name}.lang
%{_datadir}/%{name}/certs
%{_datadir}/%{name}/iconsets
%{_datadir}/%{name}/sound
%{_datadir}/%{name}/themes
%{_datadir}/%{name}/*.txt

%files plugins
%{_libdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 14 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-8
- Moved localizations to the -common subpackage.

* Sat May 14 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-7
- Performed SPEC sync with psi-plus.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-4
- Rebuilt due to libtidy soversion bump.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-2
- Backported upstream patch with Qt 5.15 build fixes.

* Mon Sep 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-1
- Updated to upstream version 1.5.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.4-2
- use %%_metainfodir macro

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4-1
- Updated to upstream version 1.4.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 1.3-6
- rebuild for hunspell-1.7.0

* Mon Sep 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3-5
- Use bundled minizip for Fedora 30+.

* Tue Aug 28 2018 Patrik Novotný <panovotn@redhat.com> - 1.3-4
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3-2
- Fixed build against Qt 5.11 on Rawhide.

* Sat May 12 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3-1
- Updated to upstream version 1.3.
- Major SPEC cleanup and fixes.
- Added additional plugins as subpackage.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15-23
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15-21
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  4 2016 Ivan Romanov <drizt@land.ru> - 0.15-17
- Fix armhfp compilation rhbz #1304549

* Fri Jan 22 2016 Rex Dieter <rdieter@fedoraproject.org> 0.15-16
- fix build flags harder (#1301086)

* Mon Jan 18 2016 Rex Dieter <rdieter@fedoraproject.org> 0.15-15
- ensure proper qmake and build flags (see also bug #1279265)

* Wed Jan  6 2016 Ivan Romanov <drizt@land.ru> - 0.15-14
- Rebuild with forgottent patch

* Wed Jan  6 2016 Ivan Romanov <drizt@land.ru> - 0.15-13
- Rebuild with new qconf
- Use external minizip
- Update qjdns patch

* Mon Nov 23 2015 Raphael Groner <projects.rg@smart.ms> - 0.15-12
- use better configure options
- modernize, restructure and cleanup for better readability

* Sun Nov 22 2015 Raphael Groner <projects.rg@smart.ms> - 0.15-11
- bump for rebuild

* Wed Oct 14 2015 Raphael Groner <projects.rg@smart.ms> - 0.15-10
- bundled(iris), rhbz#737304
- cleanup

* Thu Jul 23 2015 Raphael Groner <projects.rg@smart.ms> - 0.15-9
- bump for rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.15-7
- Rebuilt for GCC 5 C++11 ABI change

* Fri Dec 12 2014 Raphael Groner <projects.rg [AT] smart.ms> - 0.15-6
- unbundle jdns (and iris later)
- cleanup to spec

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 05 2012 Sven Lankes <sven@lank.es> - 0.15-1
- new upstream release

* Wed Sep 26 2012 Sven Lankes <sven@lank.es> - 0.15-0.2.rc3
- new upstream release

* Tue Sep 18 2012 Sven Lankes <sven@lank.es> - 0.15-0.2.rc2
- new upstream release

* Tue Aug 28 2012 Sven Lankes <sven@lank.es> 0.15-0.2.rc1
- new upstream release

* Wed Aug 22 2012 Sven Lankes <sven@lank.es> 0.15-0.1beta2
- new upstream (beta) release
- drop all patches (all upstream now)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 07 2012 Sven Lankes <sven@lank.es> 0.14-8
- fix compile with gcc 4.7.0

* Sun Nov 27 2011 Sven Lankes <sven@lank.es> 0.14-7
- Change certificate ui to use plain-text fields to avoid security
    issue with qlabel. rhbz #746877

* Wed Mar 16 2011 Rex Dieter <rdieter@fedoraproject.org> 0.14-6
- fix FTBFS (drop Requires(hint) usage)
- make qca plugin deps arched
- add arched/versioned qt4 runtime dep
- update scriptlets
- drop desktop-file-install --vendor usage (f15+)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Sven Lankes <sven@lank.es> 0.14-4
- Don't crash in chat room configuration dialog (rhbz #668850)

* Thu Apr 08 2010 Aurelien Bompard <abompard@fedoraproject.org> -  0.14-3
- disable debug, but don't break the -debuginfo pkg (rhbz#579131)

* Sun Apr 04 2010 Aurelien Bompard <abompard@fedoraproject.org> -  0.14-2
- disable debug (rhbz#579131)

* Thu Dec 03 2009 Aurelien Bompard <abompard@fedoraproject.org> -  0.14-1
- 0.14 final
- patch1 merged upstream

* Sun Nov 29 2009 Sven Lankes <sven@lank.es> 0.14-0.2.rc3
- Add (upstream) patch to make enchant spelling-suggestions work
- Remove old patches

* Sun Nov 29 2009 Sven Lankes <sven@lank.es> 0.14-0.1.rc3
- 0.14 rc3

* Mon Nov 09 2009 Aurelien Bompard <abompard@fedoraproject.org> -  0.14-0.1.rc1
- 0.14 rc1

* Tue Jul 28 2009 Aurelien Bompard <abompard@fedoraproject.org> - 0.13-1
- 0.13 final

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-0.3.rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Sven Lankes <sven@lank.es> 0.13-0.2.rc4
- 0.13 rc4

* Mon Jul 13 2009 Sven Lankes <sven@lank.es> 0.13-0.2.rc3
- 0.13 rc3
- remove qt 4.5 patch

* Sun Jul 05 2009 Sven Lankes <sven@lank.es> 0.13-0.2.rc2
- own plugin directories (bz #509683)

* Thu Jul 02 2009 Sven Lankes <sven@lank.es> 0.13-0.1.rc2
- 0.13 rc2

* Sun May 24 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.13-0.1.rc1
- 0.13 rc1

* Sat Mar 28 2009 Sven Lankes <sven@lank.es> 0.12.1-2
- bump Version to avoid newer EVR in F9/F10

* Tue Mar 03 2009 Sven Lankes <sven@lank.es> 0.12.1-1
- Update to 0.12.1 (fix for CVE-2008-6393)
- add patch for qt 4.5 support

* Sun Mar 01 2009 Robert Scheck <robert@fedoraproject.org> 0.12-3
- Added missing build requirement to glib2-devel

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 13 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.12-1
- version 0.12

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.11-5
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.11-4
- Autorebuild for GCC 4.3

* Sat Nov 24 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.11-3
- Require qca-gnupg for GnuPG support

* Wed Oct 17 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.11-1
- version 0.11

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.10-5
- rebuild

* Thu Apr 13 2006 Aurelien Bompard <gauret[AT]free.fr> 0.10-4
- update translations for CS, DE, ET and VI

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 0.10-3
- rebuild for FC5

* Thu Jan 12 2006 Aurelien Bompard <gauret[AT]free.fr> 0.10-1
- version 0.10 final

* Tue Jan 03 2006 Aurelien Bompard <gauret[AT]free.fr> 0.10-0.3.test4
- version 0.10 test4

* Thu Nov 03 2005 Aurelien Bompard <gauret[AT]free.fr> 0.10-0.2.test3
- version 0.10 test3

* Sat Oct 15 2005 Aurelien Bompard <gauret[AT]free.fr> 0.10-0.2.test2
- version 0.10 test2
- drop patch 3 (applied upstream)
- drop icon symlink (useless)

* Thu Aug 25 2005 Aurelien Bompard <gauret[AT]free.fr> 0.10-0.1.test1
- version 0.10 test1
- spec cleanups

* Wed Jun  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.3-4
- patch it for 64-bit/GCC 4

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.9.3-3
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.3-2
- rebuilt

* Sun Jan 09 2005 Aurelien Bompard <gauret[AT]free.fr> 0:0.9.3-1
- version 0.9.3 final

* Mon Jan 03 2005 Aurelien Bompard <gauret[AT]free.fr> 0:0.9.3-0.fdr.0.3.test2
- version 0.9.3-test2

* Thu Nov 25 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.9.3-0.fdr.0.2.test1
- Drop hardcoded requirement on qca-tls, it should be a plugin

* Mon Nov 22 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.9.3-0.fdr.0.1.test1
- update to 0.9.3test1
- use the provided icon in the menu and drop Source1.
- add crystal iconset
- added Russian and Eesti translations

* Sat Sep 18 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.9.2-0.fdr.3
- add patch for typing notification
- add crystal iconset
- update translations (adding kiswahili and Eesti)

* Fri Jun 11 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.9.2-0.fdr.2
- split qca-tls out of this package and require it
- fix build on FC1

* Thu Jun 10 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.9.2-0.fdr.1
- version 0.9.2
- drop libgnome patch, %%{name} now uses gnome-open
- rediffed the other patches

* Sat Feb 28 2004 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9.1-0.fdr.9
- add a patch to build with mach
- removed URLs in iconsets because the website changed
- add one iconset

* Tue Feb 17 2004 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9.1-0.fdr.8
- add a patch from Debian
- avoid stripping of binary

* Sat Feb 14 2004 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9.1-0.fdr.7
- add German (de) and Simplified Chinese (zh) translations
- Apply suggestions from Michael Schwendt :
  - BuildRequies kdelibs-devel if built --with kde
  - Drop rostericonset "neos" because it is buggy
  - Put docs in %%_datadir/%%{name} to avoid empty about box
  - Fix source URL
  - Fix files list for FC2

* Mon Feb 09 2004 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9.1-0.fdr.6
- add Cesky (cs) and Catalan (ca) translations

* Sat Jan 31 2004 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9.1-0.fdr.5
- add polish (pl) translation.
- improve description of the i18n package

* Wed Jan 28 2004 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9.1-0.fdr.4
- add spanish (es) and svenska (se) translations.
- *really* add GNOME icon...

* Tue Jan 27 2004 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9.1-0.fdr.3
- add slovak (sk) and italian (it) translations.

* Tue Jan 20 2004 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9.1-0.fdr.2
- add GNOME icon

* Sun Jan 11 2004 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9.1-0.fdr.1
- version 0.9.1
- add jisp emoticons in a separate package (%%{name}-icons)
- add ICONSET-HOWTO
- drop old iconsets (and thus remove buildrequires: unzip)
- add rebuild option "--without kde" to prepare for future version of %%{name}
  which will take this into account. Right now it is ignored.

* Sat Nov 22 2003 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9-0.fdr.4
- add Requires: sox to play sound (thanks to you-know-who ;-) )
- fix date in changelog.

* Fri Nov 21 2003 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9-0.fdr.3
- Thanks to Michael Schwendt (again :-) ) :
  * exclude lang files from main package
  * preserve timestamps when possible
  * fix .desktop file
  * add ssl support

* Tue Nov 18 2003 Aurelien Bompard <gauret[AT]free.fr> - 0:0.9-0.fdr.2
- Thanks to Michael Schwendt :
  * group language packs into one subpackage.
  * added epoch=0
  * added environnement variables to ./configure
  * added BuildRequires: XFree86-devel

* Wed Nov 12 2003 Aurelien Bompard <gauret[AT]free.fr> - 0.9-0.fdr.1
- port to Fedora (from Mandrake)
