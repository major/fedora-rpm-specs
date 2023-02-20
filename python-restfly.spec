%global pypi_name restfly

Name:           python-%{pypi_name}
Version:        1.4.7
Release:        %autorelease
Summary:        Library to make API wrappers creation easier

License:        MIT4
URL:            https://github.com/stevemcgrath/restfly
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
RESTfly is a framework for building libraries to easily interact with RESTful
APIs.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %py3_dist setuptools
BuildRequires:  %py3_dist requests
BuildRequires:  %py3_dist responses
BuildRequires:  %py3_dist pytest
BuildRequires:  %py3_dist pytest-cov
BuildRequires:  %py3_dist pytest-vcr
BuildRequires:  %py3_dist pytest-datafiles
BuildRequires:  %py3_dist python-box
BuildRequires:  %py3_dist arrow
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
RESTfly is a framework for building libraries to easily interact with RESTful
APIs.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests -k "not test_session_ssl_error"

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
%autochangelog

