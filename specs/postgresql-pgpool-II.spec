%global short_name	pgpool-II
%if 0%{?rhel} && 0%{?rhel} <= 6
%global systemd_enabled 0
%else
%global systemd_enabled 1
%endif

%global _varrundir %{_rundir}/pgpool

Summary:		Pgpool is a connection pooling/replication server for PostgreSQL
Name:			postgresql-%{short_name}
Version:		4.5.1
Release:		5%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:		LicenseRef-Callaway-BSD

URL:			http://pgpool.net
Source0:		http://www.pgpool.net/mediawiki/images/%{short_name}-%{version}.tar.gz
Source1:		pgpool.service
Source2:		pgpool.sysconfig
Source3:		pgpool.init

# Stop building i686 architecture
ExcludeArch: %{ix86}

BuildRequires:		make
BuildRequires:		gcc
BuildRequires:		clang-devel llvm-devel
BuildRequires:		postgresql-server-devel
BuildRequires:		pam-devel, libmemcached-awesome-devel, openssl-devel
BuildRequires:		libxcrypt-devel

%if %{systemd_enabled}
BuildRequires:		systemd

# We require this to be present for %%{_prefix}/lib/tmpfiles.d
Requires:		systemd
Requires(post):		systemd-sysv
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%else
Requires(post):		chkconfig
Requires(preun):	chkconfig
# This is for /sbin/service
Requires(preun):	initscripts
Requires(postun):	initscripts
%endif
Provides:		postgresql-pgpool = 3.4.3
Obsoletes:		postgresql-pgpool <= 3.4.2

%description
pgpool-II is a inherited project of pgpool (to classify from
pgpool-II, it is sometimes called as pgpool-I). For those of
you not familiar with pgpool-I, it is a multi-functional
middle ware for PostgreSQL that features connection pooling,
replication and load balancing functions. pgpool-I allows a
user to connect at most two PostgreSQL servers for higher
availability or for higher search performance compared to a
single PostgreSQL server.

pgpool-II, on the other hand, allows multiple PostgreSQL
servers (DB nodes) to be connected, which enables queries
to be executed simultaneously on all servers. In other words,
it enables "parallel query" processing. Also, pgpool-II can
be started as pgpool-I by changing configuration parameters.
pgpool-II that is executed in pgpool-I mode enables multiple
DB nodes to be connected, which was not possible in pgpool-I.

%package devel
Summary:	The development files for pgpool-II
Requires:	%{name}%{?_isa} = %{version}-%{release}

# Stop building i686 architecture
ExcludeArch: %{ix86}

%description devel
Development headers and libraries for pgpool-II.

%package extensions
Summary:	Postgresql extensions for pgpool-II
Obsoletes:	postgresql-pgpool-II-recovery <= 3.3.4-1
Provides:	postgresql-pgpool-II-recovery = %{version}-%{release}
Requires:	postgresql-server
Requires:	%{name}%{?_isa} = %{version}-%{release}

# Stop building i686 architecture
ExcludeArch: %{ix86}

%description extensions
Postgresql extensions libraries and sql files for pgpool-II.

%prep
%setup -q -n %{short_name}-%{version}

%build
%configure \
	--with-pgsql-includedir=%{_includedir}/pgsql \
	--with-pgsql=%{_libdir}/pgsql \
	--disable-static \
	--with-pam \
	--with-openssl \
	--with-memcached=%{_includedir}/libmemcached \
	--sysconfdir=%{_sysconfdir}/%{short_name}/

# https://fedoraproject.org/wiki/Packaging:Guidelines#Removing_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# GCC 10 defaults to -fno-common which
# https://gcc.gnu.org/gcc-10/changes.html (see C section)
%make_build CFLAGS="%{optflags} -fcommon"
%make_build CFLAGS="%{optflags} -fcommon" -C src/sql/pgpool-recovery
%make_build CFLAGS="%{optflags} -fcommon" -C src/sql/pgpool-regclass

