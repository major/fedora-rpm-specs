# Generated by rust2rpm 23
%bcond_without check
%global debug_package %{nil}

%global crate darling_macro

Name:           rust-darling_macro0.13
Version:        0.13.4
Release:        %autorelease
Summary:        Internal support for a proc-macro library for reading attributes into structs

License:        MIT
URL:            https://crates.io/crates/darling_macro
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Internal support for a proc-macro library for reading attributes into structs
when implementing custom derives. Use https://crates.io/crates/darling in your
code.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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
