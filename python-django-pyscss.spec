%global pypi_name django-pyscss
%global desc %{expand: \
A collection of tools for making it easier to use pyScss within Django.}

%global with_checks 0

Name:           python-%{pypi_name}
Version:        2.0.2
Release:        %autorelease
Summary:        Makes it easier to use PySCSS in Django

License:        BSD
URL:            https://github.com/fusionbox/django-pyscss
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description %{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}

Obsoletes:      python2-%{pypi_name} < 2.0.2-8
Obsoletes:      python-%{pypi_name} < 2.0.2-8

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

# Use the standard library instead of a backport
sed -i -e 's/^import mock/from unittest import mock/' \
       -e 's/^from mock import /from unittest.mock import /' \
    tests/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files django_pyscss

%if 0%{?with_checks} > 0
%check
%pytest -v
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
