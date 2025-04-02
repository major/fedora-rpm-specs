%global pypi_name eth_rlp

Name:          python-eth-rlp
Version:       2.2.0
Release:       %autorelease
BuildArch:     noarch
Summary:       RLP definitions for common Ethereum objects in Python
License:       MIT
URL:           https://github.com/ethereum/eth-rlp
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-rlp
Summary: %{summary}

%description -n python3-eth-rlp
%{summary}.

%check -a
%pytest -k 'not test_install_local_wheel'

%files -n python3-eth-rlp -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
