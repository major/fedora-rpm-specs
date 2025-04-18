# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate itoa

Name:           rust-itoa
Version:        1.0.15
Release:        %autorelease
Summary:        Fast integer primitive to string conversion

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/itoa
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Fast integer primitive to string conversion.}

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

%package     -n %{name}+no-panic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no-panic-devel %{_description}

This package contains library source intended for building other packages which
use the "no-panic" feature of the "%{crate}" crate.

%files       -n %{name}+no-panic-devel
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
