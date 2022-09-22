%bcond_without pgdump
%bcond_without pg_basebackup
%bcond_without xtrabackup
%bcond_without commvault
%bcond_without mongodump
%bcond_without mariabackup

Name: holland
Version: 1.2.10
Release: 2%{?dist}
Summary: Pluggable Backup Framework
License: BSD
URL: http://hollandbackup.org
Source0: https://github.com/holland-backup/holland/archive/v%{version}/holland-%{version}.tar.gz
Source1: https://github.com/holland-backup/holland-backup.github.com/archive/v%{version}/holland-docs-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
# need at least 1.0 for man page builder
BuildRequires: python3-sphinx >= 1.0
BuildRequires: make
Requires: python3-setuptools
Requires: python3-six
Requires: python3-configobj


%description
A pluggable backup framework which focuses on, but is not limited to, highly
configurable database backups.


%package common
Summary: Common library functionality for Holland Plugins
License: GPLv2+
Requires: %{name} = %{version}-%{release}


%description common
Library for common functionality used by holland plugins


%package mysql
Summary: MySQL library functionality for Holland Plugins
License: GPLv2+
Requires: %{name}-common = %{version}-%{release}
Requires: python3-mysqlclient


%description mysql
Library for MySQL functionality used by holland plugins


%package mysqldump
Summary: Logical mysqldump backup plugin for Holland
License: GPLv2+
Requires: %{name}-mysql = %{version}-%{release}
Requires: /usr/bin/mysqldump


%description mysqldump
This plugin allows holland to perform logical backups of a MySQL database
using the mysqldump command.


%package lvm
Summary: LVM library functionality for Holland Plugins
License: GPLv2+
Requires: %{name} = %{version}-%{release}


%description lvm
Library for LVM functionality used by holland plugins


%package mysqllvm
Summary: Holland LVM snapshot backup plugin for MySQL
License: GPLv2+
Requires: %{name}-mysql = %{version}-%{release}
Requires: %{name}-lvm = %{version}-%{release}
Requires: lvm2 tar


%description mysqllvm
This plugin allows holland to perform LVM snapshot backups of a MySQL database
and to generate a tar archive of the raw data directory.


%if %{with pgdump}
%package pgdump
Summary: Holland Backup Provider for PostgreSQL
License: GPLv2+
Requires: %{name}-common = %{version}-%{release}
Requires: python3-psycopg2


%description pgdump
This plugin allows holland to backup PostgreSQL databases via the pg_dump command.
%endif


%if %{with pg_basebackup}
%package pg_basebackup
Summary: Holland Backup Provider for PostgreSQL
License: GPLv2+
Requires: %{name}-common = %{version}-%{release}
Requires: python3-psycopg2
 
 
%description pg_basebackup
This plugin allows holland to backup PostgreSQL databases via the pg_basebackup command.
%endif


%if %{with xtrabackup}
%package xtrabackup
Summary: Holland plugin for Percona XtraBackup
License: GPLv2+
Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-mysql = %{version}-%{release}
Requires: /usr/bin/xtrabackup
Requires: python3-mysqlclient


%description xtrabackup
This package provides a Holland plugin for Percona Xtrabackup. This
plugin requires Percona XtraBackup and runs the provided
/usr/bin/innobackupex script.
%endif


%if %{with mongodump}
%package mongodump
Summary: Mongodump backup provider plugin for holland
License: GPLv2+
Requires: %{name}-common = %{version}-%{release}
Requires: python3-pymongo


%description mongodump
This plugin allows holland to backup MongoDB databases via the mongodump command.
%endif


%if %{with mariabackup}
%package mariabackup
Summary: Holland plugin for Mariabackup
License: GPLv2+
Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-mysql = %{version}-%{release}
# This plugin shells out to the `mariabackup` command, which was added in
# MariaDB 10.1.  In Fedora it is packaged as mariadb-backup, but the
# mariadb.org repo calls it MariaDB-backup.  To allow either to be used,
# require the command path instead of a package name.
Requires: /usr/bin/mariabackup


