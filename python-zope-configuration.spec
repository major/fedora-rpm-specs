%global modname zope.configuration
%global desc The zope configuration system provides an extensible system for supporting\
various kinds of configurations.\
\
It is based on the idea of configuration directives. Users of the configuration\
system provide configuration directives in some language that express\
configuration choices. The intent is that the language be pluggable. An XML\
language is provided by default.
%global sum Zope Configuration Markup Language (ZCML)



Name:           python-zope-configuration
Version:        4.4.1
Release:        2%{?dist}
Summary:        %{sum}

License:        ZPLv2.1
URL:            https://github.com/zopefoundation/zope.configuration
Source0:        %{url}/archive/4.4.1/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-zope-schema
BuildRequires:  python3-zope-interface
BuildRequires:  python3-zope-i18nmessageid
BuildRequires:  python3-zope-testing


%description
%{desc}


%package -n python3-zope-configuration
Summary:        %{sum}

Requires:  python3-zope-schema
Requires:  python3-zope-interface
Requires:  python3-zope-i18nmessageid

%{?python_provide:%python_provide python3-zope-configuration}


%description -n python3-zope-configuration
%{desc}

%prep
%setup -q -n %{modname}-%{version}
rm -rf %{modname}.egg-info


%build
%py3_build

%install
%py3_install
rm -r %{buildroot}%{python3_sitelib}/zope/configuration/tests


#check
# The tests do not pass with Python 3.6 as has been documented upstream:
# https://github.com/zopefoundation/zope.configuration/issues/16
#{__python3} setup.py test


%files -n python3-zope-configuration
%license COPYRIGHT.txt LICENSE.txt
%doc README.rst CHANGES.rst
%{python3_sitelib}/zope/configuration/
%{python3_sitelib}/%{modname}*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Kevin Fenzi <kevin@scrye.com> - 4.4.1-1
- Update to 4.4.1. Fixes rhbz#2072854

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 4.4.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.4.0-2
- Rebuilt for Python 3.10

* Sat May 22 2021 Kevin Fenzi <kevin@scrye.com> - 4.4.0-1
- Update to 4.4.0. Fixes rhbz#1446009

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-18
- Subpackage python2-zope-configuration has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-13
- Rebuilt for Python 3.7

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0.3-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.0.3-10
- The python2- subpackage now provides the python- name.
- Correct a changelog entry from the last build not to use a macro.

* Fri Feb 24 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
- Disabled tests in Python 3 due to them failing upstream.
- Mark the license with the license macro.
- Rename python-zope-configuration to python2-zope-configuration.
- Used GitHub as new URL and Source0 since the old URLs were 404.
- Dropped BuildRoot.
- Use global instead of define for modname variable.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun May 04 2014 Luke Macken <lmacken@redhat.com> - 4.0.3-1
- Update to 4.0.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Ralph Bean <rbean@redhat.com> - 4.0.2-1
- Latest upstream
- Added python3 subpackage
- Removed clean section
- Removed defattr

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan  2 2010 Luke Macken <lmacken@redhat.com> - 3.7.2-1
- Initial package
