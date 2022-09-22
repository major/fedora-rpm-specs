%global pypi_name pytest-sanic

Name:           python-%{pypi_name}
Version:        1.9.1
Release:        %autorelease
Summary:        Pytest plugin for Sanic

License:        ASL 2.0
URL:            https://github.com/yunstanford/pytest-sanic
Source0:        %{pypi_source}

BuildArch:      noarch

%description
A pytest plugin for Sanic. It helps you to test your code asynchronously 
very easy testing with async coroutines, common and useful fixtures, 
asynchronous fixture support, test_client/sanic_client and a test_server.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-async-generator
BuildRequires:  python3-httpx
BuildRequires:  python3-pytest
BuildRequires:  python3-websockets
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A pytest plugin for Sanic. It helps you to test your code asynchronously 
very easy testing with async coroutines, common and useful fixtures, 
asynchronous fixture support, test_client/sanic_client and a test_server.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%py3_check_import pytest_sanic

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_sanic/
%{python3_sitelib}/pytest_sanic-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog

