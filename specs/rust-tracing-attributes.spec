# Generated by rust2rpm 27
# * resolve dependency loop with tracing
%bcond check 0
%global debug_package %{nil}

%global crate tracing-attributes

Name:           rust-tracing-attributes
Version:        0.1.30
Release:        %autorelease
Summary:        Procedural macro attributes for automatically instrumenting functions

License:        MIT
URL:            https://crates.io/crates/tracing-attributes
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Procedural macro attributes for automatically instrumenting functions.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%package     -n %{name}+async-await-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-await-devel %{_description}

This package contains library source intended for building other packages which
use the "async-await" feature of the "%{crate}" crate.

%files       -n %{name}+async-await-devel
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
