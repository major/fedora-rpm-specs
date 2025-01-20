%global pypi_name inject

%global pkg_description %{expand:Dependency injection the python way, the good way.

Key features:
  - Fast.
  - Thread-safe.
  - Simple to use.
  - Does not steal class constructors.
  - Does not try to manage your application object graph.
  - Transparently integrates into tests.
  - Supports type hinting in Python 3.5+.
  - Autoparams leveraging type annotations.
}
 
Name: python-%{pypi_name}
Summary: Dependency injection, the Python way
License: Apache-2.0

Version: 5.2.1
Release: 4%{?dist}

URL: https://github.com/ivankorobkov/python-%{pypi_name}
Source0: %pypi_source

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(pytest-runner)

BuildArch: noarch

%description
%{pkg_description}


%package -n python3-%{pypi_name}
Summary: %{summary}
BuildArch: noarch

%description -n python3-%{pypi_name}
%{pkg_description}


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
%pyproject_check_import
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.md README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.2.1-2
- Rebuilt for Python 3.13

* Sun Mar 24 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 5.2.1-1
- Update to v5.2.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 23 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 5.2.0-1
- Update to v5.2.0

* Sat Oct 21 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 5.1.0-1
- Update to v5.1.0
- Migrate License tag to SPDX

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.3.1-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.3.1-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.3.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 4.3.1-2
- Use python3dist() for specifying dependencies
- Run tests using pytest instead of nosetests

* Fri Sep 25 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 4.3.1-1
- Initial packaging
