Name:           kea
Version:        2.6.1
Release:        %autorelease
Summary:        DHCPv4, DHCPv6 and DDNS server from ISC
License:        MPL-2.0 AND BSL-1.0
URL:            http://kea.isc.org

# TODO: no support for netconf/sysconf yet
%bcond_with sysrepo
%bcond_with gtest

#%%global prever P1
%global keama_version 4.5.0
# Bundled version of Bind libraries linked into Keama
%global bind_version 9.11.36

# Conflict with kea-next
%global upstream_name kea
%define upstream_name_compat() \
%if "%{name}" != "%{upstream_name}" \
Provides: %1 = %{version}-%{release} \
Conflicts: %1 \
%endif

Source0:        https://downloads.isc.org/isc/kea/%{version}%{?prever:-%{prever}}/kea-%{version}%{?prever:-%{prever}}.tar.gz
Source1:        https://downloads.isc.org/isc/kea/%{version}%{?prever:-%{prever}}/kea-%{version}%{?prever:-%{prever}}.tar.gz.asc
Source2:        https://downloads.isc.org/isc/keama/%{keama_version}/keama-%{keama_version}.tar.gz
Source3:        https://downloads.isc.org/isc/keama/%{keama_version}/keama-%{keama_version}.tar.gz.asc
Source10:       https://www.isc.org/docs/isc-keyblock.asc
Source11:       kea-dhcp4.service
Source12:       kea-dhcp6.service
Source13:       kea-dhcp-ddns.service
Source14:       kea-ctrl-agent.service
Source15:       systemd-tmpfiles.conf
Source16:       systemd-sysusers.conf

Patch1:         kea-openssl-version.patch
Patch2:         kea-gtest.patch

# autoreconf
BuildRequires: autoconf automake libtool
BuildRequires: boost-devel
BuildRequires: gcc-c++
# %%configure --with-openssl
BuildRequires: openssl-devel
%if 0%{?fedora} > 40
# https://bugzilla.redhat.com/show_bug.cgi?id=2300868#c4
BuildRequires: openssl-devel-engine
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
# %%configure --with-mysql
BuildRequires: mariadb-connector-c-devel
# %%configure --with-pgsql
%if 0%{?fedora} > 40 || 0%{?rhel} > 9
BuildRequires: libpq-devel
%else
BuildRequires: postgresql-server-devel
%endif
%else
# %%configure --with-mysql
BuildRequires: mariadb-devel
# %%configure --with-pgsql
BuildRequires: postgresql-devel
%endif
BuildRequires: log4cplus-devel
%if %{with sysrepo}
# %%configure --with-sysrepo
BuildRequires: sysrepo-devel
%endif

%ifarch %{valgrind_arches}
BuildRequires: valgrind-devel
%endif
%if %{with gtest}
# %%configure --enable-gtest
BuildRequires: gtest-devel
# src/lib/testutils/dhcp_test_lib.sh
BuildRequires: procps-ng
%endif
# %%configure --enable-generate-parser
BuildRequires: bison
BuildRequires: flex
# %%configure --enable-shell
BuildRequires: python3-devel
# in case you ever wanted to use %%configure --enable-generate-docs
#BuildRequires: elinks asciidoc plantuml
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: make
BuildRequires: gnupg2

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%upstream_name_compat %{upstream_name}
Requires: coreutils util-linux
%{?systemd_requires}

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
%upstream_name_compat %{upstream_name}-libs

%description libs
This package contains shared libraries used by Kea DHCP server.


%package keama
Summary: Experimental migration assistant for Kea
Provides: bundled(bind-libs) = %{bind_version}

%description keama
The KEA Migration Assistant is an experimental tool which helps to translate
ISC DHCP configurations to Kea.


%prep
%if 0%{?fedora} || 0%{?rhel} > 8
%{gpgverify} --keyring='%{S:10}' --signature='%{S:1}' --data='%{S:0}'
%{gpgverify} --keyring='%{S:10}' --signature='%{S:3}' --data='%{S:2}'
%endif

%autosetup -T -b2 -N -n keama-%{keama_version}
%autosetup -p1 -n kea-%{version}%{?prever:-%{prever}}

rm -rf doc/sphinx/_build

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
    --enable-generate-docs \
    --enable-generate-messages \
    --enable-generate-parser \
    --enable-shell \
    --enable-perfdhcp \
