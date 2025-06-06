# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate vsimd

Name:           rust-vsimd
Version:        0.8.0
Release:        %autorelease
Summary:        SIMD utilities

License:        MIT
URL:            https://crates.io/crates/vsimd
Source:         %{crates_source}
# * https://github.com/Nugine/simd/commit/c6540229a0f02c14eedfa4ed8694815cd6410ba7
Source10:       https://github.com/Nugine/simd/raw/refs/tags/v%{version}/LICENSE
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          vsimd-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * Update const-str to 0.6. This is just a dev-depencency. We have not
#   suggested updating upstream because this would increase the MSRV from 1.63
#   to 1.77, and we suspect that (especially considering both libraries are by
#   the same author) upstream is trying to avoid this.
Patch:          vsimd-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
SIMD utilities.}

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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+detect-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+detect-devel %{_description}

This package contains library source intended for building other packages which
use the "detect" feature of the "%{crate}" crate.

%files       -n %{name}+detect-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
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
cp -p '%{SOURCE10}' .

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
