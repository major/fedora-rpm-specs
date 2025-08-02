%global pypi_name vvm
%global common_description %{expand:
Python wrapper and version management tool for the Vyper compiler.}

Name:          python-%{pypi_name}
Version:       0.3.2
Release:       %autorelease
BuildArch:     noarch
Summary:       Vyper version manager
License:       MIT
URL:           https://github.com/vyperlang/vvm
VCS:           git:%{url}.git
# FIXME PyPi package missing ./tests/conftest.py
Source0:       %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Patch:         python-vvm-0001-chore-remove-upper-version-limit-from-packaging-40.patch
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%check -a
# FIXME unfortunately tests requires internet access which we currently do not
# have in Koji
#%%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
