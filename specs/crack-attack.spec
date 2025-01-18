Summary:        Puzzle action game
Name:           crack-attack
Version:        1.1.14
Release:        55%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/crack-attack/
Source0:        http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}-sounds.tar.gz
Source2:        %{name}-music.tar.gz
Patch0:         crack-attack-1.1.14-glutInit.patch
Patch1:         crack-attack-1.1.14-sanitize.patch
Patch2:         crack-attack-1.1.14-audio.patch
Patch3:         crack-attack-1.1.14-gcc43.patch
Patch4:         crack-attack-1.1.14-audio-ppc.patch
Patch5:         crack-attack-1.1.14-format-security.patch
Patch6:         crack-attack-1.1.14-rhbz1065649.patch
Patch7:         crack-attack-configure-c99.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  libstdc++-devel desktop-file-utils ImageMagick
BuildRequires:  SDL-devel gtk2-devel pkgconfig SDL_mixer-devel freeglut-devel
BuildRequires:  mesa-libGLU-devel libXmu-devel
BuildRequires: make

%description
A puzzle/action game in which you rush to eliminate colored blocks
before they fill your screen. Particularly clever eliminations cause
garbage to clutter your opponent's screen. Who will survive the
longest!? Playable both online and off.


%prep
%setup -q -a 1 -a 2
%patch -P0 -p1 -b .glutinit
%patch -P1 -p1 -b .sanitize
%patch -P2 -p1 -b .audio
%patch -P3 -p1 -b .gcc43
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
# fixup provided desktop file
sed -i -e 's/%{name}\.xpm/%{name}\.png/' \
  -e 's/Application;Games/Game;BlocksGame/' data/%{name}.desktop
echo "Comment=A Puzzle Game" >> data/%{name}.desktop


%build
%configure --enable-sound
make %{?_smp_mflags}


%install
%make_install

#copy Music and Sounds
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
install -m 644 data/sounds/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
cp -a music $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor fedora --delete-original \
%endif
  $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
convert -resize 48x48 $RPM_BUILD_ROOT%{_datadir}/%{name}/logo.tga \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
convert $RPM_BUILD_ROOT%{_datadir}/%{name}/logo.tga \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%files
%doc doc/*.html doc/*.jpg doc/*.xpm AUTHORS COPYING README ChangeLog
%doc music-sound-copyright.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6.gz


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.14-54
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Florian Weimer <fweimer@redhat.com> - 1.1.14-48
- Port configure script to C99

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.1.14-39
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.14-36
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.14-30
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 Hans de Goede <hdegoede@redhat.com> - 1.1.14-28
- Fix building with -Werror=format-security (rhbz#1037025)
- Fix crack-attack process sticking around when closing the gui with alt+F4
  (rhbz#1065649)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 1.1.14-25
- Remove no longer needed autoreconf call, %%configure from redhat-rpm-config
  >= 9.1.0-42 updates config.guess and config.sub for new architecture support

* Wed May  1 2013 Hans de Goede <hdegoede@redhat.com> - 1.1.14-24
- run autoreconf for aarch64 support (rhbz#925195)
- add a bigger version of the logo

* Fri Feb 22 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.1.14-23
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-20
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.1.14-18
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jun 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.14-14
- Fix sound on bigendian machines (bz 452394)

* Wed Mar  5 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.14-13
- Stop using a full URL for Source1 (upstream file somehow got trunkated to
  0 bytes)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.14-12
- Autorebuild for GCC 4.3

* Tue Dec  4 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.14-11
- Fix building with gcc 4.3

* Mon Aug  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.14-10
- Update License tag for new Licensing Guidelines compliance

* Fri Jan 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.14-9
- Add music and sounds based on a suggestion by Michal Ambroz <rebus@seznam.cz>

* Sun Aug 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.14-8
- Some small specfile cleanups
- Don't ship patch backup files and other cruft as docs
- Remove redundant desktop file from /usr/share/crack-attack

* Mon Aug 14 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1.14-7
- Submit to Fedora Extras since I see no reason it cannot live there
- Install icon into /usr/share/icons, instead of /usr/share/pixmaps
- Add scriptlets to update icon cache

* Sun May 14 2006 Noa Resare <noa@resare.com> 1.1.14-6.lvn5
- Really apply the patch also

* Thu May 11 2006 Noa Resare <noa@resare.com> 1.1.14-5.lvn5
- added call to glutInit (#245)

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sun Jan 29 2006 Adrian Reber <adrian@lisas.de> - 1.1.14-0.lvn.4
- Changed BR for modular X
- Dropped 0 Epoch
- Changed BuildRoot

* Sat Aug 13 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:1.1.14-0.lvn.3
- Include only one desktop menu entry for GUI version (#536).
 
* Mon Jul  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.1.14-0.lvn.2
- Clean up obsolete pre-FC2 support.

* Tue Jun 14 2005 Dams <anvil[AT]livna.org> - 0:1.1.14-0.lvn.1
- Updated to 1.1.14
- Man page switched from section 1 to 6.

* Sat Apr 30 2005 Dams <anvil[AT]livna.org> - 0:1.1.13-0.lvn.1
- Dont strip binary
- Honor optflags

* Thu Apr 28 2005 Dams <anvil[AT]livna.org> - 0:1.1.13-0.lvn.1
- Updated to 1.1.13

* Wed Nov 17 2004 Dams <anvil[AT]livna.org> - 0:1.1.10-0.lvn.4
- Added build switch for glut/freeglut

* Tue Nov 16 2004 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0:1.1.10-0.lvn.3
- Add gcc34 patch

* Sun Jul 11 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.1.10-0.lvn.2
- Add full Source0 URL.

* Mon Dec  1 2003 Dams <anvil[AT]livna.org> 0:1.1.10-0.lvn.1
- Updated to 1.1.10

* Sun Oct  5 2003 Dams <anvil[AT]livna.org> 0:1.1.9-0.fdr.1
- Updated to 1.1.9

* Tue Sep 16 2003 Dams <anvil[AT]livna.org> 0:1.1.8-0.fdr.7
- Updated patches from Mandrake contribs (Olivier Blin's package)
- Added patch from Guillaume Cottenceau to prevent segfault with
  voodoo3 cards

* Sun Sep  7 2003 Dams <anvil[AT]livna.org> 0:1.1.8-0.fdr.6
- Added another desktop entry for extreme mode

* Mon Aug 25 2003 Dams <anvil[AT]livna.org> 0:1.1.8-0.fdr.5
- Removed gl.h patch. Added real 'fix' for ARB GL functions

* Fri Aug 22 2003 Dams <anvil[AT]livna.org> 0:1.1.8-0.fdr.3
- desktop entry and icon
- gl.h patch dependent of XFree86 version
- Compiling with RPM_OPT_FLAGS

* Fri Aug 22 2003 Dams <anvil[AT]livna.org> 0:1.1.8-0.fdr.2
- Added patch to allow build with gcc 3.3
- Fixed gl.h bug

* Tue Jul  1 2003 Dams <anvil[AT]livna.org> 
- Initial build.
