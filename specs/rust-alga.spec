# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate alga

Name:           rust-alga
Version:        0.9.3
Release:        %autorelease
Summary:        Abstract algebra for Rust

License:        Apache-2.0
URL:            https://crates.io/crates/alga
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump approx from 0.3 to 0.5
# * bump num-complex from 0.2 to 0.4
# * bump quickcheck dev-dependency from 0.8 to 0.9
Patch:          alga-fix-metadata.diff
# * patch to fix doctests with Rust 1.62+
Patch2:         0001-ignore-doctests-for-non-exported-macro_rules-macros.patch
# * patch to fix doctests with Rust 1.80+
Patch3:         0002-fix-typo-in-doc-code-block-annotation-that-caused-te.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Abstract algebra for Rust.}

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

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
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
