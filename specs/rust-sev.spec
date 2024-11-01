# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate sev

Name:           rust-sev
Version:        4.0.0
Release:        2%{?dist}
Summary:        Library for AMD SEV

License:        Apache-2.0
URL:            https://crates.io/crates/sev
Source:         %{crates_source}

# SEV is an AMD x86_64 CPU feature so doesn't make sense to
# try to build on other arches
ExclusiveArch:  x86_64

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Library for AMD SEV.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%files       -n %{name}+openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sev-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sev-devel %{_description}

This package contains library source intended for building other packages which
use the "sev" feature of the "%{crate}" crate.

%files       -n %{name}+sev-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+snp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+snp-devel %{_description}

This package contains library source intended for building other packages which
use the "snp" feature of the "%{crate}" crate.

%files       -n %{name}+snp-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Mon Oct 28 2024 Tyler Fanelli <tfanelli@redhat.com> - 4.0.0-2
- Build with fixed rdrand dependency.

* Thu Sep 05 2024 Tyler Fanelli <tfanelli@redhat.com> - 4.0.0-1
- Update to version 4.0.0

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Tyler Fanelli <tfanelli@redhat.com> - 3.2.0
- Update to version 3.2.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Tyler Fanelli <tfanelli@redhat.com> - 1.2.1-1
- Remove mmarinus dependency
- Use older version of serde-big-array

* Thu Jul 06 2023 Tyler Fanelli <tfanelli@redhat.com> - 1.2.0-1
- Update to version 1.2.0

* Thu Feb 09 2023 Sergio Lopez <slp@redhat.com> - 1.1.0-1
- Update to version 1.1.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Tyler Fanelli <tfanelli@redhat.com> - 1.0.1-1
- Rebase to 1.0.1 release (rhbz#2141113)

* Fri Aug 26 2022 Cole Robinson <crobinso@redhat.com> - 0.3.0-3
- Only build for x86_64

* Thu Aug 25 2022 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-2
- Regenerate with rust2rpm v22.

* Thu Aug 25 2022 Tyler Fanelli <tfanelli@redhat.com> - 0.3.0-1
- Rebase to 0.3.0 release (rhbz#2097874)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan  4 2022 Daniel P. Berrangé <berrange@redhat.com> - 0.2.0-1
- Rebase to 0.2.0 release (rhbz#2034272)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 09 2021 Connor Kuehl <ckuehl@redhat.com> - 0.1.0-1
- Initial package
