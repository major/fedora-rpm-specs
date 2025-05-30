# Generated by rust2rpm 27
# * Deactivate tests because of a missing dev-dependency (gix-testtools)
# * See https://github.com/Byron/gitoxide/discussions/900 for more information
%bcond check 0
%global debug_package %{nil}

%global crate gix-path

Name:           rust-gix-path
Version:        0.10.14
Release:        %autorelease
Summary:        Utility crate for handling paths in gix

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-path
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          gix-path-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A crate of the gitoxide project dealing paths and their conversions.}

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
