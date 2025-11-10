%global _hardened_build 1

Name:           darkhttpd
Version:        1.17
Release:        %autorelease
Summary:        Secure, lightweight, fast, single-threaded HTTP/1.1 server
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/emikulic/darkhttpd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysconfig
BuildRequires:  gcc
BuildRequires:  systemd
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
%{__cc} %{optflags} darkhttpd.c -o %{name} %{?__global_ldflags}

%install
install -pDm755 %{name} %{buildroot}%{_sbindir}/%{name}
install -pDm644 %{S:1} %{buildroot}%{_unitdir}/%{name}.service
install -pDm644 %{S:2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%post
%systemd_post darkhttpd.service

%preun
%systemd_preun darkhttpd.service

%postun
%systemd_postun_with_restart darkhttpd.service

%files
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog
