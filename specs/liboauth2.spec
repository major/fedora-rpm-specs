Name: liboauth2
Version: 2.0.0
Release: 2%{?dist}
Summary: Generic library to build OAuth 2.x and OpenID Connect servers and clients in C
License: Apache-2.0
URL: https://github.com/OpenIDC/liboauth2
Source0: https://github.com/OpenIDC/liboauth2/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: automake
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: httpd-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: check
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(cjose)
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(libcurl)
## BUG RHBZ#2307714 - libcurl-devel has incomplete requires
BuildRequires: openldap-devel
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: gdb-minimal

%description
liboauth2 library provides primitives to create OAuth 2.x and OpenID Connect
servers and clients

%package devel
Summary: Library to build OAuth 2.x and OpenID Connect servers and clients in C
License: Apache-2.0
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
liboauth2 library provides primitives to create OAuth 2.x and OpenID Connect
servers and clients.

%package apache
Summary: OAuth 2.x and OpenID Connect library integration to Apache
License: Apache-2.0
Requires: %{name}%{?_isa} = %{version}-%{release}

%description apache
OAuth 2.x and OpenID Connect library integration to Apache web server

%package apache-devel
Summary: Development components to build Apache module with liboauth2 library
License: Apache-2.0
Requires: %{name}-apache%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description apache-devel
Development components to build Apache module with liboauth2 library

%prep
%autosetup -p1 -n liboauth2-%{version}

%build
autoreconf -ivf
%configure --with-apache --without-redis --without-memcache
%make_build

%check
%make_build check

%install
%make_install
# Don't install static libraries and .la files
rm -vf %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/*.a
find %{buildroot}%{_includedir}/oauth2 -name '*.h' | grep -v apache | sed 's@%{buildroot}@@g' > file.headers

%files devel -f file.headers
%dir %{_includedir}/oauth2
%{_libdir}/pkgconfig/liboauth2.pc
%{_libdir}/liboauth2.so

%files
%{_libdir}/liboauth2.so.0
%{_libdir}/liboauth2.so.0.0.0
%license LICENSE
%doc README.md

%files apache
%{_libdir}/liboauth2_apache.so.0
%{_libdir}/liboauth2_apache.so.0.0.0

%files apache-devel
%{_includedir}/oauth2/apache.h
%{_libdir}/pkgconfig/liboauth2_apache.pc
%{_libdir}/liboauth2_apache.so


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 24 2024 Packit <hello@packit.dev> - 2.0.0-1
- Update to version 2.0.0
- License changed to Apache-2.0 by upstream in version 2.0.0
- Upstream moved to https://github.com/OpenIDC/liboauth2
- Resolves: rhbz#2307691

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.3-2
- convert license to SPDX

* Tue Jun 25 2024 Packit <hello@packit.dev> - 1.6.3-1
- Update to version 1.6.3
- Resolves: rhbz#2294261

* Wed Jun 5 2024 Packit <hello@packit.dev> - 1.6.2-1
- Update to version 1.6.2
- Resolves: rhbz#2290605

* Tue Mar 12 2024 Packit <hello@packit.dev> - 1.6.1-1
- release 1.6.1 (Hans Zandbelt)
- add Mutual-TLS Certificate-Bound Access Tokens support to NGINX (Hans Zandbelt)
- add support for Redis 6 ACL username based authentication (Hans Zandbelt)
- update copyright year to 2024 (Hans Zandbelt)
- Resolves rhbz#2269222

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 7 2023 Packit <hello@packit.dev> - 1.6.0-1
- 1.6.0: use libcurl version macro that works on older platforms (Hans Zandbelt)
- 1.6.0: add support for the OAuth 2.0 Client Credentials grant type (Hans Zandbelt)
- Use CURLOPT_REDIR_PROTOCOLS_STR when curl >= 7.85.0 (Nicolas Mora)
- Resolves rhbz#2253482

* Fri Nov 10 2023 Packit <hello@packit.dev> - 1.5.2-1
- 1.5.2: update DPoP support to RFC 9449 (Hans Zandbelt)
- printout more cjose error details in JWT access token verification (Hans Zandbelt)
- fix timing issue in check_openidc.c; closes #47 (Hans Zandbelt)
- Resolves rhbz#2248991

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Packit <hello@packit.dev> - 1.5.1-1
- fix pcre2-8 dependency
- add END_TEST to test_openidc_resolver_url (Hans Zandbelt)
- release 1.5.1 (Hans Zandbelt)
- oops: copy/paste omisson for oauth2_jose_jwt_verify_ctx iat_validate (Hans Zandbelt)
- avoid memory leak and fix check_oauth2 (Hans Zandbelt)
- add issuer validation for JWT access tokens (Hans Zandbelt)
- add support for resolving provider metadata from a Discovery endpoint (Hans Zandbelt)
- add error logs about missing or invalid "active" boolean claim (Hans Zandbelt)
- update eclipse .cproject (Hans Zandbelt)
- update cjose link; see #43; thanks @compoundradius (Hans Zandbelt)
- move repo to OpenIDC github organization (Hans Zandbelt)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Alexander Bokovoy <abokovoy@redhat.com> - 1.4.4-1
- New upstream release 1.4.4
- allow build against OpenSSL 3.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.4.2-4
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Alexander Bokovoy <abokovoy@redhat.com> 1.4.2-2
- Re-enable tests on ARMv7

* Tue May 25 2021 Alexander Bokovoy <abokovoy@redhat.com> 1.4.2-1
- New upstream release 1.4.2
- Fix unaligned memory access on ARMv7

* Mon Apr 19 2021 Alexander Bokovoy <abokovoy@redhat.com> 1.4.1-2
- Fedora packaging review updates

* Sat Apr 17 2021 Alexander Bokovoy <abokovoy@redhat.com> 1.4.1-1
- Initial package
