# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate tuikit

Name:           rust-tuikit
Version:        0.5.0
Release:        %autorelease
Summary:        Toolkit for writing TUI applications

License:        MIT
URL:            https://crates.io/crates/tuikit
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Toolkit for writing TUI applications.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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
# skip a test that is not supported in non-terminal environments
%cargo_test -- -- --skip raw::test::test_into_raw_mode
%endif

%changelog
%autochangelog
