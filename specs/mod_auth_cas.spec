%global commit be1e01ea173defc9837bd1b90dc72ed63c8131e7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mod_auth_cas
Version:        1.2
Release:        10%{?dist}
Summary:        Apache CAS Authentication Module for the JASIG/Apereo CAS Server

License:        Apache-2.0
URL:            https://github.com/apereo/mod_auth_cas
Source0:        https://github.com/apereo/mod_auth_cas/archive/%{commit}/%{name}-v%{version}.tar.gz
Source1:        auth_cas_mod.conf
Source2:        auth_cas_httpd.conf

BuildRequires:  openssl-devel
BuildRequires:  httpd-devel
BuildRequires:  m4, readline-devel, autoconf, automake
BuildRequires:  libcurl-devel
BuildRequires:  libtool
# Created issue with upstream https://github.com/apereo/mod_auth_cas/issues/208
BuildRequires:  pcre2-devel
BuildRequires:  gcc

Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       mod_ssl

%description
The purpose of this module is to allow an Apache web server to interact
with an authentication server that conforms to the CAS version 1 or 2
protocol or SAML protocol as used by the JASIG/Apereo CAS Server

%prep
%autosetup -p1 -n mod_auth_cas-%{commit}

%build
autoreconf -vif #BZ926155 - support aarch64
%configure --with-apxs=%{_httpd_apxs}
%make_build

%install
%make_install
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}/10-auth_cas.conf
install -Dp -m 644 %{SOURCE2} %{buildroot}%{_httpd_confdir}/auth_cas.conf

mkdir -p %{buildroot}%{_localstatedir}/cache/httpd/%{name}

%files
%doc README
%{_libdir}/httpd/modules/mod_auth_cas.so
%config(noreplace) %{_httpd_confdir}/auth_cas.conf
%config(noreplace) %{_httpd_modconfdir}/10-auth_cas.conf

%dir %attr(-,apache,apache) %{_localstatedir}/cache/httpd/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 20 2024 Scott Williams <vwbusguy@fedoraproject.org> - 1.2-8
- Rebase to upstream be1e01ea173defc9837bd1b90dc72ed63c8131e7
- Remove patches that were merged upstream
- BZ2249532 - Fix tilde operator

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 14 2023 Scott Williams <vwbusguy@fedoraproject.org> - 1.2-4
- Patch whitespace in spec file
- Fix syntax for applying patches during rpm build
- Bump BuildRequires to use pcre2-devel

* Tue Mar 14 2023 Tim Hansen <timhansen46@fedoraproject.org> - 1.2-3
- Add patches for pending upstream pull requests.

* Tue Mar 07 2023 Tim Hansen <timhansen46@fedoraproject.org> - 1.2-2
- spec file modernization

* Tue Mar 02 2021 Scott Williams <vwbusguy@fedoraproject.org> - 1.2-1
- Version bump to v1.2 and support for EL8

* Fri Sep 02 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-3
- Fix /var/cache/httpd/mod_auth_cas directory ownership (BZ#1368448)

* Fri Sep 02 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-2
- Fix EPEL6 conditionals for 1.1 update

* Thu Jun 16 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-1
- Update to latest stable upstream

* Wed May 11 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-0.2.rc3
- Update refs to apache versions
- Fix entry module conf in _httpd_modconfdir
- Add conf to _httpd_confdir
- Add cachedir

* Tue May 10 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-0.1.rc3
- Pull in latest RC from upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Adam Miller <maxamillion@fedoraproject.org> - 1.0.9.1-1
- Update to latest upstream.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-8
- BZ926155 - support aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Joe Orton <jorton@redhat.com> - 1.0.8.1-5
- update packaging (#803065)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 29 2010 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-2
- Fixed svn export link, upstream changed canonical URL names.

* Wed Apr 28 2010 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-1
- added requires of httpd
- fixed mixed use of macros
- updated to latest version

* Fri Aug 07 2009 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8-1
- First attempt to package mod_auth_cas for Fedora
