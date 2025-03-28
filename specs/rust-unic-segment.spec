# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate unic-segment

Name:           rust-unic-segment
Version:        0.9.0
Release:        %autorelease
Summary:        UNIC — Unicode Text Segmentation Algorithms

# Upstream license specification: MIT/Apache-2.0
# https://github.com/open-i18n/rust-unic/issues/267
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unic-segment
Source0:        %{crates_source}
Source1:        https://github.com/open-i18n/rust-unic/raw/v0.9.0/LICENSE-APACHE
Source2:        https://github.com/open-i18n/rust-unic/raw/v0.9.0/LICENSE-MIT
# Manually created patch for downstream crate metadata changes
# * Update quickcheck dev-dependency to v1:
#   https://github.com/open-i18n/rust-unic/pull/289
Patch:          unic-segment-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
UNIC — Unicode Text Segmentation Algorithms.}

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
%cargo_prep
cp -pav %{SOURCE1} %{SOURCE2} .

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