%description mariabackup
This package provides a Holland plugin for MariaDB-backup. This plugin requires
MariaDB-backup and runs the provided /usr/bin/mariabackup.
%endif


%if %{with commvault}
%package commvault
Summary: Holland plugin for Commvault
License: BSD
Requires: %{name} = %{version}-%{release}
Requires: python3-pid
Requires: tar
Obsoletes: %{name}-commvault < 1.0.3-3


%description commvault
This package provides the holland Commvault command plugin, enabling Commvault
environments to trigger a backup through holland.
%endif


%prep
%setup -q -a 1
rmdir docs
mv holland-backup.github.io-%{version} docs

find -name setup.cfg -delete
mv plugins/README README.plugins
mv config/providers/README README.providers

# cleanup, will be removed upstream at some point
rm plugins/ACTIVE


%build
%py3_build
make -C docs man

# library : holland.lib.common
pushd plugins/holland.lib.common
%py3_build
popd

# library : holland.lib.mysql
pushd plugins/holland.lib.mysql
%py3_build
popd

# library: holland.lib.lvm
pushd plugins/holland.lib.lvm
%py3_build
popd

# plugin : holland.backup.mysqldump
pushd plugins/holland.backup.mysqldump
%py3_build
popd

# plugin : holland.backup.mysql_lvm
pushd plugins/holland.backup.mysql_lvm
%py3_build
popd

%if %{with pgdump}
# plugin : holland.backup.pgdump
pushd plugins/holland.backup.pgdump
%py3_build
popd
%endif
	
%if %{with pg_basebackup}
# plugin : holland.backup.pg_basebackup
pushd plugins/holland.backup.pg_basebackup
%py3_build
popd
%endif

%if %{with xtrabackup}
# plugin : holland.backup.xtrabackup
pushd plugins/holland.backup.xtrabackup
%py3_build
popd
%endif

%if %{with mongodump}
# plugin : holland.backup.mongodump
pushd plugins/holland.backup.mongodump
%py3_build
popd
%endif

%if %{with mariabackup}
# plugin : holland.backup.mariabackup
pushd plugins/holland.backup.mariabackup
%py3_build
popd
%endif

%if %{with commvault}
# plugin : holland_commvault
pushd contrib/holland-commvault
%py3_build
popd
%endif


%install
mkdir -p %{buildroot}%{_sysconfdir}/holland/{backupsets,providers} \
         %{buildroot}%{_localstatedir}/spool/holland \
         %{buildroot}%{_localstatedir}/log/holland \
         %{buildroot}%{_mandir}/man5

# holland-core
%py3_install
mkdir -p %{buildroot}%{python3_sitelib}/holland/{lib,backup,commands,restore}
install -m 0640 config/holland.conf %{buildroot}%{_sysconfdir}/holland/
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 docs/_build/man/holland.1 %{buildroot}%{_mandir}/man1

# library : holland.lib.common
pushd plugins/holland.lib.common
%py3_install
popd

# library : holland.lib.mysql
pushd plugins/holland.lib.mysql
%py3_install
popd

# library: holland.lib.lvm
pushd plugins/holland.lib.lvm
%py3_install
popd

# plugin : holland.backup.mysqldump
pushd plugins/holland.backup.mysqldump
%py3_install
popd
install -m 0640 config/providers/mysqldump.conf %{buildroot}%{_sysconfdir}/holland/providers/

# plugin : holland.backup.mysql_lvm
pushd plugins/holland.backup.mysql_lvm
%py3_install
popd
install -m 0640 config/providers/mysql-lvm.conf %{buildroot}%{_sysconfdir}/holland/providers/
install -m 0640 config/providers/mysqldump-lvm.conf %{buildroot}%{_sysconfdir}/holland/providers/

# plugin : holland.backup.pgdump
%if %{with pgdump}
pushd plugins/holland.backup.pgdump
%py3_install
popd
install -m 0640 config/providers/pgdump.conf %{buildroot}%{_sysconfdir}/holland/providers/
%endif

