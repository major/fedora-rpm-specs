# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate tracing-test-macro

Name:           rust-tracing-test-macro
Version:        0.2.5
Release:        %autorelease
Summary:        Procedural macro that allow for easier testing of crates that use tracing

License:        MIT
URL:            https://crates.io/crates/tracing-test-macro
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A procedural macro that allow for easier testing of crates that use
`tracing`. Internal crate, should only be used through the `tracing-
test` crate.}

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

%package     -n %{name}+no-env-filter-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no-env-filter-devel %{_description}

This package contains library source intended for building other packages which
use the "no-env-filter" feature of the "%{crate}" crate.

%files       -n %{name}+no-env-filter-devel
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
