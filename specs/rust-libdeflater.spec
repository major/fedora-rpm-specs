# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate libdeflater

Name:           rust-libdeflater
Version:        1.21.0
Release:        %autorelease
Summary:        Bindings to libdeflate for DEFLATE

License:        Apache-2.0
URL:            https://crates.io/crates/libdeflater
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli

%global _description %{expand:
Bindings to libdeflate for DEFLATE (de)compression exposed as non-
streaming buffer operations. Contains bindings for raw deflate, zlib,
and gzip data.}

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
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dynamic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dynamic-devel %{_description}

This package contains library source intended for building other packages which
use the "dynamic" feature of the "%{crate}" crate.

%files       -n %{name}+dynamic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+freestanding-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+freestanding-devel %{_description}

This package contains library source intended for building other packages which
use the "freestanding" feature of the "%{crate}" crate.

%files       -n %{name}+freestanding-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+use_rust_alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_rust_alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "use_rust_alloc" feature of the "%{crate}" crate.

%files       -n %{name}+use_rust_alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Do not depend on criterion; it is needed only for benchmarks.
tomcli set Cargo.toml del dev-dependencies.criterion

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