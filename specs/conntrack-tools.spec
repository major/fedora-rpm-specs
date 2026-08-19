Name:           conntrack-tools
Version:        1.4.9
Release:        %autorelease
Summary:        Manipulate netfilter connection tracking table and run High Availability
License:        GPL-2.0-only
URL:            http://conntrack-tools.netfilter.org/
Source0:        https://www.netfilter.org/pub/conntrack-tools/conntrack-tools-%{version}.tar.xz
Source1:        https://www.netfilter.org/pub/conntrack-tools/conntrack-tools-%{version}.tar.xz.sig
Source2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt
Source3:        conntrackd.service
Source4:        conntrackd.conf

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires: gnupg2
BuildRequires:  libnfnetlink-devel >= 1.0.1, libnetfilter_conntrack-devel >= 1.1.1
BuildRequires:  libnetfilter_cttimeout-devel >= 1.0.0, libnetfilter_cthelper-devel >= 1.0.0
BuildRequires:  libmnl-devel >= 1.0.3, libnetfilter_queue-devel >= 1.0.2
BuildRequires:  libtirpc-devel systemd-devel
BuildRequires:  pkgconfig bison flex
Provides:       conntrack = 1.0-1
Obsoletes:      conntrack < 1.0-1
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd
BuildRequires: make

%description
With conntrack-tools you can setup a High Availability cluster and
synchronize conntrack state between multiple firewalls.

The conntrack-tools package contains two programs:
- conntrack: the command line interface to interact with the connection
             tracking system.
- conntrackd: the connection tracking userspace daemon that can be used to
              deploy highly available GNU/Linux firewalls and collect
              statistics of the firewall use.

conntrack is used to search, list, inspect and maintain the netfilter
connection tracking subsystem of the Linux kernel.
Using conntrack, you can dump a list of all (or a filtered selection  of)
currently tracked connections, delete connections from the state table,
and even add new ones.
In addition, you can also monitor connection tracking events, e.g.
show an event message (one line) per newly established connection.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static --enable-systemd
%make_build
chmod 644 doc/sync/primary-backup.sh
rm -f doc/sync/notrack/conntrackd.conf.orig doc/sync/alarm/conntrackd.conf.orig doc/helper/conntrackd.conf.orig

%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
mkdir -p %{buildroot}%{_sysconfdir}/conntrackd
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/conntrackd/

%files
%license COPYING
%doc AUTHORS TODO doc
%dir %{_sysconfdir}/conntrackd
%config(noreplace) %{_sysconfdir}/conntrackd/conntrackd.conf
%{_unitdir}/conntrackd.service
%{_sbindir}/conntrack
%{_sbindir}/conntrackd
%{_sbindir}/nfct
%{_mandir}/man5/*
%{_mandir}/man8/*
%dir %{_libdir}/conntrack-tools
%{_libdir}/conntrack-tools/*

%post
%systemd_post conntrackd.service

%preun
%systemd_preun conntrackd.service

%postun
%systemd_postun conntrackd.service

%changelog
%autochangelog
