#global candidate rc2
# * missing dev-dependencies: rust-cryptoauthlib, spiffe
%bcond_with check

# prevent library files from being installed
%global cargo_install_lib 0

%global enabled_cargo_features default,tpm-provider,pkcs11-provider,mbed-crypto-provider,direct-authenticator,unix-peer-credentials-authenticator

Name:          parsec
Version:       1.4.1
Release:       4%{?candidate:.%{candidate}}%{?dist}
Summary:       The PARSEC daemon

SourceLicense: Apache-2.0
# LICENSE.dependencies contains a full license breakdown
License:       Apache-2.0
URL:           https://github.com/parallaxsecond/parsec
Source0:       %{url}/archive/v%{version}/%{name}-%{version}%{?candidate:-%{candidate}}.tar.gz
Source1:       parsec.service
Source2:       config.toml
Source3:       parsec.tmpfile.conf
Patch1:        parsec-fix-metadata.diff

BuildRequires: rust-packaging
BuildRequires: systemd
Requires: tpm2-tss >= 4.0.0
Requires(pre): tpm2-tss >= 4.0.0
%{?systemd_requires}

%description
PARSEC is the Platform AbstRaction for SECurity, an open-source initiative to
provide a common API to hardware security and cryptographic services in a
platform-agnostic way. This abstraction layer keeps workloads decoupled from
physical platform details, enabling cloud-native delivery flows within the data
center and at the edge.

%prep
%autosetup -p1 -n %{name}-%{version}%{?candidate:-%{candidate}}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -f %{enabled_cargo_features}

# Create a sysusers.d config file
cat >parsec.sysusers.conf <<EOF
g parsec-clients -
u parsec - 'PARSEC service' /var/lib/parsec -
m parsec parsec-clients
EOF

%build
%cargo_build -f %{enabled_cargo_features}
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install -f %{enabled_cargo_features}

install -D -p -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/parsec.service
install -D -p -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/parsec/config.toml
install -D -p -m0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/parsec.conf
install -d -m0755 %{buildroot}%{_localstatedir}/lib/parsec
install -d -m0755 %{buildroot}%{_localstatedir}/lib/parsec/mappings
install -d -m0755 %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/parsec %{buildroot}%{_libexecdir}/

install -m0644 -D parsec.sysusers.conf %{buildroot}%{_sysusersdir}/parsec.conf

%if %{with check}
%check
%cargo_test -f %{enabled_cargo_features} -- -- --skip real_ --skip loop_ --skip travis_
%endif


%post
%systemd_post parsec.service

%preun
%systemd_preun parsec.service

%postun
%systemd_postun_with_restart parsec.service

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md config.toml
%attr(0750,parsec,parsec) %dir %{_sysconfdir}/parsec/
%attr(0750,parsec,parsec) %dir %{_localstatedir}/lib/parsec/
%attr(0750,parsec,parsec) %dir %{_localstatedir}/lib/parsec/mappings/
%config(noreplace) %{_sysconfdir}/parsec/config.toml
%{_libexecdir}/parsec
%{_tmpfilesdir}/parsec.conf
%{_unitdir}/parsec.service
%{_sysusersdir}/parsec.conf

%changelog
* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.1-4
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 20 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Tue Apr 09 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Sat Mar 30 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.0-0.2.rc2
- Update to 1.4.0 RC2

* Sun Mar 10 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 09 2023 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-4
- Ensure build honors default Rust compiler flags and simplify Rust packaging.

* Tue Feb 07 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.0-3
- Rebuild for tss-esapi 7.2.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 30 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 GA

* Wed Sep 28 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.0-0.1.rc2
- Update to 1.1.0 RC2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 30 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 GA

* Mon Mar 21 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0-0.1rc3
- Update to 1.0.0 RC3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 08 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.7.0-2
- Update the default parsec config file

* Tue Apr 06 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.0-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6.0-2
- Update default config file

* Thu Oct 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Wed Oct 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.0-2
- Enable pkcs11 provider

* Fri Oct 02 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Thu Sep 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-5
- Enable the MBed provider

* Thu Sep 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-4
- User fixess, service file fixes, include default config

* Wed Sep 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-3
- Minor fixes

* Wed Sep 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-2
- Add service user creation, enable TPM2 provider, other fixes

* Tue Sep 01 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.0-1
- Initial package
