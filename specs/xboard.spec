Summary: An X Window System graphical chessboard
Name: xboard
Version: 4.9.1
Release: 22%{?dist}
URL: https://www.gnu.org/software/xboard/
Source0: ftp://ftp.gnu.org/pub/gnu/xboard/xboard-%{version}.tar.gz
Source1: xboard.desktop
Requires: chessprogram, xorg-x11-fonts-100dpi
License: GPL-3.0-or-later
BuildRequires: make
BuildRequires:  gcc
BuildRequires: desktop-file-utils >= 0.2.93
BuildRequires: texinfo
BuildRequires: xorg-x11-xbitmaps, libICE-devel, libXmu-devel, libSM-devel
BuildRequires: libXaw-devel, libXt-devel, xorg-x11-proto-devel
BuildRequires: libXpm-devel, libXext-devel
BuildRequires: automake
BuildRequires: gettext
BuildRequires: texinfo-tex
BuildRequires: librsvg2-devel
BuildRequires: gtk2-devel
BuildRequires: pango-devel

%description
Xboard is an X Window System based graphical chessboard which can be
used with the GNU chess and Crafty chess programs, with Internet Chess
Servers (ICSs), with chess via email, or with your own saved games.

Install the xboard package if you need a graphical chessboard.

%prep
%setup -q 

# Needed for ppc64, automake can't be run here
cp -f %{_datadir}/automake-*/config.* .

%build
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure
make %{?_smp_mflags}

%install
%make_install

desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	*.desktop

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
install -pm 755 -p cmail $RPM_BUILD_ROOT%{_bindir}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING COPYRIGHT
%doc AUTHORS NEWS README FAQ.html
%doc engine-intf.html
%config(noreplace) %{_sysconfdir}/xboard.conf
%{_bindir}/xboard
%{_bindir}/cmail
%{_mandir}/man6/xboard.6*
%{_infodir}/xboard.info*
%{_datadir}/icons/hicolor/*/apps/xboard.png
%{_datadir}/icons/hicolor/*/apps/xboard.svg
%{_datadir}/games/xboard
%{_datadir}/applications/xboard*.desktop
%{_datadir}/mime/packages/xboard.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.9.1-18
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 4.9.1-11
- Fix FTBFS.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.9.1-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 14 2016 Filipe Rosset <rosset.filipe@gmail.com> - 4.9.1-1
- Rebuilt for new upstream version, fixes rhbz #1362159

* Mon May 16 2016 Filipe Rosset <rosset.filipe@gmail.com> - 4.9.0-1
- Rebuilt for new upstream version + fixes deps, fixes rhbz #1336257

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Filipe Rosset <rosset.filipe@gmail.com> - 4.8.0-1
- Rebuilt for new upstream version, fixes rhbz #1160319

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-4
- update/optimize mime scriptlets

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Filipe Rosset <rosset.filipe@gmail.com> - 4.7.3-1
- Rebuilt for new upstream version, fixes rhbz #742743

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 4.6.2-2
- add BR on texinfo-tex to workaround texinfo packaging bug

* Tue Feb 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 4.6.2-1
- 4.6.2 release
- https://www.gnu.org/software/xboard/whats_new/4.6.2/index.html
- drop xboard-4.5.1-default_engine.patch
- update url, use find_lang macro, handle extra desktop files and mime info
- clean up spec to follow current guidelines

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun May  8 2011 Christopher Aillon <caillon@redhat.com> - 4.5.2a-1
- Update to 4.5.2a

* Thu Apr 14 2011 Christopher Aillon <caillon@redhat.com> - 4.5.1-2
- Rebuild

* Mon Apr 11 2011 Christopher Aillon <caillon@redhat.com> - 4.5.1-1
- Update to 4.5.1
- Now licensed under GPLv3+

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 26 2010 Chris Ricker <kaboom@oobleck.net> 4.4.2-1
- Update to new upstream release

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Robert Scheck <robert@fedoraproject.org> 4.2.7-19
- Solve the ppc64-redhat-linux-gnu configure target error

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Chris Ricker <kaboom@oobleck.net> 4.2.7-17
- Rebuild for GCC 4.3
- Fix license

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 4.2.7-16
- Fix build

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 4.2.7-15
- Bump and rebuild

