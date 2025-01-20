%global pypi_name pyairvisual

Name:           python-%{pypi_name}
Version:        2023.12.0
Release:        2%{?dist}
Summary:        Python API client for AirVisual air quality data

License:        MIT
URL:            https://github.com/bachya/pyairvisual
# pypi source does not contain tests
Source0:        https://github.com/bachya/pyairvisual/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pyairvisual is a simple library for interacting with AirVisual to retrieve
air quality information.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-aresponses

%description -n python3-%{pypi_name}
pyairvisual is a simple library for interacting with AirVisual to retrieve
air quality information.

%prep
%autosetup -n %{pypi_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# test_cloud_api requires network access
%pytest -v --ignore examples/test_cloud_api.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2023.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 21 2024 Orion Poplawski <orion@nwra.com> - 2023.12.0-1
- Update to 2023.12.0 for numpy 2.x support
- Use github source and run tests

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 5.0.5-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 5.0.5-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 5.0.5-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.0.5-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.5-1
- Update to latest upstream release 5.0.5

* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.2-1
- Update to latest upstream release 5.0.2 (#1880002)

* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.1-2
- Update to latest upstream release 5.0.1

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.0-1
- Initial package for Fedora
