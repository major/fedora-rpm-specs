# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate jsonwebtoken

Name:           rust-jsonwebtoken
Version:        9.3.1
Release:        %autorelease
Summary:        Create and decode JWTs in a strongly typed way

License:        MIT
URL:            https://crates.io/crates/jsonwebtoken
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          jsonwebtoken-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop criterion and wasm_bindgen_test dependencies
Patch:          jsonwebtoken-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Create and decode JWTs in a strongly typed way.}

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
%exclude %{crate_instdir}/tests/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pem-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pem-devel %{_description}

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%files       -n %{name}+pem-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+simple_asn1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simple_asn1-devel %{_description}

This package contains library source intended for building other packages which
use the "simple_asn1" feature of the "%{crate}" crate.

%files       -n %{name}+simple_asn1-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+use_pem-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_pem-devel %{_description}

This package contains library source intended for building other packages which
use the "use_pem" feature of the "%{crate}" crate.

%files       -n %{name}+use_pem-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Drop usage of wasm_bindgen_test
grep -lr wasm_bindgen_test | xargs sed -i /wasm_bindgen_test/d

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
