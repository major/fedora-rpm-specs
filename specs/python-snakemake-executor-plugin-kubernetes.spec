# Tests need network access and credentials for a real Kubernetes cluster
%bcond tests 0

Name:           python-snakemake-executor-plugin-kubernetes
Version:        0.4.2
Release:        %autorelease
Summary:        A snakemake executor plugin for submission of jobs to Kubernetes

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-kubernetes
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-kubernetes-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_executor_plugin_kubernetes

BuildArch:      noarch

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  snakemake >= 8
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist snakemake-storage-plugin-s3}
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-executor-plugin-kubernetes
Summary:        %{summary}

%description -n python3-snakemake-executor-plugin-kubernetes %{common_description}


%prep -a
# Remove upstream’s upper-bound on the version of kubernetes. This package
# routinely ends up briefly failing to build from source and sometimes failing
# to install due to “incompatible” major-version updates in python-kubernetes,
# but there have so far never been any real incompatibilities in practice.
# Upstream will still (eventually) keep up with new versions without us filing
# PR’s because they have configured dependabot, e.g.
# https://github.com/snakemake/snakemake-executor-plugin-kubernetes/pull/45.
sed -r -i 's/(kubernetes = ".*),<[^"]+"/\1"/' pyproject.toml


%check -a
%if %{with tests}
%pytest -v tests/tests.py
%endif


%files -n python3-snakemake-executor-plugin-kubernetes -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
