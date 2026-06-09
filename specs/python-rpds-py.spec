%global srcname rpds-py
%global modname rpds_py

Name:           python-rpds-py
Version:        2026.5.1
Release:        %autorelease
Summary:        Python bindings to the Rust rpds crate
# Full license breakdown in LICENSES.dependencies
License:        MIT AND Apache-2.0 AND (MIT OR Apache-2.0) AND MPL-2.0
URL:            https://github.com/crate-py/rpds
Source:         %{pypi_source %{modname}}

# The 'generate-import-lib' extension is only useful on MS Win
Patch:          do_not_require_win_only_pyo3_extension.patch

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
