# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate dtparse

Name:           rust-dtparse
Version:        2.0.1
Release:        %autorelease
Summary:        Dateutil-compatible timestamp parser for Rust

License:        Apache-2.0
URL:            https://crates.io/crates/dtparse
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A dateutil-compatible timestamp parser for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%license %{crate_instdir}/LICENSE-APACHE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/CONTRIBUTORS.md
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
%autochangelog
