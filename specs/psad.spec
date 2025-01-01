Summary: Port Scan Attack Detector (psad) watches for suspect traffic
Name: psad
Version: 2.4.6
Release: 20%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://www.cipherdyne.org/psad/
Source0: https://www.cipherdyne.org/psad/download/psad-%{version}.tar.bz2
Source1: https://www.cipherdyne.org/psad/download/psad-%{version}.tar.bz2.asc
# curl -O https://www.cipherdyne.org/signing_key ; gpg --import ./signing_key
# gpg --export --export-options export-minimal 4D6644A9DA036904BDA2CB90E6C9E3350D3E7410 > 4D6644A9DA036904BDA2CB90E6C9E3350D3E7410.gpg
Source2: 4D6644A9DA036904BDA2CB90E6C9E3350D3E7410.gpg
Source4: psad-tmpfiles.conf
# patch to:
# * allow specifying Fedora CFLAGS
# * use system whois
# * set some sensible defaults in /etc/psad/psad.conf
Patch0: psad-fedora.patch
# https://github.com/mrash/psad/issues/53
Patch1: psad-issue53.patch
BuildArch: noarch
BuildRequires: %{_bindir}/gpgv2
BuildRequires: perl-generators
BuildRequires: systemd-rpm-macros
# works with system one, but doesn't crash or break without it
%if 0%{?fedora}
Recommends: %{_bindir}/whois
Recommends: %{_sbindir}/sendmail
Recommends: /bin/mail
%endif
Requires: %{_bindir}/killall
Requires: /bin/ps
Requires: gzip
Requires: iproute
Requires: iptables
# The automatic dependency generator doesn't find these
Requires: perl(Bit::Vector)
Requires: perl(Carp::Clan)
Requires: perl(Date::Calc)
Requires: perl(IPTables::ChainMgr)
Requires: perl(IPTables::Parse)
Requires: perl(NetAddr::IP)
Requires: perl(Storable)
Requires: perl(Unix::Syslog)
Requires(post): policycoreutils >= 2.4
Requires(post): %{_sbindir}/semodule
Requires(postun): %{_sbindir}/semodule

