%global srcname jiter
%global _description %{summary}.

Name:           python-%{srcname}
Version:        0.9.0
Release:        %autorelease
Summary:        Fast iterable JSON parser

# python-jiter is MIT only, but the rest are rust libraries
# based on cargo_license_summary output:
#
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0 (duplicate)
License:        %{shrink:
                (Apache-2.0 OR MIT) AND
                (BSD-2-Clause OR Apache-2.0 OR MIT) AND
                MIT
                }
URL:            https://github.com/pydantic/jiter/
Source:         %{pypi_source %{srcname}}

BuildRequires:  python3-devel
BuildRequires:  tomcli

# For included rust code
BuildRequires:  cargo-rpm-macros

# For tests
BuildRequires:  python3dist(dirty-equals)
BuildRequires:  python3dist(pytest)

%description
%{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}
# There is no top-level LICENSE file, but the one from the bundled jiter crate
# is the correct license.
mv crates/jiter/LICENSE ./

# We want to use the system copy of the jiter crate, but we need the JSON data
# files from its benchmarks for testing the Python extension.
find crates/jiter -mindepth 1 -maxdepth 1 ! -name benches -exec rm -rv '{}' '+'
find crates/jiter/benches -type f ! -name '*.json' -print -delete

# E.g., for 0.5.0, this would allow 0.5.x.
tomcli set crates/jiter-python/Cargo.toml str dependencies.jiter.version "%{version}"
tomcli set crates/jiter-python/Cargo.toml del dependencies.jiter.path

# This feature only applies to Windows, and is hidden in our PyO3 packages.
# We can and should remove it with no consequence.
tomcli set pyproject.toml lists delitem \
    tool.maturin.features pyo3/generate-import-lib
tomcli set crates/jiter-python/Cargo.toml lists delitem \
    features.extension-module pyo3/generate-import-lib

%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires -a
%pyproject_buildrequires


%build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%check
%pyproject_check_import
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
