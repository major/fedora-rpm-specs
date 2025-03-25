%global pypi_name eth_utils

Name:          python-eth-utils
Version:       5.2.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Utility functions for working with Ethereum related codebases
License:       MIT
URL:           https://github.com/ethereum/eth-utils
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch1:        python-eth-utils-0001-Disable-this-test-we-don-t-have-internet-access-anyw.patch
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-utils
Summary: %{summary}

%description -n python3-eth-utils
%{summary}.

%prep -a
# We don't have mypy fixtures anyway
rm -rf ./tests/core/functional-utils/test_type_inference.py
# Remove egg-info
rm -rf %{pypi_name}.egg-info/

%check -a
%pytest

%files -n python3-eth-utils -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
