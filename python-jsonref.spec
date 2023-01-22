%global pypi_name jsonref

Name:           python-%{pypi_name}
Version:        0.2
Release:        9%{?dist}
Summary:        An implementation of JSON Reference for Python

License:        MIT
URL:            https://github.com/gazpachoking/jsonref
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-pytest

%description
jsonref is a library for automatic dereferencing of JSON Reference objects
for Python (supporting Python 2.6+ and Python 3.3+).

This library lets you use a data structure with JSON reference objects, as if
the references had been replaced with the referent data.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
jsonref is a library for automatic dereferencing of JSON Reference objects
for Python (supporting Python 2.6+ and Python 3.3+).

This library lets you use a data structure with JSON reference objects, as if
the references had been replaced with the referent data.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# DOS line ending
sed -i -e 's/\r$//' README.rst


%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest tests.py


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/proxytypes.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Nils Philippsen <nils@redhat.com> - 0.2-2
- Don't be obsoleted by fedora-obsolete-packages (on F33, #1900537).

* Tue Sep 08 2020 Aurelien Bompard <abompard@fedoraproject.org> - 0.2-1
- Initial package.
