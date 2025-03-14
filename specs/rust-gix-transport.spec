# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate gix-transport

Name:           rust-gix-transport
Version:        0.45.0
Release:        %autorelease
Summary:        Implementation of the git transport layer used by gix

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-transport
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Patch out macos feature of reqwest
Patch:          gix-transport-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A crate of the gitoxide project dedicated to implementing the git
transport layer.}

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
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-client-devel %{_description}

This package contains library source intended for building other packages which
use the "async-client" feature of the "%{crate}" crate.

%files       -n %{name}+async-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-std-devel %{_description}

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%files       -n %{name}+async-std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-trait-devel %{_description}

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%files       -n %{name}+async-trait-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+base64-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+base64-devel %{_description}

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%files       -n %{name}+base64-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blocking-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-client-devel %{_description}

This package contains library source intended for building other packages which
use the "blocking-client" feature of the "%{crate}" crate.

%files       -n %{name}+blocking-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+curl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+curl-devel %{_description}

This package contains library source intended for building other packages which
use the "curl" feature of the "%{crate}" crate.

%files       -n %{name}+curl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+document-features-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+document-features-devel %{_description}

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%files       -n %{name}+document-features-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-io-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%files       -n %{name}+futures-io-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-lite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-lite-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-lite" feature of the "%{crate}" crate.

%files       -n %{name}+futures-lite-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gix-credentials-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gix-credentials-devel %{_description}

This package contains library source intended for building other packages which
use the "gix-credentials" feature of the "%{crate}" crate.

%files       -n %{name}+gix-credentials-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-client-devel %{_description}

This package contains library source intended for building other packages which
use the "http-client" feature of the "%{crate}" crate.

%files       -n %{name}+http-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-client-curl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-client-curl-devel %{_description}

This package contains library source intended for building other packages which
use the "http-client-curl" feature of the "%{crate}" crate.

%files       -n %{name}+http-client-curl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-client-reqwest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-client-reqwest-devel %{_description}

This package contains library source intended for building other packages which
use the "http-client-reqwest" feature of the "%{crate}" crate.

%files       -n %{name}+http-client-reqwest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-client-reqwest-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-client-reqwest-native-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "http-client-reqwest-native-tls" feature of the "%{crate}" crate.

%files       -n %{name}+http-client-reqwest-native-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-client-reqwest-rust-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-client-reqwest-rust-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "http-client-reqwest-rust-tls" feature of the "%{crate}" crate.

%files       -n %{name}+http-client-reqwest-rust-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http-client-reqwest-rust-tls-trust-dns-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-client-reqwest-rust-tls-trust-dns-devel %{_description}

This package contains library source intended for building other packages which
use the "http-client-reqwest-rust-tls-trust-dns" feature of the "%{crate}" crate.

%files       -n %{name}+http-client-reqwest-rust-tls-trust-dns-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pin-project-lite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pin-project-lite-devel %{_description}

This package contains library source intended for building other packages which
use the "pin-project-lite" feature of the "%{crate}" crate.

%files       -n %{name}+pin-project-lite-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+reqwest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reqwest-devel %{_description}

This package contains library source intended for building other packages which
use the "reqwest" feature of the "%{crate}" crate.

%files       -n %{name}+reqwest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
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
