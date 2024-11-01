# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate ndarray

Name:           rust-ndarray
Version:        0.16.1
Release:        %autorelease
Summary:        N-dimensional array for general elements and for numerics

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ndarray
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          ndarray-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * Remove oper test: Uses workspace-only crate ndarray-gen
Patch:          ndarray-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
An n-dimensional array for general elements and for numerics.
Lightweight array views and slicing; views support chunking and
splitting.}

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
%doc %{crate_instdir}/README-crates.io.md
%doc %{crate_instdir}/README-quick-start.md
%doc %{crate_instdir}/README.rst
%doc %{crate_instdir}/RELEASES.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+approx-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+approx-devel %{_description}

This package contains library source intended for building other packages which
use the "approx" feature of the "%{crate}" crate.

%files       -n %{name}+approx-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+matrixmultiply-threading-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+matrixmultiply-threading-devel %{_description}

This package contains library source intended for building other packages which
use the "matrixmultiply-threading" feature of the "%{crate}" crate.

%files       -n %{name}+matrixmultiply-threading-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+portable-atomic-critical-section-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+portable-atomic-critical-section-devel %{_description}

This package contains library source intended for building other packages which
use the "portable-atomic-critical-section" feature of the "%{crate}" crate.

%files       -n %{name}+portable-atomic-critical-section-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test-devel %{_description}

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%files       -n %{name}+test-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Remove upstream dev files
rm -r misc scripts clippy.toml rustfmt.toml

%generate_buildrequires
%cargo_generate_buildrequires -f default,matrixmultiply-threading,portable-atomic-critical-section,rayon,serde,std,test

%build
%cargo_build -f default,matrixmultiply-threading,portable-atomic-critical-section,rayon,serde,std,test

%install
%cargo_install -f default,matrixmultiply-threading,portable-atomic-critical-section,rayon,serde,std,test

%if %{with check}
%check
%cargo_test -f default,matrixmultiply-threading,portable-atomic-critical-section,rayon,serde,std,test
%endif

%changelog
%autochangelog
