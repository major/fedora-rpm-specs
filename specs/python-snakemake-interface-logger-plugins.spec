# Test dependency, not yet packaged: python-snakemake-logger-plugin-rich
#
# Blocked for now by:
#
# Please select a license
# https://github.com/cademirch/snakemake-logger-plugin-rich/issues/25
%bcond tests 0

Name:           python-snakemake-interface-logger-plugins
Version:        2.0.0
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

%if %{with tests}
# See: [tool.pixi.feature.dev.dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist snakemake-interface-common}
BuildRequires:  %{py3_dist snakemake_logger_plugin_rich}
%endif

%global common_description %{expand:
This package provides a stable interface for interactions between Snakemake and
its logger plugins.}

%description %{common_description}


%package -n python3-snakemake-interface-logger-plugins
Summary:        %{summary}

%description -n python3-snakemake-interface-logger-plugins %{common_description}


%if %{with tests}
%check -a
%pytest -v tests/tests.py
%endif


%files -n python3-snakemake-interface-logger-plugins -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
