# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

# prevent executables from being installed
%global cargo_install_bin 0

%global crate nu-utils

Name:           rust-nu-utils
Version:        0.99.1
Release:        %autorelease
Summary:        Nushell utility functions

License:        MIT
URL:            https://crates.io/crates/nu-utils
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          nu-utils-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
Nushell utility functions.}

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
