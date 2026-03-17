%global _hardened_build 1

Name:           darkhttpd
Version:        1.17
Release:        %autorelease
Summary:        Secure, lightweight, fast, single-threaded HTTP/1.1 server
License:        BSD-2-Clause
URL:            https://github.com/emikulic/darkhttpd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        darkhttpd.service
Source2:        darkhttpd.sysconfig

BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
Requires:       /etc/mime.types

%description
darkhttpd is a secure, lightweight, fast and single-threaded HTTP/1.1 server.

Features:
* Simple to set up:
* Single binary, no other files.
* Standalone, doesn't need inetd or ucspi-tcp.
* No messing around with config files.
* Written in C - efficient and portable.
* Small memory footprint.
* Event loop, single threaded - no fork() or pthreads.
* Generates directory listings.
* Supports HTTP GET and HEAD requests.
* Supports Range / partial content.
* Supports If-Modified-Since.
* Supports Keep-Alive connections.
* Can serve 301 redirects based on Host header.
* Uses sendfile().

Security:
* Can log accesses, including Referer and User-Agent.
* Can chroot.
* Can drop privileges.
* Impervious to /../ sniffing.
* Times out idle connections.
* Drops overly long requests.

Limitations:
* This server only serves static content - *NO* CGI supported!

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}"

%install
install -pDm755 %{name} %{buildroot}%{_sbindir}/%{name}
install -pDm644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -pDm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -pDm644 COPYING %{buildroot}%{_licensedir}/%{name}

%post
%systemd_post darkhttpd.service

%preun
%systemd_preun darkhttpd.service

%postun
%systemd_postun_with_restart darkhttpd.service

%files
%license %{_licensedir}/%{name}
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog
