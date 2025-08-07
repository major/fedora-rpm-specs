%global pypi_name eth_abi

Name:          python-eth-abi
Version:       5.2.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python utilities for working with Ethereum ABI definitions
License:       MIT
URL:           https://github.com/ethereum/eth-abi
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-abi
Summary: %{summary}

%description -n python3-eth-abi
%{summary}.

%check -a
# FIXME test_get_abi_strategy_returns_certain_strategies_for_known_type_strings
# fails because of PEP 515 enforcement in Hypothesis 6.108.7 or later.
PYTHONPATH=$(pwd) %pytest -k 'not test_install_local_wheel and not test_get_abi_strategy_returns_certain_strategies_for_known_type_strings'

%files -n python3-eth-abi -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
