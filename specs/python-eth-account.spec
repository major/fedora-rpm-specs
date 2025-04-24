%global pypi_name eth_account

Name:          python-eth-account
Version:       0.13.7
Release:       %autorelease
BuildArch:     noarch
Summary:       Ethereum account abstraction library
License:       MIT
URL:           https://github.com/ethereum/eth-account
Source0:       %{pypi_source %pypi_name}
Patch:         python-eth-account-0001-Relax-dependencies-a-bit.patch
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

%check -a
# Ignored tests requires Node.js with a custom setup or Internet access
PYTHONPATH=$(pwd) %pytest -k 'not test_install_local_wheel and not test_messages_where_all_3_sigs_match and not test_messages_where_eth_account_matches_ethers_but_not_metamask and not test_messages_where_eth_account_matches_metamask_but_not_ethers and not test_compatibility'

%files -n python3-eth-account -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
