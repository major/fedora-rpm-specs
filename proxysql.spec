Summary:       A high-performance MySQL proxy
Name:          proxysql
Version:       2.4.8
Release:       3%{?dist}
# Proxysql Google group for free community support: https://groups.google.com/g/proxysql
URL:           https://proxysql.com/
# GPL-3.0-or-later
# deps/jemalloc: BSD-2-Clause
# deps/mariadb-connector-c: LGPL-2.1-or-later
# deps/prometheus-cpp: MIT
# deps/re2: BSD-3-Clause
License:       GPL-3.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND BSD-2-Clause AND MIT

BuildRequires: make, automake
BuildRequires: cmake, gcc-c++
BuildRequires: systemd-rpm-macros

# Required by proxysql code
BuildRequires: libtool
BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: libev-devel
BuildRequires: sqlite-devel
BuildRequires: openssl-devel
BuildRequires: libcurl-devel
BuildRequires: libdaemon-devel
BuildRequires: libconfig-devel
BuildRequires: lz4-devel
BuildRequires: libuuid-devel

# Used by provided (scripts) tools
BuildRequires: perl
BuildRequires: python3

# Specific dependency for Fedora/RHEL/Centos
BuildRequires: gnutls-devel

Suggests: mariadb, community-mysql

# Build in other architectures aside from x86 is not yet supported due to some
# use of assembly code, but is on the upstream roadmap to support them.
# https://github.com/sysown/proxysql/issues/977

# Update 8/2021
# Support for arm64 has been added.
ExcludeArch:   %{power64} s390x

Provides:      bundled(jemalloc) = 5.2.0
Provides:      bundled(mariadb-connector-c) = 3.1.9
Provides:      bundled(re2) = 20200706
Provides:      bundled(clickhouse-cpp) = 2.1.0
Provides:      bundled(prometheus-cpp) = 0.9.0
Provides:      bundled(cityhash) = 1.1.1
Provides:      bundled(libhttpserver) = 0.18.1
Provides:      bundled(libmicrohttpd) = 0.9.68

# There is inconsistency between name and URL of file and main unpacked source folder
Source0:       https://github.com/sysown/proxysql/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Manpage for binary is missing. Instead we provide it manually.
# Link for tracking current status in upstream:
# https://github.com/sysown/proxysql/issues/3564
Source1:       proxysql.1

# The upstream code bundles multiple libraries: libconfig, libdaemon, sqlite3, re2,
# mariadb-connector-c, pcre, clickhouse-cpp, prometheus-cpp, lz4, cityhash, microhttpd, curl
# ev, coredumper, libssl and jemalloc.
# This patch de-bundles 8 of these libraries: libconfig, libdaemon and sqlite3,
# libsl, pcre, curl, lz4, ev
# The remaining libraries are not de-bundled due to different reasons (mainly
# being patched, more info here: https://bugzilla.redhat.com/show_bug.cgi?id=1457929).
# Other remaining libraries are not maintained in Fedora (clickhouse-cpp,
# cityhash, prometheus-cpp)

Patch0001: 0001-Unbundle-system-deps.patch
Patch0002: 0002-Enable-tcp_fastopen-in-bundled-libhttpserver.patch
Patch0003: 0003-Simplify-proxysql.service.patch

%description
ProxySQL is a high performance, high availability, protocol aware proxy for
MySQL and forks (like Percona Server and MariaDB).

%prep
%autosetup -p1
# Remove sources of debundled libraries
rm -r deps/{libssl,pcre,curl,lz4,libev,libconfig,libdaemon,sqlite3}

%build
export GIT_VERSION=%{version}
%global _configure :
%configure help
export CPPFLAGS=$CXXFLAGS
%make_build

