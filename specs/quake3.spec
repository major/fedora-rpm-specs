Name:           quake3
Version:        1.36
Release:        49.svn2102%{?dist}
Summary:        Quake 3 Arena engine (ioquake3 version)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://ioquake3.org/
# to regenerate (note included systemlib copies are removed for size, lcc
# is removed as it is not Free software):
# svn co svn://svn.icculus.org/quake3/tags/%%{version} %%{name}-%%{version}
# pushd %%{name}-%%{version}
# rm -fr `find -name .svn` code/AL code/SDL12 code/libcurl code/libs
# rm -fr code/jpeg-8c code/zlib code/libspeex code/tools/lcc
# popd
# tar cvfj %%{name}-%%{version}.tar.bz2 %%{name}-%%{version}
Source0:        %{name}-%{version}-svn2102.tar.bz2
Source1:        %{name}-demo.sh
Source2:        %{name}.autodlrc
Source3:        %{name}.desktop
Source4:        %{name}.png
Source5:        %{name}-update.sh
Source6:        %{name}-update.autodlrc
Source7:        urbanterror.sh
Source8:        urbanterror.autodlrc
Source9:        urbanterror.desktop
Source10:       urbanterror.png
# Note this is for wop 1.5, 1.6 is available but that needs a custom engine
Source11:       worldofpadman.sh
Source12:       worldofpadman.autodlrc
Source13:       worldofpadman.desktop
Source14:       wop.png
Source15:       jpeg_memsrc.h
Source16:       jpeg_memsrc.c
Source17:       %{name}.appdata.xml
Source18:       urbanterror.appdata.xml
Source19:       worldofpadman.appdata.xml
Source20:       wop.svg
Patch0:         quake3-1.36-syslibs.patch
Patch1:         quake3-1.34-rc4-demo-pak.patch
# patches from Debian for openarena compatibility (increase some buffer sizes)
Patch2:         0011-Double-the-maximum-number-of-cvars.patch
Patch3:         0012-Increase-the-command-buffer-from-16K-to-128K-followi.patch
# big-endian build fix
Patch4:         quake3-1.36-build.patch
Patch5:         quake3-fastcall.patch
Patch6:         quake3-aarch64.patch
# For urban-terror 4.2
Patch7:         quake3-1.36-unaligned-qvm.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL-devel libXt-devel openal-soft-devel libjpeg-devel
BuildRequires:  speex-devel speexdsp-devel libvorbis-devel curl-devel
BuildRequires:  zlib-devel desktop-file-utils libappstream-glib
%ifarch %{ix86} x86_64
BuildRequires:  nasm
%endif
# for quake3-update
Requires:       autodownloader tar

%description
This package contains the enhanced opensource ioquake3 version of the Quake 3
Arena engine. This engine can be used to play a number of games based on this
engine, below is an (incomplete list):

* OpenArena, Free, Open Source Quake3 like game, recommended!
  (packagename: openarena)

* Urban Terror, gratis, but not Open Source FPS best be described as a
  Hollywood tactical shooter, a downloader and installer including an
  application menu entry is available in the urbanterror package.

* World of Padman, gratis, but not Open Source Comic FPS, a downloader and
  installer including an application menu entry is available in the
  worldofpadman package.

* Quake3 Arena, the original! A downloader and installer for the gratis, but
  not Open Source demo, including an application menu entry is available in
  the quake3-demo package.
  
  If you own a copy of quake 3, you will need to copy pak0.pk3 from the
  original CD-ROM and your q3key to /usr/share/quake3/baseq3 or ~/.q3a/baseq3.
  Also copy the pak?.pk3 files from the original 1.32 Quake 3 Arena point
  release there if you have them available or run quake3-update to download
  them for you.


%package demo
Summary:        Quake 3 Arena tournament 3D shooter game demo installer
Requires:       quake3 = %{version}-%{release}
Requires:       hicolor-icon-theme opengl-games-utils unzip
# quake3-demo used to be part of the quake3 package, make sure that people
# who have the old version with the demo included don't all of a sudden have
# the demo menu entry disappear.
Obsoletes:      quake3 <= 1.34-0.4.rc4.fc9

