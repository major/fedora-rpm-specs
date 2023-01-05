%global modname zope.schema

Summary: Zope 3 schemas
Name: python-zope-schema
Version: 7.0.1
Release: 1%{?dist}
License: ZPLv2.1
BuildArch: noarch
URL: http://pypi.python.org/pypi/zope.schema
Source0: %{pypi_source %{modname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This package is a zope.interface extension for defining data schemas.

%package -n python3-zope-schema
Summary:        Zope 3 schemas
%{?python_provide:%python_provide python3-zope-schema}

%description -n python3-zope-schema
This package is a zope.interface extension for defining data schemas.

%prep
%setup -q -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

# build Sphinx documents
PYTHONPATH="src" sphinx-build-%{python3_version} -b html docs/ build/sphinx/html
cp -pr build/sphinx/html .
rm -fr html/{.buildinfo,.doctrees}

%install
%pyproject_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} zope-testrunner --test-path=src

%files -n python3-zope-schema
%doc CHANGES.rst COPYRIGHT.txt README.rst
%doc html/
%license LICENSE.txt
%{python3_sitelib}/zope/schema/
%exclude %{python3_sitelib}/zope/schema/tests/
%{python3_sitelib}/%{modname}-*.dist-info
%{python3_sitelib}/%{modname}-*-nspkg.pth


%changelog
* Tue Jan 03 2023 Lumír Balhar <lbalhar@redhat.com> - 7.0.1-1
- Update to 7.0.1 (rhbz#2157742)

* Mon Jan 02 2023 Lumír Balhar <lbalhar@redhat.com> - 7.0.0-1
- Update to 7.0.0 (rhbz#2157265)

* Thu Sep 15 2022 Lumír Balhar <lbalhar@redhat.com> - 6.2.1-1
- Update to 6.2.1
Resolves: rhbz#2127023

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 6.2.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Lumír Balhar <lbalhar@redhat.com> - 6.2.0-1
- Update to 6.2.0
Resolves: rhbz#2014998

* Thu Oct 14 2021 Lumír Balhar <lbalhar@redhat.com> - 6.1.1-1
- Update to 6.1.1
Resolves: rhbz#2013600

* Sun Jul 25 2021 Neal Gompa <ngompa@fedoraproject.org> - 6.1.0-1
- Rebase to 6.1.0 (#1469326)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.4.2-21
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.4.2-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.2-16
- Subpackage python2-zope-schema has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.2-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 4.4.2-11
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.4.2-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Adam Williamson <awilliam@redhat.com> - 4.4.2-6
- Fix Sphinx doc generation
- Fix (in a stupid way, but it works) test running on recent Python 3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Ralph Bean <rbean@redhat.com> - 4.4.2-5
- Modernize python macros.
- Add an explicit python2 subpackage.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Ralph Bean <rbean@redhat.com> - 4.4.2-1
- new version

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 4.4.1-1
- Latest upstream.
- Modernized python macros.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 4.4.0-1
- Latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 4.3.2-1
- Latest upstream.
- README and CHANGES renamed from .txt to .rst.

* Wed Feb 13 2013 Ralph Bean <rbean@redhat.com> - 4.2.2-1
- Latest upstream.
- Added Python3 subpackage.
- Removed dos2unix references.  No longer needed.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 26 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1 (#741003)
- Fix ends of lines

* Thu Mar 31 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0 (#689215)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Robin Lee <cheeselee@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1
- Build Sphinx documents

* Thu Sep 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.7.0-1
- Update to 3.7.0
- Move the documents to proper place
- Exclude the tests

* Sat Sep 11 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.6.4-2
- Spec cleaned up
- Requires: python-zope-filesystem and python-setuptools removed
- Add %%check section and run tests
- BR: python-zope-testing and runtime requirements added
- Don't move the text files

* Wed Jun 16 2010 Robin Lee <robinlee.sysu@gmail.com> - 3.6.4-1
- Initial packaging
