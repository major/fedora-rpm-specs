%global _hardened_build 1

Name:           darkhttpd
Version:        1.16
Release:        3%{?dist}
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
%systemd_post %{S:1}

%preun
%systemd_preun %{S:1}

%postun
%systemd_postun_with_restart %{S:1}

%files
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sbindir}/%{name}
%config %{_unitdir}/%{name}.service

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.16-2
- convert license to SPDX

* Thu Jul 18 2024 Filipe Rosset <rosset.filipe@gmail.com> - 1.16-1
- Update to 1.16 fixes rhbz#2259096

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 18 2022 Filipe Rosset <rosset.filipe@gmail.com> - 1.14-1
- Update to 1.14.0 fixes rhbz#2131519

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.13-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Sun Feb 21 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.13-1
- Update to latest upstream release 1.13 (#1931188)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.12-3
- Rebuilt to fix FTBFS rhbz#1423324

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 11 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.12-1
- Update to latest upstream release 1.12

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 17 2015 Christopher Meng <rpm@cicku.me> - 1.11-1
- Update to 1.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Christopher Meng <rpm@cicku.me> - 1.10-1
- Update to 1.10

* Tue Mar 25 2014 Christopher Meng <rpm@cicku.me> - 1.9-5
- Harden rebuild.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Christopher Meng <rpm@cicku.me> - 1.9-3
- Fix systemd support.

* Wed May 22 2013 Christopher Meng <rpm@cicku.me> - 1.9-2
- Add systemd support.

* Wed May 01 2013 Christopher Meng <rpm@cicku.me> - 1.9-1
- Initial Package.
