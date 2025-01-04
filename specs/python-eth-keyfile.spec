%global pypi_name eth_keyfile

Name:          python-eth-keyfile
Version:       0.8.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Tools for handling the encrypted keyfile format used to store private keys
License:       MIT
URL:           https://github.com/ethereum/eth-keyfile
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
# Fedora-specific
Patch1:        python-eth_keyfile-0001-Fedora-use-cryptodome-explicitly.patch
# Fedora-specific
Patch2:        python-eth_keyfile-0002-Relax-dependencies.patch
# Backported from upstream. PyPi tarball doesn't have a test-suite.
Patch3:        python-eth_keyfile-0003-Add-fixtures-back.patch
BuildRequires: python3-devel
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-eth-keyfile
Summary: %{summary}

%description -n python3-eth-keyfile
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
PYTHONPATH=$(pwd) %pytest

%files -n python3-eth-keyfile -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
