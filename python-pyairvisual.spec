%global pypi_name pyairvisual

Name:           python-%{pypi_name}
Version:        5.0.5
Release:        8%{?dist}
Summary:        Python API client for AirVisual air quality data

License:        MIT
URL:            https://github.com/bachya/pyairvisual
Source0:        %{pypi_source}
BuildArch:      noarch

%description
pyairvisual is a simple library for interacting with AirVisual to retrieve
air quality information.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%{?python_provide:%python_provide python3-%{pypi_name}}

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

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
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