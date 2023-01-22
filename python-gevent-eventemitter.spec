%global pypi_name gevent-eventemitter
%global modname eventemitter
%global eggname gevent_%{modname}

Name:       python-%{pypi_name}
Version:    2.1
Release:    8%{?dist}
Summary:    EventEmitter using gevent
BuildArch:  noarch

# https://github.com/rossengeorgiev/gevent-eventemitter/pull/3
License:    MIT

URL:        https://github.com/rossengeorgiev/gevent-eventemitter

# Tests works only woth GitHub sources
Source0:    %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(coverage) >= 4.0.3
BuildRequires: python3dist(gevent) >= 1.3
BuildRequires: python3dist(mock)
BuildRequires: python3dist(pytest-cov) >= 2.5.1
BuildRequires: python3dist(pytest) >= 3.2.1

%global _description %{expand:
This module implements EventEmitter with gevent.}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
%{python3} -m pytest -v


%files -n python3-%{pypi_name}
%dnl %license LICENSE
%doc README.rst
%{python3_sitelib}/%{eggname}-%{version}-*.egg-info
%{python3_sitelib}/%{modname}/


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1-3
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1-2
- build: Polish to conform Fedora guidelines

* Wed Sep 16 2020 gasinvein <gasinvein@gmail.com> - 2.1-0.1
- Initial package
