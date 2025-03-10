# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate libflate

Name:           rust-libflate1
Version:        1.4.0
Release:        %autorelease
Summary:        Rust implementation of DEFLATE algorithm and related formats

License:        MIT
URL:            https://crates.io/crates/libflate
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused no_std feature with missing dependencies
Patch:          libflate-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A Rust implementation of DEFLATE algorithm and related formats (ZLIB,
GZIP).}

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
