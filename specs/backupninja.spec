
Name:		backupninja
Version:	1.2.2
Release:	7%{?dist}
Summary:	Lightweight, extensible backup system

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://0xacab.org/liberate/backupninja
Source0:	https://0xacab.org/liberate/backupninja/-/archive/backupninja-%{version}/backupninja-backupninja-%{version}.tar.gz#/backupninja-%{version}.tar.gz

Patch0:		backupninja-1.2.1-redhat.patch
Patch1:		backupninja-1.2.1-duplicity.patch
Patch2:		backupninja-1.2.1-extbackup.patch

BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make

Requires:	cronie
Requires:	gawk
Requires:	logrotate
Requires:	rdiff-backup


%description
Backupninja allows you to coordinate system backup by dropping a few simple
configuration files into /etc/backup.d/. Most programs you might use for making
backups don't have their own configuration file format. Backupninja provides
a centralized way to configure and schedule many different backup utilities.

It allows for secure, remote, incremental file system backup (via rdiff-backup),
compressed incremental data, backup system and hardware info, encrypted remote
backups (via duplicity), safe backup of MySQL/PostgreSQL databases, subversion
or trac repositories, burn CD/DVDs or create ISOs, incremental rsync with
hard-linking.


%prep
%setup -q -n backupninja-backupninja-%{version}
%patch -P0 -p1 -b .redhat
%patch -P1 -p1 -b .dupver
%patch -P2 -p1 -b .extbck

%build
# prepare build script
./autogen.sh

# put all script 'libs' into one dir
%configure --libdir=%{_libexecdir}

%make_build

%install
%make_install
mkdir -p -m 0750 %{buildroot}/%{_sysconfdir}/backup.d


%files
%{_sbindir}/backupninja
%{_sbindir}/ninjahelper
%{_libexecdir}/backupninja
%doc AUTHORS CHANGELOG.md FAQ.md README.md TODO
%license COPYING
%config(noreplace) %{_sysconfdir}/backupninja.conf
%config(noreplace) %{_sysconfdir}/cron.d/backupninja
%config(noreplace) %{_sysconfdir}/logrotate.d/backupninja
%dir %attr(0750,root,root )%{_sysconfdir}/backup.d
%{_datadir}/backupninja
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.2-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 25 2023 Denis Fateyev <denis@fateyev.com> - 1.2.2-1
- Update to 1.2.2 version

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 27 2022 Denis Fateyev <denis@fateyev.com> - 1.2.1-1
- Update to 1.2.1 version

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Denis Fateyev <denis@fateyev.com> - 1.1.0-5
- Update patch set for backupninja-1.1.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 30 2018 Denis Fateyev <denis@fateyev.com> - 1.1.0-1
- Update to 1.1.0 version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 08 2016 Denis Fateyev <denis@fateyev.com> - 1.0.1-8
- Fix duplicity path and S3, CloudFiles usage

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 21 2014 Denis Fateyev <denis@fateyev.com> - 1.0.1-5
- Added patch for RH-system specific

* Mon Sep 08 2014 Denis Fateyev <denis@fateyev.com> - 1.0.1-4
- Fix rsync action handler

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 19 2014 Denis Fateyev <denis@fateyev.com> - 1.0.1-2
- Fix RHEL5 cron dependencies

* Thu Jan 16 2014 Denis Fateyev <denis@fateyev.com> - 1.0.1-1
- Initial Fedora RPM package
