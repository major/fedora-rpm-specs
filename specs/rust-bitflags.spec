# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate bitflags

Name:           rust-bitflags
Version:        2.6.0
Release:        %autorelease
Summary:        Macro to generate structures which behave like bitflags

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bitflags
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A macro to generate structures which behave like bitflags.}

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
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/SECURITY.md
%doc %{crate_instdir}/spec.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+arbitrary-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary-devel %{_description}

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%files       -n %{name}+arbitrary-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bytemuck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytemuck-devel %{_description}

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%files       -n %{name}+bytemuck-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+example_generated-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+example_generated-devel %{_description}

This package contains library source intended for building other packages which
use the "example_generated" feature of the "%{crate}" crate.

%files       -n %{name}+example_generated-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
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
# * test sources are not included in published crates
%cargo_test -- --doc
%endif

%changelog
%autochangelog