%undefine __cmake_in_source_build

%bcond doxy 0
%bcond testsqtwebkit 0
# disable ragel since it is failing on i686:
#   [ 17%] Generating Rfc5322HeaderParser.generated.cpp from /builddir/build/BUILD/trojita-5295175f234c73c2df03eb59d571c239c2d19e58/src/Imap/Parser/Rfc5322HeaderParser.cpp
#   /usr/bin/ragel-c -T1 -o /builddir/build/BUILD/trojita-5295175f234c73c2df03eb59d571c239c2d19e58/redhat-linux-build/Rfc5322HeaderParser.generated.cpp /builddir/build/BUILD/trojita-5295175f234c73c2df03eb59d571c239c2d19e58/src/Imap/Parser/Rfc5322HeaderParser.cpp
#   fatal: UNKNOWN INSTRUCTION: 0x00 -- something is wrong
%bcond ragel 0

%global gitdate 20230430
%global commit0 d1e1b4a69e934d1fed930634b4a6a637bea273a8
%global srcurl  https://github.com/KDE/%{name}

Name:           trojita
Version:        0.7.0.1
Release:        0.22.%{gitdate}git%(c=%{commit0}; echo ${c:0:7} )%{?dist}
Source0:        %{srcurl}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz

# run the script that calls svn to get latest po files:
# cd $SRCDIR
# sed -i -e s/extragear-pim/trojita/g l10n-fetch-po-files.py
# python2 l10n-fetch-po-files.py
# tar cJf ../trojita_common-po-20220125.tar.xz po/
Source10:       %{name}_common-po-20221113.tar.xz

## upstream patches

## downstream patches
# disable the GPG tests because they fail due to a GPG limitation:
# gpg: can't connect to the agent: File name too long
# https://bugs.kde.org/show_bug.cgi?id=410414
Patch11:        trojita-0.7.0.1-disable-gpg-tests.patch

# Almost everything: dual-licensed under the GPLv2 or GPLv3
# (with KDE e.V. provision for relicensing)
# src/XtConnect: BSD
# src/Imap/Parser/3rdparty/kcodecs.*: LGPLv2
# Nokia imports: LGPLv2.1 or GPLv3
# src/Imap/Parser/3rdparty/rfccodecs.cpp: LGPLv2+
# src/qwwsmtpclient/: GPLv2
## note that LGPL 2.1 short name is LGPLv2 according to
## https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
#License:        GPLv2+ and LGPLv2+ and BSD
#License:        GPLv2+
License:        GPL-2.0-or-later

Summary:        IMAP e-mail client
URL:            http://%{name}.flaska.net

# rhbz#1402577 ppc64* FIXME: src/Imap/Parser/Rfc5322HeaderParser.cpp:2238:3:
# error: narrowing conversion of '-1' from 'int' to 'char' inside { } [-Wnarrowing]
# also rhbz#1402580 aarch64 and rhbz#1450505 s390x
ExcludeArch:    ppc64 ppc64le s390x

BuildRequires:  kf5-rpm-macros
%global ctest ctest%{?rhel:3} %{?_smp_mflags} --output-on-failure -VV

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qt5-qttools-devel

# explicitly install Qt5Svg for runtime, rpmbuild's magic fails
Requires:       qt5-qtsvg

# (optional) features
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qtkeychain-qt5-devel
%if %{with ragel}
BuildRequires:  ragel
%endif

# (optional) support for GPG and S/MIME
BuildRequires:  gnupg2-smime
BuildRequires:  gpgme-devel
BuildRequires:  gpgmepp-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  boost-devel
BuildRequires:  mimetic-devel
# fix for inside mockbuild, gpg: deleting secret key failed: No pinentry
BuildRequires:  pinentry
BuildRequires:  qgpgme-devel

%if %{undefined flatpak}
# kf5-akonadi-server-devel (and hence kf5-akonadi-contacts-devel) implicitly
# requires this (#2046299):
BuildRequires:  kf5-kio-devel
# kf5-kcontacts-devel (and hence kf5-akonadi-contacts-devel) implicitly
# requires this (#2046310):
BuildRequires:  kf5-ki18n-devel
# kf5-grantleetheme-devel (and hence kf5-akonadi-contacts-devel) implicitly
# requires this (#2046574):
BuildRequires:  grantlee-qt5-devel

BuildRequires:  kf5-akonadi-contacts-devel
%endif
BuildRequires:  kf5-sonnet-devel

%if %{with doxy}
BuildRequires:  doxygen graphviz
%endif

# needs for %%check
BuildRequires:  desktop-file-utils
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif
BuildRequires:  xorg-x11-server-Xvfb

# provide some icons
Requires:       hicolor-icon-theme

