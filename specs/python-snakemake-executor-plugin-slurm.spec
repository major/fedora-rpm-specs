%bcond tests 1

Name:           python-snakemake-executor-plugin-slurm
Version:        2.2.0
Release:        %autorelease
Summary:        A Snakemake executor plugin for submitting jobs to a SLURM cluster

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-slurm
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-slurm-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_executor_plugin_slurm

BuildArch:      noarch

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  snakemake >= 8
# If slurm is not installed, importing snakemake_executor_plugin_slurm
# produces:
#
# snakemake_interface_common.exceptions.WorkflowError: Neither 'sacct' nor
# 'squeue' commands are available on this system. At least one of these
# commands is required for job status queries.
BuildRequires:  slurm
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-executor-plugin-slurm
Summary:        %{summary}

# The plugin cannot even be imported without slurm; see the note above the
# corresponding BuildRequires.
Requires:       slurm

%description -n python3-snakemake-executor-plugin-slurm %{common_description}


%check -a
%if %{with tests}
# These tests seem to want to talk to a real cluster controller:
#
# tests/tests.py::TestEfficiencyReport::test_group_workflow
# tests/tests.py::TestEfficiencyReport::test_simple_workflow
# tests/tests.py::TestSLURMResources::test_group_workflow
# tests/tests.py::TestSLURMResources::test_simple_workflow
# tests/tests.py::TestWildcardsWithSlashes::test_group_workflow
# tests/tests.py::TestWildcardsWithSlashes::test_simple_workflow
# tests/tests.py::TestWorkflows::test_group_workflow
# tests/tests.py::TestWorkflows::test_simple_workflow
# tests/tests.py::TestWorkflowsRequeue::test_group_workflow
# tests/tests.py::TestWorkflowsRequeue::test_simple_workflow
k="${k-}${k+ and }not test_group_workflow"
k="${k-}${k+ and }not test_simple_workflow"

%pytest -k "${k-}" -v tests/tests.py
%endif


%files -n python3-snakemake-executor-plugin-slurm -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
