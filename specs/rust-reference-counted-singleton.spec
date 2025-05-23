# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate reference-counted-singleton

Name:           rust-reference-counted-singleton
Version:        0.1.5
Release:        %autorelease
Summary:        Reference-counted singleton whose protected data can be recreated as needed

License:        MIT
URL:            https://crates.io/crates/reference-counted-singleton
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * exclude unnecessary files
#   https://github.com/koutheir/reference-counted-singleton/pull/2
Patch:          reference-counted-singleton-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Reference-counted singleton whose protected data can be recreated as
needed.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
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
%cargo_test
%endif

%changelog
%autochangelog
