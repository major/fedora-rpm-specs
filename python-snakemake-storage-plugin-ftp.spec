# We can’t run tests that access the network in koji, but this build
# conditional allows us to try them in local mock builds for added confidence:
#   fedpkg mockbuild --enable-network --with network_tests
%bcond network_tests 0

Name:           python-snakemake-storage-plugin-ftp
Version:        0.1.2
Release:        %autorelease
Summary:        A Snakemake plugin for handling input and output via FTP

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-ftp
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-ftp-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8

%global common_description %{expand:
A Snakemake storage plugin that handles files and directories on an FTP
server.}

%description %{common_description}


%package -n python3-snakemake-storage-plugin-ftp
Summary:        %{summary}

%description -n python3-snakemake-storage-plugin-ftp %{common_description}


%prep
%autosetup -n snakemake-storage-plugin-ftp-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_storage_plugin_ftp


%check
# Just in case the tests are not very thorough:
%pyproject_check_import

%if %{without network_tests}
# The following tests require network access:
k="${k-}${k+ and }not (TestStorage and test_storage)"
k="${k-}${k+ and }not (TestStorage and test_storage_not_existing)"
k="${k-}${k+ and }not (TestStorage and test_inventory)"
%endif

%pytest -v -k "${k-}" tests/tests.py


%files -n python3-snakemake-storage-plugin-ftp -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
