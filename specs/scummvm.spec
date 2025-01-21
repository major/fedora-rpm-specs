# Filter provides of private plugins.
%if 0%{?fedora} || 0%{?rhel} >= 7
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$
%else
%{?filter_setup:
%filter_provides_in %{_libdir}/%{name}/.*\.so$
%filter_setup
}
%endif

# Url to upstream GitHub repo.
%global git_url https://github.com/%{name}/%{name}

%global org_name org.scummvm.scummvm

Name:		scummvm
Version:	2.8.1
Release:	3%{?dist}
Summary:	Interpreter for several adventure games
# OFL only used by font files (distributed as fonts.dat)
License:	GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-OFL and LicenseRef-Callaway-MIT and ISC and Catharon AND Apache-2.0
URL:		https://www.scummvm.org/
Source0:	https://www.scummvm.org/frs/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0005:	scummvm-2.1.1-ftbfs-use-bfd-linker-on-x86.patch
# Compile fix for F40 with GCC 14
# https://github.com/scummvm/scummvm/commit/a04bb51bf5984896ba1b9c9fadef0b1f7ae73f8b
Patch0006:	0001-ICB-compile-fix-for-GCC-14.patch

BuildRequires:	make
BuildRequires:	libappstream-glib speech-dispatcher-devel alsa-lib-devel
BuildRequires:	SDL2-devel libvorbis-devel flac-devel zlib-devel
BuildRequires:	fluidsynth-devel desktop-file-utils libtheora-devel
BuildRequires:	libpng-devel freetype-devel libjpeg-devel libmad-devel
BuildRequires:	readline-devel libcurl-devel libmpeg2-devel gtk3-devel
BuildRequires:	gcc-c++ giflib-devel glew-devel
BuildRequires:	libmikmod-devel libvpx-devel sonivox-devel

%ifarch %{ix86}
BuildRequires:	nasm
%endif
Requires:	hicolor-icon-theme
Requires:	%{name}-data = %{version}-%{release}

Provides:	bundled(mt32emu) = 2.5.1
# Lua is bundled twice: modified version 5.1 and 3.1
Provides:	bundled(lua)
Provides:	bundled(ags)

%description
ScummVM is a program which allows you to run certain classic graphical
point-and-click adventure games, provided you already have their
data files.

ScummVM supports many adventure games, including LucasArts SCUMM games
(such as Monkey Island 1-3, Day of the Tentacle, Sam & Max, ...),
many of Sierra's AGI and SCI games (such as King's Quest 1-6,
Space Quest 1-5, ...), Discworld 1 and 2, Simon the Sorcerer 1 and 2,
Beneath A Steel Sky, Lure of the Temptress, Broken Sword 1 and 2,
Flight of the Amazon Queen, Gobliiins 1-3, The Legend of Kyrandia 1-3,
many of Humongous Entertainment's children's SCUMM games (including
Freddi Fish and Putt Putt games) and many more.

The complete list can be found on ScummVM's compatibility page:
http://scummvm.org/compatibility/%{version}/


%package data
Summary:	Data files for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description data
This package contains the data files for %{name}.


%prep
%autosetup -p 1


%build
# LTO combined with -Wl,--gdb-index and the Gold linker sometimes triggers
# occasional faults in the Gold linker.  We have already decided to deprecate
# the Gold linker so it does not seem worth the effort to reproduce, reduce,
# analyze # and report the heisenbug in Gold.
# Disable LTO
%define _lto_cflags %{nil}

# workaround FTBFS on i386
%ifarch %{ix86}
export LDFLAGS="-fuse-ld=bfd"
%endif

# The configure script shall ignore the parameter for the --host option
#passed by %%configure.
export CONFIGURE_NO_HOST=true

# The disables are so that these don't accidently get build in when rebuilding
# on a system with the necesarry deps installed.
%configure					\
	--datadir=%{_datadir}/%{name}		\
	--default-dynamic			\
	--enable-all-engines			\
	--enable-plugins			\
	--enable-release			\
	--enable-text-console			\
	--enable-translation			\
	--enable-verbose-build			\
	--enable-cloud				\
	--enable-libcurl			\
	--enable-mpeg2				\
	--with-freetype2-prefix=%{_prefix}
%make_build


