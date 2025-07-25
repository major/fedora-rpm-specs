%global srcname resalloc

%global sysuser  resalloc
%global sysgroup %sysuser
%global _homedir %_sharedstatedir/%{name}server

%global agent_user  resalloc-agent-spawner
%global agent_group %agent_user

%global create_user_group() \
getent group "%1" >/dev/null || groupadd -r "%1" \
getent passwd "%1" >/dev/null || \\\
useradd -r -g "%2" -G "%2" -s "%3" \\\
        -c "%1 service user" "%1" \\\
        -d "%4"

%global _logdir  %_var/log/%{name}server

%global sum Resource allocator for expensive resources
%global desc \
The resalloc project aims to help with taking care of dynamically \
allocated resources, for example ephemeral virtual machines used for \
the purposes of CI/CD tasks.


%bcond_without check

%if 0%{?fedora} || 0%{?rhel} > 7 || 0%{?is_opensuse}
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

# Modern distributions (using RPM v4.19+; for example, Fedora 39+) do not
# require the %%pre scriptlet for creating users/groups because the sysusers
# feature is now built directly into RPM.  Simply including the sysusers
# `mock.conf` file in a package payload is sufficient to leverage this feature.
# However, for older distributions that lack this capability, we still define
# the %%pre scriptlet.
%if (0%{?rhel} && 0%{?rhel} < 10) || (0%{?mageia} && 0%{?mageia} < 10) || (0%{?suse_version} && 0%{?suse_version} < 1660)
%bcond_without sysusers_compat
%else
%bcond_with sysusers_compat
%endif

%global default_python  %{?with_python3:python3}%{!?with_python3:python2}
%global default_sitelib %{?with_python3:%python3_sitelib}%{!?with_python3:%python_sitelib}

Name:       %srcname
Summary:    %sum - client tooling
Version:    5.11
Release:    2%{?dist}
License:    GPL-2.0-or-later
URL:        https://github.com/praiskup/resalloc
BuildArch:  noarch

BuildRequires: make
BuildRequires: postgresql-server


%if %{with python3}
BuildRequires: python3-alembic
BuildRequires: python3-argparse-manpage
BuildRequires: python3-devel
BuildRequires: python3-psycopg2
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-setuptools
BuildRequires: python3-six
BuildRequires: python3-sqlalchemy
%if 0%{?is_opensuse}
BuildRequires: python3-PyYAML
BuildRequires: cron
%else
BuildRequires: python3-yaml
%endif
%endif

%if %{with python2}
BuildRequires: python-alembic
BuildRequires: python2-argparse-manpage
BuildRequires: python2-devel
BuildRequires: python-psycopg2
BuildRequires: python2-mock
BuildRequires: python2-pytest
BuildRequires: python2-pytest-cov
BuildRequires: python2-setuptools
BuildRequires: python2-six
BuildRequires: python-sqlalchemy
BuildRequires: python-yaml
%endif

Requires:   %default_python-%srcname = %version-%release

%if %{with sysusers_compat}
Requires(pre): shadow-utils
%endif

Source0: https://github.com/praiskup/%name/releases/download/v%version/%name-%version.tar.gz
Source1: resalloc.service
Source5: resalloc-agent-spawner.service
Source2: logrotate
Source3: merge-hook-logs
Source4: cron.hourly
# GPL-2.0-or-later too
Source6: https://raw.githubusercontent.com/praiskup/wait-for-ssh/main/wait-for-ssh

%description
%desc

The %name package provides the client-side tooling.


%package server
Summary:    %sum - server part

Requires: crontabs
Requires: logrotate
Requires:   %default_python-%srcname = %version-%release
Requires:   %srcname-helpers = %version-%release
%if %{with python3}
Requires: python3-alembic
Requires: python3-six
Requires: python3-sqlalchemy
Requires: python3-yaml
%else
Requires: python-alembic
Requires: python2-six
Requires: python-sqlalchemy
Requires: python-yaml
%endif

%description server
%desc

The %name-server package provides the resalloc server, and
some tooling for resalloc administrators.


%package helpers
Summary:    %sum - helper/library scripts

%description helpers
%desc

Helper and library-like scripts for external Resalloc plugins like resalloc-aws,
resalloc-openstack, etc.


%if %{with python3}
%package webui
Summary:    %sum - webui part

%if %{with python3}
Requires:   %default_python-%srcname = %version-%release
Requires: %name-server
Requires: python3-flask
Recommends: %name-selinux
%endif

%description webui
%desc

The %name-webui package provides the resalloc webui,
it shows page with information about resalloc resources.
%endif

%if %{with python3}
%package agent-spawner
Summary: %sum - daemon starting agent-like resources

Requires: python3-copr-common >= 0.23
Requires: python3-daemon
Requires: python3-redis
Requires: python3-resalloc = %version-%release
Requires: python3-setproctitle

%description agent-spawner
%desc

Agent Spawner maintains sets resources (agents) of certain kind and in certain
number, according to given configuration.  Typical Resalloc resource is
completely dummy, fully controlled from the outside.  With agent-like resources
this is different — such resources are self-standing, they take care of
themselves, perhaps interacting/competing with each other.  The only thing that
agent-spawner needs to do is to control the ideal number of them.
%endif

%if %{with python3}
%package -n python3-%srcname
Summary: %sum - Python 3 client library
%{?python_provide:%python_provide python3-%srcname}
%description -n python3-%srcname
%desc

The python3-%name package provides Python 3 client library for talking
to the resalloc server.
%endif


%if %{with python2}
%package -n python2-%srcname
Summary: %sum - Python 2 client library
%{?python_provide:%python_provide python2-%srcname}
%description -n python2-%srcname
%desc

The python2-%name package provides Python 2 client library for talking
to the resalloc server.
%endif


%package selinux
Summary: SELinux module for %{name}
# Requires(post): policycoreutils-python
BuildRequires: selinux-policy-devel
%{?selinux_requires}

%description selinux
%desc

%post selinux
semanage fcontext -a -t httpd_sys_script_exec_t \
    %_var/www/cgi-%{name} 2>/dev/null || :
restorecon -R %_var/www/cgi-%{name} || :


%prep
%autosetup -p1 -n %name-%version
%if %{without python3}
rm -r resalloc_agent_spawner
%endif

# Create sysusers.d config files
cat >resalloc.sysusers.conf <<EOF
u resalloc - '%sysuser service user' %_homedir /bin/bash
m resalloc %sysgroup
EOF
cat >resalloc-agent-spawner.sysusers.conf <<EOF
u resalloc-agent-spawner - '%agent_user service user' - -
m resalloc-agent-spawner %agent_group
EOF


%build
%if %{with python2}
python=%__python2
%py2_build
%else
%py3_build
python=%__python3
%endif
sed "1c#! $python" %SOURCE6 > %{name}-wait-for-ssh


%install
%if %{with python2}
%py2_install
rm -r %buildroot%python2_sitelib/%{name}webui
%else
%py3_install
install -d -m 755 %buildroot%_datadir/%{name}webui
cp -r %{name}webui/templates %buildroot%_datadir/%{name}webui/
cp -r %{name}webui/static %buildroot%_datadir/%{name}webui/

install -d -m 755 %buildroot%_var/www/
install -p -m 755 %{name}webui/cgi-resalloc %buildroot%_var/www/cgi-%{name}
%endif

mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_logdir
install -p -m 644 %SOURCE1 %buildroot%_unitdir
%if %{with python3}
install -p -m 644 %SOURCE5 %buildroot%_unitdir
%endif
install -d -m 700 %buildroot%_homedir
install -d -m 700 %buildroot%_sysconfdir/logrotate.d
install -p -m 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/resalloc-server
install -p -m 644 man/resalloc-server.1 %buildroot%_mandir/man1
install -d -m 755 %buildroot/%_libexecdir
install -p -m 755 %SOURCE3 %buildroot/%_libexecdir/%name-merge-hook-logs
install -d %buildroot%_sysconfdir/cron.hourly
install -p -m 755 %SOURCE4 %buildroot%_sysconfdir/cron.hourly/resalloc
install -p -m 755 %name-wait-for-ssh %buildroot%_bindir/%name-wait-for-ssh

