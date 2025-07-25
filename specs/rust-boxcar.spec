# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate boxcar

Name:           rust-boxcar
Version:        0.2.13
Release:        %autorelease
Summary:        Concurrent, append-only vector

License:        MIT
URL:            https://crates.io/crates/boxcar
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          boxcar-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * Do not depend on criterion; it is needed only for benchmarks.
# * Exclude benchmarks, since bench.rs carries its own MIT license and this
#   complicates packaging. We suggested this upstream in
#   https://github.com/ibraheemdev/boxcar/pull/8, which was merged, but upstream
#   subsequently decided to include benchmarks in published crates,
#   https://github.com/ibraheemdev/boxcar/commit/7131dc44d35d4b4e88d9d80374a7528c59bd6cfe.
#   This patch basically reverts that commit.
Patch:          boxcar-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A concurrent, append-only vector.}

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
