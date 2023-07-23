%global upstream_name fdb
%global sum Firebird RDBMS bindings for Python

Name:           python-%{upstream_name}
Version:        2.0.1
Release:        10%{?dist}
Summary:        %{sum}

License:        BSD
URL:            http://www.firebirdsql.org/
Source0:        https://pypi.io/packages/source/f/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildArch:      noarch      
BuildRequires:  firebird-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%description
Set of Firebird RDBMS bindings for Python. 

%package -n python3-%{upstream_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{upstream_name}}
Requires:       libfbclient2

%description -n python3-%{upstream_name}
Set of Firebird RDBMS bindings for Python.


%prep
%autosetup -n %{upstream_name}-%{version}
rm -rf %{upstream_name}.egg-info

%build
%py3_build

%install
%py3_install
 
%files -n python3-%{upstream_name}
%doc README.rst
%license LICENSE.TXT
%{python3_sitelib}/*


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.1-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Philippe Makowski <makowski@fedoraproject.org> - 2.0.1-1
- New upstream 2.0.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Philippe Makowski <makowski@fedoraproject.org> - 2.0.0-1
- New upstream 2.0.0

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8-5
- Subpackage python2-fdb has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Philippe Makowski <makowski@fedoraproject.org> - 1.8-1
- New upstream 1.8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Philippe Makowski <makowski@fedoraproject.org> - 1.7-1
- New upstream 1.7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6-5
- Rebuild for Python 3.6

* Fri Oct 14 2016 Philippe Makowski <makowski@fedoraproject.org> - 1.6-4
- Change requires for Firebird 3 

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 27 2016 Till Maas <opensource@till.name> - 1.6-2
- Use %%upstream_name instead of undefined %%srcname (RH #1337609)

* Thu Mar 31 2016 Philippe Makowski <makowski@fedoraproject.org> - 1.6-1
- New upstream 1.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Philippe Makowski <makowski@fedoraproject.org> 1.4.11-1
- New upstream 1.4.11
- Use new macros and packaging rules

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun May 25 2014 Philippe Makowski <makowski@fedoraproject.org> 1.4-1
- New upstream 1.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 18 2013 Philippe Makowski <makowski@fedoraproject.org> 1.1-1
- New upstream 1.1 fix bug PYFB-30 - BLOBs are truncated at first zero byte

* Mon Apr 01 2013 Philippe Makowski <makowski@fedoraproject.org> 1.0-1
- New upstream 1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 01 2012 Philippe Makowski <makowski@fedoraproject.org> 0.9.9-1
- New upstream 0.9.9

* Tue Nov 27 2012 Philippe Makowski <makowski@fedoraproject.org> 0.9.1-1
- Initial package
