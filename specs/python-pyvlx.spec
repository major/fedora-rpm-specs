%global pypi_name pyvlx

Name:           python-%{pypi_name}
Version:        0.2.26
Release:        2%{?dist}
Summary:        Python wrapper for the Velux KLF 200 API

License:        LGPL-3.0-or-later
URL:            https://github.com/Julius2342/pyvlx
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
PyVLX allow you to control VELUX windows with Python. It uses the Velux
KLF 200 interface to control io-Homecontrol devices, e.g., Velux
Windows.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(typing-extensions)

%description -n python3-%{pypi_name}
PyVLX allow you to control VELUX windows with Python. It uses the Velux
KLF 200 interface to control io-Homecontrol devices, e.g., Velux
Windows.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

%check
%pytest -v test

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 09 2025 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.26-1
- Update to latest upstream release (closes rhbz#2327983)

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.2.20-13
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.20-10
- convert license to SPDX

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.20-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.20-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.20-2
- Rebuilt for Python 3.11

* Wed Jan 26 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.20-1
- Update to latest upstream release 0.2.20 (closes #2046039)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.19-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.19-1
- Update to latest upstream release 0.2.19

* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.17-1
- Initial package for Fedora
