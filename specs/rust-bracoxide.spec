# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate bracoxide

Name:           rust-bracoxide
Version:        0.1.6
Release:        %autorelease
Summary:        A powerful Rust library for handling and expanding brace expansions

License:        MIT
URL:            https://crates.io/crates/bracoxide
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop criterion dep and disable benchmarks
Patch:          bracoxide-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A feature-rich library for brace pattern combination, permutation
generation, and error handling.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/Contributing.md
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
