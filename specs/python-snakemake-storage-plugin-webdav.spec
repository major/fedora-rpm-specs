Name:           python-snakemake-storage-plugin-webdav
Version:        0.1.2
Release:        %autorelease
Summary:        Snakemake storage plugin for webdav

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-webdav
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-storage-plugin-webdav-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_storage_plugin_webdav

BuildArch:      noarch

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 9

%global common_description %{expand:
A Snakemake storage plugin for handling input and output via webdav.}

%description %{common_description}


%package -n python3-snakemake-storage-plugin-webdav
Summary:        %{summary}

%description -n python3-snakemake-storage-plugin-webdav %{common_description}


%check -a
# The following tests require network access and a webdav test server that
# upstream CI sets up with docker, which will of course not be possible here:
k="${k-}${k+ and }not (TestStorage and test_storage)"
k="${k-}${k+ and }not (TestStorage and test_storage_not_existing)"

%pytest -v -k "${k-}" tests/tests.py


%files -n python3-snakemake-storage-plugin-webdav -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
