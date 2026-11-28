%global pypi_name pytest-testmon

Name:           python-%{pypi_name}
Version:        2.4.1
Release:        %autorelease
Summary:        A py.test plug-in which executes only tests affected by recent changes
License:        MIT
URL:            http://testmon.org/
Source0:        %{pypi_source pytest_testmon}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-coverage
#BuildRequires:  python3-unittest_mixins

%description
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

%package -n     python3-%{pypi_name}
Summary:        A py.test plug-in which executes only tests affected by recent changes
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pytest
Requires:       python3-coverage
%description -n python3-%{pypi_name}
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

This a Python 3 version of the package.

%prep
%autosetup -n pytest_testmon-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files testmon

%check
# upstream sdist ships no tests; at least verify the module imports
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