# plugin : holland.backup.pg_basebackup
%if %{with pg_basebackup}
pushd plugins/holland.backup.pg_basebackup
%py3_install
popd
install -m 0640 config/providers/pg_basebackup.conf %{buildroot}%{_sysconfdir}/holland/providers/
%endif

%if %{with xtrabackup}
# plugin : holland.backup.xtrabackup
pushd plugins/holland.backup.xtrabackup
%py3_install
popd
install -m 0640 config/providers/xtrabackup.conf %{buildroot}%{_sysconfdir}/holland/providers/
%endif

%if %{with mongodump}
# plugin : holland.backup.mongodump
pushd plugins/holland.backup.mongodump
%py3_install
popd
install -m 0640 config/providers/mongodump.conf %{buildroot}%{_sysconfdir}/holland/providers/
%endif

%if %{with mariabackup}
# plugin : holland.backup.mariabackup
pushd plugins/holland.backup.mariabackup
%py3_install
popd
install -m 0640 config/providers/mariabackup.conf %{buildroot}%{_sysconfdir}/holland/providers/
%endif

%if %{with commvault}
# plugin : holland_commvault
pushd contrib/holland-commvault
%py3_install
install -m 0644 doc/holland_cvmysqlsv.1 %{buildroot}%{_mandir}/man1
popd
%endif

# logrotate
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/holland <<EOF
/var/log/holland.log /var/log/holland/holland.log {
    rotate 4
    weekly
    compress
    missingok
    create root adm
}
EOF


%files
%license LICENSE
%doc CHANGES.rst README.md README.plugins README.providers config/backupsets/examples/
%{_bindir}/holland
%{_mandir}/man1/holland.1*
%{_localstatedir}/log/holland/
%attr(0755,root,root) %dir %{_sysconfdir}/holland/
%attr(0755,root,root) %dir %{_sysconfdir}/holland/backupsets/
%attr(0755,root,root) %dir %{_sysconfdir}/holland/providers/
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/holland/holland.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/holland
%attr(0755,root,root) %{_localstatedir}/spool/holland/
%dir %{python3_sitelib}/holland/
%dir %{python3_sitelib}/holland/backup/
%dir %{python3_sitelib}/holland/backup/__pycache__
%dir %{python3_sitelib}/holland/restore/
%dir %{python3_sitelib}/holland/lib/
%dir %{python3_sitelib}/holland/lib/__pycache__
%{python3_sitelib}/holland/commands/
%{python3_sitelib}/holland/core/
%{python3_sitelib}/holland-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland-%{version}-py%{python3_version}.egg-info/


%files common
%license plugins/holland.lib.common/LICENSE
%doc plugins/holland.lib.common/README
%{python3_sitelib}/holland/lib/archive/
%{python3_sitelib}/holland/lib/compression.py
%{python3_sitelib}/holland/lib/safefilename.py
%{python3_sitelib}/holland/lib/which.py
%{python3_sitelib}/holland/lib/util.py
%{python3_sitelib}/holland/lib/__pycache__/compression.cpython-%{python3_version_nodots}*.py*
%{python3_sitelib}/holland/lib/__pycache__/safefilename.cpython-%{python3_version_nodots}*.py*
%{python3_sitelib}/holland/lib/__pycache__/which.cpython-%{python3_version_nodots}*.py*
%{python3_sitelib}/holland/lib/__pycache__/util.cpython-%{python3_version_nodots}*.py*
%{python3_sitelib}/holland.lib.common-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland.lib.common-%{version}-py%{python3_version}.egg-info/


%files mysql
%license plugins/holland.lib.mysql/LICENSE
%{python3_sitelib}/holland/lib/mysql/
%{python3_sitelib}/holland.lib.mysql-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland.lib.mysql-%{version}-py%{python3_version}.egg-info/


%files mysqldump
%license plugins/holland.backup.mysqldump/LICENSE
%doc plugins/holland.backup.mysqldump/README
%{python3_sitelib}/holland/backup/mysqldump/
%{python3_sitelib}/holland.backup.mysqldump-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland.backup.mysqldump-%{version}-py%{python3_version}.egg-info/
%config(noreplace) %{_sysconfdir}/holland/providers/mysqldump.conf


