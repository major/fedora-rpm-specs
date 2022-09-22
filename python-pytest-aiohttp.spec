# Enable tests by default.
%bcond_without tests

%global pypi_name pytest-aiohttp

Name:           python-%{pypi_name}
Version:        1.0.4
Release:        4%{?dist}
Summary:        Pytest plugin for aiohttp support

License:        ASL 2.0
URL:            https://github.com/aio-libs/pytest-aiohttp/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The library allows to use aiohttp pytest plugin without need for implicitly
loading it like pytest_plugins = 'aiohttp.pytest_plugin'.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The library allows to use aiohttp pytest plugin without need for implicitly
loading it like pytest_plugins = 'aiohttp.pytest_plugin'.

%prep
%autosetup -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_aiohttp


%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{pypi_name}  -f %{pyproject_files}
%doc CHANGES.rst README.rst
%license LICENSE

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.4-3
- Rebuilt for Python 3.11

* Thu Apr 28 2022 Major Hayden <major@mhtx.net> - 1.0.4-2
- Update to use pyproject-rpm-macros.

* Thu Mar 03 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.4-1
- Update to latest upstream release 1.0.4 (closes rhbz#2054997)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.0-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-9
- Add python3-setuptools as BR

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-8
- Add python3-setuptools as BR

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-2
- Change source (rhbz#1719010)

* Mon Jun 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package for Fedora
