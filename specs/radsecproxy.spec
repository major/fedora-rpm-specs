Summary:        Generic RADIUS proxy with RadSec support
Name:           radsecproxy
Version:        1.11.1
Release:        2%{?dist}
License:        BSD-3-Clause
URL:            https://radsecproxy.github.io/
Source0:        https://github.com/radsecproxy/radsecproxy/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/radsecproxy/radsecproxy/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/210FA7FB28E45779777BAA1C5963D59C3D68633B
Source3:        %{name}.conf
Source4:        %{name}.service
Source5:        %{name}.logrotate
Source6:        %{name}.tmpfilesd
Source7:        %{name}.sysusersd
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  nettle-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
Requires:       logrotate
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
radsecproxy is a generic RADIUS proxy that in addition to usual RADIUS UDP
transport, also supports TLS (RadSec), as well as RADIUS over TCP and DTLS.
The aim is for the proxy to have sufficient features to be flexible, while
at the same time to be small, efficient and easy to configure.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%configure
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir}/pki,%{_rundir},%{_localstatedir}/{lib,log}}/%{name}/
install -D -p -m 0640 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
chmod 644 tools/*.sh

%check
make check

%pre
%sysusers_create_compat %{SOURCE7}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc AUTHORS ChangeLog radsecproxy.conf-example THANKS tools
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/
%{_bindir}/%{name}-conf
%{_bindir}/%{name}-hash
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}-hash.8*
%{_mandir}/man5/%{name}.conf.5*
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 06 2024 Robert Scheck <robert@fedoraproject.org> 1.11.1-1
- Upgrade to 1.11.1 (#2330848)

* Sat Oct 19 2024 Robert Scheck <robert@fedoraproject.org> 1.11.0-1
- Upgrade to 1.11.0 (#2290989)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 03 2024 Robert Scheck <robert@fedoraproject.org> 1.10.1-1
- Upgrade to 1.10.1 (#2278768)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 26 2023 Robert Scheck <robert@fedoraproject.org> 1.10.0-1
- Upgrade to 1.10.0 (#2207652)

* Tue May 02 2023 Robert Scheck <robert@fedoraproject.org> 1.9.3-1
- Upgrade to 1.9.3

* Tue Jan 24 2023 Robert Scheck <robert@fedoraproject.org> 1.9.2-1
- Upgrade to 1.9.2 (#2163576)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 29 2022 Robert Scheck <robert@fedoraproject.org> 1.9.1-4
- Added sysusers.d file to achieve user() and group() provides

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Robert Scheck <robert@fedoraproject.org> 1.9.1-1
- Upgrade to 1.9.1 (#2017132)

* Tue Sep 14 2021 Robert Scheck <robert@fedoraproject.org> 1.9.0-5
- Use -Wno-error=deprecated-declarations with OpenSSL 3.0.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.9.0-4
- Rebuilt with OpenSSL 3.0.0

* Mon Jul 26 2021 Robert Scheck <robert@fedoraproject.org> 1.9.0-3
- Added upstream patch to fix setstacksize() for glibc >= 2.34

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Robert Scheck <robert@fedoraproject.org> 1.9.0-1
- Upgrade to 1.9.0 (#1959532, #1965675)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Robert Scheck <robert@fedoraproject.org> 1.8.2-2
- Build against OpenSSL 1.1 on RHEL 7 (for TLSv1.3 support)

* Fri Aug 07 2020 Robert Scheck <robert@fedoraproject.org> 1.8.2-1
- Upgrade to 1.8.2 (#1867106)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Robert Scheck <robert@fedoraproject.org> 1.8.1-3
- Added patch to declare pthread_attr as extern in header file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Robert Scheck <robert@fedoraproject.org> 1.8.1-1
- Upgrade to 1.8.1

* Tue Sep 17 2019 Robert Scheck <robert@fedoraproject.org> 1.8.0-1
- Upgrade to 1.8.0 (#1753052)
- Initial spec file for Fedora and Red Hat Enterprise Linux
