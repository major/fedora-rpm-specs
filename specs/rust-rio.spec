# Generated by rust2rpm 26
%ifarch %{ix86}
# Tests do not work properly on i686
%bcond_with check
%else
%bcond_without check
%endif
%global debug_package %{nil}

%global crate rio

Name:           rust-rio
Version:        0.9.4
Release:        %autorelease
Summary:        Rust bindings for io_uring

License:        GPL-3.0-or-later
URL:            https://crates.io/crates/rio
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Fix the license identifier
Patch:          rio-fix-metadata.diff
# * Use correct pointer size on 32-bit arches
Patch2:        rio-pointer-size.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
This package provides Rust bindings for io_uring.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LIZENZ
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/code-of-conduct.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_metrics-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_metrics-devel %{_description}

This package contains library source intended for building other packages which
use the "no_metrics" feature of the "%{crate}" crate.

%files       -n %{name}+no_metrics-devel
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