%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name: mysql-mmm
Version: 2.2.1
Release: 36%{?dist}
Summary: Multi-Master Replication Manager for MySQL
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://mysql-mmm.org
Source: http://mysql-mmm.org/_media/:mmm2:/%{name}-%{version}.tar.gz
Source1: mysql-mmm.logrotate
Source2: http://mysql-mmm.org/_media/:mmm2:/%{name}-%{version}.pdf
Source3: mmm_mon_log.conf
Source4: mmm_agent.conf
Source5: mmm_mon.conf
Source6: mmm_tools.conf
Source7: mmm_common.conf
Source8: mysql-mmm-agent.service
Source9: mysql-mmm-monitor.service

BuildArch: noarch
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: systemd

Provides: mmm = %{version}-%{release}
Provides: mysql-master-master = %{version}-%{release}

Patch0: mysql-mmm-2.1.0-paths.patch
Patch1: mysql-mmm-fix-bug-with-newer-net-arp.patch
Patch2: mysql-mmm-fix-cve-remote-command-injection.patch

%description
MMM (MySQL Master-Master Replication Manager) is a set of flexible scripts
to perform monitoring/failover and management of MySQL Master-Master
replication configurations (with only one node writable at any time). The
toolset also has the ability to read balance standard master/slave
configurations with any number of slaves, so you can use it to move virtual
IP addresses around a group of servers depending on whether they are behind
in replication. In addition to that, it also has scripts for data backups,
resynchronization between nodes etc.

%package agent
Summary: MMM Database Server Agent Daemon and Libraries
Requires: %{name} = %{version}-%{release}
Requires: iproute
Requires: perl-DBD-mysql
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Provides: mysql-master-master-agent = %{version}-%{release}
Provides: mmm-agent = %{version}-%{release}

%description agent
Agent daemon and libraries which run on each MySQL server and provides the
monitoring node with a simple set of remote services.

%package monitor
Summary: MMM Monitor Server Daemon and Libraries
Requires: %{name} = %{version}-%{release}
Requires: perl(Class::Singleton), perl(DBD::mysql), perl(Time::HiRes)
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Provides: mysql-master-master-monitor = %{version}-%{release}
Provides: mmm-monitor = %{version}-%{release}

%description monitor
Monitoring daemon and libraries that do all monitoring work and make all
decisions about roles moving and so on.

%package tools
Summary: MMM Control Scripts and Libraries
Requires: %{name} = %{version}-%{release}
Provides: mysql-master-master-tools = %{version}-%{release}
Provides: mmm-tools = %{version}-%{release}

%description tools
Scripts and libraries dedicated to management of the mmm_mond processes
by commands.

%prep
%setup -q
cp -a %{SOURCE2} .

# currently the README included with mysql-mmm is zero-length
cat >>README <<EOF
Full documentation can be found at:

    %{_pkgdocdir}/%{name}-%{version}.pdf
EOF


%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
find . -type f -name "*.orig" -print0 | xargs -0r rm

%build


%install
make install DESTDIR=%{buildroot}

%{__install} -D -p -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/logrotate.d/mysql-mmm
%{__install} -d -m 0755 %{buildroot}%{_localstatedir}/lib/%{name}

