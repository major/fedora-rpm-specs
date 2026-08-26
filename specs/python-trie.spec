%global pypi_name trie
%global common_description %{expand:
Self-describing content-addressed identifiers for distributed systems
implementation in Python.}

Name:          python-%{pypi_name}
Version:       4.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Library which implements the Ethereum Trie structure
License:       MIT
URL:           https://github.com/ApeWorX/py-trie
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
# PyPi archive lacks tests-suite
Patch:         python-trie-0001-Re-add-Trie-fixtures.patch
Patch:         python-trie-0002-relax-dependencies.patch
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
