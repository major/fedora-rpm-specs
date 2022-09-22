%global pypi_name jsonmodels
# Tests require invoke, which is only available for Fedora
%global use_tests 0%{?fedora:1}
# Python3 is not available on centos <= 7
%if 0%{?fedora} || 0%{?rhel} > 7
%global is_install_py3 1
%else
%global is_install_py3 0
%endif
Summary: Create Python structures that are converted to, or read from JSON
Name: python-jsonmodels
Version: 2.4
Release: 13%{?dist}
Source0: https://github.com/beregond/%{pypi_name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
License: BSD
BuildArch: noarch
Url: https://github.com/beregond/jsonmodels

%if %{is_install_py3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-invoke
%endif

%description
Models to make it easier to deal with structures that are converted to, or
read from JSON.

%if %{is_install_py3}
%package -n     python3-%{pypi_name}
Summary: %summary

BuildRequires: python3-dateutil
BuildRequires: python3-pytest
%if %{use_tests}
BuildRequires: python3-pytest-cov
%endif
BuildRequires: python3-six
Requires: python3-dateutil
Requires: python3-six

%description -n     python3-%{pypi_name}
Python 3 models to make it easier to deal with structures that are
converted to, or read from JSON.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if 0%{is_install_py3}
%py3_build
%endif

%install
%if 0%{is_install_py3}
%py3_install
%endif

%if %{use_tests}
%check
%if 0%{?py3_build:1}
PYTHONPATH=$(pwd) %{__python3} setup.py test
%endif
%endif

%if %{is_install_py3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}/
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.4-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Yatin Karel <ykarel@redhat.com> - 2.4-1
- Update to 2.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2-6
- Subpackage python2-jsonmodels has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 15 2017 Omer Anson <oaanson@gmail.com> 2.2-1
- Fix use_tests and is_install_py3 conditions
- Initial release
