# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate p256

Name:           rust-p256
Version:        0.13.2
Release:        %autorelease
Summary:        Pure Rust implementation of the NIST P-256 elliptic curve

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/p256
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused, benchmark-only criterion dev-dependency
Patch:          p256-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Pure Rust implementation of the NIST P-256 (a.k.a. secp256r1,
prime256v1) elliptic curve as defined in SP 800-186, with support for
ECDH, ECDSA signing/verification, and general purpose curve arithmetic.}

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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+arithmetic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arithmetic-devel %{_description}

This package contains library source intended for building other packages which
use the "arithmetic" feature of the "%{crate}" crate.

%files       -n %{name}+arithmetic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bits-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bits-devel %{_description}

This package contains library source intended for building other packages which
use the "bits" feature of the "%{crate}" crate.

%files       -n %{name}+bits-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+digest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+digest-devel %{_description}

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%files       -n %{name}+digest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ecdh-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ecdh-devel %{_description}

This package contains library source intended for building other packages which
use the "ecdh" feature of the "%{crate}" crate.

%files       -n %{name}+ecdh-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ecdsa-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ecdsa-devel %{_description}

This package contains library source intended for building other packages which
use the "ecdsa" feature of the "%{crate}" crate.

%files       -n %{name}+ecdsa-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ecdsa-core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ecdsa-core-devel %{_description}

This package contains library source intended for building other packages which
use the "ecdsa-core" feature of the "%{crate}" crate.

%files       -n %{name}+ecdsa-core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+expose-field-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+expose-field-devel %{_description}

This package contains library source intended for building other packages which
use the "expose-field" feature of the "%{crate}" crate.

%files       -n %{name}+expose-field-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hash2curve-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hash2curve-devel %{_description}

This package contains library source intended for building other packages which
use the "hash2curve" feature of the "%{crate}" crate.

%files       -n %{name}+hash2curve-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+jwk-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+jwk-devel %{_description}

This package contains library source intended for building other packages which
use the "jwk" feature of the "%{crate}" crate.

%files       -n %{name}+jwk-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pem-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pem-devel %{_description}

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%files       -n %{name}+pem-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pkcs8-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pkcs8-devel %{_description}

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%files       -n %{name}+pkcs8-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serdect-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serdect-devel %{_description}

This package contains library source intended for building other packages which
use the "serdect" feature of the "%{crate}" crate.

%files       -n %{name}+serdect-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sha2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sha2-devel %{_description}

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%files       -n %{name}+sha2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sha256-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sha256-devel %{_description}

This package contains library source intended for building other packages which
use the "sha256" feature of the "%{crate}" crate.

%files       -n %{name}+sha256-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+test-vectors-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test-vectors-devel %{_description}

This package contains library source intended for building other packages which
use the "test-vectors" feature of the "%{crate}" crate.

%files       -n %{name}+test-vectors-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+voprf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+voprf-devel %{_description}

This package contains library source intended for building other packages which
use the "voprf" feature of the "%{crate}" crate.

%files       -n %{name}+voprf-devel
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