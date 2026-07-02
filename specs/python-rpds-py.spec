%global srcname rpds-py
%global modname rpds_py

Name:           python-rpds-py
Version:        2026.6.3
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
