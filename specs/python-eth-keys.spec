%global pypi_name eth_keys

Name:          python-eth-keys
Version:       0.7.0
Release:       %autorelease
BuildArch:     noarch
Summary:       A common API for Ethereum key operations
License:       MIT
URL:           https://github.com/ethereum/eth-keys
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-asn1tools
BuildRequires: python3-coincurve
BuildRequires: python3-factory-boy
BuildRequires: python3-hypothesis
BuildRequires: python3-pyasn1
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-keys
Summary: %{summary}

%description -n python3-eth-keys
%{summary}.

%check -a
%pytest -k 'not test_install_local_wheel'

%files -n python3-eth-keys -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
