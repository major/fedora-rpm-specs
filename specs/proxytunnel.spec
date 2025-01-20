Name:           proxytunnel
Version:        1.10.20200907
Release:        13%{?dist}
Summary:        Tool to tunnel a connection through an standard HTTP(S) proxy

# Automatically converted from old format: GPLv2+ and BSD and MIT - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            https://github.com/proxytunnel/proxytunnel
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  xmlto

%description
ProxyTunnel is a program that connects stdin and stdout to a server somewhere 
on the network, through a standard HTTPS proxy. We mostly use it to tunnel SSH
sessions through HTTP(S) proxies.
Proxytunnel can currently do the following:
* Create tunnels using HTTP and HTTPS proxies (That understand the HTTP 
  CONNECT command).
* Work as a back-end driver for an OpenSSH client, and create SSH
  connections through HTTP(S) proxies.
* Work as a stand-alone application, listening on a port for connections, 
  and then tunneling these connections to a specified destination. 

%prep
%autosetup
# Fix permissions
chmod -c 644 CHANGES
# Convert docs to UTF-8
for f in CHANGES; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.tmp
    touch -r $f $f.tmp
    mv -f $f.tmp $f
done

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install prefix=%{_prefix} DESTDIR=%{buildroot}

%files
%doc CHANGES CREDITS KNOWN_ISSUES README.md TODO
%license LICENSE.txt
%{_bindir}/proxytunnel
%{_mandir}/man1/proxytunnel.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20200907-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.20200907-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20200907-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20200907-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20200907-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20200907-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20200907-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20200907-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20200907-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.10.20200907-4
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20200907-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20200907-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.20200907
- Remove patches
- Remove outdated docs
- Update to latest upstream release 1.10.20200907 (rhbz#1880084)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Paul Howarth <paul@city-fan.org> - 1.9.1-10
- Fix FTBFS with GCC 10 (https://github.com/proxytunnel/proxytunnel/pull/43)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul  4 2018 Paul Howarth <paul@city-fan.org> - 1.9.1-6
- Switch upstream to github
- Use %%license where possible
- Drop %%defattr, redundant since rpm 4.4
- Drop buildroot cleaning in %%install section
- Drop legacy Group: tag

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 31 2016 Paul Howarth <paul@city-fan.org> - 1.9.1-1
- Update to 1.9.1
  - Switch to HTTP/1.1 commands, so we can tunnel over JoikuSpot's which don't
    understand http/1.0 command
  - NTLMv2 fixes
- Add TLS support (#1284776)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 09 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.9.0-4
- Fix Source0
- Fix man dir

* Wed Apr 07 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.9.0-3
- Fix the license

* Sat Mar 13 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.9.0-2
- Fix the summary
- Replace generally useful macros by regular commands
- Preserve timestamps of documentation files

* Thu Feb 11 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 1.9.0-1
- Initial package build

