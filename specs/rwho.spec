Summary: Displays who is logged in to local network machines
Name: rwho
Version: 0.17
Release: 79%{?dist}
# part of rwhod is under GPL+, other parts are under BSD
# Automatically converted from old format: BSD and GPL+ - review is highly recommended.
License: LicenseRef-Callaway-BSD AND GPL-1.0-or-later
Source: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit/netkit-rwho-%{version}.tar.gz
Source1: rwhod.service
Patch0: rwho-0.15-alpha.patch
Patch1: rwho-0.17-bug22014.patch
Patch2: rwho-0.17-fixbcast.patch
Patch3: rwho-0.17-fixhostname.patch
Patch4: rwho-0.17-strip.patch
Patch5: rwho-0.17-include.patch
Patch6: rwho-0.17-wd_we.patch
Patch7: rwho-0.17-time.patch
Patch8: rwho-0.17-gcc4.patch
Patch9: rwho-0.17-waitchild.patch
Patch10: rwho-0.17-neighbours.patch
Patch11: rwho-0.17-hostnamelen.patch
Patch12: rwho-0.17-stderr.patch
Patch13: rwho-c99.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: make
BuildRequires: gcc
BuildRequires: systemd, perl-interpreter

%description
The rwho command displays output similar to the output of the who
command (it shows who is logged in) for all machines on the local
network running the rwho daemon.

Install the rwho command if you need to keep track of the users who
are logged in to your local network.

%prep
%setup -q -n netkit-rwho-%{version}
%patch -P0 -p1 -b .alpha
%patch -P1 -p1 -b .bug22014
%patch -P2 -p1 -b .fixbcast
%patch -P3 -p1 -b .fixhostname
%patch -P4 -p1 -b .strip
%patch -P5 -p1 -b .include
%patch -P6 -p1 -b .wd_we
%patch -P7 -p1 -b .time
%patch -P8 -p1 -b .gcc4
%patch -P9 -p1 -b .waitchild
%patch -P10 -p1 -b .neighbours
%patch -P11 -p1 -b .hostnamelen
%patch -P12 -p1 -b .stderr
%patch -P13 -p1

%{__perl} -pi -e '
    s|^LDFLAGS=|LDFLAGS="-pie -Wl,-z,relro,-z,now"|;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' configure

%build
%ifarch s390 s390x
CFLAGS="$RPM_OPT_FLAGS -I../include -fPIC" \
%else
CFLAGS="$RPM_OPT_FLAGS -I../include -fpic" \
%endif
sh configure --with-c-compiler=gcc
make %{?_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,8}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
mkdir -p ${RPM_BUILD_ROOT}/var/spool/rwho

make INSTALLROOT=${RPM_BUILD_ROOT} install
make INSTALLROOT=${RPM_BUILD_ROOT} install -C ruptime

install -m 644 %SOURCE1 ${RPM_BUILD_ROOT}%{_unitdir}/rwhod.service

%post
%systemd_post rwhod.service

%preun
%systemd_preun rwhod.service

%postun
%systemd_postun_with_restart rwhod.service

