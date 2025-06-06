# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate ammonia

Name:           rust-ammonia
Version:        4.0.0
Release:        %autorelease
Summary:        HTML Sanitization

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ammonia
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump html5ever dependency from 0.27 to 0.29:
#   https://github.com/rust-ammonia/ammonia/commit/50d02c6
Patch:          ammonia-fix-metadata.diff
Patch:          50d02c6-backport.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
HTML Sanitization.}

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
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/RELEASE_PROCESS.md
%doc %{crate_instdir}/SECURITY.md
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
