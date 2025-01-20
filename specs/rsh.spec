%global _hardened_build 1

Summary: Clients for remote access commands (rsh, rlogin, rcp)
Name: rsh
Version: 0.17
Release: 111%{?dist}
License: BSD-4-Clause-UC

BuildRequires: make
BuildRequires: perl-interpreter, ncurses-devel, pam-devel, audit-libs-devel, systemd, gcc

URL: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit
Source0: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit/netkit-rsh-%{version}.tar.gz
Source1: rexec.pam
Source2: rlogin.pam
Source3: rsh.pam
# Source is no longer publicly available.
Source4: rexec-1.5.tar.gz
Source5: rsh@.service
Source6: rsh.socket
Source7: rlogin@.service
Source8: rlogin.socket
Source9: rexec@.service
Source10: rexec.socket

Patch1: netkit-rsh-0.17-sectty.patch
# Make rexec installation process working
Patch2: netkit-rsh-0.17-rexec.patch
Patch3: netkit-rsh-0.10-stdarg.patch
# Improve installation process
Patch4: netkit-rsh-0.16-jbj.patch
# Link rshd against libpam
Patch8: netkit-rsh-0.16-jbj4.patch
Patch9: netkit-rsh-0.16-prompt.patch
Patch10: netkit-rsh-0.16-rlogin=rsh.patch
# Improve documentation
Patch11: netkit-rsh-0.16-nokrb.patch
# Remove spurious double-reporting of errors
Patch12: netkit-rsh-0.17-pre20000412-jbj5.patch
# RH #42880
Patch13: netkit-rsh-0.17-userandhost.patch
# Don't strip binaries during installation
Patch14: netkit-rsh-0.17-strip.patch
# RH #67362
Patch15: netkit-rsh-0.17-lfs.patch
# RH #57392
Patch16: netkit-rsh-0.17-chdir.patch
# RH #63806
Patch17: netkit-rsh-0.17-pam-nologin.patch
# RH #135643
Patch19: netkit-rsh-0.17-rexec-netrc.patch
# RH #68590
Patch20: netkit-rsh-0.17-pam-sess.patch
# RH #67361
Patch21: netkit-rsh-0.17-errno.patch
# RH #118630
Patch22: netkit-rsh-0.17-rexec-sig.patch
# RH #135827
Patch23: netkit-rsh-0.17-nohost.patch
# RH #122315
Patch24: netkit-rsh-0.17-ignchld.patch
# RH #146464
Patch25: netkit-rsh-0.17-checkdir.patch
Patch26: netkit-rsh-0.17-pam-conv.patch
# RH #174045
Patch27: netkit-rsh-0.17-rcp-largefile.patch
# RH #174146
Patch28: netkit-rsh-0.17-pam-rhost.patch
# RH #178916
Patch29: netkit-rsh-0.17-rlogin-linefeed.patch
Patch30: netkit-rsh-0.17-ipv6.patch
Patch31: netkit-rsh-0.17-pam_env.patch
Patch33: netkit-rsh-0.17-dns.patch
Patch34: netkit-rsh-0.17-nohostcheck-compat.patch
# RH #448904
Patch35: netkit-rsh-0.17-audit.patch
Patch36: netkit-rsh-0.17-longname.patch
# RH #440867
Patch37: netkit-rsh-0.17-arg_max.patch
Patch38: netkit-rsh-0.17-rh448904.patch
Patch39: netkit-rsh-0.17-rh461903.patch
Patch40: netkit-rsh-0.17-rh473492.patch
Patch41: netkit-rsh-0.17-rh650119.patch
Patch42: netkit-rsh-0.17-rh710987.patch
Patch43: netkit-rsh-0.17-rh784467.patch
Patch44: netkit-rsh-0.17-rh896583.patch
Patch45: netkit-rsh-0.17-rh947213.patch
Patch46: 0001-rshd-use-sockaddr_in-for-non-native-IPv6-clients.patch
Patch47: 0002-rlogind-use-sockaddr_in-for-non-native-IPv6-client.patch
Patch48: netkit-rsh-0.17-ipv6-rexec.patch
Patch49: 0001-rshd-include-missing-header-file.patch
Patch50: 0001-rshd-use-upper-bound-for-cmdbuflen.patch   
Patch51: 0001-rcp-don-t-advance-pointer-returned-from-rcp_basename.patch
Patch52: netkit-rsh-0.17-union-wait.patch
Patch53: netkit-rsh-0.17-cmdbuflen.patch
Patch54: netkit-rsh-0.17-CVE-2019-7282.patch
Patch55: netkit-rsh-0.17-c99.patch
Patch56: netkit-rsh-0.17-c99-2.patch