%files lvm
%license plugins/holland.lib.lvm/LICENSE
%doc plugins/holland.lib.lvm/README
%{python3_sitelib}/holland/lib/lvm/
%{python3_sitelib}/holland.lib.lvm-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland.lib.lvm-%{version}-py%{python3_version}.egg-info/


%files mysqllvm
%license plugins/holland.backup.mysql_lvm/LICENSE
%doc plugins/holland.backup.mysql_lvm/README
%{python3_sitelib}/holland/backup/mysql_lvm/
%{python3_sitelib}/holland.backup.mysql_lvm-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland.backup.mysql_lvm-%{version}-py%{python3_version}.egg-info/
%config(noreplace) %{_sysconfdir}/holland/providers/mysql-lvm.conf
%config(noreplace) %{_sysconfdir}/holland/providers/mysqldump-lvm.conf


%if %{with pgdump}
%files pgdump
%license plugins/holland.backup.pgdump/LICENSE
%doc plugins/holland.backup.pgdump/README
%{python3_sitelib}/holland/backup/pgdump/
%{python3_sitelib}/holland.backup.pgdump-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland.backup.pgdump-%{version}-py%{python3_version}.egg-info/
%config(noreplace) %{_sysconfdir}/holland/providers/pgdump.conf
%endif

	
%if %{with pg_basebackup}
%files pg_basebackup
%license plugins/holland.backup.pg_basebackup/LICENSE
%doc plugins/holland.backup.pg_basebackup/README
%{python3_sitelib}/holland/backup/pg_basebackup/
%{python3_sitelib}/holland.backup.pg_basebackup-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland.backup.pg_basebackup-%{version}-py%{python3_version}.egg-info/
%config(noreplace) %{_sysconfdir}/holland/providers/pg_basebackup.conf
%endif


%if %{with xtrabackup}
%files xtrabackup
%license plugins/holland.backup.xtrabackup/LICENSE
%doc plugins/holland.backup.xtrabackup/README
%{python3_sitelib}/holland/backup/xtrabackup/
%{python3_sitelib}/holland.backup.xtrabackup-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland.backup.xtrabackup-%{version}-py%{python3_version}.egg-info/
%config(noreplace) %{_sysconfdir}/holland/providers/xtrabackup.conf
%endif


%if %{with mongodump}
%files mongodump
%license plugins/holland.backup.mongodump/LICENSE
%doc plugins/holland.backup.mongodump/README
%{python3_sitelib}/holland/backup/mongodump.py
%{python3_sitelib}/holland/backup/__pycache__/mongodump.cpython-%{python3_version_nodots}*.py*
%{python3_sitelib}/holland.backup.mongodump-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland.backup.mongodump-%{version}-py%{python3_version}.egg-info/
%config(noreplace) %{_sysconfdir}/holland/providers/mongodump.conf
%endif


%if %{with mariabackup}
%files mariabackup
%license plugins/holland.backup.mariabackup/LICENSE
%doc plugins/holland.backup.mariabackup/README
%{python3_sitelib}/holland/backup/mariabackup/
%{python3_sitelib}/holland.backup.mariabackup-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/holland.backup.mariabackup-%{version}-py%{python3_version}.egg-info/
%config(noreplace) %{_sysconfdir}/holland/providers/mariabackup.conf
%endif


%if %{with commvault}
%files commvault
%license contrib/holland-commvault/LICENSE
%doc contrib/holland-commvault/README
%{_bindir}/holland_cvmysqlsv
%{_mandir}/man1/holland_cvmysqlsv.1*
%{python3_sitelib}/holland_commvault/
%{python3_sitelib}/holland_commvault-%{version}-py%{python3_version}.egg-info/
%endif


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 survient@fedoraproject.org - 1.2.10-1
- Latest upstream release.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.9-4
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Sam P <survient@fedoraproject.org> - 1.2.9-2
- Incorporated soulen's changes from #9. Fixed Changelog formatting. Fixed path to pgbasedump license file.

* Fri Dec 03 2021 Sam P <survient@fedoraproject.org> - 1.2.9-1
- Latest upstream release.

