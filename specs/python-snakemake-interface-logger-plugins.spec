Name:           python-snakemake-interface-logger-plugins
Version:        1.2.4
Release:        %autorelease
Summary:        Logger plugin interface for snakemake

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-interface-logger-plugins
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-interface-logger-plugins-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l snakemake_interface_logger_plugins

BuildArch:      noarch

# See: [tool.pixi.feature.dev.dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
This package provides a stable interface for interactions between Snakemake and
its logger plugins.}

%description %{common_description}


%package -n python3-snakemake-interface-logger-plugins
Summary:        %{summary}

%description -n python3-snakemake-interface-logger-plugins %{common_description}


%check -a
%pytest -v tests/tests.py


%files -n python3-snakemake-interface-logger-plugins -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
