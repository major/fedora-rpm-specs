Name:           python-snakemake-interface-common
Version:        1.17.4
Release:        %autorelease
Summary:        Common functions and classes for Snakemake and its plugins

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-common
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-interface-common-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_interface_common

BuildArch:      noarch

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-interface-common
Summary:        %{summary}

%description -n python3-snakemake-interface-common %{common_description}


%check -a
%pytest -v tests/tests.py


%files -n python3-snakemake-interface-common -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
