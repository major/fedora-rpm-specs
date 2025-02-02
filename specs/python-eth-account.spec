%global pypi_name eth_account

Name:          python-eth-account
Version:       0.13.4
Release:       %autorelease
BuildArch:     noarch
Summary:       Ethereum account abstraction library
License:       MIT
URL:           https://github.com/ethereum/eth-account
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-devel
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-eth-account
Summary: %{summary}

%description -n python3-eth-account
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# FIXME requires Node.js with a custom setup and Internet access
rm -f tests/integration/test_comparison_js_eip712_signing.py tests/integration/test_ethers_fuzzing.py

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

%files -n python3-eth-account -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