* Wed Nov 17 2021 Sam P <survient@fedoraproject.org> - 1.2.8-1
- Latest upstream release.

* Fri Aug 20 2021 Sam P <survient@fedoraproject.org> - 1.2.7-1
- Updated to latest upstream release.

* Thu Aug 05 2021 Sam P <survient@fedoraproject.org> - 1.2.6-1
- Updated to latest upstream release.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.4-2
- Rebuilt for Python 3.10

* Fri Mar 12 2021 Sam P <survient@fedoraproject.org> - 1.2.4-1
- Updated to latest upstream release.

* Tue Mar 09 2021 Sam P <survient@fedoraproject.org> - 1.2.3-3
- Incorporated changes from pull request #7 from fab for 
  python3-mysqlclient dependency.

* Mon Mar 08 2021 Sam P <survient@fedoraproject.org> - 1.2.3-2
- Identified github tagging issue and reverted source URL.

* Thu Mar 04 2021 Sam P <survient@fedoraproject.org> - 1.2.3-1
- Updated to latest upstream release.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Sam P <survient@fedoraproject.org> - 1.2.2-1
- Updated to latest upstream release.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.21-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Pete Travis <immanetize@fedoraproject.org - 1.1.21-1
- Update to latest upstream 1.1.21
- Fixes encoding issue https://github.com/holland-backup/holland/issues/302

* Thu Dec 05 2019 Sam P <survient@fedoraproject.org> - 1.1.20-1
- Latest upstream

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.18-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.18-2
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Sam P <survient@fedoraproject.org> - 1.1.18-1
- Latest upstream

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Pete Travis <me@petetravis.com> - 1.1.15-2
- add dependencies for holland-mysql to relevant subpackages

* Thu May 02 2019 Pete Travis <immanetize@fedoraproject.org> - 1.1.15-1
- Latest upstream

* Tue Mar 12 2019 Carl George <carl@george.computer> - 1.1.13-1
- Latest upstream

* Mon Feb 18 2019 Carl George <carl@george.computer> - 1.1.12-1
- Latest upstream

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Carl George <carl@george.computer> - 1.1.10-1
- Latest upstream

* Tue Dec 18 2018 Carl George <carl@george.computer> - 1.1.9-1
- Latest upstream

* Thu Oct 11 2018 Pete Travis <immanetize@fedoraproject.org> - 1.1.8-2
- Latest upstream
- change requires for xtrabackup subpackage to path to allow for alternative sources

* Wed Oct 03 2018 Carl George <carl@george.computer> - 1.1.7-1
- Latest upstream

* Wed Oct 03 2018 Carl George <carl@george.computer> - 1.1.6-1
- Latest upstream

* Thu Sep 13 2018 Carl George <carl@george.computer> - 1.1.5-1
- Latest upstream

* Wed Sep 05 2018 Carl George <carl@george.computer> - 1.1.4-1
- Latest upstream

* Fri Aug 31 2018 Carl George <carl@george.computer> - 1.1.3-2
- Add missing configobj dependency

* Fri Aug 31 2018 Carl George <carl@george.computer> - 1.1.3-1
- Latest upstream
- Add missing pymongo dependency

* Fri Aug 17 2018 Carl George <carl@george.computer> - 1.1.2-1
- Latest upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Pete Travis <immanetize@fedoraproject.org> - 1.1.0-1
- build in py3 for Fedora
- new upstream release 1.1.0
- deprecate mysql-hotcopy subpackage

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Carl George <carl.george@rackspace.com> - 1.0.14-2
- Remove unneeded holland_version macro
- Remove example, maatkit, and random subpackages
- Move holland.lib.mysql and holland.lib.lvm modules into their own subpackages
- Clean up requirements

* Fri Nov 18 2016 Ben Harper <ben.harper@rackspace.com> - 1.0.14-1
- Latest upstream
- remove Patch0, fixed upstream

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.12-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 22 2016 Carl George <carl.george@rackspace.com> - 1.0.12-6
- Integrate commvault plugin

