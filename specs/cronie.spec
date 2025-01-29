%bcond selinux 1
%bcond pam 1
%bcond audit 1
%bcond inotify 1

Summary:   Cron daemon for executing programs at set times
Name:      cronie
Version:   1.7.2
Release:   %autorelease
License:   GPL-2.0-or-later AND BSD-3-Clause AND BSD-2-Clause AND ISC AND LGPL-2.1-or-later
URL:       https://github.com/cronie-crond/cronie
Source0:   https://github.com/cronie-crond/cronie/releases/download/cronie-%{version}/cronie-%{version}.tar.gz

Patch:     0001-do-no-leak-file-descriptors.patch
# https://github.com/cronie-crond/cronie/issues/193
Patch:     make_error_func_prototype_complete.patch

Requires:  dailyjobs

%if %{with selinux}
Requires:      libselinux >= 2.0.64
Buildrequires: libselinux-devel >= 2.0.64
%endif
%if %{with pam}
Requires:      pam >= 1.0.1
Buildrequires: pam-devel >= 1.0.1
%endif
%if %{with audit}
Buildrequires: audit-libs-devel >= 1.4.1
%endif

BuildRequires:    gcc
BuildRequires:    systemd
BuildRequires:    make
Obsoletes:        %{name}-sysvinit

Requires(post):   coreutils sed

%if 0%{?fedora} && 0%{?fedora} < 28 || 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on Fedora27/RHEL7
%endif


%description
Cronie contains the standard UNIX daemon crond that runs specified programs at
scheduled times and related tools. It is a fork of the original vixie-cron and
has security and configuration enhancements like the ability to use pam and
SELinux.

%package anacron
Summary:   Utility for running regular jobs
Requires:  crontabs
Provides:  dailyjobs
Provides:  anacron = 2.4
Obsoletes: anacron <= 2.3
Requires(post): coreutils
Requires:  %{name} = %{version}-%{release}

%description anacron
Anacron is part of cronie that is used for running jobs with regular
periodicity which do not have exact time of day of execution.

The default settings of anacron execute the daily, weekly, and monthly
jobs, but anacron allows setting arbitrary periodicity of jobs.

Using anacron allows running the periodic jobs even if the system is often
powered off and it also allows randomizing the time of the job execution
for better utilization of resources shared among multiple systems.

%package noanacron
Summary:   Utility for running simple regular jobs in old cron style
Provides:  dailyjobs
Requires:  crontabs
Requires:  %{name} = %{version}-%{release}

%description noanacron
Old style of running {hourly,daily,weekly,monthly}.jobs without anacron. No
extra features.

%prep
%autosetup -p1

%build
%configure \
    %{?with_pam:--with-pam} \
    %{?with_selinux:--with-selinux} \
    %{?with_audit:--with-audit} \
    %{?with_inotify:--with-inotify} \
    --enable-anacron \
    --enable-pie \
    --enable-relro

%make_build V=2

%install
%make_install DESTMAN=$RPM_BUILD_ROOT%{_mandir}
mkdir -pm700 $RPM_BUILD_ROOT%{_localstatedir}/spool/cron
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/
mkdir -pm755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/
%if ! %{with pam}
    rm -f $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/crond
%endif
install -m 644 crond.sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/crond
touch $RPM_BUILD_ROOT%{_sysconfdir}/cron.deny
install -m 644 contrib/anacrontab $RPM_BUILD_ROOT%{_sysconfdir}/anacrontab
install -c -m755 contrib/0hourly $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/0hourly
mkdir -pm 755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly
install -c -m755 contrib/0anacron $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/0anacron
mkdir -p $RPM_BUILD_ROOT/var/spool/anacron
touch $RPM_BUILD_ROOT/var/spool/anacron/cron.daily
touch $RPM_BUILD_ROOT/var/spool/anacron/cron.weekly
touch $RPM_BUILD_ROOT/var/spool/anacron/cron.monthly

# noanacron package
install -m 644 contrib/dailyjobs $RPM_BUILD_ROOT/%{_sysconfdir}/cron.d/dailyjobs

# install systemd initscript
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system/
install -m 644 contrib/cronie.systemd $RPM_BUILD_ROOT/lib/systemd/system/crond.service

%post
# run after an installation
%systemd_post crond.service

%post anacron
[ -e /var/spool/anacron/cron.daily ] || install -m 0600 -D /dev/null /var/spool/anacron/cron.daily 2>/dev/null || :
[ -e /var/spool/anacron/cron.weekly ] || install -m 0600 -D /dev/null /var/spool/anacron/cron.weekly 2>/dev/null || :
[ -e /var/spool/anacron/cron.monthly ] || install -m 0600 -D /dev/null /var/spool/anacron/cron.monthly 2>/dev/null || :

%preun
# run before a package is removed
%systemd_preun crond.service

%postun
# run after a package is removed
%systemd_postun_with_restart crond.service

%triggerun -- cronie-anacron < 1.4.1
# empty /etc/crontab in case there are only old regular jobs
cp -a /etc/crontab /etc/crontab.rpmsave
sed -e '/^01 \* \* \* \* root run-parts \/etc\/cron\.hourly/d'\
  -e '/^02 4 \* \* \* root run-parts \/etc\/cron\.daily/d'\
  -e '/^22 4 \* \* 0 root run-parts \/etc\/cron\.weekly/d'\
  -e '/^42 4 1 \* \* root run-parts \/etc\/cron\.monthly/d' /etc/crontab.rpmsave > /etc/crontab
exit 0

%triggerun -- cronie < 1.4.7-2
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply crond
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save crond

# The package is allowed to autostart:
/bin/systemctl enable crond.service >/dev/null 2>&1

/bin/chkconfig --del crond >/dev/null 2>&1 || :
/bin/systemctl try-restart crond.service >/dev/null 2>&1 || :
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%triggerin -- pam, glibc, libselinux
# changes in pam, glibc or libselinux can make crond crash
# when it calls pam
/bin/systemctl try-restart crond.service >/dev/null 2>&1 || :

%files
%doc AUTHORS README ChangeLog
%{!?_licensedir:%global license %%doc}
%license COPYING
%attr(755,root,root) %{_bindir}/crond
%attr(4755,root,root) %{_bindir}/crontab
%attr(755,root,root) %{_bindir}/cronnext
%{_mandir}/man8/crond.*
%{_mandir}/man8/cron.*
%{_mandir}/man5/crontab.*
%{_mandir}/man1/crontab.*
%{_mandir}/man1/cronnext.*
%dir %{_localstatedir}/spool/cron
%dir %{_sysconfdir}/cron.d
%if %{with pam}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/crond
%endif
%config(noreplace) %{_sysconfdir}/sysconfig/crond
%config(noreplace,missingok) %{_sysconfdir}/cron.deny
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/0hourly
%attr(0644,root,root) /lib/systemd/system/crond.service

%files anacron
%{_bindir}/anacron
%attr(0755,root,root) %{_sysconfdir}/cron.hourly/0anacron
%config(noreplace) %{_sysconfdir}/anacrontab
%dir /var/spool/anacron
%ghost %attr(0600,root,root) %verify(not md5 size mtime) /var/spool/anacron/cron.daily
%ghost %attr(0600,root,root) %verify(not md5 size mtime) /var/spool/anacron/cron.weekly
%ghost %attr(0600,root,root) %verify(not md5 size mtime) /var/spool/anacron/cron.monthly
%{_mandir}/man5/anacrontab.*
%{_mandir}/man8/anacron.*

%files noanacron
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/dailyjobs

%changelog
%autochangelog
