%global pypi_name pytenable

Name:           python-%{pypi_name}
Version:        1.4.10
Release:        %autorelease
Summary:        Python library to interface with Tenable's products and applications

License:        MIT
URL:            https://github.com/tenable/pytenable
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pyTenable is intended to be a pythonic interface into the Tenable application
APIs. Further by providing a common interface and a common structure between
all of the various applications, we can ease the transition from the vastly
different APIs between some of the products.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(restfly)
BuildRequires:  python3-dateutil
BuildRequires:  python3dist(defusedxml)
BuildRequires:  python3dist(requests-pkcs12)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-vcr)
BuildRequires:  python3dist(pytest-datafiles)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(semver)
BuildRequires:  python3dist(marshmallow)
BuildRequires:  python3-box
BuildRequires:  python3dist(responses)
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
pyTenable is intended to be a pythonic interface into the Tenable application
APIs. Further by providing a common interface and a common structure between
all of the various applications, we can ease the transition from the vastly
different APIs between some of the products.

# Fedora doesn't have the furo template
#%package -n python-%{pypi_name}-doc
#Summary:        Documentation for %{pypi_name}
#
#BuildRequires:  python3-sphinx
#
#%description -n python-%{pypi_name}-doc
#Documentation for %{pypi_name}.

%prep
%autosetup -n pyTenable-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
#PYTHONPATH=${PWD} sphinx-build-3 docs html
#rm -rf html/.{doctrees,buildinfo,nojekyll}

%install
%py3_install

%check
%pytest -v tests -k "not docker"

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/tenable/
%{python3_sitelib}/pyTenable-%{version}-py*.egg-info
%exclude %{python3_sitelib}/tests

#%files -n python-%{pypi_name}-doc
#%doc html
#%license LICENSE

%changelog
%autochangelog

