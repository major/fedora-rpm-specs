Name:           python-snakemake-storage-plugin-fs
Version:        1.0.6
Release:        %autorelease
Summary:        Snakemake storage plugin that reads and writes from a local filesystem

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-fs
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-fs-%{version}.tar.gz

BuildArch:      noarch

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_storage_plugin_fs

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8

%global common_description %{expand:
A Snakemake storage plugin that reads and writes from a locally mounted
filesystem using rsync.}

%description %{common_description}


%package -n python3-snakemake-storage-plugin-fs
Summary:        %{summary}

%description -n python3-snakemake-storage-plugin-fs %{common_description}


%check -a
%pytest -v tests/tests.py


%files -n python3-snakemake-storage-plugin-fs -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
