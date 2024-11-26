%global srcname jiter
%global _description %{summary}.

Name:           python-%{srcname}
Version:        0.7.1
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

# However, we want to use the system copy of the jiter crate.
rm -r crates/jiter

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
%pyproject_wheel

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE LICENSE.dependencies
%doc README.md


%changelog
%autochangelog
