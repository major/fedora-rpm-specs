%global nhgamedir /usr/games/nethack
%global nhdatadir /var/games/nethack

%global fontname nethack-bitmap

Name:           nethack
Version:        5.0.0
Release:        1%{?dist}
Summary:        A rogue-like single player dungeon exploration game

License:        NGPL
URL:            https://nethack.org
Source0:        https://nethack.org/download/5.0.0/nethack-500-src.tgz
Patch:          nethack-5.0.0-guidebook.patch
Patch:          nethack-5.0.0-hackdir.patch
Patch:          nethack-5.0.0-playground.patch
Obsoletes:      nethack-bitmap-fonts <= 5.0.0-2
Obsoletes:      nethack-bitmap-fonts-core <= 5.0.0-2

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  lua-devel lua-static


%description
NetHack is a single player dungeon exploration game that runs on a
wide variety of computer systems, with a variety of graphical and text
interfaces all using the same game engine.

Unlike many other Dungeons & Dragons-inspired games, the emphasis in
NetHack is on discovering the detail of the dungeon and not simply
killing everything in sight - in fact, killing everything in sight is
a good way to die quickly.

Each game presents a different landscape - the random number generator
provides an essentially unlimited number of variations of the dungeon
and its denizens to be discovered by the player in one of a number of
characters: you can pick your race, your role, and your gender.


%prep
%autosetup -p1 -n NetHack-5.0.0

%{__sed} -i -e "s:PREFIX=\$(wildcard ~)/nh/install:PREFIX=/usr:" sys/unix/hints/linux.500
%{__sed} -i -e "s:^\(HACKDIR=\).*:\1%{nhgamedir}:" sys/unix/hints/linux.500
sh sys/unix/setup.sh sys/unix/hints/linux.500

# Set our paths
%{__sed} -i -e "s:^\(HACKDIR=\).*:\1%{nhgamedir}:" sys/unix/nethack.sh
%{__sed} -i -e "s:FEDORA_CONFDIR:%{nhgamedir}:" sys/unix/nethack.sh
%{__sed} -i -e "s:FEDORA_STATEDIR:%{nhdatadir}:" include/unixconf.h
%{__sed} -i -e "s:FEDORA_HACKDIR:%{nhgamedir}:" include/config.h
%{__sed} -i -e "s:/usr/games/lib/nethackdir:%{nhgamedir}:" \
        doc/nethack.6 doc/nethack.txt doc/recover.6 doc/recover.txt

%build

# Instead of downloading lua from the network and building it
# just link to the fedora lua-static/lua-devel
# Note that the version here doesn't matter
mkdir -p lib/lua-5.4.8/src/
cp -a %{_includedir}/lua.h lib/lua-5.4.8/src/
cp -a %{_includedir}/lauxlib.h lib/lua-5.4.8/src/
cp -a %{_includedir}/lualib.h lib/lua-5.4.8/src/
cp -a %{_libdir}/liblua.a lib/lua-5.4.8/src/liblua.a

export CFLAGS+="%{optflags}"
%make_build WANT_WIN_TTY=1 WANT_WIN_CURSES=1

%install
%make_install \
        PREFIX=$RPM_BUILD_ROOT \
        HACKDIR=$RPM_BUILD_ROOT%{nhgamedir} \
        GAMEDIR=$RPM_BUILD_ROOT%{nhgamedir} \
        VARDIR=$RPM_BUILD_ROOT%{nhdatadir} \
        SHELLDIR=$RPM_BUILD_ROOT%{_bindir} \
        CHOWN=/bin/true \
        CHGRP=/bin/true

install -d -m 0755 $RPM_BUILD_ROOT%{_mandir}/man6
make -C doc MANDIR=$RPM_BUILD_ROOT%{_mandir}/man6 manpages

# drop duplicate license file
rm -f $RPM_BUILD_ROOT%{nhgamedir}/license

