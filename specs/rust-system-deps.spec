# Generated by rust2rpm 27
# * files required by tests are not shipped with published crates
%bcond check 0
%global debug_package %{nil}

%global crate system-deps

Name:           rust-system-deps
Version:        7.0.5
Release:        %autorelease
Summary:        Declarative system dependencies in Cargo.toml

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/system-deps
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Discover and configure system dependencies from declarative dependencies
in Cargo.toml.}

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
