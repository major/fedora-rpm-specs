# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate num-modular

Name:           rust-num-modular
Version:        0.5.1
Release:        %autorelease
Summary:        A generic implementation of integer division and modular arithmetics

License:        Apache-2.0
URL:            https://crates.io/crates/num-modular
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Implementation of efficient integer division and modular arithmetic
operations with generic number types. Supports various backends
including num-bigint, etc..}

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

%package     -n %{name}+num-bigint-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+num-bigint-devel %{_description}

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%files       -n %{name}+num-bigint-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
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
# * fails intermittently with `attempt to calculate the remainder with a divisor
#   of zero`
%cargo_test -- -- --exact --skip reduced::tests::test_against_prim stdout
%endif

%changelog
%autochangelog
