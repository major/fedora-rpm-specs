%global pypi_name py-august
%global pkg_name august

Name:           python-%{pkg_name}
Version:        0.25.2
Release:        7%{?dist}
Summary:        Python API for August Smart Lock and Doorbell

License:        MIT
URL:            https://github.com/snjoetw/py-august
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python API for August Smart Lock and Doorbell.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(aiounittest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(aioresponses)
BuildRequires:  python3dist(aiofiles)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3-dateutil
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Python API for August Smart Lock and Doorbell.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# Tests depend on asynctest: https://github.com/snjoetw/py-august/issues/51
#%%check
#%%pytest -v tests

%files -n python3-%{pkg_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pkg_name}/
%{python3_sitelib}/py_august-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.25.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.25.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.25.2-1
- Update to latest upstream release 0.25.2 (#1911706)

* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.25.0-1
- Initial package for Fedora
