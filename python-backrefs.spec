# Created by pyp2rpm-3.3.5
%global pypi_name backrefs

Name:           python-%{pypi_name}
Version:        5.3
Release:        2%{?dist}
Summary:        A wrapper around re and regex that adds additional back references

License:        MIT
URL:            https://github.com/facelessuser/backrefs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(setuptools)

%description
Backrefs is a wrapper around Python's built-in Re and the 3rd party Regex
library. Backrefs adds various additional back references (and a couple other
features) that are known to some regular expression engines, but not to
Python's Re and/or Regex. The supported back references actually vary depending
on the regular expression engine being used as the engine may already have
support for some.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Backrefs is a wrapper around Python's built-in Re and the 3rd party Regex
library. Backrefs adds various additional back references (and a couple other
features) that are known to some regular expression engines, but not to
Python's Re and/or Regex. The supported back references actually vary depending
on the regular expression engine being used as the engine may already have
support for some.

%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{pypi_name} -i %{python3_sitelib}/%{pypi_name}-%{version}.dist-info extras}

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -w


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
py.test-3

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Parag Nemade <pnemade AT redhat DOT com> - 5.3-1
- Update to 5.3.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.0.1-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.0.1-6
- Rebuilt for Python 3.10

* Thu Mar 04 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0.1-5
- Drop some docs files which are not needed (rh#1929991)

* Wed Feb 24 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0.1-4
- Drop Requires: on (backrefs[extras])

* Wed Feb 24 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0.1-3
- Simplify URL: tag usage
- Drop unnecessary egg-info removal
- Use python-extras guidelines to provide python3.Xdist(backrefs[extras])

* Sat Feb 20 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0.1-2
- Change Source to github to use tests

* Thu Feb 18 2021 Parag Nemade <pnemade AT redhat DOT com> - 5.0.1-1
- Initial package.
