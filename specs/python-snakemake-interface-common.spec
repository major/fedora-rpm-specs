# Work around a circular dependency on snakemake
%bcond bootstrap 0

Name:           python-snakemake-interface-common
Version:        1.22.0
Release:        %autorelease
Summary:        Common functions and classes for Snakemake and its plugins

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-common
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-interface-common-%{version}.tar.gz

# Do not upper-bound the version of packaging
Patch:          %{url}/pull/89.patch

BuildSystem:            pyproject
BuildOption(install):   -l snakemake_interface_common
%if %{without bootstrap}
BuildOption(generate_buildrequires): -g dev
%endif

BuildArch:      noarch

# See: [tool.pixi.feature.dev.dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-interface-common
Summary:        %{summary}

%description -n python3-snakemake-interface-common %{common_description}


%check -a
%if %{with bootstrap}
k="${k-}${k+ and }not test_snakemake_version"
%endif

%pytest -k "${k-}" -v tests/tests.py


%files -n python3-snakemake-interface-common -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
