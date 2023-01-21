#global candidate rc2
%bcond_with check
%global __cargo_skip_build 0
%global __cargo_is_lib() false

# mbed-crypto-provider, pkcs11-provider, tpm-provider, all-providers, all-authenticators
%global __cargo_parse_opts --features=tpm-provider,pkcs11-provider,mbed-crypto-provider,direct-authenticator,unix-peer-credentials-authenticator

%global custom_cargo_build /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo build %{_smp_mflags} -Z avoid-dev-deps --release
%global custom_cargo_test /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo test %{_smp_mflags} -Z avoid-dev-deps --release --no-fail-fast

Name:          parsec
Version:       1.1.0
Release:       2%{?candidate:.%{candidate}}%{?dist}
Summary:       The PARSEC daemon

License:       ASL 2.0
URL:           https://github.com/parallaxsecond/parsec
Source0:       %{url}/archive/v%{version}/%{name}-%{version}%{?candidate:-%{candidate}}.tar.gz
Source1:       parsec.service
Source2:       config.toml
Source3:       parsec.tmpfile.conf
Patch1:        parsec-metadata.diff

ExclusiveArch: %{rust_arches}
ExcludeArch:   s390x

BuildRequires: protobuf-compiler
BuildRequires: rust-packaging
BuildRequires: systemd
Requires: tpm2-tss >= 3.1.0
Requires(pre): shadow-utils
Requires(pre): tpm2-tss >= 3.1.0
%{?systemd_requires}

%description
PARSEC is the Platform AbstRaction for SECurity, an open-source initiative to
provide a common API to hardware security and cryptographic services in a
platform-agnostic way. This abstraction layer keeps workloads decoupled from
physical platform details, enabling cloud-native delivery flows within the data
center and at the edge.

%prep
%autosetup -p1 -n %{name}-%{version}%{?candidate:-%{candidate}}

export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%custom_cargo_build --features=tpm-provider,pkcs11-provider,mbed-crypto-provider,direct-authenticator,unix-peer-credentials-authenticator

%install
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_install -a

install -D -p -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/parsec.service
install -D -p -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/parsec/config.toml
install -D -p -m0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/parsec.conf
install -d -m0755 %{buildroot}%{_localstatedir}/lib/parsec
install -d -m0755 %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/parsec %{buildroot}%{_libexecdir}/

%if %{with check}
%check
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%custom_cargo_test -- -- --skip real_ --skip loop_ --skip travis_
%endif

%pre
getent group parsec >/dev/null || groupadd -r parsec
# For PARSEC consumers
getent group parsec-clients >/dev/null || groupadd -r parsec-clients
getent passwd parsec >/dev/null || \
    useradd -r -g parsec -G tss -G parsec-clients -d /var/lib/parsec -s /sbin/nologin \
    -c "PARSEC service" parsec
exit 0

%post
%systemd_post parsec.service

%preun
%systemd_preun parsec.service

%postun
%systemd_postun_with_restart parsec.service

%files
%license LICENSE
%doc README.md config.toml
%attr(0750,parsec,parsec) %dir %{_sysconfdir}/parsec/
%attr(0750,parsec,parsec) %dir %{_localstatedir}/lib/parsec/
%config(noreplace) %{_sysconfdir}/parsec/config.toml
%{_libexecdir}/parsec
%{_tmpfilesdir}/parsec.conf
%{_unitdir}/parsec.service

%changelog
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
