Name:           kea
Version:        3.0.2
Release:        %autorelease
Summary:        DHCPv4, DHCPv6 and DDNS server from ISC
License:        MPL-2.0 AND BSL-1.0
URL:            http://kea.isc.org

# Support for netconf is not enabled
%bcond_with sysrepo
%bcond_with tests

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

Source0:        https://downloads.isc.org/isc/kea/%{version}/kea-%{version}.tar.xz
Source1:        https://downloads.isc.org/isc/kea/%{version}/kea-%{version}.tar.xz.asc
Source2:        https://downloads.isc.org/isc/keama/%{keama_version}/keama-%{keama_version}.tar.gz
Source3:        https://downloads.isc.org/isc/keama/%{keama_version}/keama-%{keama_version}.tar.gz.asc
Source10:       https://www.isc.org/docs/isc-keyblock.asc
Source11:       kea-dhcp4.service
Source12:       kea-dhcp6.service
Source13:       kea-dhcp-ddns.service
Source14:       kea-ctrl-agent.service
Source15:       systemd-tmpfiles.conf
Source16:       systemd-sysusers.conf

Patch1:         kea-sd-daemon.patch

BuildRequires: boost-devel
# %%meson -D crypto=openssl
BuildRequires: openssl-devel
%if 0%{?fedora}
# https://bugzilla.redhat.com/show_bug.cgi?id=2300868#c4
BuildRequires: openssl-devel-engine
%endif
# %%meson -D krb5=enabled
BuildRequires: krb5-devel
# %%meson -D mysql=enabled
BuildRequires: mariadb-connector-c-devel
# %%meson -D postgresql=enabled
%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires: libpq-devel
%else
BuildRequires: postgresql-server-devel
%endif
# %%meson -D systemd=enabled
BuildRequires: systemd-devel
%if %{with sysrepo}
# %%meson -D netconf=enabled
BuildRequires: sysrepo-devel
%endif
%if %{with tests}
# %%meson -D tests=enabled
%ifarch %{valgrind_arches}
BuildRequires: valgrind-devel
%endif
BuildRequires: gtest-devel
BuildRequires: procps-ng
%endif
BuildRequires: log4cplus-devel
BuildRequires: python3-devel

BuildRequires: gcc-c++
BuildRequires: autoconf automake libtool
BuildRequires: make
BuildRequires: meson
BuildRequires: bison
BuildRequires: flex
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
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
%autosetup -p1 -n kea-%{version}

%build
# This removes RPATH from binaries
export KEA_PKG_TYPE_IN_CONFIGURE="rpm"

%meson \
    --install-umask 0022 \
%if %{with sysrepo}
    -D netconf=enabled \
%else
    -D netconf=disabled \
%endif
%if %{with tests}
    -D tests=enabled \
%else
    -D tests=disabled \
%endif
    -D crypto=openssl \
    -D krb5=enabled \
    -D mysql=enabled \
    -D postgresql=enabled \
    -D systemd=enabled

%meson_build
%meson_build doc

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

%if %{with tests}
%check
%meson_test
%endif

%install
%meson_install

# Install Keama
pushd ../keama-%{keama_version}
%make_install
popd

# Remove Keama's static library, dhcp headers and man pages
rm %{buildroot}/%{_libdir}/libdhcp.a
rm -rf %{buildroot}/%{_includedir}/omapip/
rm -rf %{buildroot}%{_mandir}/man5/

# Remove keactrl
rm %{buildroot}%{_sysconfdir}/kea/keactrl.conf
rm %{buildroot}%{_sbindir}/keactrl 
rm %{buildroot}%{_mandir}/man8/keactrl.8*

%if %{without sysrepo}
# Remove netconf files
rm %{buildroot}%{_mandir}/man8/kea-netconf.8
%endif

rm %{buildroot}%{_pkgdocdir}/COPYING

rm -rf %{buildroot}/usr/share/kea/meson-info/

# Create empty password file for the Kea Control Agent
install -m 0640 /dev/null %{buildroot}%{_sysconfdir}/kea/kea-api-password

