# Generated by rust2rpm 25
# * disable check as all tests are excluded in the crate
%bcond_with check
%global debug_package %{nil}

%global crate jxl-oxide

Name:           rust-jxl-oxide
Version:        0.3.0
Release:        %autorelease
Summary:        JPEG XL decoder written in pure Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/jxl-oxide
Source:         %{crates_source}
# Add missing license files from upstream
# https://github.com/tirr-c/jxl-oxide/pull/111
Source1:        https://github.com/tirr-c/jxl-oxide/raw/main/LICENSE-APACHE
Source2:        https://github.com/tirr-c/jxl-oxide/raw/main/LICENSE-MIT
# Manually created patch for downstream crate metadata changes
# * drop unwanted "generate-fixtures" binary (used by the test suite)
Patch:          jxl-oxide-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
JPEG XL decoder written in pure Rust.}

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
cp %{SOURCE1} .
cp %{SOURCE2} .
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