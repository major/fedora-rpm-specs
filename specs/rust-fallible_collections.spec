# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate fallible_collections

Name:           rust-fallible_collections
Version:        0.4.9
Release:        %autorelease
Summary:        Which adds fallible allocation api to std collections

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fallible_collections
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * use hashbrown 0.14 instead of 0.13
#   (https://github.com/vcombey/fallible_collections/pull/46)
Patch:          fallible_collections-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A crate which adds fallible allocation api to std collections.}

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

%package     -n %{name}+hashbrown-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hashbrown-devel %{_description}

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%files       -n %{name}+hashbrown-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hashmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hashmap-devel %{_description}

This package contains library source intended for building other packages which
use the "hashmap" feature of the "%{crate}" crate.

%files       -n %{name}+hashmap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rust_1_57-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rust_1_57-devel %{_description}

This package contains library source intended for building other packages which
use the "rust_1_57" feature of the "%{crate}" crate.

%files       -n %{name}+rust_1_57-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std_io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std_io-devel %{_description}

This package contains library source intended for building other packages which
use the "std_io" feature of the "%{crate}" crate.

%files       -n %{name}+std_io-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-devel
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
# * skip two tests that rely on UB and crash with recent Rust versions:
#   https://github.com/vcombey/fallible_collections/issues/35
%cargo_test -- -- --skip try_clone_oom --skip tryvec_try_clone_oom
%endif

%changelog
%autochangelog