%description
Trojitá is a IMAP e-mail client which:
  * Enables you to access your mail anytime, anywhere.
  * Does not slow you down. If we can improve the productivity of an e-mail
    user, we better do.
  * Respects open standards and facilitates modern technologies. We value
    the vendor-neutrality that IMAP provides and are committed to be as
    inter-operable as possible.
  * Is efficient — be it at conserving the network bandwidth, keeping memory
    use at a reasonable level or not hogging the system's CPU.
  * Can be used on many platforms. One UI is not enough for everyone, but our
    IMAP core works fine on anything from desktop computers to cell phones
    and big ERP systems.
  * Plays well with the rest of the ecosystem. We don't like reinventing wheels,
    but when the existing wheels quite don't fit the tracks, we're not afraid
    of making them work.

This application is heavily based on Qt and uses WebKit.


%if %{with doxy}
# optional developer documentation
%package doc
BuildArch: noarch
Summary:   Documentation files for %{name}

%description doc
%{summary}.
%endif


%prep
%setup -qn%{name}-%{commit0} -a10
%patch 11 -p1 -b .disable-gpg-tests

%build
%if %{without testsqtwebkit}
export CXXFLAGS="%{optflags} -DSKIP_WEBKIT_TESTS"
%endif
# change path for the library, https://bugs.kde.org/show_bug.cgi?id=332579
%cmake_kf5 \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}/%{name} \
    -DCMAKE_INSTALL_RPATH=%{_libdir}/%{name} \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON \
    -DWITH_AKONADIADDRESSBOOK_PLUGIN:BOOL=%{!?flatpak:ON}%{?flatpak:OFF} \
    -DWITH_GPGMEPP:BOOL=ON \
    -DWITH_SONNET_PLUGIN:BOOL=ON \
    -DWITH_RAGEL:BOOL=%{?with_ragel:ON}%{!?with_ragel:OFF}
%cmake_build

%if %{with doxy}
doxygen src/Doxyfile
%endif

%install
%cmake_install
%find_lang %{name}_common --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*%{name}.desktop
# appstream is not available in EPEL
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*%{name}.appdata.xml
%endif
# do tests in some fake X
xvfb-run -a %ctest


