%global _hardened_build 1

%global commit 72dd0a308130b9778828d143d1b9d9906218d6ac
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commdate 20191209
%global fromgit 0
## Use when first building a package set to see what patches are needed
%global bootstrap 0

%if 0%{?fedora} >= 36 || 0%{?rhel} >= 9
%bcond_with libdbi
%else
%bcond_without libdbi
%endif

%if 0%{?rhel} >= 9
%bcond_with radius
%else
%bcond_without radius
%endif

Name: nagios-plugins
Version: 2.4.9
%if 0%{?fromgit}
Release: 3.%{?commdate}git%{?shortcommit}%{?dist}
%else
Release: 4%{?dist}
%endif

Summary: Host/service/network monitoring program plugins for Nagios

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://www.nagios-plugins.org/

## When using checkouts from git, use the following
%if 0%{?fromgit} 
Source0: https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0: https://github.com/%{name}/%{name}/releases/download/release-%{version}/%{name}-%{version}.tar.gz
%endif
Source1: nagios-plugins.README.Fedora

# Patch from upstream PR https://github.com/nagios-plugins/nagios-plugins/pull/581
Patch1: %{name}-ntpsec-support.patch
Patch2: nagios-plugins-0002-Remove-assignment-of-not-parsed-to-jitter.patch
Patch7: nagios-plugins-0007-Fix-the-use-lib-statement-and-the-external-ntp-comma.patch
Patch12: nagios-plugins-0012-fix-perl-ntp-ipv6.patch

BuildRequires: make
BuildRequires: %{_bindir}/mailq
BuildRequires: procps
BuildRequires: %{_bindir}/ssh
BuildRequires: %{_bindir}/uptime
BuildRequires: %{_sbindir}/fping

# Needed for the git code
%if 0%{?fromgit}
BuildRequires: automake
BuildRequires: autoconf
%endif
#
BuildRequires: bind-utils
BuildRequires: gcc
BuildRequires: gettext
%if %{with libdbi}
BuildRequires: libdbi-devel
%else
Obsoletes: nagios-plugins-dbi < 2.4.0-6
%endif
BuildRequires: iputils
BuildRequires: net-snmp-devel
BuildRequires: net-snmp-utils
%if 0%{?fedora}
BuildRequires: ntpsec
%endif
BuildRequires: openldap-devel
BuildRequires: perl(Net::SNMP)
BuildRequires: perl(Crypt::X509)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(LWP::Simple)
BuildRequires: perl(Text::Glob)
BuildRequires: perl-generators
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: postgresql-devel
%else
BuildRequires: libpq-devel
%endif
BuildRequires: qstat
BuildRequires: samba-client

BuildRequires: mariadb-connector-c-devel
%if %{with radius}
BuildRequires: freeradius-client-devel
%endif
BuildRequires: %{_bindir}/uptime
BuildRequires: iputils
BuildRequires: %{_bindir}/ps

Requires: nagios-common >= 3.3.1-1

Obsoletes: nagios-plugins-linux_raid < 1.4.16-11

# nagios-plugins-1.4.16: the included gnulib files were last updated
# in June/July 2010
# Bundled gnulib exception (https://fedorahosted.org/fpc/ticket/174)
Provides: bundled(gnulib)

# Do not provide private Perl modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(utils\\)
%global reqfilt sh -c "%{__perl_requires} | sed -e 's!perl(utils)!nagios-plugins-perl!'"
%global __perl_requires %{reqfilt}


%description
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a Unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios. This package
contains those plugins.

%package all
Summary: Nagios Plugins - All plugins
Requires: nagios-plugins-breeze, nagios-plugins-by_ssh, nagios-plugins-dhcp, nagios-plugins-dig, nagios-plugins-disk, nagios-plugins-disk_smb, nagios-plugins-dns, nagios-plugins-dummy, nagios-plugins-file_age, nagios-plugins-flexlm, nagios-plugins-fping, nagios-plugins-hpjd, nagios-plugins-http, nagios-plugins-icmp, nagios-plugins-ide_smart, nagios-plugins-ircd, nagios-plugins-ldap, nagios-plugins-load, nagios-plugins-log, nagios-plugins-mailq, nagios-plugins-mrtg, nagios-plugins-mrtgtraf, nagios-plugins-mysql, nagios-plugins-nagios, nagios-plugins-nt, nagios-plugins-ntp, nagios-plugins-nwstat, nagios-plugins-oracle, nagios-plugins-overcr, nagios-plugins-pgsql, nagios-plugins-ping, nagios-plugins-procs, nagios-plugins-game, nagios-plugins-real, nagios-plugins-rpc, nagios-plugins-smtp, nagios-plugins-snmp, nagios-plugins-ssh, nagios-plugins-ssl_validity, nagios-plugins-swap, nagios-plugins-tcp, nagios-plugins-time, nagios-plugins-ups, nagios-plugins-users, nagios-plugins-wave, nagios-plugins-cluster
%ifnarch ppc ppc64 ppc64p7 sparc sparc64
Requires: nagios-plugins-sensors
%endif
%if 0%{?fedora}
Requires: nagios-plugins-ntp-perl
%endif

%description all
This package provides all Nagios plugins.

%package apt
Summary: Nagios Plugin - check_apt
Requires: nagios-plugins = %{version}-%{release}

%description apt
Provides check_apt support for Nagios.

%package breeze
Summary: Nagios Plugin - check_breeze
Requires: nagios-plugins = %{version}-%{release}

