# Generated by rust2rpm 26
# * tests can only be run in-tree
%bcond_with check
%global debug_package %{nil}

%global crate cxxbridge-macro

Name:           rust-cxxbridge-macro
Version:        1.0.128
Release:        %autorelease
Summary:        Implementation detail of the cxx crate

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cxxbridge-macro
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Implementation detail of the `cxx` crate.}

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

%package     -n %{name}+clang-ast-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clang-ast-devel %{_description}

This package contains library source intended for building other packages which
use the "clang-ast" feature of the "%{crate}" crate.

%files       -n %{name}+clang-ast-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+experimental-async-fn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+experimental-async-fn-devel %{_description}

This package contains library source intended for building other packages which
use the "experimental-async-fn" feature of the "%{crate}" crate.

%files       -n %{name}+experimental-async-fn-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+flate2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+flate2-devel %{_description}

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

%files       -n %{name}+flate2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_derive-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_derive" feature of the "%{crate}" crate.

%files       -n %{name}+serde_derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%files       -n %{name}+serde_json-devel
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