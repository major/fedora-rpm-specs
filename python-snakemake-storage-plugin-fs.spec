Name:           python-snakemake-storage-plugin-fs
Version:        0.1.5
Release:        %autorelease
Summary:        Snakemake storage plugin that reads and writes from a local filesystem

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-fs
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-fs-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
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


%prep
%autosetup -n snakemake-storage-plugin-fs-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_storage_plugin_fs


%check
# Just in case the tests are not very thorough:
%pyproject_check_import

%pytest -v tests/tests.py


%files -n python3-snakemake-storage-plugin-fs -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
