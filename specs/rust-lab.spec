# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate lab

Name:           rust-lab
Version:        0.11.0
Release:        %autorelease
Summary:        Tools for converting RGB colors to the CIE-L*a*b* color space

License:        MIT
URL:            https://crates.io/crates/lab
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump pretty_assertions dev-dependecy from ^0.7 to ^1
# * drop unused, benchmark-only criterion dev-dependency
Patch:          lab-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Tools for converting RGB colors to the CIE-L*a*b* color space, and
comparing differences in color.}

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
