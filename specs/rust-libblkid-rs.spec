# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate libblkid-rs

Name:           rust-libblkid-rs
Version:        0.4.0
Release:        2%{?dist}
Summary:        High level bindings for libblkid

License:        MPL-2.0
URL:            https://crates.io/crates/libblkid-rs
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
High level bindings for libblkid.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGES.txt
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

%package     -n %{name}+deprecated-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deprecated-devel %{_description}

This package contains library source intended for building other packages which
use the "deprecated" feature of the "%{crate}" crate.

%files       -n %{name}+deprecated-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-devel %{_description}

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%files       -n %{name}+static-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
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
* Thu Mar 13 2025 Chung Chung <cchung@redhat.com> - 0.4.0-2
- Rebuild for RAWHIDE

* Wed Feb 19 2025 Chung Chung <cchung@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 26 2024 Bryan Gurney <bgurney@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 27 2023 Bryan Gurney <bgurney@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Bryan Gurney <bgurney@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 mulhern <amulhern@redhat.com> - 0.2.0-3
- Get the date right and bump the release number

* Wed May 25 2022 mulhern <amulhern@redhat.com> - 0.2.0-2
- Re-release new version 0.2.0

* Thu Apr 21 2022 mulhern <amulhern@redhat.com> - 0.1.1-3
- Revert to previous; version number incompatible with stratisd requirements

* Wed Apr 20 2022 mulhern <amulhern@redhat.com> - 0.2.0-1
- Rebuild with rust2rpm v20; release new version 0.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 John Baublitz <jbaublitz@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Thu Oct 28 15:28:52 EDT 2021 John Baublitz <jbaublitz@redhat.com> - 0.1.0-1
- Initial package
