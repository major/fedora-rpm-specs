# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate crossfont

Name:           rust-crossfont
Version:        0.8.1
Release:        %autorelease
Summary:        Cross platform native font loading and rasterization

License:        Apache-2.0
URL:            https://crates.io/crates/crossfont
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          crossfont-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * Update dependencies to the versions available in Fedora
Patch:          crossfont-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Cross platform native font loading and rasterization.}

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
