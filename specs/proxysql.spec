Summary:       A high-performance MySQL proxy
Name:          proxysql
Version:       2.7.2
Release:       %autorelease
# Proxysql Google group for free community support: https://groups.google.com/g/proxysql
URL:           https://proxysql.com/
# GPL-3.0-or-later
# deps/coredumper: BSD-3-Clause
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
ExcludeArch:   %{power64} s390x %{ix86}

Provides:      bundled(jemalloc) = 5.2.0
Provides:      bundled(mariadb-connector-c) = 3.3.8
Provides:      bundled(re2) = 20221201
Provides:      bundled(clickhouse-cpp) = 2.3.0
Provides:      bundled(prometheus-cpp) = 1.1.0
# The hash looks weird but it is still 1.1.1
Provides:      bundled(cityhash) = 1.1.1
Provides:      bundled(libhttpserver) = 0.18.2
Provides:      bundled(libmicrohttpd) = 0.9.77
Provides:      bundled(coredumper) = 0^cb6cead

# There is inconsistency between name and URL of file and main unpacked source folder
Source0:       https://github.com/sysown/proxysql/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Manpage for binary is missing. Instead we provide it manually.
# Link for tracking current status in upstream:
# https://github.com/sysown/proxysql/issues/3564
Source1:       proxysql.1

Source2:       0007-Fix-gcc-15.patch

%description
ProxySQL is a high performance, high availability, protocol aware proxy for
MySQL and forks (like Percona Server and MariaDB).

# The upstream code bundles multiple libraries: libconfig, libdaemon, sqlite3, re2,
# mariadb-connector-c, pcre, clickhouse-cpp, prometheus-cpp, lz4, cityhash, microhttpd, curl
# ev, coredumper, libssl and jemalloc.
# This patch de-bundles 8 of these libraries: libconfig, libdaemon and sqlite3,
# libsl, pcre, curl, lz4, ev
# The remaining libraries are not de-bundled due to different reasons (mainly
# being patched, more info here: https://bugzilla.redhat.com/show_bug.cgi?id=1457929).
# Other remaining libraries are not maintained in Fedora (clickhouse-cpp,
# cityhash, prometheus-cpp)
#
# NOTE: libdaemon contains custom patch (since https://github.com/sysown/proxysql/pull/4291)
#       but I don't believe it is worth to bundle it just because of that.
%patchlist
0001-Unbundle-libconfig-libdaemon-sqlite3-pcre-lz3-curl-e.patch
0002-Enable-tcp_fastopen-in-bundled-libhttpserver.patch
0003-Simplify-systemd-services.patch
0004-Apply-fPIC-properly-in-re2-build.patch
0005-Fix-clickhouse-cpp-build-on-i686-aarch64.patch
0006-Fix-coredumper-build.patch

%prep
%autosetup -p1
# Remove sources of debundled libraries
rm -r deps/{libssl,pcre,curl,lz4,libev,libconfig,libdaemon,sqlite3}

# Create a sysusers.d config file
cat >proxysql.sysusers.conf <<EOF
u proxysql - 'ProxySQL' /var/lib/proxysql -
EOF

# Patch 0007
mv %{SOURCE2} deps/mariadb-client-library/ma_global.h.patch

%build
export GIT_VERSION=%{version}
%global _configure :
%configure help
CXXFLAGS="$CXXFLAGS -Wno-error=cpp -Wno-error=template-body"
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

install -m0644 -D proxysql.sysusers.conf %{buildroot}%{_sysusersdir}/proxysql.conf


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
%{_sysusersdir}/proxysql.conf

%changelog
%autochangelog
