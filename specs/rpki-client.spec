%if 0%{?with_snapshot}
%global gitdate              20220207
%global portable_commit      20d0b2306452fedf56b8487e517a59848d246eea
%global portable_shortcommit %(c=%{portable_commit}; echo ${c:0:7})
%global openbsd_commit       0c3ff93cf8e4880e3099a7bbee8956929fd6ceb2
%global openbsd_shortcommit  %(c=%{openbsd_commit}; echo ${c:0:7})
%endif

Summary:        OpenBSD RPKI validator to support BGP Origin Validation
Name:           rpki-client
Version:        9.4
Release:        1%{?with_snapshot:.git%{gitdate}}%{?dist}
# rpki-client itself is ISC but uses other source codes, breakdown:
# BSD-2-Clause: include/sys/tree.h and src/{http,output}.c
# BSD-3-Clause: compat/{setproctitle,vis}.c and include/{sha2_openbsd,vis,sys/queue}.h and src/mkdir.c
# OpenSSL: compat/x509_purp.c
# LicenseRef-Fedora-Public-Domain: include/{{poll,sha2,stdlib,string,unistd},openssl/{asn1,safestack,x509v3}}.h
#                                  and include/sys/{_null,socket,types,wait}.h and compat/explicit_bzero.c
License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND OpenSSL AND LicenseRef-Fedora-Public-Domain
URL:            https://www.rpki-client.org/
%if !0%{?with_snapshot}
Source0:        https://ftp.openbsd.org/pub/OpenBSD/rpki-client/%{name}-%{version}.tar.gz
Source1:        https://ftp.openbsd.org/pub/OpenBSD/rpki-client/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/B5B6416FEA6DDA05EA562A9FCB987F2783972FF9
%else
Source0:        https://github.com/rpki-client/rpki-client-portable/archive/%{portable_commit}/%{name}-portable-%{version}-%{portable_shortcommit}.tar.gz
Source1:        https://github.com/rpki-client/rpki-client-openbsd/archive/%{openbsd_commit}/%{name}-openbsd-%{version}-%{openbsd_shortcommit}.tar.gz
%endif
Source3:        TALs.md
Source4:        %{name}.sysusersd
Source5:        %{name}.service
Source6:        %{name}.timer
Source7:        %{name}.service.el8
%if !0%{?with_snapshot}
BuildRequires:  gnupg2
%else
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel >= 1.1.0
BuildRequires:  libretls-devel
BuildRequires:  expat-devel
BuildRequires:  rsync
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
Requires:       rsync
%{?systemd_requires}
%{?sysusers_requires_compat}
# https://github.com/rpki-client/rpki-client-portable/commit/764aadf4d8d42ac198def7ef3e8077f0a324276f
ExcludeArch:    %{ix86}

%description
The OpenBSD rpki-client is a free, easy-to-use implementation of the
Resource Public Key Infrastructure (RPKI) for Relying Parties (RP) to
facilitate validation of the Route Origin of a BGP announcement. The
program queries the RPKI repository system, downloads and validates
Route Origin Authorisations (ROAs) and finally outputs Validated ROA
Payloads (VRPs) in the configuration format of OpenBGPD, BIRD, and
also as CSV or JSON objects for consumption by other routing stacks.

%prep
%if !0%{?with_snapshot}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%else
%setup -q -n %{name}-portable-%{portable_commit}
tar xfz %{SOURCE1}
mv -f %{name}-openbsd-%{openbsd_commit} openbsd
./autogen.sh
%endif
cp -pf %{SOURCE3} .

%build
%configure \
  --with-user=%{name} \
  --with-tal-dir=%{_sysconfdir}/pki/tals \
  --with-base-dir=%{_localstatedir}/cache/%{name} \
  --with-output-dir=%{_localstatedir}/lib/%{name}
%make_build

%install
%make_install
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/%{name}.timer
%{?el8:install -D -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service}

%pre
%sysusers_create_compat %{SOURCE4}

%post
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.timer

%postun
%systemd_postun %{name}.timer

%files
%license LICENSE
%doc AUTHORS README.md TALs.md
%{_sbindir}/%{name}
%{_sysconfdir}/pki/tals/
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%{_sysusersdir}/%{name}.conf
%{_mandir}/man8/%{name}.8*
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/cache/%{name}/
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/lib/%{name}/