%if %{with gtest}
    --with-gtest \
%endif
    --with-mysql \
    --with-pgsql \
    --with-gnu-ld \
    --with-log4cplus \
%if %{with sysrepo}
    --with-sysrepo \
%endif
    --with-openssl

%make_build

# Configure & build Keama
pushd ../keama-%{keama_version}

# We need to unpack the embedded copy of bind and call autoreconf to
# ensure that config.{sub,guess} is up to date, since the copies
# included in the archive are extremely old (2013) and unaware of
# more recent architectures such as riscv64. The Keama build system
# would normally take care of unpacking the archive, but it also
# handles gracefully us doing it ourselves
tar -C bind/ -zxvf bind/bind.tar.gz

pushd bind/bind-%{bind_version}/

autoreconf --verbose --force --install

# Back to Keama. Its build system will take care of configuring and
# building the embedded copy of bind
popd

autoreconf --verbose --force --install

%configure \
    --disable-dependency-tracking \
    --disable-silent-rules

%make_build
popd


%if %{with gtest}
%check
make check
%endif


%install
%make_install docdir=%{_pkgdocdir}

# Install Keama
pushd ../keama-%{keama_version}
%make_install
popd

# Remove Keama's static library, dhcp headers and man pages
rm -f %{buildroot}/%{_libdir}/libdhcp.a
rm -rf %{buildroot}/%{_includedir}/omapip/
rm -rf %{buildroot}%{_mandir}/man5/

# Get rid of .la files
find %{buildroot} -type f -name "*.la" -delete -print

%if %{without sysrepo}
# Remove netconf files
rm %{buildroot}%{_mandir}/man8/kea-netconf.8
%endif

# Install systemd units
install -Dpm 0644 %{S:11} %{buildroot}%{_unitdir}/kea-dhcp4.service
install -Dpm 0644 %{S:12} %{buildroot}%{_unitdir}/kea-dhcp6.service
install -Dpm 0644 %{S:13} %{buildroot}%{_unitdir}/kea-dhcp-ddns.service
install -Dpm 0644 %{S:14} %{buildroot}%{_unitdir}/kea-ctrl-agent.service

# systemd-sysusers
install -p -D -m 0644 %{S:16} %{buildroot}%{_sysusersdir}/kea.conf

# Start empty lease databases
mkdir -p %{buildroot}%{_sharedstatedir}/kea/
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases4.csv
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases6.csv

rm -f %{buildroot}%{_pkgdocdir}/COPYING
rm -f %{buildroot}%{_pkgdocdir}/html/.buildinfo

mkdir -p %{buildroot}/run
install -dm 0755 %{buildroot}/run/kea/

install -Dpm 0644 %{S:15} %{buildroot}%{_tmpfilesdir}/kea.conf

# Create log dir /var/log/kea for logging, since kea user can't create log files in /var/log
mkdir -p %{buildroot}%{_localstatedir}/log/kea
sed -i -e 's|log\/|log\/kea\/|g' \
    %{buildroot}%{_sysconfdir}/kea/kea-dhcp4.conf \
    %{buildroot}%{_sysconfdir}/kea/kea-dhcp6.conf \
    %{buildroot}%{_sysconfdir}/kea/kea-dhcp-ddns.conf \
    %{buildroot}%{_sysconfdir}/kea/kea-ctrl-agent.conf
#    %{buildroot}%{_sysconfdir}/kea/kea-netconf.conf  # TODO: no support for netconf/sysconf yet


%post
# Kea runs under kea user instead of root now, but if its files got altered, their new
# ownership&permissions won't get changed so fix them to prevent startup failures
[ "`stat --format '%U:%G' %{_rundir}/kea/logger_lockfile 2>&1 | grep root:root`" = "root:root" ] \
    && chown kea:kea %{_rundir}/kea/logger_lockfile
[ "`stat --format '%U:%G' %{_sharedstatedir}/kea/kea-leases4.csv 2>&1 | grep root:root`" = "root:root" ] \
    && chown kea:kea %{_sharedstatedir}/kea/kea-leases4.csv && chmod 0640 %{_sharedstatedir}/kea/kea-leases4.csv
[ "`stat --format '%U:%G' %{_sharedstatedir}/kea/kea-leases6.csv 2>&1 | grep root:root`" = "root:root" ] \
    && chown kea:kea %{_sharedstatedir}/kea/kea-leases6.csv && chmod 0640 %{_sharedstatedir}/kea/kea-leases6.csv
