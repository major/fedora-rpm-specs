Name:           python-wheel0.37
Version:        0.37.1
Release:        %autorelease
Summary:        A built-package format for Python

License:        MIT
URL:            https://github.com/pypa/wheel
Source:         %{url}/archive/%{version}/wheel-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# For tests
BuildRequires:  gcc

%global python_wheel_name wheel-%{version}-py2.py3-none-any.whl

%global _description %{expand:
Wheel is the reference implementation of the Python wheel packaging standard,
as defined in PEP 427.

It has two different roles:

 1. A setuptools extension for building wheels that provides the bdist_wheel
    setuptools command.
 2. A command line tool for working with wheel files.

This is a compatibility package with an older version of wheel used by
virtualenv to create virtual environments for Python < 3.7.}

%description %_description


%package -n     %{python_wheel_pkg_prefix}-wheel0.37-wheel
Summary:        The Python wheel 0.37.x module packaged as a wheel
Conflicts:      %{python_wheel_pkg_prefix}-wheel-wheel < 1:0.38
# Virtual provides for the packages bundled by wheel.
# Actual version can be found in git history:
# https://github.com/pypa/wheel/commits/master/src/wheel/vendored/packaging/tags.py
Provides:       bundled(python2dist(packaging)) = 20.9
Provides:       bundled(python3dist(packaging)) = 20.9

%description -n %{python_wheel_pkg_prefix}-wheel0.37-wheel
A Python wheel of wheel 0.37.x to use with virtualenv
to create virtual environments for Python < 3.7.


%prep
%autosetup -p1 -n wheel-%{version}
sed -Ei '/(pytest|-)-cov/d' setup.cfg


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
mkdir -p %{buildroot}%{python_wheel_dir}
install -p %{_pyproject_wheeldir}/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}


%check
# We will use this wheel in virtualenv with Python 2.7 and 3.6,
# so running the tests with the current Python version is not exactly what we need
# but it is the best we can do here.
export PYTHONPATH=%{buildroot}%{python_wheel_dir}/%{python_wheel_name}
%pytest


%files -n %{python_wheel_pkg_prefix}-wheel0.37-wheel
%license LICENSE.txt
# we own the dir for simplicity
%dir %{python_wheel_dir}/
%{python_wheel_dir}/%{python_wheel_name}


%changelog
%autochangelog
