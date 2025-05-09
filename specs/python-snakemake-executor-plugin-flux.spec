Name:           python-snakemake-executor-plugin-flux
Version:        0.1.1
Release:        %autorelease
Summary:        A snakemake executor plugin for the Flux scheduler

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-flux
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-flux-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_executor_plugin_flux

BuildArch:      noarch

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  snakemake >= 8
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
This serves both as an example implementation for an external snakemake plugin
and as a usable executor plugin for the Flux scheduler.}

%description %{common_description}


%package -n python3-snakemake-executor-plugin-flux
Summary:        %{summary}

%description -n python3-snakemake-executor-plugin-flux %{common_description}


%check -a
# While testing is stubbed out, there are no actual tests to collect:
# %%pytest -v tests/tests.py


%files -n python3-snakemake-executor-plugin-flux -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
