%global _with_bootstrap 1
# Work around a circular dependency on snakemake and on
# python-snakemake-executor-plugin-cluster-generic.
%bcond bootstrap 0

Name:           python-snakemake-interface-executor-plugins
Version:        9.3.5
Release:        %autorelease
Summary:        Stable interface for interactions between Snakemake and its executor plugins

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-executor-plugins
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-interface-executor-plugins-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_interface_executor_plugins

BuildArch:      noarch

%if %{without bootstrap}
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8
BuildRequires:  %{py3_dist snakemake-executor-plugin-cluster-generic}
%endif

%global common_description %{expand:
This package provides a stable interface for interactions between Snakemake and
its executor plugins.}

%description %{common_description}


%package -n python3-snakemake-interface-executor-plugins
Summary:        %{summary}

%description -n python3-snakemake-interface-executor-plugins %{common_description}


%check -a
%if %{without bootstrap}
%pytest -v tests/tests.py
%endif


%files -n python3-snakemake-interface-executor-plugins -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
