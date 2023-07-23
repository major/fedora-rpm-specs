%global srcname twitter
%global sum A python wrapper around the Twitter API

Name:			python-%{srcname}
Summary:		%{sum}
Version:		3.5
Release:		18%{?dist}
License:		ASL 2.0
Source0:		https://github.com/bear/python-twitter/archive/v%{version}.tar.gz
URL:			https://github.com/bear/python-twitter
BuildArch:		noarch
BuildRequires:		python3-devel, python3-setuptools, python3-simplejson
BuildRequires:		python3-future, python3-httplib2, python3-requests-oauthlib
BuildRequires:		python3-pytest, python3-responses, python3-mccabe, python3-pytest-runner
BuildRequires:		python3-coverage, python3-mock, python3-setuptools_scm

%description
This library provides a pure python interface for the Twitter API. Twitter 
(http://twitter.com) provides a service that allows people to connect via the 
web, IM, and SMS. Twitter exposes a web services API 
(http://twitter.com/help/api) and this library is intended to make it even 
easier for python programmers to use. 

%package -n python3-%{srcname}
Summary:		%{sum}
Requires:		python3-simplejson, python3-httplib2, python3-requests-oauthlib
Requires:		python3-future
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This library provides a pure python interface for the Twitter API. Twitter 
(http://twitter.com) provides a service that allows people to connect via the 
web, IM, and SMS. Twitter exposes a web services API 
(http://twitter.com/help/api) and this library is intended to make it even 
easier for python programmers to use.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%check
# Tests assume network is up. Can't run them in koji.
%if 0 
export PYTHONPATH=%{buildroot}/%{python_sitelib}
%{__python} setup.py test
%endif

%files -n python3-%{srcname}
%doc README.rst CHANGES COPYING AUTHORS.rst
%license LICENSE
%{python3_sitelib}/*

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 3.5-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 3.5-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.5-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.5-8
- Remove flake8 build dependency

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct  1 2018 Tom Callaway <spot@fedoraproject.org> - 3.5-1
- update to 3.5
- drop python2 support (bz1634877)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3-4
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 05 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.3-1
- 3.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.1-2
- Rebuild for Python 3.6

* Fri Aug 12 2016 Tom Callaway <spot@fedoraproject.org> - 3.1-1
- update to 3.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Callaway <spot@fedoraproject.org> - 3.0-1
- update to 3.0
- modern packaging for Python 3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 24 2014 Tom Callaway <spot@fedoraproject.org> - 2.0-1
- fix missing dep (bz1167232)
- update to v2.0
- correct URL and Source0 for new home

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct  8 2013 Tom Callaway <spot@fedoraproject.org> - 1.1-1
- update to 1.1

* Fri Jun  7 2013 Tom Callaway <spot@fedoraproject.org> - 1.0-1
- update to 1.0 (supports twitter api v1.1)

* Fri Feb  8 2013 Tom Callaway <spot@fedoraproject.org> - 0.8.5-1
- 0.8.5

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 09 2011 Tom Callaway <spot@fedoraproject.org> - 0.8.2-1
- update to 0.8.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan  4 2011 Tom Callaway <spot@fedoraproject.org> - 0.8.1-1
- update to 0.8.1

* Fri Oct 22 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.8-1
- update to 0.8, fixes code to work with oauth twitter

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6-2
- fix files so they do not have hardcoded !#/usr/bin/python2.4

* Thu Jul  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6-1
- update to 0.6

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5-2
- Rebuild for Python 2.6

* Mon Oct 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.5-1
- Initial package for Fedora
