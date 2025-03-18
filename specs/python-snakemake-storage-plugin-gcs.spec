Name:           python-snakemake-storage-plugin-gcs
Version:        1.1.3
Release:        %autorelease
Summary:        A Snakemake storage plugin for Google Cloud Storage

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-gcs
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-gcs-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-storage-plugin-gcs
Summary:        %{summary}

%description -n python3-snakemake-storage-plugin-gcs %{common_description}


%prep
%autosetup -n snakemake-storage-plugin-gcs-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_storage_plugin_gcs


%check
# Just in case the tests are not very thorough:
%pyproject_check_import

# The following tests require network access *and* cloud credentials:
k="${k-}${k+ and }not (TestStorage and test_list_candidate_matches)"
k="${k-}${k+ and }not (TestStorage and test_storage)"
k="${k-}${k+ and }not (TestStorage and test_storage_dbg)"
k="${k-}${k+ and }not (TestStorage and test_storage_not_existing)"

%pytest -v -k "${k-}" tests/tests.py


%files -n python3-snakemake-storage-plugin-gcs -f %{pyproject_files}
%license COPYRIGHT LICENSE NOTICE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
