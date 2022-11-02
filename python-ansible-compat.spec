%global srcname ansible-compat
%global pkgname python-ansible-compat
%global forgeurl https://github.com/ansible/ansible-compat

%bcond_without tests

Name:    %{pkgname}
Version: 2.2.3
%forgemeta
Release: %autorelease
Summary: Ansible python helper functions

URL:       %{forgeurl}
Source0:   %{pypi_source}
License:   MIT
BuildArch: noarch

BuildRequires: pyproject-rpm-macros
BuildRequires: ansible-core
BuildRequires: python3dist(flaky)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-mock)

# This patch skips the tests requiring a connection to
# ansible galaxy
Patch0: 0001_skip_tests_requiring_network_connectivity.patch

Requires: python3dist(pyyaml)
Requires: python3dist(subprocess-tee)

%global common_description %{expand:
A python package containing functions that help interacting with
various versions of Ansible}

%description %{common_description}

%package -n python-%{srcname}-doc
Summary: %summary

%description -n python-%{srcname}-doc
Documentation for python-ansible-compat

%package -n python3-%{srcname}
Summary: %summary

%py_provides python3-%{srcname}

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x testing}

%build
%pyproject_wheel

%if %{with doc}
PYTHONPATH=src sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%if %{with tests}
%check
PYTHONPATH=src %{python3} -m pytest -vv test
%endif

%files -n python3-%{srcname}
%{python3_sitelib}/ansible_compat/
%{python3_sitelib}/ansible_compat-*.dist-info/
%license LICENSE

%if %{with doc}
%files -n python-%{srcname}-doc
%license LICENSE
%doc *.rst
%doc html/
%endif

%changelog
%autochangelog
