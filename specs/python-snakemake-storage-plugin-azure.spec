# Currently, even *collecting* the tests requires network access, and even when
# that is enabled (--enable-network option to mock, or working in a git
# checkout from upstream), this hangs and eventually fails with:
#   [Errno 111] Connection refused.
%bcond tests 0

Name:           python-snakemake-storage-plugin-azure
Version:        0.4.3
Release:        %autorelease
Summary:        Snakemake storage plugin for Azure Blob Storage

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-azure
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-azure-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_storage_plugin_azure

BuildArch:      noarch

%if %{with tests}
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
%endif
BuildRequires:  snakemake >= 8

%global common_description %{expand:
A Snakemake storage plugin to read and write from Azure Blob Storage.}

%description %{common_description}


%package -n python3-snakemake-storage-plugin-azure
Summary:        %{summary}

%description -n python3-snakemake-storage-plugin-azure %{common_description}


%check -a
%if %{with tests}
%pytest -v -k "${k-}" tests/tests.py
%endif


%files -n python3-snakemake-storage-plugin-azure -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
