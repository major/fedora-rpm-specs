# Generated by rust2rpm 26
# * tests can only be run in-tree
%bcond_with check
%global debug_package %{nil}

%global crate actix-tls

Name:           rust-actix-tls
Version:        3.4.0
Release:        %autorelease
Summary:        TLS acceptor and connector services for Actix ecosystem

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-tls
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused support for rustls
Patch:          actix-tls-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
TLS acceptor and connector services for Actix ecosystem.}

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
%doc %{crate_instdir}/CHANGES.md
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

%package     -n %{name}+accept-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+accept-devel %{_description}

This package contains library source intended for building other packages which
use the "accept" feature of the "%{crate}" crate.

%files       -n %{name}+accept-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+connect-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+connect-devel %{_description}

This package contains library source intended for building other packages which
use the "connect" feature of the "%{crate}" crate.

%files       -n %{name}+connect-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%files       -n %{name}+native-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%files       -n %{name}+openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+uri-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+uri-devel %{_description}

This package contains library source intended for building other packages which
use the "uri" feature of the "%{crate}" crate.

%files       -n %{name}+uri-devel
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