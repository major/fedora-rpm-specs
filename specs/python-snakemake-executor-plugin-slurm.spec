# Tests need to run in an environment with Slurm
%bcond tests 0

Name:           python-snakemake-executor-plugin-slurm
Version:        0.15.0
Release:        %autorelease
Summary:        A Snakemake executor plugin for submitting jobs to a SLURM cluster

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-slurm
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-slurm-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  snakemake >= 8
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-executor-plugin-slurm
Summary:        %{summary}

%description -n python3-snakemake-executor-plugin-slurm %{common_description}


%prep
%autosetup -n snakemake-executor-plugin-slurm-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_executor_plugin_slurm


%check
%pyproject_check_import

%if %{with tests}
%pytest -v tests/tests.py
%endif


%files -n python3-snakemake-executor-plugin-slurm -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
