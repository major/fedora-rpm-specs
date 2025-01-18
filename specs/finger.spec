%global _hardened_build 1

Summary: The finger client
Name: finger
Version: 0.17
Release: 81%{?dist}
License: BSD-4-Clause-UC

Source0: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit/bsd-finger-%{version}.tar.gz
Source1: finger.socket
Source2: finger@.service
#BSD license text from sources
Source3: COPYING

Patch1: bsd-finger-0.16-pts.patch
Patch2: bsd-finger-0.17-exact.patch
Patch3: bsd-finger-0.16-allocbroken.patch
Patch4: bsd-finger-0.17-rfc742.patch
Patch5: bsd-finger-0.17-time.patch
Patch6: bsd-finger-0.17-usagi-ipv6.patch
Patch7: bsd-finger-0.17-typo.patch
Patch8: bsd-finger-0.17-strip.patch
Patch9: bsd-finger-0.17-utmp.patch
Patch10: bsd-finger-wide-char-support5.patch
Patch11: bsd-finger-0.17-init-realname.patch
Patch12: bsd-finger-0.17-host-info.patch
Patch13: bsd-finger-0.17-match_sigsegv.patch
Patch14: bsd-finger-0.17-man_page_systemd.patch
Patch15: bsd-finger-0.17-coverity-bugs.patch

# gcc is no longer in buildroot by default
BuildRequires: gcc
# uses make
BuildRequires: make
# uses autosetup
BuildRequires: git-core

BuildRequires: glibc-devel, systemd
BuildRequires: %{__perl}

%description
Finger is a utility which allows users to see information about system
users (login name, home directory, name, how long they've been logged
in to the system, etc.).  The finger package includes a standard
finger client.

You should install finger if you'd like to retrieve finger information
from other systems.

%package server
Summary: The finger daemon
Requires:         finger
Requires:         systemd
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description server
Finger is a utility which allows users to see information about system
users (login name, home directory, name, how long they've been logged
in to the system, etc.).  The finger-server package includes a standard
finger server. The server daemon (fingerd) must be started using 
systemctl to receive finger requests.

You should install finger-server if your system is used by multiple users
and you'd like finger information to be available.


%prep
%autosetup -n bsd-finger-%{version} -S git

install -m 644 %{SOURCE3} COPYING


%build
%set_build_flags
sh configure --enable-ipv6
%{__perl} -pi -e '
	s,^CC=.*$,CC=gcc,;
	s,^CFLAGS=.*,CFLAGS=\$(RPM_OPT_FLAGS),;
	s,^BINDIR=.*$,BINDIR=%{_bindir},;
	s,^MANDIR=.*$,MANDIR=%{_mandir},;
	s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
	s,^LDFLAGS=.*$,LDFLAGS=\$(RPM_LD_FLAGS),;
	' MCONFIG

%make_build


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man{1,8}
mkdir -p %{buildroot}%{_sbindir}

mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}

%make_install INSTALLROOT=%{buildroot}


%post server
%systemd_post finger.socket


%preun server
%systemd_preun finger.socket


%postun server
%systemd_postun_with_restart finger.socket


%files
%doc COPYING
%attr(0755,root,root) %{_bindir}/finger
%{_mandir}/man1/finger.1*


%files server
%doc COPYING
%{_unitdir}/finger.socket
%{_unitdir}/finger@.service
%attr(0755,root,root) %{_sbindir}/in.fingerd
%{_mandir}/man8/in.fingerd.8*
%{_mandir}/man8/fingerd.8*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Zdenek Dohnal <zdohnal@redhat.com> - 0.17-79
- 2292737 - systemd for finger-server uses user nobody

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 23 2023 Zdenek Dohnal <zdohnal@redhat.com> - 0.17-76
- SPDX migration, update spec file

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-75
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.17-70
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 0.17-68
- make is no longer in buildroot by default

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Zdenek Dohnal <zdohnal@redhat.com> - 0.17-62
- gcc is no longer in buildroot by default

* Thu Feb 08 2018 Zdenek Dohnal <zdohnal@redhat.com> - 0.17-61
- remove old stuff https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MRWOMRZ6KPCV25EFHJ2O67BCCP3L4Y6N/

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.17-57
- Add BR: %%{__perl} (Fix F26FTBFS).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Tomas Hozza <thozza@redhat.com> - 0.17-51
- finger-server now requires finger utility

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Tomas Hozza <thozza@redhat.com> - 0.17-49
- Compile finger with Full RELRO
- Explicitly use gcc
- Use only RPM_OPT_FLAGS and RPM_LD_FLAGS
- Add systemd as BuildRequires because of unitdir macro

