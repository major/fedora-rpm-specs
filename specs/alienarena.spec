Name:		alienarena
Summary:	Multiplayer retro sci-fi deathmatch game
Version:	7.72.4
Release:	1%{?dist}
License:	GPL-2.0-or-later AND Zlib
# The tarball carries prebuilt Windows binaries (*.exe, *.dll), deleted in
# %%prep
Source0:	https://github.com/alienarena/alienarena/archive/%{version}/%{name}-%{version}.tar.gz
Source2:	GPL.acebot.txt
Source3:	org.alienarena.alienarena.metainfo.xml
Patch5:		alienarena-7.71.2-svn5674-system-ode-double.patch
# Globals defined in headers in the game, server and common code: declare
# them extern and define them once, as GCC defaults to -fno-common since
# GCC 10. The client and renderer have hundreds more, which upstream builds
# with -fcommon.
Patch6:		alienarena-7.72.4-fno-common.patch
Patch7:		alienarena-c99.patch
Patch12:	alienarena-7.72.4-fix-CL_GetLatestGameVersion.patch
URL:		https://alienarena.org/
BuildRequires:  gcc
BuildRequires:	libX11-devel, libXext-devel, libXxf86vm-devel, libjpeg-devel
BuildRequires:	mesa-libGL-devel, mesa-libGLU-devel, curl-devel, libpng-devel
BuildRequires:	libvorbis-devel, ode-devel, openal-soft-devel, freetype-devel
BuildRequires:	zlib-devel, minizip-devel
BuildRequires:	desktop-file-utils
BuildRequires:  make
Requires:	%{name}-data = 1:%{version}
Requires:	opengl-games-utils
Requires:	openal-soft%{?_isa}
# s390x cannot unpack the very large source tarball reliably.
# given the unlikely scenario where someone wants to play alienarena
# (or run a server) on an s390x... i feel it is safe to excludearch
# If you disagree, feel free to FIX LARGE FILE OPS ON s390x.
ExcludeArch:	s390x

%description
Alien Arena is a furious frag fest with arenas ranging from the small
to the massive. With game modes such as Capture The Flag and Tactical,
there are terrific team-based experiences to be had as well as 1v1
duels, free-for-all and dozens of mutators to alter the game play to
your liking.

%package server
Summary:	Dedicated server for alienarena, the FPS game
Requires:	%{name}-data = 1:%{version}

%description server
Alien Arena is a furious frag fest with arenas ranging from the small
to the massive. With game modes such as Capture The Flag and Tactical,
there are terrific team-based experiences to be had as well as 1v1
duels, free-for-all and dozens of mutators to alter the game play to
your liking.

This is the dedicated server.

%package data
Summary:	Game Data for alienarena, the FPS game
Epoch:		1
BuildArch:	noarch
License:	GPL-2.0-or-later

%description data
Alien Arena is a furious frag fest with arenas ranging from the small
to the massive. With game modes such as Capture The Flag and Tactical,
there are terrific team-based experiences to be had as well as 1v1
duels, free-for-all and dozens of mutators to alter the game play to
your liking.

This is the game data.

%prep
%autosetup -p1

# We don't want the bundled ode code.
rm -rf source/unix/ode

# Nor the prebuilt Windows binaries.
find . -name "*.dll" -type f -delete
find . -name "*.exe" -type f -delete

# Copy license clarification for acebot
cp -p %{SOURCE2} .

# clean up end-line encoding
[[ -e docs/README.txt ]] && sed -i 's/\r//' docs/README.txt

%build
%configure --without-xf86dga --with-system-libode
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/metainfo
cp -a %{SOURCE3} %{buildroot}%{_datadir}/metainfo

sed -i 's|/usr/games/alien-arena --quiet|alienarena-wrapper|g' unix_dist/alien-arena.desktop
sed -i 's|alien-arena.png|alien-arena|g' unix_dist/alien-arena.desktop
desktop-file-install --dir %{buildroot}%{_datadir}/applications	unix_dist/alien-arena.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
cp -a unix_dist/alien-arena.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

