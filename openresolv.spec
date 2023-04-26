#
# spec file for package openresolv
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%global manext .gz
%global forgeurl0 https://github.com/NetworkConfiguration/openresolv

Name:           openresolv
Version:        3.13.1
Release:        %autorelease
Summary:        DNS management framework
License:        BSD
URL:            https://roy.marples.name/projects/openresolv
VCS:            git:%{forgeurl0}
Source0:        %{forgeurl0}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{forgeurl0}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xa785ed2755955d9e93ea59f6597f97ea9ad45549#/roy.marples.asc
Requires:       bash
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  gnupg2
Provides:       resolvconf = %{version}-%{release}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description
/etc/resolv.conf is a file that holds the configuration for the local resolution of domain names.
Normally this file is either static or maintained by a local daemon, normally a DHCP daemon.
openresolv will make sure, that multiple processes (eg. dhcpcd, NetworkManager, openvpn)
can write the resolv.conf without overwriting each others changes.

openresolv can generate a combined resolv.conf or a configuration file for a local nameserver
(like unbound, dnsmasq or bind) that will route the dns requests according to the search domain.

%prep
%if 0%{?fedora} || 0%{?rhel} > 8
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif

%autosetup
for F in *.in; do
  [ "$F" != "resolvconf.in" ] && sed -i -e '1 s,^#!/bin/sh$,#,' $F
done

%build
# not GNU autoconf
./configure --bindir=%{_sbindir} --libexecdir=%{_prefix}/lib/resolvconf
%make_build

%install
%make_install
mv %{buildroot}%{_sbindir}/resolvconf{,.%{name}}
mv %{buildroot}%{_mandir}/man8/resolvconf{,.%{name}}.8
touch %{buildroot}%{_sbindir}/resolvconf %{buildroot}%{_mandir}/man8/resolvconf.8%{?manext}

%post
%{_sbindir}/update-alternatives \
  --install %{_sbindir}/resolvconf resolvconf %{_sbindir}/resolvconf.%{name} 30 \
  --slave %{_mandir}/man8/resolvconf.8%{?manext} resolvconf.8%{?manext} %{_mandir}/man8/resolvconf.%{name}.8%{?manext}

%postun
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove resolvconf %{_sbindir}/resolvconf.%{name}
fi

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/resolvconf.conf
%dir %{_prefix}/lib/resolvconf
%{_prefix}/lib/resolvconf/*
%{_sbindir}/resolvconf.%{name}
%{_mandir}/man5/resolvconf.conf.5*
%{_mandir}/man8/resolvconf.%{name}.8*
%ghost %{_sbindir}/resolvconf
%ghost %{_mandir}/man8/resolvconf.8*

%changelog
%autochangelog
