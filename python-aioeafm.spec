%global pypi_name aioeafm

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        9%{?dist}
Summary:        Python wrapper for the UK Environment Agency Flood Monitoring API

License:        ASL 2.0
URL:            https://github.com/Jc2k/aioeafm
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a thin Python wrapper for the Real Time flood
monitoring API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a thin Python wrapper for the Real Time flood
monitoring API.

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
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 1.0.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.0.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to latest upstream release 1.0.0

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Initial package for Fedora