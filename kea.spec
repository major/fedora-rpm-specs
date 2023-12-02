%global sysrepo 0

#%%global prever P1

Name:           kea
Version:        2.4.1
Release:        %autorelease
Summary:        DHCPv4, DHCPv6 and DDNS server from ISC

License:        MPL-2.0 AND BSL-1.0
URL:            http://kea.isc.org
Source0:        https://downloads.isc.org/isc/kea/%{version}%{?prever:-%{prever}}/kea-%{version}%{?prever:-%{prever}}.tar.gz
Source1:        https://downloads.isc.org/isc/kea/%{version}%{?prever:-%{prever}}/kea-%{version}%{?prever:-%{prever}}.tar.gz.asc
# Obtained from https://www.isc.org/pgpkey/
Source2:        isc-keyblock.asc
Source3:        kea-dhcp4.service
Source4:        kea-dhcp6.service
Source5:        kea-dhcp-ddns.service
Source6:        kea-ctrl-agent.service
Source7:        kea-tmpfiles.d.conf

Patch1:         kea-openssl-version.patch

# autoreconf
BuildRequires: autoconf automake libtool
BuildRequires: boost-devel
BuildRequires: gcc-c++
# %%configure --with-openssl
BuildRequires: openssl-devel
# %%configure --with-dhcp-mysql
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: mariadb-connector-c-devel
# TODO: propose upstream fix so this is not needed (no server-side related
# headers nor configuration should be needed)
BuildRequires: postgresql-server-devel
%else
# %%configure --with-dhcp-mysql
BuildRequires: mariadb-devel
# %%configure --with-dhcp-pgsql
BuildRequires: postgresql-devel
%endif
BuildRequires: log4cplus-devel
%if %{sysrepo}
# %%configure --with-sysrepo
BuildRequires: sysrepo-devel
%endif

%ifnarch s390 %{mips}
BuildRequires: valgrind-devel
%endif
# src/lib/testutils/dhcp_test_lib.sh
BuildRequires: procps-ng
# %%configure --enable-generate-parser
BuildRequires: bison
BuildRequires: flex
# %%configure --enable-shell
BuildRequires: python3-devel
# in case you ever wanted to use %%configure --enable-generate-docs
#BuildRequires: elinks asciidoc plantuml
BuildRequires: systemd
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: make
BuildRequires: gnupg2

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
DHCP implementation from Internet Systems Consortium, Inc. that features fully
functional DHCPv4, DHCPv6 and Dynamic DNS servers.
Both DHCP servers fully support server discovery, address assignment, renewal,
rebinding and release. The DHCPv6 server supports prefix delegation. Both
servers support DNS Update mechanism, using stand-alone DDNS daemon.


%package doc
Summary: Documentation for Kea DHCP server
BuildArch: noarch

%description doc
Documentation and example configuration for Kea DHCP server.


%package devel
Summary: Development headers and libraries for Kea DHCP server
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# to build hooks (#1335900)
Requires: boost-devel
Requires: openssl-devel
Requires: pkgconfig

%description devel
Header files and API documentation.


%package hooks
Summary: Hooks libraries for kea
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description hooks
Hooking mechanism allow Kea to load one or more dynamically-linked libraries
(known as "hooks libraries") and, at various points in its processing
("hook points"), call functions in them.  Those functions perform whatever
custom processing is required.


%package libs
Summary: Shared libraries used by Kea DHCP server

%description libs
This package contains shared libraries used by Kea DHCP server.


%prep
%if 0%{?fedora} || 0%{?rhel} > 8
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%endif
rm -rf doc/sphinx/_build
%autosetup -p1 -n kea-%{version}%{?prever:-%{prever}}

# to be able to build on ppc64(le)
# https://sourceforge.net/p/flex/bugs/197
# https://lists.isc.org/pipermail/kea-dev/2016-January/000599.html
sed -i -e 's|ECHO|YYECHO|g' src/lib/eval/lexer.cc


%build
autoreconf --verbose --force --install

%configure \
    --disable-dependency-tracking \
    --disable-rpath \
    --disable-silent-rules \
    --disable-static \
    --enable-debug \
    --enable-generate-parser \
    --enable-shell \
    --enable-generate-docs \
    --enable-generate-messages \
    --enable-perfdhcp \
    --with-mysql \
    --with-pgsql \
    --with-gnu-ld \
    --with-log4cplus \
%if %{sysrepo}
    --with-sysrepo \
%endif
    --with-openssl

%make_build


%install
%make_install docdir=%{_pkgdocdir}

# Get rid of .la files
find %{buildroot} -type f -name "*.la" -delete -print

