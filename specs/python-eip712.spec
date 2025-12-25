%global pypi_name eip712

Name:          python-%{pypi_name}
Version:       0.3.3
Release:       %autorelease
BuildArch:     noarch
Summary:       Message classes for typed structured data hashing and signing in Ethereum
License:       Apache-2.0
URL:           https://github.com/ApeWorX/eip712
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch:         python-eip712-0001-refactor-move-pytest-cov-to-lint-dependency-group.patch
BuildRequires: python3-eth-account
BuildRequires: python3-eth-utils
BuildRequires: python3-hypothesis
BuildRequires: python3-pydantic
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