%description demo
Quake 3 Arena tournament 3D shooter game demo installer. The Quake3 engine is
Open Source and as such is available as part of Fedora. The original Quake3
datafiles however are not Open Source and thus are not available as part of
Fedora. There is a gratis, but not Open Source demo available on the internet.

This package installs an applications menu entry for playing the Quake3 Arena
demo. The first time you click this menu entry, it will offer to download and
install the Quake 3 demo datafiles for you.


%package -n urbanterror
Summary:        FPS best be described as a Hollywood tactical shooter
URL:            http://www.urbanterror.net/
Requires:       quake3 = %{version}-%{release}
Requires:       hicolor-icon-theme opengl-games-utils unzip

%description -n urbanterror
Urban Terror could best be described as a Hollywood tactical shooter; it is
realism based to a certain extent (environments/weapons/player models), but
also goes by the motto "fun over realism" (fast gameplay and lots of action).
This combination of reality and action results in a very unique, enjoyable
and addictive game.

Urban Terror uses the GPL licensed ioquake3 engine, however the Urban Terror
datafiles are not freely redistributable. This package will install an Urban
Terror menu entry, which will automatically download the necessary datafiles
(2GB!) the first time you start Urban Terror.


%package -n worldofpadman
Summary:        World Of Padman - Comic 3D-Shooter
URL:            http://padworld.myexp.de/
Requires:       quake3 = %{version}-%{release}
Requires:       hicolor-icon-theme opengl-games-utils tar gzip

%description -n worldofpadman
World of Padman (WoP) is a first-person shooter computer game available in
both English and German. The idea is based on the Padman comic strip for the
magazine PlayStation Games created by the professional cartoon artist Andreas
'ENTE' Endres, who is also the man who made many of the maps included with the
game in 1998. Most of the maps in the game are lilliput style.

World of Padman uses the GPL licensed ioquake3 engine, however the Wop data-
files are not freely redistributable. This package will install a World of
Padman menu entry, which will automatically download the necessary datafiles
(1GB!) the first time you start World of Padman.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
# Add jpeg_memsrc
cp -p %{SOURCE15} %{SOURCE16} ./code/renderer/


%build
# the CROSS_COMPILING=1 is a hack to not build q3cc and qvm files
# since we've stripped out q3cc as this is not Free Software.
make %{?_smp_mflags} \
    OPTIMIZE="$RPM_OPT_FLAGS -fno-strict-aliasing" \
    DEFAULT_BASEDIR=%{_datadir}/%{name} USE_CODEC_VORBIS=1 \
    USE_LOCAL_HEADERS=0 BUILD_GAME_SO=0 GENERATE_DEPENDENCIES=0 \
    USE_INTERNAL_SPEEX=0 USE_INTERNAL_ZLIB=0 USE_INTERNAL_JPEG=0 \
    BUILD_CLIENT_SMP=1 CROSS_COMPILING=1
appstream-util validate-relax --nonet %{SOURCE17} %{SOURCE18} %{SOURCE19}


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

install -m 755 build/release-linux-*/ioquake3.* \
  $RPM_BUILD_ROOT%{_bindir}/quake3
install -m 755 build/release-linux-*/ioquake3-smp.* \
  $RPM_BUILD_ROOT%{_bindir}/quake3-smp
install -m 755 build/release-linux-*/ioq3ded.* \
  $RPM_BUILD_ROOT%{_bindir}/q3ded
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/quake3-demo
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}

install -p -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/quake3-update
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/%{name}

install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/urbanterror
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/%{name}

install -p -m 755 %{SOURCE11} $RPM_BUILD_ROOT%{_bindir}/worldofpadman
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE9}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE13}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE17} $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE18} $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE19} $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE10} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE14} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE20} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps

