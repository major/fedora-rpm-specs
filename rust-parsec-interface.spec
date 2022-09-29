%bcond_without check
%global debug_package %{nil}

%global custom_cargo_build /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo build %{_smp_mflags} -Z avoid-dev-deps --release
%global custom_cargo_test /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo test %{_smp_mflags} -Z avoid-dev-deps --release --no-fail-fast

%global crate parsec-interface

Name:           rust-%{crate}
Version:        0.27.0
Release:        %autorelease
Summary:        Parsec interface library to communicate using the wire protocol

License:        Apache-2.0
URL:            https://crates.io/crates/parsec-interface
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  protobuf-compiler
BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Parsec interface library to communicate using the wire protocol.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%license %{crate_instdir}/parsec-operations/LICENSE
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

%package     -n %{name}+arbitrary-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary-devel %{_description}

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%files       -n %{name}+arbitrary-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fuzz-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fuzz-devel %{_description}

This package contains library source intended for building other packages which
use the "fuzz" feature of the "%{crate}" crate.

%files       -n %{name}+fuzz-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+prost-build-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+prost-build-devel %{_description}

This package contains library source intended for building other packages which
use the "prost-build" feature of the "%{crate}" crate.

%files       -n %{name}+prost-build-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+regenerate-protobuf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regenerate-protobuf-devel %{_description}

This package contains library source intended for building other packages which
use the "regenerate-protobuf" feature of the "%{crate}" crate.

%files       -n %{name}+regenerate-protobuf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+testing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing-devel %{_description}

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%files       -n %{name}+testing-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%custom_cargo_build

%install
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_install

%if %{with check}
%check
%custom_cargo_test
%endif

%changelog
%autochangelog
