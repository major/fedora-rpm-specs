Summary: Talk client for one-on-one Internet chatting
Name: talk
Version: 0.17
Release: 72%{?dist}
License: BSD-4-Clause-UC AND BSD-3-Clause
# URL: There's no upstream URL at the moment, here's the latest one.
URL: http://web.archive.org/web/20070817165301/http://www.hcs.harvard.edu/~dholland/computers/netkit.html

Source: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit/netkit-ntalk-%{version}.tar.gz
# Source1: systemd socket file
Source1: ntalk.socket
# Source2: systemd service file
Source2: ntalk.service
# Patch0: Includes time.h to the relevant files.
Patch0: netkit-ntalk-0.17-pre20000412-time.patch
# Patch1: We don't want to strip compiled files.
Patch1: netkit-ntalk-0.17-strip.patch
# Patch2: Small socket fix.
Patch2: netkit-ntalk-0.17-sockopt.patch
# Patch3: Adds i18n.
Patch3: netkit-ntalk-0.17-i18n.patch
# Patch4: Fixes spurious 0x9a ("^Z") on window resize.
Patch4: netkit-ntalk-0.17-resize.patch
# Patch5: Adds support (via new flag) for user names containing dot character
Patch5: netkit-ntalk-0.17-person.patch
BuildRequires: make
BuildRequires: ncurses-devel systemd
BuildRequires: %{__perl}
BuildRequires: gcc

%description
The talk package provides client programs for the Internet talk 
protocol, which allows you to chat with other users on different
systems.  Talk is a communication program which copies lines from one
terminal to the terminal of another user.

Install talk if you'd like to use talk for chatting with users on
different systems.

%package server
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Obsoletes: ntalk < %{version}-%{release}
Provides: ntalk = %{version}-%{release}
Summary: The talk server for one-on-one Internet chatting

%description server
The talk-server package provides daemon programs for the Internet talk
protocol, which allows you to chat with other users on different
machines.  Talk is a communication program which copies lines from one
terminal to the terminal of another user.

%prep
%setup -q -n netkit-ntalk-%{version}
%autopatch -p1

%build
./configure --with-c-compiler=cc
%{__perl} -pi -e '
    s,-O2,\$(RPM_OPT_FLAGS) -D_GNU_SOURCE -fpic -I/usr/include/ncursesw,;
    s,^LDFLAGS=,LDFLAGS=-pie,;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    s,^LIBCURSES=.*$,LIBCURSES=-lncursesw,;
    ' MCONFIG
%ifarch s390 s390x
%{__perl} -pi -e 's,-fpic,-fPIC,;' MCONFIG
%endif
make

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,8}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}

make INSTALLROOT=${RPM_BUILD_ROOT} install

mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/ntalk.socket
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/ntalk.service

