%global fonts font(dejavusans) font(dejavusansmono)

Name:           scorched3d
Version:        44
Release:        38%{?dist}
Summary:        Game based loosely on the classic DOS game Scorched Earth
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://www.scorched3d.co.uk/
Source0:        http://downloads.sourceforge.net/%{name}/Scorched3D-%{version}-src.tar.gz
Source1:        %{name}.desktop
# Fake openal-config as openal-soft doesn't have it
Source2:        openal-config
Patch1:         %{name}-syslibs.patch
Patch2:         %{name}-help.patch
Patch3:         %{name}-freetype-buildfix.patch
Patch4:         %{name}-sys-lua.patch
Patch5:         %{name}-returntype.patch
Patch6:         %{name}-wx3.0.patch
Patch7:         %{name}-lua54.patch
Patch8:         %{name}-fix-hang-on-fast-machines.patch
Patch9:         scorched3d-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  wxGTK-devel SDL_net-devel libGLU-devel
BuildRequires:  expat-devel libvorbis-devel glew-devel fftw-devel libjpeg-devel
BuildRequires:  freetype-devel openal-soft-devel freealut-devel >= 1.1.0-10
BuildRequires:  lua-devel libtool autoconf automake
BuildRequires:  ImageMagick desktop-file-utils
BuildRequires:  fontconfig %{fonts}
Requires:       hicolor-icon-theme opengl-games-utils %{fonts}
# Upstream naming compatibility
Provides:       Scorched3D = %{version}-%{release}

%description
Scorched 3D is a game based on the classic DOS game Scorched Earth
"The Mother Of All Games".  Scorched 3D adds amongst other new
features a 3D island environment and LAN and internet play.  At its
lowest level, Scorched 3D is just an artillery game with two+ tanks
taking turns to destroy opponents in an arena.  Choose the angle,
direction and power of each shot, launch your weapon, and try to blow
up other tanks.  But Scorched 3D can be a lot more complex than that,
if you want it to be.  You can earn money from successful battles and
use it to invest in additional weapons and accessories.  You can play
with up to twenty four other players at a time, mixing computer
players with humans.  There's a variety of changing environmental
conditions and terrains to be dealt with.