# Replace config files
%{__rm} -f %{buildroot}%{_sysconfdir}/mysql-mmm/*.conf

%{__install} -p -m 0640 %SOURCE3 %{buildroot}%{_sysconfdir}/mysql-mmm/mmm_mon_log.conf
%{__install} -p -m 0640 %SOURCE4 %{buildroot}%{_sysconfdir}/mysql-mmm/mmm_agent.conf
%{__install} -p -m 0640 %SOURCE5 %{buildroot}%{_sysconfdir}/mysql-mmm/mmm_mon.conf
%{__install} -p -m 0640 %SOURCE6 %{buildroot}%{_sysconfdir}/mysql-mmm/mmm_tools.conf
%{__install} -p -m 0640 %SOURCE7 %{buildroot}%{_sysconfdir}/mysql-mmm/mmm_common.conf
%{__install} -D -p -m 0644 %SOURCE8 %{buildroot}%{_unitdir}/mysql-mmm-agent.service
%{__install} -D -p -m 0644 %SOURCE9 %{buildroot}%{_unitdir}/mysql-mmm-monitor.service

%{__rm} -rvf %{buildroot}%{_sysconfdir}/init.d/

%post agent
%systemd_post mysql-mmm-agent.service

%preun agent
%systemd_preun mysql-mmm-agent.service

%postun agent
%systemd_postun mysql-mmm-agent.service

%post monitor
%systemd_post mysql-mmm-monitor.service

%preun monitor
%systemd_preun mysql-mmm-monitor.service

%postun monitor
%systemd_postun mysql-mmm-monitor.service

%files
%doc COPYING README VERSION %{name}-%{version}.pdf
%dir %{_sysconfdir}/mysql-mmm
%attr(755,root,root) %dir %{_localstatedir}/lib/mysql-mmm
%attr(755,root,root) %dir %{_localstatedir}/log/mysql-mmm
%config(noreplace) %{_sysconfdir}/logrotate.d/mysql-mmm
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/mysql-mmm/mmm_common.conf
%{perl_vendorlib}/MMM/Common

%files tools
%doc README
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/mysql-mmm/mmm_tools.conf
%{perl_vendorlib}/MMM/Tools
%{_libexecdir}/mysql-mmm/tools/
%{_sbindir}/mmm_backup
%{_sbindir}/mmm_clone
%{_sbindir}/mmm_restore

%files agent
%doc README
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/mysql-mmm/mmm_agent.conf
%{perl_vendorlib}/MMM/Agent
%{_libexecdir}/mysql-mmm/agent/
%{_sbindir}/mmm_agentd
%{_unitdir}/mysql-mmm-agent.service

%files monitor
%doc README
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/mysql-mmm/mmm_mon.conf
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/mysql-mmm/mmm_mon_log.conf
%{perl_vendorlib}/MMM/Monitor
%{_libexecdir}/mysql-mmm/monitor/
%{_sbindir}/mmm_mond
%{_sbindir}/mmm_control
%{_unitdir}/mysql-mmm-monitor.service


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.1-35
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 David Beveridge <dave@bevhost.com> 2.2.1-20
- Patch for mmm_agentd Remote Command Injection Vulnerabilities
- TALOS-2017-0501, CVE-2017-14474 - CVE-2017-14481

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Ruben Kerkhof <ruben@rubenkerkhof.com> - 2.2.1-18
- Correct permissions for systemd units (#1527992)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.2.1-14
- Fix bug with newer Net::ARP version numbers (#1169914)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 15 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.2.1-11
- Convert to systemd (#913501)

* Sun Sep 15 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.2.1-10
- Monitor needs perl-Time-HiRes (#915665)

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 2.2.1-9
- Perl 5.18 rebuild

* Fri Jul 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.2.1-8
- Honor %%{_pkgdocdir} where available.
- Don't ship patch backup files.

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.2.1-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 BJ Dierkes <wdierkes@rackspace.com> - 2.2.1-2
- Updated agent/monitor init scripts to create /var/run/mysql-mmm
  if it does not exist.  Resolves BZ#656634
- List /var/run, /var/lock/subsys files as %%ghost entries

* Tue May 11 2010 BJ Dierkes <wdierkes@rackspace.com> - 2.2.1-1
- Latest upstream release, fixes possible errors related to
  replication. Full ChangeLog available at:
  http://mysql-mmm.org/mmm2:changelog

* Wed Mar 10 2010 BJ Dierkes <wdierkes@rackspace.com> - 2.2.0-1
- Latest upstream release.  Resolves LaunchPad Issues 416572, 422549,
  531011, 531841, 525719. Full ChangeLog available at:
  http://mysql-mmm.org/mmm2:changelog

* Mon Mar 08 2010 BJ Dierkes <wdierkes@rackspace.com> - 2.1.1-1
- Latest upstream release, resolves DBI timeout issue. Full changelog
  available at: http://mysql-mmm.org/mmm2:changelog
- Removing Patch4: mysql-mmm-2.0.10-default_logging.patch (applied upstream)

* Fri Feb 26 2010 BJ Dierkes <wdierkes@rackspace.com> - 2.1.0-4
- Agent Requires: perl-DBD-mysql.  Resolves BZ #568870

* Thu Feb 25 2010 BJ Dierkes <wdierkes@rackspace.com> - 2.1.0-3
- Fixed init scripts to check for ENABLED only within the start
  function.

* Tue Feb 23 2010 BJ Dierkes <wdierkes@rackspace.com> - 2.1.0-2
- Added defaults file for mysql-mmm-agent and mysql-mmm-monitor
  Resolves BZ #567753
- Init scripts exit if ENABLED != 1
- Fixed typo in mysql-mmm-monitor where mmmd_mon was still referenced

* Mon Feb 22 2010 BJ Dierkes <wdierkes@rackspace.com> - 2.1.0-1.1
- Latest sources from upstream
- Updated init scripts to reflect new binary paths
  (i.e. mmmd_agent -> mmm_agentd)
- Updated Patch0: mysql-mmm-2.1.0-paths.patch
- Removed Patch1: mysql-mmm-2.0.9-configs.patch (added source
  config files)

* Wed Feb 17 2010 BJ Dierkes <wdierkes@rackspace.com> - 2.0.11-2
- Rebuild for F13/devel retag

* Mon Feb 08 2010 BJ Dierkes <wdierkes@rackspace.com> - 2.0.11-1
- Latest sources from upstream
- Removed Patch3: mysql-mmm-2.0.10-lp473446.patch (appied upstream)
- Added default mmm_mon_log.conf to allow logger modification

* Fri Dec 04 2009 BJ Dierkes <wdierkes@rackspace.com> - 2.0.10-4
- Add auto_set_online to 60 in mmm_mon.conf
- Provides full version-release for all subpackages
- Append doc location to pdf documentation in README
- Use subsys/lockfile in init scripts

* Thu Nov 19 2009 BJ Dierkes <wdierkes@rackspace.com> - 2.0.10-3
- BuildArch: noarch
- Monitor subpackage Requires: perl(DBD::mysql)
- Provides full version-release for  mmm, mysql-master-master
- Removed redundant /var/run/mysql-mmm entry
- Use _localstatedir macro for /var/log/mysql-mmm file listing
- Fixed logic in post and postun scripts to properly handle
  install/upgrade conditions.
- Post scripts now perform condrestart
- Added Source3: mysql-mmm-agent.init
- Added Source4: mysql-mmm-monitor.init

* Tue Nov 17 2009 BJ Dierkes <wdierkes@rackspace.com> - 2.0.10-2
- Removed Patch2: mysql-mmm-2.0.10-sleep.patch (obsoleted by Patch3)
- Added Patch3: mysql-mmm-2.0.10-lp473446.patch
- Added Patch4: mysql-mmm-2.0.10-default_logging.patch

* Tue Nov 03 2009 BJ Dierkes <wdierkes@rackspace.com> - 2.0.10-1
- Latest sources from upstream.
- Added Patch1: mysql-mmm-2.0.9-configs.patch
- Added Patch2: mysql-mmm-2.0.10-sleep.patch
- Moved mmm_control under monitor package

* Mon Oct 19 2009 BJ Dierkes <wdierkes@rackspace.com> - 2.0.9-1
- Starting mostly from scratch with 2.0 branch
- Added Patch0: mysql-mmm-2.0.9-patchs.patch

* Tue Oct 13 2009 BJ Dierkes <wdierkes@rackspace.com> - 1.2.6-4
- Cleaning up rpmlint errors
- No longer require perl-DBD-MySQL

* Tue Sep 29 2009 BJ Dierkes <wdierkes@rackspace.com> - 1.2.6-3.3
- Removing .rs tag (Packaging for Fedora/Epel).

* Mon Sep 28 2009 BJ Dierkes <wdierkes@rackspace.com> - 1.2.6-3.2.rs
- Change subpackage -control to -tools
- No longer build or include send_arp, removing requirement of
  libnet
- Keep etc config files actually in /etc, symlink at _mmm_instdir/etc

* Wed Sep 23 2009 BJ Dierkes <wdierkes@rackspace.com> - 1.2.6-3.rs
- Cleaned up spec a bit further, moved sed changes to patches
- Added Patch1: mysql-master-master-1.2.6-libnet_1.1.patch
- Added Patch2: mysql-master-master-1.2.6-paths.patch
- Explicitly require libnet >= 1.1
- Added subpackages to break up agent, monitor, and control (backup/restore)

* Mon Sep 21 2009 Andrew Garner <andrew.garner@rackspace.com> - 1.2.6-2.abg
- Added patch for http://code.google.com/p/mysql-master-master/issues/detail?id=35

* Wed Sep 02 2009 Andrew Garner <andrew.garner@rackspace.com> - 1.2.6-1.abg
- New upstream release

* Thu Jul 09 2009 Andrew Garner <andrew.garner@rackspace.com>
- Fix release string to drop out incorrect ~rs identifier
- Updated to release 5.abg

* Thu Apr 16 2009 Andrew Garner <andrew.garner@rackspace.com>
- Change /etc/init.d/mysql-mmm_{mon,agent} back to mmm_{mon,agent}
- symlink /etc/mysql-mmm to /usr/lib/mysql-mmm (not the other way around)

* Tue Apr 14 2009 Andrew Garner <andrew.garner@rackspace.com>
- Cleanup spec
- Use standard state/log paths
- Rebuild fping
- Added dist suffix
- Changed Release to 4.rs-abg

* Mon Apr 13 2009 Andrew Garner <andrew.garner@rackspace.com>
- Fix send_arp for RHEL 5.3's libnet
- Changed /usr/local/mmm to /usr/lib/mysql-mmm/
- Changed /etc/init.d/mmm_{mon,agent} to mysql-mmm_{mon,agent}
- Changed Release to 3.rs-abg

* Thu Apr 09 2009 Andrew Garner <andrew.garner@rackspace.com>
- Updating for Rackspace

* Wed Feb 25 2009 Ryan Lowe <ryan.a.lowe@percona.com>
- Initial build (I owe JayKim)
