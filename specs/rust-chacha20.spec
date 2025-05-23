# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate chacha20

Name:           rust-chacha20
Version:        0.9.1
Release:        %autorelease
Summary:        ChaCha20 stream cipher

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/chacha20
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
The ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using
traits from the RustCrypto `cipher` crate, with optional architecture-
specific hardware acceleration (AVX2, SSE2). Additionally provides the
ChaCha8, ChaCha12, XChaCha20, XChaCha12 and XChaCha8 stream ciphers, and
also optional rand_core-compatible RNGs based on those ciphers.}

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

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zeroize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zeroize-devel %{_description}

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

%files       -n %{name}+zeroize-devel
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
