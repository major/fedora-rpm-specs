Name:           python-snakemake-executor-plugin-cluster-sync
Version:        0.1.4
Release:        %autorelease
Summary:        A Snakemake executor plugin for cluster jobs that are executed synchronously

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-cluster-sync
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-cluster-sync-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-executor-plugin-cluster-sync
Summary:        %{summary}

%description -n python3-snakemake-executor-plugin-cluster-sync %{common_description}


%prep
%autosetup -n snakemake-executor-plugin-cluster-sync-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_executor_plugin_cluster_sync


%check
# Just in case the tests are not very thorough:
%pyproject_check_import

%pytest -v tests/tests.py


%files -n python3-snakemake-executor-plugin-cluster-sync -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
