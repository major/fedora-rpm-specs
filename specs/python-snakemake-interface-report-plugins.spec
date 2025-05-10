# Work around a circular dependency on snakemake.
%bcond bootstrap 0

Name:           python-snakemake-interface-report-plugins
Version:        1.1.0
Release:        %autorelease
Summary:        The interface for Snakemake report plugins

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-report-plugins
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-interface-report-plugins-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_interface_report_plugins

BuildArch:      noarch

%if %{without bootstrap}
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8.5
%endif

%global common_description %{expand:
This package defines the interface between Snakemake and its report plugins.}

%description %{common_description}


%package -n python3-snakemake-interface-report-plugins
Summary:        %{summary}

%description -n python3-snakemake-interface-report-plugins %{common_description}


%check -a
%if %{without bootstrap}
%pytest -v tests/tests.py
%endif


%files -n python3-snakemake-interface-report-plugins -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
