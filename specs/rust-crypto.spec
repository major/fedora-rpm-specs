# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate crypto

Name:           rust-crypto
Version:        0.5.1
Release:        %autorelease
Summary:        Facade crate for all of the RustCrypto traits

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/crypto
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Facade crate for all of the RustCrypto traits (e.g. `aead`, `cipher`,
`digest`).}

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

%package     -n %{name}+aead-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+aead-devel %{_description}

This package contains library source intended for building other packages which
use the "aead" feature of the "%{crate}" crate.

%files       -n %{name}+aead-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cipher-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cipher-devel %{_description}

This package contains library source intended for building other packages which
use the "cipher" feature of the "%{crate}" crate.

%files       -n %{name}+cipher-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+digest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+digest-devel %{_description}

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%files       -n %{name}+digest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+elliptic-curve-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+elliptic-curve-devel %{_description}

This package contains library source intended for building other packages which
use the "elliptic-curve" feature of the "%{crate}" crate.

%files       -n %{name}+elliptic-curve-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+getrandom-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+getrandom-devel %{_description}

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%files       -n %{name}+getrandom-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+password-hash-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+password-hash-devel %{_description}

This package contains library source intended for building other packages which
use the "password-hash" feature of the "%{crate}" crate.

%files       -n %{name}+password-hash-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rand_core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand_core-devel %{_description}

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%files       -n %{name}+rand_core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+signature-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+signature-devel %{_description}

This package contains library source intended for building other packages which
use the "signature" feature of the "%{crate}" crate.

%files       -n %{name}+signature-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+universal-hash-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+universal-hash-devel %{_description}

This package contains library source intended for building other packages which
use the "universal-hash" feature of the "%{crate}" crate.

%files       -n %{name}+universal-hash-devel
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
