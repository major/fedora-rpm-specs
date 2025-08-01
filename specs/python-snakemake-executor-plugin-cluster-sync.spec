Name:           python-snakemake-executor-plugin-cluster-sync
Version:        0.1.5
Release:        %autorelease
Summary:        A Snakemake executor plugin for cluster jobs that are executed synchronously

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-cluster-sync
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-cluster-sync-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_executor_plugin_cluster_sync

BuildArch:      noarch

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-executor-plugin-cluster-sync
Summary:        %{summary}

%description -n python3-snakemake-executor-plugin-cluster-sync %{common_description}


%check -a
%pytest -v tests/tests.py


%files -n python3-snakemake-executor-plugin-cluster-sync -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
