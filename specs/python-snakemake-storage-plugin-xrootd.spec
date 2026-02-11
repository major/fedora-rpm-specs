Name:           python-snakemake-storage-plugin-xrootd
Version:        1.0.0
Release:        %autorelease
Summary:        Snakemake storage plugin for xrootd storage

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-xrootd
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-xrootd-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l snakemake_storage_plugin_xrootd

BuildArch:      noarch

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  xrootd-server
BuildRequires:  snakemake >= 8

%global common_description %{expand:
A Snakemake storage plugin for handling input and output via XRootD.}

%description %{common_description}


%package -n python3-snakemake-storage-plugin-xrootd
Summary:        %{summary}

%description -n python3-snakemake-storage-plugin-xrootd %{common_description}


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%check -a
%pytest -v -k "${k-}" tests/tests.py


%files -n python3-snakemake-storage-plugin-xrootd -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