%check
# Check the AppData add-on to comply with guidelines.
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.xml


%install
%make_install
# Remove doc files we want to include with %%doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--set-key=Keywords --set-value="game;emulator;adventure;adventuregame;" \
	--set-key=StartupWMClass --set-value="scummvm" \
	--add-category=Emulator \
	dists/%{org_name}.desktop

# Plugins should be executable.
find $RPM_BUILD_ROOT%{_libdir} -type f -name '*.so' | xargs chmod -Rc 0755

%files
%license COPYING LICENSES/COPYING.*
%doc AUTHORS README.md NEWS.md TODO doc/{cz,da,de,es,fr,it,no-nb,QuickStart,se}
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{org_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{org_name}.svg
%{_datadir}/pixmaps/%{org_name}.xpm
%{_metainfodir}/%{org_name}.metainfo.xml


%files data
%{_datadir}/%{name}/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Christian Krause <chkr@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1 (#2254942)
- Fix FTBFS (#2261685)
- Adjust filenames
- Set StartupWMClass in desktop file in order to enable the window manager
  to reference the correct desktop file (e.g. needed for the
  task switcher to show the correct application icon)
- Add upstreamed patch to fix compile issue with GCC 14
- Update license tag
- Add BR: libmikmod-devel, libvpx-devel and sonivox-devel

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 01 2023 Christian Krause <chkr@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1 (#2223153)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 16 2023 Christian Krause <chkr@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0 (#2170137)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 06 2022 Christian Krause <chkr@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1 (#2135801)

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.6.0-2
- Rebuilt for flac 1.4.0

* Sat Aug 13 2022 Christian Krause <chkr@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0 (#2107935)
- Flag bundled ags (#2089196)
- Update license tag

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 2.5.1-3
- Rebuild for glew 2.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Christian Krause <chkr@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1 (#2035598)
- Remove patches already included upstream

* Sat Dec 11 2021 Christian Krause <chkr@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0 (#2009713)
- Remove patches already included upstream
- Add upstream patch to allow building without tinygl
- Flag bundled mt32emu library (#1991802)
- Flag bundled lua (#1077764)
- Update License tag and add more %%license files
- Add BR: giflib-devel and glew-devel

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 04 2021 Christian Krause <chkr@fedoraproject.org> - 2.2.0-4
- Rebuilt for fluidsynth soname bump (#1976457)
- Add upstream patches to support fluidsynth 2.2
- Add upstream patch to fix compile issue on non-x86 architectures
- Correct LGPLv2+ license tag

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Christian Krause <chkr@fedoraproject.org> - 2.2.0-2
- Update License tag and add more %%license files

* Sun Oct 18 2020 Christian Krause <chkr@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0 (#1819020)
- Remove patches already included upstream
- Update patch to disable LTO
- Use new directory for AppData files
- Add gtk3-devel to BuildRequires

* Mon Sep 14 2020 Than Ngo <than@redhat.com> - 2.1.1-11
- Fix FTBFS

* Wed Sep 09 2020 Than Ngo <than@redhat.com> - 2.1.1-10
- Rebuilt

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jeff Law <law@redhat.com> - 2.1.1-7
- Disable LTO

* Tue May 26 2020 Jeff Law <law@redhat.com> - 2.1.1-6
- Fix configure test compromised by LTO

* Sat Feb 22 2020 Björn Esser <besser82@fedoraproject.org> - 2.1.1-5
- Update patch for properly using LDFLAGS

* Fri Feb 21 2020 Björn Esser <besser82@fedoraproject.org> - 2.1.1-4
- Add patch from upstreamed PR to add compatibility for RPM's configure macro

* Tue Feb 18 2020 Björn Esser <besser82@fedoraproject.org> - 2.1.1-3
- Export build-flags in a more elaborated way
- Use GitHub url for patches from upstream

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.1.1-2
- Rebuild against fluidsynth2

* Sat Feb 08 2020 Christian Krause <chkr@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1 (#1792610)
- Remove patch already included upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Christian Krause <chkr@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 (#1758740)
- Remove patches already included upstream
- Adjust names of doc files
- Add BR: alsa-lib-devel, needs to be referenced explicitly now
- Add BR: speech-dispatcher-devel to enable text-to-speech support
- Add patch to fix a build issue when text-to-speech support is enabled

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Christian Krause <chkr@fedoraproject.org> - 2.0.0-6
- Enable mpeg2 video support (BZ #1710796)
- Switch to SDL2 (BZ #1716769)

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-5
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.0.0-3
- rebuilt to fix FTBFS rhbz #1606321

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Christian Krause <chkr@fedoraproject.org> - 2.0.0-1
- update to latest upstream (BZ 1536755)
- add upstream patch for CVE-2017-17528 (and one follow-up patch, BZ 1528426,
  BZ 1528425)
- turn off virtual keyboard (the keyboard pack files are not installed
  and scummvm doesn't have a global search path for them on platform sdl/posix)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.0-7
- Remove obsolete scriptlets

* Sun Aug 20 2017 Björn Esser <besser82@fedoraproject.org> - 1.9.0-6
- Properly apply compiler / linker flags
- Add BR: libmad-devel for MP3 support
- Add BR: readline-devel for text-console support
- Build game engines as dynamic plugins
- Build with C++11
- Enable several optional features
- Split data into noarch sub-package
- Move COPYING to %%license

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.9.0-3
- re-enable MP3 support (1400069)

* Mon Nov 07 2016 Christian Krause <chkr@fedoraproject.org> - 1.9.0-2
- add keywords to desktop file
- add category Emulator to desktop file
- remove outdated sed statements

* Mon Oct 31 2016 Christian Krause <chkr@fedoraproject.org> - 1.9.0-1
- update to latest upstream
- validate and install appdata file

* Sat May 21 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.8.1-1
- drop patch - fixed upstream
- update to latest upstream

* Sat Mar 12 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.8.0-1
- update url/download links
- cleanup specfile
- drop patch - fixed upstream
- update to latest upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Jan 03 2015 Christian Krause <chkr@fedoraproject.org> - 1.7.0-2
- remove freetype patch, BZ 1161963 was fixed
- add upstream patch to support aarch64 (BZ 926503)
- fix typo in %%description (BZ 1164474)

* Sun Nov 09 2014 Christian Krause <chkr@fedoraproject.org> - 1.7.0-1
- new upstream release (BZ 1144386)
- added patch to work-around the currently broken freetype-config script
  (BZ 1161963)
- added libjpg-devel to BuildRequires

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 01 2013 Christian Krause <chkr@fedoraproject.org> - 1.6.0-1
- new upstream release
- added freetype-devel, libtheora-devel and libpng-devel to BuildRequires
- drop nostrip patch - fixed upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 28 2012 Christian Krause <chkr@fedoraproject.org> - 1.5.0-1
- new upstream release
- use shipped SVG icon instead of manually extracted PNG files
- add shipped XPM icon for openbox compatibility
- update Icon Cache scriptlets

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Christian Krause <chkr@fedoraproject.org> - 1.4.1-1
- new upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Christian Krause <chkr@fedoraproject.org> - 1.4.0-2
- update description

* Thu Nov 10 2011 cooly@gnome.eu.org - 1.4.0-1
- new upstream release

* Mon Jul 25 2011 Christian Krause <chkr@fedoraproject.org> - 1.3.1-1
- new upstream release

* Wed May 25 2011 Lucian Langa <cooly@gnome.eu.org> - 1.3.0-1
- new upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2.1-1
- new upstream release

* Fri Oct 15 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2.0-1
- update nostrip patch
- drop patch1 - fixed upstream
- new upstream release

* Fri Sep 17 2010 Lucian Langa <cooly@gnome.eu.org> - 1.1.1-2
- update description
- add enable-release flag

* Mon May 03 2010 Lucian Langa <cooly@gnome.eu.org> - 1.1.1-1
- new upstream release

* Mon Apr 05 2010 Lucian Langa <cooly@gnome.eu.org> - 1.1.0-1
- new upstream release

* Sun Apr  4 2010 Hans de Goede <hdegoede@redhat.com> - 1.0.0-2
- When starting lure from the cmdline (as the lure fedora package .desktop
  file does) prefer the VGA version over the EGA version

* Wed Nov 25 2009 Lucian Langa <cooly@gnome.eu.org> - 1.0.0-1
- drop patch1 - fixed upstream
- update patch0 to 1.0.0 release
- new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Lucian Langa <cooly@gnome.eu.org> - 0.13.1-1
- new upstream release

* Mon Mar 09 2009 Lucian Langa <cooly@gnome.eu.org> - 0.13.0-1
- new upstream release
- update patch0
- drop installing uneeded theme files
- drop vendor from desktop file; fix icon entry

* Thu Feb 26 2009 Lucian Langa <cooly@gnome.eu.org> - 0.12.0-3
- add patch1 for gcc44 fixes

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 01 2008 Lucian Langa <cooly@gnome.eu.org> - 0.12.0-1
- new upstream 0.12.0
- drop 0.11.0 patches (fixed upstream)
- drop 0.9.0 patch (fixed upstream)

* Sat Mar  8 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.11.1-2
- Various bugfixes to lure sound support
- Enable libfluidsynth support 

* Sat Mar  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.11.1-1
- New upstream version 0.11.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.11.0-2
- Autorebuild for GCC 4.3

* Wed Jan 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.11.0-1
- New upstream version 0.11.0
- Drop no longer needed gcc 4.3 patch

* Sat Jan 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.0-3
- Fix compilation with gcc 4.3

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.0-2
- Update License tag for new Licensing Guidelines compliance

* Thu Jun 21 2007 Matthias Saou <http://freshrpms.net/> 0.10.0-1
- Update to 0.10.0, since Hans is away for a few days ;-)
- Install icons the same way as the theme, and preserve timestamps.
- Use a downloads.sf.net source URL.
- Remove two no longer needed patches (gcc41 and new-flac).

* Thu Feb 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-3
- Take patches from svn for new flac support and rebuild for new flac
- Fix (remove) execstack usage

* Sat Nov 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-2
- Fix desktop-file so that scummvm doesn't end up in the "Other" menu under
  gnome (bug 215097)

* Sat Nov  4 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9.1-1
- New upstream release 0.9.1
- Prepare for inclusion into FE
- Remove mp3 support (the same files are also available in ogg format)
- Remove mpeg2 video support (problem, but only for one game I will
  request upstream to add theora support)

* Sun Oct 29 2006 Matthias Saou <http://freshrpms.net/> 0.9.0-1
- Update to 0.9.0.
- Spec file cleanup.
- Add datadir patch from upstream in order to include themes.

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Mon Feb 06 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.8.2-0.lvn.1
- version upgrade

* Mon Jan 30 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.8.1-0.lvn.1
- version upgrade

* Thu Dec 08 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.8.0-0.lvn.2
- fix #693 (desktop entry)
- beautify desktop-file-install

* Sat Oct 29 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.8.0-0.lvn.1
- version upgrade

* Mon Jun 20 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.1-0.lvn.3
- add --disable--mt32emu switch to fix build with gcc4

* Mon May 30 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.1-0.lvn.2
- fix x86_64 build

* Thu Mar 31 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.1-0.lvn.1
- Version Upgrade

* Tue Feb 22 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.0-0.lvn.3
- add nasm <-> x86_64

* Tue Feb 22 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.0-0.lvn.2
- fixed #371 (bild on non ix86 - David Woodhouse)

* Fri Dec 24 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.7.0-0.lvn.1
- added AUTHORS and TODO

* Thu Dec 23 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- added off. 0.7.0 sources

* Sun Dec 19 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- upgrade to 0.7.0 cvs (20041219), prep. for 0.7.0
- added more BuildRequires
- if without-alsa is defined actually disable alsa via configure

* Thu Nov 25 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.6.1b-0.lvn.1
-upgrade to 0.6.1b

* Thu May 27 2004 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.6.0-0.lvn.1
- upgrade to 0.6.0

* Thu Oct 02 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.5.1-0.fdr.6
- removed #--- lines

* Tue Sep 16 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.5.1-0.fdr.5
- added ${RPM_OPT_FLAGS}

* Mon Sep 08 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.5.1-0.fdr.4
- added libvorbis-devel

* Tue Sep 02 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.5.1-0.fdr.3
- upgrade to new minor version

* Wed Aug 06 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.5.0-0.fdr.2
- upgrade to new major version

* Fri Aug 01 2003 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:0.4.1-0.fdr.1
- Initial RPM release.
