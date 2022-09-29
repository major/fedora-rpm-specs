%bcond_with check
%global debug_package %{nil}

%global custom_cargo_build /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo build %{_smp_mflags} -Z avoid-dev-deps --release
%global custom_cargo_test /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo test %{_smp_mflags} -Z avoid-dev-deps --release --no-fail-fast

%global crate parsec-client

Name:           rust-%{crate}
Version:        0.14.1
Release:        %autorelease
Summary:        Parsec Client library for the Rust ecosystem

License:        Apache-2.0
URL:            https://crates.io/crates/parsec-client
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  protobuf-compiler
BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Parsec Client library for the Rust ecosystem.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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
%ghost %{cargo_registry}/Cargo.toml

%package     -n %{name}+spiffe-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+spiffe-devel %{_description}

This package contains library source intended for building other packages which
use the "spiffe" feature of the "%{crate}" crate.

%files       -n %{name}+spiffe-devel
%ghost %{cargo_registry}/Cargo.toml

%package     -n %{name}+spiffe-auth-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+spiffe-auth-devel %{_description}

This package contains library source intended for building other packages which
use the "spiffe-auth" feature of the "%{crate}" crate.

%files       -n %{name}+spiffe-auth-devel
%ghost %{cargo_registry}/Cargo.toml

%package     -n %{name}+testing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing-devel %{_description}

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%files       -n %{name}+testing-devel
%ghost %{cargo_registry}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%custom_cargo_build

%install
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_install

%if %{with check}
%check
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%custom_cargo_test
%endif

%changelog
%autochangelog
