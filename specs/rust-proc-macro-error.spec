# Generated by rust2rpm 24
# * tests can only be run in-tree
%bcond_with check
%global debug_package %{nil}

%global crate proc-macro-error

Name:           rust-proc-macro-error
Version:        1.0.4
Release:        %autorelease
Summary:        Almost drop-in replacement to panics in proc-macros

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proc-macro-error
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

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

%package     -n %{name}+syn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+syn-devel %{_description}

This package contains library source intended for building other packages which
use the "syn" feature of the "%{crate}" crate.

%files       -n %{name}+syn-devel
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
