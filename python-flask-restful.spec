%global srcname flask-restful
%global sum Simple framework for creating REST APIs for Flask

Name:           python-%{srcname}
Version:        0.3.9
Release:        6%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://www.github.com/%{srcname}/%{srcname}/
Source0:        https://github.com/%{srcname}/%{srcname}/archive/v%{version}.tar.gz

# From flask 2.1.0 the redirects are now relative
# Sent upstream: https://github.com/flask-restful/flask-restful/pull/942
Patch0:         fix-relative-redirect.patch

BuildArch:      noarch

BuildRequires:  python3-flask
BuildRequires:  python3-six
BuildRequires:  python3-aniso8601
BuildRequires:  python3-pytz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-blinker

%description
Flask-RESTful is Python extension for Flask that adds support
for quickly building REST APIs. It is a lightweight abstraction
that works with your existing ORM/libraries.

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       python3-flask
Requires:       python3-six
Requires:       python3-aniso8601
Requires:       python3-pytz
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Flask-RESTful is Python 3 extension for Flask that adds support
for quickly building REST APIs. It is a lightweight abstraction
that works with your existing ORM/libraries.

%prep
%setup -qn %{srcname}-%{version}
rm -rf docs/_themes/.gitignore

%patch0 -p1

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc AUTHORS.md README.md examples/ docs/
%license LICENSE
%{python3_sitelib}/flask_restful/
%{python3_sitelib}/Flask_RESTful-*.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.3.9-5
- Rebuilt for Python 3.11

* Fri May 13 2022 Charalampos Stratakis <cstratak@redhat.com> - 0.3.9-4
- Fix to a relative redirect on test_api with Flask >= 2.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Lumír Balhar <lbalhar@redhat.com> - 0.3.9-1
- Update to 0.3.9

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.8-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-3
- Rebuilt for Python 3.9

* Thu May 07 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.3.8-2
- Fix tests with python3-werkzeug >= 1.0

* Fri Feb 07 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.3.8-1
- Release 0.3.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.7-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.3.7-2
- Don't include entire python3_sitelib in files

* Tue Feb 12 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.3.7-1
- Update to upstream 0.3.7 release
- Drop upstreamed patch: 0003-Fix-tests_api-list-traceback.patch
- Drop upstreamed patch: 0001-Fix-arguments-with-type-list-705.patch
- Drop upstreamed patch: 0002-Support-aniso8601-3.0-in-tests.patch
- Drop no longer needed patch: python-flask-restful.remove_q0_testcase.patch
- Drop Fedora 27 support
- Drop Python 2 support

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Kamil Páral <kparal@redhat.com> - 0.3.6-7
- Add Patch3 to fix tests

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-6
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-5
- Rebuilt for Python 3.7

* Mon Jun 04 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.3.6-4
- Backport upstream fix: Support-aniso8601-3.0-in-tests

* Thu Mar 29 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.3.6-3
- Backport upstream fix: Fix-arguments-with-type-list-705

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.6-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Mar 15 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.5-5
- Rebuild for Python 3.6

* Mon Oct 17 2016 Ralph Bean <rbean@redhat.com> - 0.3.5-4
- Conditionalize python3 package for EPEL7.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Jan Sedlak <jsedlak@redhat.com> - 0.3.5-1
- update to newest version

* Fri Nov 13 2015 Jan Sedlak <jsedlak@redhat.com> - 0.3.4-3
- change specfile to be more aligned with guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Aug 20 2015 Jan Sedlak <jsedlak@redhat.com> - 0.3.4-1
- update version, correct project URL

* Tue Jul 07 2015 Jan Sedlak <jsedlak@redhat.com> - 0.3.3-1
- package newest version

* Wed Jan 22 2014 Jan Sedlak <jsedlak@redhat.com> - 0.2.11-1
- initial packaging
