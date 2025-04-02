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
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildSystem:   pyproject
BuildOption(prep): -n eth-tester-%{version}-%{pre_release_tag}
BuildOption(generate_buildrequires): -t
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-tester
Summary: %{summary}

%description -n python3-eth-tester
%{summary}.

%prep -a
# FIXME return as soon as we package py-evm
rm -rf tests/backends

%check -a
# FIXME return as soon as we package py-evm
PYTHONPATH=$(pwd) %pytest -k 'not test_install_local_wheel'

%files -n python3-eth-tester -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
