# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate ed25519-compact

Name:           rust-ed25519-compact
Version:        2.1.1
Release:        %autorelease
Summary:        Small, self-contained, wasm-friendly Ed25519 implementation

License:        MIT
URL:            https://crates.io/crates/ed25519-compact
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          ed25519-compact-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A small, self-contained, wasm-friendly Ed25519 implementation.}

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

%package     -n %{name}+blind-keys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blind-keys-devel %{_description}

This package contains library source intended for building other packages which
use the "blind-keys" feature of the "%{crate}" crate.

%files       -n %{name}+blind-keys-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ct-codecs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ct-codecs-devel %{_description}

This package contains library source intended for building other packages which
use the "ct-codecs" feature of the "%{crate}" crate.

%files       -n %{name}+ct-codecs-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+disable-signatures-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+disable-signatures-devel %{_description}

This package contains library source intended for building other packages which
use the "disable-signatures" feature of the "%{crate}" crate.

%files       -n %{name}+disable-signatures-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ed25519-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ed25519-devel %{_description}

This package contains library source intended for building other packages which
use the "ed25519" feature of the "%{crate}" crate.

%files       -n %{name}+ed25519-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+getrandom-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+getrandom-devel %{_description}

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%files       -n %{name}+getrandom-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+opt_size-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+opt_size-devel %{_description}

This package contains library source intended for building other packages which
use the "opt_size" feature of the "%{crate}" crate.

%files       -n %{name}+opt_size-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pem-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pem-devel %{_description}

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%files       -n %{name}+pem-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+random-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+random-devel %{_description}

This package contains library source intended for building other packages which
use the "random" feature of the "%{crate}" crate.

%files       -n %{name}+random-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+self-verify-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+self-verify-devel %{_description}

This package contains library source intended for building other packages which
use the "self-verify" feature of the "%{crate}" crate.

%files       -n %{name}+self-verify-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+traits-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+traits-devel %{_description}

This package contains library source intended for building other packages which
use the "traits" feature of the "%{crate}" crate.

%files       -n %{name}+traits-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+x25519-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+x25519-devel %{_description}

This package contains library source intended for building other packages which
use the "x25519" feature of the "%{crate}" crate.

%files       -n %{name}+x25519-devel
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