# Install systemd units
install -Dpm 0644 %{S:3} %{buildroot}%{_unitdir}/kea-dhcp4.service
install -Dpm 0644 %{S:4} %{buildroot}%{_unitdir}/kea-dhcp6.service
install -Dpm 0644 %{S:5} %{buildroot}%{_unitdir}/kea-dhcp-ddns.service
install -Dpm 0644 %{S:6} %{buildroot}%{_unitdir}/kea-ctrl-agent.service

# Start empty lease databases
mkdir -p %{buildroot}%{_sharedstatedir}/kea/
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases4.csv
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases6.csv

rm -f %{buildroot}%{_pkgdocdir}/COPYING
rm -f %{buildroot}%{_pkgdocdir}/html/.buildinfo

mkdir -p %{buildroot}/run
install -dm 0755 %{buildroot}/run/kea/

install -Dpm 0644 %{S:7} %{buildroot}%{_tmpfilesdir}/kea.conf


%post
%systemd_post kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%preun
%systemd_preun kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%postun
%systemd_postun_with_restart kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service


%ldconfig_scriptlets libs


%files
%license COPYING
%{_bindir}/kea-msg-compiler
%{_sbindir}/kea-admin
%{_sbindir}/kea-ctrl-agent
%{_sbindir}/kea-dhcp-ddns
%{_sbindir}/kea-dhcp4
%{_sbindir}/kea-dhcp6
%{_sbindir}/kea-lfc
%{_sbindir}/kea-shell
%{_sbindir}/keactrl
%{_sbindir}/perfdhcp
%{_unitdir}/kea*.service
%dir %{_sysconfdir}/kea/
%config(noreplace) %{_sysconfdir}/kea/kea*.conf
%{_datarootdir}/kea
%dir %{_sharedstatedir}/kea
%config(noreplace) %{_sharedstatedir}/kea/kea-leases*.csv
%{python3_sitelib}/kea
%{_mandir}/man8/kea-admin.8*
%{_mandir}/man8/kea-ctrl-agent.8*
%{_mandir}/man8/kea-dhcp-ddns.8*
%{_mandir}/man8/kea-dhcp4.8*
%{_mandir}/man8/kea-dhcp6.8*
%{_mandir}/man8/kea-lfc.8*
%{_mandir}/man8/kea-netconf.8*
%{_mandir}/man8/kea-shell.8*
%{_mandir}/man8/keactrl.8*
%{_mandir}/man8/perfdhcp.8*
%dir /run/kea/
%{_tmpfilesdir}/kea.conf

%files doc
%{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/README
%{_pkgdocdir}/examples
%{_pkgdocdir}/CONTRIBUTING.md
%{_pkgdocdir}/platforms.rst
%{_pkgdocdir}/code_of_conduct.md
%{_pkgdocdir}/html

%files devel
%{_includedir}/kea
%{_libdir}/libkea-*.so

%files hooks
%dir %{_libdir}/kea
%{_libdir}/kea/hooks

%files libs
%license COPYING
# find `rpm --eval %%{_topdir}`/BUILDROOT/kea-*/usr/lib64/ -type f | grep /usr/lib64/libkea | sed -e 's#.*/usr/lib64\(.*\.so\.[0-9]\+\)\.[0-9]\+\.[0-9]\+#%%{_libdir}\1*#' | sort
%{_libdir}/libkea-asiodns.so.35*
%{_libdir}/libkea-asiolink.so.56*
%{_libdir}/libkea-cc.so.54*
%{_libdir}/libkea-cfgclient.so.51*
%{_libdir}/libkea-cryptolink.so.38*
%{_libdir}/libkea-d2srv.so.30*
%{_libdir}/libkea-database.so.48*
%{_libdir}/libkea-dhcp_ddns.so.41*
%{_libdir}/libkea-dhcp++.so.74*
%{_libdir}/libkea-dhcpsrv.so.90*
%{_libdir}/libkea-dns++.so.42*
%{_libdir}/libkea-eval.so.52*
%{_libdir}/libkea-exceptions.so.23*
%{_libdir}/libkea-hooks.so.78*
%{_libdir}/libkea-http.so.56*
%{_libdir}/libkea-log.so.48*
%{_libdir}/libkea-mysql.so.53*
%{_libdir}/libkea-pgsql.so.53*
%{_libdir}/libkea-process.so.57*
%{_libdir}/libkea-stats.so.29*
%{_libdir}/libkea-tcp.so.5*
%{_libdir}/libkea-util-io.so.0*
%{_libdir}/libkea-util.so.68*


%changelog
%autochangelog
