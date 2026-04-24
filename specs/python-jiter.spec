Name:           python-jiter
Version:        0.14.0
Release:        %autorelease
Summary:        Fast iterable JSON parser

# python-jiter is MIT only, but the rest are rust libraries
# based on cargo_license_summary output:
#
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
License:        %{shrink:
    MIT AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0)
    }
URL:            https://github.com/pydantic/jiter
Source:         %{pypi_source jiter}

BuildSystem:            pyproject
BuildOption(install):   -l jiter

BuildRequires:  cargo-rpm-macros
BuildRequires:  tomcli

# The following are from the “dev” dependency group in the *workspace* pyproject.toml, not
# included in the PyPI sdist. We omit maturin (since it is already in the
# build-system.requires) and pytest-pretty (since it is purely cosmetic).
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist dirty-equals}

%global _description %{expand:
%{summary}.}

%description %{_description}


%package -n     python3-jiter
Summary:        %{summary}

%description -n python3-jiter %{_description}


%prep -a
# We want to use the system copy of the jiter crate, but we need the JSON data
# files from its benchmarks for testing the Python extension.
find crates/jiter -mindepth 1 -maxdepth 1 ! -name benches -exec rm -rv '{}' '+'
find crates/jiter/benches -type f ! -name '*.json' -print -delete
tomcli set Cargo.toml lists delitem workspace.members 'crates/jiter'

# Convert the path-based dependency on jiter to one on the separate rust-jiter
# package. It should suffice to have a SemVer-compatible version, but since
# these are developed in the same repository and workspace, it’s safest to
# ensure the versions remain exactly synchronized.
tomcli set crates/jiter-python/Cargo.toml str dependencies.jiter.version "=%{version}"
tomcli set crates/jiter-python/Cargo.toml del dependencies.jiter.path

# This feature only applies to Windows, and is hidden in our PyO3 packages.
# We can and should remove it with no consequence.
tomcli set pyproject.toml lists delitem \
    tool.maturin.features pyo3/generate-import-lib
tomcli set crates/jiter-python/Cargo.toml lists delitem \
    features.extension-module pyo3/generate-import-lib

%cargo_prep


%generate_buildrequires -p
%cargo_generate_buildrequires -a


%build -p
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies


%check -a
%pytest


%files -n python3-jiter -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
