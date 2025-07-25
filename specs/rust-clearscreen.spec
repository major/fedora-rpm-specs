# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate clearscreen

Name:           rust-clearscreen
Version:        4.0.2
Release:        %autorelease
Summary:        Cross-platform terminal screen clearing

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/clearscreen
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          clearscreen-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * Do not expose the windows-console feature
Patch:          clearscreen-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Cross-platform terminal screen clearing.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYRIGHT
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/TERMINALS.md
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
# * skip tests that only work in real terminals
%{cargo_test -- -- --exact %{shrink:
    --skip terminfo_screen
    --skip terminfo_scrollback
    --skip tput_clear
    --skip tput_reset
}}
%endif

%changelog
%autochangelog
