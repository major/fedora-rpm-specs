%global pypi_name pydaikin
%global pkg_name daikin

Name:           python-%{pkg_name}
Version:        2.4.0
Release:        7%{?dist}
Summary:        Python Daikin HVAC appliances interface

License:        GPLv3
URL:            https://bitbucket.org/mustang51/pydaikin
Source0:        %{url}/get/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
PyDaikin is a standalone program and a library that interface air conditioners
from Daikin. Currently the following Daikin WiFi modules are supported:

- BRP069Axx/BRP069Bxx/BRP072Axx
- BRP15B61 aka. AirBase (similar protocol as BRP069Axx)
- BRP072B/Cxx (needs HTTPS access and a key)
- SKYFi (different protocol, have a password)

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(freezegun)
BuildRequires:  python3dist(netifaces)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(urllib3)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
PyDaikin is a standalone program and a library that interface air conditioners
from Daikin. Currently the following Daikin WiFi modules are supported:

- BRP069Axx/BRP069Bxx/BRP072Axx
- BRP15B61 aka. AirBase (similar protocol as BRP069Axx)
- BRP072B/Cxx (needs HTTPS access and a key)
- SKYFi (different protocol, have a password)

%prep
%autosetup -n mustang51-%{pypi_name}-d768d0acee75
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pkg_name}
%doc README.md
%license LICENSE
%{_bindir}/pydaikin
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.4.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.0-1
- Initial package for Fedora
