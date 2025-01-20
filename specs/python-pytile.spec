%global pypi_name pytile

Name:           python-%{pypi_name}
Version:        2022.02.0
Release:        11%{?dist}
Summary:        Python API for Tile Bluetooth trackers

License:        MIT
URL:            https://github.com/bachya/pytile
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pytile is a simple Python library for retrieving information on Tile
Bluetooth trackers (including last location and more).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(aresponses)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(yarl)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pytile is a simple Python library for retrieving information on Tile
Bluetooth trackers (including last location and more).

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/pylint/d' pyproject.toml      

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2022.02.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.02.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2022.02.0-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.02.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.02.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.02.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 2022.02.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.02.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.02.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2022.02.0-2
- Rebuilt for Python 3.11

* Thu Mar 24 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2022.02.0-1
- Update to latest upstream release 2022.02.0 (closes rhbz#2050067)

* Tue Jan 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2022.01.0-1
- Update to latest upstream release 2022.01.0 (closes rhbz#2014944)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 5.2.3-1
- Update to latest upstream release 5.2.3 (closes rhbz#1934437)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.2.1-2
- Rebuilt for Python 3.10

* Wed Mar 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 5.2.1-1
- Update to latest upstream release 5.1. (fedora#1934437)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Fabian Affolter <mail@fabian-affolter.ch> - 5.1.1-1
- Update to latest upstream release 5.1.1

* Sat Sep 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.1-1
- Initial package for Fedora
