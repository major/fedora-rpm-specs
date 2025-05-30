# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate chromaterm

Name:           rust-chromaterm
Version:        0.1.1
Release:        %autorelease
Summary:        Yet another crate for terminal colors

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/chromaterm
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Allow older rstest (0.23) until it can be updated
Patch:          chromaterm-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Yet another crate for terminal colors.}

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