%files
%license dat/license
%doc doc/*.txt README dat/history
%doc dat/opthelp dat/wizhelp
%{_mandir}/man6/*
%{_bindir}/nethack
%defattr(0664,root,games)
%config(noreplace) %{nhdatadir}/record
%config(noreplace) %{nhdatadir}/perm
%config(noreplace) %{nhdatadir}/logfile
%config(noreplace) %{nhdatadir}/xlogfile
%config(noreplace) %{nhdatadir}/livelog
%attr(0775,root,games) %dir %{nhdatadir}
%attr(0775,root,games) %dir %{nhdatadir}/save
%dir %{nhgamedir}
%attr(2755,root,games) %{nhgamedir}/nethack
%config(noreplace) %{nhgamedir}/nhdat
%config(noreplace) %{nhgamedir}/sysconf
%config(noreplace) %attr(0555,root,games) %{nhgamedir}/recover
%config(noreplace) %{nhgamedir}/symbols

%changelog
* Tue Jul 07 2026 Kevin Fenzi <kevin@scrye.com> - 5.0.0-1
- Update to 5.0.0. Fixes rhbz#2483160
- Drop old X11 interface and bitmap fonts

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jan 22 2025 Ron Olson <tachoknight@gmail.com> - 3.6.7-7
- Fixes for gcc changes
  Resolves: rhbz#2340917

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 18 2023 Ron Olson <tachoknight@gmail.com> - 3.6.7-1
- Update to NetHack 3.6.7

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Ron Olson <tachoknight@gmail.com> - 3.6.6-10
- SPDX migration

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Jeff Mendoza <jlm@jlm.name> - 3.6.6-8
- Enable build option for .xpm format support

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 10 2021 Ron Olson <tachoknight@gmail.com> 3.6.6-5
- Fixed some issues under Fedora 35 not building properly and
  not being able to run correctly when installed

* Thu Mar 04 2021 Peter Hutterer <peter.hutterer@redhat.com> 3.6.6-4
- Require only mkfontdir, not all of xorg-x11-font-utils (#1933533)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Ron Olson <tachoknight@gmail.com> - 3.6.6-1
- Update to NetHack 3.6.6

* Tue Jan 28 2020 Ron Olson <tachoknight@gmail.com> - 3.6.5-1
- Update to NetHack 3.6.5 and removed gcc 10 patch because
  the code was properly fixed upstream

* Fri Jan 24 2020 Ron Olson <tachoknight@gmail.com> - 3.6.4-2
- Added patch to compile properly with gcc 10

* Thu Dec 19 2019 Ron Olson <tachoknight@gmail.com> - 3.6.4-1
- Update to NetHack 3.6.4

* Mon Dec 09 2019 Ron Olson <tachoknight@gmail.com> - 3.6.3-1
- Update to NetHack 3.6.3

* Tue Aug 13 2019 Ron Olson <tachoknight@gmail.com> - 3.6.2-3
- Removed Group tag and clean section

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Ron Olson <tachoknight@gmail.com> - 3.6.2-1
- Update to NetHack 3.6.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Ron Olson <tachoknight@gmail.com> - 3.6.1-3
- Added gcc as an explicit build dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Ron Olson <tachoknight@gmail.com> 3.6.1-1
- First version of 3.6.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Ron Olson <tachoknight@gmail.com> - 3.6.0-38
- Added pilemark.xbm to game directory to fix error when playing 
  under X11

* Mon Jun 05 2017 Ron Olson <tachoknight@gmail.com> - 3.6.0-37
- Set executable bit on recover program

* Sun Oct 02 2016 Ron Olson <tachoknight@gmail.com> - 3.6.0-36
- Upgraded to version 3.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 18 2014 Luke Macken <lmacken@redhat.com> - 3.4.3-31
- Apply a patch to fix the build with -Werror=format-security (#1037215, #1106286)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 3.4.3-28
- Drop desktop vendor tag.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 11 2010 Luke Macken <lmacken@redhat.com> - 3.4.3-24
- Fix the source URL

* Tue Sep 01 2009 Luke Macken <lmacken@redhat.com> - 3.4.3-23
- Fix the categories for the nethack desktop entry (#485362)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Luke Macken <lmacken@redhat.com> - 3.4.3-21
- Apply a patch from Iain Arnell to update our spec to comply with
  the new font packaging guidelines (#505613)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Jochen Schmitt <Jochen herr-schmitt de> - 3.4.3-19
- Add missing Requires

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.4.3-18
- fix license tag

* Fri Feb  8 2008 Luke Macken <lmacken@redhat.com> - 3.4.3-17
- Rebuild for gcc 4.3

* Thu Jan 17 2008 Luke Macken <lmacken@redhat.com> 3.4.3-16
- Create a symlink to our fonts in /etc/X11/fontpath.d (Bug #221692)

* Tue Aug 21 2007 Luke Macken <lmacken@redhat.com> 3.4.3-15
- Rebuild

* Mon Jul  9 2007 Luke Macken <lmacken@redhat.com> 3.4.3-14
- Fix nethack.desktop (Bug #247373)

* Sun Jul 08 2007 Florian La Roche <laroche@redhat.com> 3.4.3-13
- require xorg-x11-font-utils (to run mkfontdir) for post script

* Mon Oct 16 2006 Luke Macken <lmacken@redhat.com> 3.4.3-12
- Own /usr/games/nethack-3.4.3

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> 3.4.3-11
- Rebuild for FC6

* Mon Apr 10 2006 Luke Macken <lmacken@redhat.com> 3.4.3-10
- Remove $RPM_BUILD_ROOT from %post (Bug #188008)

* Wed Feb 15 2006 Luke Macken <lmacken@redhat.com> 3.4.3-9
- Add nethack-3.4.3-guidebook.patch to fix issues with generating the Guidebook
  (this patch also removes the need for our groff dep)

* Wed Feb 15 2006 Luke Macken <lmacken@redhat.com> 3.4.3-8
- Add groff to BuildRequires

* Tue Feb 14 2006 Luke Macken <lmacken@redhat.com> 3.4.3-7
- Rebuild for FE5

* Tue Dec 27 2005 Luke Macken <lmacken@redhat.com> 3.4.3-6
- Rebuild

* Wed Nov 23 2005 Luke Macken <lmacken@redhat.com> 3.4.3-5
- Keep the license in the game directory (Bug #173385)
- Don't obsolete falconseye anymore (Bug #173385)

* Fri Nov 11 2005 Luke Macken <lmacken@redhat.com> 3.4.3-4
- Utilize modular xorg

* Thu Sep 08 2005 Luke Macken <lmacken@redhat.com> 3.4.3-3
- Point linker in the right direction using %%{_lib} to fix x86_64 build issues

* Tue Sep 06 2005 Luke Macken <lmacken@redhat.com> 3.4.3-2
- Enable x11 support

* Sun Jul 10 2005 Luke Macken <lmacken@redhat.com> 3.4.3-1
- Initial package for Fedora Extras
