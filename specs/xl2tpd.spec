%global commit 5619e1771048e74b729804e8602f409af0f3faea

Summary: Layer 2 Tunnelling Protocol Daemon (RFC 2661)
Name: xl2tpd
Version: 1.3.17
Release: 8%{?dist}
License: GPL-1.0-or-later
Url: https://github.com/xelerance/xl2tpd/
Source0: https://github.com/xelerance/xl2tpd/archive/refs/tags/v%{version}/xl2tpd-%{version}.tar.gz
Source1: xl2tpd.service
Source2: tmpfiles-xl2tpd.conf
Patch1: xl2tpd-1.3.14-conf.patch
Patch2: xl2tpd-1.3.14-md5-fips.patch
Patch3: xl2tpd-1.3.14-kernelmode.patch
# https://github.com/xelerance/xl2tpd/pull/272
Patch4: xl2tpd-1.3.18-gcc15.patch

Requires: ppp >= 2.4.5-18, kmod(l2tp_ppp.ko)
# If you want to authenticate against a Microsoft PDC/Active Directory
# Requires: samba-winbind
BuildRequires: make
BuildRequires:  gcc
BuildRequires: libpcap-devel
BuildRequires: systemd-units
BuildRequires: openssl-devel
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# dnf resolving prefers kernel-debug-modules-extra over kernel-modules-extra
Suggests: kernel-modules-extra

%description
xl2tpd is an implementation of the Layer 2 Tunnelling Protocol (RFC 2661).
L2TP allows you to tunnel PPP over UDP. Some ISPs use L2TP to tunnel user
sessions from dial-in servers (modem banks, ADSL DSLAMs) to back-end PPP
servers. Another important application is Virtual Private Networks where
the IPsec protocol is used to secure the L2TP connection (L2TP/IPsec,
RFC 3193). The L2TP/IPsec protocol is mainly used by Windows and
Mac OS X clients. On Linux, xl2tpd can be used in combination with IPsec
implementations such as Openswan.
Example configuration files for such a setup are included in this RPM.

xl2tpd works by opening a pseudo-tty for communicating with pppd.
It runs completely in userspace.

xl2tpd supports IPsec SA Reference tracking to enable overlapping internak
NAT'ed IP's by different clients (eg all clients connecting from their
linksys internal IP 192.168.1.101) as well as multiple clients behind
the same NAT router.

xl2tpd supports the pppol2tp kernel mode operations on 2.6.23 or higher,
or via a patch in contrib for 2.4.x kernels.

Xl2tpd is based on the 0.69 L2TP by Jeff McAdams <jeffm@iglou.com>
It was de-facto maintained by Jacco de Leeuw <jacco2@dds.nl> in 2002 and 2003.

%prep
%setup
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
export CFLAGS="$CFLAGS -fPIC -Wall -DTRUST_PPPD_TO_DIE"
export DFLAGS="$RPM_OPT_FLAGS -g "
export LDFLAGS="$LDFLAGS -pie -Wl,-z,relro -Wl,-z,now"
# fixup for obsoleted pppd options
sed -i "s/crtscts/#obsolete: crtscts/" examples/ppp-options.xl2tpd
sed -i "s/lock/#obsolete: lock/" examples/ppp-options.xl2tpd
# if extra debugging is needed, use:
# %make_build DFLAGS="$RPM_OPT_FLAGS -g -DDEBUG_HELLO -DDEBUG_CLOSE -DDEBUG_FLOW -DDEBUG_PAYLOAD -DDEBUG_CONTROL -DDEBUG_CONTROL_XMIT -DDEBUG_FLOW_MORE -DDEBUG_MAGIC -DDEBUG_ENTROPY -DDEBUG_HIDDEN -DDEBUG_PPPD -DDEBUG_AAA -DDEBUG_FILE -DDEBUG_FLOW -DDEBUG_HELLO -DDEBUG_CLOSE -DDEBUG_ZLB -DDEBUG_AUTH"
%make_build

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} SBINDIR=%{buildroot}%{_sbindir} install
install -d 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/xl2tpd.service
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}/%{name}.conf

