%global pypi_name solcx

Name:          python-%{pypi_name}
Version:       2.0.5
Release:       %autorelease
BuildArch:     noarch
Summary:       Python wrapper and version management tool for the Solidity compiler
License:       MIT
URL:           https://github.com/ApeWorX/py-solc-x
VCS:           git:%{url}.git
Source0:       %{pypi_source py_solc_x}
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
# FIXME unfortunately tests requires internet access which we currently do not
# have in Koji.
#%%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
