%global pypi_name eth_tester
%global pre_release_tag beta.1

Name:          python-eth-tester
Version:       0.14.0
Release:       %autorelease -e %{pre_release_tag}
BuildArch:     noarch
Summary:       Tool suite for testing Ethereum applications
License:       MIT
URL:           https://github.com/ApeWorX/eth-tester
VCS:           git:%{url}.git
Source0:       %{url}/archive/v%{version}-%{pre_release_tag}/%{name}-%{version}.tar.gz
Patch:         python-eth-tester-0001-Relax-deps.patch
BuildRequires:  python3-devel

%description
%{summary}.

%package -n python3-eth-tester
Summary:        %{summary}

%description -n python3-eth-tester
%{summary}.

%prep
%autosetup -p1 -n eth-tester-%{version}-%{pre_release_tag}
# Remove zero-length file
rm -f eth_tester/rpc.py
# FIXME return as soon as we package py-evm
rm -rf tests/backends

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}%{?pre_release_tag:b1}
%pyproject_buildrequires -g test

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}%{?pre_release_tag:b1}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}%{?pre_release_tag:b1}
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
# FIXME return as soon as we package py-evm
%pytest

%files -n python3-eth-tester -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
