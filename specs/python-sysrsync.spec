Name:           python-sysrsync
Version:        1.1.1
Release:        %autorelease
Summary:        Simple and safe python wrapper for calling system rsync

# SPDX
License:        MIT
URL:            https://github.com/gchamon/sysrsync
# PyPI source distributions lack tests; use the GitHub archive
Source:         %{url}/archive/%{version}/sysrsync-%{version}.tar.gz

# Declare build-system dependencies and correctly exclude tests from packaging
# https://github.com/gchamon/sysrsync/pull/39
Patch:          %{url}/pull/39.patch

# In Python 3.11 and later, use tomllib instead of toml
# https://github.com/gchamon/sysrsync/pull/42
# Rebased on 1.1.1 with https://github.com/gchamon/sysrsync/pull/39.
Patch:          0001-In-Python-3.11-and-later-use-tomllib-instead-of-toml.patch

BuildSystem:            pyproject
BuildOption(install):   -l sysrsync

BuildArch:      noarch

BuildRequires:  rsync

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-sysrsync
Summary:        %{summary}

Requires:       rsync

%description -n python3-sysrsync %{common_description}


%check -a
# We cannot run the end-to-end-tests/ because they require Docker and network
# access, but we can run the unit tests.
%{py3_test_envvars} %{python3} -m unittest discover -v -s test/


%files -n python3-sysrsync -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
