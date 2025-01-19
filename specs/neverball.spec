Name:           neverball
Version:        1.6.0
Release:        33%{?dist}

Summary:        Common files for neverball and neverputt

License:        GPL-2.0-or-later
URL:            http://neverball.org
Source0:        http://neverball.org/neverball-%{version}.tar.gz
Source1:        neverball.desktop
Source2:        neverputt.desktop
#Patch0:         neverball-1.5.4-dso.patch
#Patch1:		neverball-1.5.4-sizeof.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL2_image-devel, SDL2_ttf-devel, SDL2_mixer-devel
BuildRequires:  freetype-devel, desktop-file-utils, zlib-devel
BuildRequires:  libGL-devel, libjpeg-devel, libpng-devel, physfs-devel
BuildRequires:  gettext, libvorbis-devel

%description
This package provides common files needed by both the Neverball and Neverputt
games.

%package neverputt
Summary: Minigolf like game
Requires: opengl-games-utils dejavu-sans-fonts
Requires: %{name}%{?_isa} = %{version}-%{release}

%description neverputt
A hot-seat multiplayer miniature golf game, built on the physics and graphics
engine of Neverball.

%package neverball
Summary: Roll a ball through an obstacle course
Requires: opengl-games-utils dejavu-sans-fonts
Requires: %{name}%{?_isa} = %{version}-%{release}

%description neverball
Tilt the floor to roll a ball through an obstacle course within the
given time.  If the ball falls or time expires, a ball is lost.

Collect 100 coins to save your progress and earn an extra ball.  Red
coins are worth 5.  Blue coins are worth 10.

%prep
%setup -q
#%patch0 -p0
#%patch1 -p0

%build
make CFLAGS="$RPM_OPT_FLAGS -ansi `sdl2-config --cflags` -fcommon" DATADIR=%{_datadir}/%{name} %{?_smp_mflags}

%install
install -p -D -m0755 neverball $RPM_BUILD_ROOT/%{_bindir}/neverball
install -p -D -m0755 neverputt $RPM_BUILD_ROOT/%{_bindir}/neverputt
install -p -d -m0755 $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -ap  data/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/

# install proper icons
install -p -D -m0644 dist/neverball_128.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/128x128/apps/neverball.png
install -p -D -m0644 dist/neverball_16.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/neverball.png
install -p -D -m0644 dist/neverball_24.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/24x24/apps/neverball.png
install -p -D -m0644 dist/neverball_256.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/neverball.png
install -p -D -m0644 dist/neverball_32.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/neverball.png
install -p -D -m0644 dist/neverball_48.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/neverball.png
install -p -D -m0644 dist/neverball_512.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/512x512/apps/neverball.png
install -p -D -m0644 dist/neverball_64.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/neverball.png
install -p -D -m0644 dist/neverputt_128.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/128x128/apps/neverputt.png
install -p -D -m0644 dist/neverputt_16.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/neverputt.png
install -p -D -m0644 dist/neverputt_24.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/24x24/apps/neverputt.png
install -p -D -m0644 dist/neverputt_256.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/neverputt.png
install -p -D -m0644 dist/neverputt_32.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/neverputt.png
install -p -D -m0644 dist/neverputt_48.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/neverputt.png
install -p -D -m0644 dist/neverputt_512.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/512x512/apps/neverputt.png
install -p -D -m0644 dist/neverputt_64.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/neverputt.png

