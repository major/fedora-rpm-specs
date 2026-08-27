Name:           python-crate-ingredients
Version:        0.3.0
Release:        %autorelease
Summary:        Check contents of published Rust crates

License:        MIT
URL:            https://codeberg.org/decathorpe/ingredients
Source:         %{pypi_source crate_ingredients}

# build against published "ingredients" crate instead of copy bundled for PyPI
Patch:          0001-Unbundle-ingredients-crate.patch

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros

%global _description %{expand:
This package contains Python bindings for the ingredients crate, which
implements checks for the contents ("ingredients") of published Rust
crates.}

%description %_description

%package -n python3-crate-ingredients
Summary:        Check contents of published Rust crates

# required for "cargo metadata" calls via cargo_metadata crate
Requires:       cargo
# required for cloning upstream git repositories
Requires:       git-core

# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
License:        %{shrink:
    MIT
    AND Apache-2.0
    AND Unicode-3.0
    AND Zlib
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

%description -n python3-crate-ingredients %_description

%files -n python3-crate-ingredients -f %{pyproject_files}
%doc README.md

%prep
%autosetup -C -p1
%cargo_prep
# drop bundled "ingredients" crate
rm -rf ingredients

%generate_buildrequires
# maturin requires that all dependencies are available,
# including optional dependencies for disabled features and dev-dependencies 
%cargo_generate_buildrequires -a -t
%pyproject_buildrequires

%build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l crate_ingredients

%check
# run import check only:
# * pytest unit tests require internet access
# * cargo test fails to compile doctests for cdylib targets
%pyproject_check_import

%changelog
%autochangelog
