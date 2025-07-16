Summary: A Python client for the Akamai Fast Purge API
Name: python-fastpurge
Version: 1.0.5
Release: %autorelease
URL: https://github.com/release-engineering/python-fastpurge
# PyPI tarball doesn't have tests
Source: %{url}/archive/v%{version}/fastpurge-%{version}.tar.gz
License: GPL-3.0-or-later
BuildArch: noarch

# https://github.com/release-engineering/python-fastpurge/pull/34
Patch: 0001-Use-unittest.mock-on-Python-3.3.patch


%global _description %{expand:
This library provides a simple asynchronous Python wrapper for the Fast
Purge API, including authentication and error recovery.}


%description %_description


%package -n python3-fastpurge
Summary:	%{summary}
BuildRequires:	python3-devel


%description -n python3-fastpurge %_description


%prep
%autosetup -p 1 -n python-fastpurge-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -e '/bandit/d' -i test-requirements.txt


%generate_buildrequires
%pyproject_buildrequires test-requirements.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l fastpurge


%check
%pytest -v


%files -n python3-fastpurge -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md


%changelog
%autochangelog