install -p -D -m644 examples/xl2tpd.conf %{buildroot}%{_sysconfdir}/xl2tpd/xl2tpd.conf
install -p -D -m644 examples/ppp-options.xl2tpd %{buildroot}%{_sysconfdir}/ppp/options.xl2tpd
install -p -D -m600 doc/l2tp-secrets.sample %{buildroot}%{_sysconfdir}/xl2tpd/l2tp-secrets
install -p -D -m600 examples/chapsecrets.sample %{buildroot}%{_sysconfdir}/ppp/chap-secrets.sample
install -p -D -m755 -d %{buildroot}%{_rundir}/xl2tpd

%preun
%systemd_preun xl2tpd.service

%post
%systemd_post xl2tpd.service

%postun
%systemd_postun_with_restart xl2tpd.service

%triggerun -- xl2td < 1.3.1-3
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply xl2tpd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save xl2tpd >/dev/null 2>&1 ||:
# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del xl2tpd >/dev/null 2>&1 || :
/bin/systemctl try-restart xl2tpd.service >/dev/null 2>&1 || :

%files
%doc BUGS CHANGES CREDITS README.* TODO
%license LICENSE
%doc doc/README.patents examples/chapsecrets.sample
%{_sbindir}/xl2tpd
%{_sbindir}/xl2tpd-control
%{_bindir}/pfc
%{_mandir}/*/*
%dir %{_sysconfdir}/xl2tpd
%config(noreplace) %{_sysconfdir}/xl2tpd/*
%config(noreplace) %{_sysconfdir}/ppp/*
%dir %{_rundir}/xl2tpd
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%ghost %attr(0600,root,root) %{_rundir}/xl2tpd/l2tp-control

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.17-5
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 19 2022 Paul Wouters <paul.wouters@aiven.io - 1.3.17-1
- Resolves: rhbz#2043773 xl2tpd-1.3.17 is available (no material change from 1.3.16)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.3.16-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Paul Wouters <paul.wouters@aiven.io> - 1.3.16-1
- Resolves: rhbz#1891104 xl2tpd-1.3.16 is available

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.15-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Paul Wouters <pwouters@redhat.com> - 1.3.15-1
- Resolves: rhbz#1761700 xl2tpd-1.3.15 is available
- Resolves: rhbz#1875262 Unsupported options 'crtscts' and 'lock' in /etc/ppp/options.xl2tpd
- Resolves: rhbz#1869420 xl2tpd.service:8: PIDFile= references a path below legacy directory /var/run/

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Paul Wouters <pwouters@redhat.com> - 1.3.14-1
- Resolves: rhbz#1322190 Updated to 1.3.14
- Resolves: rhbz#1722121 Use proper /run directory
- Resolves: rhbz#1399648 Review Request: xl2tpd

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 01 2018 Paul Wouters <pwouters@redhat.com> - 1.3.8-7
- Resolves: rhbz#1562512 kernels 4.15 and 4.16 break xl2tpd

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Paul Wouters <pwouters@redhat.com> - 1.3.8-2
- Very reluctantly add a Suggests: tag to work around dnf/kernel bug
- Resolves: rhbz#1192189 Both kernel-debug-core and kernel-core are installed

* Wed Aug 24 2016 Paul Wouters <pwouters@redhat.com> - 1.3.8-1
- Upgraded to 1.3.8 and updated existing patches still required
- Fix kernel mode breaking the closing tunnels

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Paul Wouters <pwouters@redhat.com> - 1.3.6-8
- Bump EVR

* Tue Mar 31 2015 Paul Wouters <pwouters@redhat.com> - 1.3.6-7
- Rebuild with -DTRUST_PPPD_TO_DIE so pppd will execute its down script

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 1.3.6-6
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 Paul Wouters <pwouters@redhat.com> - 1.3.6-4
- Resolves rhbz#1109470 l2tpd/ipsec breaks when "ipsec saref" not set

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Switch to using Requires on individual kernel modules
- Resolves rhbz#1056192

* Tue May 13 2014 Paul Wouters <pwouters@redhat.com> - 1.3.6-1
- Updated to 1.3.6 - using github-only monstrosity packaging
- Resolves: rhbz#1051785 (new upstream version available)
- Resolves: rhbz#868391 xl2tpd sends response packets from wrong IP address
- Revert: rhbz#929447 Incorrect "ipparam" manipulation
- Resolves: rhbz#1055196 Don't order service after syslog.target
- Resolves: rhbz#984332 xl2tpd tmpfiles configuration file in wrong directory
- Removed patches merged in upstream.
- FIPS patch updated with advertising clause for openssl in xl2tpd -V
  (although the GPL code was already basically taken from openssl)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 01 2013 Paul Wouters <pwouters@redhat.com> - 1.3.1-13
- rhbz#929447 - Fix ipparam so ipv6-up does not fail (Michal Bruncko)
- rhbz#850372 - Introduce new systemd-rpm macros in xl2tpd spec file
- Use relro,pie for compiling
- rhbz#947209 - Use openssl's MD5 function instead of private copy
  (so FIPS restrictions work)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Paul Wouters <pwouters@redhat.com> - 1.3.1-10
- Updated comments in config files on how to authenticate against
  a Windows PDC / Active Directory

* Tue Jul 03 2012 Paul Wouters <pwouters@redhat.com> - 1.3.1-9
- Rename non-existing openswan.service to ipsec.service (rhbz#836783)
- Start after ipsec.service, but do not require it

* Tue Jun 26 2012 Paul Wouters <pwouters@redhat.com> - 1.3.1-8
- The l2tp_ppp kernel module is now in kernel-module-extra
  (rhbz#832149)
- Don't insist on openswan, some ISPS use L2TP without IPsec
- Don't call grantpt(), it's not needed and triggers SElinux
  block (rhbz#834861)

* Fri Jun 15 2012 Paul Wouters <pwouters@redhat.com> - 1.3.1-7
- Moved modprobe code from daemon to initscript/systemd
  (SElinux does not allow a daemon to do this, see rhbz#832149)

* Tue Jun 12 2012 Paul Wouters <pwouters@redhat.com> - 1.3.1-6
- Added patch for xl2tpd.conf to improve interop settings
  (no longer need to say "no encryption" on Windows)
- Improved patch, more doc fixed (esp. "force userspace" option)
- don't use old version of if_pppol2tp.h

* Wed Apr 18 2012 Paul Wouters <pwouters@redhat.com> - 1.3.1-5
- Added support for CONFIG_PPPOL2TP by sigwall <fionov@gmail.com>
- Require current ppp because some old versions lacked pppol2tp.so plugin

* Thu Apr 05 2012 Paul Wouters <pwouters@redhat.com> - 1.3.1-4
- Fix parse error on lines > 80 chars, rhbz#806963

* Tue Feb 28 2012 Paul Wouters <pwouters@redhat.com> - 1.3.1-3
- Converted to systemd
- Added -Wunused patch to fix two minor warnings

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 06 2011 Paul Wouters <paul@xelerance.com> - 1.3.1-1
- Upgraded to 1.3.1
- Use ghost for /var/run files

* Sat Jul 23 2011 Paul Wouters <paul@xelerance.com> - 1.3.0-1
- Upgraded to 1.3.0 with better NetworkManager support
- Compiled without DEBUG per default to gain more performance
- Added xl2tpd-control

* Wed Feb 23 2011 Paul Wouters <paul@xelerance.com> - 1.2.8-1
- Updated to 1.2.8
- Add ghosting for l2tp pipe (bz#656725)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Paul Wouters <paul@xelerance.com> - 1.2.7-2
- fix md5 of init script in sources

* Tue Nov 30 2010 Paul Wouters <paul@xelerance.com> - 1.2.7-1
- Updated to 1.2.7
- Added more DEBUG build options to the make command
- Minor cleanups

* Sat Jan 09 2010 Paul Wouters <paul@xelerance.com> - 1.2.5-2
- Bump for EVR

* Sat Jan 09 2010 Paul Wouters <paul@xelerance.com> - 1.2.5-1
- Upgraded to 1.2.5. (fixes interop with two Windows machines behind same NAT)
- Fix mix space/tab in spec file
- Added missing keyword Default-Stop

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 08 2009 Paul Wouters <paul@xelerance.com> - 1.2.4-3
- Bump version for tagging mistake

* Sun Mar 08 2009 Paul Wouters <paul@xelerance.com> - 1.2.4-2
-Fix initscript for https://bugzilla.redhat.com/show_bug.cgi?id=247100

* Sun Mar 08 2009 Paul Wouters <paul@xelerance.com> - 1.2.4-1
- Upgraded to 1.2.4
- Merged spec file with upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct  9 2008 Paul Wouters <paul@xelerance.com> - 1.2.0-1
- Updated to new upstream release

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.12-3
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.12-2
- Autorebuild for GCC 4.3

* Fri Oct 26 2007 Paul Wouters <paul@xelerance.com> 1.1.12-1
- Upgraded to new release upstream
- Removed l2tpd to xl2tpd migration in post

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.1.11-3
- Rebuild for selinux ppc32 issue.

* Sat Jul 28 2007 Paul Wouters <paul@xelerance.com> 1.1.11-2
- Upgraded to 1.1.11
- Include new split README.*

* Mon Mar 19 2007 Paul Wouters <paul@xelerance.com> 1.1.09-1
- Upgraded to 1.1.09

* Fri Feb 23 2007 Paul Wouters <paul@xelerance.com> 1.1.08-2
- Bump for EVR

* Fri Feb 23 2007 Paul Wouters <paul@xelerance.com> 1.1.08-1
- Upgraded to 1.1.08
- This works around the ppp-2.4.2-6.4 issue of not dying on SIGTERM

* Tue Feb 20 2007 Paul Wouters <paul@xelerance.com> 1.1.07-2
- Fixed version usage in source macro

* Tue Feb 20 2007 Paul Wouters <paul@xelerance.com> 1.1.07-1
- Upgraded to 1.1.07
- Added /var/run/xl2tpd to the spec file so this pacakge
  owns /var/run/xl2tpd

* Thu Dec  7 2006 Paul Wouters <paul@xelerance.com> 1.1.06-5
- Changed space/tab replacing method

* Wed Dec  6 2006 Paul Wouters <paul@xelerance.com> 1.1.06-4
- Added -p to keep original timestamps
- Added temporary hack to change space/tab in init file.
- Added /sbin/service dependancy

* Tue Dec  5 2006 Paul Wouters <paul@xelerance.com> 1.1.06-3
- Added Requires(post) / Requires(preun)
- changed init file to create /var/run/xl2tpd fixed a tab/space
- changed control file to be within /var/run/xl2tpd/

* Tue Dec  5 2006 Paul Wouters <paul@xelerance.com> 1.1.06-2
- Changed Mr. Karlsen's name to not be a utf8 problem
- Fixed Obosoletes/Provides to be more specific wrt l2tpd.
- Added dist tag which accidentally got deleted.

* Mon Dec  4 2006 Paul Wouters <paul@xelerance.com> 1.1.06-1
- Rebased spec file on Fedora Extras copy, but using xl2tpd as package name

* Sun Nov 27 2005 Paul Wouters <paul@xelerance.com> 0.69.20051030
- Pulled up sourceforget.net CVS fixes.
- various debugging added, but debugging should not be on by default.
- async/sync conversion routines must be ready for possibility that the read
  will block due to routing loops.
- refactor control socket handling.
- move all logic about pty usage to pty.c. Try ptmx first, if it fails try
  legacy ptys
- rename log() to l2tp_log(), as "log" is a math function.
- if we aren't deamonized, then log to stderr.
- added install: and DESTDIR support.

* Thu Oct 20 2005 Paul Wouters <paul@xelerance.com> 0.69-13
- Removed suse/mandrake specifics. Comply for Fedora Extras guidelines

* Tue Jun 21 2005 Jacco de Leeuw <jacco2@dds.nl> 0.69-12jdl
- Added log() patch by Paul Wouters so that l2tpd compiles on FC4.

* Sat Jun 4 2005 Jacco de Leeuw <jacco2@dds.nl>
- l2tpd.org has been hijacked. Project moved back to SourceForge:
  http://l2tpd.sourceforge.net

* Tue May 3 2005 Jacco de Leeuw <jacco2@dds.nl>
- Small Makefile fixes. Explicitly use gcc instead of cc.
  Network services library was not linked on Solaris due to typo.

* Thu Mar 17 2005 Jacco de Leeuw <jacco2@dds.nl> 0.69-11jdl
- Choosing between SysV or BSD style ptys is now configurable through
  a compile-time boolean "unix98pty".

* Fri Feb 4 2005 Jacco de Leeuw <jacco2@dds.nl>
- Added code from Roaring Penguin (rp-l2tp) to support SysV-style ptys.
  Requires the N_HDLC kernel module.

* Fri Nov 26 2004 Jacco de Leeuw <jacco2@dds.nl>
- Updated the README.

* Wed Nov 10 2004 Jacco de Leeuw <jacco2@dds.nl> 0.69-10jdl
- Patch by Marald Klein and Roger Luethi. Fixes writing PID file.
  (http://l2tpd.graffl.net/msg01790.html)
  Long overdue. Rereleasing 10jdl.

* Tue Nov 9 2004 Jacco de Leeuw <jacco2@dds.nl> 0.69-10jdl
- [SECURITY FIX] Added fix from Debian because of a bss-based
  buffer overflow.
  (http://www.mail-archive.com/l2tpd-devel@l2tpd.org/msg01071.html)
- Mandrake's FreeS/WAN, Openswan and Strongswan RPMS use configuration
  directories /etc/{freeswan,openswan,strongswan}. Install our
  configuration files to /etc/ipsec.d and create symbolic links in
  those directories.

* Wed Aug 18 2004 Jacco de Leeuw <jacco2@dds.nl>
- Removed 'leftnexthop=' lines. Not relevant for recent versions
  of FreeS/WAN and derivates.

* Tue Jan 20 2004 Jacco de Leeuw <jacco2@dds.nl>  0.69-9jdl
- Added "noccp" because of too much MPPE/CCP messages sometimes.

* Wed Dec 31 2003 Jacco de Leeuw <jacco2@dds.nl>
- Added patch in order to prevent StopCCN messages.

* Sat Aug 23 2003 Jacco de Leeuw <jacco2@dds.nl>
- MTU/MRU 1410 seems to be the lowest possible for MSL2TP.
  For Windows 2000/XP it doesn't seem to matter.
- Typo in l2tpd.conf (192.168.128/25).

* Fri Aug 8 2003 Jacco de Leeuw <jacco2@dds.nl>  0.69-8jdl
- Added MTU/MRU 1400 to options.l2tpd. I don't know the optimal
  value but some apps had problems with the default value.

* Fri Aug 1 2003 Jacco de Leeuw <jacco2@dds.nl>
- Added workaround for the missing hostname bug in the MSL2TP client
  ('Specify your hostname', error 629: "You have been disconnected
  from the computer you are dialing").

* Sun Jul 20 2003 Jacco de Leeuw <jacco2@dds.nl>  0.69-7jdl
- Added the "listen-addr" global parameter for l2tpd.conf. By
  default, the daemon listens on *all* interfaces. Use
  "listen-addr" if you want it to bind to one specific
  IP address (interface), for security reasons. (See also:
  http://www.jacco2.dds.nl/networking/freeswan-l2tp.html#Firewallwarning)
- Explained in l2tpd.conf that two different IP addresses should be
  used for 'listen-addr' and 'local ip'.
- Modified init script. Upgrades should work better now. You
  still need to start/chkconfig l2tpd manually.
- Renamed the example Openswan .conf files to better reflect
  the situation. There are two variants using different portselectors.
  Previously I thought Windows 2000/XP used portselector 17/0
  and the rest used 17/1701. But with the release of an updated
  IPsec client by Microsoft, it turns out that 17/0 must have
  been a mistake: the updated client now also uses 17/1701.

* Thu Apr 10 2003 Jacco de Leeuw <jacco2@dds.nl>  0.69-6jdl
- Changed sample chap-secrets to be valid only for specific
  IP addresses.

* Thu Mar 13 2003 Bernhard Thoni <tech-role@tronicplanet.de>
- Adjustments for SuSE8.x (thanks, Bernhard!)
- Added sample chap-secrets.

* Thu Mar 6 2003 Jacco de Leeuw <jacco2@dds.nl> 0.69-5jdl
- Replaced Dominique's patch by Damion de Soto's, which does not
  depend on the N_HDLC kernel module.

* Wed Feb 26 2003 Jacco de Leeuw <jacco2@dds.nl> 0.69-4jdl
- Seperate example config files for Win9x (MSL2TP) and Win2K/XP
  due to left/rightprotoport differences.
  Fixing preun for Red Hat.

* Mon Feb 3 2003 Jacco de Leeuw <jacco2@dds.nl> 0.69-3jdl
- Mandrake uses /etc/freeswan/ instead of /etc/ipsec.d/
  Error fixed: source6 was used for both PSK and CERT.

* Wed Jan 29 2003 Jacco de Leeuw <jacco2@dds.nl> 0.69-3jdl
- Added Dominique Cressatti's pty patch in another attempt to
  prevent the Windows 2000 Professional "loopback detected" error.
  Seems to work!

* Wed Dec 25 2002 Jacco de Leeuw <jacco2@dds.nl> 0.69-2jdl
- Added 'connect-delay' to PPP parameters in an attempt to
  prevent the Windows 2000 Professional "loopback detected" error.
  Didn't seem to work.

* Fri Dec 13 2002 Jacco de Leeuw <jacco2@dds.nl> 0.69-1jdl
- Did not build on Red Hat 8.0. Solved by adding comments(?!).
  Bug detected in spec file: chkconfig --list l2tpd does not work
  on Red Hat 8.0. Not important enough to look into yet.

* Sun Nov 17 2002 Jacco de Leeuw <jacco2@dds.nl> 0.69-1jdl
- Tested on Red Hat, required some changes. No gprintf. Used different
  pty patch, otherwise wouldn't run. Added buildroot sanity check.

* Sun Nov 10 2002 Jacco de Leeuw <jacco2@dds.nl>
- Specfile adapted from Mandrake Cooker. The original RPM can be
  retrieved through:
  http://www.rpmfind.net/linux/rpm2html/search.php?query=l2tpd
- Config path changed from /etc/l2tp/ to /etc/l2tpd/
  (Seems more logical and rp-l2tp already uses /etc/l2tp/).
- Do not run at boot or install. The original RPM uses a config file
  which is completely commented out, but it still starts l2tpd on all
  interfaces. Could be a security risk. This RPM does not start l2tpd,
  the sysadmin has to edit the config file and start l2tpd explicitly.
- Renamed patches to start with l2tpd-
- Added dependencies for pppd, glibc-devel.
- Use %%{name} as much as possible.
- l2tp-secrets contains passwords, thus should not be world readable.
- Removed dependency on rpm-helper.

* Mon Oct 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.69-3mdk
- from Per 0yvind Karlsen <peroyvind@delonic.no> :
 - PreReq and Requires
 - Fix preun_service

* Thu Oct 17 2002 Per 0yvind Karlsen <peroyvind@delonic.no> 0.69-2mdk
- Move l2tpd from /usr/bin to /usr/sbin
- Added SysV initscript
- Patch0
- Patch1

* Thu Oct 17 2002 Per 0yvind Karlsen <peroyvind@delonic.no> 0.69-1mdk
- Initial release