%install
%make_install
%make_install -C src/sql/pgpool-recovery
%make_install -C src/sql/pgpool-regclass

install -d %{buildroot}%{_datadir}/%{short_name}
install -d %{buildroot}%{_sysconfdir}/%{short_name}
mv %{buildroot}/%{_sysconfdir}/%{short_name}/pcp.conf.sample %{buildroot}%{_sysconfdir}/%{short_name}/pcp.conf
mv %{buildroot}/%{_sysconfdir}/%{short_name}/pgpool.conf.sample %{buildroot}%{_sysconfdir}/%{short_name}/pgpool.conf
mv %{buildroot}/%{_sysconfdir}/%{short_name}/pool_hba.conf.sample %{buildroot}%{_sysconfdir}/%{short_name}/pool_hba.conf
mv %{buildroot}/%{_sysconfdir}/%{short_name}/failover.sh.sample %{buildroot}%{_sysconfdir}/%{short_name}/failover.sh
mv %{buildroot}/%{_sysconfdir}/%{short_name}/pgpool_remote_start.sample %{buildroot}%{_sysconfdir}/%{short_name}/pgpool_remote_start
mv %{buildroot}/%{_sysconfdir}/%{short_name}/recovery_1st_stage.sample %{buildroot}%{_sysconfdir}/%{short_name}/recovery_1st_stage

%if %{systemd_enabled}
install -d %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/pgpool.service

# ... and make a tmpfiles script to recreate it at reboot.
mkdir -p $RPM_BUILD_ROOT%{_tmpfilesdir}
cat > $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf <<EOF
d %{_varrundir} 0755 root root -
EOF

%else
install -d %{buildroot}%{_sysconfdir}/init.d
install -m 755 %{SOURCE3} %{buildroot}%{_sysconfdir}/init.d/pgpool
%endif

install -d %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/pgpool

# nuke libtool archive and static lib
rm -f %{buildroot}%{_libdir}/libpcp.{a,la}

%post
/sbin/ldconfig
%if %{systemd_enabled}
%systemd_post pgpool.service
%else
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add pgpool
%endif
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%if %{systemd_enabled}
%systemd_preun pgpool.service
%else
if [ $1 -eq 0 ] ; then
    /sbin/service pgpool stop >/dev/null 2>&1
    /sbin/chkconfig --del pgpool
fi
%endif

%postun 
/sbin/ldconfig
%if %{systemd_enabled}
%systemd_postun_with_restart pgpool.service
%else
if [ $1 -ge 1 ] ; then
    /sbin/service pgpool condrestart >/dev/null 2>&1 || :
fi
%endif

%if %{systemd_enabled}
%triggerun -- pgpool < 3.1-1
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply pgpool
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save pgpool >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del pgpool >/dev/null 2>&1 || :
/bin/systemctl try-restart pgpool.service >/dev/null 2>&1 || :
%endif

