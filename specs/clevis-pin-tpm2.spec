# Generated by rust2rpm 26
# * tests need access to TPM2 hardware
%bcond_with check

# prevent library files from being installed
%global cargo_install_lib 0

Name:           clevis-pin-tpm2
Version:        0.5.3
Release:        10%{?dist}
Summary:        Clevis PIN for unlocking with TPM2 supporting Authorized Policies

SourceLicense:  MIT
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# EUPL-1.2
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# Unlicense OR MIT
License:        MIT AND Apache-2.0 AND EUPL-1.2 AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/fedora-iot/clevis-pin-tpm2/
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# To create the vendor tarball:
#   tar xf %%{name}-%%{version}.crate ; pushd %%{name}-%%{version} ; \
#   cargo vendor && tar Jcvf ../%%{name}-%%{version}-vendor.tar.xz vendor/ ; popd
Source1:        %{name}-%{version}-vendor.tar.xz

%if 0%{?rhel}
BuildRequires:  rust-toolset
BuildRequires:  clang-devel
BuildRequires:  openssl-devel
BuildRequires:  tpm2-tss-devel
%else
BuildRequires:  cargo-rpm-macros >= 26
%endif

Requires:       clevis

%description
%{summary}.

%prep
%autosetup -p1 %{?rhel:-a1}
%if 0%{?rhel}
%cargo_prep -v vendor
%else
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
%endif

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%if 0%{?rhel}
%cargo_vendor_manifest
%endif

%install
%cargo_install
ln -s /usr/bin/clevis-pin-tpm2 %{buildroot}/usr/bin/clevis-encrypt-tpm2plus
ln -s /usr/bin/clevis-pin-tpm2 %{buildroot}/usr/bin/clevis-decrypt-tpm2plus

%if %{with check}
%check
%cargo_test -- -- --skip real_ --skip loop_ --skip travis_
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%if 0%{?rhel}
%license cargo-vendor.txt
%endif
%doc README.md
%{_bindir}/clevis-pin-tpm2
%{_bindir}/clevis-*-tpm2plus

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Feb 06 2025 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-9
- Rebuild for openssl crate >= v0.10.70 (RUSTSEC-2025-0004)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 22 2024 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-6
- Refresh spec for rust-packaging v26

* Fri Feb 02 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 0.5.3-5
- Update Rust macro usage

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-2
- Rebuild for openssl crate >= v0.10.60 (RUSTSEC-2023-0044, RUSTSEC-2023-0072)

* Fri Jul 28 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.3-1
- Update to 0.5.3

* Wed Jul 19 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 0.5.2-7
- Use vendored dependencies in RHEL builds

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 03 2023 Fabio Valentini <decathorpe@gmail.com> - 0.5.2-5
- Rebuild for openssl crate >= v0.10.48 (RUSTSEC-2023-{0022,0023,0024})

* Tue Feb 07 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.2-4
- Rebuild for tss-esapi 7.2.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 22 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2
- License EUPL 1.2 -> MIT

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Wed Nov 03 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 06 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Tue Nov 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sat Aug 29 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Tue Aug 25 2020 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.1.2-2
- Add symlink to clevis-{en,de}crypt-tpm2plus

* Fri Aug 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Thu Aug 13 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Mon Aug  3 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.1-1
- Initial release
