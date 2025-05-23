# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate codespan-reporting

Name:           rust-codespan-reporting
Version:        0.12.0
Release:        %autorelease
Summary:        Beautiful diagnostic reporting for text-based programming languages

License:        Apache-2.0
URL:            https://crates.io/crates/codespan-reporting
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop example code and example-only dev-dependencies
Patch:          codespan-reporting-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Beautiful diagnostic reporting for text-based programming languages.}

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

%package     -n %{name}+ascii-only-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ascii-only-devel %{_description}

This package contains library source intended for building other packages which
use the "ascii-only" feature of the "%{crate}" crate.

%files       -n %{name}+ascii-only-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serialization-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialization-devel %{_description}

This package contains library source intended for building other packages which
use the "serialization" feature of the "%{crate}" crate.

%files       -n %{name}+serialization-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+termcolor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+termcolor-devel %{_description}

This package contains library source intended for building other packages which
use the "termcolor" feature of the "%{crate}" crate.

%files       -n %{name}+termcolor-devel
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
