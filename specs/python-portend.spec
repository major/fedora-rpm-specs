# Created by pyp2rpm-3.3.2
%global pypi_name portend
# theres a dependency resolution issue with
# sphinx to build docs. Turning it off for now
%global with_docs 0
%{?python_enable_dependency_generator}

Name:           python-%{pypi_name}
Version:        3.2.1
Release:        %autorelease
Summary:        TCP port monitoring utilities

License:        MIT
URL:            https://github.com/jaraco/portend
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%generate_buildrequires
%pyproject_buildrequires

%description
 por·tend pôrˈtend/ be a sign or warning that (something, especially something
momentous or calamitous) is likely to happen.

%package -n python3-%{pypi_name}
Summary:        portend documentation

%description -n python3-%{pypi_name}
 por·tend pôrˈtend/ be a sign or warning that (something, especially something
momentous or calamitous) is likely to happen.

%if 0%{?with_docs}
%package -n python-%{pypi_name}-doc
Summary:        portend documentation

BuildRequires:  python3dist(jaraco-packaging) >= 3.2
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(rst-linker) >= 1.9
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(tox)
BuildRequires:  python3-more-itertools

%description -n python-%{pypi_name}-doc
Documentation for portend
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%if 0%{?with_docs}
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%check
%if 0%{?el8}
# disable flake8 in the tests, need a newer version of pytest (3.5) which is not
# available on EL8, and is pulled in by python-pytest-flake8.
sed -i 's/ --flake8//' pytest.ini
%endif
LANG=C.utf-8 %{__python3} -m pytest --ignore=build

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%if 0%{?with_docs}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