%files
%doc README
%{_bindir}/ruptime
%{_mandir}/man1/ruptime.1*
%{_bindir}/rwho
%{_mandir}/man1/rwho.1*
%{_sbindir}/rwhod
%{_mandir}/man8/rwhod.8*
/var/spool/rwho
%{_unitdir}/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.17-78
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-75
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 04 2023 Florian Weimer <fweimer@redhat.com> - 0.17-74
- Fix C99 compatibility issue (#2167090)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.17-69
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Petr Kubat <pkubat@redhat.com> - 0.17-63
- Add BuildRequires for gcc (#1606286)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Petr Kubat <pkubat@redhat.com> - 0.17-58
- Start rwhod after the network is properly configured (#1473089)

* Mon Feb 13 2017 Petr Kubat <pkubat@redhat.com> - 0.17-57
- Add BuildRequires for perl

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jul 29 2013 Honza Horak <hhorak@redhat.com> - 0.17-52
- Use systemd instead of systemd-units

* Fri May 24 2013 Honza Horak <hhorak@redhat.com> - 0.17-51
- Remove syslog.target from unit requries, it doesn't need to exist

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Honza Horak <hhorak@redhat.com> - 0.17-49
- Build the daemon with full relro

* Fri Nov 16 2012 Honza Horak <hhorak@redhat.com> - 0.17-48
- Spec file clean up according comments from Ville Skytta
  Related: #873838

* Wed Nov 07 2012 Honza Horak <hhorak@redhat.com> - 0.17-47
- Remove linkage against systemd-daemon
- Print errors into stderr

* Fri Oct 05 2012 Honza Horak <hhorak@redhat.com> - 0.17-45
- Remove sdnotify message, while it doesn't work with forking service

* Thu Oct 04 2012 Honza Horak <hhorak@redhat.com> - 0.17-44
- Use sdnotify message to inform systemd the daemon is ready

* Thu Oct 04 2012 Honza Horak <hhorak@redhat.com> - 0.17-43
- Run %%triggerun regardless of systemd_post variable definition

* Tue Sep 11 2012 Honza Horak <hhorak@redhat.com> - 0.17-42
- GPL+ added since part of rwhod is licensed under that license

* Tue Sep 11 2012 Honza Horak <hhorak@redhat.com> - 0.17-41
- Minor spec file cleanup
- Use new systemd macros (Resolves: #850304)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012 Honza Horak <hhorak@redhat.com> - 0.17-39
- removed pid file specification from unit file
  Related: #799246

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Honza Horak <hhorak@redhat.com> - 0.17-37
- systemd unit file mod fix
  removed non-essential Requires: /sbin/chkconfig /etc/init.d
- allow longer hostnames (bug #212076)
- add -n option to ruptime manpage

* Mon Aug 01 2011 Honza Horak <hhorak@redhat.com> - 0.17-36
- added systemd native unit file

* Thu Jun 02 2011 Honza Horak <hhorak@redhat.com> - 0.17-35
- applied patch from Ian Donaldson to transmit status reliably
  (bug #708385)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  26 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 0.17-33
- added README

* Fri Jan  8 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 0.17-32
- fixed rpmlint warnings

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.17-29
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.17-28
- Rebuild for selinux ppc32 issue.

* Mon Jul 23 2007 Jiri Moskovcak <jmoskovc@redhat.com> - 0.17-27
- Fixed init script to comply with the LSB standard
- Resolves: #247049

* Tue Aug 15 2006 Harald Hoyer <harald@redhat.com> - 0.17-26
- exit daemon, if child process dies (bug #202493)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.17-25.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.17-25.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.17-25.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Mar 17 2005 Phil Knirsch <pknirsch@redhat.com> 0.17-25
- gcc4 rebuild fixes

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> 0.17-24
- bump release and rebuild with gcc 4

* Fri Oct 22 2004 Phil Knirsch <pknirsch@redhat.com> 0.17-23
- Fixed long standig bug with only 42 entries per host showing up (#27643)
- Fixed some warnings of missing prototypes.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 12 2004 Phil Knirsch <pknirsch@redhat.com> 0.17-21
- Enabled PIE for server and application.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.17-17
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Phil Knirsch <pknirsch@redhat.com> 0.17-15
- Don't forcibly strip binaries

* Tue Jun 04 2002 Phil Knirsch <pknirsch@redhat.com>
- bumped release number and rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Apr  4 2001 Jakub Jelinek <jakub@redhat.com>
- don't let configure to guess compiler, it can pick up egcs

* Tue Feb 13 2001 Preston Brown <pbrown@redhat.com>
- hostname was getting null terminated incorrectly.  fixed. (#27419)

* Mon Feb  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- i18nize init script (#26083)

* Fri Feb  2 2001 Preston Brown <pbrown@redhat.com>
- don't bcast on virtual interfaces (#20435).  Patch from dwagoner@interTrust.com; thanks.

* Wed Dec 27 2000 Jeff Johnson <jhbj@redhat.com>
- use glibc's <protocols/rwhod.h>, internal version broken on alpha (#22014).

* Thu Aug 10 2000 Bill Nottingham <notting@redhat.com>
- fix broken init script

* Sat Aug 05 2000 Bill Nottingham <notting@redhat.com>
- condrestart fixes

* Thu Jul 20 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Preston Brown <pbrown@redhat.com>
- move initscript

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- update to 0.17.

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man pages.

* Tue Dec 21 1999 Jeff Johnson <jbj@redhat.com>
- update to 0.16.

* Thu Sep 09 1999 Preston Brown <pbrown@redhat.com>
- postun should have been preun.

* Thu Aug 26 1999 Jeff Johnson <jbj@redhat.com>
- fix unaligned trap on alpha.
- update to 0.15.

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Fri Apr  9 1999 Jeff Johnson <jbj@redhat.com>
- add ruptime (#2023)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscripts

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added /var/spool/rwho

* Fri Oct 31 1997 Donnie Barnes <djb@redhat.com>
- fixed init script

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- added an init script
- uses chkconfig
- uses attr tags

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
