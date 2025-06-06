# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate proc-macro-error2

Name:           rust-proc-macro-error2
Version:        2.0.1
Release:        %autorelease
Summary:        Almost drop-in replacement to panics in proc-macros

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proc-macro-error2
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop test that requires an unpublished test_crate workspace member
Patch:          proc-macro-error2-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Almost drop-in replacement to panics in proc-macros.}

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

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+syn-error-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+syn-error-devel %{_description}

This package contains library source intended for building other packages which
use the "syn-error" feature of the "%{crate}" crate.

%files       -n %{name}+syn-error-devel
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
