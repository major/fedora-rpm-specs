Name:           torcs
Version:        1.3.7
Release:        23%{?dist}
Summary:        The Open Racing Car Simulator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://torcs.org/
Source0:        http://downloads.sf.net/torcs/torcs-%{version}.tar.bz2
Source1:        torcs.png

Patch0:         torcs-1.3.7-isnan.patch
Patch1:         torcs-1.3.7-nullptr.patch
Patch2:         format-argument.patch
Patch3:         torcs-freeglut.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  libGL-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  openal-soft-devel
BuildRequires:  plib-devel
BuildRequires:  zlib-devel

Requires:       hicolor-icon-theme
Requires:       torcs-data = %{version}

%description
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.


%prep
%autosetup -p1

# Prevent useless executable files in the debuginfo package (as of 1.3.1)
chmod -x src/libs/learning/policy.*


%build
%configure
make


%install
%make_install

# Icon for the desktop file
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/torcs.png

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --remove-category Application \
    --add-category Simulation \
    --dir %{buildroot}%{_datadir}/applications \
    torcs.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/torcs.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: torcs-devel@lists.sourceforge.net
SentUpstream: 2014-05-22
-->
<application>
  <id type="desktop">torcs.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>GPL-2.0+</project_license>
  <description>
    <p>
     TORCS is a highly portable multi platform car racing simulation.
     It is used as ordinary car racing game, as AI racing game and as research
     platform.
    </p>
    <p>
     TORCS features many different cars, tracks, and opponents to race against.
     You can steer with a joystick, steering wheel, mouse or the keyboard.
     Graphic features lighting, smoke, skid marks and glowing brake disks.
     The simulation features a simple damage model, collisions, tire and wheel
     properties, aerodynamics and much more.
    </p>
    <p>
     The game play allows different types of races from the simple practice
     session up to the championship.
     Enjoy racing against your friends in the split screen mode with up to four
     human players.
    </p>
  </description>
  <releases>
    <release version="1.3.7" date="2016-05-19"/>
  </releases>
  <content_rating type="oars-1.1">
    <content_attribute id="violence-cartoon">none</content_attribute>
    <content_attribute id="violence-fantasy">none</content_attribute>
    <content_attribute id="violence-realistic">none</content_attribute>
    <content_attribute id="violence-bloodshed">none</content_attribute>
    <content_attribute id="violence-sexual">none</content_attribute>
    <content_attribute id="violence-desecration">none</content_attribute>
    <content_attribute id="violence-slavery">none</content_attribute>
    <content_attribute id="violence-worship">none</content_attribute>
    <content_attribute id="drugs-alcohol">none</content_attribute>
    <content_attribute id="drugs-narcotics">none</content_attribute>
    <content_attribute id="drugs-tobacco">none</content_attribute>
    <content_attribute id="sex-nudity">none</content_attribute>
    <content_attribute id="sex-themes">none</content_attribute>
    <content_attribute id="sex-homosexuality">none</content_attribute>
    <content_attribute id="sex-prostitution">none</content_attribute>
    <content_attribute id="sex-adultery">none</content_attribute>
    <content_attribute id="sex-appearance">none</content_attribute>
    <content_attribute id="language-profanity">none</content_attribute>
    <content_attribute id="language-humor">none</content_attribute>
    <content_attribute id="language-discrimination">none</content_attribute>
    <content_attribute id="social-chat">none</content_attribute>
    <content_attribute id="social-info">none</content_attribute>
    <content_attribute id="social-audio">none</content_attribute>
    <content_attribute id="social-location">none</content_attribute>
    <content_attribute id="social-contacts">none</content_attribute>
    <content_attribute id="money-purchasing">none</content_attribute>
    <content_attribute id="money-gambling">none</content_attribute>
  </content_rating>
  <screenshots>
    <screenshot type="default">http://a.fsdn.com/con/app/proj/torcs/screenshots/torcs-20121025123603.png</screenshot>
    <screenshot>http://a.fsdn.com/con/app/proj/torcs/screenshots/torcs-20121025125922.png</screenshot>
  </screenshots>
  <url type="homepage">http://torcs.sourceforge.net/</url>
</application>
EOF

# We need this for proper automatic stripping to take place (still in 1.3.0)
find %{buildroot}%{_libdir}/torcs/ -name '*.so' | xargs %{__chmod} +x

