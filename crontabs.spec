%global snapshot_date 20190603
%global snapshot_commit 9e74f2d

Summary: Root crontab files used to schedule the execution of programs
Name: crontabs
Version: 1.11^%{snapshot_date}git%{snapshot_commit}
Release: %autorelease
# See https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/359 for reasoning why Public Domain is not here.
License: GPL-2.0-or-later
URL: https://github.com/cronie-crond/crontabs
Source0: https://github.com/cronie-crond/crontabs/releases/download/crontabs-%{snapshot_date}/%{name}-%(echo %{version}|cut -d\^ -f1)-%{snapshot_date}git.tar.gz
BuildArch: noarch
Requires: sed
Requires: cronie

%description
This package is used by Fedora mainly for executing files by cron.

The crontabs package contains root crontab files and directories.
You will need to install cron daemon to run the jobs from the crontabs.
The cron daemon such as cronie or fcron checks the crontab files to
see when particular commands are scheduled to be executed.  If commands
are scheduled, it executes them.

Crontabs handles a basic system function, so it should be installed on
your system.

%prep
%autosetup -n %{name}-%(echo %{version}|cut -d\^ -f1)

%build
#empty

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/cron.{hourly,daily,weekly,monthly}
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man4/

install -m644 ./crontab $RPM_BUILD_ROOT/etc/crontab
install -m755 ./run-parts $RPM_BUILD_ROOT/usr/bin/run-parts
install -m644 ./{crontabs,run-parts}.4 $RPM_BUILD_ROOT/%{_mandir}/man4/

mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/
touch $RPM_BUILD_ROOT/etc/sysconfig/run-parts

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%config(noreplace) /etc/crontab
%attr(0644,root,root) %config(noreplace) /etc/sysconfig/run-parts
%{_bindir}/run-parts
%dir /etc/cron.hourly
%dir /etc/cron.daily
%dir /etc/cron.weekly
%dir /etc/cron.monthly
%{_mandir}/man4/*

%changelog
%autochangelog
