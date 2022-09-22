# Created by pyp2rpm-3.0.0
%global pypi_name virtualenv-api
%global underscore_name virtualenv_api

# test suite is disabled default for koji builds,
# because the tests require internet connection.
%global run_test_suite 0

Name:           python-%{pypi_name}
Version:        2.1.18
Release:        7%{?dist}
Summary:        An API for virtualenv/pip

License:        BSD
URL:            https://github.com/sjkingo/virtualenv-api
Source0:        %pypi_source

# Add tests and LICENSE missing in sources
Patch0:         add_tests_license.patch

BuildArch:      noarch
 
BuildRequires:  git-all
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-virtualenv
BuildRequires:  python3-six
BuildRequires:  python3-pip

%description
virtualenv-api - an API for virtualenv
Tool to create isolated Python environments. Unfortunately, 
it does not expose a native Python API. This package aims to 
provide an API in the form of a wrapper around virtualenv.

%package -n     python3-%{pypi_name}
Summary:        An API for virtualenv/pip
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-six
Requires:       python3-virtualenv
Requires:       python3-pip
%description -n python3-%{pypi_name}
virtualenv-api - an API for virtualenv
Tool to create isolated Python environments. Unfortunately, 
it does not expose a native Python API. This package aims to 
provide an API in the form of a wrapper around virtualenv.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if 0%{run_test_suite}
%check
%{__python3} tests.py
%endif # run_test_suite

%files -n python3-%{pypi_name} 
%license LICENSE
%doc README.rst
%{python3_sitelib}/virtualenvapi
%{python3_sitelib}/%{underscore_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.18-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.18-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 09 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.1.18-1
- Update to 2.1.18 (rhbz#1797387)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.16-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.16-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.16-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.16-7
- Subpackage python2-virtualenv-api has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.16-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Michal Cyprian <mcyprian@redhat.com> - 2.1.16-1
- Update to 2.1.16

* Thu Feb 23 2017 Michal Cyprian <mcyprian@redhat.com> - 2.1.14-1
- Update to 2.1.14

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.9-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Michal Cyprian <mcyprian@redhat.com> - 2.1.8-4
- Update to 2.1.9

* Wed Apr 13 2016 Michal Cyprian <mcyprian@redhat.com> - 2.1.8-2
- Add requires, use test_suite enabling macro

* Wed Mar 30 2016 Michal Cyprian <mcyprian@redhat.com> - 2.1.8-1
- Initial package.
