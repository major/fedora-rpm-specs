# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate oo7

Name:           rust-oo7
Version:        0.3.3
Release:        %autorelease
Summary:        Library to access freedesktop.org D-Bus Secret Service

License:        MIT
URL:            https://crates.io/crates/oo7
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
James Bond went on a new mission and this time as a Secret Service
provider.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%package     -n %{name}+async-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-std-devel %{_description}

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%files       -n %{name}+async-std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+local_tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+local_tests-devel %{_description}

This package contains library source intended for building other packages which
use the "local_tests" feature of the "%{crate}" crate.

%files       -n %{name}+local_tests-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+native_crypto-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native_crypto-devel %{_description}

This package contains library source intended for building other packages which
use the "native_crypto" feature of the "%{crate}" crate.

%files       -n %{name}+native_crypto-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+openssl_crypto-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl_crypto-devel %{_description}

This package contains library source intended for building other packages which
use the "openssl_crypto" feature of the "%{crate}" crate.

%files       -n %{name}+openssl_crypto-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tracing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tracing-devel %{_description}

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%files       -n %{name}+tracing-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-devel
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