# Work around a circular dependency on snakemake.
%bcond bootstrap 0

Name:           python-snakemake-interface-scheduler-plugins
Version:        2.0.1
Release:        %autorelease
Summary:        Scheduler plugin interface for snakemake

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-scheduler-plugins
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-interface-scheduler-plugins-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l snakemake_interface_scheduler_plugins

BuildArch:      noarch

%if %{without bootstrap}
# See: [tool.pixi.feature.dev.dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 9.10.0
%endif

%global common_description %{expand:
This package provides a stable interface for interactions between Snakemake and
its scheduler plugins.}

%description %{common_description}


%package -n python3-snakemake-interface-scheduler-plugins
Summary:        %{summary}

%description -n python3-snakemake-interface-scheduler-plugins %{common_description}


%check -a
%if %{without bootstrap}
%pytest -v tests/tests.py
%endif


%files -n python3-snakemake-interface-scheduler-plugins -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
