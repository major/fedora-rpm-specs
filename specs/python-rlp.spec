%global pypi_name rlp

Name:          python-%{pypi_name}
Version:       4.1.0
Release:       %autorelease
BuildArch:     noarch
Summary:       A Python implementation of Recursive Length Prefix encoding
License:       MIT
URL:           https://github.com/ethereum/pyrlp
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest -k 'not test_install_local_wheel'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