%if %{without python3}
rm %buildroot%_bindir/%name-agent-*
rm %buildroot%_sysconfdir/resalloc-agent-spawner/config.yaml
%endif

install -m0644 -D resalloc.sysusers.conf %{buildroot}%{_sysusersdir}/resalloc.conf
install -m0644 -D resalloc-agent-spawner.sysusers.conf %{buildroot}%{_sysusersdir}/resalloc-agent-spawner.conf


%if %{with check}
%check
%if %{with python2}
make check TEST_PYTHONS="python2"
%else
make check TEST_PYTHONS="python3"
%endif
%endif


# Simplify "alembic upgrade head" actions.
ln -s "%{default_sitelib}/%{name}server" %buildroot%_homedir/project


%if %{with sysusers_compat}
%pre server
%create_user_group %sysuser %sysgroup /bin/bash %_homedir
%endif

%post server
%systemd_post resalloc.service

%postun server
%systemd_postun_with_restart resalloc.service


%if %{with python3}
%if %{with sysusers_compat}
%pre agent-spawner
%create_user_group %agent_user %agent_group /bin/false /
%endif

%post agent-spawner
%systemd_post resalloc-agent-spawner.service

%postun agent-spawner
%systemd_postun_with_restart resalloc-agent-spawner.service
%endif


%global doc_files NEWS README.md

%files
%doc %doc_files
%license COPYING
%{_bindir}/%{name}
%_mandir/man1/%{name}.1*


%if %{with python3}
%files -n python3-%srcname
%doc %doc_files
%license COPYING
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*.egg-info
%endif


%if %{with python2}
%files -n python2-%srcname
%doc %doc_files
%license COPYING
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}-*.egg-info
%endif


