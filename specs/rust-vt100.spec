# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate vt100

Name:           rust-vt100
Version:        0.15.2
Release:        %autorelease
Summary:        Library for parsing terminal data

License:        MIT
URL:            https://crates.io/crates/vt100
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump vte from 0.11.0 to 0.13.0
# * drop dev-dependencies that are only used in tests or examples that are not
#   included in the crate: nix, quickcheck, rand, serde, serde_json,
#   terminal_size
Patch:          vt100-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Library for parsing terminal data.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
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
