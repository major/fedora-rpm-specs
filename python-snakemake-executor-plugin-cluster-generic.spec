Name:           python-snakemake-executor-plugin-cluster-generic
Version:        1.0.9
Release:        %autorelease
Summary:        Generic cluster executor for Snakemake

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-cluster-generic
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-cluster-generic-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8

%global common_description %{expand:
A generic Snakemake executor plugin for submission of jobs to cluster systems
that provide a submission command that accepts the path to a job script (like
PBS, LSF, SGE, ...).}

%description %{common_description}


%package -n python3-snakemake-executor-plugin-cluster-generic
Summary:        %{summary}

%description -n python3-snakemake-executor-plugin-cluster-generic %{common_description}


%prep
%autosetup -n snakemake-executor-plugin-cluster-generic-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_executor_plugin_cluster_generic


%check
# Just in case the tests are not very thorough:
%pyproject_check_import

%if %{without bootstrap}
%pytest -v tests/tests.py
%endif


%files -n python3-snakemake-executor-plugin-cluster-generic -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