%description
The rsh package contains a set of programs which allow users to run
commands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp).  All three of these commands
use rhosts style authentication.  This package contains the clients
needed for all of these services.
The rsh package should be installed to enable remote access to other
machines

%package server
Summary: Servers for remote access commands (rsh, rlogin, rcp)
Requires: pam, /etc/pam.d/system-auth
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description server
The rsh-server package contains a set of programs which allow users
to run commands on remote machines, login to other machines and copy
files between machines (rsh, rlogin and rcp).  All three of these
commands use rhosts style authentication.  This package contains the
servers needed for all of these services.  It also contains a server
for rexec, an alternate method of executing remote commands.
All of these servers are run by systemd and configured using
systemd units and PAM.

The rsh-server package should be installed to enable remote access
from other machines

%prep
%setup -q -n netkit-rsh-%{version} -a 4
%patch -P1 -p1 -b .sectty
%patch -P2 -p1 -b .rexec
%patch -P3 -p1 -b .stdarg
%patch -P4 -p1 -b .jbj
%patch -P8 -p1 -b .jbj4
%patch -P9 -p1 -b .prompt
%patch -P10 -p1 -b .rsh
%patch -P11 -p1 -b .rsh.nokrb
%patch -P12 -p1 -b .jbj5
%patch -P13 -p1 -b .userandhost
%patch -P14 -p1 -b .strip
%patch -P15 -p1 -b .lfs
%patch -P16 -p1 -b .chdir
%patch -P17 -p1 -b .pam-nologin
%patch -P19 -p1 -b .rexec-netrc
%patch -P20 -p1 -b .pam-sess
%patch -P21 -p1 -b .errno
%patch -P22 -p1 -b .rexec-sig
%patch -P23 -p1 -b .nohost
%patch -P24 -p1 -b .ignchld
%patch -P25 -p1 -b .checkdir
%patch -P26 -p1 -b .pam-conv
%patch -P27 -p1 -b .largefile
%patch -P28 -p1 -b .pam-rhost
%patch -P29 -p1 -b .linefeed
%patch -P30 -p1 -b .ipv6
%patch -P31 -p1 -b .pam_env
%patch -P33 -p1 -b .dns
%patch -P34 -p1 -b .compat
%patch -P35 -p1 -b .audit
%patch -P36 -p1 -b .longname
%patch -P37 -p1 -b .arg_max
%patch -P38 -p1 -b .rh448904
%patch -P39 -p1 -b .rh461903
%patch -P40 -p1 -b .rh473492
%patch -P41 -p1 -b .rh650119
%patch -P42 -p1 -b .rh710987
%patch -P43 -p1 -b .rh784467
%patch -P44 -b .rh896583
%patch -P45 -p1 -b .rh947213
%patch -P46 -p1
%patch -P47 -p1
%patch -P48 -p1 -b .ipv6-rexec
%patch -P49 -p1 -b .waitpid
%patch -P50 -p1
%patch -P51 -p1
%patch -P52 -p1 -b .union-wait
%patch -P53 -p1 -b .cmdbuflen
%patch -P54 -p1 -b .cve-2019-7282
%patch -P55 -p1 -b .c99
%patch -P56 -p1 -b .c99-2

# No, I don't know what this is doing in the tarball.
rm -f rexec/rexec

%build
sh configure --with-c-compiler=%{__cc}
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%ifarch s390 s390x
%{__perl} -pi -e '
    s,^CC=.*$,CC=cc,;
    s,-O2,\$(RPM_OPT_FLAGS) -fPIC -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE,;
    s,^LDFLAGS=,LDFLAGS=\$(RPM_LD_FLAGS),;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' MCONFIG
%else
%{__perl} -pi -e '
    s,^CC=.*$,CC=cc,;
    s,-O2,\$(RPM_OPT_FLAGS) -fpic -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE,;
    s,^LDFLAGS=,LDFLAGS=\$(RPM_LD_FLAGS),;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' MCONFIG
