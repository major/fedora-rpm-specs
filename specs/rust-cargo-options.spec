# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate cargo-options

Name:           rust-cargo-options
Version:        0.7.5
Release:        %autorelease
Summary:        Reusable common Cargo command line options

License:        MIT
URL:            https://crates.io/crates/cargo-options
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump trycmd dev-dependency from 0.14 to 0.15:
#   https://github.com/messense/cargo-options/pull/16
Patch:          cargo-options-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Reusable common Cargo command line options.}

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

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
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
# * integration tests hang indefinitely
%cargo_test -- --lib
%cargo_test -- --doc
%endif

%changelog
%autochangelog
