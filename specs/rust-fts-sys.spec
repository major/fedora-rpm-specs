# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate fts-sys

Name:           rust-fts-sys
Version:        0.2.9
Release:        %autorelease
Summary:        File hierarchy traversal functions (FTS)

License:        MIT
URL:            https://crates.io/crates/fts-sys
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop links = "c"
Patch:          fts-sys-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  glibc-devel

%global _description %{expand:
File hierarchy traversal functions (FTS).}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       glibc-devel

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