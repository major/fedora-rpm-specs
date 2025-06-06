# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

# prevent executables from being installed
%global cargo_install_bin 0

%global crate assert_cmd

Name:           rust-assert_cmd
Version:        2.0.17
Release:        %autorelease
Summary:        Test CLI Applications

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/assert_cmd
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
Test CLI Applications.}

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

%package     -n %{name}+color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+color-devel %{_description}

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%files       -n %{name}+color-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+color-auto-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+color-auto-devel %{_description}

This package contains library source intended for building other packages which
use the "color-auto" feature of the "%{crate}" crate.

%files       -n %{name}+color-auto-devel
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
