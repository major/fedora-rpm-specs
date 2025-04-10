# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate az

Name:           rust-az
Version:        1.2.1
Release:        %autorelease
Summary:        Casts and checked casts

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/az
Source:         %{crates_source}
Patch:          0001-deny-warnings-considered-harmful.patch

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Casts and checked casts.}

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
%doc %{crate_instdir}/RELEASES.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fail-on-warnings-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fail-on-warnings-devel %{_description}

This package contains library source intended for building other packages which
use the "fail-on-warnings" feature of the "%{crate}" crate.

%files       -n %{name}+fail-on-warnings-devel
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