%description breeze
Provides check_breeze support for Nagios.

%package by_ssh
Summary: Nagios Plugin - check_by_ssh
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/ssh

%description by_ssh
Provides check_by_ssh support for Nagios.

%package cluster
Summary: Nagios Plugin - check_cluster
Requires: nagios-plugins = %{version}-%{release}

%description cluster
Provides check_cluster support for Nagios.

%if %{with libdbi}
%package dbi
Summary: Nagios Plugin - check_dbi
Requires: nagios-plugins = %{version}-%{release}

%description dbi
Provides check_dbi support for Nagios.
%endif

%package dhcp
Summary: Nagios Plugin - check_dhcp
Requires: nagios-plugins = %{version}-%{release}
Requires: group(nagios)
Requires(pre): group(nagios)

%description dhcp
Provides check_dhcp support for Nagios.

%package dig
Summary: Nagios Plugin - check_dig
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/dig

%description dig
Provides check_dig support for Nagios.

%package disk
Summary: Nagios Plugin - check_disk
Requires: nagios-plugins = %{version}-%{release}

%description disk
Provides check_disk support for Nagios.

%package disk_smb
Summary: Nagios Plugin - check_disk_smb
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/smbclient
Requires: perl(utf8::all)

%description disk_smb
Provides check_disk_smb support for Nagios.

%package dns
Summary: Nagios Plugin - check_dns
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/nslookup

%description dns
Provides check_dns support for Nagios.

%package dummy
Summary: Nagios Plugin - check_dummy
Requires: nagios-plugins = %{version}-%{release}

%description dummy
Provides check_dummy support for Nagios.
This plugin does not actually check anything, simply provide it with a flag
0-4 and it will return the corresponding status code to Nagios.

%package file_age
Summary: Nagios Plugin - check_file_age
Requires: nagios-plugins = %{version}-%{release}

%description file_age
Provides check_file_age support for Nagios.

%package flexlm
Summary: Nagios Plugin - check_flexlm
Requires: nagios-plugins = %{version}-%{release}

%description flexlm
Provides check_flexlm support for Nagios.

%package fping
Summary: Nagios Plugin - check_fping
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_sbindir}/fping
Requires: group(nagios)
Requires(pre): group(nagios)

%description fping
Provides check_fping support for Nagios.

%package game
Summary: Nagios Plugin - check_game
Requires: nagios-plugins = %{version}-%{release}
Requires: qstat

%description game
Provides check_game support for Nagios.

%package hpjd
Summary: Nagios Plugin - check_hpjd
Requires: nagios-plugins = %{version}-%{release}

%description hpjd
Provides check_hpjd support for Nagios.

%package http
Summary: Nagios Plugin - check_http
Requires: nagios-plugins = %{version}-%{release}
Requires: openssl

%description http
Provides check_http support for Nagios.

%package icmp
Summary: Nagios Plugin - check_icmp
Requires: nagios-plugins = %{version}-%{release}
Requires: group(nagios)
Requires(pre): group(nagios)

%description icmp
Provides check_icmp support for Nagios.

%package ide_smart
Summary: Nagios Plugin - check_ide_smart
Requires: nagios-plugins = %{version}-%{release}
Requires: group(nagios)
Requires(pre): group(nagios)

%description ide_smart
Provides check_ide_smart support for Nagios.

%package ifoperstatus
Summary: Nagios Plugin - check_ifoperstatus
Requires: nagios-plugins = %{version}-%{release}

%description ifoperstatus
Provides check_ifoperstatus support for Nagios to monitor network interfaces.

%package ifstatus
Summary: Nagios Plugin - check_ifstatus
Requires: nagios-plugins = %{version}-%{release}

%description ifstatus
Provides check_ifstatus support for Nagios to monitor network interfaces.

%package ircd
Summary: Nagios Plugin - check_ircd
Requires: nagios-plugins = %{version}-%{release}

%description ircd
Provides check_ircd support for Nagios.

%package ldap
Summary: Nagios Plugin - check_ldap
Requires: nagios-plugins = %{version}-%{release}
Requires: openssl

%description ldap
Provides check_ldap support for Nagios.

%package load
Summary: Nagios Plugin - check_load
Requires: nagios-plugins = %{version}-%{release}

%description load
Provides check_load support for Nagios.

%package log
Summary: Nagios Plugin - check_log
Requires: nagios-plugins = %{version}-%{release}
Requires: grep
Requires: coreutils

%description log
Provides check_log support for Nagios.

%package mailq
Summary: Nagios Plugin - check_mailq
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/mailq

%description mailq
Provides check_mailq support for Nagios.

%package mrtg
Summary: Nagios Plugin - check_mrtg
Requires: nagios-plugins = %{version}-%{release}

%description mrtg
Provides check_mrtg support for Nagios.

%package mrtgtraf
Summary: Nagios Plugin - check_mrtgtraf
Requires: nagios-plugins = %{version}-%{release}

%description mrtgtraf
Provides check_mrtgtraf support for Nagios.

%package mysql
Summary: Nagios Plugin - check_mysql
Requires: nagios-plugins = %{version}-%{release}
Requires: openssl

%description mysql
Provides check_mysql and check_mysql_query support for Nagios.

%package nagios
Summary: Nagios Plugin - check_nagios
Requires: nagios-plugins = %{version}-%{release}

%description nagios
Provides check_nagios support for Nagios.

