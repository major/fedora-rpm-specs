%global pypi_name eth_account

Name:          python-eth-account
Version:       0.13.5
Release:       %autorelease
BuildArch:     noarch
Summary:       Ethereum account abstraction library
License:       MIT
URL:           https://github.com/ethereum/eth-account
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-account
Summary: %{summary}

%description -n python3-eth-account
%{summary}.

%prep -a
rm -f ./scripts/release/test_package.py
# FIXME requires Node.js with a custom setup and Internet access
rm -f tests/integration/test_comparison_js_eip712_signing.py tests/integration/test_ethers_fuzzing.py

%check -a
PYTHONPATH=$(pwd) %pytest

%files -n python3-eth-account -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
