%global srcname rpds-py
%global modname rpds_py

Name:           python-rpds-py
Version:        0.29.0
Release:        %autorelease
Summary:        Python bindings to the Rust rpds crate
# Full license breakdown in LICENSES.dependencies
License:        MIT AND Apache-2.0 AND (MIT OR Apache-2.0) AND MPL-2.0
URL:            https://github.com/crate-py/rpds
Source:         %{pypi_source %{modname}}

# The 'generate-import-lib' extension is only useful on MS Win
Patch:          do_not_require_win_only_pyo3_extension.patch
# Remove pytest-run-parallel from test dependencies
# and relax pytest version requirement
Patch:          fix_test_group_dependencies.patch

BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
BuildRequires:  python3-devel

# we don't use pyproject_buildrequires -g test because
# pytest 9 is not yet in repos
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Python bindings to the Rust rpds crate.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{modname}-%{version}

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