%files
%doc BUGS ChangeLog id-readme.txt md4-readme.txt NOTTODO README TODO
%license COPYING.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-smp
%{_bindir}/%{name}-update
%{_bindir}/q3ded
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}-update.autodlrc

%files demo
%{_bindir}/%{name}-demo
%{_datadir}/%{name}/%{name}.autodlrc
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%files -n urbanterror
%{_bindir}/urbanterror
%{_datadir}/%{name}/urbanterror.autodlrc
%{_datadir}/appdata/urbanterror.appdata.xml
%{_datadir}/applications/urbanterror.desktop
%{_datadir}/icons/hicolor/128x128/apps/urbanterror.png

%files -n worldofpadman
%{_bindir}/worldofpadman
%{_datadir}/%{name}/worldofpadman.autodlrc
%{_datadir}/appdata/worldofpadman.appdata.xml
%{_datadir}/applications/worldofpadman.desktop
%{_datadir}/icons/hicolor/32x32/apps/wop.png
%{_datadir}/icons/hicolor/scalable/apps/wop.svg


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-49.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.36-48.svn2102
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-47.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-46.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-45.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-44.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Arjun Shankar <arjun@redhat.com> - 1.36-43.svn2102
- Port to C99

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-42.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-41.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-40.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-39.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-38.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-37.svn2102
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-36.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-35.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-34.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Vít Ondruch <vondruch@redhat.com> - 1.36-33.svn2102
- Relax AppData validation to fix the FTBFS and comply with guidelines.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-33.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-32.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-31.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-30.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-29.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-28.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-27.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Hans de Goede <hdegoede@redhat.com> - 1.36-26.svn2102
- Add Keywords to the .desktop files