* Tue Mar 01 2016 Carl George <carl.george@rackspace.com> - 1.0.12-2
- Backport gh#145

* Tue Feb 09 2016 Carl George <carl.george@rackspace.com> - 1.0.12-1
- Latest upstream
- Switch to python2 macros
- Require python-mysql on F22+ (not MySQL-python)
- Update xtrabackup summary/description (see upstream commit 3487d01)
- Drop obsoletes for -random and -lvm
- Require percona-xtrabackup where available (F21+)
- Add tar subpackage, but leave it disabled
- Remove redundant requirements
- Remove redundant provides

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 22 2014 Ben Harper <ben.harper@rackspace.com> - 1.0.10-3
- RH#884890 add requires for /usr/bin/mysqldump
- add mysqldump-lvm.conf

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.10-1
- Latest 1.0 sources from upstream.
- LP#706997 has been addressed upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 18 2012 BJ Dierkes <wdierkes@rackspace.com> - 1.0.6-7
- Fixed -pgdump summary per BZ#847855.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 BJ Dierkes <wdierkes@rackspace.com> - 1.0.6-3
- Added Patch0: holland-1.0.6-bug706997.patch which resolves
  LP#706997 purge-policy = before-backup problem

* Thu Jan 13 2011 BJ Dierkes <wdierkes@rackspace.com> - 1.0.6-2
- Remove Requires: xtrabackup from holland-xtrabackup.  Fedora
  doesn't provide xtrabackup currently, however there are solutions
  out there that people may want to use holland-xtrabackup for.

* Wed Jan 12 2011 BJ Dierkes <wdierkes@rackspace.com> - 1.0.6-1
- Latest sources from upstream.  Full change log available at:
  http://hollandbackup.org/releases/stable/1.0/CHANGES.txt
- ChangeLog became CHANGES.txt
- Add pgdump and xtrabackup by default
- No longer package -random by default (shouldn't have been in
  anyway).  Main package Obsoletes: holland-random < 1.0.6

* Tue Dec 14 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0.5-1
- Development version

* Tue Dec 14 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0.4-3
- Remove condition check around setting python_site{lib,arch} as
  it is not supported in el4.
- No longer set python_sitearch as we aren't using it

* Tue Nov 02 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0.4-2
- Make the example plugin optional (do not include by default)

* Tue Oct 26 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0.4-1
- Latest sources from upstream.
- No longer install /etc/holland/backupsets/examples, only keep it
  in %%doc
- Install config/providers/README to doc README.providers

* Thu Jul 08 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0.2-2
- Updated Source0 URL
- Updated python_sitelib/python_sitearch (per FPG)
- BuildRequires: python2-devel (per FPG)

* Thu Jul 08 2010 Andrew Garner <andrew.garner@rackspace.com> - 1.0.2-1
- Source updated to 1.0.2

* Tue Jul 06 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0.0-4
- Source update, 1.0.0 final
- Add ChangeLog back in under %%doc

* Thu Jul 01 2010 Andrew Garner <andrew.garner@rackspace.com> - 1.0.0-3.rc3
- Source updated to rc3

* Mon Jun 28 2010 Andrew Garner <andrew.garner@rackspace.com> - 1.0.0-2.rc2
- Source updated to rc2

* Fri Jun 11 2010 Andrew Garner <andrew.garner@rackspace.com> - 1.0.0-1.rc1
- Repackaging for release candidate
- Using conditional builds to exclude experimental plugins

* Tue Jun 08 2010 Andrew Garner <andrew.garner@rackspace.com> - 0.9.9-12
- Revert directory permissions back to standard 0755

* Sun Jun 06 2010 Andrew Garner <andrew.garner@rackspace.com> - 0.9.9-11
- Updated for changes from LVM cleanup

* Thu Jun 03 2010 Andrew Garner <andrew.garner@rackspace.com> - 0.9.9-10
- Added xtrabackup plugin

* Thu May 27 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.9.9-9
- Move plugins/README to README.plugins and install via %%doc

* Tue May 25 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.9.9-8
- Adding holland.lib.lvm under -common subpackage

