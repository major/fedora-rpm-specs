%global pypi_name eth_hash
%global common_description %{expand:
The Ethereum hashing function, keccak256, sometimes (erroneously) called sha256
or sha3.}

Name:          python-eth-hash
Version:       0.7.1
Release:       %autorelease
BuildArch:     noarch
Summary:       The Ethereum hashing function
License:       MIT
URL:           https://github.com/ethereum/eth-hash
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
# Fedora-specific. Cryptodome shipped in Fedora is not drop-in replacement for
# pycrypto. We have to adjust.
Patch:         python-eth-hash-0001-Fedora-use-cryptodome-explicitly.patch
# Fedora-secific. We don't have pysha3
Patch:         python-eth-hash-0002-Remove-pysha3.patch
BuildRequires: python3-pycryptodomex
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description  %{common_description}

%package -n python3-eth-hash
Summary: %{summary}

%description -n python3-eth-hash %{common_description}

%pyproject_extras_subpkg -n python3-eth-hash pycryptodomex

%check -a
%pytest ./tests/core/ ./tests/backends/pycryptodome

%files -n python3-eth-hash -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
