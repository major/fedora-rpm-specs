Name:           python-snakemake-storage-plugin-xrootd
Version:        0.4.0
Release:        %autorelease
Summary:        Snakemake storage plugin for xrootd storage

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-xrootd
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-xrootd-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
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


%prep
%autosetup -n snakemake-storage-plugin-xrootd-%{version} -p1


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l snakemake_storage_plugin_xrootd


%check
# Just in case the tests are not very thorough:
%pyproject_check_import

%pytest -v -k "${k-}" tests/tests.py


%files -n python3-snakemake-storage-plugin-xrootd -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
