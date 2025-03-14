# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate x509-cert

Name:           rust-x509-cert
Version:        0.2.5
Release:        %autorelease
Summary:        Pure Rust implementation of the X.509 PKI Certificate format from RFC 5280

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/x509-cert
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused sct feature / tls_codec dependency
# * bump rstest dev-dependency from 0.18 to 0.23
Patch:          x509-cert-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Pure Rust implementation of the X.509 Public Key Infrastructure
Certificate format as described in RFC 5280.}

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
%exclude %{crate_instdir}/tests/examples/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+arbitrary-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary-devel %{_description}

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%files       -n %{name}+arbitrary-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+builder-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+builder-devel %{_description}

This package contains library source intended for building other packages which
use the "builder" feature of the "%{crate}" crate.

%files       -n %{name}+builder-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hazmat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hazmat-devel %{_description}

This package contains library source intended for building other packages which
use the "hazmat" feature of the "%{crate}" crate.

%files       -n %{name}+hazmat-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pem-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pem-devel %{_description}

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%files       -n %{name}+pem-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sha1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sha1-devel %{_description}

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%files       -n %{name}+sha1-devel
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