%package nt
Summary: Nagios Plugin - check_nt
Requires: nagios-plugins = %{version}-%{release}

%description nt
Provides check_nt support for Nagios.

%package ntp
Summary: Nagios Plugin - check_ntp
Requires: nagios-plugins = %{version}-%{release}

%description ntp
Provides check_ntp support for Nagios.

%if 0%{?fedora}
%package ntp-perl
Summary: Nagios Plugin - check_ntp.pl
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_sbindir}/ntpdate
Requires: %{_sbindir}/ntpq

%description ntp-perl
Provides check_ntp.pl support for Nagios.
%endif

%package nwstat
Summary: Nagios Plugin - check_nwstat
Requires: nagios-plugins = %{version}-%{release}

%description nwstat
Provides check_nwstat support for Nagios.

%package oracle
Summary: Nagios Plugin - check_oracle
Requires: nagios-plugins = %{version}-%{release}

%description oracle
Provides check_oracle support for Nagios.

%package overcr
Summary: Nagios Plugin - check_overcr
Requires: nagios-plugins = %{version}-%{release}

%description overcr
Provides check_overcr support for Nagios.

%package perl
Summary: Nagios plugins perl dep.
Requires: nagios-plugins = %{version}-%{release}

%description perl
Perl dep for nagios plugins.  This is *NOT* an actual plugin it simply provides
utils.pm


%package pgsql
Summary: Nagios Plugin - check_pgsql
Requires: nagios-plugins = %{version}-%{release}

%description pgsql
Provides check_pgsql (PostgreSQL)  support for Nagios.

%package ping
Summary: Nagios Plugin - check_ping
Requires: nagios-plugins = %{version}-%{release}
Requires: iputils
Requires: iputils

%description ping
Provides check_ping support for Nagios.

%package procs
Summary: Nagios Plugin - check_procs
Requires: nagios-plugins = %{version}-%{release}

%description procs
Provides check_procs support for Nagios.

%if %{with radius}
%package radius
Summary: Nagios Plugin - check_radius
Requires: nagios-plugins = %{version}-%{release}

%description radius
Provides check_radius support for Nagios.
%endif

%package real
Summary: Nagios Plugin - check_real
Requires: nagios-plugins = %{version}-%{release}

%description real
Provides check_real (rtsp) support for Nagios.

%package remove_perfdata
Summary: Nagios plugin tool to remove perf data
Requires: nagios-plugins = %{version}-%{release}

%description remove_perfdata
Removes perfdata from specified plugin's output

%package rpc
Summary: Nagios Plugin - check_rpc
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_sbindir}/rpcinfo

%description rpc
Provides check_rpc support for Nagios.

%ifnarch ppc ppc64 sparc sparc64
%package sensors
Summary: Nagios Plugin - check_sensors
Requires: nagios-plugins = %{version}-%{release}
Requires: grep
Requires: %{_bindir}/sensors

%description sensors
Provides check_sensors support for Nagios.
%endif

%package smtp
Summary: Nagios Plugin - check_smtp
Requires: nagios-plugins = %{version}-%{release}
Requires: openssl

%description smtp
Provides check_smtp support for Nagios.

%package snmp
Summary: Nagios Plugin - check_snmp
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/snmpgetnext
Requires: %{_bindir}/snmpget

%description snmp
Provides check_snmp support for Nagios.

%package ssh
Summary: Nagios Plugin - check_ssh
Requires: nagios-plugins = %{version}-%{release}

%description ssh
Provides check_ssh support for Nagios.

%package ssl_validity
Summary: Nagios Plugin - check_ssl_validity
Requires: nagios-plugins = %{version}-%{release}
Requires: perl(Crypt::X509)
Requires: perl(Date::Parse)
Requires: perl(LWP::Simple)
Requires: perl(Text::Glob)
Requires: openssl

%description ssl_validity
Provides check_ssl_validity support for Nagios.

%package swap
Summary: Nagios Plugin - check_swap
Requires: nagios-plugins = %{version}-%{release}

%description swap
Provides check_swap support for Nagios.

%package tcp
Summary: Nagios Plugin - check_tcp
Requires: nagios-plugins = %{version}-%{release}
Provides: nagios-plugins-ftp = %{version}-%{release}
Provides: nagios-plugins-imap = %{version}-%{release}
Provides: nagios-plugins-jabber = %{version}-%{release}
Provides: nagios-plugins-nntp = %{version}-%{release}
Provides: nagios-plugins-nntps = %{version}-%{release}
Provides: nagios-plugins-pop = %{version}-%{release}
Provides: nagios-plugins-simap = %{version}-%{release}
Provides: nagios-plugins-spop = %{version}-%{release}
Provides: nagios-plugins-ssmtp = %{version}-%{release}
Provides: nagios-plugins-udp = %{version}-%{release}
Provides: nagios-plugins-udp2 = %{version}-%{release}
Obsoletes: nagios-plugins-udp < 1.4.15-2
Requires: openssl

%description tcp
Provides check_tcp, check_ftp, check_imap, check_jabber, check_nntp,
check_nntps, check_pop, check_simap, check_spop, check_ssmtp, check_udp
and check_clamd support for Nagios.

%package time
Summary: Nagios Plugin - check_time
Requires: nagios-plugins = %{version}-%{release}

%description time
Provides check_time support for Nagios.

%package ups
Summary: Nagios Plugin - check_ups
Requires: nagios-plugins = %{version}-%{release}

%description ups
Provides check_ups support for Nagios.

