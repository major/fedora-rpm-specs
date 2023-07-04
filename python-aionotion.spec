%global pypi_name aionotion

Name:           python-%{pypi_name}
Version:        2.0.3
Release:        10%{?dist}
Summary:        Python library for Notion Home Monitoring

License:        MIT
URL:            https://github.com/bachya/aionotion
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A asyncio-friendly library for Notion Home Monitoring devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A asyncio-friendly library for Notion Home Monitoring devices.

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
* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 2.0.3-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.0.3-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.3-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.3-2
- Use pyproject-rpm-macros (rhbz#1875865)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.3-1
- Initial package for Fedora