%files
# Directory default mode of 0755 is MANDATORY, since installed dirs are 0777
%defattr(-,root,root,0755)
%license COPYING
%doc README
%{_bindir}/*
%{_libdir}/torcs/
%{_datadir}/appdata/torcs.appdata.xml
%{_datadir}/applications/torcs.desktop
%{_datadir}/games/torcs/
%{_datadir}/icons/hicolor/48x48/apps/torcs.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.7-22
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.7-11
- Rebuilt for new freeglut

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Pete Walter <pwalter@fedoraproject.org> - 1.3.7-9
- Add OARS and release data
- Update icon to 48x48 px version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Pete Walter <pwalter@fedoraproject.org> - 1.3.7-6
- Fix FTBFS with GCC 7 (#1556505)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Pete Walter <pwalter@fedoraproject.org> - 1.3.7-1
- Update to 1.3.7

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 05 2015 Pete Walter <pwalter@fedoraproject.org> - 1.3.6-1
- Update to 1.3.6

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.3-8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.3.3-7
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar  8 2012 Tom Callaway <spot@fedoraproject.org> - 1.3.3-1
- update to 1.3.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3.1-5
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 16 2009 Hans de Goede <hdegoede@redhat.com> 1.3.1-3
- Switch to openal-soft

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 10 2009 Matthias Saou <http://freshrpms.net/> 1.3.1-1
- Update to 1.3.1.
- Remove the drivers sub-package since only one is provided upstream now and
  it's mandatory (all of the separate drivers seem to be merged there now).

* Sun Mar 01 2009 Caolán McNamara <caolanm@redhat.com> - 1.3.0-10
- constify ret of strchr(const *char)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Matthias Saou <http://freshrpms.net/> 1.3.0-8
- Add Simulation category to the desktop file (#485369).

* Fri May 16 2008 Matthias Saou <http://freshrpms.net/> 1.3.0-7
- Rebuild for plib update.

* Sun Feb 24 2008 Matthias Saou <http://freshrpms.net/> 1.3.0-6
- Include patch to fix build with gcc 4.3.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Mon Oct 22 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-4
- Use opengl-games-utils provided wrapper in the desktop file (#304831).

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-3
- Rebuild for new BuildID feature.
- Update Source URLs s/dl.sf.net/downloads.sf.net/.

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-2
- Update License field.
- Minor spec file cleanups.
- Minor desktop file cleanups.

* Fri Nov 10 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-1
- Update to 1.3.0.
- Remove no longer needed track.cpp patch1.
- Remove no longer needed extraqualif patch2.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.2.4-4
- FC6 rebuild.

* Fri Mar 10 2006 Matthias Saou <http://freshrpms.net/> 1.2.4-3
- Remove patch that disabled checking for openal, since it also disabled
  linking against it, and caused nasty things to happen.
- Include track.cpp patch from Debian.
- Explicitly set X includes and libraries with modular X, since otherwise
  configure checks fail badly (first libm, then all X libs...).
- Add missing modular X build requirements.
- Include patch to fix one extra qualifification error with gcc 4.1.

* Wed Mar  1 2006 Matthias Saou <http://freshrpms.net/> 1.2.4-2
- Add support for modular X on FC >= 5.
- Include patches to rebuild against new openal and freealut (#179614).

* Wed Oct 12 2005 Matthias Saou <http://freshrpms.net/> 1.2.4-1
- Update to 1.2.4.
- Add torcs-data-tracks-road requirement directly to main torcs.
- Drop no longer needed TORCS-1.2.3-64bit.patch.
- Add openal-devel build dependency.

* Wed Aug  3 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-5
- Move base robots from the sub-package to the main one to have the default
  quick race work. Hopefully this will change in later versions if the game
  checks which drivers are available before starting the default quick race.
- Add torcs-data-cars-extra requirement for the same reason as above : Without,
  none of the drivers of the default quick race have a car and the game exits.
- Add olethros robots.
- Change %%files section to explicitly list all robots since the above change
  moved many of them to the main package, not just "human".
- Renamed 64bit patch to TORCS-1.2.3-64bit.patch.

* Thu May 26 2005 Jeremy Katz <katzj@redhat.com> - 1.2.3-4
- fix build on 64bit arches

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.2.3-3
- rebuild on all arches

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1.2.3-2
- rebuilt

* Mon Feb  7 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-1
- Update to 1.2.3.
- Remove billy and K1999 robot packages (no longer upstream).
- Update plib requirement from plib16 to plib (1.8.x).
- Remove %%{?_smp_mflags} as the build fails with -jN.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-4
- Add +x chmod'ing to .so files in order to get them stripped properly.

* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-3
- Remove un-needed /sbin/ldconfig calls.

* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-3
- Change build dependency of plib to compat package plib16-devel as
  rebuilding against 1.8 is not currently possible.
- Add patch for -fPIC to fix x86_64 build (hmm, doesn't work).

* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-2
- Rebuild for Fedora Core 2.
- Change XFree86 deps to xorg-x11 and glut to freeglut.

* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Update to 1.2.2.
- No longer require compat-libstdc++-devel for building.
- This version broke %%makeinstall, so switch to DESTDIR method.
- Re-enabled K1999 build, it works again.
- Added new robots : billy and bt.

* Tue Jan 13 2004 Matthias Saou <http://freshrpms.net/> 1.2.1-4
- Work around the XFree86 dependency problem by adding XFree86-Mesa-libGLU.

* Tue Dec  2 2003 Matthias Saou <http://freshrpms.net/> 1.2.1-3
- Rebuild for Fedora Core 1.
- Disabled build of the K1999 driver (strstream.h seems obsolete).

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Added a torcs requirement to the robots package.

* Wed Apr 23 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

