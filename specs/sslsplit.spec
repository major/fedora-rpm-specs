Summary: Transparent and scalable SSL/TLS interception
Name: sslsplit
Version: 0.5.5
Release: %autorelease
# Automatically converted from old format: BSD - review is highly recommended.
License: BSD-2-Clause
Url: http://www.roe.ch/SSLsplit
Source: http://mirror.roe.ch/rel/sslsplit/sslsplit-%{version}.tar.bz2

# https://github.com/droe/sslsplit/commit/e17de8454a65d2b9ba432856971405dfcf1e7522
#Patch1: sslsplit-0.5.5-openssl3.patch
# Patch the devel branch into the latest release since upstream isn't releasing
# and we need build system fixes anyway. This includes the openssl3 patch.
Patch1: sslsplit-0.5.5-develop20260512.patch

BuildRequires: make
Buildrequires: libevent-devel, openssl-devel, check-devel gcc
%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif
Buildrequires: libpcap-devel libnet-devel
Requires: iptables, iproute

%description
SSLsplit is a tool for man-in-the-middle attacks against SSL/TLS encrypted
network connections. Connections are transparently intercepted through a
network address translation engine and redirected to SSLsplit. SSLsplit
terminates SSL/TLS and initiates a new SSL/TLS connection to the original
destination address, while logging all data transmitted. SSLsplit is
intended to be useful for network forensics and penetration testing.

It uses Linux netfilter REDIRECT and TPROXY

%prep
%setup -q
%autopatch -p1

%build
%make_build

%check
# Requires a network connection
# make test

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1/
cp -a %{name} %{buildroot}%{_bindir}
cp -a %{name}.1  %{buildroot}%{_mandir}/man1/

%files
%attr(0755,root,root) %{_bindir}/%{name}
%doc *.md
%{_mandir}/*/*

%changelog
%autochangelog
