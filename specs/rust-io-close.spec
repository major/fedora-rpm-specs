# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate io-close

Name:           rust-io-close
Version:        0.3.7
Release:        %autorelease
Summary:        Extension trait for safely dropping I/O writers such as File and BufWriter

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/io-close
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          io-close-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop unused "os_pipe" feature with outdated dependencies
Patch:          io-close-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
An extension trait for safely dropping I/O writers such as File and
BufWriter.}

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