%global pypi_name eth_abi

Name:          python-eth-abi
Version:       6.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python utilities for working with Ethereum ABI definitions
License:       MIT
URL:           https://github.com/ApeWorX/eth-abi
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch:         python-eth-abi-0001-Do-not-package-docs-directory.patch
Patch:         python-eth-abi-0002-Support-Hypothesis-with-PEP-515-underscores.patch
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
PYTHONPATH=. %pytest

%files -n python3-eth-abi -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