%package uptime
Summary: Nagios Plugin - check_uptime
Requires: nagios-plugins = %{version}-%{release}

%description uptime
Provides check_uptime support for Nagios.

%package users
Summary: Nagios Plugin - check_users
Requires: nagios-plugins = %{version}-%{release}

%description users
Provides check_users support for Nagios.

%package wave
Summary: Nagios Plugin - check_wave
Requires: nagios-plugins = %{version}-%{release}

%description wave
Provides check_wave support for Nagios.

%prep

%if 0%{?fromgit}
%autosetup -n %{name}-%{commit} -N
%else
%autosetup -n %{name}-%{version} -N
%endif

%patch -P 1 -p1 -b .ntpsec-support.patch
%patch -P 2 -p1 -b .remove_ntp_jitter
%patch -P 7 -p1 -b .fix_ntpcommands
%if 0%{?bootstrap} == 0
%patch -P 12 -p1 -b .fix_perl_ntp
%endif

%build

%if 0%{?fromgit}
./tools/setup
%endif
%configure \
	--libexecdir=%{_libdir}/nagios/plugins \
%if %{with libdbi}
	--with-dbi \
%endif
	--with-mysql \
	PATH_TO_SUDO=%{_bindir}/sudo \
	PATH_TO_QSTAT=%{_bindir}/quakestat \
	PATH_TO_FPING=%{_sbindir}/fping \
%if 0%{?fedora}
	PATH_TO_NTPQ=%{_sbindir}/ntpq \
	PATH_TO_NTPDC=%{_sbindir}/ntpdc \
	PATH_TO_NTPDATE=%{_sbindir}/ntpdate \
%endif
	PATH_TO_RPCINFO=%{_sbindir}/rpcinfo \
	--with-ps-command="`which ps` -eo 's uid pid ppid vsz rss pcpu etime comm args'" \
	--with-ps-format='%s %d %d %d %d %d %f %s %s %n' \
	--with-ps-cols=10 \
	--with-ping-command='%{_bindir}/ping -n -U -w %d -c %d %s' \
	--with-ping6-command='%{_sbindir}/ping6 -n -U -w %d -c %d %s' \
	--enable-extra-opts \
	--with-ps-varlist='procstat,&procuid,&procpid,&procppid,&procvsz,&procrss,&procpcpu,procetime,procprog,&pos'

%make_build

%if 0%{?fromgit}
make THANKS
%endif

cd plugins-scripts
%make_build check_ntp
cd ..

cp %{SOURCE1} ./README.Fedora

%install
sed -i 's,^MKINSTALLDIRS.*,MKINSTALLDIRS = ../mkinstalldirs,' po/Makefile
%make_install AM_INSTALL_PROGRAM_FLAGS=""
install -m 0755 plugins-root/check_icmp %{buildroot}/%{_libdir}/nagios/plugins
install -m 0755 plugins-root/check_dhcp %{buildroot}/%{_libdir}/nagios/plugins
install -m 0755 plugins/check_ide_smart %{buildroot}/%{_libdir}/nagios/plugins
install -m 0755 plugins/check_ldap %{buildroot}/%{_libdir}/nagios/plugins
%if 0%{?fedora}
install -m 0755 plugins-scripts/check_ntp %{buildroot}/%{_libdir}/nagios/plugins/check_ntp.pl
%endif
## This is to fix https://bugzilla.redhat.com/show_bug.cgi?id=1664981 because they are installing the wrong thing
install -m 0755 plugins/check_ntp %{buildroot}/%{_libdir}/nagios/plugins/check_ntp
%if %{with radius}
install -m 0755 plugins/check_radius %{buildroot}/%{_libdir}/nagios/plugins
%endif
install -m 0755 plugins/check_pgsql %{buildroot}/%{_libdir}/nagios/plugins

%ifarch ppc ppc64 ppc64p7 sparc sparc64
rm -f %{buildroot}/%{_libdir}/nagios/plugins/check_sensors
%endif

chmod 644 %{buildroot}/%{_libdir}/nagios/plugins/utils.pm

%find_lang %{name}

%files -f %{name}.lang
%doc ACKNOWLEDGEMENTS AUTHORS po/ChangeLog CODING FAQ LEGAL NEWS README REQUIREMENTS SUPPORT THANKS README.Fedora
%license COPYING
%{_libdir}/nagios/plugins/negate
%{_libdir}/nagios/plugins/urlize
%{_libdir}/nagios/plugins/utils.sh

%files all

%files apt
%{_libdir}/nagios/plugins/check_apt

%files breeze
%{_libdir}/nagios/plugins/check_breeze

%files by_ssh
%{_libdir}/nagios/plugins/check_by_ssh

%files cluster
%{_libdir}/nagios/plugins/check_cluster

%if %{with libdbi}
%files dbi
%{_libdir}/nagios/plugins/check_dbi
%endif

%files dhcp
%defattr(4750,root,nagios,-)
%{_libdir}/nagios/plugins/check_dhcp

%files dig
%{_libdir}/nagios/plugins/check_dig

%files disk
%{_libdir}/nagios/plugins/check_disk

%files disk_smb
%{_libdir}/nagios/plugins/check_disk_smb

%files dns
%{_libdir}/nagios/plugins/check_dns

%files dummy
%{_libdir}/nagios/plugins/check_dummy

%files file_age
%{_libdir}/nagios/plugins/check_file_age

%files flexlm
%{_libdir}/nagios/plugins/check_flexlm

