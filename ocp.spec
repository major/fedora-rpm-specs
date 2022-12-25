#global snapshot 0
%global commit 30b272a5086730ab7f124302ec137ab1fb614e77
%global commitdate 20221223
%global gittag v0.2.101
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		ocp
Version:	0.2.101%{?snapshot:^%{commitdate}git%{shortcommit}}
Release:	1%{?dist}
Summary:	Open Cubic Player for MOD/S3M/XM/IT/MIDI music files

# 2010/08/08: Verified that upstream has removed GPLv3+ gnulib and added
# GPLv2+ license text to all source files.
# Graphics and animations are CC-BY.
License:	GPLv2+ and CC-BY
URL:		https://stian.cubic.org/project-ocp.php
%if 0%{?snapshot}
# Since this project uses git submodules and Github's auto-archive
# feature doesn't archive the submodules, you need to create a git
# snapshot tarball manually with ocp-git-snapshot.sh.
Source0:	ocp-%{commit}.tar.bz2
%else
Source0:	https://stian.cubic.org/ocp/ocp-%{version}.tar.bz2
%endif
Source1:	ftp://ftp.cubic.org/pub/player/gfx/opencp25image1.zip
Source2:	ftp://ftp.cubic.org/pub/player/gfx/opencp25ani1.zip
Source3:	ocp-git-snapshot.sh
Source4:	ocp-bundled-versions.sh
Patch0:		ocp-0.2.95-ini-optimize.patch
Patch1:		ocp-0.2.98-ini-rompaths.patch

BuildRequires:	alsa-lib-devel
BuildRequires:	bzip2-devel
BuildRequires:	cjson-devel
BuildRequires:	desktop-file-utils
BuildRequires:	flac-devel
BuildRequires:	freetype-devel
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	libdiscid-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXxf86vm-devel
BuildRequires:	make
BuildRequires:	ncurses-devel
BuildRequires:	perl-interpreter
BuildRequires:	SDL2-devel
BuildRequires:	texinfo
BuildRequires:	unifont-fonts
BuildRequires:	unzip
BuildRequires:	xa
BuildRequires:	zlib-devel

# For the hicolor icon directories
Requires:	hicolor-icon-theme
Requires:	unifont-fonts

# Bundled code
Provides:	bundled(timidity++) = 2.15.0
Provides:	bundled(libsidplayfp) = 2.5.0a
Provides:	bundled(adplug) = 2.3.4-beta
Provides:	bundled(libbinio) = 1.5
Provides:	bundled(reSID) = 1.0-pre2
Provides:	bundled(libexsid) = 2.1

%description
Open Cubic Player is a music file player ported from DOS that supports
Amiga MOD module formats and many variants, such as MTM, STM, 669,
S3M, XM, and IT.  It is also able to render MIDI files using sound
patches and play SID, OGG Vorbis, FLAC, and WAV files.  OCP provides a
nice text-based interface with several text-based and graphical
visualizations.


%prep
%if 0%{?snapshot}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif
unzip %{SOURCE1}
mv license.txt license-images.txt
unzip %{SOURCE2}
mv license.txt license-videos.txt


%build
%configure --with-x11 \
	   --with-alsa \
	   --without-coreaudio \
	   --without-oss \
	   --with-lzw \
	   --with-lzh \
	   --with-flac \
	   --without-sdl \
	   --with-sdl2 \
	   --with-mad \
	   --with-libiconv=auto \
	   --with-timidity-default-path=/etc \
	   --with-unifontdir-ttf=/usr/share/fonts/unifont \
	   --without-unifont-csur-ttf \
	   --with-dumptools \
	   --docdir=%{_pkgdocdir} \
#	   --with-debug
# Makefiles are not SMP-clean
%global _smp_mflags -j1
%make_build


%install
mkdir -p %{buildroot}/etc
%make_install

# mv config to /etc (ocp will search here if it isn't found in the original location)
mv %{buildroot}%{_datadir}/%{name}/etc/ocp.ini %{buildroot}/etc/ocp.ini
rmdir %{buildroot}%{_datadir}/%{name}/etc

# remove info/dir
rm -f %{buildroot}/%{_infodir}/dir