%description
Port Scan Attack Detector (psad) is a lightweight
system daemon written in Perl designed to work with Linux
iptables firewalling code to detect port scans and other suspect traffic.  It
features a set of highly configurable danger thresholds (with sensible
defaults provided), verbose alert messages that include the source,
destination, scanned port range, begin and end times, tcp flags and
corresponding nmap options, reverse DNS info, email and syslog alerting,
automatic blocking of offending ip addresses via dynamic configuration of
iptables rulesets, and passive operating system fingerprinting.  In addition,
psad incorporates many of the tcp, udp, and icmp signatures included in the
snort intrusion detection system (https://www.snort.org) to detect highly
suspect scans for various backdoor programs (e.g. EvilFTP, GirlFriend,
SubSeven), DDoS tools (mstream, shaft), and advanced port scans (syn, fin,
xmas) which are easily leveraged against a machine via nmap.  psad can also
alert on snort signatures that are logged via fwsnort
(https://www.cipherdyne.org/fwsnort/), which makes use of the
iptables string match module to detect application layer signatures.

%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q
%patch -P0 -p1 -b .f
%patch -P1 -p1 -b .i53
# remove bundled stuff
rm -r deps/{Bit-Vector,Carp-Clan,Date-Calc,IPTables-ChainMgr,IPTables-Parse,NetAddr-IP,Storable,Unix-Syslog,whois}

%build
echo Nothing to build.

%install
install  -dm755 %{buildroot}{%{_mandir}/man{1,8},%{_sbindir},%{_sysconfdir}/%{name}}
install  -pm755 -t %{buildroot}%{_sbindir} psad
install -Dpm755 fwcheck_psad.pl %{buildroot}%{_sbindir}/fwcheck_psad
install -Dpm755 nf2csv %{buildroot}%{_bindir}/nf2csv
install -Dpm644 misc/logrotate.psad %{buildroot}%{_sysconfdir}/logrotate.d/psad
install  -pm644 -t %{buildroot}%{_sysconfdir}/%{name} \
 auto_dl \
 icmp_types \
 icmp6_types \
 ip_options \
 pf.os \
 posf \
 protocols \
 psad.conf \
 signatures \
 snort_rule_dl \

install -pm644 -t %{buildroot}%{_mandir}/man8 doc/{fwcheck_psad,psad}.8
install -pm644 -t %{buildroot}%{_mandir}/man1 doc/nf2csv.1

cp -pr deps/snort_rules %{buildroot}%{_sysconfdir}/%{name}

install -Dpm644 init-scripts/systemd/psad.service %{buildroot}%{_unitdir}/psad.service
install -Dpm644 %{S:4} %{buildroot}%{_tmpfilesdir}/psad.conf

# upstream's installer creates those as root-accessible only
install  -dm700 %{buildroot}/{var/{lib,log},run}/%{name}
touch %{buildroot}/var/lib/%{name}/psadfifo
touch %{buildroot}/run/%{name}/psad.cmd

%post
# missing from current SELinux policy (Fedora: #1174309, RHEL7: #1389191)
TMPDIR=$(%{_bindir}/mktemp -d)
cat >> $TMPDIR/psad-rpm.cil << __EOF__
(allow firewalld_t psad_t(dbus (send_msg)))
(allow psad_t firewalld_t(dbus (send_msg)))
(allow psad_t journalctl_exec_t(file (execute execute_no_trans map open read)))
(allow psad_t kernel_t (system (module_request)))
(allow psad_t psad_var_log_t(file (read rename unlink write)))
(allow psad_t self (netlink_tcpdiag_socket (bind create setopt)))
(allow psad_t sysfs_t (dir (read)))
(allow psad_t sysfs_t (file (getattr open read)))
(allow psad_t syslogd_var_run_t (dir (read watch)))
(allow psad_t var_log_t (dir (watch)))
(dontaudit psad_t apmd_exec_t(file (getattr)))
(dontaudit psad_t auditd_exec_t(file (getattr)))
(dontaudit psad_t crond_exec_t(file (getattr)))
(dontaudit psad_t dovecot_exec_t(file (getattr)))
(dontaudit psad_t getty_exec_t(file (getattr)))
(dontaudit psad_t httpd_exec_t(file (getattr)))
(dontaudit psad_t init_exec_t(file (getattr)))
(dontaudit psad_t load_policy_t (dir (getattr search)))
(dontaudit psad_t load_policy_t (file (open read)))
(dontaudit psad_t load_policy_t (lnk_file (read)))
(dontaudit psad_t mandb_t (dir (getattr search)))
(dontaudit psad_t mandb_t (file (open read)))
(dontaudit psad_t radvd_exec_t (file (getattr)))
(dontaudit psad_t rngd_exec_t (file (getattr)))
(dontaudit psad_t rpcd_exec_t (file (getattr)))
(dontaudit psad_t self (capability (dac_override sys_ptrace sys_resource)))
(dontaudit psad_t self (cap_userns (sys_ptrace)))
(dontaudit psad_t sshd_exec_t (file (getattr)))
(dontaudit psad_t syslogd_exec_t (file (getattr)))
(dontaudit psad_t systemd_logind_exec_t (file (getattr)))
(dontaudit psad_t systemd_machined_exec_t (file (getattr)))
(dontaudit psad_t udev_exec_t (file (getattr)))
(dontaudit psad_t virtd_exec_t (file (getattr)))
(dontaudit psad_t xserver_log_t (dir (search)))
__EOF__
%{_sbindir}/semodule -i $TMPDIR/psad-rpm.cil
rm -rf $TMPDIR
%systemd_post psad.service
exit 0

%preun
%systemd_preun psad.service

%postun
%systemd_postun_with_restart psad.service
if [ $1 -eq 0 ]; then
  %{_sbindir}/semodule -r psad-rpm > /dev/null || :
fi

%files
%license LICENSE
%doc doc/BENCHMARK ChangeLog CREDITS doc/FW_EXAMPLE_RULES README.md doc/README.SYSLOG doc/SCAN_LOG
%{_bindir}/nf2csv
%{_sbindir}/fwcheck_psad
%{_sbindir}/psad
%{_mandir}/man1/nf2csv.1*
%{_mandir}/man8/fwcheck_psad.8*
%{_mandir}/man8/psad.8*
%{_tmpfilesdir}/psad.conf
%{_unitdir}/psad.service
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/psad
%config(noreplace) %{_sysconfdir}/%{name}/psad.conf
%config(noreplace) %{_sysconfdir}/%{name}/signatures
%config(noreplace) %{_sysconfdir}/%{name}/auto_dl
%config(noreplace) %{_sysconfdir}/%{name}/ip_options
%config(noreplace) %{_sysconfdir}/%{name}/snort_rule_dl
%config(noreplace) %{_sysconfdir}/%{name}/posf
%config(noreplace) %{_sysconfdir}/%{name}/pf.os
%config(noreplace) %{_sysconfdir}/%{name}/icmp_types
%config(noreplace) %{_sysconfdir}/%{name}/icmp6_types
%config(noreplace) %{_sysconfdir}/%{name}/protocols
%dir %{_sysconfdir}/%{name}/snort_rules
%config(noreplace) %{_sysconfdir}/%{name}/snort_rules/*
%dir /var/lib/%{name}
%ghost %attr(0700,root,root) /var/lib/%{name}/psadfifo
%dir /var/log/%{name}
%ghost %dir /run/%{name}
%ghost %attr(0700,root,root) /run/%{name}/psad.cmd

%changelog
* Mon Dec 30 2024 Dominik Mierzejewski <rpm@greysector.net> - 2.4.6-20
- fix some new SELinux AVC denials
- drop old Obsoletes
- limit build dependency on systemd to macro subpackage

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.6-19
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild
- complete move to /run (fixes rhbz#2113605) (Dominik Mierzejewski)

* Fri Jun 10 2022 Dominik Mierzejewski <rpm@greysector.net> - 2.4.6-12
- move PID file to /run
- silence some new SELinux getattr AVC denials

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4.6-9
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Dominik Mierzejewski <rpm@greysector.net> - 2.4.6-5
- fix netlink_tcpdiag_socket AVC denials
- allow ss command to trigger kernel module loads
- silence more getattr AVC denials
- drop obsolete triggerpostun

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Dominik Mierzejewski <rpm@greysector.net> - 2.4.6-3
- silence sys_ptrace AVC denials (#1615087)
- use upstream patch to drop net-tools dependency (#1496149)
- stop shipping obsolete binaries kmsgsd and psadwatchd
- switch to noarch

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Dominik Mierzejewski <rpm@greysector.net> - 2.4.6-1
- update to 2.4.6 (#1611013)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Dominik Mierzejewski <rpm@greysector.net> - 2.4.5-1
- update to 2.4.5 (#1394902, #1476553)
- use upstream systemd unit
- include additional docs
- fix SELinux policy installation scriptlet logic (#1438190)
- drop HLL policy, CIL import is supported in 2.4+ and RHEL 7.3 ships 2.5
- add gcc to BRs, use set_build_flags macro
- add more missing SELinux rules
- silence last module removal semodule warning

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.4.3-3
- EPEL7 install doesn't support -D and -t together
- EPEL7 SELinux policy update (#1389191)
- add missing dependencies
- add dependencies to the systemd unit

* Sun Oct 09 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.4.3-2
- fix SELinux policy temporarily (#1040425)
- document patch purpose and file/dir permissions
- depend on whois binary, not package
- verify tarball GPG signature in prep

* Fri Aug 12 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.4.3-1
- update to 2.4.3
- use https in URLs
- supply native systemd unit
- drop obsolete patches
- merge Fedora-specific changes into one patch
- use system whois client instead of bundled one
- update (and sort) Requires list
- tighten file list
- remove bundled stuff in prep

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.2.1-2
- Perl 5.18 rebuild

* Tue Jan 22 2013 Viktor Hercinger <vhercing@redhat.com> - 2.2.1-1
- Update to psad-2.2.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Peter Vrabec <pvrabec@redhat.com>  2.1.7-5
- don't write to /tmp (#782527)

* Thu Jan 19 2012 Peter Vrabec <pvrabec@redhat.com>  2.1.7-4
- adjust qw() use to new perl (#771779)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Peter Vrabec <pvrabec@redhat.com>  2.1.7-1
- upgrade

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.1.3-4
- Use bzipped upstream tarball.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 13 2008 Peter Vrabec <pvrabec@redhat.com>  2.1.3-1
- some adjustments to meet fedora standartds

* Sun Apr 27 2008 Steve Grubb <sgrubb@redhat.com> 2.1.2-1
- Initial packaging