# Fedora's little opengl checker
ln -s opengl-game-wrapper.sh %{buildroot}/%{_bindir}/%{name}-wrapper

cp -a GPL.acebot.txt %{buildroot}%{_defaultdocdir}/%{name}/

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_datadir}/applications/alien-arena.desktop
%{_datadir}/icons/%{name}
%{_datadir}/icons/hicolor/256x256/apps/*.png
%{_datadir}/metainfo/*.xml

%files server
%{_bindir}/alienarena-ded

%files data
%doc GPL.acebot.txt
%{_defaultdocdir}/%{name}/
%{_datadir}/%{name}

%changelog
* Thu Nov 26 2026 Trung Lê <8@tle.id.au> - 7.72.4-1
- Update to 7.72.4, from the GitHub release tarball
- Drop the incompatible-pointer, bad-sprintf-use and minizip patches, fixed
  upstream
- Drop the libopenal.so soname fix-up, upstream dlopen()s libopenal.so.1
- Rebase the gcc10 and CL_GetLatestGameVersion patches; rename the gcc10
  patch to fno-common
- Drop -fcommon from optflags, upstream's configure adds it
- Drop Requires: desktop-file-utils and the PTHREAD_* exports
- Use %%autosetup and %%make_build
- Drop the no-qglBlitFramebufferEXT patch, a workaround for old Mesa

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Aug 12 2025 Tom Callaway <spot@fedoraproject.org> - 7.71.7-4
- no more 32x32 icon
- rename metainfo

* Mon Aug 11 2025 Tom Callaway <spot@fedoraproject.org> - 7.71.7-3
- fix desktop file (more)

* Mon Aug 11 2025 Tom Callaway <spot@fedoraproject.org> - 7.71.7-2
- fix appstream file, thanks to Daniel Rusek

* Tue Aug  5 2025 Tom Callaway <spot@fedoraproject.org> - 7.71.7-1
- update to 7.71.7
- use upstream desktop and logo png

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Tom Callaway <spot@fedoraproject.org> - 7.71.6-1
- update to 7.71.6

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Florian Weimer <fweimer@redhat.com> - 7.71.2-7
- C99 compatibility fix (#2154541)

* Sun Jul 24 2022 Robert-André Mauchin <zebob.m@gmail.com> - 7.71.2-6
- Rebuilt for Ode soname bump

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Tom Callaway <spot@fedoraproject.org> - 7.71.2-1
- update to 7.71.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb  5 2020 Tom Callaway <spot@fedoraproject.org> - 7.71.1-3
- fix FTBFS
- excludeArch s390x

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Tom Callaway <spot@fedoraproject.org> - 7.71.1-1
- update to svn trunk (7.71.1)
- update descriptions

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.71.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Tom Callaway <spot@fedoraproject.org> - 7.71.0-1
- update to 7.71.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.66-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.66-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.66-13
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.66-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.66-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.66-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.66-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.66-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  9 2015 Tom Callaway <spot@fedoraproject.org> - 7.66-7
- bring all code to SVN4307 to try to resolve ragdoll crashes

* Mon Jan 12 2015 Tom Callaway <spot@fedoraproject.org> - 7.66-6
- ragdoll fix (SVN: 4304)

* Tue Nov  4 2014 Tom Callaway <spot@fedoraproject.org> - 7.66-5
- rebuild for new libode

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 5 2013 Tom Callaway <spot@fedoraproject.org> - 7.66-1
- update to 7.66
- add appdata file (bz 1023990)

* Wed Sep 4 2013 Chandler Wilkerson <chwilk@rice.edu> - 7.65-5
- Added aarch64 patch pending upstream move to autoconf 2.69 in next release (bz 924982)
- Tweaked license line of alienarena-data package to match license text. (bz 888201)

* Fri Aug 16 2013 Tom Callaway <spot@fedoraproject.org> - 7.65-4
- fix license text (bz 888201)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.65-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Hans de Goede <hdegoede@redhat.com> - 7.65-2
- Rebuild for new ode

* Tue Feb 19 2013 Chandler Wilkerson <chwilk@rice.edu> - 7.65-1
- update to 7.65 upstream
- remove ode-quickstep patch after upstream fix now works with 0.12

* Sat Feb 09 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 7.60.1-6
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 7.60.1-5
- rebuild due to "jpeg8-ABI" feature drop

* Sun Nov 4 2012 Chandler Wilkerson <chwilk@rice.edu> - 7.60.1-4
- Fixed epoch mismatch for -data dependency in -server subpackage stanza

* Wed Oct 31 2012 Chandler Wilkerson <chwilk@rice.edu> - 7.60.1-3
- Added epoch 1 to -data package to override previously separate alienarena-data package
- Reapplied original patches for FBOblit fix and libopenal linking

* Thu Oct 25 2012 Chandler Wilkerson <chwilk@rice.edu> - 7.60.1-2
- Added ode-quickstep patch to fix obsoleted function call from pre 0.12 ode

* Wed Oct 24 2012 Chandler Wilkerson <chwilk@rice.edu> - 7.60.1-1
- update to 7.60.1
- change to using source tarball

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jan  6 2012 Tom Callaway <spot@fedoraproject.org> - 7.53-1
- update to 7.53

* Fri Oct 21 2011 Tom Callaway <spot@fedoraproject.org> - 7.52-1
- update to 7.52

* Thu Mar 24 2011 Tom Callaway <spot@fedoraproject.org> - 7.51-2
- use system ode-double
- disable xf86dga to add mouse sanity

* Wed Mar 23 2011 Tom Callaway <spot@fedoraproject.org> - 7.51-1
- update to 7.51

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 7.50-1
- update to 7.50
- fix ode NAN issue

* Mon Aug  2 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 7.45-1
- update to 7.45

* Thu Jul 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 7.40-2
- add hard dependency on openal-soft (bz 597684)

* Thu Jul 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 7.40-1
- update to 7.40

* Tue Apr  6 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 7.33-2
- fix security issues identified in bz 577810
 - By supplying various invalid parameters to the download command,
   it is possible to cause a DoS condition by causing the server to
   crash. A path ending in . or / will crash on Linux. Supplying
   a negative offset will cause a crash on all platforms.
 - Fix buffer overflow identified in R1Q2 client code

* Fri Jan 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 7.33-1
- update to 7.33

* Sat Nov  7 2009 Hans de Goede <hdgoede@redhat.com> - 7.32-2
- dlopen openal.so.x, not openal.so.x.y. this fixes a crash on startup when
  the openal minor version has changed
- fix deprecation warning with latest libXxf86dga-devel

* Mon Nov  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 7.32-1
- update to 7.32
- fix CVE-2009-3637 (bugzilla 530514)

* Wed Aug 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 7.30-2
- fix dlopen code to find proper openal library
- use openal-soft instead of old openal

* Thu Jul 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 7.30-1
- update to 7.30

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 7.21-1
- update to 7.21
- apply Paul's patch to print the search paths

* Wed Oct 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 7.20-5
- use /bin/bash for the scripts due to the export LD_LIBRARY_PATH

* Sun Oct 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 7.20-4
- re-enable "don't search data path" patch

* Sun Oct 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 7.20-3
- use LD_LIBRARY_PATH in scripts

* Sat Oct 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 7.20-2 
- drop old "don't search data path" patch
- call alienarena-wrapper in .desktop file

* Mon Oct 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 7.20-1
- sync up with Paul Bredbury's spec file
- update to 7.20

* Fri Sep 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 7.10-2
- drop fhs patch, use Makefile DATADIR options instead

* Wed Jul  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 7.10-1
- update to 7.10 (2008)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 6.10-6
- Autorebuild for GCC 4.3

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> 6.10-5
- generic optflags only

* Tue Nov 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 6.10-4
- lots of cleanups from review

* Fri Nov 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 6.10-3
- include legal clarification text for ace bot code
- simplify description

* Thu Nov 8 2007 Tom "spot" Callaway <tcallawa@redhat.com> 6.10-2
- make shell script launcher to get game working
  (run alienarena, not crx.sdl directly)

* Thu Nov 1 2007 Tom "spot" Callaway <tcallawa@redhat.com> 6.10-1
- Initial package for Fedora
