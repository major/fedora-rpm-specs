# Generated by rust2rpm 27
# * /etc/hosts and /etc/resolv.conf are not available in mock
# * no internet connectivity in mock
%bcond check 0
%global debug_package %{nil}

%global crate hickory-resolver

Name:           rust-hickory-resolver
Version:        0.24.4
Release:        %autorelease
Summary:        Hickory DNS is a safe and secure DNS library

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hickory-resolver
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          hickory-resolver-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * remove unused tracing-subscriber dev-dependency
Patch:          hickory-resolver-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Hickory DNS is a safe and secure DNS library. This Resolver library
uses the Client library to perform all DNS queries. The Resolver is
intended to be a high-level library for any DNS record resolution see
Resolver and AsyncResolver for supported resolution types. The Client
can be used for other queries.}

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

%package     -n %{name}+backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-devel %{_description}

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%files       -n %{name}+backtrace-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dns-over-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dns-over-native-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "dns-over-native-tls" feature of the "%{crate}" crate.

%files       -n %{name}+dns-over-native-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dns-over-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dns-over-openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "dns-over-openssl" feature of the "%{crate}" crate.

%files       -n %{name}+dns-over-openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dns-over-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dns-over-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "dns-over-tls" feature of the "%{crate}" crate.

%files       -n %{name}+dns-over-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dnssec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dnssec-devel %{_description}

This package contains library source intended for building other packages which
use the "dnssec" feature of the "%{crate}" crate.

%files       -n %{name}+dnssec-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dnssec-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dnssec-openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "dnssec-openssl" feature of the "%{crate}" crate.

%files       -n %{name}+dnssec-openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+resolv-conf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+resolv-conf-devel %{_description}

This package contains library source intended for building other packages which
use the "resolv-conf" feature of the "%{crate}" crate.

%files       -n %{name}+resolv-conf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-config-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-config-devel %{_description}

This package contains library source intended for building other packages which
use the "serde-config" feature of the "%{crate}" crate.

%files       -n %{name}+serde-config-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+system-config-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+system-config-devel %{_description}

This package contains library source intended for building other packages which
use the "system-config" feature of the "%{crate}" crate.

%files       -n %{name}+system-config-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+testing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing-devel %{_description}

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%files       -n %{name}+testing-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-native-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio-native-tls" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-native-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio-openssl" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-runtime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-runtime-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio-runtime" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-runtime-devel
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
