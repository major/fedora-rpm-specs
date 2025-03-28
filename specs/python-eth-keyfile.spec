%global pypi_name eth_keyfile

Name:          python-eth-keyfile
Version:       0.9.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Tools for handling the encrypted keyfile format used to store private keys
License:       MIT
URL:           https://github.com/ethereum/eth-keyfile
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
# Fedora-specific
Patch:         python-eth_keyfile-0001-Fedora-use-cryptodome-explicitly.patch
# Backported from upstream. PyPi tarball doesn't have a test-suite.
Patch:         python-eth_keyfile-0002-Add-fixtures-back.patch
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-keyfile
Summary: %{summary}

%description -n python3-eth-keyfile
%{summary}.

%check -a
PYTHONPATH=$(pwd) %pytest -k 'not test_install_local_wheel'

%files -n python3-eth-keyfile -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
