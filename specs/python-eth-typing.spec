%global pypi_name eth_typing

Name:          python-eth-typing
Version:       5.2.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python types for type hinting commonly used Ethereum types
License:       MIT
URL:           https://github.com/ethereum/eth-typing
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-typing
Summary: %{summary}

%description -n python3-eth-typing
%{summary}.

%check -a
%pytest -k 'not test_install_local_wheel'

%files -n python3-eth-typing -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