%endif
%{make_build}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man{1,5,8}
mkdir -p %{buildroot}%{_sysconfdir}/pam.d

%{make_install} INSTALLROOT=%{buildroot} BINDIR=%{_bindir} MANDIR=%{_mandir}

install -m 644 %SOURCE1 %{buildroot}%{_sysconfdir}/pam.d/rexec
install -m 644 %SOURCE2 %{buildroot}%{_sysconfdir}/pam.d/rlogin
install -m 644 %SOURCE3 %{buildroot}%{_sysconfdir}/pam.d/rsh

mkdir -p %{buildroot}%{_unitdir}
install -m644 %SOURCE5 %{buildroot}%{_unitdir}/rsh@.service
install -m644 %SOURCE6 %{buildroot}%{_unitdir}/rsh.socket
install -m644 %SOURCE7 %{buildroot}%{_unitdir}/rlogin@.service
install -m644 %SOURCE8 %{buildroot}%{_unitdir}/rlogin.socket
install -m644 %SOURCE9 %{buildroot}%{_unitdir}/rexec@.service
install -m644 %SOURCE10 %{buildroot}%{_unitdir}/rexec.socket

%post server
%systemd_post rsh.socket
%systemd_post rlogin.socket
%systemd_post rexec.socket

%preun server
%systemd_preun rsh.socket
%systemd_preun rlogin.socket
%systemd_preun rexec.socket

%postun server
%systemd_postun_with_restart rsh.socket
%systemd_postun_with_restart rlogin.socket
%systemd_postun_with_restart rexec.socket

