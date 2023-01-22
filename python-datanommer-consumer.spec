%global modname datanommer.consumer

Name:           python-datanommer-consumer
Version:        0.8.1
Release:        19%{?dist}
Summary:        Hub consumer plugin for datanommer

License:        GPLv3+
URL:            https://pypi.io/project/%{modname}
Source0:        https://pypi.io/packages/source/d/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
Hub consumer plugin for datanommer.

%description %_description

%package -n python3-datanommer-consumer
Summary: %summary

%{?python_provide:%python_provide python3-datanommer-consumer}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  python3-datanommer-models >= 0.6.0
BuildRequires:  python3-fedmsg-core

Requires:       python3-datanommer-models >= 0.6.0
Requires:       python3-fedmsg-core

%description -n python3-datanommer-consumer %_description

%prep
%setup -q -n %{modname}-%{version}

# Remove upstream egg-info so that it gets rebuilt.
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-datanommer-consumer
%doc README.rst LICENSE
%{python3_sitelib}/datanommer/consumer/
%{python3_sitelib}/%{modname}-%{version}*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.8.1-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.1-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.1-5
- Subpackage python2-datanommer-consumer has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.7

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.8.1-2
- Python3 subpackage.

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.8.1-1
- new version

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.0-3
- Python 2 binary package renamed to python2-datanommer-consumer
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Ralph Bean <rbean@redhat.com> - 0.8.0-1
- new version

* Fri Mar 03 2017 Ralph Bean <rbean@redhat.com> - 0.7.0-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- Latest upstream with license headers.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 11 2013 Ian Weller <iweller@redhat.com> - 0.6.0-1
- UUID support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Ralph Bean <rbean@redhat.com> - 0.4.3-1
- Latest upstream with a bugfix; catch sqlalchemy session
  errors and rollback to avoid crippling ourselves.

* Thu Feb 07 2013 Ralph Bean <rbean@redhat.com> - 0.4.1-1
- Latest upstream from Jessica Anderson.
- Removed dep on python-nose since tests are not run.

* Mon Oct 22 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-4
- Remove exlicit versioned conflicts with old datanommer.

* Fri Oct 12 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-3
- Remove unnecessary CFLAGS definition.

* Thu Oct 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-2
- Remove upstream egg-info so that it gets rebuilt.

* Thu Oct 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-1
- Initial split out from the main datanommer package.
