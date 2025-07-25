# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate pest_generator

Name:           rust-pest_generator
Version:        2.8.1
Release:        %autorelease
Summary:        Pest code generator

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pest_generator
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop feature and dependencies for bootstrap build mode
Patch:          pest_generator-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Pest code generator.}

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
%doc %{crate_instdir}/_README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+export-internal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+export-internal-devel %{_description}

This package contains library source intended for building other packages which
use the "export-internal" feature of the "%{crate}" crate.

%files       -n %{name}+export-internal-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+grammar-extras-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+grammar-extras-devel %{_description}

This package contains library source intended for building other packages which
use the "grammar-extras" feature of the "%{crate}" crate.

%files       -n %{name}+grammar-extras-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
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
