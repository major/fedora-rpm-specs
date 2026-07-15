Name:           kea
Version:        3.2.0
Release:        %autorelease
Summary:        DHCPv4, DHCPv6 and DDNS server from ISC
License:        MPL-2.0 AND BSL-1.0
URL:            http://kea.isc.org

# Support for netconf is not enabled
%bcond_with sysrepo
%bcond_with tests

# The upstream tagged the 4.5.0 on Sep 19, 2023; grab the latest Keama from git instead
# To switch to a tagged release: uncomment keama_version
#%%global keama_version 4.5.0
%global keama_commit 046ceef7a5db084211179dac42e986cda88a3c0e
%global keama_shortcommit %{lua:print(rpm.expand("%{keama_commit}"):sub(1,7))}
%global keama_dir keama-%{?keama_version}%{!?keama_version:%{keama_shortcommit}}

# Conflict with kea-next
%global upstream_name kea
%define upstream_name_compat() \
%if "%{name}" != "%{upstream_name}" \
Provides: %1 = %{version}-%{release} \
Conflicts: %1 \
%endif

Source0:        https://downloads.isc.org/isc/kea/%{version}/kea-%{version}.tar.xz
Source1:        https://downloads.isc.org/isc/kea/%{version}/kea-%{version}.tar.xz.asc
%if 0%{?keama_version:1}
Source2:        https://downloads.isc.org/isc/keama/%{keama_version}/keama-%{keama_version}.tar.gz
Source3:        https://downloads.isc.org/isc/keama/%{keama_version}/keama-%{keama_version}.tar.gz.asc
%else
Source2:        https://gitlab.isc.org/isc-projects/keama/-/archive/%{keama_shortcommit}/keama-%{keama_shortcommit}.tar.gz
%endif
Source10:       https://www.isc.org/docs/isc-keyblock.asc
Source11:       kea-dhcp4.service
Source12:       kea-dhcp6.service
Source13:       kea-dhcp-ddns.service
Source14:       systemd-tmpfiles.conf
Source15:       systemd-sysusers.conf

Patch1:         kea-sd-daemon.patch
# Fix build with OpenSSL 4.0
Patch2:         kea-add-const-qualifiers-to-OpenSSL-X509-pointers.patch

BuildRequires: boost-devel
# %%meson -D crypto=openssl
BuildRequires: openssl-devel
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
BuildRequires: gpgverify

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

%description keama
The KEA Migration Assistant is an experimental tool which helps to translate
ISC DHCP configurations to Kea.

%prep
%{gpgverify} --keyring='%{S:10}' --signature='%{S:1}' --data='%{S:0}'
%if 0%{?keama_version:1}
%{gpgverify} --keyring='%{S:10}' --signature='%{S:3}' --data='%{S:2}'
%endif

%autosetup -T -b2 -N -n %{keama_dir}
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
pushd ../%{keama_dir}

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
pushd ../%{keama_dir}
%make_install
popd

# Remove keactrl
find %{buildroot} -name keactrl\* -delete

%if %{without sysrepo}
# Remove netconf files
find %{buildroot} -name kea-netconf\* -delete
%endif

rm %{buildroot}%{_pkgdocdir}/COPYING

rm -rf %{buildroot}/usr/share/kea/meson-info/

# Install systemd units
install -Dpm 0644 %{S:11} %{buildroot}%{_unitdir}/kea-dhcp4.service
install -Dpm 0644 %{S:12} %{buildroot}%{_unitdir}/kea-dhcp6.service
install -Dpm 0644 %{S:13} %{buildroot}%{_unitdir}/kea-dhcp-ddns.service

# Start empty lease databases
mkdir -p %{buildroot}%{_sharedstatedir}/kea/
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases4.csv
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases6.csv

# Install systemd sysusers and tmpfiles configs
install -Dpm 0644 %{S:15} %{buildroot}%{_sysusersdir}/kea.conf
install -Dpm 0644 %{S:14} %{buildroot}%{_tmpfilesdir}/kea.conf

mkdir -p %{buildroot}%{_rundir}
install -dm 0750 %{buildroot}%{_rundir}/kea/

mkdir -p %{buildroot}%{_localstatedir}/log
install -dm 0750 %{buildroot}%{_localstatedir}/log/kea/

%pretrans
if [ $1 -ge 2 ]; then
    # kea-ctrl-agent was removed in 3.2.0; stop any running instance on upgrade
    systemctl disable --now kea-ctrl-agent.service >/dev/null 2>&1 || :
fi

%post
%systemd_post kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service

%preun
%systemd_preun kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service

%postun
%systemd_postun_with_restart kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service
%ldconfig_scriptlets libs

%files
%license COPYING
%{_sbindir}/kea-admin
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
%dir %attr(0750,kea,kea) %{_sharedstatedir}/kea
%config(noreplace) %attr(0640,kea,kea) %{_sharedstatedir}/kea/kea-leases*.csv
%dir %attr(0750,kea,kea) %{_rundir}/kea/
%dir %attr(0750,kea,kea) %{_localstatedir}/log/kea
%{python3_sitelib}/kea
%{_mandir}/man8/kea-admin.8*
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
# find `rpm --eval %%{_topdir}`/BUILD/kea-*/BUILDROOT/usr/lib64/ -type f | grep /usr/lib64/libkea | sed -e 's#.*/usr/lib64\(.*\.so\.[0-9]\+\)\.[0-9]\+\.[0-9]\+#%%{_libdir}\1*#' | sort
%{_libdir}/libkea-asiodns.so.75*
%{_libdir}/libkea-asiolink.so.105*
%{_libdir}/libkea-cc.so.98*
%{_libdir}/libkea-cfgrpt.so.3*
%{_libdir}/libkea-config.so.98*
%{_libdir}/libkea-cryptolink.so.76*
%{_libdir}/libkea-d2srv.so.75*
%{_libdir}/libkea-database.so.88*
%{_libdir}/libkea-dhcp_ddns.so.82*
%{_libdir}/libkea-dhcp.so.129*
%{_libdir}/libkea-dhcpsrv.so.149*
%{_libdir}/libkea-dns.so.84*
%{_libdir}/libkea-eval.so.97*
%{_libdir}/libkea-exceptions.so.55*
%{_libdir}/libkea-hooks.so.139*
%{_libdir}/libkea-http.so.100*
%{_libdir}/libkea-log-interprocess.so.4*
%{_libdir}/libkea-log.so.86*
%{_libdir}/libkea-mysql.so.106*
%{_libdir}/libkea-pgsql.so.105*
%{_libdir}/libkea-process.so.105*
%{_libdir}/libkea-stats.so.64*
%{_libdir}/libkea-tcp.so.45*
%{_libdir}/libkea-util-io.so.12*
%{_libdir}/libkea-util.so.118*

%files keama
%license COPYING
%{_bindir}/keama
%{_mandir}/man8/keama.8*

%changelog
%autochangelog