* Mon Feb 11 2013 Tomas Hozza <thozza@redhat.com> - 0.17-48
- Fixing errors found by static analysis of code (Coverity) (#909325)

* Fri Nov 23 2012 Tomas Hozza <thozza@redhat.com> - 0.17-47
- Provide native systemd service file (#737178)
- SPEC file cleanup

* Tue Oct 16 2012 Tomas Hozza <thozza@redhat.com> - 0.17-46
- finger segfaults if pw->pw_gecos is NULL (#866873)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Petr Lautrbach <plautrba@redhat.com> 0.17-42
- print user host information in better format  (#532414) - <spoyarek@redhat.com>

* Mon Jul 12 2010 Petr Lautrbach <plautrba@redhat.com> 0.17-41
- fix UTF-8 output in list of logged users (#490443)

* Thu Jul 08 2010 Petr Lautrbach <plautrba@redhat.com> 0.17-40
- added license text

* Mon Sep  7 2009 Radek Vokal <rvokal@redhat.com> - 0.17-39
- init realname fix (#520203)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.17-36
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Radek Vokál <rvokal@redhat.com> - 0.17-35
- rebuilt

* Sun Feb  4 2007 Radek Vokál <rvokal@redhat.com> - 0.17-34
- finger server permissions (#225754)

* Sun Feb  4 2007 Radek Vokál <rvokal@redhat.com> - 0.17-33
- spec files cleanups according to MergeReview (#225754)
- dist tag added

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.17-32.2.1.1
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.17-32.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.17-32.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.17-32.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Dec 15 2005 Radek Vokal <rvokal@redhat.com> 0.17-32
- another UTF-8 fix

* Tue Dec 13 2005 Radek Vokal <rvokal@redhat.com> 0.17-31
- real UTF-8 patch by <bnocera@redhat.com>

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 28 2005 Radek Vokal <rvokal@redhat.com> 0.17-30
- make finger UTF-8 happy (#174352)

* Wed Jul 13 2005 Radek Vokal <rvokal@redhat.com> 0.17-29
- make finger world readable (#162643)

* Fri Mar 04 2005 Radek Vokal <rvokal@redhat.com> 0.17-28
- gcc4 rebuilt

* Wed Feb 09 2005 Radek Vokal <rvokal@redhat.com> 0.17-27
- rebuilt to get fortified

* Mon Sep 06 2004 Radek Vokal <rvokal@redhat.com> 0.17-26
- rebuilt

* Tue Jun 15 2004 Alan Cox <alan@redhat.com>
- Made finger agree with our other apps about how utmp is managed
- Removed dead users from the lists as a result
- Fixed random idle time bug

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 25 2004 Phil Knirsch <pknirsch@redhat.com> 0.17-21
- rebuilt
- Made fingerd PIE.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Sep 01 2003 Phil Knirsch <pknirsch@redhat.com> 0.17-18.1
- rebuilt

* Mon Sep 01 2003 Phil Knirsch <pknirsch@redhat.com> 0.17-18
- Fixed manpage bug (#75705).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com> 0.17-17
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 0.17-16
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.17-15
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.17-14
- automated rebuild

* Wed Jun 19 2002 Phil Knirsch <pknirsch@redhat.com> 0.17-13
- Don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jan 24 2002 Phil Knirsch <pknirsch@redhat.com>
- Fixed various typos in manpage/app (#51891, #54916, #57588)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Apr 18 2001 Crutcher Dunnavant <crutcher@redhat.com>
- Approved
- * Sun Mar 11 2001 Pekka Savola <pekkas@netcore.fi>
- - Add IPv6 support from USAGI, update to 0.17 final (no changes)

* Tue Feb 27 2001 Preston Brown <pbrown@redhat.com>
- noreplace xinetd.d config file

* Mon Feb 12 2001 Crutcher Dunnavant <crutcher@redhat.com>
- time patch to handle time.h moving, credit to howarth@fuse.net
- closes bug #26766

* Fri Dec  1 2000 Trond Eivind Glomsred <teg@redhat.com>
- make sure finger is turned off by default

* Sun Aug 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- add patch to always call getpwnam() instead of just when -m is specified

* Sat Jul 22 2000 Jeff Johnson <jbj@redhat.com>
- fix RFC742 problem (again) (#6728).

* Tue Jul 18 2000 Bill Nottingham <notting@redhat.com>
- add description & default to xinetd file

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- update to 0.17.

* Wed May 31 2000 Cristian Gafton <gafton@redhat.com>
- fix the broken malloc code in finger client

* Mon May 22 2000 Trond Eivind Glomsred <teg@redhat.com>
- converted to use /etc/xinetd.d

* Tue May 16 2000 Chris Evans <chris@ferret.lmh.ox.ac.uk>
- make some files mode -rwx--x--x as a security hardening measure 

* Fri Feb 11 2000 Bill Nottingham <notting@redhat.com>
- fix description

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description
- man pages are compressed

* Tue Jan  4 2000 Bill Nottingham <notting@redhat.com>
- split client and server

* Tue Dec 21 1999 Jeff Johnson <jbj@redhat.com>
- update to 0.16.

* Wed Jul 28 1999 Jeff Johnson <jbj@redhat.com>
- exact match w/o -m and add missing pts patch (#2118).
- recompile with correct PATH_MAILDIR (#4218).

* Thu Apr  8 1999 Jeff Johnson <jbj@redhat.com>
- fix process table filled DOS attack (#1271)
- fix pts display problems (#1987 partially)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- fix error message typo.

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added check for getpwnam() failure