%changelog
* Mon Jan 13 2025 Robert Scheck <robert@fedoraproject.org> 9.4-1
- Upgrade to 9.4 (#2336356)

* Sun Sep 22 2024 Robert Scheck <robert@fedoraproject.org> 9.3-1
- Upgrade to 9.3 (#2314116)

* Sat Aug 24 2024 Robert Scheck <robert@fedoraproject.org> 9.2-1
- Upgrade to 9.2 (#2307710)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Robert Scheck <robert@fedoraproject.org> 9.1-1
- Upgrade to 9.1 (#2293864)

* Sun Mar 03 2024 Robert Scheck <robert@fedoraproject.org> 9.0-1
- Upgrade to 9.0 (#2267565)

* Tue Feb 13 2024 Robert Scheck <robert@fedoraproject.org> 8.9-1
- Upgrade to 8.9 (#2264085)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Robert Scheck <robert@fedoraproject.org> 8.8-1
- Upgrade to 8.8 (#2256244)

* Fri Dec 22 2023 Robert Scheck <robert@fedoraproject.org> 8.7-1
- Upgrade to 8.7 (#2255458)

* Sun Nov 05 2023 Robert Scheck <robert@fedoraproject.org> 8.6-2
- Rebuilt for libretls 3.8.1

* Wed Oct 04 2023 Robert Scheck <robert@fedoraproject.org> 8.6-1
- Upgrade to 8.6 (#2242194)

* Sun Jul 30 2023 Robert Scheck <robert@fedoraproject.org> 8.5-1
- Upgrade to 8.5 (#2227464)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 10 2023 Robert Scheck <robert@fedoraproject.org> 8.4-2
- Added systemd unit and timer

* Tue May 02 2023 Robert Scheck <robert@fedoraproject.org> 8.4-1
- Upgrade to 8.4

* Sun Mar 19 2023 Robert Scheck <robert@fedoraproject.org> 8.3-1
- Upgrade to 8.3 (#2179641)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 24 2022 Robert Scheck <robert@fedoraproject.org> 8.2-3
- Rebuilt for libretls 3.7.0

* Thu Dec 22 2022 Robert Scheck <robert@fedoraproject.org> 8.2-2
- Added upstream patch for AF_INET6 support in inet_net_pton()

* Wed Dec 14 2022 Robert Scheck <robert@fedoraproject.org> 8.2-1
- Upgrade to 8.2 (#2153077)

* Sun Sep 11 2022 Robert Scheck <robert@fedoraproject.org> 8.0-1
- Upgrade to 8.0 (#2125925)

* Thu Jul 28 2022 Robert Scheck <robert@fedoraproject.org> 7.9-3
- Added sysusers.d file to achieve user() and group() provides

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Robert Scheck <robert@fedoraproject.org> 7.9-1
- Upgrade to 7.9 (#2106947)

* Sat May 14 2022 Robert Scheck <robert@fedoraproject.org> 7.8-2
- Rebuilt for libretls 3.5.2

* Sat Apr 09 2022 Robert Scheck <robert@fedoraproject.org> 7.8-1
- Upgrade to 7.8 (#2073705)

* Fri Apr 08 2022 Robert Scheck <robert@fedoraproject.org> 7.7-1
- Upgrade to 7.7 (#2073214)

* Sun Feb 27 2022 Robert Scheck <robert@fedoraproject.org> 7.6-2
- Rebuilt for libretls 3.5.0

* Mon Feb 07 2022 Robert Scheck <robert@fedoraproject.org> 7.6-1
- Upgrade to 7.6 (#2051736)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 09 2021 Robert Scheck <robert@fedoraproject.org> 7.5-1
- Upgrade to 7.5 (#2021523)

* Sat Oct 30 2021 Robert Scheck <robert@fedoraproject.org> 7.4-1
- Upgrade to 7.4 (#2018729)

* Sat Oct 16 2021 Robert Scheck <robert@fedoraproject.org> 7.3-2
- Rebuilt for libretls 3.4.1

* Thu Sep 23 2021 Robert Scheck <robert@fedoraproject.org> 7.3-1
- Upgrade to 7.3 (#2007447)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 7.2-2
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 28 2021 Robert Scheck <robert@fedoraproject.org> 7.2-1
- Upgrade to 7.2 (#1987093)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 18 2021 Robert Scheck <robert@fedoraproject.org> 7.1-1
- Upgrade to 7.1 (#1961870)

* Fri Apr 16 2021 Robert Scheck <robert@fedoraproject.org> 7.0-1
- Upgrade to 7.0 (#1950163)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.8p1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Robert Scheck <robert@fedoraproject.org> 6.8p1-2
- Added upstream hotfix for stalled rsync servers in the wild

* Thu Nov 12 2020 Robert Scheck <robert@fedoraproject.org> 6.8p1-1
- Upgrade to 6.8p1 (#1897161)

* Tue Oct 20 2020 Robert Scheck <robert@fedoraproject.org> 6.8p0-1
- Upgrade to 6.8p0 (#1889618)

* Wed Jul 29 2020 Robert Scheck <robert@fedoraproject.org> 6.7p1-1
- Upgrade to 6.7p1 (#1861137)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7p0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Robert Scheck <robert@fedoraproject.org> 6.7p0-1
- Upgrade to 6.7p0 (#1837150)

* Sun Apr 19 2020 Robert Scheck <robert@fedoraproject.org> 6.6p2-1
- Upgrade to 6.6p2

* Tue Apr 14 2020 Robert Scheck <robert@fedoraproject.org> 6.6p1-1
- Upgrade to 6.6p1

* Sun Apr 05 2020 Robert Scheck <robert@fedoraproject.org> 0.3.0-2
- Apply fixes from upstream (rebase to commit 87683e9)

* Mon Feb 24 2020 Robert Scheck <robert@fedoraproject.org> 0.3.0-1
- Upgrade to 0.3.0 (#1806049)
- Install bundled Trust Anchor Locators (TALs)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jun 19 2019 Robert Scheck <robert@fedoraproject.org> 0.2.0-1
- Upgrade to 0.2.0 (#1745770)
- Initial spec file for Fedora and Red Hat Enterprise Linux
