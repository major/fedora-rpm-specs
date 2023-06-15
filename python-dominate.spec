%global pypi_name dominate

Name:           python-%{pypi_name}
Version:        2.7.0
Release:        3%{?dist}
Summary:        Python library for HTML documents

License:        GPLv3
URL:            http://github.com/Knio/dominate/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Dominate is a Python library for creating and manipulating HTML documents 
using an elegant DOM API. It allows you to write HTML pages in pure Python
very concisely, which eliminates the need to learn another template language,
and lets you take advantage of the more powerful features of Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Dominate is a Python library for creating and manipulating HTML documents 
using an elegant DOM API. It allows you to write HTML pages in pure Python
very concisely, which eliminates the need to learn another template language,
and lets you take advantage of the more powerful features of Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check 
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*egg-info

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.7.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.0-1
- Update to latest upstream release 2.7.0 (closes rhbz#2110288)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.6.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.0-1
- Update to latest upstream release 2.6.0 (#1890015)

* Sat Aug 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.2-1
- Update to latest upstream release 2.5.2 (#1871364)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.1-1
- Update to latest upstream release 2.5.1 (#1697397)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-6
- Subpackage python2-dominate has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-4
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jul 04 2017 David Hannequin <david.hannequin@gmail.com> - 2.3.1-1
- Initial package.