* Wed May 19 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.9.9-7
- BuildRequires: python-sphinx (to build docs)

* Mon May 17 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.9.9-6
- Added sqlite plugin
- Loop over plugins rather than explicity build/install each.  Removes
  currently incomplete plugins first (pgdump)

* Fri May 14 2010 Tim Soderstrom <tsoderst@racksapce.com> - 0.9.9-5
- Added random plugin

* Mon May 10 2010 Andrew Garner <andrew.garner@rackspace.com> - 0.9.9-4
- Added missingok to holland.logrotate

* Sat May 8 2010 Andrew Garner <andrew.garner@rackspace.com> - 0.9.9-3
- Cleaned up /usr/share/docs/holland-* to only include html user documentation
  rather than everything in docs/
- /var/spool/holland and /var/log/holland/ are no longer world-readable
- /etc/holland/backupsets/examples is now a symlink to examples in the
  /usr/share/docs/holland-* directory
- The plugins/ACTIVE file is no longer used in order to have more flexibility
  in handling each individual plugin
- The setup.py --record mechanism is no longer used
- holland/{lib,commands,backup,restore} are now owned by the main holland
  package.

* Wed Apr 14 2010 Andrew Garner <andrew.garner@rackspace.com> - 0.9.9-2
- Updated rpm for new tree layout

* Tue Apr 13 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.9.9-1.rs
- Removed -commvault subpackage
- Removed mysql-lvm config file hack
- Changed URL to http://hollandbackup.org
- No longer package plugins as eggs
- Conditionally BuildRequire: python-nose and run nose tests if _with_tests

* Wed Apr 07 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.9.8-2.rs
- Rename holland-lvm to holland-mysqllvm, Obsoletes: holland-lvm
- Manually install mysql-lvm.conf provider config (fixed in 0.9.9)
- Install man files to _mandir
- Make logrotate.d/holland config(noreplace)

* Fri Apr 02 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.9.8-1.rs
- Latest stable source from upstream.

* Wed Dec 09 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.9.7dev-1.rs
- Latest development trunk.
- Adding /etc/logrotate.d/holland logrotate script.

* Wed Dec 09 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.9.6-1.rs
- Latest stable sources from upstream.

* Fri Dec 04 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.9.5dev-1.rs
- Removing mysqlcmds by default
- Adding lvm subpackage

* Thu Oct 08 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.9.4-1.1.rs
- BuildRequires: python-dev
- Rebuilding for Fedora Core

* Tue Sep 15 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.9.4-1.rs
- Latest sources.

* Mon Jul 13 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.9.3-1.rs
- Latest sources.

* Mon Jul 06 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.9.2-1.1.rs
- Rebuild

* Thu Jun 11 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.9.2-1.rs
- Latest sources from upstream.
- Only require epel for el4 (for now), and use PreReq rather than Requires.
- Require 'mysql' rather than 'mysqlclient'

* Wed Jun 03 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.9.1-1.rs
- Latest sources from upstream.
- Requires epel.

* Mon May 18 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.9.0-1.rs
- Latest from upstream
- Adding mysqlcmds package

* Tue May 05 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.4-1.2.rs
- Rebuild from trunk

* Sun May 03 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.4-1.1.rs
- Rebuild from trunk
- Adding commvault addon package.
- Removing Patch2: holland-0.3-config.patch
- Disable backupsets by default

* Sat May 02 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.3.1-1.2.rs
- Build as noarch.

* Wed Apr 29 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.3.1-1.rs
- Latest sources.

* Tue Apr 28 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.3-1.rs
- Latest sources.
- Removed tests for time being
- Added Patch2: holland-0.3-config.patch
- Sub package holland-mysqldump obsoletes holland-mysql = 1.0.  Resolves
  tracker [#1189].

* Fri Apr 17 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.2-2.rs
- Rebuild.

* Wed Mar 11 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.2-1.rs
- Latest sources from upstream.

* Fri Feb 20 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.1.1.rs
- Updated with subpackages/plugins

* Wed Jan 28 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.1-1.rs
- Initial spec build
