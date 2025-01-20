%if %{defined rhel} && 0%{?rhel} <= 7 || %{defined fedora} && 0%{?fedora} < 30
%bcond_with timers
%else
%bcond_without timers
%endif

Name: recap
Version: 2.1.0
Release: 19%{?dist}
Summary: Generates reports of various system information
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/rackerlabs/recap
Source0: https://github.com/rackerlabs/recap/archive/%{version}/recap-%{version}.tar.gz
BuildArch: noarch
%if %{without timers}
Requires: crontabs
%endif
Requires: iotop
Requires: iproute
%if 0%{?rhel} && 0%{?rhel} < 7
Requires: procps
%else
Requires: procps-ng
%endif
Requires: psmisc
Requires: sysstat >= 9

%if %{defined rhel} && 0%{?rhel} > 7 || %{defined fedora}
Recommends: elinks
%endif

BuildRequires: make
%if %{with timers}
BuildRequires: systemd
Requires: systemd
%endif
Obsoletes: rs-sysmon < 0.9.5-2
Provides: rs-sysmon = %{version}-%{release}


%description
This program is intended to be used as a companion for the reporting provided
by sysstat. It will create a set of reports summarizing hardware resource
utilization. The script also provides optional reporting on Apache, MySQL, and
network connections.


%prep
%autosetup

%install
export PREFIX=%{_prefix}
export DESTDIR=%{buildroot}
make install-base
make install-man

%if %{with timers}
make install-systemd
%else
make install-cron
%endif


%posttrans
# https://github.com/rackerlabs/recap/pull/137
if [ -f /etc/recap.rpmsave ]; then
    mv -vf /etc/recap.conf /etc/recap.conf.rpmnew
    mv -vf /etc/recap.rpmsave /etc/recap.conf
fi


%files
%license COPYING
%doc README.md CHANGELOG.md
%dir %{_localstatedir}/log/recap
%dir %{_localstatedir}/log/recap/backups
%dir %{_localstatedir}/log/recap/snapshots
%{_sbindir}/recap
%{_sbindir}/recaplog
%{_sbindir}/recaptool

# systemd unit files
%if %{with timers}
%{_unitdir}/recap.service
%{_unitdir}/recaplog.service
%{_unitdir}/recap-onboot.service
%{_unitdir}/recap.timer
%{_unitdir}/recaplog.timer
%{_unitdir}/recap-onboot.timer
%else
# crontab
%config(noreplace) %{_sysconfdir}/cron.d/recap
%endif

%config(noreplace) %{_sysconfdir}/recap.conf
%{_mandir}/man5/recap.conf.5.gz
%{_mandir}/man8/recap.8.gz
%{_mandir}/man8/recaplog.8.gz
%{_mandir}/man8/recaptool.8.gz

# core functions
%{_prefix}/lib/recap/core/fdisk
%{_prefix}/lib/recap/core/mysql
%{_prefix}/lib/recap/core/netstat
%{_prefix}/lib/recap/core/ps
%{_prefix}/lib/recap/core/pstree
%{_prefix}/lib/recap/core/resources
%{_prefix}/lib/recap/core/send_mail

# plugins
%{_prefix}/lib/recap/plugins-available/docker_top
%{_prefix}/lib/recap/plugins-available/http_status
%{_prefix}/lib/recap/plugins-available/kernel_cmd
%{_prefix}/lib/recap/plugins-available/redis
%{_prefix}/lib/recap/plugins-available/system_locks
%dir %{_prefix}/lib/recap/plugins-enabled


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-18
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Tony Garcia <tony.garcia@rackspace.com> - 2.1.0-6
- Use Recommends only in RPM supported versions (4.12.0)

* Tue Nov 19 2019 Tony Garcia <tony.garcia@rackspace.com> - 2.1.0-5
- Update dependencies, set elinks to recommends

* Thu Oct 17 2019 Pete Travis <immanetize@fedoraproject.org> - 2.1.0-4
- Add obsoletes and provides for 'rs-sysmon', upstream predecessor of recap

* Fri Sep 20 2019 Tony Garcia <tony.garcia@rackspace.com> - 2.1.0-3
- Update dependencies when using timers

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Tony Garcia <tony.garcia@rackspace.com> - 2.1.0-1
- Latest upstream rhbz#1669250
- Adding a new plugin: system_locks

* Tue Feb 26 2019 Tony Garcia <tony.garcia@rackspace.com> - 2.0.2-1
- Latest upstream rhbz#1669250