# rename desktop file to name.desktop to match packaging guidelines
mv %{buildroot}%{_datadir}/applications/*opencubicplayer.desktop \
   %{buildroot}%{_datadir}/applications/ocp.desktop
desktop-file-install --add-category="Audio" \
		     --add-category="Midi" \
		     --add-category="Player" \
		     --dir=%{buildroot}%{_datadir}/applications \
		     --delete-original \
		     %{buildroot}%{_datadir}/applications/ocp.desktop

# install images and animations
cp -p CPPIC*.TGA CPANI*.DAT %{buildroot}%{_datadir}/%{name}/data

# remove COPYING from buildroot/docdir as it will be installed as a license file below
rm -f %{buildroot}%{_pkgdocdir}/COPYING


%files
%license COPYING license-images.txt license-videos.txt
# install already installs the docs here for us
%doc %{_pkgdocdir}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_bindir}/ocp
%{_bindir}/ocp-curses
%{_bindir}/ocp-sdl2
%{_bindir}/ocp-vcsa
%{_bindir}/ocp-x11
%{_bindir}/dump*
%{_infodir}/ocp.info*
%{_mandir}/man1/ocp.1*
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/64x64/apps/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*ocp.desktop
%config(noreplace) /etc/ocp.ini


%changelog
* Fri Dec 23 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.101-1
- update to 0.2.101

* Sun Sep 25 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.100-1
- update to 0.2.100

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.2.99-3
- Rebuilt for flac 1.4.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.99-1
- update to 0.2.99
- simplify ocp-git-shapshot.sh to automatically checkout the correct
  submodule branches

* Sat Jun 11 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.98^20220610gitfbe858b-2
- patch ocp.ini to set ROM paths for libsidplayfp (rhbz#2086434)

* Fri Jun 10 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.98^20220610gitfbe858b-1
- add ocp-git-snapshot.sh shell script as Source3 to create git snapshot tarball
- add ocp-bundled-versions.sh shell script as Source4 to find bundled code versions
- document bundled reSID and libexsid versions
- update to git snapshot
- fixes several issues:
  Parsing RIFF files could randomly crash (#58)
  Delay FX command should use the last note given in the channel (#59)
  Going from wurfel to text mode caused OCP to freeze (#61)
  Does not close after typing Ctrl-C or clicking the window close box (#62, rhbz#2086433)

* Sat Jun 04 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.98-2
- Reenable X11 which will be used by default.
- Run ocp-sdl2 to try the SDL2 version but there are various issues:
  https://github.com/mywave82/opencubicplayer/issues/60

* Thu Jun 02 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.98-1
- update to 0.2.98

* Mon May 09 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.97^20220508git81214c8-1
- update to git snapshot

* Fri May 06 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.97-2
- Patch Makefile to simplify sub-make usage and attempt to allow parallel build

* Tue May 03 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.97-1
- update to 0.2.97
- Fixes failure to find adplug/opl.h

* Mon May 02 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.96-1
- update to 0.2.96
- New bundled code: libbinio and adplug
- Workaround for failure to find adplug/opl.h

* Sat Mar 26 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.95-1
- update to 0.2.95
- disable X11, OSS, and SDL
- enable SDL2
- patch ocp.ini to remove references to drivers that are not packaged
- add dumptools: dumpahx dumpay dumpmidi dumpmod dumps3m dumpsid dumpstm
- build with unversioned private datadir and libdir
- Provides bundled(libsidplayfp) and bundled(timidity++)
- mark license files
- spec file cleanups and modernization

* Sat Mar 26 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.1-2
- Remove possibility to build i386 assembly version

* Thu Mar 17 2022 Charles R. Anderson <cra@alum.wpi.edu> - 0.2.1-1
- New upstream on github
- Update to 0.2.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.31.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.30.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.29.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Robert Scheck <robert@fedoraproject.org> - 0.1.22-0.28.git849cc42
- Rebuilt for adplug 2.3.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.27.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 0.1.22-0.26.git849cc42
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Thu Jan 30 2020 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.25.git849cc42
- patch out configure gcc version check

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.24.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.23.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.22.git849cc42
- Fix broken %%post section caused by rhbz#1663320 commit 8ea18fad9af93c28dee92f79ed97dd7de80695dc
- Quote macro in comment

* Tue Feb 05 2019 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.21.git849cc42
- Patch configure to accept gcc 9

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.20.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.19.git849cc42
- add BR gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.18.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 27 2018 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.17.git849cc42
- Patch configure to accept gcc 8

* Sun Feb 18 2018 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.16.git849cc42
- add BR gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.15.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.22-0.14.git849cc42
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.13.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.12.git849cc42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.11.git849cc42
- Patch configure to accept gcc 7

* Mon Dec 05 2016 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.10.git849cc42
- bz#1400073: Re-enable libmad for mp3 support

* Fri Feb 05 2016 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.9.git849cc42
- Update to latest git snapshot
- Patch configure to accept gcc 6 (rhbz#1305102)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-0.8.gite62ae52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 31 2015 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.7.gite62ae525
- Update to latest git snapshot
- Rework spec

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.22-0.6.20150224gita07bf5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.22-0.5.20150224gita07bf5d
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 24 2015 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.4.20150224gita07bf5d
- update to current git snapshot
- remove timidity-parse-config.patch, no longer needed

* Mon Feb 23 2015 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.3.20150223gitbceb98e
- re-add pat-use-first-sample.patch, still needed
- remove docdir.patch, no longer needed

* Mon Feb 23 2015 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.2.20150223gitbceb98e
- update timidity-parse-config.patch

* Mon Feb 23 2015 Charles R. Anderson <cra@wpi.edu> - 0.1.22-0.1.20150223gitbceb98e
- update to current git snapshot

* Fri Dec 27 2013 Charles R. Anderson <cra@wpi.edu> - 0.1.21-2
- allow multi-sample PAT files by only using the first sample

* Fri Dec 27 2013 Charles R. Anderson <cra@wpi.edu> - 0.1.21-1
- update to 0.1.21
- fix parsing timidity.cfg with absolute paths to patch files

* Tue Aug 06 2013 Charles R. Anderson <cra@wpi.edu> - 0.1.20-9
- Drop version from docdir (rhbz#993999)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-8.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Jon Ciesla <limburgher@gmail.com> - 0.1.20-8.5
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-8.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Adam Jackson <ajax@redhat.com> 0.1.20-8.2
- Rebuild without libsidplay, dropped from F18.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 05 2011 Charles R. Anderson <cra@wpi.edu> 0.1.20-8
- fix fcontext regexp for /usr/bin/ocp-[0-9].*

* Sun Jun 05 2011 Charles R. Anderson <cra@wpi.edu> 0.1.20-7
- also apply unconfined_execmem_exec_t to /usr/bin/ocp-.*
- fix ocp-0.1.20-no-i386-asm.patch to actually work at all

* Sun Jun 05 2011 Charles R. Anderson <cra@wpi.edu> 0.1.20-6
- remove textrel_shlib_t fcontexts on non-i386asm version and on package removal
- update gtk-update-icon-cache scriptlets to latest guidelines
- update upstream URL

* Sat Jun 04 2011 Charles R. Anderson <cra@wpi.edu> 0.1.20-5
- conditionalize compiling the i386 assembly version, and default to off:
  --with-i386asm
- only set SELinux fcontexts when compiling i386 assembly version
- fix changelog days

* Sat Jun 04 2011 Charles R. Anderson <cra@wpi.edu> 0.1.20-4
- correct fcontext regexps and restorecon glob

* Fri Jun 03 2011 Charles R. Anderson <cra@wpi.edu> 0.1.20-3
- fix parsing timidity.cfg
- set SELinux file context textrel_shlib_t on libraries which contain non-PIC
  i386 assembly so we don't need allow_execmod (32-bit i386 build only)

* Wed Jun 01 2011 Charles R. Anderson <cra@wpi.edu> 0.1.20-2
- remove --with-debug since it overrides optflags (bz#625884)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 08 2010 Charles R. Anderson <cra@wpi.edu> 0.1.20-1
- update to 0.1.20
- upstream license audit has been performed:
  - all components are GPLv2+ (or compatible)
  - license text added to all source files
  - images and animation data remain under CC-BY

* Sun Apr 04 2010 Charles R. Anderson <cra@wpi.edu> 0.1.19-0.5.20100401snap
- ocp-snapshot-20100401
- remove obsoleted patches
- add image and animation data which is under CC Attribution 3.0 license

* Fri Feb 12 2010 Charles R. Anderson <cra@wpi.edu> 0.1.19-0.4.20100110snap
- add patch to fix crash in Scopes (o) and Phase (b) visualization modes.

* Sat Feb 06 2010 Charles R. Anderson <cra@wpi.edu> 0.1.19-0.3.20100110snap
- patch Makefiles to remove hardcoded -O flags

* Mon Feb 01 2010 Charles R. Anderson <cra@wpi.edu> 0.1.19-0.2.20100110snap
- --with-debug
- patch configure to use -O0 when --with-debug is specified

* Tue Jan 19 2010 Charles R. Anderson <cra@wpi.edu> 0.1.19-0.1.20100110snap
- 0.1.19-0.1.20100110snap

* Tue Jan 19 2010 Charles R. Anderson <cra@wpi.edu> 0.1.18-1
- 0.1.18
- enable SDL: ocp-sdl

* Tue Oct 06 2009 Charles R. Anderson <cra@wpi.edu> 0.1.17-20090926snap
- snapshot 20090926
- adds ocp-curses, ocp-sdl, ocp-vcsa, and ocp-x11 binaries

* Tue Oct 06 2009 Charles R. Anderson <cra@wpi.edu> 0.1.17-1
- 0.1.17-1

* Sat Sep 12 2009 Charles R. Anderson <cra@wpi.edu> 0.1.17-0.20090730cvs
- snapshot 20090730

* Mon Mar 02 2009 Charles R. Anderson <cra@wpi.edu> 0.1.16-1
- 0.1.16-1
- upstreamed patches: alsa condmad docdir gcc43 info-dir symlink
- upstreamed: move icons to hicolor theme
- remove info/dir from buildroot
- patch configure.ac to correctly find byteswap.h
- no longer BR libid3tag

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 10 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-4
- Add missing Requires: hicolor-icon-theme for the hicolor icon
  directories
- remove wmconfig bits in a more succinct way
- rename ultrafix.sh to ocp-ultrafix.sh to prevent possible conflicts
- add comments about the applied patches and their upstream status

* Sun Nov 02 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-3
- fix condmad.patch: add HAVE_MAD & HAVE_ID3TAG to Rules.make.in
- update desktop file patch (keep Terminal=false change, 
  use themed icon name "ocp" rather than path)
- move icons to hicolor theme, call gtk-update-icon-cache in %%post(un)

* Tue Jun 24 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-2
- don't need redundant BR libogg-devel
- remove ExlusiveArch, try build on all arches
- alphabetize BR's on separate lines
- enable oss and id3tag support
- remove obsolete wmconfig desktop file
- fix Makefile to install standard documentation files under /usr/share/doc/
- fix Makefile to create relative symlink instead of absolute
- use --delete-original on desktop-file-install
- add @dircategory and @direntry to info file so it can be installed

* Tue Jun 24 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-1.2
- BR texinfo for /usr/bin/makeinfo

* Tue Jun 24 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-1.1
- create /usr/share/doc/%%{name}-%%{version} in buildroot

* Tue Jun 24 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-1
- Initial Fedora Package submission
- clean up summary, description and comments
- don't try to install-info since there is no directory entry

* Tue Jun 24 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-0.8cra
- No longer BR libid3tag-devel

* Sun Jun 22 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-0.7cra
- conditionalize mp3 support and disable it
- explicitly disable coreaudio

* Fri Jun 20 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-0.6cra
- BR libXext-devel alsa-lib-devel

* Tue Jun 17 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-0.5cra
- disable ALSA_DEBUG

* Tue Jun 17 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-0.4cra
- Enable ALSA_DEBUG
- workaround pulseaudio alsa plugin bug (snd_pcm_hw_params_any returns > 0)

* Sun Jun 08 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-0.3cra
- gcc 4.3 patch
- install-info in post/preun
- rename desktop file to fedora-ocp.desktop
- use desktop-file-install

* Sun Jun 08 2008 Charles R. Anderson <cra@wpi.edu> 0.1.15-0.2cra
- BR libid3tag-devel libXxf86vm-devel
- use proper macros in file section
- explicitly enable configure flags, disable OSS
- License: GPL+ because no specific version is mentioned in the docs
  or source code.
- Patch desktop file to specify UTF-8 encoding
