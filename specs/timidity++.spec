# Workaround LTO breaking alsa symbol versioning, see:
# https://bugzilla.redhat.com/show_bug.cgi?id=1993671
# https://bugzilla.redhat.com/show_bug.cgi?id=2087786
# https://bugzilla.redhat.com/show_bug.cgi?id=2087904
%global _lto_cflags %nil

Summary: A software wavetable MIDI synthesizer
Name: timidity++
Version: 2.15.0
Release: 12%{?dist}
Source0: http://downloads.sourceforge.net/timidity/TiMidity++-2.15.0.tar.xz
Source1: timidity.desktop
Source2: timidity-xaw.desktop
# Select patches from Debian. Debian patches 0004 and 0005 are *wrong* AFAICT:
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=999709
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=999710
# 0006, 0007, 0008, 0011 and 0012 are not applicable with the 2.15.0 release
Patch01: 0001-don-t-url_unexpand_home_dir-when-opening-a-file.patch
Patch02: 0002-improve-error-message.patch
Patch03: 0003-use-exponentional-backup-select-in-interface-alsaseq.patch
Patch09: 0009-Debian-adaptions-of-manpages.patch
Patch10: 0010-Pass-LDFLAGS-to-addon-linking.patch
Patch13: 0013-readmidi-Fix-division-by-zero.patch
Patch14: 0014-resample-Fix-out-of-bound-access-in-resamplers.patch
Patch15: 0015-timidity-no_date.patch
Patch16: timidity++-configure-c99.patch
URL: http://timidity.sourceforge.net
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
BuildRequires: make gcc
BuildRequires: alsa-lib-devel ncurses-devel gtk2-devel Xaw3d-devel
BuildRequires: libao-devel libvorbis-devel flac-devel speex-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: desktop-file-utils
Requires: soundfont2-default hicolor-icon-theme

%description
TiMidity++ is a MIDI format to wave table format converter and
player. Install timidity++ if you'd like to play MIDI files and your
sound card does not natively support wave table format.


%package        GTK-interface
Summary:        GTK user interface for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    GTK-interface
The %{name}-GTK-interface package contains a GTK based UI for %{name}.


%package        Xaw3D-interface
Summary:        Xaw3D user interface for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    Xaw3D-interface
The %{name}-Xaw3D-interface package contains a Xaw3D based UI for %{name}.


%prep
%autosetup -p1 -n TiMidity++-2.15.0
autoreconf -ivf


%build
export EXTRACFLAGS="$RPM_OPT_FLAGS -DCONFIG_FILE=\\\"/etc/timidity++.cfg\\\""
# Note the first argument to --enable-audio is the default output, and
# we use libao to get pulse output
%configure --disable-dependency-tracking \
  --with-module-dir=%{_libdir}/%{name} \
  --enable-interface=ncurses,vt100,alsaseq,server,network,gtk,xaw \
  --enable-dynamic=gtk,xaw \
  --enable-audio=ao,alsa,oss,jack,vorbis,speex,flac
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 interface/pixmaps/timidity.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/timidity.xpm

