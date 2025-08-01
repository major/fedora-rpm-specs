# Created by pyp2rpm-3.3.5
%global pypi_name bracex

Name:           python-%{pypi_name}
Version:        2.5
Release:        4%{?dist}
Summary:        Bash style brace expander

License:        MIT
URL:            https://github.com/facelessuser/bracex
Source0:        https://github.com/facelessuser/bracex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
Bracex is a brace expanding library (à la Bash) for Python.
Brace expanding is used to generate arbitrary strings.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Bracex is a brace expanding library (à la Bash) for Python.
Brace expanding is used to generate arbitrary strings.


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -vv

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md docs/src/markdown/about/license.md
%doc README.md

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 2.5-3
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 Parag Nemade <pnemade AT redhat DOT com> - 2.5-1
- Update to new upstream release 2.5

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.1-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Parag Nemade <pnemade AT redhat DOT com> - 2.1.1-11
- Mark this as SPDX license expression converted

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.1.1-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.1-3
- Rebuilt for Python 3.10

* Sat Feb 20 2021 Parag Nemade <pnemade AT redhat DOT com> - 2.1.1-2
- Fix this package as per package review (#1929990)
- Change Source to github to use tests

* Thu Feb 18 2021 Parag Nemade <pnemade AT redhat DOT com> - 2.1.1-1
- Initial package.
