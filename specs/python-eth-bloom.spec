%global pypi_name eth_bloom

Name:          python-eth-bloom
Version:       3.1.0
Release:       %autorelease
BuildArch:     noarch
Summary:       An implementation of the Ethereum bloom filter
License:       MIT
URL:           https://github.com/ethereum/eth-bloom
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch:         python-eth-bloom-0001-Relax-deps.patch
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -L %{pypi_name}

%description
%{summary}.

%package -n python3-eth-bloom
Summary: %{summary}

%description -n python3-eth-bloom
%{summary}.

%check -a
%pytest -k 'not test_install_local_wheel'

%files -n python3-eth-bloom -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