%files
%doc README TODO COPYING AUTHORS ChangeLog NEWS
%{_bindir}/pg_enc
%{_bindir}/pgpool
%{_bindir}/pgpool_setup
%{_bindir}/pgproto
%{_bindir}/watchdog_setup
%{_bindir}/pcp_attach_node
%{_bindir}/pcp_detach_node
%{_bindir}/pcp_node_count
%{_bindir}/pcp_node_info
%{_bindir}/pcp_pool_status
%{_bindir}/pcp_proc_count
%{_bindir}/pcp_proc_info
%{_bindir}/pcp_promote_node
%{_bindir}/pcp_recovery_node
%{_bindir}/pcp_stop_pgpool
%{_bindir}/pcp_watchdog_info
%{_bindir}/pcp_health_check_stats
%{_bindir}/pcp_reload_config
%{_bindir}/wd_cli
%{_bindir}/pg_md5
%dir %{_datadir}/%{short_name}
%{_datadir}/%{short_name}/insert_lock.sql
%{_libdir}/libpcp.so.*
%{_datadir}/%{short_name}/pgpool.pam
%if %{systemd_enabled}
%ghost %{_varrundir}
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/pgpool.service
%else
%{_sysconfdir}/init.d/pgpool
%endif
%dir %{_sysconfdir}/%{short_name}
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{short_name}/*
%config(noreplace) %{_sysconfdir}/sysconfig/pgpool

%files devel
%{_includedir}/libpcp_ext.h
%{_includedir}/pcp.h
%{_includedir}/pool_process_reporting.h
%{_includedir}/pool_type.h
%{_libdir}/libpcp.so

%files extensions
%{_libdir}/pgsql/pgpool-recovery.so
%{_datadir}/pgsql/extension/pgpool-recovery.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.1.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.2.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.3.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.4.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.1--1.2.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.2--1.3.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.3--1.4.sql
%{_datadir}/pgsql/extension/pgpool_recovery.control
%{_datadir}/pgsql/extension/pgpool-regclass.sql
%{_datadir}/pgsql/extension/pgpool_regclass--1.0.sql
%{_datadir}/pgsql/extension/pgpool_regclass.control
# From PostgreSQL 9.4 pgpool-regclass.so is not needed anymore
# because 9.4 or later has to_regclass.
%{_libdir}/pgsql/pgpool-regclass.so


%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 4.5.1-5
- Add explicit BR: libxcrypt-devel

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.5.1-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Ondrej Sloup <osloup@redhat.com> - 4.5.1-1
- Rebase to the latest upstream version (rhbz#2266774)

* Tue Jan 30 2024 Ondrej Sloup <osloup@redhat.com> - 4.5.0-3
- Stop building i686 permanently
- https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval

* Fri Jan 26 2024 Ondrej Sloup <osloup@redhat.com> - 4.5.0-2
- Temporarily stop building i686

* Fri Jan 26 2024 Ondrej Sloup <osloup@redhat.com> - 4.5.0-1
- Rebase to the latest upstream version (rhbz#2252211)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 05 2023 Filip Janus <fjanus@redhat.com> - 4.4.5-1
- Update to 4.4.5

* Tue Dec 05 2023 Filip Janus <fjanus@redhat.com> - 4.4.4-2
- Rebuild for demodularized version of postgresql
- remove postgresq-_module_compat since it is not working with demodularized packages

* Tue Aug 22 2023 Ondrej Sloup <osloup@redhat.com> -  4.4.4-1
- Rebase to the latest upstream version (rhbz#2232454)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 02 2023 Ondrej Sloup <osloup@redhat.com> -  4.4.3-1
- Rebase to the latest upstream version (rhbz#2208166)

* Fri Jan 27 2023 Ondrej Sloup <osloup@redhat.com> - 4.4.2-1
- Rebase to the latest upstream version (rhbz#2163118)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 23 2022 Ondrej Sloup <osloup@redhat.com> - 4.4.1-1
- Rebase to the latest upstream version (rhbz#2155852)

* Tue Dec 06 2022 Ondrej Sloup <osloup@redhat.com> - 4.4.0-1
- Rebase to the latest upstream version (rhbz#1930321)

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 4.3.3-2
- Rebuild for new PostgreSQL 15

* Tue Aug 23 2022 Ondrej Sloup <osloup@redhat.com> - 4.3.3-1
- Rebase to the latest upstream version (rhbz#2119261ZZ)

* Thu Jun 30 2022 Ondrej Sloup <osloup@redhat.com> - 4.3.2-2
- Fix the legacy directory /var/run/ (rhbz#2102041)

* Thu May 19 2022 Ondrej Sloup <osloup@redhat.com> - 4.3.2-1
- Rebase to the latest upstream version (rhbz#2088219)

* Thu May 05 2022 Ondrej Sloup <osloup@redhat.com> - 4.3.1-1
- Fix mixed spaces and tabs
- Remove config files as they were unified
- Fix chronology of changelog made by Mass_Rebuild
- Add pgpool_recovery 1.4 and 1.3-1.4
- Rebase to the latest upstream version (rhbz#1870431)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Filip Januš <fjanus@redhat.com> - 4.2.0-6
- Rebuild for Postgresql 14

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.2.0-5
- Rebuilt with OpenSSL 3.0.0

* Tue Jul 27 2021 Filip Januš <fjanus@redhat.com> - 4.2.0-4
- Remove libpq-devel requirement, it conflicts with postgresql-server-devel
  dependencies

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.0-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 13 2021 Patrik Novotný <panovotn@redhat.com> - 4.2.0-1
- Rebase to upstream release 4.2.0

* Tue Jan 12 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-3
- This record was edited on May 06 2022, to change the date from Jan 27 to Jan 12 to preserve chronology
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Ondrej Dubaj <odubaj@redhat.com> - 4.1.2-1
- Rebase to upstream release version 4.1.2

* Sun Mar 08 2020 Patrik Novotný <panovotn@redhat.com> - 4.1.1-1
- Rebase to upstream release version 4.1.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Petr Kubat <pkubat@redhat.com> - 4.0.3-2
- Fix build failure due to missing tmpfiles_create arguments

* Thu Feb 21 2019 Jozef Mlich <imlich@fit.vutbr.cz> - 4.0.3-1
- update to the latest version, per release notes:
  http://www.pgpool.net/docs/latest/en/html/release-4-0-3.html

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pavel Raiskup <praiskup@redhat.com> - 4.0.2-1
- update to the latest version, per release notes:
  http://www.pgpool.net/docs/latest/en/html/release-4-0-2.html
  http://www.pgpool.net/docs/latest/en/html/release-3-7-5.html

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 3.7.4-5
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Oct 18 2018 Petr Kubat <pkubat@redhat.com> - 3.7.5-4
- rebuild for PostgreSQL 11

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 3.7.4-3
- rebuild against postgresql-server-devel (rhbz#1618698)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jozef Mlich <imlich@fit.vutbr.cz> - 3.7.4-1
- update to 3.7.4, per release notes:
  http://www.pgpool.net/docs/latest/en/html/release-3-7-4.html

* Tue Apr 17 2018 Jozef Mlich <imlich@fit.vutbr.cz> - 3.7.3-1
- update to 3.7.3, per release notes:
  http://www.pgpool.net/docs/latest/en/html/release-3-7-3.html

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.7.1-2
- Rebuilt for switch to libxcrypt

* Tue Jan 09 2018 Jozef Mlich <imlich@fit.vutbr.cz> - 3.7.1-1
- update to 3.7.1, per release notes:
  http://www.pgpool.net/docs/latest/en/html/release-3-7-1.html

* Wed Nov 22 2017 Jozef Mlich <imlich@fit.vutbr.cz> - 3.7.0-1
- update to 3.7.0, per release notes:
  http://www.pgpool.net/docs/latest/en/html/release-3-7.html

* Wed Nov 08 2017 Pavel Raiskup <praiskup@redhat.com> - 3.6.7-1
- update to 3.6.7, per release notes:
  http://www.pgpool.net/docs/latest/en/html/release-3-6-7.html

* Tue Oct 10 2017 Pavel Raiskup <praiskup@redhat.com> - 3.6.5-4
- rebuild for PostgreSQL 10

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Jozef Mlich <imlich@fit.vutbr.cz> - 3.6.5-1
- rebuild for pgpool 3.6.5
  see http://www.pgpool.net/docs/pgpool-II-3.6.5/doc/en/html/release-3-6-5.html

* Thu May 11 2017 Jozef Mlich <imlich@fit.vutbr.cz> - 3.6.4-1
- rebuild for pgpool 3.6.4

* Fri Apr 28 2017 Jozef Mlich <imlich@fit.vutbr.cz> - 3.6.3-1
- rebuild for pgpool 3.6.3

* Fri Mar 17 2017 Jozef Mlich <imlich@fit.vutbr.cz> - 3.6.2-1
- rebuild for pgpool 3.6.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 3.6.1-1
- rebuild for pgpool 3.6.1

* Mon Nov 21 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 3.6.0-1
- rebuild for pgpool 3.6.0
  Improve the behavior of fail-over.
  New PGPOOL SET command has been introduced.
  Watchdog is significantly enhanced.
  Handling of extended query protocol (e.g. used by Java applications) in streaming replication mode speeds up if many rows are returned in a result set.
  Import parser of PostgreSQL 9.6.
  In some cases pg_terminate_backend() now does not trigger a fail-over.
  Change documentation format from raw HTML to SGML.

* Mon Oct 10 2016 Pavel Raiskup <praiskup@redhat.com> - 3.5.4-3
- bump: build in rawhide done too early

* Mon Oct 10 2016 Petr Kubat <pkubat@redhat.com> - 3.5.4-2
- Rebuild for PostgreSQL 9.6.0

* Wed Aug 31 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 3.5.4-1
- rebuild for pgpool 3.5.4
  see http://www.pgpool.net/docs/pgpool-II-3.5.4/NEWS.txt

* Fri Jun 17 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 3.5.3-1
- rebuild for pgpool 3.5.3
  see http://www.pgpool.net/docs/pgpool-II-3.5.3/NEWS.txt

* Tue Apr 26 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 3.5.2-1
- rebuld for pgpool 3.5.2
  see http://www.pgpool.net/docs/pgpool-II-3.5.2/NEWS.txt

* Mon Apr 04 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 3.5.1-1
- rebuld for pgool 3.5.1
  see http://www.pgpool.net/docs/pgpool-II-3.5.1/NEWS.txt

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 3.5.0-1
- rebuld for pgool 3.5.0
  See http://pgpool.net/mediawiki/index.php?title=pgpool-II_3.5_features&redirect=no

* Fri Jan 08 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 3.4.3-3
- rebuild for PostgreSQL 9.5

* Mon Jul 27 2015 Jozef MLich <imlich@fit.vutbr.cz> - 3.4.3-2
- Add memcached support
- Add OpenSSL support
- remove white spaces on end of lines in spec file

* Fri Jul 24 2015 Jozef Mlich <imlich@fit.vutbr.cz> - 3.4.3-1
- Update to 3.4.3
  see http://www.pgpool.net/docs/pgpool-II-3.4.3/NEWS.txt

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Jozef Mlich <jmlich@redhat.com> - 3.4.2-1
- Update to 3.4.2
  see http://www.pgpool.net/docs/pgpool-II-3.4.2/NEWS.txt

* Thu Feb 5 2015 Devrim Gündüz <devrim@gunduz.org> - 3.4.1-1
- Update to 3.4.1

* Tue Jan 06 2015 Jozef Mlich <jmlich@redhat.com> - 3.4.0-6
- rebuild because of broken dependency
  requires postgresql-server(:MODULE_COMPAT_9.3)

* Mon Dec 15 2014 Jozef Mlich <jmlich@redhat.com> - 3.4.0-5
- incorrect permissions on init script.

* Thu Dec 11 2014 Jozef Mlich <jmlich@redhat.com> - 3.4.0-4
- incorrect epoch in obsoletes of recovery subpackage
- fixed some rpmlint warnings

* Wed Dec 10 2014 Pavel Raiskup <praiskup@redhat.com> - 3.4.0-3
- lint the spec file, remove RPATH (rhbz#1166534)

* Fri Nov 21 2014 Pavel Raiskup <praiskup@redhat.com> - 3.4.0-2
- remove redundant 'cd ../..' in sub-shell, cleanup comments, use %%_smp_mflags,
  use %%global

* Wed Nov 12 2014 Jozef Mlich <jmlich@redhat.com> - 3.4.0-1
- update to 3.4.0
  see http://www.pgpool.net/docs/pgpool-II-3.4.0/NEWS.txt
- recovery subpackage renamed to extensions
- added module compat for extensions

* Tue Sep 09 2014 Jozef Mlich <jmlich@redhat.com> - 3.3.4-1
- update to 3.3.4
  see http://www.pgpool.net/docs/pgpool-II-3.3.4/NEWS.txt

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Pavel Raiskup <praiskup@redhat.com> - 3.3.3-2
- create %%_varrundir after installation, specify it on one place,

* Thu Jun 12 2014 Jozef Mlich <jmlich@redhat.com> - 3.3.3-1
- adding tmpfiles.d (allow pid file to be created in /var/run/pgpool - dir
  created after reboot)
- Rebase to pgpool-II 3.3.3 (#1094713)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Pavel Raiskup <praiskup@redhat.com> - 3.2.0-4
- Rebuilt against PostgreSQL 9.3 (#1007855)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 19 2012 Tom Callaway <spot@fedoraproject.org> - 3.2.0-1
- update to 3.2.0
- add recovery subpackage (thanks to Dmitry S. Makovey)
- add rhel conditionalization (thanks to Dmitry S. Makovey)
- update systemd scriptlets

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Devrim GUNDUZ <devrim@gunduz.org> - 3.1.3-1
- Update to 3.1.3, per changes described at:
  http://www.pgpool.net/docs/pgpool-II-3.1.3/doc/NEWS.txt

* Tue Mar 27 2012 Devrim Gunduz <devrim@gunduz.org> - 3.1.2-1
- update to 3.1.2

* Tue Mar 27 2012 Devrim Gunduz <devrim@gunduz.org> - 3.1.2-1
- update to 3.1.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Tom Callaway <spot@fedoraproject.org> - 3.1-1
- update to 3.1
- convert to systemd

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 25 2009 Devrim GUNDUZ <devrim@gunduz.org> - 2.3.1-1
- Update to 2.3.1
- Adjust order of startup and kill, per RH bugzilla #545739.

* Tue Dec 1 2009 Devrim GUNDUZ <devrim@gunduz.org> - 2.2.6-1
- Update to 2.2.6

* Sun Nov 01 2009 Devrim GUNDUZ <devrim@gunduz.org> - 2.2.5-2
- Remove init script from all runlevels before uninstall. Per RH Bugzilla
  #532177

* Sun Oct 4 2009 Devrim Gunduz <devrim@CommandPrompt.com> 2.2.5-1
- Update to 2.2.5, for various fixes described at
  http://lists.pgfoundry.org/pipermail/pgpool-general/2009-October/002188.html

* Sat Oct 3  2009 Devrim Gunduz <devrim@CommandPrompt.com> 2.2.4-1
- Update to 2.2.4
- Re-apply a fix for #442372

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 7 2009 Devrim Gunduz <devrim@CommandPrompt.com> 2.2.2-1
- Update to 2.2.2

* Mon Mar 23 2009 Devrim Gunduz <devrim@CommandPrompt.com> 2.2-1.1
- Fix pid file path in init script.
- Fix spec file -- we don't use short_name macro in pgcore spec file.
- Create pgpool pid file directory.
- Fix stop/start routines, also improve init script a bit.
- Install conf files to a new directory (/etc/pgpool-II), and get rid
  of sample conf files.

* Sun Mar 1 2009 Devrim Gunduz <devrim@CommandPrompt.com> 2.2-1
- Update to 2.2
- Update URL

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> 2.1-2
- Include /usr/share/pgpool-II directory.

* Tue Aug 12 2008 Devrim Gunduz <devrim@CommandPrompt.com> 2.1-1
- Update to 2.1 Gold
- Set group of sample config files to root, not apache. Fixes RH #442372.
- Update patch #1: Fix build failure caused by new default patch
fuzz = 0 policy in rawhide

* Fri Apr 11 2008 Devrim Gunduz <devrim@CommandPrompt.com> 2.1-0.2.beta2
- Fix Requires: issue, per #442021 (Alex Lancaster)

* Sun Apr 6 2008 Devrim Gunduz <devrim@CommandPrompt.com> 2.1-beta2
- Update to 2.1 beta2

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.1-3.1
- Autorebuild for GCC 4.3

* Mon Jan 21 2008 Devrim GUNDUZ <devrim@commandprompt.com> 2.0.1-2.1
- Rebuilt against PostgreSQL 8.3

* Sat Jan 19 2008 Devrim Gunduz <devrim@CommandPrompt.com> 2.0.1-2
- Fix Requires of -devel package, per bz#429436

* Sun Jan 13 2008 Devrim Gunduz <devrim@CommandPrompt.com> 2.0.1-1
- Update to 2.0.1
- Add a temp patch that will disappear in 2.0.2

* Tue Oct 23 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.3-1
- Update to 1.3

* Fri Oct 5 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.2.1-1
- Update to 1.2.1

* Wed Aug 29 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.2-5
- Chmod sysconfig/pgpool to 644, not 755. Per BZ review.
- Run chkconfig --add pgpool during %%post.

* Thu Aug 16 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.2-4
- Fixed the directory name where sample conf files and sql files 
  are installed.

* Sun Aug 5 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.2-3
- Added a patch for sample conf file to use Fedora defaults

* Sun Aug 5 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.2-2
- Added an init script for pgpool
- Added /etc/sysconfig/pgpool

* Wed Aug 1 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.2-1
- Update to 1.2

* Fri Jun 15 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.1.1-1
- Update to 1.1.1

* Sat Jun 2 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.1-1
- Update to 1.1
- added --disable-rpath configure parameter.
- Chowned sample conf files, so that they can work with pgpoolAdmin.

* Sun Apr 22 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.0.2-4
- Added postgresql-devel as BR, per bugzilla review.
- Added --disable-static flan, per bugzilla review.
- Removed superfluous manual file installs, per bugzilla review.

* Sun Apr 22 2007 Devrim Gunduz <devrim@CommandPrompt.com> 1.0.2-3
- Rebuilt for the correct tarball
- Fixed man8 file ownership, per bugzilla review #229321 

* Tue Feb 20 2007 Jarod Wilson <jwilson@redhat.com> 1.0.2-2
- Create proper devel package, drop -libs package
- Nuke rpath
- Don't install libtool archive and static lib
- Clean up %%configure line
- Use proper %%_smp_mflags
- Install config files properly, without .sample on the end
- Preserve timestamps on header files

* Tue Feb 20 2007 Devrim Gunduz <devrim@commandprompt.com> 1.0.2-1
- Update to 1.0.2-1

* Mon Oct 02 2006 Devrim Gunduz <devrim@commandprompt.com> 1.0.1-5
- Rebuilt

* Mon Oct 02 2006 Devrim Gunduz <devrim@commandprompt.com> 1.0.1-4
- Added -libs and RPM
- Fix .so link problem
- Cosmetic changes to spec file

* Wed Sep 27 2006 - Devrim GUNDUZ <devrim@commandprompt.com> 1.0.1-3
- Fix spec, per Yoshiyuki Asaba

* Tue Sep 26 2006 - Devrim GUNDUZ <devrim@commandprompt.com> 1.0.1-2
- Fixed rpmlint errors
- Fixed download url
- Added ldconfig for .so files

* Thu Sep 21 2006 - David Fetter <david@fetter.org> 1.0.1-1
- Initial build pgpool-II 1.0.1 for PgPool Global Development Group

