# Generated by rust2rpm 23
# * tests can only be run in-tree
%bcond_with check
%global debug_package %{nil}

%global crate actix-utils

Name:           rust-actix-utils
Version:        3.0.1
Release:        %autorelease
Summary:        Various utilities used in the Actix ecosystem

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-utils
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Various utilities used in the Actix ecosystem.}

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
%doc %{crate_instdir}/CHANGES.md
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