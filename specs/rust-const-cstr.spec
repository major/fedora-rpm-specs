# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate const-cstr

Name:           rust-const-cstr
Version:        0.3.0
Release:        %autorelease
Summary:        Create static C-compatible strings from Rust string literals

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/const-cstr
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Create static C-compatible strings from Rust string literals.}

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
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