# Install systemd units
install -Dpm 0644 %{S:11} %{buildroot}%{_unitdir}/kea-dhcp4.service
install -Dpm 0644 %{S:12} %{buildroot}%{_unitdir}/kea-dhcp6.service
install -Dpm 0644 %{S:13} %{buildroot}%{_unitdir}/kea-dhcp-ddns.service
install -Dpm 0644 %{S:14} %{buildroot}%{_unitdir}/kea-ctrl-agent.service

# Start empty lease databases
mkdir -p %{buildroot}%{_sharedstatedir}/kea/
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases4.csv
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases6.csv

# Install systemd sysusers and tmpfiles configs
install -Dpm 0644 %{S:16} %{buildroot}%{_sysusersdir}/kea.conf
install -Dpm 0644 %{S:15} %{buildroot}%{_tmpfilesdir}/kea.conf

mkdir -p %{buildroot}%{_rundir}
install -dm 0750 %{buildroot}%{_rundir}/kea/

mkdir -p %{buildroot}%{_localstatedir}/log
install -dm 0750 %{buildroot}%{_localstatedir}/log/kea/

%post
# Set a pseudo-random password for default config to secure fresh install and allow CA startup without user intervention
if [[ ! -s %{_sysconfdir}/kea/kea-api-password && -n `grep '"password-file": "kea-api-password"' %{_sysconfdir}/kea/kea-ctrl-agent.conf` ]]; then
    (umask 0027; head -c 32 /dev/urandom | base64 > %{_sysconfdir}/kea/kea-api-password)
    chown root:kea %{_sysconfdir}/kea/kea-api-password
fi
%systemd_post kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%preun
%systemd_preun kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%postun
%systemd_postun_with_restart kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service
%ldconfig_scriptlets libs

%files
%license COPYING
%{_sbindir}/kea-admin
%{_sbindir}/kea-ctrl-agent
%{_sbindir}/kea-dhcp-ddns
%{_sbindir}/kea-dhcp4
%{_sbindir}/kea-dhcp6
%{_sbindir}/kea-lfc
%{_sbindir}/kea-shell
%{_sbindir}/perfdhcp
%{_unitdir}/kea*.service
%{_datarootdir}/kea
%dir %attr(0750,root,kea) %{_sysconfdir}/kea/
%config(noreplace) %attr(0640,root,kea) %{_sysconfdir}/kea/kea*.conf
%ghost %config(noreplace,missingok) %attr(0640,root,kea) %verify(not md5 size mtime) %{_sysconfdir}/kea/kea-api-password
%dir %attr(0750,kea,kea) %{_sharedstatedir}/kea
%config(noreplace) %attr(0640,kea,kea) %{_sharedstatedir}/kea/kea-leases*.csv
%dir %attr(0750,kea,kea) %{_rundir}/kea/
%dir %attr(0750,kea,kea) %{_localstatedir}/log/kea
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
%{_mandir}/man8/perfdhcp.8*
%{_tmpfilesdir}/kea.conf
%{_sysusersdir}/kea.conf

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
%{_bindir}/kea-msg-compiler
%{_includedir}/kea
%{_libdir}/libkea-asiodns.so
%{_libdir}/libkea-asiolink.so
%{_libdir}/libkea-cc.so
%{_libdir}/libkea-cfgrpt.so
%{_libdir}/libkea-config.so
%{_libdir}/libkea-cryptolink.so
%{_libdir}/libkea-d2srv.so
%{_libdir}/libkea-database.so
%{_libdir}/libkea-dhcp_ddns.so
%{_libdir}/libkea-dhcp.so
%{_libdir}/libkea-dhcpsrv.so
%{_libdir}/libkea-dns.so
%{_libdir}/libkea-eval.so
%{_libdir}/libkea-exceptions.so
%{_libdir}/libkea-hooks.so
%{_libdir}/libkea-http.so
%{_libdir}/libkea-log-interprocess.so
%{_libdir}/libkea-log.so
%{_libdir}/libkea-mysql.so
%{_libdir}/libkea-pgsql.so
%{_libdir}/libkea-process.so
%{_libdir}/libkea-stats.so
%{_libdir}/libkea-tcp.so
%{_libdir}/libkea-util-io.so
%{_libdir}/libkea-util.so
%{_libdir}/pkgconfig/kea.pc

