%global pypi_name trie
%global common_description %{expand:
Self-describing content-addressed identifiers for distributed systems
implementation in Python.}

Name:          python-%{pypi_name}
Version:       3.1.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Library which implements the Ethereum Trie structure
License:       MIT
URL:           https://github.com/ethereum/py-trie
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
# PyPi archive lacks tests-suite
Patch:         python-trie-0001-Readd-tools.patch
Patch:         python-trie-0002-Re-add-Trie-fixtures.patch
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%check
PYTHONPATH=$(pwd) %pytest -k 'not test_install_local_wheel'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