%files fping
%defattr(4750,root,nagios,-)
%{_libdir}/nagios/plugins/check_fping

%files game
%{_libdir}/nagios/plugins/check_game

%files hpjd
%{_libdir}/nagios/plugins/check_hpjd

%files http
%{_libdir}/nagios/plugins/check_http

%files icmp
%defattr(4750,root,nagios,-)
%{_libdir}/nagios/plugins/check_icmp

%files ifoperstatus
%{_libdir}/nagios/plugins/check_ifoperstatus

%files ifstatus
%{_libdir}/nagios/plugins/check_ifstatus

%files ide_smart
%defattr(4750,root,nagios,-)
%{_libdir}/nagios/plugins/check_ide_smart

%files ircd
%{_libdir}/nagios/plugins/check_ircd

%files ldap
%{_libdir}/nagios/plugins/check_ldap
%{_libdir}/nagios/plugins/check_ldaps

%files load
%{_libdir}/nagios/plugins/check_load

%files log
%{_libdir}/nagios/plugins/check_log

%files mailq
%{_libdir}/nagios/plugins/check_mailq

%files mrtg
%{_libdir}/nagios/plugins/check_mrtg

%files mrtgtraf
%{_libdir}/nagios/plugins/check_mrtgtraf

%files mysql
%{_libdir}/nagios/plugins/check_mysql
%{_libdir}/nagios/plugins/check_mysql_query

%files nagios
%{_libdir}/nagios/plugins/check_nagios

%files nt
%{_libdir}/nagios/plugins/check_nt

%files ntp
%{_libdir}/nagios/plugins/check_ntp
%{_libdir}/nagios/plugins/check_ntp_peer
%{_libdir}/nagios/plugins/check_ntp_time

%if 0%{?fedora}
%files ntp-perl
%{_libdir}/nagios/plugins/check_ntp.pl
%endif

%files nwstat
%{_libdir}/nagios/plugins/check_nwstat

%files oracle
%{_libdir}/nagios/plugins/check_oracle

%files overcr
%{_libdir}/nagios/plugins/check_overcr

%files perl
%{_libdir}/nagios/plugins/utils.pm

%files pgsql
%{_libdir}/nagios/plugins/check_pgsql

%files ping
%{_libdir}/nagios/plugins/check_ping

%files procs
%{_libdir}/nagios/plugins/check_procs

%if %{with radius}
%files radius
%{_libdir}/nagios/plugins/check_radius
%endif

%files real
%{_libdir}/nagios/plugins/check_real

%files remove_perfdata
%{_libdir}/nagios/plugins/remove_perfdata

%files rpc
%{_libdir}/nagios/plugins/check_rpc

%ifnarch ppc ppc64 ppc64p7 sparc sparc64
%files sensors
%{_libdir}/nagios/plugins/check_sensors
%endif

%files smtp
%{_libdir}/nagios/plugins/check_smtp

%files snmp
%{_libdir}/nagios/plugins/check_snmp

%files ssh
%{_libdir}/nagios/plugins/check_ssh

%files ssl_validity
%{_libdir}/nagios/plugins/check_ssl_validity

%files swap
%{_libdir}/nagios/plugins/check_swap

%files tcp
%{_libdir}/nagios/plugins/check_clamd
%{_libdir}/nagios/plugins/check_ftp
%{_libdir}/nagios/plugins/check_imap
%{_libdir}/nagios/plugins/check_jabber
%{_libdir}/nagios/plugins/check_nntp
%{_libdir}/nagios/plugins/check_nntps
%{_libdir}/nagios/plugins/check_pop
%{_libdir}/nagios/plugins/check_simap
%{_libdir}/nagios/plugins/check_spop
%{_libdir}/nagios/plugins/check_ssmtp
%{_libdir}/nagios/plugins/check_tcp
%{_libdir}/nagios/plugins/check_udp

%files time
%{_libdir}/nagios/plugins/check_time

%files ups
%{_libdir}/nagios/plugins/check_ups

%files uptime
%{_libdir}/nagios/plugins/check_uptime

%files users
%{_libdir}/nagios/plugins/check_users

%files wave
%{_libdir}/nagios/plugins/check_wave

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.9-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 28 2024 Guido Aulisi <guido.aulisi@gmail.com> - 2.4.9-1
- Update to 2.4.9

* Sat Mar 09 2024 Guido Aulisi <guido.aulisi@gmail.com> - 2.4.8-1
- Update to 2.4.8

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 06 2023 Michal Schorm <mschorm@redhat.com> - 2.4.6-2
- Build against the mariadb-connector-c-devel package

* Wed Aug 16 2023 Guido Aulisi <guido.aulisi@gmail.com> - 2.4.6-1
- Update to 2.4.6

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 03 2023 Guido Aulisi <guido.aulisi@gmail.com> - 2.4.4-1
- Update to 2.4.4

* Thu Apr 27 2023 Florian Weimer <fweimer@redhat.com> - 2.4.3-2
- Backport part of upstream patch to fix C99 compatibility issue

