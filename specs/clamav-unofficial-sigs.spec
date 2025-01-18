%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
%global with_systemd 1
%global clamupdateuser clamupdate
%global clamupdategrp  clamupdate
%else
%global with_systemd 0
%global clamupdateuser clam-update
%global clamupdategrp  clam-update
%endif
Name:           clamav-unofficial-sigs
Version:        7.2.5
Release:        13%{?dist}
Summary:        Scripts to download unofficial clamav signatures 
Group:          Applications/System
License:        BSD-3-Clause
URL:            https://github.com/extremeshok/%{name}
Source0:        https://github.com/extremeshok/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        clamav-unofficial-sigs.cron
Source2:        clamav-unofficial-sigs.logrotate
Source3:        clamav-unofficial-sigs.man8
Patch1:         clamav-unofficial-sigs-grep-backslash.patch
# Fix urlhaus mkdir and ownership (https://github.com/extremeshok/clamav-unofficial-sigs/pull/390)
Patch2:         https://patch-diff.githubusercontent.com/raw/extremeshok/clamav-unofficial-sigs/pull/390.patch#/clamav-unofficial-sigs-7.2.5-urlhaus.patch
BuildArch:      noarch
BuildRequires:  bind-utils
BuildRequires:  rsync
%if %{with_systemd}
BuildRequires:  systemd
%endif
Requires:       clamav clamav-update rsync gnupg diffutils curl bind-utils
%if %{with_systemd}
Requires(post): systemd-sysv
%endif

%description
This package contains scripts and configuration files
that provide the capability to download, test, and 
update the 3rd-party signature databases provide by 
Sanesecurity, SecuriteInfo, MalwarePatrol, OITC, 
INetMsg and ScamNailer.

%prep
%setup -qn %{name}-%{version}
%autopatch -p1
sed -i -e '/user_configuration_complete/ s/^#//' config/user.conf
sed -i -e '/ExecStart/ s^/usr/local/sbin^/usr/sbin^' systemd/clamav-unofficial-sigs.service

%build
cp %{SOURCE1} clamav-unofficial-sigs.cron
cp %{SOURCE2} clamav-unofficial-sigs.logrotate
cp %{SOURCE3} clamav-unofficial-sigs.man8
%if 0%{?rhel} && 0%{?rhel} == 6
sed -i -e '/create/ s/clamupdate/%{clamupdateuser}/g' clamav-unofficial-sigs.logrotate
%endif
# Fix shebang
sed -i -e 's^/usr/bin/env bash^/bin/bash^g' clamav-unofficial-sigs.sh
sed -i -e 's^/usr/bin/bash^/bin/bash^g' clamav-unofficial-sigs.cron

%if 0%{?rhel} && 0%{?rhel} <= 7
sed -i -e '/^#pkg_mgr/ s/^#//;s/""/"yum"/' config/master.conf
%else
sed -i -e '/^#pkg_mgr/ s/^#//;s/""/"dnf"/' config/master.conf
%endif
# Fix script path
sed -i -e '/ExecStart=/ s|/usr/local/sbin|%{_sbindir}|' systemd/clamav-unofficial-sigs.service
# Disable yara rules
sed -i -e '/^enable_yararules/ s/yes/no/' config/master.conf

%install
rm -rf %{buildroot}
install -d -p %{buildroot}%{_unitdir}
install -d -p %{buildroot}%{_sysconfdir}/%{name}
install -d -p %{buildroot}%{_sbindir}
install -d -p %{buildroot}%{_localstatedir}/log/%{name}
install -d -p %{buildroot}%{_localstatedir}/lib/%{name}
install -d -p %{buildroot}%{_sysconfdir}/cron.d
install -d -p %{buildroot}%{_sysconfdir}/logrotate.d
install -d -p %{buildroot}%{_mandir}/man8
install -p -m0755 clamav-unofficial-sigs.sh %{buildroot}%{_sbindir}/clamav-unofficial-sigs.sh
# config/packaging/os.centos7.conf file is for epel and fedora
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
install -p -m0644 config/packaging/os.centos7.conf %{buildroot}%{_sysconfdir}/%{name}/os.conf
%else
install -p -m0644 config/packaging/os.centos6.conf %{buildroot}%{_sysconfdir}/%{name}/os.conf
%endif
install -p -m0644 config/user.conf %{buildroot}%{_sysconfdir}/%{name}/user.conf
install -p -m0644 config/master.conf %{buildroot}%{_sysconfdir}/%{name}/master.conf
install -Dp -m 0644 systemd/clamav-unofficial-sigs.service %{buildroot}%{_unitdir}/clamav-unofficial-sigs.service
install -Dp -m 0644 systemd/clamav-unofficial-sigs.timer %{buildroot}%{_unitdir}/clamav-unofficial-sigs.timer
install -p -m0644 clamav-unofficial-sigs.cron %{buildroot}%{_sysconfdir}/cron.d/clamav-unofficial-sigs
install -p -m0644 clamav-unofficial-sigs.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/clamav-unofficial-sigs
install -p -m0644 clamav-unofficial-sigs.man8 %{buildroot}%{_mandir}/man8/clamav-unofficial-sigs.8

