%global srcname rpds-py
%global modname rpds_py

Name:           python-rpds-py
Version:        2026.5.1
Release:        %autorelease
Summary:        Python bindings to the Rust rpds crate
# The package is MIT; statically-linked Rust dependencies are (from
# %%{cargo_license_summary}):
#
# MIT
# MIT OR Apache-2.0
#
# Full license breakdown in LICENSES.dependencies
License:        MIT AND (MIT OR Apache-2.0)
URL:            https://github.com/crate-py/rpds
Source:         %{pypi_source %{modname}}

# Update to PyO3 0.29, fixing RUSTSEC-2026-0176 and RUSTSEC-2026-0177.
# https://github.com/crate-py/rpds/commit/3b6dbc0bfc9f2b2cfa7e75d29eb23c3630372e20
# Released upstream in 2026.6.1, but this release is not yet on PyPI:
# https://github.com/crate-py/rpds/issues/279.
#
# Also drop the generate-import-lib feature, which was Windows-only, and is now
# deprecated: https://github.com/crate-py/rpds/pull/280.
Patch:          use_pyo3_0.29.patch

BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
BuildRequires:  python3-devel

%global _description %{expand:
Python bindings to the Rust rpds crate.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{modname}-%{version}
%pyproject_patch_dependency pytest-run-parallel:ignore

# Fix line terminations
dos2unix README* LICENSE* *.pyi


%cargo_prep


%generate_buildrequires
%pyproject_buildrequires -g test
%cargo_generate_buildrequires


%build
export RUSTFLAGS='%{build_rustflags}'
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l rpds


%check
%pytest -vv


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
