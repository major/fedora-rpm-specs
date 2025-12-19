# Tests need to run in an environment with Slurm
%bcond tests 0

Name:           python-snakemake-executor-plugin-slurm-jobstep
Version:        0.4.0
Release:        %autorelease
Summary:        A Snakemake executor plugin for running srun jobs inside of SLURM jobs

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-slurm-jobstep
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-slurm-jobstep-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_executor_plugin_slurm_jobstep

BuildArch:      noarch

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  snakemake >= 8
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%global common_description %{expand:
A Snakemake executor plugin for running srun jobs inside of SLURM jobs (meant
for internal use by snakemake-executor-plugin-slurm).}

%description %{common_description}


%package -n python3-snakemake-executor-plugin-slurm-jobstep
Summary:        %{summary}

%description -n python3-snakemake-executor-plugin-slurm-jobstep %{common_description}


%check -a
%if %{with tests}
%pytest -v tests/tests.py
%endif


%files -n python3-snakemake-executor-plugin-slurm-jobstep -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