# Use system fonts instead of bundling our own
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/ttf/DejaVuSans-Bold.ttf
ln -s %{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/ttf/DejaVuSans-Bold.ttf

ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/neverball-wrapper
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/neverputt-wrapper

desktop-file-install \
  --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
%{SOURCE1}

desktop-file-install \
  --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
%{SOURCE2}

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
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: http://forum.nevercorner.net/viewtopic.php?pid=31145
SentUpstream: 2014-09-22
-->
<application>
  <id type="desktop">neverball.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Tilt the floor to roll a ball through an obstacle course before time runs
      out.
      Neverball is part puzzle game, part action game, and entirely a test of
      skill.
    </p>
    <p>
      The current version includes 141 Neverball levels and 134 Neverputt holes.
    </p>
  </description>
  <url type="homepage">http://neverball.org/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/neverball/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/neverball/b.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/neverball/c.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/neverputt.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 William Moreno Reyes <williamjmorenor@gmail.com> -->
<!--
BugReportURL: http://forum.nevercorner.net/viewtopic.php?pid=31149#p31149
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">neverputt.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Guide a ball around the obstacles tilting the floor</summary>
  <description>
    <p>
      In Neverball you must guide a ball around the obstacle tilting the floor
      before the time is over.
    </p>
    <p>
      Neverball is very similar to Super Monkey Ball, you must guide the ball to
      the end point of each level getting all coins as you can.
    </p>
  </description>
  <url type="homepage">http://neverball.org</url>
</application>
EOF

%files
%defattr(0644,root,root,0755)
%doc README.md LICENSE.md doc/
%{_datadir}/%{name}/

%files neverputt
%doc LICENSE.md
%attr(0755,root,root) %{_bindir}/neverputt
%attr(0755,root,root) %{_bindir}/neverputt-wrapper
%{_datadir}/appdata/neverputt.appdata.xml
%{_datadir}/applications/neverputt.desktop
%{_datadir}/icons/hicolor/*/apps/neverputt.png

%files neverball
%doc LICENSE.md
%attr(0755,root,root) %{_bindir}/neverball
%attr(0755,root,root) %{_bindir}/neverball-wrapper
%{_datadir}/appdata/neverball.appdata.xml
%{_datadir}/applications/neverball.desktop
%{_datadir}/icons/hicolor/*/apps/neverball.png

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-28
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-21
- Fix dejavu font path.

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-20
- Fix FTBFS.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.6.0-17
- Permissions fixes.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.6.0-15
- Fix FTBFS.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.0-12
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Richard Hughes <rhughes@redhat.com> - 1.6.0-7
- Install high quality version of the icons

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.6.0-5
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Richard Hughes <richard@hughsie.com> - 1.6.0-3
- Split out neverputt and neverball into subpackages so that each one is
  installable in the GNOME and KDE software centers.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Jon Ciesla <limburgher@gmail.com> - 1.6.0-1
- 1.6.0, BZ 1100662.
- Dropped desktop icon extensions.
- Drop upstreamed patches.

* Mon Aug 05 2013 Jon Ciesla <limburgher@gmail.com> - 1.5.4-13
- Date fixes, fix FTBFS, BZ 992353.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 1.5.4-11
- Drop desktop vendor tag.

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.5.4-10
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.5.4-9
- rebuild against new libjpeg

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Tom Callaway <spot@fedoraproject.org> - 1.5.4-6
- rebuild for physfs2

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.5.4-5
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 19 2010 Wart <wart@kobold.org> - 1.5.4-3 
- Add explicit link against -lX11 -lm to remove implicit library
  linkage (#565203)

* Sun Jan 10 2010 Wart <wart@kobold.org> - 1.5.4-2 
- Set DATADIR so that neverball and neverputt can find their data (#538210)

* Thu Oct 8 2009 Wart <wart@kobold.org> - 1.5.4-1
- Update to 1.5.4

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Wart <wart@kobold.org> - 1.4.0-15
- Change from bitstream-vera font to equivalent dejavu font.

* Fri Jan 16 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.4.0-14
- Fix font Requires bitstream-vera-fonts-sans ->
  bitstream-vera-sans-fonts (another font naming convention change).

* Thu Jan 1 2009 Wart <wart@kobold.org> - 1.4.0-13
- Fix font package name for F11

* Tue Dec 23 2008 Wart <wart@kobold.org> - 1.4.0-12
- Replace bundled font with a symlink to an identical system font (BZ #477432)

* Fri Feb 8 2008 Wart <wart@kobold.org> - 1.4.0-11
- Rebuild for gcc 4.3

* Sat Sep 29 2007 Wart <wart@kobold.org> - 1.4.0-10
- Add wrapper for detecting DRI when launching game (BZ #304811)

* Mon Aug 20 2007 Wart <wart@kobold.org> - 1.4.0-9
- License tag clarification

* Fri Mar 9 2007 Wart <wart@kobold.org> - 1.4.0-8
- Updated desktop file categories

* Sat Sep 2 2006 Wart <wart@kobold.org> - 1.4.0-7
- Change BR: for opengl
- Rebuild for Fedora Extras

* Thu Mar 2 2006 Wart <wart@kobold.org> - 1.4.0-6
- Add dist tag now that spec files are different between releases

* Mon Feb 27 2006 Wart <wart@kobold.org> - 1.4.0-5
- Added BR: mesa-libGL-devel for modular xorg
- Added smp_mflags to compile line to speed up build on smp machines

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.4.0-4
- rebuild on all arches

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Nov 11 2004 Matthias Saou <http://freshrpms.net/> 1.4.0-2
- Bump release to provide Extras upgrade path.
- Fix tabs/spaces mixture.
- Make the changelog breathe a little, and be readable.

* Sat Oct 16 2004 Nils O. Selåsdal <NOS@Utel.no>- 0:1.4.0-0.fdr.1
- Update to 1.4.0
- Remove libGLU BuildRequires, it seems to be gone with an xorg errata,
  xorg-x11-devel should be all thats needed now though.
- Add neverputt .desktop file

* Fri Aug 13 2004 Nils O. Selåsdal <NOS@Utel.no>- 0:1.3.7-0.fdr.1
- Update to 1.3.7, which fixes a corruption in Neverputt level 16

* Tue Aug 03 2004 Nils O. Selåsdal <NOS@Utel.no>- 0:1.3.6-0.fdr.1
- Update to 1.3.6

* Thu Jul 08 2004 Nils O. Selåsdal <NOS@Utel.no>- 0:1.3.1-0.fdr.1
- Update to 1.3.1
- Add icon to .desktop file
- Really include neverputt binary

* Thu Jun 03 2004 Nils O. Selåsdal <NOS@Utel.no>- 0:1.2.5-0.fdr.2
- Sign the src.rpm

* Tue Jun 01 2004 Nils O. Selåsdal <NOS@Utel.no>- 0:1.2.5-0.fdr.1
- 1.2.5 and updated to work on FC2
- Include new neverputt binary.
- Use CFLAGS for pullingin RPM_OPT_FLAGS

* Fri Mar 19 2004 Nils O. Selåsdal <NOS@Utel.no>- 0:1.1.0-0.fdr.1
- 1.1.0

* Fri Nov 21 2003 Nils O. Selåsdal <NOS@Utel.no>- 0:1.0.0-0.fdr.2
- Add missing BuildRequires.

* Sat May 03 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:1.0.0-0.fdr.1
- Initial RPM release.