%prep
%setup -q -c
pushd scorched
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p0
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p2
touch NEWS AUTHORS ChangeLog
autoreconf -ivf
install -m 755 %{SOURCE2} .
# for %%doc
mkdir apoc
cp -a data/globalmods/apoc/*.txt apoc
# ensure we use the system versions of these
rm src/common/common/snprintf.c
rm src/common/lua/l*.{cpp,h}
rm src/common/lua/print.cpp
popd


%build
pushd scorched
export OPENAL_CONFIG=$PWD/openal-config
%configure --disable-dependency-tracking --datadir=%{_datadir}/%{name}
make %{?_smp_mflags}

# Note that tank2.ico has 48x48 and 32x32 icons embedded in it.
# The 48x48 icon ends up in tank2-0.png
convert data/images/tank2.ico tank2.png
popd


%install
pushd scorched
%make_install
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

ln -f -s $(fc-match -f "%{file}" "sans") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts/dejavusans.ttf
ln -f -s $(fc-match -f "%{file}" "sans:condensed:bold") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts/dejavusconbd.ttf
ln -f -s $(fc-match -f "%{file}" "monospace:bold") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts/dejavusmobd.ttf

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 tank2-0.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
popd

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: http://www.scorched3d.co.uk/mantisbt/view.php?id=209
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">scorched3d.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Turn based 3D artillery game</summary>
  <description>
    <p>
      Scorched 3D is a turn-based 3D artillery game where you take control of a
      tank and attack your opponents in a 3D landscape with a range of weapons.
      It also features some real-time elements allowing you to counter opponents
      attacks, and also features online multiplayer modes.
    </p>
  </description>
  <screenshots>
    <screenshot type="default">http://www.scorched3d.co.uk/phpBB3/gallery/image.php?album_id=8&amp;image_id=61&amp;view=no_count</screenshot>
    <screenshot>http://www.scorched3d.co.uk/phpBB3/gallery/image.php?album_id=3&amp;image_id=4&amp;view=no_count</screenshot>
  </screenshots>
  <url type="homepage">http://www.scorched3d.co.uk/</url>
</application>
EOF


%files
%doc scorched/COPYING scorched/apoc
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 44-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 44-37
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Florian Weimer <fweimer@redhat.com> - 44-34
- Fix C type error in configure script (#2255225)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 44-31
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 44-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 44-29
- Rebuild for glew 2.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 44-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 44-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 44-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Hans de Goede <hdegoede@redhat.com> - 44-25
- Fix FTBFS (rhbz#1865470)
- Fix hang of non-networked games on fast machines

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 44-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 44-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Bruno Wolff III <bruno@wolff.to> - 44-22
- Automate finding font paths during build

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 44-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 44-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 44-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Scott Talbert <swt@techie.net> - 44-18
- Rebuild with wxWidgets 3.0

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 44-17
- Rebuilt for glew 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 44-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 44-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 44-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 44-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 44-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 44-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 44-10
- Rebuild for glew 2.0.0

* Sat Feb 13 2016 Bruno Wolff III <bruno@wolff.to> - 44-9
- Fix thinko in return type

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 44-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Adam Jackson <ajax@redhat.com> 44-7
- Fix freetype include fix

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 44-6
- Rebuild for glew 1.13

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 44-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 44-3
- Add an AppData file for the software center

* Sat Aug 30 2014 Hans de Goede <hdegoede@redhat.com> - 44-2
- Fix build on F-20

* Sat Aug 30 2014 Hans de Goede <hdegoede@redhat.com> - 44-1
- Update to 44 release
- Fix FTBFS (rhbz#1107285)
- Use system lua (rhbz#1077728)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 43.3d-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 43.3d-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 43.3d-10
- rebuilt for GLEW 1.10

* Sun Sep 15 2013 Hans de Goede <hdegoede@redhat.com> - 43.3d-9
- Remove unused docdir stuff (rhbz#993874)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 43.3d-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 43.3d-7
- Compress tarball with xz -e.

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 43.3d-6
- Drop desktop vendor tag.

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 43.3d-5
- rebuild due to "jpeg8-ABI" feature drop

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 43.3d-4
- Rebuild for glew 1.9.0

* Fri Jul 27 2012 Bruno Wolff III <bruno@wolff.to> - 43.3d-3
- Rebuild for libGLEW soname bump

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 43.3d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Bruno Wolff III <bruno@wolff.to> - 43.3d-1
- Lots of minor bugfixes, but incompatible with 43.3.
- 43.3d release announcement: http://www.scorched3d.co.uk/phpBB3/viewtopic.php?t=6594

* Tue Feb 07 2012 Jon Ciesla <limburgher@gmail.com> - 43.3-1
- New upstream.

* Tue Jan 17 2012 Hans de Goede <hdegoede@redhat.com> - 43.2a-7
- Fix building with gcc-4.7

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 43.2a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 06 2011 Bruno Wolff III <bruno@wolff.to> - 43.2a-5
- Fix broken fix for broken fix

* Sun Nov 06 2011 Bruno Wolff III <bruno@wolff.to> - 43.2a-4
- Fix broken palette fix

* Sun Nov 06 2011 Bruno Wolff III <bruno@wolff.to> - 43.2a-3
- Rebuild for libpng 1.5
- Make sure all direct png struct references are through accessors

* Tue Jun 21 2011 Bruno Wolff III <bruno@wolff.to> - 43.2a-2
- Extract a 48x48 png to use as the icon

* Mon Jun 20 2011 Bruno Wolff III <bruno@wolff.to> - 43.2a-1
- Update to upstream 43.2a
- Release anouncement for 43.2a http://www.scorched3d.co.uk/phpBB3/viewtopic.php?t=6340
- Release anouncement for 43.2 http://www.scorched3d.co.uk/phpBB3/viewtopic.php?t=6330
- Release anouncement for 43.1c http://www.scorched3d.co.uk/phpBB3/viewtopic.php?t=6184
- Release anouncement for 43.1b http://www.scorched3d.co.uk/phpBB3/viewtopic.php?t=6129
- Release anouncement for 43 http://www.scorched3d.co.uk/phpBB3/viewtopic.php?t=6128
- Use included png image instead of converting icon

* Mon Jun 20 2011 ajax@redhat.com - 42.1-6
- Rebuild for new glew soname

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 42.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 42.1-4
- rebuilt against wxGTK-2.8.11-2

* Sun Aug 16 2009 Hans de Goede <hdegoede@redhat.com> 42.1-3
- Switch to openal-soft

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 42.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  8 2009 Hans de Goede <hdegoede@redhat.com> 42.1-1
- New upstream release 42.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Hans de Goede <hdegoede@redhat.com> 42-1
- New upstream release 42

* Tue Jan 20 2009 Hans de Goede <hdegoede@redhat.com> 41.3-5
- Adjust font requires for font rename (rh 480471)

* Sat Dec 27 2008 Hans de Goede <hdegoede@redhat.com> 41.3-4
- Replace included vera font with symlinks to dejavu (rh 477454)

* Sun Sep  7 2008 Hans de Goede <hdegoede@redhat.com> 41.3-3
- Fix patch fuzz build failure

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 41.3-2
- Autorebuild for GCC 4.3

* Mon Jan 21 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 41.3-1
- New upstream release 41.3
- Rebuild for new glew

* Wed Jan 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 41.2-1
- New upstream release 41.2
- No longer uses ode so stop BuildRequiring and linking to it

* Fri Jan 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 41.1-2
- Fix compilation with gcc 4.3

* Tue Nov  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 41.1-1
- New upstream release 41.1

* Mon Sep 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 40.1d-6
- Use opengl-games-utils wrapper to show error dialog when DRI is missing

* Tue Aug 28 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 40.1d-5
- Rebuild for new expat 2.0

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 40.1d-4
- Update License tag for new Licensing Guidelines compliance

* Wed Apr 18 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 40.1d-3
- Fix build with new ODE, scorched3d tries to force a double build of (its own
  included version of) ODE, however we use the system version which is compiled
  with single precision. With the new ODE the header files throw an #error
  because this causes both dSINGLE and dDOUBLE to be defined. This is fixed by
  patching scorched3d's configure to not add -DdDOUBLE to the CFLAGS

* Wed Dec 20 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 40.1d-2
- Rebuild for new wxGTK 2.8

* Sat Nov 18 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 40.1d-1
- New upstream release 40.1d

* Fri Nov  3 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 40.1c-2
- Add libvorbis-devel BR so that ogg/vorbis support gets build in

* Thu Nov  2 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 40.1c-1
- New upstream release 40.1c
- Drop 64 bit patch (integrated upstream)
- Don't install our data files in /usr/share/games, but in /usr/share
- Some minor specfile cleanups

* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 40-2
- FE6 Rebuild

* Sat Jul 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 40-1
- New upstream release 40
- Drop many upstreamed patches
- Use system ode library instead of included one

* Thu Feb 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> - 39.1-5
- Patch included apoc mod version 3.1 to the 3.1 version as distributed by
  the ApocHQ servers for a smooth (no download required) experience joining
  apoc-mod using games on the internet. Also not entirely unimportant this
  fixes bz 182166, making the apoc mod actually usuable for local games.

* Mon Feb 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> - 39.1-4
- Bump release and rebuild for new gcc4.1 and glibc.

* Sun Feb 12 2006 <j.w.r.degoede@hhs.nl> - 39.1-3
- fix server crashing with certain landscape types (patch 13)

* Sat Feb 11 2006 <j.w.r.degoede@hhs.nl> - 39.1-2
- upgrade to CVS snapshot of 20050929, as Debian does, but not to
  the newer apoc version as this causes problems playing online (patch 0)
- fix gcc41 compilation (patch 3)
- fix 64 bit compilation (bz 158646) (patch 4)
- fix compile with openal-0.9 (patch 5)
- use htmlview for helpfile viewing instead of hardcoded mozilla,
  run this in background so the game doesn't freeze (patch 6)
- fix all the security issues reported on the fulldisclosure mailinglist:
  http://seclists.org/lists/fulldisclosure/2005/Nov/0079.html
  (bz 161694) (patch 7, 8, 9, 10)
- fix 2 additonal security issues found while fixing the above (patch 11, 12)
- this release also fixes bz 161694

* Sat Oct  8 2005 Ville Skyttä <ville.skytta at iki.fi> - 39.1-1
- 39.1.
- Avoid aclocal >= 1.8 warnings.
- Install icon into icons/hicolor.
- Clean up build dependencies.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 37.2-3
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 37.2-2
- rebuilt

* Mon Aug 16 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:37.2-0.fdr.1
- Update to 37.2.

* Mon Aug  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.33.9.35-0.fdr.1
- First build.
