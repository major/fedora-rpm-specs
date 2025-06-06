# Generated by rust2rpm 27
# * tests can only be run in-tree
%bcond check 0
%global debug_package %{nil}

%global crate actix-web

Name:           rust-actix-web
Version:        4.11.0
Release:        %autorelease
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-web
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused support for brotli
# * drop unused support for io_uring
# * drop unused support for rustls
Patch:          actix-web-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Actix Web is a powerful, pragmatic, and extremely fast web framework for
Rust.}

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
%doc %{crate_instdir}/MIGRATION-0.x.md
%doc %{crate_instdir}/MIGRATION-1.0.md
%doc %{crate_instdir}/MIGRATION-2.0.md
%doc %{crate_instdir}/MIGRATION-3.0.md
%doc %{crate_instdir}/MIGRATION-4.0.md
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

%package     -n %{name}+__compress-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__compress-devel %{_description}

This package contains library source intended for building other packages which
use the "__compress" feature of the "%{crate}" crate.

%files       -n %{name}+__compress-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+__tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__tls-devel %{_description}

This package contains library source intended for building other packages which
use the "__tls" feature of the "%{crate}" crate.

%files       -n %{name}+__tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+actix-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+actix-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "actix-tls" feature of the "%{crate}" crate.

%files       -n %{name}+actix-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compat-devel %{_description}

This package contains library source intended for building other packages which
use the "compat" feature of the "%{crate}" crate.

%files       -n %{name}+compat-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compat-routing-macros-force-pub-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compat-routing-macros-force-pub-devel %{_description}

This package contains library source intended for building other packages which
use the "compat-routing-macros-force-pub" feature of the "%{crate}" crate.

%files       -n %{name}+compat-routing-macros-force-pub-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compress-gzip-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compress-gzip-devel %{_description}

This package contains library source intended for building other packages which
use the "compress-gzip" feature of the "%{crate}" crate.

%files       -n %{name}+compress-gzip-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compress-zstd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compress-zstd-devel %{_description}

This package contains library source intended for building other packages which
use the "compress-zstd" feature of the "%{crate}" crate.

%files       -n %{name}+compress-zstd-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cookies-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cookies-devel %{_description}

This package contains library source intended for building other packages which
use the "cookies" feature of the "%{crate}" crate.

%files       -n %{name}+cookies-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http2-devel %{_description}

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%files       -n %{name}+http2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macros-devel %{_description}

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%files       -n %{name}+macros-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%files       -n %{name}+openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+secure-cookies-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+secure-cookies-devel %{_description}

This package contains library source intended for building other packages which
use the "secure-cookies" feature of the "%{crate}" crate.

%files       -n %{name}+secure-cookies-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-devel
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
