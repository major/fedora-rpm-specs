Name: tecnoballz
Version: 0.92
Release: 46%{?dist}
Summary: A Brick Busting game

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://linux.tlk.fr/games/TecnoballZ/
Source0: http://linux.tlk.fr/games/TecnoballZ/download/%{name}-%{version}.tgz
Source1: %{name}.xpm
Source2: %{name}.desktop
# Andrea Musuruane
# Fix dependencies
Patch0: tecnoballz-0.92-dependecies.patch
# Andrea Musuruane
# Don't combine explicit and implicit rules for make 3.82
# Set correct gamedir for Fedora
Patch1: tecnoballz-0.92-Makefile.patch
# Debian
# Fix configure.ac Makefile.am to include missing files
Patch2: tecnoballz-0.92-level_data.patch
Patch3: tecnoballz-0.92-texts_dir.patch
# Debian
# Use tinyxml system library
Patch4: tecnoballz-0.92-tinyxml.patch
# Upstream CVS
# Compile with gcc 4.3
Patch5: tecnoballz-0.92-gcc43.patch
# Hans de Goede
# Drop setgid privileges when not needed
Patch6: tecnoballz-0.92-dropsgid.patch
# Raphael Groner/Upstream GIT
# Compile with gcc 6
Patch7: tecnoballz-0.92-gcc6-narrowing.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel
BuildRequires: mikmod-devel
BuildRequires: tinyxml-devel
BuildRequires: desktop-file-utils
Requires: hicolor-icon-theme


%description
A exciting Brick Breaker with 50 levels of game and 11 special levels, 
distributed on the 2 modes of game to give the player a sophisticated 
system of attack weapons with an enormous power of fire that can be 
build by gaining bonuses. Numerous decors, musics and sounds 
complete this great game. This game was ported from the Commodore Amiga.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
# Patch4 must be called after Patch0
%patch -P4 -p1
%patch -P5 -p2
%patch -P6 -p1
%patch -P7 -p1


%build
autoreconf -fvi
%configure
# FIX: ovverride CXXFLAGS to pick up RPM_OPT_FLAGS
%make_build CXXFLAGS="$RPM_OPT_FLAGS"


%install
%make_install

# install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install         \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}

# install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%files
%attr(2755,root,games) %{_bindir}/tecnoballz
%{_datadir}/tecnoballz
%{_localstatedir}/games/tecnoballz
%attr(-,root,games) %config(noreplace) %{_localstatedir}/games/tecnoballz/tecnoballz.hi
%{_mandir}/man6/%{name}.6*
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
%doc AUTHORS CHANGES README
%license COPYING


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.92-45
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-36
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Andrea Musuruane <musuruan@gmail.com> - 0.92-30
- Added gcc-c++ dependency
- Added license tag
- Spec file clean up

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.92-28
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 26 2016 Andrea Musuruane <musuruan@gmail.com> - 0.92-24
- Fix gcc6 narrowing. Thanks to Raphael Groner. Fix #1308179.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.92-21
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.92-16
- Remove vendor tag from desktop file
- spec clean up

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-14
- Rebuilt for c++ ABI breakage

* Mon Feb 13 2012 Andrea Musuruane <musuruan@gmail.com> 0.92-13
- Rebuilt because of BZ #758251

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Andrea Musuruane <musuruan@gmail.com> 0.92-11
- use tinyxml system library (patch from Debian)
- fix configure.ac and Makefile.am to include missing files (patches from 
  Debian)
- fix dependencies in configure.ac

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.92-9
- Rebuilt for gcc bug 634757

* Sun Sep 12 2010 Andrea Musuruane <musuruan@gmail.com> 0.92-8
- fix building with make 3.82 (BZ #631335)
- fix dependencies
- fix desktop file

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 03 2008 Andrea Musuruane <musuruan@gmail.com> 0.92-5
- fix unowned directory (BZ #473980)

* Sun Feb 17 2008 Andrea Musuruane <musuruan@gmail.com> 0.92-4
- rebuilt against libmikmod 3.2.0

* Sun Feb 10 2008 Andrea Musuruane <musuruan@gmail.com> 0.92-3
- rebuilt against gcc 4.3

* Sun Jan 06 2008 Andrea Musuruane <musuruan@gmail.com> 0.92-2
- added a patch from upstream CVS to compile with GCC 4.3

* Sat Dec 22 2007 Andrea Musuruane <musuruan@gmail.com> 0.92-1
- updated to v0.92
- license changed to GPLv3+
- changed description
- dropped French man page because it is outdated
- added SDL_image-devel to BR
- added a new patch by Hans de Goede to drop setgid privileges when not needed
- dropped no longer needed patches

* Sat Aug 25 2007 Andrea Musuruane <musuruan@gmail.com> 0.91-6
- changed license due to new guidelines
- removed %%{?dist} tag from changelog
- updated icon cache scriptlets to be compliant to new guidelines
- changed desktop categories from Game;ArcadeGame; to
  Game;ArcadeGame;BlocksGame; (resolves bugzilla #250940)

* Tue Apr 03 2007 Andrea Musuruane <musuruan@gmail.com> 0.91-5
- changed summary to avoid naming trademarks.

* Sun Apr 01 2007 Andrea Musuruane <musuruan@gmail.com> 0.91-4
- corrected silly error in the %%postun script

* Sat Mar 31 2007 Andrea Musuruane <musuruan@gmail.com> 0.91-3
- added a patch by Hans de Goede to drop setgid privileges when not needed
- changed icon cache scriptles to be compliant with updated guidelines
- changed vendor to fedora in desktop-file-install

* Sun Mar 25 2007 Andrea Musuruane <musuruan@gmail.com> 0.91-2
- moved from Livna to Fedora
- added a patch by Hans de Goede to fix compiling on 64 bits (Livna #1367)
- added a patch by Hans de Goede not to require smpeg (Livna #1367)
- changed desktop category to Game;ArcadeGame
- binary setgid 'games' in order to allow a shared scoreboard file
- cosmetic changes

* Sun Dec 17 2006 Andrea Musuruane <musuruan@gmail.com> 0.91-1
- initial build for Livna based on Vine Linux package
- used icon file from Debian package
- used patches from Debian and Vine Linux packages
- used a patch by BoredByPolitics via happypenguin.org to fix building
- used a patch by Martin Michlmayr to fix compiling with gcc 4.1 (Debian
  #355841)
- used a patch from upstream to fix segfault into configfile.cc file

