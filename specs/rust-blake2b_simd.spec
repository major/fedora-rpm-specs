# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate blake2b_simd

Name:           rust-blake2b_simd
Version:        1.0.3
Release:        %autorelease
Summary:        Pure Rust BLAKE2b implementation with dynamic SIMD

License:        MIT
URL:            https://crates.io/crates/blake2b_simd
Source:         %{crates_source}
# * add missing license text: https://github.com/oconnor663/blake2_simd/pull/31
Source2:        https://github.com/oconnor663/blake2_simd/raw/refs/tags/1.0.3/LICENSE

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A pure Rust BLAKE2b implementation with dynamic SIMD.}

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

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+uninline_portable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+uninline_portable-devel %{_description}

This package contains library source intended for building other packages which
use the "uninline_portable" feature of the "%{crate}" crate.

%files       -n %{name}+uninline_portable-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
cp -p %{SOURCE2} .

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