%files server
%doc %doc_files
%license COPYING
%{default_sitelib}/%{name}server
%{_bindir}/%{name}-server
%{_bindir}/%{name}-maint
%attr(0750, %sysuser, %sysgroup) %dir %{_sysconfdir}/%{name}server
%config(noreplace) %{_sysconfdir}/%{name}server/*
%_unitdir/resalloc.service
%attr(0700, %sysuser, %sysgroup) %dir %_logdir
%_mandir/man1/%{name}-maint.1*
%_mandir/man1/%{name}-server.1*
%attr(0700, %sysuser, %sysgroup) %_homedir
%config %_sysconfdir/logrotate.d/resalloc-server
%_libexecdir/resalloc-merge-hook-logs
%config %attr(0755, root, root) %{_sysconfdir}/cron.hourly/resalloc
%{_sysusersdir}/resalloc.conf


%files helpers
%doc %doc_files
%license COPYING
%{_bindir}/%{name}-check-vm-ip
%{_bindir}/%{name}-wait-for-ssh


%if %{with python3}
%files agent-spawner
%_bindir/resalloc-agent*
%{default_sitelib}/%{name}_agent_spawner
%_unitdir/resalloc-agent-spawner.service
%config(noreplace) %_sysconfdir/resalloc-agent-spawner
%{_sysusersdir}/resalloc-agent-spawner.conf

%files webui
%doc %doc_files
%license COPYING
%{default_sitelib}/%{name}webui/
%_datadir/%{name}webui/
%_var/www/cgi-%{name}
%endif

%files selinux


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 21 2025 Pavel Raiskup <praiskup@redhat.com> - 5.11-1
- new upstream release, don't keep cleanup processes indefinitely:
  https://github.com/praiskup/resalloc/releases/tag/v5.11

* Thu Jun 12 2025 Pavel Raiskup <praiskup@redhat.com> - 5.10-1
- new upstream release, packages use RPM built-in sysusers support:
  https://github.com/praiskup/resalloc/releases/tag/v5.10

* Thu Jun 05 2025 Python Maint <python-maint@redhat.com> - 5.9-2
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Pavel Raiskup <praiskup@redhat.com> - 5.9-1
- New upstream release https://github.com/praiskup/resalloc/releases/tag/v5.9

* Thu Jan 16 2025 Jakub Kadlcik <frostyx@email.cz> - 5.8-1
- New upstream release https://github.com/praiskup/resalloc/releases/tag/v5.8

* Fri Jan 10 2025 Jakub Kadlcik <frostyx@email.cz> - 5.7-1
- New upstream release https://github.com/praiskup/resalloc/releases/tag/v5.7

* Mon Oct 07 2024 Pavel Raiskup <praiskup@redhat.com> - 5.6-1
- New upstream release https://github.com/praiskup/resalloc/releases/tag/v5.6

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 5.5-2
- Rebuilt for Python 3.13

* Wed Apr 24 2024 Pavel Raiskup <praiskup@redhat.com> - 5.5-1
- New upstream release https://github.com/praiskup/resalloc/releases/tag/v5.5

* Fri Mar 15 2024 Pavel Raiskup <praiskup@redhat.com> - 5.4-1
- New upstream release https://github.com/praiskup/resalloc/releases/tag/v5.4

* Wed Feb 28 2024 Pavel Raiskup <praiskup@redhat.com> - 5.3-1
- New upstream release https://github.com/praiskup/resalloc/releases/tag/v5.3

* Wed Feb 28 2024 Pavel Raiskup <praiskup@redhat.com> - 5.2-1
- New upstream release https://github.com/praiskup/resalloc/releases/tag/v5.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 06 2023 Pavel Raiskup <praiskup@redhat.com> - 5.1-1
- new upstream release https://github.com/praiskup/resalloc/releases/tag/v5.1

* Fri Aug 11 2023 Pavel Raiskup <praiskup@redhat.com> - 5.0-1
- new upstream release https://github.com/praiskup/resalloc/releases/tag/v5.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 4.9-3
- Rebuilt for Python 3.12

* Mon Jan 30 2023 Miro Hrončok <mhroncok@redhat.com> - 4.9-2
- Rebuilt to change Python shebangs to /usr/bin/python3.6 on EPEL 8

* Mon Jan 23 2023 Pavel Raiskup <praiskup@redhat.com> - 4.9-1
- new upstream release https://github.com/praiskup/resalloc/releases/tag/v4.9

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 23 2022 Pavel Raiskup <praiskup@redhat.com> - 4.8-1
- new upstream release:
  https://github.com/praiskup/resalloc/releases/tag/v4.8

* Tue Sep 20 2022 Pavel Raiskup <praiskup@redhat.com> - 4.7-1
- new upstream release:
  https://github.com/praiskup/resalloc/releases/tag/v4.7

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Jakub Kadlcik <frostyx@email.cz> - 4.6-2
- Add resalloc-selinux subpackage

* Wed Jun 29 2022 Jakub Kadlcik <frostyx@email.cz> - 4.6-1
- New upstream version:
  https://github.com/praiskup/resalloc/releases/tag/v4.6

* Thu Jun 23 2022 Pavel Raiskup <praiskup@redhat.com> - 4.5-1
- New upstream version:
  https://github.com/praiskup/resalloc/releases/tag/v4.5

* Wed Jun 22 2022 Jakub Kadlcik <python-maint@redhat.com> - 4.4-1
- New upstream version:
  https://github.com/praiskup/resalloc/releases/tag/v4.4

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 4.3-2
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Pavel Raiskup <praiskup@redhat.com> - 4.3-1
- new upstream release:
  https://github.com/praiskup/resalloc/releases/tag/v4.3

* Thu Jan 20 2022 Pavel Raiskup <praiskup@redhat.com> - 4.2-1
- new upstream release:
  https://github.com/praiskup/resalloc/releases/tag/v4.2

* Tue Aug 24 2021 Pavel Raiskup <praiskup@redhat.com> - 4.1-1
- bugfix release, with prioritized released resources again

* Mon Aug 23 2021 Pavel Raiskup <praiskup@redhat.com> - 4-1
- new release, with tag-priority

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Pavel Raiskup <praiskup@redhat.com> - 3.7-1
- new upstream release, see NEWS file

* Wed Jun 09 2021 Pavel Raiskup <praiskup@redhat.com> - 3.6-1
- rebase to a new version having DB performance fixes

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.4-3
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.4-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Fri Feb 19 2021 Silvie Chlupova <schlupov@redhat.com> - 3.4-1
- New upstream release v3.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Pavel Raiskup <praiskup@redhat.com> - 3.3-1
- new release, mostly fixing one bug causing traceback on too-long stdout output
  from AllocWorker script

* Tue Jun 02 2020 Pavel Raiskup <praiskup@redhat.com> - 3.2-1
- new configuration option cmd_release - command to be run before we mark the
  resource as reusable again
- after server restart, schedule all inconsistent resources to be terminated
  (mitigates issue#41)
- systemd service is restarted upon failure (just in case)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1-2
- Rebuilt for Python 3.9

* Tue May 26 2020 Pavel Raiskup <praiskup@redhat.com> - 3.1-1
- new version v3.1, improved resource checker

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Pavel Raiskup <praiskup@redhat.com> - 3.0-1
- new 3.0 version - new possibility to re-use resources, and client requests can
  survive server restarts

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Pavel Raiskup <praiskup@redhat.com> - 2.6-1
- don't assign resources to closed tickets

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Pavel Raiskup <praiskup@redhat.com> - 2.5-1
- thread safety - don't change os.environ

* Tue Jun 11 2019 Pavel Raiskup <praiskup@redhat.com> - 2.4-1
- fix improperly handled thread communication

* Fri May 10 2019 Pavel Raiskup <praiskup@redhat.com> - 2.3-3
- drop mkhomedir requires leftover
- configure logrotate to compress rotated logs

* Fri May 10 2019 Pavel Raiskup <praiskup@redhat.com> - 2.3-2
- fix logrotate typo s/lib/log/, package it as config file

* Fri May 10 2019 Pavel Raiskup <praiskup@redhat.com> - 2.3-1
- logrotate config (per review rhbz#1707302)
- provide manual page for resalloc-server (per rhbz#1707302)
- logrotate also the hooks directory

* Fri May 10 2019 Pavel Raiskup <praiskup@redhat.com> - 2.2-2
- move homedir from /home to /var/lib (per msuchy's review)

* Thu May 09 2019 Pavel Raiskup <praiskup@redhat.com> - 2.2-1
- new release

* Tue May 07 2019 Pavel Raiskup <praiskup@redhat.com> - 2.1-3
- provide summary/description (per msuchy's review)

* Tue May 07 2019 Pavel Raiskup <praiskup@redhat.com> - 2.1-2
- only support Python 3 or Python 2

* Tue May 07 2019 Pavel Raiskup <praiskup@redhat.com> - 2.1-1
- fixed racy testsuite

* Tue May 07 2019 Pavel Raiskup <praiskup@redhat.com> - 2.0-1
- release 2.0 (changed db schema for "id" within pool)

* Wed Oct 31 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-1
- bump, rebuild for Python 3.7

* Tue Jan 30 2018 Pavel Raiskup <praiskup@redhat.com> - 1.1-0
- release with removed 'cat' hack (commit 970b99725acf1dc)

* Thu Jan 18 2018 Pavel Raiskup <praiskup@redhat.com> - 0.1-12
- first release

* Wed Jan 17 2018 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-12
- better setup default directories

* Wed Jan 17 2018 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-11
- log both stdout and stderr for start/stop/livecheck commands

* Sat Jan 06 2018 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-10
- service: add WantedBy=multi-user.target

* Fri Sep 29 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-9
- fix homedir for ansible

* Fri Sep 29 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-8
- resalloc-maint resource-delete fix

* Thu Sep 28 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-7
- resalloc ticket-wait puts output to stdout
- new command resalloc-maint ticket-list

* Tue Sep 26 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-6
- create datadir directory for database files

* Tue Sep 26 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-5
- install manual pages
- add '--with check' option

* Thu Sep 21 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-4
- python2/python3 fixes

* Wed Sep 20 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-3
- resalloc user is not nologin anymore
- add resalloc-maint

* Tue Sep 19 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-2
- add service file
- install log directory for server

* Mon Sep 18 2017 Pavel Raiskup <praiskup@redhat.com>
- no changelog