%files hooks
%dir %{_sysconfdir}/kea/radius
%{_sysconfdir}/kea/radius/dictionary
%dir %{_libdir}/kea
%dir %{_libdir}/kea/hooks
%{_libdir}/kea/hooks/libddns_gss_tsig.so
%{_libdir}/kea/hooks/libdhcp_bootp.so
%{_libdir}/kea/hooks/libdhcp_class_cmds.so
%{_libdir}/kea/hooks/libdhcp_ddns_tuning.so
%{_libdir}/kea/hooks/libdhcp_flex_id.so
%{_libdir}/kea/hooks/libdhcp_flex_option.so
%{_libdir}/kea/hooks/libdhcp_ha.so
%{_libdir}/kea/hooks/libdhcp_host_cache.so
%{_libdir}/kea/hooks/libdhcp_host_cmds.so
%{_libdir}/kea/hooks/libdhcp_lease_cmds.so
%{_libdir}/kea/hooks/libdhcp_lease_query.so
%{_libdir}/kea/hooks/libdhcp_legal_log.so
%{_libdir}/kea/hooks/libdhcp_limits.so
%{_libdir}/kea/hooks/libdhcp_mysql.so
%{_libdir}/kea/hooks/libdhcp_perfmon.so
%{_libdir}/kea/hooks/libdhcp_pgsql.so
%{_libdir}/kea/hooks/libdhcp_ping_check.so
%{_libdir}/kea/hooks/libdhcp_radius.so
%{_libdir}/kea/hooks/libdhcp_run_script.so
%{_libdir}/kea/hooks/libdhcp_stat_cmds.so
%{_libdir}/kea/hooks/libdhcp_subnet_cmds.so

%files libs
%license COPYING
# older: find `rpm --eval %%{_topdir}`/BUILDROOT/kea-*/usr/lib64/ -type f | grep /usr/lib64/libkea | sed -e 's#.*/usr/lib64\(.*\.so\.[0-9]\+\)\.[0-9]\+\.[0-9]\+#%%{_libdir}\1*#' | sort
# >=f41: find `rpm --eval %%{_topdir}`/BUILD/kea-*/BUILDROOT/usr/lib64/ -type f | grep /usr/lib64/libkea | sed -e 's#.*/usr/lib64\(.*\.so\.[0-9]\+\)\.[0-9]\+\.[0-9]\+#%%{_libdir}\1*#' | sort
%{_libdir}/libkea-asiodns.so.62*
%{_libdir}/libkea-asiolink.so.88*
%{_libdir}/libkea-cc.so.82*
%{_libdir}/libkea-cfgrpt.so.3*
%{_libdir}/libkea-config.so.83*
%{_libdir}/libkea-cryptolink.so.64*
%{_libdir}/libkea-d2srv.so.63*
%{_libdir}/libkea-database.so.76*
%{_libdir}/libkea-dhcp_ddns.so.68*
%{_libdir}/libkea-dhcp.so.109*
%{_libdir}/libkea-dhcpsrv.so.131*
%{_libdir}/libkea-dns.so.71*
%{_libdir}/libkea-eval.so.84*
%{_libdir}/libkea-exceptions.so.45*
%{_libdir}/libkea-hooks.so.120*
%{_libdir}/libkea-http.so.87*
%{_libdir}/libkea-log-interprocess.so.3*
%{_libdir}/libkea-log.so.75*
%{_libdir}/libkea-mysql.so.88*
%{_libdir}/libkea-pgsql.so.88*
%{_libdir}/libkea-process.so.90*
%{_libdir}/libkea-stats.so.53*
%{_libdir}/libkea-tcp.so.33*
%{_libdir}/libkea-util-io.so.12*
%{_libdir}/libkea-util.so.101*

%files keama
%license COPYING
%{_bindir}/keama
%{_mandir}/man8/keama.8*

%changelog
%autochangelog
