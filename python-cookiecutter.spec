%global srcname  cookiecutter
%global pkgname  python-cookiecutter
%global forgeurl https://github.com/audreyr/cookiecutter
%global common_description %{expand:
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.}

%bcond_without tests

Name:      %{pkgname}
Version:   2.6.0
%forgemeta
Release:   %autorelease
Summary:   CLI utility to create projects from templates
License:   BSD-3-Clause
URL:       %{forgeurl}
Source0:   https://github.com/audreyr/%{srcname}/archive/%{version}.tar.gz
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
%if %{with tests}
BuildRequires: python3-pytest-cov
BuildRequires: python3-freezegun
BuildRequires: python3-pytest-mock
BuildRequires: git
%endif

%description %{common_description}

%package -n python-%{srcname}-doc
Summary: Documentation for %{srcname}
%description -n python-%{srcname}-doc
Documentation for %{srcname}

%package -n python3-%{srcname}
Summary: %summary

Recommends: python-%{srcname}-doc
Requires: python3-binaryornot
Requires: python3-click
Requires: python3-jinja2
Requires: python3-jinja2-time
Requires: python3-pyyaml
Requires: python3-requests
Requires: python3-slugify

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -n %{srcname}-%{version}
sed -i 's#python -c#%{__python3} -c#' Makefile

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x testing}

%build
%pyproject_wheel

%if %{with doc}
make docs
%endif

%install
%pyproject_install

%if %{with tests}
%check
%{python3} -m pytest tests -v
%endif

%files -n python3-%{srcname}
%license LICENSE
# For noarch packages: sitelib
%{python3_sitelib}/*
%{_bindir}/%{srcname}

%files -n python-%{srcname}-doc
%license LICENSE
%doc docs
%doc *.md

%changelog
%autochangelog
