%global pypi_name torchdata
%global pypi_version 0.7

%bcond_with gitcommit
%if %{with gitcommit}
# The top of the 0.7 branch - update to whatever..
%global commit0 4e255c95c76b1ccde4f6650391c0bc30650d6dbe
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%endif

Name:           python-%{pypi_name}
Version:        %{pypi_version}.0
Release:        3%{?dist}
Summary:        A PyTorch module for data loading

License:        BSD-3-Clause
URL:            https://github.com/pytorch/data
%if %{with gitcommit}
Source0:        %{url}/archive/%{commit0}/data-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/data-%{version}.tar.gz
# Do not use git submodules
# Do not use distutils
Patch0:         0001-Prepare-torchdata-setup-for-fedora.patch
%endif

# Limit to these because that is what torch is on
ExclusiveArch:  x86_64 aarch64
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-torch-devel
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(urllib3)

%description
torchdata is a library of common modular data loading primitives for
easily constructing data pipelines.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
torchdata is a library of common modular data loading primitives for
easily constructing data pipelines.

%prep
%if %{with gitcommit}
%autosetup -p1 -n data-%{commit0}
%else
%autosetup -p1 -n data-%{version}
%endif

rm -rf third_party/*

# pyproject_ is broken it is generate_buildrequires looks for
# python3-cmake and python3-ninja, revert to old py3_

%build
%py3_build

# Depends on 
# E   ModuleNotFoundError: No module named 'expecttest'
# %%check
# %%pytest

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info

%changelog
* Thu Dec 14 2023 Tom Rix <trix@redhat.com> - 0.7.0-3
- Remove dir generation

* Fri Dec 8 2023 Tom Rix <trix@redhat.com> - 0.7.0-2
- Comment why no check

* Tue Dec 5 2023 Tom Rix <trix@redhat.com> - 0.7.0-1
- Initial package.