* Fri Dec  4 2015 Hans de Goede <hdegoede@redhat.com> - 1.36-25.svn2102
- Update Urban Terror autodlrc to Urban Terror 4.2.023 (rhbz#1213158)
- Add a patch to make Urban Terror 4.2 work with ioquake3
- Remove dead mirrors from quake3-demo, quake3-update and wop autodlrc files
- Add appdata files

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-24.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.36-23.svn2102
- Add AArch64 support

* Thu Feb 26 2015 Jon Ciesla <limburgher@gmail.com> - 1.36.22.svn2102
- Update speex BR.

* Thu Feb 26 2015 Jon Ciesla <limburgher@gmail.com> - 1.36.21.svn2102
- Move argument passing from VM to engine to global variables (rhbz#1018398)
- per Jeff Layton <jlayton@poochiereds.net>

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-20.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-19.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-18.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Jon Ciesla <limburgher@gmail.com> - 1.36-17.svn2102
- Fix FTBFS.

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 1.36-16.svn2102
- Drop desktop vendor tag.

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.36-15.svn2102
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-14.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-13.svn2102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Dan Horák <dan[at]danny.cz> - 1.36-12.svn2102
- big-endian build fix

* Thu Jul 28 2011 Hans de Goede <hdegoede@redhat.com> - 1.36-11.svn2102
- Update to 1.36 svn snapshot r2102
- This fixes 2 security issues where a malicious server could execute arbitrary
  code on connecting clients (rhbz#725951):
  CVE-2011-1412: Execute arbitrary shell commands on connecting clients
  CVE-2011-2764: Arbitrary code execution when native-code DLLs are enabled
- Update the autodownload + launch script for UrbanTerror to 4.1.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-10.svn1802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan  4 2011 Hans de Goede <hdegoede@redhat.com> 1.36-9.svn1802
- Update worldofpadman autodownloader files and wrapper script to
  download and play World of Padman version 1.5

* Thu Nov 11 2010 Hans de Goede <hdegoede@redhat.com> 1.36-8.svn1802
- Update release to svn revision (r1802)
- Add a whole bunch of patches from Debian which allow using ioquake3 as an
  engine for total conversions and compability with network play with
  official openarena servers (#565763)
- Remove our own hacks for ioquake3 as an engine for total conversions

* Wed May 12 2010 Xavier Lamien <laxathom@fedoraproject.org> - 1.36-7.svn1783
- Update release to svn revision (r1783).
- Remove botlib-strcpy-abuse patch (added upstream).

* Thu Jan 21 2010 Hans de Goede <hdegoede@redhat.com> 1.36-6
- Update (fix) autodlrc mirror URL's (#557252)

* Fri Dec 18 2009 Hans de Goede <hdegoede@redhat.com> 1.36-5
- Modify Urban Terror launch script to allow downloading of maps by default

* Wed Nov  4 2009 Hans de Goede <hdegoede@redhat.com> 1.36-4
- Fix bots not working on Intel 64 bit CPU's (#526338)

* Sun Aug 16 2009 Hans de Goede <hdegoede@redhat.com> 1.36-3
- Switch to openal-soft

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Hans de Goede <hdegoede@redhat.com> 1.36-1
- New upstream release 1.36

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-0.11.rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Hans de Goede <hdegoede@redhat.com> 1.34-0.10.rc4
- Update (fix) autodlrc mirror URL's (rh 481592)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.34-0.9.rc4
- Autorebuild for GCC 4.3

* Thu Jan 17 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.34-0.8.rc4
- Properly recognize the demo pak0 file instead of complaining that no valid
  pak0 was found

* Fri Jan 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.34-0.7.rc4
- Various patches to make openarena work with the generic ioquake3 we ship
- Update urbanterror launcher script to set a much bigger com_hunkMegs,
  otherwise urbanterror will abort when loading bigger levels

* Sun Dec 23 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.34-0.6.rc4
- Update urbanterror autodlrc file to refer to version 4.1 (was 4.0)

* Sun Dec 23 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.34-0.5.rc4
- Split of the demo launcher into a quake3-demo package, so that when for
  example openarena requires quake3 for the engine people don't automatically
  get the demo launcher installed
- Add installer / launcher for Urban Terror in an urbanterror subpackage
  (bz 385771)
- Add installer / launcher for World of Padman in a worldofpadman subpackage

* Wed Dec 12 2007 Alexey Kuznetsov <kuznetsov.alexey@gmail.com> 1.34-0.4.rc4
- Add quake3-update srcipt.

* Thu Sep 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.34-0.3.rc4
- Update autodlrc file to use fast mirrors instead of the slow and unreliable
  official ID software site

* Tue Sep 25 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.34-0.2.rc4
- Use autodownloader to download demo files, thus making the game playable
  without the original CD
- Submit for Fedora inclusion now that the game is playable without the CD
- Update to 1.34-rc4
- Use system libjpeg, system SDL, OpenAL and curl headers

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 1.34-0.1.rc2.svn908
- Update to today's svn code (rev. 908), rc2 from the 1.34 branch.

* Mon May 29 2006 Matthias Saou <http://freshrpms.net/> 1.34-0.1.rc1.svn792
- Update to today's svn code (rev. 792).
- Update the nostrip patch.
- Fix wrapper script since the binary has been renamed from quake3 to
  ioquake3.<arch>, which we rename to plain ioquake3 (in the patch).
- Include new documentation.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.34-0.1.rc1.svn649
- Update to today's svn code (rev. 649).
- Update nostrip patch, now pass OPTFLAGS to the build too.
- Build requires subversion (required for make dist).

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 1.33-0.2.svn470
- Update to today's svn sode (rev. 470).
- Add modular xorg build conditional.
- Revisit nostrip patch for the new code.
- Add (new?) openal-devel build requirement.
- Update %%doc files.

* Sun Nov 13 2005 Matthias Saou <http://freshrpms.net/> 1.33-0.1.svn338
- Update to GPL'ed 1.33 and spec file cleanup.

* Sun Oct 15 2000 Matthias Saou <http://freshrpms.net/> 1.17-1
- Initial RPM based on Loki's 1.17 point release

