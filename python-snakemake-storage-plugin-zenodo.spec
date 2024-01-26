# Currently, all of the tests require network access *and* Zenodo credentials.
%bcond tests 0

Name:           python-snakemake-storage-plugin-zenodo
Version:        0.1.2
Release:        %autorelease
Summary:        A Snakemake storage plugin for reading from and writing to zenodo.org

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-zenodo
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-zenodo-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  snakemake >= 8
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%global common_description %{expand:
A Snakemake storage plugin for reading from and writing to zenodo.org. The
plugin takes queries of the form zenodo://record/121246/path/to/file.txt for
downloading files (here from record 121246), and
zenodo://deposition/121246/path/to/file.txt for uploading files to an existing
deposition (i.e. an unpublished and therefore still writable record).}

%description %{common_description}


%package -n python3-snakemake-storage-plugin-zenodo
Summary:        %{summary}

%description -n python3-snakemake-storage-plugin-zenodo %{common_description}


%prep
%autosetup -n snakemake-storage-plugin-zenodo-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_storage_plugin_zenodo


%check
%pyproject_check_import

%if %{with tests}
%pytest -v -k "${k-}" tests/tests.py
%endif


%files -n python3-snakemake-storage-plugin-zenodo -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
