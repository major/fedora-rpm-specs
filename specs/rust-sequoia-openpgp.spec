# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate sequoia-openpgp

Name:           rust-sequoia-openpgp
Version:        2.0.0
Release:        %autorelease
Summary:        OpenPGP data types and associated machinery

License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-openpgp
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          sequoia-openpgp-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop unused, benchmark-only criterion dev-dependency
Patch:          sequoia-openpgp-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
OpenPGP data types and associated machinery.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
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

%package     -n %{name}+__implicit-crypto-backend-for-tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__implicit-crypto-backend-for-tests-devel %{_description}

This package contains library source intended for building other packages which
use the "__implicit-crypto-backend-for-tests" feature of the "%{crate}" crate.

%files       -n %{name}+__implicit-crypto-backend-for-tests-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+allow-experimental-crypto-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+allow-experimental-crypto-devel %{_description}

This package contains library source intended for building other packages which
use the "allow-experimental-crypto" feature of the "%{crate}" crate.

%files       -n %{name}+allow-experimental-crypto-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+allow-variable-time-crypto-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+allow-variable-time-crypto-devel %{_description}

This package contains library source intended for building other packages which
use the "allow-variable-time-crypto" feature of the "%{crate}" crate.

%files       -n %{name}+allow-variable-time-crypto-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compression-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compression-devel %{_description}

This package contains library source intended for building other packages which
use the "compression" feature of the "%{crate}" crate.

%files       -n %{name}+compression-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compression-bzip2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compression-bzip2-devel %{_description}

This package contains library source intended for building other packages which
use the "compression-bzip2" feature of the "%{crate}" crate.

%files       -n %{name}+compression-bzip2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compression-deflate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compression-deflate-devel %{_description}

This package contains library source intended for building other packages which
use the "compression-deflate" feature of the "%{crate}" crate.

%files       -n %{name}+compression-deflate-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crypto-nettle-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crypto-nettle-devel %{_description}

This package contains library source intended for building other packages which
use the "crypto-nettle" feature of the "%{crate}" crate.

%files       -n %{name}+crypto-nettle-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crypto-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crypto-openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "crypto-openssl" feature of the "%{crate}" crate.

%files       -n %{name}+crypto-openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crypto-rust-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crypto-rust-devel %{_description}

This package contains library source intended for building other packages which
use the "crypto-rust" feature of the "%{crate}" crate.

%files       -n %{name}+crypto-rust-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
# * ensure all dependencies for tests are generated
%cargo_generate_buildrequires -f crypto-nettle,crypto-openssl,crypto-rust,compression

%build
# * build with the Nettle crypto backend (default)
%cargo_build -n -f crypto-nettle,compression
# * build with the OpenSSL crypto backend
%cargo_build -n -f crypto-openssl,compression
# * build with the RustCrypto crypto backend
%cargo_build -n -f crypto-rust,compression,allow-experimental-crypto,allow-variable-time-crypto

%install
%cargo_install

%if %{with check}
%check
# * skip tests that exploit undefined behaviour and are not reliable:
#   https://gitlab.com/sequoia-pgp/sequoia/-/issues/1064
# * run tests with the Nettle crypto backend (default)
%cargo_test -n -f crypto-nettle,compression -- -- --skip leak_tests
# * run tests with the OpenSSL crypto backend
%cargo_test -n -f crypto-openssl,compression -- -- --skip leak_tests
# * run tests with the RustCrypto crypto backend
%cargo_test -n -f crypto-rust,compression,allow-experimental-crypto,allow-variable-time-crypto -- -- --skip leak_tests
%endif

%changelog
%autochangelog