* Sun Mar 26 2023 Guido Aulisi <guido.aulisi@gmail.com> - 2.4.3-1
- Update to 2.4.3

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 27 2022 Guido Aulisi <guido.aulisi@gmail.com> - 2.4.0-6
- Obsolete nagios-plugins-dbi in F36+ and EL9+ (#2079243)

* Fri Jan 28 2022 Guido Aulisi <guido.aulisi@gmail.com> - 2.4.0-5
- Support ntpsec (upstream PR)

* Wed Jan 26 2022 Xavier Bachelot <xavier@bachelot.org> - 2.4.0-4
- Don't build radius plugin for EL9+

* Sat Jan 22 2022 Xavier Bachelot <xavier@bachelot.org> - 2.4.0-3
- Don't build dbi plugin for F36+ and EL9+

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Guido Aulisi <guido.aulisi@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.3.3-12
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Guido Aulisi <guido.aulisi@gmail.com> - 2.3.3-10
- Fix FTBFS on f35 and f34 (#1923642)
- Use license tag

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 2.3.3-9
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Martin Jackson <mhjacks@swbell.net> - 2.3.3-6
- Specify ping and ping6 commands

* Tue May 26 2020 Martin Jackson <mhjacks@swbell.net> - 2.3.3-5
- Correct spelling of dep for -all subpackage. BZ#1840031

* Sun May 24 2020 Martin Jackson <mhjacks@swbell.net> - 2.3.3-4
- Reinstate ssl_validity.  Packager overreacted.

* Tue May 19 2020 Martin Jackson <mhjacks@swbell.net> - 2.3.3-3
- Remove ssl_validity as perl-Convert-ASN1 has been retired.  BZ#1837397

* Thu Apr 9 2020 Martin Jackson <mhjacks@swbell.net> - 2.3.3-2
- Add ssl_validity to all plugins metapackage

* Sun Mar 15 2020 Martin Jackson <mhjacks@swbell.net> - 2.3.3-1
- New upstream version
- Remove reference to path10 which no longer is in the specfile

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Stephen Smoogen <smooge@fedoraproject.org> - 2.3.1-2
- Add in perl entries needed for perl oracle plugin to work.


* Tue Dec 10 2019 Stephen Smoogen <smooge@fedoraproject.org> - 2.3.1-1
- Make first attempt at making this work for 2.3.1
- Fix BZ#1768270
- Fix BZ#1752383
- Fix BZ#1781292

* Thu Sep 26 2019 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.2-2.20190926git1b8ad57
- Add conditional for perl-UTF8. Thanks to Todd Zullinger and Alexander Kohr
- Update to newer git tag to fix check_smb

* Sat Sep 21 2019 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.2-1.20190919git00cff01

- Update to 2.2.2 and update to latest patchset to fix things missed in 2.2.2

* Thu Aug 29 2019 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.1-17.20190829gitfb792ff
- Update to latest git and fix release string to match again
- check_ntp.pl was still getting installed as check_ntp. Fix BZ#1664981
- check_ntp.pl has ipv6 problem. Fix BZ#1731468

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-16.20180725git3429dad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.2.1-15.20180725git3429dad
- Update requirement for ps to procps
- Fix check_smtp certificate verification

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-15.20180725git3429dad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.2.1-16.20180725git3429dad
- Fix check_smtp certificate verification

* Thu Dec 13 2018 Patrick Uiterwijk <puiterwijk@puiterwijk.org> - 2.2.1-15.20180725git3429dad
- Add upstream PR #428 to add PROXY protocol support to check_smtp

* Wed Jul 25 2018 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.1-14.20180725git3429dad
- Update to latest git and fix release string to match
- Fix BZ#1604915
- Fix BZ#1579292
- Possibly fix BZ#1525609
- Possibly fix BZ#1518811
- Possibly fix BZ#1470823


* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Karsten Hopp <karsten@redhat.com> - 2.2.1-12
- fix conditionals
- include mysql_version for MYSQL_PORT macro
- fix perl shebang in plugin-scripts/check_ntp

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.2.1-10
- Rebuilt for switch to libxcrypt

* Tue Nov 21 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.1-9
- Fix mysql patch problem with <f26
- Fix BZ#1478721

* Tue Nov 21 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.1-8
- remove git from the release as it isn't standard
- Fix BZ#1512892
- Fix BZ#1512380
- Fix BZ#1500028
- Fix BZ#1494080
- Fix BZ#1478721

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.1-5git
- Try to make the logic so it works with mariadb and mysql
- Fail. revert that part.

* Fri Jul 14 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.1-4git
- Add explicit file require. Fix BZ# 1470823
- Add explicit file require. Fix BZ# 1471007
- Add explicit file require. Fix BZ# 1471012

* Wed Jul 12 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.1-3git
- Updated patches to fix check_http problems

* Mon Jul  3 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.1-2git
- Update to git for 20170703

* Thu Apr 20 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.1-1
- New version of plugins. Remove old patches

* Wed Mar 22 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.0-8
- Bump the release number to have a working version in rawhide due to rpm bug.

* Sun Mar 12 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.0-7
- Fix the patch order to get the code working again.
- get final fix from patrick for check_http header problem

* Fri Mar 10 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.0-6
- Consolidate the patches from patrick and git 

* Tue Mar 07 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.2.0-5
- Add patch for check_http to not choke

* Sat Feb 25 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.0-4
- OK so it turns out writing to a non initialized pointer is bad. mmmkay.

* Sat Feb 25 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.0-3
- Try to put in a logic fix for http. It gives answer expected but may not work for upstream

* Sat Feb 25 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.0-2
- My patch to clean up code broke TXT records because they need to go back one char in the c-string array. 

* Fri Feb 24 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- Add fix for MX to match old 2.0.3 MX
- Remove patches that were incorporated into 2.2.0
- Remove autoconf patch for openssl110 

* Thu Feb 16 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.1.4-7
- Got feedback on bz 1422993. Put in fix from github

* Thu Feb 16 2017 Stephen Smoogen <smooge@fedoraproject.org> - 2.1.4-6
- Start collecting and fixing bugzilla reports. This one fixes ipv6 for check_snmp

* Wed Feb 15 2017 Stephen Smoogen <smooge@redhat.com> - 2.1.4-5
- Grab other fixes from git maintenance branch to fix other check_ problems
- Fix autoconf/automake so that it works with openssl 1.1.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Stephen Smoogen <smooge@redhat.com> - 2.1.4-3
- Put in patch to fix check_file_age

* Fri Dec 16 2016 Scott Wilkerson <swilkerson@nagios.com> 2.1.4-1
- Updated to 2.1.4

* Thu Feb 04 2016 Scott Wilkerson <swilkerson@nagios.com> 2.1.1-1
- Updated to 2.1.1
- Fixes bug #1191896

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Scott Wilkerson <swilkerson@nagios.com> 2.0.3-3
- Fix issue where check_mysql was looking in wrong place for my.cnf
- Fixes bug #1256731

* Thu Aug 27 2015 Kevin Fenzi <kevin@scrye.com> 2.0.3-2
- Add obsoletes for nagios-plugin-linux_raid < 1.4.3-11
- Fixes bug #1256682

* Tue Aug 04 2015 Josh Boyer <jwboyer@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 1 2014 Sam Kottler <skottler@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1
- Moved SSD-specific patch which landed upstream
- Update patch to binary paths in plugins-scripts/check_log.sh so it applies
- Add -uptime subpackage

* Thu Oct 24 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.5-2
- New check_dbi plugin (BR: libdbi-devel; subpackage: nagios-plugins-dbi)

* Wed Oct 23 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.5-1
- Update to version 1.5
- New project homepage and source download locations
- Disabled patches 1, 6, 8, and 9.
- No linux_raid subpackage (the contrib directory was removed)

* Wed Oct 16 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.4.16-10
- Remove EL4 and EL5 support
- Backport patches to fix check_linux_raid in case of resyncing (rhbz #504721)
- Fix smart attribute comparison (rhbz #913085)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.4.16-8
- Perl 5.18 rebuild

* Wed May 22 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.16-7
- Build package with PIE flags (#965536)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 17 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.16-5
- Fix the use lib statement and the external ntp commands paths in check-ntp.pl
  (nagios-plugins-0008-ntpdate-and-ntpq-paths.patch).

* Thu Aug 16 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.16-4
- Remove the erroneous requirements of nagios-plugins-ntp (#848830)
- Ship check-ntp.pl in the new nagios-plugins-ntp-perl subpackage (#848830)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  9 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.16-2
- Provides bundled(gnulib) (#821779)

* Mon Jul  9 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.16-1
- Update to version 1.4.16
- Dropped nagios-plugins-0005-Patch-for-check_linux_raid-with-on-linear-raid0-arra.patch
  (upstream).

* Tue Jun 26 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.15-7
- glibc 2.16 no longer defines gets for ISO C11, ISO C++11, and _GNU_SOURCE
  (#835621): nagios-plugins-0007-undef-gets-and-glibc-2.16.patch

* Tue Jun 26 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.15-6
- The nagios-plugins RPM no longer needs to own the /usr/lib{,64}/nagios/plugins
  directory; this directory is now owned by nagios-common (#835621)
- Small updates (clarification) to the file nagios-plugins.README.Fedora

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.4.15-4
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct  7 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.15-2
- Dropped check_udp sub-package (see rhbz #634067). Anyway it
  provided just a symlink to check_tcp.
- Fixed weird issue with check_swap returning ok in case of
  missing swap (see rhbz #512559).

* Wed Aug 18 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.15-1
- Ver. 1.4.15
- Dropped patch for restoration of behaviour in case of ssl checks

* Tue May 18 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.14-4
- Restore ssl behaviour for check_http in case of self-signed
  certificates (see rhbz #584227).

* Sat Apr 24 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.14-3
- Removed Requires - nagios (see rhbz #469530).
- Added "Requires,Requires(pre): group(nagios)" where necessary
- Sorted %%files sections
- No need to ship INSTALL file
- Added more doc files to main package

* Mon Apr 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.14-2
- Added missing Requires - nagios (see rhbz #469530).
- Fixed path to qstat -> quakestat (see rhbz #533777)
- Disable radius plugin for EL4 - there is not radiuscleint-ng for EL-4

* Wed Mar 10 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4.14-1
- Ver. 1.4.14
- Rebased patches.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.4.13-17
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Mike McGrath <mmcgrath@redhat.com> - 1.4.13-15
- Added patch from upstream to fix ntp faults (bz #479030)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Caolán McNamara <caolanm@redhat.com> 1.4.13-13
- rebuild for dependencies

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 1.4.13-12
- rebuild with new openssl

* Mon Oct 20 2008 Robert M. Albrecht <romal@gmx.de> 1.4.13-11
- Enabled --with-extra-opts again

* Mon Oct 20 2008 Robert M. Albrecht <romal@gmx.de> 1.4.13-10
- removed provides perl plugins Bugzilla 457404

* Thu Oct 16 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-9
- This is a "CVS is horrible" rebuild

* Thu Oct  9 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-8
- Rebuilt with a proper patch

* Wed Oct  8 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-7
- Added changed recent permission changes to allow nagios group to execute

* Wed Oct  8 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-6
- Fixed up some permission issues

* Mon Oct  6 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-5
- Fixing patch, missing semicolon

* Sun Sep 28 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-4
- Upstream released new version #464419
- Added patch fix for check_linux_raid #253898
- Upstream releases fix for #451015 - check_ntp_peers
- Upstream released fix for #459309 - check_ntp
- Added Provides Nagios::Plugins for #457404
- Fixed configure line for #458985 check_procs

* Thu Jul 10 2008 Robert M. Albrecht <romal@gmx.de> 1.4.12-3
- Removed --with-extra-opts, does not build in Koji

* Mon Jun 30 2008 Robert M. Albrecht <romal@gmx.de> 1.4.12-2
- Enabled --with-extra-opts

* Sun Jun 29 2008 Robert M. Albrecht <romal@gmx.de> 1.4.12-1
- Upstream released version 1.4.12
- Removed patches ping_timeout.patch and pgsql-fix.patch

* Wed Apr 30 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.11-4
- added patch for check_pgsql

* Wed Apr 09 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.11-2
- Fix for 250588

* Thu Feb 28 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.11-1
- Upstream released version 1.4.11
- Added check_ntp peer and time

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.10-6
- Autorebuild for GCC 4.3

* Tue Feb 12 2008 Mike McGrath <mmcgrath@redhat.com> 1.4-10-5
- Rebuild for gcc43

* Thu Jan 10 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.10-4
- Fixed check_log plugin #395601

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.4.10-2
- Rebuild for deps

* Thu Dec 06 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.10-1
- Upstream released new version
- Removed some patches

* Fri Oct 26 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-9
- Fix for Bug 348731 and CVE-2007-5623

* Wed Aug 22 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-7
- Rebuild for BuildID
- License change

* Fri Aug 10 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-6
- Fix for check_linux_raid - #234416
- Fix for check_ide_disk - #251635

* Tue Aug 07 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-2
- Fix for check_smtp - #251049

* Fri Apr 13 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-1
- Upstream released new version

* Fri Feb 23 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.6-1
- Upstream released new version

* Sun Dec 17 2006 Mike McGrath <imlinux@gmail.com> 1.4.5-1
- Upstream released new version

* Fri Oct 27 2006 Mike McGrath <imlinux@gmail.com> 1.4.4-2
- Enabled check_smart_ide
- Added patch for linux_raid
- Fixed permissions on check_icmp

* Tue Oct 24 2006 Mike McGrath <imlinux@gmail.com> 1.4.4-1
- Upstream new version
- Disabled check_ide_smart (does not compile cleanly/too lazy to fix right now)
- Added check_apt

* Sun Aug 27 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-18
- Removed utils.pm from the base nagios-plugins package into its own package

* Tue Aug 15 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-17
- Added requires qstat for check_game

* Thu Aug 03 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-16
- Providing path to qstat

* Thu Aug 03 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-15
- Fixed permissions on check_dhcp
- Added check_game
- Added check_radius
- Added patch for ntp

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-14
- Patched upstream issue: 196356

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-13
- nagios-plugins-all now includes nagios-plugins-mysql

* Thu Jun 22 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-12
- removed sensors support for sparc and sparc64

* Thu Jun 22 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-11
- Created a README.Fedora explaining how to install other plugins

* Sun Jun 11 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-9
- Removed check_sensors in install section

* Sat Jun 10 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-8
- Inserted conditional blocks for ppc exception.

* Wed Jun 07 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-7
- Removed sensors from all plugins and added excludearch: ppc

* Tue Jun 06 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-6
- For ntp plugins requires s/ntpc/ntpdc/

* Sat Jun 03 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-5
- Fixed a few syntax errors and removed an empty export

* Fri May 19 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-4
- Now using configure macro instead of ./configure
- Added BuildRequest: perl(Net::SNMP)
- For reference, this was bugzilla.redhat.com ticket# 176374

* Fri May 19 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-3
- Added check_ide_smart
- Added some dependencies
- Added support for check_if* (perl-Net-SNMP now in extras)
- nagios-plugins now owns dir %%{_libdir}/nagios

* Sat May 13 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-2
- Added a number of requires that don't get auto-detected

* Sun May 07 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-1
- Upstream remeased 1.4.3

* Tue Apr 18 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-9
- Fixed a typo where nagios-plugins-all required nagios-plugins-httpd

* Mon Mar 27 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-8
- Updated to CVS head for better MySQL support

* Sun Mar 5 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-7
- Added a nagios-plugins-all package

* Wed Feb 1 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-6
- Added provides for check_tcp

* Mon Jan 30 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-5
- Created individual packages for all check_* scripts

* Tue Dec 20 2005 Mike McGrath <imlinux@gmail.com> 1.4.2-4
- Fedora friendly spec file

* Mon May 23 2005 Sean Finney <seanius@seanius.net> - cvs head
- just include the nagios plugins directory, which will automatically include
  all generated plugins (which keeps the build from failing on systems that
  don't have all build-dependencies for every plugin)

* Thu Mar 04 2004 Karl DeBisschop <karl[AT]debisschop.net> - 1.4.0alpha1
- extensive rewrite to facilitate processing into various distro-compatible specs

* Thu Mar 04 2004 Karl DeBisschop <karl[AT]debisschop.net> - 1.4.0alpha1
- extensive rewrite to facilitate processing into various distro-compatible specs

