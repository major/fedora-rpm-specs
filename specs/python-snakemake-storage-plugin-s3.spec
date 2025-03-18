# We can’t run tests that access the network in koji, but this build
# conditional allows us to try them in local mock builds for added confidence:
#   fedpkg mockbuild --enable-network --with network_tests
%bcond network_tests 0

Name:           python-snakemake-storage-plugin-s3
Version:        0.3.1
Release:        %autorelease
Summary:        A Snakemake storage plugin for S3 API storage (AWS S3, MinIO, etc.)

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-s3
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-s3-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8

%global common_description %{expand:
A Snakemake storage plugin for S3 API storage (AWS S3, MinIO, etc.). For
documentation and usage instructions, see the Snakemake plugin catalog,
https://snakemake.github.io/snakemake-plugin-catalog/plugins/storage/s3.html.}

%description %{common_description}


%package -n python3-snakemake-storage-plugin-s3
Summary:        %{summary}

%description -n python3-snakemake-storage-plugin-s3 %{common_description}


%prep
%autosetup -n snakemake-storage-plugin-s3-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_storage_plugin_s3


%check
# Just in case the tests are not very thorough:
%pyproject_check_import

%if %{without network_tests}
# The following tests require network access:
k="${k-}${k+ and }not (TestStorageNoSettings and test_storage)"
k="${k-}${k+ and }not (TestStorageNoSettings and test_storage_not_existing)"
k="${k-}${k+ and }not TestWorkflows"
%endif

%pytest -v -k "${k-}" tests/tests.py


%files -n python3-snakemake-storage-plugin-s3 -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
