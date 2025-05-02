%global pypi_name decorator

Name:           python-%{pypi_name}
Version:        5.2.1
Release:        %autorelease
Summary:        Module to simplify usage of decorators

License:        BSD-2-Clause
URL:            https://github.com/micheles/decorator
Source0:        %pypi_source decorator

BuildArch:      noarch

BuildRequires:  python3-devel

%description
The aim of the decorator module is to simplify the usage of decorators for
the average programmer, and to popularize decorators usage giving examples
of useful decorators, such as memoize, tracing, redirecting_stdout, locked,
etc.  The core of this module is a decorator factory called decorator.

%package -n python3-decorator
Summary:        Module to simplify usage of decorators in python3
%{?python_provide:%python_provide python3-decorator}

%description -n python3-decorator
The aim of the decorator module is to simplify the usage of decorators for
the average programmer, and to popularize decorators usage giving examples
of useful decorators, such as memoize, tracing, redirecting_stdout, locked,
etc.  The core of this module is a decorator factory called decorator.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l decorator

%check
%{py3_test_envvars} %{python3} -m unittest tests/test.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CHANGES.md
%license LICENSE.txt

%changelog
%autochangelog
