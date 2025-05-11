Name:           python-snakemake-storage-plugin-gcs
Version:        1.1.4
Release:        %autorelease
Summary:        A Snakemake storage plugin for Google Cloud Storage

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-gcs
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-gcs-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_storage_plugin_gcs
# All tests require Docker, network access, and/or cloud credentials.

BuildArch:      noarch

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 9

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-storage-plugin-gcs
Summary:        %{summary}

%description -n python3-snakemake-storage-plugin-gcs %{common_description}


%files -n python3-snakemake-storage-plugin-gcs -f %{pyproject_files}
%license COPYRIGHT LICENSE NOTICE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