%files
%doc AUTHORS README NEWS ChangeLog
%license COPYING
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_mandir}/*/*

%files GTK-interface
%{_libdir}/%{name}/if_gtk.so
%{_datadir}/applications/timidity.desktop
%{_datadir}/icons/hicolor/48x48/apps/timidity.xpm

%files Xaw3D-interface
%{_libdir}/%{name}/if_xaw.so
%{_datadir}/applications/timidity-xaw.desktop
%{_datadir}/icons/hicolor/48x48/apps/timidity.xpm


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.15.0-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Jonathan Wakely <jwakely@redhat.com> - 2.15.0-7
- Patch configure for C99 porting effort

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.15.0-5
- Rebuilt for flac 1.4.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 Hans de Goede <hdegoede@redhat.com> - 2.15.0-3
- Disable LTO to workaround LTO causing an alsa output (-Os) crash (rhbz#1993671)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Hans de Goede <hdegoede@redhat.com> - 2.15.0-1
- New upstream release 2.15.0 (rhbz#1951906)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Hans de Goede <hdegoede@redhat.com> - 2.14.0-16
- Fix CVE-2017-11546 CVE-2017-11547 (rhbz#1480639)
- Fix the .desktop files so that opening a .mid file from a GUI filemanager
  works (rhbz#1541182)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.14.0-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.14.0-5
- Fix Failing build by renaming the timidity desktop file

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.14.0-3
- Remove vendor tag from desktop file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Hans de Goede <hdegoede@redhat.com> - 2.14.0-1
- New upstream release 2.14.0
- Drop all our patches, all 19 are upstream now!

* Mon Apr 30 2012 Hans de Goede <hdegoede@redhat.com> - 2.13.2-31.cvs20111110
- Provide a new trysource config file directive (rhbz#815611)

* Mon Feb 27 2012 Orion Poplawski <orion@cora.nwra.com> - 2.1.13.2-30.cvs20111110
- Rebuild for Xaw3d 1.6.1 

* Fri Jan 20 2012 Hans de Goede <hdegoede@redhat.com> - 2.13.2-29.cvs20111110
- Drop /etc/timidity++.cfg, it will be provided by the package providing
  soundfont2-default instead, so that it can contain tweaks to optimize for
  the default soundfont

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.2-28.cvs20111110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 19 2011 Hans de Goede <hdegoede@redhat.com> - 2.13.2-27.cvs20111110
- Add a patch fixing a whole lot of compiler warnings
- Build the gtk UI as a dynamic plugin, this stops the main binary from
  depending on gtk + a whole bunch of other deps
- Put the gtk UI plugin into its own timidity++-GTK-interface package
- Enable building the Xaw UI as dynamic plugin, and put it in its own
  timidity++-Xaw3D-interface package

* Thu Nov 10 2011 Hans de Goede <hdegoede@redhat.com> - 2.13.2-26.cvs20111110
- Upstream has not been doing new releases for years, but there have been
  some bugfixes in CVS -> upgrade to the latest CVS version
- Drop a bunch of patches for things which are fixed in this CVS version
- Add a patch which fixes the loading of sf2 files with stereo instrument
  samples with missing link-ids between the left and right samples (#710927)

* Mon Nov 07 2011 Christian Krause <chkr@fedoraproject.org> - 2.13.2-25
- add upstream patch to fix garbled sound when start playing (#710927)

* Wed Jul 27 2011 Jindrich Novy <jnovy@redhat.com> - 2.13.2-24
- fix segfault in detect() introduced by libao-first patch (#711224)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov  5 2010 Hans de Goede <hdegoede@redhat.com> - 2.13.2-22
- Drop arts and esd as supported outputs, arts is no longer used in kde4
  and esd has been dead for quite some time now. Since timidity++ does not
  have output-plugins, leaving these 2 enabled means that timidity++ often
  is the only thing on a system dragging in esound-libs and arts. If people
  for some reason still want to use esd or arts for sound output they can
  do so through libao
- Drop the don't compile jack for ppc64 hack, the toolchain issue we hit
  should be long fixed by now

* Thu Sep 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 2.13.2-21
- Bump for libao

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun  3 2009 Hans de Goede <hdegoede@redhat.com> 2.13.2-19
- Don't crash when started in daemon mode (with -iAD) (#501051)

* Tue Mar 24 2009 Hans de Goede <hdegoede@redhat.com> 2.13.2-18
- Require soundfont2-default virtual provides instead of hardcoding
  PersonalCopy-Lite-soundfont (#491421)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.13.2-16
- Some small fixes to ipv6 support from upstream

* Thu Apr  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.13.2-15
- Fix missing prototype compiler warnings

* Sun Mar  9 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.13.2-14
- Fix local ipv6 clients being rejected when running in server mode

* Mon Mar  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.13.2-13
- Merge review fixes (bz 226492)
  - merge patch0 into patch16, drop patch0
  - Make License tag just GPLv2
  - Unify macros usage

* Thu Feb 28 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.13.2-12
- Stop shipping a timidity++-patches package, investigation into the license
  of the included patches has turned up doubts about the rights of the author
  of the midas SGI midi player to release these into the Public Domain
- Instead require PersonalCopy-Lite-soundfont, and point to PCLite.sf2 in
  timidity++.cfg
- Note PersonalCopy-Lite-soundfont also has a PersonalCopy-Lite-patches
  sub-package with the .sf2 file converted to GUS patch format for other
  applications who require timidity++-patches to get GUS format patches, this
  package contains an /etc/timidity.cfg file pointing to the gus patches,
  therefor the timidity++ package now ships a timidty++.cfg instead of a
  timidity.cfg
- Check for /etc/timidity++.cfg before trying /etc/timidity.cfg, see above for
  rationale

* Thu Feb 21 2008 Jindrich Novy <jnovy@redhat.com> 2.13.2-11
- rebuild

* Thu Feb 21 2008 Jindrich Novy <jnovy@redhat.com> 2.13.2-10
- don't free a constant string if -d is specified (#433756),
  thanks to Andrew Bartlett

* Wed Feb 20 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 2.13.2-9
- Add IPv6 support, patch by Milan Zazrivec (bz 198467)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.13.2-8
- Autorebuild for GCC 4.3

* Thu Jan 24 2008 Jindrich Novy <jnovy@redhat.com> 2.13.2-7
- merge review fixes, thanks to Mamoru Tasaka: (#226492)
  - update License tag (still unclear what to do with GUS patches)
  - remove useless unversioned obsolete timidity++-X11
  - substitute /etc with %%{_sysconfdir}
  - enable parallel build
  - preserve timestamps, tar unpacking is no more verbose
  - add docs

* Tue Dec 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.13.2-6
- Disable building of the jack output on powerpc64, as that mysteriously fails
  to build there.

* Mon Dec 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.13.2-5
- Add patches to fix detect and compile of speex and flac outputs
- Add various bugfixes from Debian
- Enable ogg, flac, speex, libao and jack output formats (bz 412431)
- Make libao the default output as libao support pulseaudio directly

* Sat Oct 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.13.2-4
- Split the patches of into a seperate sub package so that they can be used
  by other wavetable midi synthesizers, without dragging in a bunch of unwanted
  dependencies (bz 250735)
- There is no reason to install the icon in /usr/share/pixmaps if it also gets
  installed under /usr/share/icons
- Rewrite autodetection of wether to use esd, aRts or alsa as output patch,
  so that it actually works (bz 200688)

* Thu Oct 11 2007 Jindrich Novy <jnovy@redhat.com> 2.13.2-3
- fix typo in package description (#185328) 
- use RPM_OPT_FLAGS, make debuginfo package usable (#249968),
  thanks to Ville Skitta
- compile with GTK interface (#231745), thanks to Brian Jedsen
  
* Mon Sep 24 2007 Jindrich Novy <jnovy@redhat.com> 2.13.2-2
- spec/license fixes
  
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.13.2-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.2-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13.2-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Aug 26 2004 Thomas Woerner <twoerner@redhat.com> 2.13.0-3
- fixed esd output plugin to not output to stderr on fault (#130633)

* Mon Jul  5 2004 Thomas Woerner <twoerner@redhat.com> 2.13.0-2
- fixed configure options (#127190)

* Thu Jul  1 2004 Thomas Woerner <twoerner@redhat.com> 2.13.0-1
- new version 2.13.0
  - with alsa support (#117024, #123327)
  - working default output (#124774)
  - working ogg output (#124776)
- spec file fixes
- fixed some configure options
- added BuildRequires for ncurses-devel (#125028)

* Sat Jun 19 2004 Alan Cox <alan@redhat.com>
- fixed compiler reported bugs 

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Oct 21 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add %%clean specfile target

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 11 2003 Thomas Woerner <twoerner@redhat.com> 2.11.3-7
- fix for x86_64 and s390x

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec  9 2002 Thomas Woerner <twoerner@redhat.com> 2.11.3-5
- fixed dependency for autoconf

* Mon Jul 22 2002 Than Ngo <than@redhat.com> 2.11.3-4
- build against current libvorbis

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jan 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.11.3-1
- Update to 2.11.3
- Extend the aRts output plugin to support KDE 3.x features
- Fix the dependency mess

* Wed Aug 22 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.10.4-2
- Finally managed to locate free versions of britepno.pat and pistol.pat
  (#50982)

* Sat Apr 14 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.10.4

* Fri Feb 23 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Change timidity.cfg to work perfectly with both the real
  TiMidity++ and the timidity version used in kmidi
- Fix a typo in the GUS drumset #0

* Mon Jan  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Autodetect whether the aRts, esd or dsp backend should
  be used

* Thu Dec  7 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Add aRts (KDE 2.x) backend (Patches #1 and #2)

* Mon Nov 27 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.10.3a2
- Move the config file to the FHSly correct place, /etc/timidity.cfg
- Enable ogg/vorbis support, now that we're shipping it

* Thu Aug 3 2000 Tim Powers <timp@redhat.com>
- rebuilt against libpng-1.0.8

* Wed Aug  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Move instrument files to /usr/share/timidity, where it's actually looking
  for them (Bug #13932)
- 2.9.5 (bugfix release)

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 17 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jun 28 2000 Than Ngo <than@redhat.de>
- FHS fixes
- clean up specfile
- use RPM macros

* Sat Jun 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.9.4

* Wed Jan 19 2000 Tim Powoers <timp@redhat.com>
- bzipped source to conserve space

* Sat Aug 14 1999 Bill Nottingham <notting@redhat.com>
- add a changelog
- strip binaries
