# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate tokio-tfo

Name:           rust-tokio-tfo
Version:        0.3.4
Release:        %autorelease
Summary:        TCP Fast Open (TFO) in Rust for tokio

License:        MIT
URL:            https://crates.io/crates/tokio-tfo
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          tokio-tfo-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
TCP Fast Open (TFO) in Rust for tokio.}

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
