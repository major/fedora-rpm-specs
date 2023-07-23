%global pypi_name aioambient

Name:           python-%{pypi_name}
Version:        2022.10.0 
Release:        3%{?dist}
Summary:        Python library for the Ambient Weather API

License:        MIT
URL:            https://github.com/bachya/aioambient
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
aioambient is a Python, asyncio-driven library that interfaces with both the
REST and Websocket APIs provided by Ambient Weather.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aioambient is a Python 3, asyncio-driven library that interfaces with both the
REST and Websocket APIs provided by Ambient Weather.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2022.10.0-2
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Fabian Affolter <mail@fabian-affolter.ch> - 2022.10.0-1
- Update to latest upstream release 2022.10.0 (closes rhbz#2010538)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Initial package for Fedora