%files
%doc README BUGS
%attr(0755,root,root) %caps(cap_net_bind_service=pe) %{_bindir}/rcp
%{_bindir}/rexec
%attr(0755,root,root) %caps(cap_net_bind_service=pe) %{_bindir}/rlogin
%attr(0755,root,root) %caps(cap_net_bind_service=pe) %{_bindir}/rsh
%{_mandir}/man1/*.1*

%files server
%config(noreplace) %{_sysconfdir}/pam.d/rsh
%config(noreplace) %{_sysconfdir}/pam.d/rlogin
%config(noreplace) %{_sysconfdir}/pam.d/rexec
%{_sbindir}/in.rexecd
%{_sbindir}/in.rlogind
%{_sbindir}/in.rshd
%{_unitdir}/*
%{_mandir}/man8/*.8*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-111
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-109
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 21 2023 Florian Weimer <fweimer@redhat.com> - 0.17-107
- Further C compatibility fixes (#2165891)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Michal Ruprich <mruprich@redhat.com> - 0.17-105
- SPDX migration

* Tue Jan 31 2023 Nikita Popov <npopov@redhat.com> - 0.17-104
- Port to C99 (fix rhbz#2165891)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-103
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-102
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Michal Ruprich <mruprich@redhat.com> - 0.17-101
- Fix for CVE-2019-7282

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-100
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.17-98
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-97
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-96
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-95
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Michal Ruprich <mruprich@redhat.com> - 0.17-94
- Resolves: #1797540 - rexecd prints incorrect IP addresses with -D

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-93
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-91
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.17-90
- Rebuilt for libcrypt.so.2 (#1666033)

* Wed Jan 02 2019 Michal Ruprich <mruprich@redhat.com> - 0.17-89
- Fix for rhbz#1503119

* Mon Jul 23 2018 Michal Ruprich <mruprich@redhat.com> - 0.17-88
- Resolves: #1606133 - rsh: FTBFS in Fedora rawhide

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-87
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.17-85
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-84
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-83
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-82
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.17-81
- Drop usage of ancient BSD "union wait" structure
- "union wait" was removed from wait.h in glibc-headers 2.24+

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul  8 2015 Michal Sekletar <msekleta@redhat.com> - 0.17-79
- use upper bound for cmdbuflen
- don't truncate first character of dirname when doing recursive copy
- disable strict aliasing optimizations

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Michal Sekletar <msekleta@redhat.com> - 0.17-75
- include missing header file and make gcc shut up

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Michal Sekletar <msekleta@redhat.com> - 0.17-73
- add IPv6 support to rexec and rexecd
- enable hardened build
- fix dates in changelog

* Wed Jun 26 2013 Michal Sekletar <msekleta@redhat.com> - 0.17-72
- unit files must not be marked as config files
- fix handling of non-native IPv6 connections via AF_INET6 socket

* Thu Apr 11 2013 Michal Sekletar <msekleta@redhat.com> - 0.17-71
- resolves: RHBZ #737244 #896583 #947213
- migrate from xinetd to systemd configuration
- close pam session correctly when client does not ask for separate error channel
- fix pty handling which was broken by changes in /bin/login

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Adam Tkac <atkac redhat com> - 0.17-68
- rcp: handle copying of directories with ending slash well (#784467)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Adam Tkac <atkac redhat com> - 0.17-66
- remove unneeded setpwent/endpwent calls

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010 Adam Tkac <atkac redhat com> - 0.17-64
- fix typo in rexec.c (#650119)

* Mon Nov 08 2010 Adam Tkac <atkac redhat com> - 0.17-63
- use filesystem-based capabilities instead of SUID (#646489)

* Tue Jan 5 2010 Jan Gorig  <jgorig redhat com> - 0.17-62
- add check for return values (#473492)

* Thu Dec 17 2009 Adam Tkac <atkac redhat com> - 0.17-61
- include README and BUGS files as documentation (#226379)

* Tue Dec 15 2009 Adam Tkac <atkac redhat com> - 0.17-60
- more merge review related fixes (#226379)

* Mon Nov 30 2009 Adam Tkac <atkac redhat com> - 0.17-59
- merge review related fixes (#226379)
- remove unused patches
  - netkit-rsh-0.16-pamfix.patch
  - netkit-rsh-0.16-jbj2.patch
  - netkit-rsh-0.16-jbj3.patch

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> - 0.17-58
- use password-auth common PAM configuration instead of system-auth

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.17-57
- rebuilt with new audit

* Tue Aug 11 2009 Adam Tkac <atkac redhat com> 0.17-56
- remove URL from rexec source, it is no longer publicly available

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 30 2009 Adam Tkac <atkac redhat com> 0.17-54
- improve pam_env patch

* Thu Mar 26 2009 Adam Tkac <atkac redhat com> 0.17-53
- check return value from close to catch errors on NFS filesystems (#461903)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 03 2008 Adam Tkac <atkac redhat com> 0.17-51
- updated ipv6 patch due rpm 4.6 (#465053)
- make in.rshd working on kernels without audit support (#448904)

* Fri May 09 2008 Adam Tkac <atkac redhat com> 0.17-50
- fixed typos in arg_max and audit patches (#445606)
- use pam_rhosts, not pam_rhosts_auth (#445606)

* Mon Apr 14 2008 Adam Tkac <atkac redhat com> 0.17-49
- use sysconf for ARG_MAX value (#440867)

* Thu Mar 27 2008 Adam Tkac <atkac redhat com> 0.17-48
- in.rexecd username limit was 14 characters, not 16

* Tue Mar 25 2008 Adam Tkac <atkac redhat com> 0.17-47
- fixed NULL pointer dereference (#437815)
- cleanup in audit patch

* Thu Feb 14 2008 Adam Tkac <atkac redhat com> 0.17-46
- rebuild with gcc4.3
- build with -D_GNU_SOURCE

* Sat Oct 20 2007 Steve Grubb <sgrubb@redhat.com> 0.17-45
- update for audit

* Tue Oct 16 2007 Adam Tkac <atkac redhat com> 0.17-44
- added -D option for compatibility with F8 test releases
- fixed rsh-server description

* Thu Sep 27 2007 Adam Tkac <atkac redhat com> 0.17-43
- removed -D option from rshd and rlogind (we have -a option when
  we need force reverse DNS lookup)
- patches netkit-rsh-0.17-nodns.patch and netkit-rsh-0.17-nohostcheck.patch
  are substituted by netkit-rsh-0.17-dns.patch

* Wed Aug 22 2007 Adam Tkac <atkac redhat com> 0.17-42
- rebuild (BuildID feature)

* Thu Jul 26 2007 Adam Tkac <atkac redhat com> 0.17-41
- improved nodns patch (in.rshd also has -D option now)

* Tue Apr 10 2007 Adam Tkac <atkac redhat com> 0.17-40
- improved -D option to rlogind - when name won't be resolved rlogind uses IP address
- added smp_mflags to make

* Mon Jan 22 2007 Adam Tkac <atkac redhat com> 0.17-39
- rebased on ncurses instead of libtermcap

* Tue Dec 05 2006 Adam Tkac <atkac redhat com> 0.17-38
- rsh now load pan_env module correctly

* Tue Oct 24 2006 Adam Tkac <atkac@redhat.com> 0.17-37
- added xinetd dependency to rsh-server

* Wed Oct  4 2006 Karel Zak <kzak@redhat.com> 0.17-36
- fix #209277 - rsh-server not linked to PAM (missing BuildRequires)

* Mon Jul 17 2006 Karel Zak <kzak@redhat.com> 0.17-35
- added support for IPv6 (patch by Jan Pazdziora)
- fix #198632 - add keyinit instructions to the rsh, rlogin and rexec PAM scripts
  (patch by David Howells)
- fix #191390 - improve linefeed patch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.17-34.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.17-34.1
- bump again for double-long bug on ppc(64)

* Thu Feb  9 2006 Karel Zak <kzak@redhat.com> 0.17-34
- fix #178916 - Line feeds when password needs changing with rlogin

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 0.17-33.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> 0.17-33.1
- rebuilt

* Mon Nov 28 2005 Karel Zak <kzak@redhat.com> 0.17-33
- fix #174146 - pam_access.so does not work with rexecd

* Thu Nov 24 2005 Karel Zak <kzak@redhat.com> 0.17-32
- fix #174045 - rcp outputs negative file size when over 2GB

* Thu Oct 13 2005 Karel Zak <kzak@redhat.com> 0.17-31
- rewrite rexecd PAM_conversation()

* Thu Oct 13 2005 Karel Zak <kzak@redhat.com> 0.17-30
- replace pam_stack with "include"

* Sat Mar  5 2005 Karel Zak <kzak@redhat.com> 0.17-29
- rebuilt

* Thu Feb  3 2005 Karel Zak <kzak@redhat.com> 0.17-28
- malicious rcp server can cause rcp to write to arbitrary files (like scp CAN-2004-0175) (#146464)

* Mon Dec  6 2004 Karel Zak <kzak@redhat.com> 0.17-27
- removed BSD stuff "signal(SIGCHLD, SIG_IGN)". It's unsupported by POSIX/linux. (#122315)

* Sat Dec  4 2004 Karel Zak <kzak@redhat.com> 0.17-26
- "-D" option turns off reverse DNS in rexecd (#135827)

* Wed Nov 17 2004 Karel Zak <kzak@redhat.com> 0.17-25
- rexecd uses PAM session now (#68590)
- fixed errno usage in rcp (#67361)
- fixed rexec fails with "Invalid Argument" (#118630)

* Mon Oct 18 2004 Radek Vokal <rvokal@redhat.com> 0.17-24
- The username and password for ~/.netrc are used (#135643)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 12 2004 Phil Knirsch <pknirsch@redhat.com> 0.17-22
- Added all other tools to list of PIE enabled apps.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb  5 2004 Thomas Woerner <twoerner@redhat.com> 0.17-20
- in.rexecd, in.rlogind and in.rshd are pie, now

* Tue Oct 21 2003 Phil Knirsch <pknirsch@redhat.com> 0.17-19
- Included updated patch from #105733.

* Thu Oct 02 2003 Phil Knirsch <pknirsch@redhat.com> 0.17-18
- Fixed YAT (#79391).
- Included feature request #105733 (-D option).

* Fri Jun 27 2003 Phil Knirsch <pknirsch@redhat.com> 0.17-17.1
- rebuilt

* Thu Jun 26 2003 Phil Knirsch <pknirsch@redhat.com> 0.17-17
- Included chdir patch (#57392).
- Included pam-nologin patch (#63806).

* Tue Jun 17 2003 Phil Knirsch <pknirsch@redhat.com> 0.17-16
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com> 0.17-15
- rebuilt

* Tue May 06 2003 Phil Knirsch <pknirsch@redhat.com>
- Fixed manpages (#7168).

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 17 2003 Phil Knirsch <pknirsch@redhat.com> 0.17-13
- Added LFS support (#67362).
- Fixed user and host patch (#80822).

* Tue Jan 14 2003 Phil Knirsch <pknirsch@redhat.com> 0.17-12
- Fixed bug #79391 (typo in description).

* Mon Nov 11 2002 Nalin Dahyabhai <nalin@redhat.com> 0.17-11
- remove directory names from PAM configuration files, allowing them to be used
  for all arches on multilib systems

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Phil Knirsch <pknirsch@redhat.com> 0.17-9
- Don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 30 2002 Phil Knirsch <pknirsch@redhat.com>
- Bumped version for rebuild
- Added the remote user and host addition (RFE #42880)

* Tue Jul 24 2001 Phil Knirsch <pknirsch@redhat.com>
- Fixed really missing BuildPrereq: libtermcap-devel (#49577)
- Fixed security problem with rexec.pam (#49181)

* Fri Jun 22 2001 Phil Knirsch <pknirsch@redhat.com>
- Update to latest stable version 0.17
- Removed unneeded glib22 patch

* Mon Apr 30 2001 Nalin Dahyabhai <nalin@redhat.com>
- tag xinetd config files as config files

* Wed Apr  4 2001 Jakub Jelinek <jakub@redhat.com>
- don't let configure to guess compiler, it can pick up egcs

* Mon Feb  5 2001 Nalin Dahyabhai <nalin@redhat.com>
- securetty is screwy because rsh doesn't allocate one and rlogin does auth
  before it has a tty, so change the hard-coded TTYs used from "tty" for all
  to "rsh" or "rlogin" or "rexec"

* Tue Oct 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix PAM config files to always honor nologin and securetty, to use rhosts,
  and to fall back to password auth only for rlogin and rexec (#17183)
- add references to pam_env to the PAM configs as well (#16170)
- disable rlogin and rsh by default

* Mon Oct 02 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix typo in the rexec xinetd configuration file (#18107)

* Fri Jul 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix typo in the rlogin PAM config file
- continue the tradition of messed-up release numbers

* Tue Jul 18 2000 Bill Nottingham <notting@redhat.com>
- add description & default to xinetd file

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- update to 0.17.

* Thu Jun  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify PAM setup to use system-auth

* Mon May 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- expunge all mentions of kerberos authentication or DES encryption using
  kerberos from the man pages

* Thu May 25 2000 Trond Eivind Glomsrod <teg@redhat.com>
- switched to xinetd

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Sat Mar 04 2000 Nalin Dahyabhai <nalin@redhat.com>
- make rlogin still work correctly when argv[0] = "rsh"

* Mon Feb 28 2000 Jeff Johnson <jbj@redhat.com>
- workaround (by explicitly prompting for password) #4328 and #9715.

* Wed Feb  9 2000 Jeff Johnson <jbj@redhat.com>
- mark pam config files as %%config.

* Fri Feb  4 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description

* Sun Jan 30 2000 Bill Nottingham <notting@redhat.com>
- remove bogus rexec binary when building; it causes weirdness

* Fri Jan 28 2000 Jeff Johnson <jbj@redhat.com>
- Make sure that rshd is compiled with -DUSE_PAM.

* Mon Jan 10 2000 Jeff Johnson <jbj@redhat.com>
- Fix bug in rshd (hangs forever with zombie offspring) (#8313).

* Wed Jan  5 2000 Jeff Johnson <jbj@redhat.com>
- fix the PAM fix yet again (#8133).

* Tue Jan  4 2000 Bill Nottingham <notting@redhat.com>
- split client and server

* Tue Dec 21 1999 Jeff Johnson <jbj@redhat.com>
- update to 0.16.
- dup setuid bits into files list.

* Fri Jul 30 1999 Jeff Johnson <jbj@redhat.com>
- update to rexec-1.5 client (#4262)

* Wed May 19 1999 Jeff Johnson <jbj@redhat.com>
- fix broken rexec protocol in in.rexecd (#2318).

* Tue May  4 1999 Justin Vallon <vallon@mindspring.com>
- rcp with error was tricked by stdarg side effect (#2300)

* Thu Apr 15 1999 Michael K. Johnson <johnsonm@redhat.com>
- rlogin pam file was missing comment magic

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip rexec

* Fri Mar 26 1999 Jeff Johnson <jbj@redhat.com>
- rexec needs pam_set_item() (#60).
- clarify protocol in rexecd.8.
- add rexec client from contrib.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 14 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Sun Apr  5 1998 Marcelo F. Vianna <m-vianna@usa.net>
- Packaged for RH5.0 (Hurricane)

* Tue Oct 14 1997 Michael K. Johnson <johnsonm@redhat.com>
- new pam conventions

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
