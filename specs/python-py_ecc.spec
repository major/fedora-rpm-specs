%global pypi_name py_ecc

Name:          python-%{pypi_name}
Version:       8.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       ECC pairing and bn_128 and bls12_381 curve operations
License:       MIT
URL:           https://github.com/ethereum/py_ecc
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
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
