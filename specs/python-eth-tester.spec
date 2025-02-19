%global pypi_name eth_tester
%global pre_release_tag beta.1

Name:          python-eth-tester
Version:       0.12.1
Release:       %autorelease -e %{pre_release_tag}
BuildArch:     noarch
Summary:       Tool suite for testing Ethereum applications
License:       MIT
URL:           https://github.com/ethereum/eth-tester
VCS:           git:%{url}.git
Source0:       %{url}/archive/v%{version}-%{pre_release_tag}/%{name}-%{version}.tar.gz
Patch1:        python-eth-tester-0001-Relax-deps.patch
Patch2:        python-eth-tester-0002-Revert-bump-towncrier-version-pins.patch
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist

%description
%{summary}.

%package -n python3-eth-tester
Summary: %{summary}

%description -n python3-eth-tester
%{summary}.

%prep
%autosetup -p1 -n eth-tester-%{version}-%{pre_release_tag}
# FIXME return as soon as we package py-evm
rm -rf tests/backends
# FIXME requires internet-access
rm -f scripts/release/test_package.py

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

%files -n python3-eth-tester -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
