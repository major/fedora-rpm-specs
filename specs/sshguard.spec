%if 0%{?rhel} >= 8 || 0%{?fedora}
%global use_subpackages 1
%endif

Name: sshguard
Version: 2.5.1
Release: %autorelease
# The entire source code is BSD-3-Clause
# except src/parser/attack_parser.{h,c} is GPL-3.0-or-later
# except src/blocker/hash_32a.c & src/blocker/fnv.h which are Public Domain
# the latter two get compiled in, the license is thus superseded
# src/parser/* is compiled into its own binary %%{_libexecdir}/%%{name}/sshg_parser
License: BSD-3-Clause AND GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
Summary: Protects hosts from brute-force attacks against SSH and other services
Url: http://www.sshguard.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.conf.in
Source2: %{name}.whitelist
Patch1: 0001-fix-backend-path-in-example.patch

# fnv is a very small implementation of the fnv hash algorithm not worth splitting
# into its own package. It has not seen updates since 2012, and upstream does not
# distribute it as a stand-alone library
# Public Domain license
Provides: bundled(fnv) = 5.0.2
# simclist is a small library not worth splitting into its own package, and has not
# seen updates since 2011
# BSD-3-Clause license
Provides: bundled(simclist) = 1.4.4

%if 0%{?use_subpackages}
# Require a firewall backend
Requires: %{name}-config = %{version}-%{release}
# Autoinstall appropriate firewall backends
Recommends: (%{name}-firewalld if firewalld)
Recommends: (%{name}-iptables if iptables-services)
Recommends: (%{name}-nftables if nftables)
%endif

BuildRequires: make
BuildRequires: gcc
BuildRequires: flex
BuildRequires: byacc
Requires: coreutils
Requires: grep

Requires: systemd
# for systemd service installation support
%if 0%{?fedora} > 29
BuildRequires: systemd-rpm-macros
%else
BuildRequires: systemd
%endif

%description
Sshguard protects hosts from brute-force attacks against SSH and other
services. It aggregates system logs and blocks repeat offenders using one of
several firewall backends.

Sshguard can read log messages from standard input or monitor one or more log
files. Log messages are parsed, line-by-line, for recognized patterns. If an
attack, such as several login failures within a few seconds, is detected, the
offending IP is blocked. Offenders are unblocked after a set interval, but can
be semi-permanently banned using the blacklist option.

%if 0%{?use_subpackages}
%package iptables
Requires: iptables-services
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-config = %{version}-%{release}
Conflicts: %{name}-firewalld %{name}-nftables
Summary: Configuration for iptables backend of SSHGuard
RemovePathPostfixes: .iptables
%description iptables
Sshguard-iptables provides a configuration file for SSHGuard to use iptables
as the firewall backend.

%package firewalld
Requires: firewalld ipset
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-config = %{version}-%{release}
Conflicts: %{name}-iptables %{name}-nftables
Summary: Configuration for firewalld backend of SSHGuard
RemovePathPostfixes: .firewalld
%description firewalld
Sshguard-firewalld provides a configuration file for SSHGuard to use firewalld
as the firewall backend.

%package nftables
Requires: nftables
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-config = %{version}-%{release}
Conflicts: %{name}-firewalld %{name}-iptables
Summary: Configuration for nftables backend of SSHGuard
RemovePathPostfixes: .nftables
%description nftables
Sshguard-nftables provides a configuration file for SSHGuard to use nftables
as the firewall backend.
%endif

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup -p1

sed -i -e "s|%%{_bindir}|%{_bindir}|g" \
       -e "s|%%{_sbindir}|%{_sbindir}|g" \
       -e "s|%%{_libexecdir}|%{_libexecdir}|g" \
       -e "s|%%{_sysconfdir}|%{_sysconfdir}|g" \
       -e "s|%%{_initddir}|%{_initddir}|g" \
       -e "s|%%{_localstatedir}|%{_localstatedir}|g" \
       -e "s|%%{_sharedstatedir}|%{_sharedstatedir}|g" \
       -e "s|%%{_rundir}|%{_rundir}|g" \
       -e "s|%%{_pkgdocdir}|%{_pkgdocdir}|g" \
       -e "s|%%{name}|%{name}|g" \
       %{SOURCE1} %{SOURCE2}

%build
%{configure} --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --sbindir=%{_sbindir} --libexecdir=%{_libexecdir}/%{name}
%{make_build}

%install
%{make_install}
install -p -d -m 0755 %{buildroot}%{_pkgdocdir}/
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/
install -p -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}/
%if 0%{?use_subpackages}
sed -e "s|__BACKEND__|sshg-fw-firewalld|g" %{SOURCE1} > %{buildroot}%{_sysconfdir}/%{name}.conf.firewalld
sed -e "s|__BACKEND__|sshg-fw-nft-sets|g" %{SOURCE1} > %{buildroot}%{_sysconfdir}/%{name}.conf.nftables
sed -e "s|__BACKEND__|sshg-fw-iptables|g" %{SOURCE1} > %{buildroot}%{_sysconfdir}/%{name}.conf.iptables
chmod 0644 %{buildroot}%{_sysconfdir}/%{name}.conf.*
%endif
install -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.whitelist
install -p -d -m 0755 %{buildroot}%{_unitdir}
sed -i -e "/ExecStartPre=/d" examples/%{name}.service
sed -i -e "s|ExecStart=/usr/local/sbin/sshguard|ExecStart=%{_sbindir}/%{name}|g" examples/%{name}.service
install -p -m 0644 examples/%{name}.service %{buildroot}%{_unitdir}/

# cleanup
# *.plist is only relevant for MacOS systems
rm examples/net.sshguard.plist
# we already ship a service file
rm examples/sshguard.service

%check
make check

#-- SCRIPTLETS -----------------------------------------------------------------#
%post
%systemd_post %{name}.service

%if 0%{?use_subpackages}
# with iptables backend, sshguard does not auto-create its tables, so we do that here
%post iptables
if [[ $1 -eq 1 ]]; then
  iptables -N sshguard
  iptables -A INPUT -j sshguard
  iptables-save > /etc/sysconfig/iptables
  ip6tables -N sshguard
  ip6tables -A INPUT -j sshguard
  ip6tables-save > /etc/sysconfig/ip6tables
fi
exit 0
%endif

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

#-- FILES ---------------------------------------------------------------------#
%files
%doc examples
%doc README.rst
%doc CONTRIBUTING.rst
%license COPYING
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*
%{_mandir}/man7/%{name}*
%dir %{_sharedstatedir}/%{name}/
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/sshg-logtail
%{_libexecdir}/%{name}/sshg-parser
%{_libexecdir}/%{name}/sshg-blocker
%{_libexecdir}/%{name}/sshg-fw-firewalld
%{_libexecdir}/%{name}/sshg-fw-hosts
%{_libexecdir}/%{name}/sshg-fw-ipfilter
%{_libexecdir}/%{name}/sshg-fw-ipfw
%{_libexecdir}/%{name}/sshg-fw-ipset
%{_libexecdir}/%{name}/sshg-fw-iptables
%{_libexecdir}/%{name}/sshg-fw-null
%{_libexecdir}/%{name}/sshg-fw-pf
%{_libexecdir}/%{name}/sshg-fw-nft-sets
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.whitelist

%if 0%{?use_subpackages}
%files iptables
%config(noreplace) %{_sysconfdir}/%{name}.conf.iptables

%files firewalld
%config(noreplace) %{_sysconfdir}/%{name}.conf.firewalld

%files nftables
%config(noreplace) %{_sysconfdir}/%{name}.conf.nftables
%endif

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
%autochangelog
