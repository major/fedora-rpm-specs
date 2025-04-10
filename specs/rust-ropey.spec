# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate ropey

Name:           rust-ropey
Version:        1.6.1
Release:        %autorelease
Summary:        Fast and robust text rope for Rust

License:        MIT
URL:            https://crates.io/crates/ropey
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Remove criterion dependency because it is only needed for benchmarking
Patch:          ropey-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A fast and robust text rope for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.md
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

%package     -n %{name}+cr_lines-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cr_lines-devel %{_description}

This package contains library source intended for building other packages which
use the "cr_lines" feature of the "%{crate}" crate.

%files       -n %{name}+cr_lines-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+simd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simd-devel %{_description}

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%files       -n %{name}+simd-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+small_chunks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+small_chunks-devel %{_description}

This package contains library source intended for building other packages which
use the "small_chunks" feature of the "%{crate}" crate.

%files       -n %{name}+small_chunks-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode_lines-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode_lines-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode_lines" feature of the "%{crate}" crate.

%files       -n %{name}+unicode_lines-devel
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