%files
%{_bindir}/talk
%{_mandir}/man1/*

%files server
%attr(0711,root,root)%{_sbindir}/in.ntalkd
%{_sbindir}/in.talkd
%{_mandir}/man8/*
%{_unitdir}/ntalk.socket
%{_unitdir}/ntalk.service

%post server
%systemd_post ntalk.service
%systemd_post ntalk.socket

%preun server
%systemd_preun ntalk.service
%systemd_preun ntalk.socket

%postun server
%systemd_postun_with_restart ntalk.service
%systemd_postun_with_restart ntalk.socket

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 31 2023 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.17-68
- SPDX migration

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.17-63
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.17-57
- Add gcc to BuildRequires
  Resolves: #1606484

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.17-52
- Add BR: %%{__perl} (Fix F26FTBFS).

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 28 2013 Vitezslav Crhonek <vcrhonek@redhat.com> -  0.17-46
- Fix FTBFS
  Resolves: #992771

* Mon Aug 05 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.17-45
- Fix wrong description of talk parameter in man page

* Sun Aug  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.17-44
- Fix FTBFS

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 02 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.17-42
- Add systemd support (thanks to Zbigniew Jędrzejewski-Szmek and Jóhann B. Guðmundsson)
  Resolves: #737219

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 10 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.17-40
- Fix issues found by fedora-review utility in the spec file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 18 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.17-37
- Improve message with response directions to reflect new option
  for user names with dot character

* Mon Mar 28 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.17-36
- Add support for user names with dot character

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar  2 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.17-34
- Add dist tag, fix buildroot, defattr, obsoletes, provides and summary,
  comment patches and sources
  Resolves: #226476

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.17-33.2.4
- Convert specfile to UTF-8.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-32.2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-31.2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.17-30.2.4
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.17-29.2.4
- Rebuild

* Thu Aug 23 2007 Vitezslav Crhonek <vcrhonek@redhat.com> 0.17-29.2.3
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.17-29.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.17-29.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.17-29.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Mar 25 2005 Miloslav Trmac <mitr@redhat.com> - 0.17-29
- Fix spurious 0x9a ("^Z") on window resize

* Sat Mar  5 2005 Miloslav Trmac <mitr@redhat.com> - 0.17-28
- Rebuild with gcc 4

* Thu Jul 29 2004 Jindrich Novy <jnovy@redhat.com> 0.17-27
- patch to handle input in UTF-8 from Miloslav Trmac (#143818)

* Thu Jul 29 2004 Jindrich Novy <jnovy@redhat.com>
- Patch to prevent using deprecated SO_BSDCOMPAT setsockopt.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 12 2004 Phil Knirsch <pknirsch@redhat.com> 0.17-24
- Enables PIE for server and application.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 04 2004 Phil Knirsch <pknirsch@redhat.com> 0.17-22
- Fixed copyright to license.
- Fixed description for main package (#114683).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb  4 2003 Tim Waugh <twaugh@redhat.com> 0.17-20
- Only one of the built packages should obsolete/provide ntalk.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.17-18
- rebuild on all arches

* Fri Jul 05 2002 Phil Knirsch <pknirsch@redhat.com> 0.17-17
- Fixed problem in IPv6 environment (#67769).

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.17-16
- automated rebuild

* Wed Jun 19 2002 Phil Knirsch <pknirsch@redhat.com> 0.17-15
- Don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jul 24 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed missing BuildRequires: ncurses-devel (#49711)

* Fri Jun 22 2001 Philipp Knirsch <pknirsch@redhat.de>
- Update to latest stable netkit package (0.17)

* Wed Apr  4 2001 Jakub Jelinek <jakub@redhat.com>
- don't let configure to guess compiler, it can pick up egcs

* Tue Feb 27 2001 Preston Brown <pbrown@redhat.com>
- %%config(noreplace) xinetd.d files

* Fri Feb 23 2001 Jakub Jelinek <jakub@redhat.com>
- make it build under glibc 2.2.2

* Wed Aug 23 2000 Nalin Dahyabhai <nalin@redhat.com>
- default to being disabled

* Tue Jul 18 2000 Bill Nottingham <notting@redhat.com>
- add description & default to xinetd file

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- update to 0.17-pre20000412.

* Tue May 23 2000 Trond Eivind Glomsrød <teg@redhat.com>
- switch to xinetd

* Tue May 16 2000 Chris Evans <chris@ferret.lmh.ox.ac.uk>
- make daemons mode -rwx--x--x as a security hardening measure 

* Fri Mar 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.17

* Wed Feb  9 2000 Jeff Johnson <jbj@redhat.com>
- compress man pages (again).

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix descriptions
- man pages are compressed

* Tue Jan  4 2000 Bill Nottingham <notting@redhat.com>
- split client and server

* Wed Dec 22 1999 Jeff Johnson <jbj@redhat.com>
- update to 0.16.

* Sat Aug 21 1999 Jeff Johnson <jbj@redhat.com>
- build for 6.1.

* Sun Jun 20 1999 Jeff Johnson <jbj@redhat.com>
- handle both talk and otalk packets (#2799).

* Fri Apr  9 1999 Jeff Johnson <jbj@redhat.com>
- update to multi-homed 0.11 version.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 14 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
