# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate unicode_categories

Name:           rust-unicode_categories
Version:        0.1.1
Release:        %autorelease
Summary:        Query Unicode category membership for chars

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode_categories
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * exclude scripts that are only useful for upstream development
Patch:          unicode_categories-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Query Unicode category membership for chars.}

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
