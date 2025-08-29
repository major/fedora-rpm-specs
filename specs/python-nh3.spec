Name:           python-nh3
Version:        0.3.0
Release:        %autorelease
Summary:        Python binding to Ammonia HTML sanitizer Rust crate
License:        MIT
URL:            https://github.com/messense/nh3
Source:         %{pypi_source nh3}

# Omit the generate-import-lib feature of the pyo3 dependency, since it is
# specific to Windows, and we do not package it.
Patch:          generate-import-lib-dep.patch

BuildRequires:  cargo-rpm-macros
BuildRequires:  python3-devel

# For tests
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Python binding to Ammonia HTML sanitizer Rust crate.}

%description %_description

%package -n python3-nh3
Summary:        %{summary}
# Rust crates compiled into the executable contribute additional license terms.
# Full license breakdown in LICENSES.dependencies. To obtain the following
# list of licenses, build the package and note the output of
# %%{cargo_license_summary}.
#
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unicode-3.0
License:        %{license} AND (Apache-2.0 OR MIT) AND Unicode-3.0

%description -n python3-nh3 %_description


%prep
%autosetup -p1 -n nh3-%{version}

%cargo_prep


%generate_buildrequires
%pyproject_buildrequires
%cargo_generate_buildrequires


%build
export RUSTFLAGS='%{build_rustflags}'
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l nh3


%check
%pytest -vv


%files -n python3-nh3 -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
