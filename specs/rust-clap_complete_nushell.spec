# Generated by rust2rpm 27
# * missing dev-dependencies: completest ^0.4, completest-nu ^0.4, snapbox ^0.5
%bcond check 0
%global debug_package %{nil}

%global crate clap_complete_nushell

Name:           rust-clap_complete_nushell
Version:        4.5.8
Release:        %autorelease
Summary:        Generator library used with clap for Nushell completion scripts

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/clap_complete_nushell
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A generator library used with clap for Nushell completion scripts.}

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
