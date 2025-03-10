# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate group

Name:           rust-group
Version:        0.13.0
Release:        %autorelease
Summary:        Elliptic curve group traits and utilities

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/group
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused wnaf-memuse feature with missing dependencies
Patch:          group-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Elliptic curve group traits and utilities.}

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
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rand_xorshift-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand_xorshift-devel %{_description}

This package contains library source intended for building other packages which
use the "rand_xorshift" feature of the "%{crate}" crate.

%files       -n %{name}+rand_xorshift-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tests-devel %{_description}

This package contains library source intended for building other packages which
use the "tests" feature of the "%{crate}" crate.

%files       -n %{name}+tests-devel
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
