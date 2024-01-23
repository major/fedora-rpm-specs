%global pypi_name boolean.py

Name:           python-%{pypi_name}
Version:        4.0
Release:        5%{?dist}
Summary:        Define boolean algebras, and create and parse boolean expressions

License:        BSD
URL:            https://github.com/bastikr/boolean.py
Source0:        %pypi_source

BuildArch:      noarch

%global _description \
"boolean.py" is a small library implementing a boolean algebra. It defines\
two base elements, TRUE and FALSE, and a Symbol class that can take on one of\
these two values. Calculations are done in terms of AND, OR and NOT - other\
compositions like XOR and NAND are not implemented but can be emulated with\
AND or and NOT. Expressions are constructed from parsed strings or in Python.

%description %{_description}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  %{py3_dist Sphinx}

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
sphinx-build-%{python3_version} docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst html/
%{python3_sitelib}/boolean.py*.egg-info/
%{python3_sitelib}/boolean/

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 4.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 06 2022 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 4.0-1
- new version

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.8-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.8-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.8-1
- Update to 3.8 (#1846144)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.7-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 3.7-1
- new version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 08 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 3.6-1
- New package.