[ "`stat --format '%U:%G' %{_sharedstatedir}/kea/kea-dhcp6-serverid 2>&1 | grep root:root`" = "root:root" ] \
    && chown kea:kea %{_sharedstatedir}/kea/kea-dhcp6-serverid
[ "`stat --format '%U:%G' %{_sysconfdir}/kea/kea*.conf 2>&1 | grep root:root | head -1`" = "root:root" ] \
    && chown root:kea %{_sysconfdir}/kea/kea*.conf && chmod 0640 %{_sysconfdir}/kea/kea*.conf
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
%config(noreplace) %attr(0640,root,kea) %{_sysconfdir}/kea/kea*.conf
%{_datarootdir}/kea
%dir %attr(0750,kea,kea) %{_sharedstatedir}/kea
%config(noreplace) %attr(0640,kea,kea) %{_sharedstatedir}/kea/kea-leases*.csv
%{python3_sitelib}/kea
%{_mandir}/man8/kea-admin.8*
%{_mandir}/man8/kea-ctrl-agent.8*
%{_mandir}/man8/kea-dhcp-ddns.8*
%{_mandir}/man8/kea-dhcp4.8*
%{_mandir}/man8/kea-dhcp6.8*
%{_mandir}/man8/kea-lfc.8*
%if %{with sysrepo}
%{_mandir}/man8/kea-netconf.8*
%endif
%{_mandir}/man8/kea-shell.8*
%{_mandir}/man8/keactrl.8*
%{_mandir}/man8/perfdhcp.8*
%dir %attr(0755,kea,kea) %{_rundir}/kea/
%{_tmpfilesdir}/kea.conf
%{_sysusersdir}/kea.conf
%dir %attr(0750,kea,kea) %{_localstatedir}/log/kea

%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/code_of_conduct.md
%doc %{_pkgdocdir}/CONTRIBUTING.md
%doc %{_pkgdocdir}/examples
%doc %{_pkgdocdir}/html
%doc %{_pkgdocdir}/platforms.rst
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/SECURITY.md

%files devel
%{_includedir}/kea
%{_libdir}/libkea-*.so

%files hooks
%dir %{_libdir}/kea
%{_libdir}/kea/hooks

%files libs
%license COPYING
# old: find `rpm --eval %%{_topdir}`/BUILDROOT/kea-*/usr/lib64/ -type f | grep /usr/lib64/libkea | sed -e 's#.*/usr/lib64\(.*\.so\.[0-9]\+\)\.[0-9]\+\.[0-9]\+#%%{_libdir}\1*#' | sort
# f41: find `rpm --eval %%{_topdir}`/BUILD/kea-*/BUILDROOT/usr/lib64/ -type f | grep /usr/lib64/libkea | sed -e 's#.*/usr/lib64\(.*\.so\.[0-9]\+\)\.[0-9]\+\.[0-9]\+#%%{_libdir}\1*#' | sort
%{_libdir}/libkea-asiodns.so.48*
%{_libdir}/libkea-asiolink.so.71*
%{_libdir}/libkea-cc.so.68*
%{_libdir}/libkea-cfgclient.so.65*
%{_libdir}/libkea-cryptolink.so.50*
%{_libdir}/libkea-d2srv.so.46*
%{_libdir}/libkea-database.so.61*
%{_libdir}/libkea-dhcp_ddns.so.56*
%{_libdir}/libkea-dhcp++.so.90*
%{_libdir}/libkea-dhcpsrv.so.109*
%{_libdir}/libkea-dns++.so.56*
%{_libdir}/libkea-eval.so.69*
%{_libdir}/libkea-exceptions.so.33*
%{_libdir}/libkea-hooks.so.98*
%{_libdir}/libkea-http.so.71*
%{_libdir}/libkea-log.so.61*
%{_libdir}/libkea-mysql.so.70*
%{_libdir}/libkea-pgsql.so.70*
%{_libdir}/libkea-process.so.72*
%{_libdir}/libkea-stats.so.41*
%{_libdir}/libkea-tcp.so.18*
%{_libdir}/libkea-util-io.so.0*
%{_libdir}/libkea-util.so.84*

%files keama
%license COPYING
%{_bindir}/keama
%{_mandir}/man8/keama.8*


%changelog
%autochangelog