%files -f %{name}_common.lang
%license LICENSE
%doc README src/Doxyfile
%{_mandir}/man1/%{name}.1*
%{_libdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/be.contacts
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale

%if %{with doxy}
%files doc
%license LICENSE
%doc _doxygen/*
%endif


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.22.20230430gitd1e1b4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.21.20230430gitd1e1b4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.20.20230430gitd1e1b4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.19.20230430gitd1e1b4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 30 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0.7.0.1-0.18.20230430gitd1e1b4a
- Update to commit d1e1b4a69e934d1fed930634b4a6a637bea273a8

* Wed Mar 22 2023 Jan Grulich <jgrulich@redhat.com> - 0.7.0.1-0.18.20220904git5295175
- Rebuild (grantlee-qt5)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.17.20220904git5295175
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Jiri Kucera <jkucera@redhat.com> - 0.7.0.1-0.16.20220904git5295175
- Rebuild for gpgme 1.17.1

* Sun Nov 13 2022 Jiri Kucera <jkucera@redhat.com> - 0.7.0.1-0.15.20220904git5295175
- New git snapshot, up to gpgme[>=1.18.0] fix (gpgme is not rebased yet)
  Note that no new strings have been added from commit 5295175 to now so it is save
  to fetch the latest ./po revision from SVN
- Fixes FTBFS with akonadi-contact>=22.04.x
- Add support for ragel 7
- Use SPDX license identifier
- Spec file cleanup

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.14.20220117git266c757
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.0.1-0.13.20220117git266c757
- Add BuildRequires: kf5-kio-devel (workaround for #2046299)
- Add BuildRequires: kf5-ki18n-devel (workaround for #2046310)
- Add BuildRequires: grantlee-qt5-devel (workaround for #2046574)

* Wed Jan 26 2022 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.0.1-0.12.20220117git266c757
- New git snapshot, hopefully fixes longstanding FTBFS (#1923550, #1988027)
- F34 only: Use -Wl,--copy-dt-needed-entries to work around F34 FTBFS (#1923550)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.11.20191104git36b0587
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.0.1-0.10.20191104git36b0587
- drop obsolete and no longer available BR kf5-gpgmepp-devel, CMakeLists.txt
  prefers already BRed gpgmepp-devel and qgpgme-devel, fixes FTBFS (#1988027)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.9.20191104git36b0587
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.8.20191104git36b0587
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.7.20191104git36b0587
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.6.20191104git36b0587
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0.1-0.5.20191104git36b0587
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.0.1-0.4.20190618git90b417b
- new git snapshot, enable builds for armv7hl and aarch64

* Thu Oct 10 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.0.1-0.3.20190618git90b417b
- rebuilt

* Mon Jul 29 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.0.1-0.2.20190618gitIcf4fda
- work around GPG test failure (kde#410414, GPG/kernel limitation) by disabling
  the offending tests for now (pending a better fix from upstream)
- add missing BuildRequires: qgpgme-devel
- fix unpackaged file (work around find_lang not supporting nds (Low Saxon))
- fix unowned locale parent directories

* Sun Jul 28 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.0.1-0.1.20190618gitIcf4fda
- use latest git snapshot with a bunch of fixes
- enable build testing, again
- enable akonadi addressbook plugin
- enable sonnet plugin
- enable gpgmepp plugin, again
- disable ragel,  rhbz#1734036

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Raphael Groner <projects.rg@smart.ms> - 0.7-9
- add patch to skip instable tests for qtwebkit
- merge unpacking of po files into setup command

* Fri May 12 2017 Raphael Groner <projects.rg@smart.ms> - 0.7-8
- add s390x to exluded architectures

* Mon Feb 27 2017 Raphael Groner <projects.rg@smart.ms> - 0.7-8
- rebuilt

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7-6
- Rebuild for gpgme 1.18

* Wed Dec 07 2016 Builder <projects.rg@smart.ms> - 0.7-5
- add ExcludeArch
- fix gpg test
- add BR: gnupg2-smime

* Sat Jul 02 2016 Raphael Groner <projects.rg@smart.ms> - 0.7-4
- [epel7] rebuild for qtkeychain-0.7.0

* Sat Jun 25 2016 Raphael Groner <projects.rg@smart.ms> - 0.7-3
- explicitly R: qt5-qtsvg

* Sat Jun 25 2016 Raphael Groner <projects.rg@smart.ms> - 0.7-2
- [epel7] enable gpg and mimetic
- [epel7] fix cmake for kf5
- improve some comments
- [epel7] appstream is not available
- [epel7] fix ctest

* Sun Jun 12 2016 Raphael Groner <projects.rg@smart.ms> - 0.7-1
- official upstream version

* Sun Jun 12 2016 Raphael Groner <projects.rg@smart.ms> - 0.7-0.1.20160610git8901a5c
- switch to git snapshot
- add support for GPG and MIME
- drop manpage
- use target build folder

* Mon May 23 2016 Nikos Roussos <comzeradd@fedoraproject.org> 0.6-6
- Rebuild for qtkeychain new release

* Fri May 20 2016 Raphael Groner <projects.rg@smart.ms> - 0.6-5
- rebuild due to qtkeychain ABI change

* Tue Apr 05 2016 Raphael Groner <projects.rg@smart.ms> - 0.6-4
- reenable tests on all arches, icu/gcc6 bug is fixed, rhbz#1307633, rhbz#1309731

* Tue Mar 08 2016 Rex Dieter <rdieter@fedoraproject.org> 0.6-3
- drop DBUS_FATAL_WARNINGS=0 hack, rhbz#1309731 fixed
- use pregenerated trojita manpage (built-time one is bad)

* Sun Feb 21 2016 Raphael Groner <projects.rg@smart.ms> - 0.6-2
- use xvfb-run -a
- workaround for FTBFS cause of dbus, rhbz#1309731
- disable fatal warnings

* Tue Feb 02 2016 Raphael Groner <projects.rg@smart.ms> - 0.6-1
- new version
- use xvfb-run

* Wed Dec 16 2015 Raphael Groner <projects.rg@smart.ms> - 0.5a-2.20151216gitefa30f3
- add QtKeyChain
- drop qt4

* Wed Dec 16 2015 Raphael Groner <projects.rg@smart.ms> - 0.5a-1.20151216gitefa30f3
- use latest upstream snapshot as post-release
- finally well Qt5.6 support!

* Sat Dec 12 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-9
- add upstream patches for Qt5.x

* Mon Oct 05 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-8
- add missing headers inclusion, rhbz#1266712

* Fri Jun 26 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-7
- fix build conditional for optional doxygen

* Fri Jun 26 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-6
- optional BR: at EPEL

* Wed Jun 24 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-5
- add files validation
- use license GPLv2+ aggregated
- use build conditionals
- insert some comments
- insert BR: zlib-devel (optional imap compression)

* Wed Apr 01 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-4
- reenable html formatting testcase
- optional doxygen

* Wed Apr 01 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-3
- ease switching build with qt4 or qt5
- disable doxygen
- remove toolkit from summary
- use build subfolder
- improve tests execution

* Tue Mar 31 2015 Raphael Groner <projects.rg@smart.ms> - 0.5-2
- build for qt5

* Sat Feb 28 2015 Raphael Groner <projects.rg (AT) smart.ms> - 0.5-1
- clean files section and R: hicolor-icon-theme
- introduce license macro
- use name macro generally
- new upstream version 0.5
- distribute doxygen files

* Mon Oct 27 2014 Karel Volný <kvolny@redhat.com> 0.4.1-3
- Added ragel build requirement

* Mon Apr 14 2014 Karel Volný <kvolny@redhat.com> 0.4.1-2
- Fixed icon handling and added comments as per the package review
- https://bugzilla.redhat.com/show_bug.cgi?id=1080411#c2

* Tue Mar 25 2014 Karel Volný <kvolny@redhat.com> 0.4.1-1
- Initial Fedora version based on upstream OBS package