* Mon Feb 11 2019 Tony Garcia <tony.garcia@rackspace.com> - 2.0.1-1
- Latest upstream rhbz#1669250
- Update dependencies
- Rename man page from recap to recap.conf
- Adding systemd timers on fedora

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Tony Garcia <tony.garcia@rackspace.com> - 1.4.0-1
- Latest upstream rhbz#1602980

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Carl George <carl@george.computer> - 1.3.0-1
- Latest upstream
- Move config file from /etc/recap to /etc/recap.conf

* Wed Nov 08 2017 Carl George <carl@george.computer> - 1.2.0-2
- Drop requirement on bc
- Add requirement on links

* Wed Nov 08 2017 Carl George <carl@george.computer> - 1.2.0-1
- Latest upstream rhbz#1489995
- Switch dependency of net-tools to iproute rhbz#1496151

* Mon Sep 11 2017 Carl George <carl@george.computer> - 1.1.0-1
- Latest upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Carl George <carl.george@rackspace.com> - 1.0.0-2
- Require crontabs
- Remove unnecessary requirements

* Mon May 15 2017 Tony Garcia <tony.garcia@rackspace.com> - 1.0.0-1
- Update to version 1.0.0
- Include recaptool man page.
- Clean up requirements.
- Obsoletes and provides rs-sysmon.

* Wed May 11 2016 Ben Harper <ben.harper@rackspace.com> - 0.9.14-1
- Latest version
- Fixing typos, removing commented old code, renaming functions

* Wed May 04 2016 Carl George <carl.george@rackspace.com> - 0.9.13-1
- Latest version
- Install recaplog man page

* Fri Apr 22 2016 Carl George <carl.george@rackspace.com> - 0.9.12-1
- Latest version
- Use Makefile to install

* Tue Apr 12 2016 Carl George <carl.george@rackspace.com> - 0.9.11-3
- Add missing recaplog file
- Use appropriate license directory when possible
- Remove httpd example configuration

* Mon Apr 11 2016 Carl George <carl.george@rackspace.com> - 0.9.11-2
- Add rs to release

* Wed Jan 06 2016 Carl George <carl.george@rackspace.com> - 0.9.11-1
- Latest version

* Mon Dec 21 2015 Carl George <carl.george@rackspace.com> - 0.9.10-1
- Latest version
- Update dependencies

* Fri Jun 12 2015 Carl George <carl.george@rackspace.com> - 0.9.8-2
- Fix EL5 COPR build

* Wed Jan 07 2015 Carl George <carl.george@rackspace.com> - 0.9.8-1
- Latest version

* Thu Nov 1 2012 Benjamin H. Graham <ben@administr8.me>
- First public release GPLv2, special thanks to Rackspace IPC, Brent Oswald, and Benjamin H. Graham
- Changed name to recap, added links for new repository
- Added recaptool and installer

* Tue Nov 16 2010 Jacob Walcik <jacob.walcik@rackspce.com>
- Added COPYING file to specify license as GPL
- Added full list of dependencies for basic reporting
- Updated description

* Thu May 27 2010 David King <david.king@rackspace.com>
- Changed version number of recap release and added a configuration file for apache to access recap logs

* Tue Oct 20 2009 David King <david.king@rackspace.com>
- Changed /etc/cron.d/recap and /etc/recap to be config noreplace files

* Thu Nov 13 2008 Jacob Walcik <jacob.walcik@rackspace.com>
- modified default mode of the output directory

* Thu Nov 01 2007 Carl Thompson <carl.thompson@rackspace.com>
- added support for service httpd fullstatus by Jacob Walcik <jacob.walcik@rackspace.com>

* Wed Sep 12 2007 Carl Thompson <carl.thompson@rackspace.com>
- added man pages created by Jacob Walcik <jacob.walcik@rackspace.com>

* Thu Jul 12 2007 Carl Thompson <carl.thompson@rackspace.com>
- Added pstree support

* Tue Jul 10 2007 Carl Thompson <carl.thompson@rackspace.com>
- Fixed permissions on cron file, added 2 cron tasks for @reboot in cron file

* Tue Jul 10 2007 Carl Thompson <carl.thompson@rackspace.com>
- Added sar -q and inline documentation, relocated doc to recap-version

* Mon Jul 09 2007 Carl Thompson <carl.thompson@rackspace.com>
- Initial build of package
