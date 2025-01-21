Summary: Client for sending messages to a host's logged in users
Name: rwall
Version: 0.17
Release: 69%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Url: ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/
Source: ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-rwall-%{version}.tar.gz
Source1: rwalld.service
Patch1: netkit-rwalld-0.10-banner.patch
Patch2: netkit-rwall-0.17-strip.patch
Patch3: netkit-rwall-0.17-netgroup.patch
Patch4: netkit-rwall-0.17-droppriv.patch
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl-interpreter
BuildRequires: libtirpc-devel
BuildRequires: libnsl2-devel
BuildRequires: rpcgen

%description
The rwall command sends a message to all of the users logged into a
specified host.  Actually, your machine's rwall client sends the
message to the rwall daemon running on the specified host, and the
rwall daemon relays the message to all of the users logged in to that
host.

Install rwall if you'd like the ability to send messages to users
logged in to a specified host machine.

%package server
Summary: Server for sending messages to a host's logged in users
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires: portmap
BuildRequires: systemd-units

%description server
The rwall command sends a message to all of the users logged into
a specified host.  The rwall-server package contains the daemon for
receiving such messages, and is disabled by default on Red Hat Linux
systems (it can be very annoying to keep getting all those messages
when you're trying to play Quake--I mean, trying to get some work done).

Install rwall-server if you'd like the ability to receive messages
from users on remote hosts.

%prep
%setup -q -n netkit-rwall-%{version}
%patch -P1 -p1 -b .banner
%patch -P2 -p1 -b .strip
%patch -P3 -p1 -b .netgroup
%patch -P4 -p1 -b .droppriv

%{__perl} -pi -e '
    s|^LDFLAGS=|LDFLAGS="-pie -Wl,-z,relro,-z,now -ltirpc"|;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' configure

%build
export CFLAGS="$CFLAGS -I/usr/include/tirpc"
%ifarch s390 s390x
CFLAGS="$CFLAGS $RPM_OPT_FLAGS -fPIC" \
%else
CFLAGS="$CFLAGS $RPM_OPT_FLAGS -fpic" \
%endif
sh configure --with-c-compiler=gcc
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,8}
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}/

make INSTALLROOT=${RPM_BUILD_ROOT} install

install -m 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_unitdir}/

%post server
%systemd_post rwalld.service

%preun server
%systemd_preun rwalld.service

%postun server
%systemd_postun_with_restart rwalld.service

%files
%{_bindir}/rwall
%{_mandir}/man1/rwall.1*

%files server
%{_sbindir}/rpc.rwalld
%{_mandir}/man8/rpc.rwalld.8*
%{_mandir}/man8/rwalld.8*
%{_unitdir}/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.17-68
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Björn Esser <besser82@fedoraproject.org> - 0.17-61
- Rebuild(libnsl2)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.17-59
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Petr Kubat <pkubat@redhat.com> - 0.17-53
- Add BuildRequires for gcc (#1606285)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Petr Kubat <pkubat@redhat.com> - 0.17-51
- Remove explicit requires

* Thu Mar 15 2018 Petr Kubat <pkubat@redhat.com> - 0.17-50
- Add dependencies on libtirpc, libnsl2 and rpcgen (#1556427)
  Related to: https://fedoraproject.org/wiki/Changes/SunRPCRemoval

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Petr Kubat <pkubat@redhat.com> - 0.17-46
- Add BuildRequires for perl

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Honza Horak <hhorak@redhat.com> - 0.17-40
- Remove syslog.target from unit file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Honza Horak <hhorak@redhat.com> - 0.17-38
- Build the daemon with full relro

* Thu Oct 04 2012 Honza Horak <hhorak@redhat.com> - 0.17-37
- Run %%triggerun regardless of systemd_post variable definition

* Tue Sep 11 2012 Honza Horak <hhorak@redhat.com> - 0.17-36
- added ordering dependencies to rpcbind
- Minor spec file changes
- Use new systemd macros (Resolves: #850303)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 01 2011 Honza Horak <hhorak@redhat.com> - 0.17-33
- added systemd native unit file

* Mon Aug 01 2011 Honza Horak <hhorak@redhat.com> - 0.17-32
- moved privileges drop after port reservation to handle 
  a bug similar to #247985
- fixed rpmlint errors

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.17-28
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.17-27
- Rebuild for selinux ppc32 issue.

* Mon Jul 23 2007 Jiri Moskovcak <jmoskovc@redhat.com> - 0.17-26
- init script rewrite to comply with the LSB standard
- Resolves: #247048

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.17-25.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.17-25.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.17-25.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> 0.17-25
- bump release and rebuild with gcc 4

* Fri Feb 18 2005 Phil Knirsch <pknirsch@redhat.com> 0.17-24
- rebuilt

* Thu Sep 02 2004 Phil Knirsch <pknirsch@redhat.com> 0.17-22
- Add netgroup feature (#62868)
- Fix garbage character at end of output (#62868)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com> 0.17-21
- rebuilt

* Wed May 12 2004 Phil Knirsch <pknirsch@redhat.com>  0.17-20
- Enabled PIE for server and application.
- Switch from Copyright to License.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.17-16
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Phil Knirsch <pknirsch@redhat.com> 0.17-14
- Don't forcibly strip binaries

* Tue Jun 04 2002 Phil Knirsch <pknirsch@redhat.com>
- bumped release number and rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Apr  4 2001 Jakub Jelinek <jakub@redhat.com>
- don't let configure to guess compiler, it can pick up egcs

* Tue Feb 13 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- also set $prog to rwalld to get it working

* Tue Feb 13 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- use $prog instead of $0 for nicer output

* Thu Feb  8 2001 Preston Brown <pbrown@redhat.com>
- fix up init script to use $0 for i18n reasons (#26566).

* Mon Feb  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- i18nize init script (#26081)

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

* Fri Feb 11 2000 Bill Nottingham <notting@redhat.com>
- fix description

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man pages.

* Sat Feb  5 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- change %%postun to %%preun

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix descriptions and summary
- man pages are compressed

* Mon Jan  4 2000 Bill Nottingham <notting@redhat.com>
- split client and server

* Tue Dec 21 1999 Jeff Johnson <jbj@redhat.com>
- update to 0.16.

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscript

* Tue Oct 28 1997 Erik Troan <ewt@redhat.com>
- fixed init script (didn't include function library)
- doesn't invoke wall with -n anymore

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- added a chkconfig compatible initscript
- added %%attr attributes

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
