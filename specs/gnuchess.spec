Summary: The GNU chess program
Name: gnuchess
Version: 6.2.9
Release: 11%{?dist}
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/chess/
Source: http://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz
#Source1: http://ftp.gnu.org/pub/gnu/chess/book_1.01.pgn.gz
# use precompiled book.dat:
Source1: book_1.02.dat.gz
Provides: chessprogram
BuildRequires: gcc-c++
BuildRequires: flex, gcc
BuildRequires: make
BuildRequires: help2man

%description
The gnuchess package contains the GNU chess program.  By default,
GNU chess uses a curses text-based interface.  Alternatively, GNU chess
can be used in conjunction with the xboard user interface and the X
Window System for play using a graphical chess board.

Install the gnuchess package if you would like to play chess on your
computer.  If you'd like to use a graphical interface with GNU chess,
you'll also need to install the xboard package and the X Window System.

%prep
%setup -q -n %{name}-%{version}
gzip -dc %{SOURCE1} > book.dat

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/games/gnuchess $RPM_BUILD_ROOT%{_bindir}
install -m 755 -p src/gnuchess $RPM_BUILD_ROOT%{_bindir}
install -m 644 -p book.dat $RPM_BUILD_ROOT%{_var}/lib/games/gnuchess
#Add gnuchess.ini, BZ 1075958
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnuchess/
install -m 644 src/gnuchess.ini $RPM_BUILD_ROOT%{_datadir}/gnuchess/

%files
%license COPYING
%attr(2755,root,games) %{_bindir}/gnuchess
%dir %{_var}/lib/games/gnuchess
%attr(664,root,games) %{_var}/lib/games/gnuchess/book.dat
%doc doc/* AUTHORS NEWS TODO README
%{_datadir}/gnuchess/gnuchess.ini

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 6.2.9-6
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 6.2.9-1
- 6.2.9

* Mon May 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 6.2.8-1
- 6.2.8

* Thu Apr 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 6.2.7-5
- Patch for CVE-2021-30184

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 6.2.7-1
- 6.2.7

* Sun Apr 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 6.2.6-1
- 6.2.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Matěj Cepl <mcepl@redhat.com> - 6.2.5-6
- Add gcc as BuildRequires and remove Groups (obsolete for many relases.)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 6.2.5-3
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 6.2.5-1
- 6.2.5, BZ 1474543.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Jon Ciesla <limburgher@gmail.com> - 6.2.4-1
- 6.2.4, BZ 1389898.

* Tue Sep 20 2016 Jon Ciesla <limburgher@gmail.com> - 6.2.3-1
- 6.2.3, BZ 1377510.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 17 2015 Jon Ciesla <limburgher@gmail.com> - 6.2.2-1
- Update to 6.2.2.
- Changelog fix.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.2.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Jan 08 2015 Jon Ciesla <limburgher@gmail.com> - 6.2.1-1
- Update to 6.2.1.

* Tue Sep 09 2014 Jon Ciesla <limburgher@gmail.com> - 6.1.2-2
- Add gnuchess.ini, BZ 1075958

* Tue Sep 02 2014 Jon Ciesla <limburgher@gmail.com> - 6.1.2-1
- Update to 6.1.2.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Jon Ciesla <limburgher@gmail.com> - 6.1.1-1
- Update to 6.1.1.
- Clean up changelog dates.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Jon Ciesla <limburgher@gmail.com> - 6.0.3-1
- Update to 6.0.3.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 05 2012 Jon Ciesla <limburgher@gmail.com> - 6.0.2-1
- Update to 6.0.2.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 11 2011 Christopher Aillon <caillon@redhat.com> - 5.08-1
- Update to 5.08
- Now licensed under GPLv3+

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.07-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 10 2009 Karsten Hopp <karsten@redhat.com> 5.07-14
- fix name collision of getline function

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Chris Ricker <kaboom@oobleck.net> 5.07-11
- Rebuild for GCC 4.3
- Fix license

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 5.07-10
- Bump and rebuild

* Wed Feb 15 2006 Chris Ricker <kaboom@oobleck.net> 5.07-9
- Bump and rebuild

* Wed Jun 01 2005 Chris Ricker <kaboom@oobleck.net> 5.07-8%{?dist}
- Add dist tag

* Thu May 26 2005 Chris Ricker <kaboom@oobleck.net> 5.07-7
- Patch to compile with gcc4

* Fri May 20 2005 Chris Ricker <kaboom@oobleck.net> 5.07-6
- Update for Fedora Extras
- Copyright -> License
- Don't strip binaries
- Preserve time stamps
- Update BuildRoot
- Drop unapplied patch

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 5.07-5
- Rebuilt for new readline.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 04 2004 Karsten Hopp <karsten@redhat.de> 5.07-3
- update and rebuild book.dat to fix #122431

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 14 2004 Karsten Hopp <karsten@redhat.de>
- update to 5.07

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 05 2003 Karsten Hopp <karsten@redhat.de> 5.06-1
- update
- precompile book.dat

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild for all arches

* Sat Jul 27 2002 Karsten Hopp <karsten@redhat.de>
- compress SRPM with bzip2 to save some space

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 30 2002 Karsten Hopp <karsten@redhat.de>
- remove obsolete Obsoletes: gnuchess

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jan 25 2002 Karsten Hopp <karsten@redhat.de>
- Fix buffer overflow

* Wed Jan 23 2002 Karsten Hopp <karsten@redhat.de> (5.02-4)
- remove ExcludeArch Alpha

* Wed Dec 19 2001 Karsten Hopp <karsten@redhat.de> 5.02-2
- fix #57687  (book.dat not writable)

* Wed Nov 28 2001 Karsten Hopp <karsten@redhat.de>
- Update gnuchess to 5.02
- added URL (#54612)
- ExcludeArch alpha until the compiler is fixed

* Wed Jul 11 2001 Karsten Hopp <karsten@redhat.de>
- dir /usr/lib/games/gnuchess owned by this package

* Sat Jul 07 2001 Karsten Hopp <karsten@redhat.de>
- add BuildRequires  (#45026)

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- rebuid in new environment

* Mon Apr  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Rebuild with new ncurses
- do NOT update to 5.00 because it sucks: The UI is gone, the print
  tools are gone, and the Makefile contains DOS-specific instructions.

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Sat Aug 14 1999 Bill Nottingham <notting@redhat.com>
- provide chessprogram, don't require xboard

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 4.0pl80

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Mon Jan 25 1999 Michael Maher <mike@redhat.com>
- changed group name

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- rebuilt for 6.0, cleaned up spec file.

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- BuildRoot'ed

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
