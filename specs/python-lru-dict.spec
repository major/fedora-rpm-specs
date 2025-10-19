%global pypi_name lru-dict

Name:          python-%{pypi_name}
Version:       1.5.0
Release:       %autorelease
Summary:       A fast and memory efficient LRU cache
License:       MIT
URL:           https://github.com/amitdev/%{pypi_name}
VCS:           git:%{url}.git
Source0:       %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Patch:         python-lru-dict-0001-Revert-Lock-a-known-good-setuptools-version-for-PEP-.patch
Patch:         python-lru-dict-0002-A-correct-version.patch
BuildRequires: gcc
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(install): -l lru

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
