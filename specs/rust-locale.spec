# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate locale

Name:           rust-locale
Version:        0.2.2
Release:        %autorelease
Summary:        Library for basic localisation

License:        MIT
URL:            https://crates.io/crates/locale
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * exclude files that are only useful for upstream development:
#   https://github.com/rust-locale/rust-locale/pull/27
Patch:          locale-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Library for basic localisation. Warning: Major rewrite pending for 0.3!.}

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
