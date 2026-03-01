%global pypi_name eth_event

Name:          python-eth-event
Version:       1.4.6
Release:       %autorelease
Summary:       Tools for Ethereum event decoding and topic generation
License:       MIT
URL:           https://github.com/iamdefinitelyahuman/eth-event
VCS:           git:%{url}.git
Source0:       %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Patch:         python-eth-event-0001-Relax-deps.patch
BuildRequires: gcc
BuildRequires: python3dist(eth-abi)
BuildRequires: python3dist(eth-utils)
BuildRequires: python3dist(mypy[mypyc])
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-event
Summary: %{summary}

%description -n python3-eth-event
%{summary}.

%check -a
%pytest --ignore=benchmarks/

%files -n python3-eth-event -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/*.so

%changelog
%autochangelog