%files
%doc README.md 
%license LICENSE
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/os.conf
%config %{_sysconfdir}/%{name}/master.conf
%config(noreplace) %{_sysconfdir}/%{name}/user.conf
%{_sbindir}/clamav-unofficial-sigs.sh
%attr(0755,%{clamupdateuser},%{clamupdategrp}) %dir %{_localstatedir}/lib/%{name}
%attr(0755,%{clamupdateuser},%{clamupdategrp}) %dir %{_localstatedir}/log/%{name}
%if %{with_systemd}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%endif
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%{_sysconfdir}/logrotate.d/%{name}
%{_mandir}/man*/%{name}*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 16 2024 Robert Scheck <robert@fedoraproject.org> - 7.2.5-11
- Added upstream patch to fix urlhaus mkdir and ownership

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 04 2023 Didier Fabert <didier.fabert@gmail.com> - 7.2.5-8
- migrated to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 17 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.2.5-6
- Fix: grep: warning: stray \ before "
- Remove clean section

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.2.5-1
- Update to upstream.

* Thu Mar 18 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.2.4-1
- Update to upstream.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.2.2-1
- Update to upstream.

* Mon Dec 14 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.2.1-1
- Update to upstream.

* Mon Dec  7 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.2-1
- Update to upstream.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 23 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.0.1-5
- Remove delay from cron script, doesn't work as expected.

* Wed Feb 19 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.0.1-4
- Backslash percent character in cron script

* Thu Feb 13 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.0.1-3
- Make cron script as config(noreplace) (bz#1786860)
- Implement random delay before running update script from cron

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.0.1-1
- Update to upstream, remove changes applied upstream

* Sat Jan 25 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 7.0-1
- Update to upstream, fix version warnings (bz#1794506)

* Tue Oct 01 2019 Didier Fabert <didier.fabert@gmail.com> - 6.1.1-2
- Fix bash path
- Fix shebang

* Sat Sep 21 2019 Didier Fabert <didier.fabert@gmail.com> - 6.1.1-1
- Update from upstream
- Add cron, logrotate and man from fixed files (upstream way is too difficult to maintain)
- Fix buggy date in changelog

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 Didier Fabert <didier.fabert@gmail.com> - 5.6.2-7
- Add patch proposal for RHEL/CentOS 6 to use /sbin/service from Robert Scheck <robert@fedoraproject.org>

* Sun Mar 17 2019 Didier Fabert <didier.fabert@gmail.com> 5.6.2-6
- Fix local state dir owner and group on el6
- Fix typo in summary
- Remove INSTALL from doc

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 5.6.2-5
- Remove obsolete requirement for %%post scriptlet

* Thu Feb 28 2019 Didier Fabert <didier.fabert@gmail.com> 5.6.2-4
- Fix spec for el6 build

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Didier Fabert <didier.fabert@gmail.com> 5.6.2-3
- Fix logrotate (files are rotated more than one time)
- Fix clamd_restart_opt with try-restart
- Disable yara rules by default (can be enabled in user.conf to overrride master.conf setting)

* Wed Sep 12 2018 Didier Fabert <didier.fabert@gmail.com> 5.6.2-2
- Generate cron, logrotate and man files

* Wed Sep 12 2018 Didier Fabert <didier.fabert@gmail.com> 5.6.2-1
- Switch to new upstream: extremeshok on github

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.7.2-1
- Update to upstream
- EPEL7 branch
- New source URL and URL at sourceforge (see also debian bug#734593)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.7.1-11
- Add a missing requirement on crontabs to spec file
- Fixes RHBZ#988602

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Andrew Colin Kissa <andrew@topdog.za.net> - 3.7.1-8
- FIX: bugzilla #842180

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr 23 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 3.7.1-5
- FIX: bugzilla #683139

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 3.7.1-3
- Fixes requested by reviewer

* Thu Dec 23 2010 Andrew Colin Kissa <andrew@topdog.za.net> - 3.7.1-2
- Fixes requested by reviewer

* Tue Jul 20 2010 Andrew Colin Kissa <andrew@topdog.za.net> - 3.7.1-1
- upgraded to latest upstream

* Thu Apr 22 2010 Andrew Colin Kissa <andrew@topdog.za.net> - 3.7-3
- Fix sed error

* Mon Mar 15 2010 Andrew Colin Kissa <andrew@topdog.za.net> - 3.7-2
- Fix the cron entry

* Tue Mar 09 2010 Andrew Colin Kissa <andrew@topdog.za.net> - 3.7-1
- Initial packaging