* Wed Aug  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 4.2.7-14
- Security: fix world-writable permissions for chess.png (#200795).

* Wed May 24 2006 Chris Ricker <kaboom@oobleck.net> 4.2.7-13
- correct debuginfo package generation (bz#192608)

* Wed Feb 15 2006 Chris Ricker <kaboom@oobleck.net> 4.2.7-12
- Update for modular X

* Thu Jun 16 2005 Chris Ricker <kaboom@oobleck.net> 4.2.7-11%{?dist}
- Add more categories to desktop file (BZ #160476)

* Wed Jun 01 2005 Chris Ricker <kaboom@oobleck.net> 4.2.7-10%{?dist}
- Add dist tag

* Thu May 26 2005 David Woodhouse <dwmw2@infradead.org> 4.2.7-9
- Re-enable PPC build

* Mon May 23 2005 Chris Ricker <kaboom@oobleck.net> 4.2.7-8
- Update for Fedora Extras
- Don't strip binaries
- Preserve time stamps
- Update BuildRoot
- Drop unapplied patch
- Clean up info handling
- Include license and other docs

* Tue Jan 25 2005 Karsten Hopp <karsten@redhat.de> 4.2.7-7 
- add BuildRequires tetex (137561)

* Tue Nov 30 2004 Karsten Hopp <karsten@redhat.de> 4.2.7-7
- add URL (#141320)

* Wed Sep 22 2004 Than Ngo <than@redhat.com> 4.2.7-6
- cleanup specfile

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 02 2004 Karsten Hopp <karsten@redhat.de> 4.2.7-4 
- add some buildrequires (#125034)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Dec 04 2003 Karsten Hopp <karsten@redhat.de> 4.2.7-2
- bump release and rebuild

* Thu Dec 04 2003 Karsten Hopp <karsten@redhat.de> 4.2.7-1
- update to 4.2.7

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 10 2003 Karsten Hopp <karsten@redhat.de>
- #74382, xboard didn't start gnuchess with correct parameters

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches
- let rpm handle the gzipping of files
- remove stuff from the buildroot that won't be included in the resulting package

* Sun Aug 04 2002 Karsten Hopp <karsten@redhat.de>
- remove duplicate entry in info (#70695)

* Wed Jul 24 2002 Karsten Hopp <karsten@redhat.de>
- s/Games/Game/

* Tue Jul 23 2002 Karsten Hopp <karsten@redhat.de>
- update to 4.2.6
- use desktop-file-install (#69536)
- add icon

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Dec 18 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 4.2.5

* Mon Dec 17 2001 Karsten Hopp <karsten@redhat.de>
- set CHESS_PROGRAM to gnuchess instead of gnuchessx
  (it isn't available anymore after the update to chess-5)

* Thu Dec 13 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 4.2.4

* Sat Jul 07 2001 Karsten Hopp <karsten@redhat.de>
- Copyright -> License

* Wed May 09 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 4.2.3

* Mon Oct 02 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 4.1.0

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 11 2000 Bill Nottingham <notting@redhat.com>
- rebuild, FHS stuff.

* Thu Mar  9 2000 Bill Nottingham <notting@redhat.com>
- update to 4.0.7

* Mon Feb 28 2000 Matt Wilson <msw@redhat.com>
- rebuild info file to have proper dir entry, etc.

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- wmconfig -> desktop

* Sat Feb 05 2000 Cristian Gafton <gafton@redhat.com>
- add dir entries in install-info

* Thu Feb  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- gzip info pages (Bug #9035)
- add install-info stuff
- deal with rpm compressing man pages
- handle RPM_OPT_FLAGS

* Fri Dec 17 1999 Bill Nottingham <notting@redhat.com>
- update to 4.0.5

* Wed Sep  8 1999 Bill Nottingham <notting@redhat.com>
- update to 4.0.3

* Sat Aug 14 1999 Bill Nottingham <notting@redhat.com>
- change requires: to virtual 'chessprogram'

* Thu Aug 12 1999 Bill Nottingham <notting@redhat.com>
- require gnuchess so it will work out of the box

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 4.0.2

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- cleaned up spec file
- built package for 6.0

* Sat Jul 11 1998 Mike Wangsmo <wanger@redhat.com>
- updated to a new version
- buildrooted the package too

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
