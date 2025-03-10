# Generated by rust2rpm 27
# * tests can only be run in-tree
%bcond check 0
%global debug_package %{nil}

# drop unnecessary debuginfo generation to fix OOM problems on 32-bit arches
%global rustflags_debuginfo 0

# prevent executables from being installed
%global cargo_install_bin 0

%global crate cargo

Name:           rust-cargo
Version:        0.79.0
Release:        %autorelease
Summary:        Package manager for Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cargo
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          cargo-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop features for statically linking cURL, libgit2, OpenSSL, and SQLite
# * update base64 dependency to version 0.22
# * update git2 / git2-curl / libgit2 dependencies
# * update gix dependency to version 0.70
# * update itertools dependency to version 0.13
# * update supports-unicode dependency to version 3
Patch:          cargo-fix-metadata.diff
# * https://github.com/rust-lang/cargo/commit/3a18044
Patch:          0001-Port-to-gix-0.69.patch

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
Package manager for Rust.}

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
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/
%exclude %{crate_instdir}/ci/
%exclude %{crate_instdir}/clippy.toml
%exclude %{crate_instdir}/deny.toml
%exclude %{crate_instdir}/publish.py
%exclude %{crate_instdir}/triagebot.toml

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%files       -n %{name}+openssl-devel
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