%install
install -p -D -m 0755 src/proxysql %{buildroot}%{_bindir}/proxysql
install -p -D -m 0640 etc/proxysql.cnf %{buildroot}%{_sysconfdir}/proxysql.cnf
install -p -D -m 0755 tools/proxysql_galera_checker.sh %{buildroot}%{_datadir}/%{name}/tools/proxysql_galera_checker.sh
install -p -D -m 0755 tools/proxysql_galera_writer.pl %{buildroot}%{_datadir}/%{name}/tools/proxysql_galera_writer.pl
install -p -D -m 0644 systemd/system/proxysql.service %{buildroot}%{_unitdir}/proxysql.service
install -p -D -m 0644 systemd/system/proxysql-initial.service %{buildroot}%{_unitdir}/proxysql-initial.service
install -p -D -m 0644 README.md %{buildroot}%{_docdir}/proxysql/README.md
install -p -D -m 0644 RUNNING.md %{buildroot}%{_docdir}/proxysql/RUNNING.md
install -p -D -m 0644 FAQ.md %{buildroot}%{_docdir}/proxysql/FAQ.md
install -p -D -m 0644 doc/release_notes/*.md -t %{buildroot}%{_docdir}/proxysql
install -p -D -m 0644 doc/internal/*.txt -t %{buildroot}%{_docdir}/proxysql
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1
install -d -m 0755 %{buildroot}%{_sharedstatedir}/proxysql

%pre
/usr/sbin/groupadd -r proxysql >/dev/null 2>&1 || :
/usr/sbin/useradd  -g proxysql -r -d /var/lib/proxysql -s /sbin/nologin \
    -c "ProxySQL" proxysql >/dev/null 2>&1 || :

%post
%systemd_post proxysql.service

%preun
%systemd_preun proxysql.service

%postun
%systemd_postun_with_restart proxysql.service

%files
%license LICENSE
%{_bindir}/proxysql
%{_unitdir}/proxysql.service
%{_unitdir}/proxysql-initial.service
%{_datadir}/proxysql/
%{_docdir}/proxysql/
%{_mandir}/man1/proxysql.1*
%attr(-,proxysql,proxysql) %{_sharedstatedir}/proxysql/
%attr(-,proxysql,root) %config(noreplace) %{_sysconfdir}/proxysql.cnf

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Igor Raits <igor@gooddata.com> - 2.4.8-1
- Update to 2.4.8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Igor Raits <igor@gooddata.com> - 2.4.4-1
- Update to 2.4.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 14 2022 Marek Kulik <mkulik@redhat.com> - 2.3.2-4
- Fix FTBFS for gcc12 (Resolves: #2053629)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 24 2021 Marek Kulik <mkulik@redhat.com> - 2.3.2-1
- Updated to ProxySQL 2.3.2

* Mon Sep 20 2021 Marek Kulik <mkulik@redhat.com> - 2.3.1-1
- Updated to ProxySQL 2.3.1

* Wed Sep 15 2021 Marek Kulik <mkulik@redhat.com> - 2.3.0-1
- Updated to ProxySQL 2.3.0

* Wed Sep 15 2021 Marek Kulik <mkulik@redhat.com> - 2.2.2-1
- Updated to ProxySQL 2.2.2

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.2.1-2
- Rebuilt with OpenSSL 3.0.0

* Mon Sep 06 2021 Marek Kulik <mkulik@redhat.com> - 2.2.1-1
- Updated to ProxySQL 2.2.1

* Tue Aug 10 2021 Marek Kulik <mkulik@redhat.com> - 2.2.0-1
- Updated to ProxySQL 2.2.0
- Add new bundled library (prometheus-cpp) - new dependencies
- Fix gcc compatibility - missing headers
- Rework Patch1 - move execution to patch macro
- Add arm rpm builds

* Mon Aug 09 2021 Marek Kulik <mkulik@redhat.com> - 2.0.13-7
- Fix FTBFS due to cmake syntax change

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 2.0.13-5
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.13-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Jeff Law <law@redhat.com> - 2.0.13-2
- Replace "swap" in mariadb library with my_swap to avoid conflict with C++
  standard headers

* Tue Aug 04 2020 Filip Januš <fjanus@redhat.com> - 2.0.13-1
- Rebase onto version 2.0.13
- Add new patch to port bundled libinjection to python 3
- Fix debundle patch, new bundled library (libhttpserver) - new dependencies
- Remove bundled google-coredumper

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Lukas Javorsky <ljavorsk@redhat.com> - 2.0.9-4
- Add mariadb and mysql client to suggests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Filip Januš <fjanus@redhat.com> - 2.0.9-2
- .service file path fix

* Tue Nov 19 2019 Filip Januš <fjanus@redhat.com> - 2.0.9-1
- Upstream released ProxySQL 2.0.9
- Patch0 was modified - lib/Makefile was modified

* Tue Oct 15 2019 Filip Januš <fjanus@redhat.com> - 2.0.8-1
- Upstream released ProxySQL 2.0.8

* Mon Sep 23 2019 Filip Januš <fjanus@redhat.com> - 2.0.7-1
- Updated to ProxySQL 2.0.7
- De-bundled new libraries (Update patch)
- Fix path to doc
- Fix man page path (bug #1722350)

* Thu Sep 12 2019 Petr Pisar <ppisar@redhat.com> - 1.3.7-11
- Build-require zlib-devel (bug #1727136)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 1.3.7-8
- Rebuild for new libconfig

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Augusto Caringi <acaringi@redhat.com> 1.3.7-5
- Made install commands in install section compatible with epel7

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017  Augusto Caringi <acaringi@redhat.com> 1.3.7-2
- Fixed build flags through exporting CPPFLAGS variable
- Remove unused bundled libraries
- Fixed configuration file ownership
- Replaced default login shell of proxysql user from /bin/false to /sbin/nologin

* Wed Jun 14 2017  Augusto Caringi <acaringi@redhat.com> 1.3.7-1
- Updated to ProxySQL 1.3.7
- De-bundled some libraries
- Added man page
- Updated license field
- Adopted proxysql user/group
- Improvements in spec file

* Tue May 16 2017  Augusto Caringi <acaringi@redhat.com> 1.3.6-1
- Initial build
