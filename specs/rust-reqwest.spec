# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate reqwest

Name:           rust-reqwest
Version:        0.12.22
Release:        %autorelease
Summary:        Higher level HTTP client library

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/reqwest
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          reqwest-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop macOS-specific features
# * drop unused support for HTTP/3
Patch:          reqwest-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Higher level HTTP client library.}

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

%package     -n %{name}+__rustls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__rustls-devel %{_description}

This package contains library source intended for building other packages which
use the "__rustls" feature of the "%{crate}" crate.

%files       -n %{name}+__rustls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+__rustls-ring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__rustls-ring-devel %{_description}

This package contains library source intended for building other packages which
use the "__rustls-ring" feature of the "%{crate}" crate.

%files       -n %{name}+__rustls-ring-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+__tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__tls-devel %{_description}

This package contains library source intended for building other packages which
use the "__tls" feature of the "%{crate}" crate.

%files       -n %{name}+__tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blocking-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-devel %{_description}

This package contains library source intended for building other packages which
use the "blocking" feature of the "%{crate}" crate.

%files       -n %{name}+blocking-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+brotli-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+brotli-devel %{_description}

This package contains library source intended for building other packages which
use the "brotli" feature of the "%{crate}" crate.

%files       -n %{name}+brotli-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+charset-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+charset-devel %{_description}

This package contains library source intended for building other packages which
use the "charset" feature of the "%{crate}" crate.

%files       -n %{name}+charset-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cookies-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cookies-devel %{_description}

This package contains library source intended for building other packages which
use the "cookies" feature of the "%{crate}" crate.

%files       -n %{name}+cookies-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+default-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "default-tls" feature of the "%{crate}" crate.

%files       -n %{name}+default-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+deflate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deflate-devel %{_description}

This package contains library source intended for building other packages which
use the "deflate" feature of the "%{crate}" crate.

%files       -n %{name}+deflate-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gzip-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gzip-devel %{_description}

This package contains library source intended for building other packages which
use the "gzip" feature of the "%{crate}" crate.

%files       -n %{name}+gzip-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+h2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+h2-devel %{_description}

This package contains library source intended for building other packages which
use the "h2" feature of the "%{crate}" crate.

%files       -n %{name}+h2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hickory-dns-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hickory-dns-devel %{_description}

This package contains library source intended for building other packages which
use the "hickory-dns" feature of the "%{crate}" crate.

%files       -n %{name}+hickory-dns-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http2-devel %{_description}

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%files       -n %{name}+http2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+multipart-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+multipart-devel %{_description}

This package contains library source intended for building other packages which
use the "multipart" feature of the "%{crate}" crate.

%files       -n %{name}+multipart-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%files       -n %{name}+native-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+native-tls-alpn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-alpn-devel %{_description}

This package contains library source intended for building other packages which
use the "native-tls-alpn" feature of the "%{crate}" crate.

%files       -n %{name}+native-tls-alpn-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls-tls" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-tls-manual-roots-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-tls-manual-roots-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls-tls-manual-roots" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-tls-manual-roots-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-tls-manual-roots-no-provider-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-tls-manual-roots-no-provider-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls-tls-manual-roots-no-provider" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-tls-manual-roots-no-provider-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-tls-native-roots-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-tls-native-roots-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls-tls-native-roots" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-tls-native-roots-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-tls-native-roots-no-provider-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-tls-native-roots-no-provider-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls-tls-native-roots-no-provider" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-tls-native-roots-no-provider-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-tls-no-provider-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-tls-no-provider-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls-tls-no-provider" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-tls-no-provider-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-tls-webpki-roots-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-tls-webpki-roots-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls-tls-webpki-roots" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-tls-webpki-roots-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-tls-webpki-roots-no-provider-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-tls-webpki-roots-no-provider-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls-tls-webpki-roots-no-provider" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-tls-webpki-roots-no-provider-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+socks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+socks-devel %{_description}

This package contains library source intended for building other packages which
use the "socks" feature of the "%{crate}" crate.

%files       -n %{name}+socks-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+stream-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stream-devel %{_description}

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

%files       -n %{name}+stream-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+system-proxy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+system-proxy-devel %{_description}

This package contains library source intended for building other packages which
use the "system-proxy" feature of the "%{crate}" crate.

%files       -n %{name}+system-proxy-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+trust-dns-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+trust-dns-devel %{_description}

This package contains library source intended for building other packages which
use the "trust-dns" feature of the "%{crate}" crate.

%files       -n %{name}+trust-dns-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zstd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zstd-devel %{_description}

This package contains library source intended for building other packages which
use the "zstd" feature of the "%{crate}" crate.

%files       -n %{name}+zstd-devel
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
# * skip tests which require internet access
%{cargo_test -- -- --exact %{shrink:
    --skip test_allowed_methods
    --skip test_badssl_modern
    --skip test_badssl_self_signed
    --skip test_tls_info
}}
%endif

%changelog
%autochangelog
