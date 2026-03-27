%global pypi_name eth_utils

Name:          python-eth-utils
Version:       6.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Utility functions for working with Ethereum related codebases
License:       MIT
URL:           https://github.com/ethereum/eth-utils
VCS:           git:%{url}.git
# PyPi doesn't contain test fixtures so we have to get GitHub's one
Source0:       %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildRequires: python3-hypothesis
BuildRequires: python3-mypy
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-utils
Summary: %{summary}

%description -n python3-eth-utils
%{summary}.

%prep -a
# Remove egg-info
rm -rf %{pypi_name}.egg-info/

%check -a
%pytest -k 'not test_install_local_wheel'

%files -n python3-eth-utils -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
