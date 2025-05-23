# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate tryfn

Name:           rust-tryfn
Version:        0.2.3
Release:        %autorelease
Summary:        File-driven snapshot testing for a function

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tryfn
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Allow libtest-mimic 0.8; see “chore(deps): Update Rust crate libtest-mimic to
#   0.8.0”, https://github.com/assert-rs/snapbox/pull/369
Patch:          tryfn-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
File-driven snapshot testing for a function.}

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
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+color-devel %{_description}

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%files       -n %{name}+color-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+color-auto-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+color-auto-devel %{_description}

This package contains library source intended for building other packages which
use the "color-auto" feature of the "%{crate}" crate.

%files       -n %{name}+color-auto-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+diff-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+diff-devel %{_description}

This package contains library source intended for building other packages which
use the "diff" feature of the "%{crate}" crate.

%files       -n %{name}+diff-devel
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
