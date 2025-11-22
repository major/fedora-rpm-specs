Name:           python-jiter
Version:        0.11.1
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
URL:            https://github.com/pydantic/jiter/
Source:         %{pypi_source jiter}

BuildSystem:            pyproject
BuildOption(install):   -l jiter
BuildOption(generate_buildrequires): crates/jiter-python/tests/requirements.txt

BuildRequires:  cargo-rpm-macros
BuildRequires:  tomcli

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

# E.g., for 0.5.0, this would allow crate(jiter) 0.5.x.
tomcli set crates/jiter-python/Cargo.toml str dependencies.jiter.version "%{version}"
tomcli set crates/jiter-python/Cargo.toml del dependencies.jiter.path

# This feature only applies to Windows, and is hidden in our PyO3 packages.
# We can and should remove it with no consequence.
tomcli set pyproject.toml lists delitem \
    tool.maturin.features pyo3/generate-import-lib
tomcli set crates/jiter-python/Cargo.toml lists delitem \
    features.extension-module pyo3/generate-import-lib

# Remove a purely-cosmetic test dependency
sed -r -i 's/^pytest-pretty\b/# &/' crates/jiter-python/tests/requirements.txt

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
