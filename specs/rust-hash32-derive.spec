# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate hash32-derive

Name:           rust-hash32-derive
Version:        0.1.1
Release:        %autorelease
Summary:        Macros 1.1 implementation of #[derive(Hash32)]

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hash32-derive
Source:         %{crates_source}
# License texts only in the main crate
Source1:        https://raw.githubusercontent.com/japaric/hash32/main/LICENSE-APACHE
Source2:        https://raw.githubusercontent.com/japaric/hash32/main/LICENSE-MIT

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Macros 1.1 implementation of #[derive(Hash32)].}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
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
%autochangelog