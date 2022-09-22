# what it's called on pypi
%global srcname flask-restx
# what it's imported as
%global libname flask_restx

Name:           python-%{srcname}
Version:        0.5.1
Release:        %autorelease
Summary:        Framework for fast, easy and documented API development with Flask
License:        BSD
URL:            https://github.com/python-restx/flask-restx
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Werkzeug >= 2.1 support
# https://github.com/python-restx/flask-restx/pull/423
Patch01:        423.patch
# https://github.com/python-restx/flask-restx/pull/427
Patch02:        427.patch
BuildArch:      noarch

%global _description %{expand:
Flask-RESTX is an extension for Flask that adds support for quickly
building REST APIs. It encourages best practices with minimal setup.
If you are familiar with Flask, Flask-RESTX should be easy to pick up.
It provides a coherent collection of decorators and tools to describe your API
and expose its documentation properly using Swagger.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Provides:       python3-flask-restplus = %{version}-%{release}
# Using < or <= would obsolete ourselves
Obsoletes:      python3-flask-restplus = 0.13.0
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf %{libname}.egg-info
rm -f %{libname}/static/files/.npmignore

%build
%py3_build

%install
%py3_install

# Upstream requires pinned dependencies versions
#%%check
#python3 setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{libname}-*.egg-info/


%changelog
%autochangelog
