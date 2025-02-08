%global srcname envisage
#global commit 872c66885d64a22502fe3efceecec99c11a1c8ff
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        7.0.3
Release:        7%{?dist}
Summary:        Extensible application framework

# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file.
# All remaining source or image files are in BSD 3-clause license
License:        BSD-3-Clause AND LGPL-2.0-only AND CC-BY-SA-1.0 AND CC-BY-SA-2.5 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0
URL:            https://github.com/enthought/envisage
Source0:        https://github.com/enthought/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
# For docs
BuildRequires:  python%{python3_pkgversion}-sphinx-copybutton
BuildRequires:  python%{python3_pkgversion}-enthought-sphinx-theme
# For tests
BuildRequires:  /usr/bin/xvfb-run

%description
Envisage is a Python-based framework for building extensible applications,
that is, applications whose functionality can be extended by adding
"plug-ins".  Envisage provides a standard mechanism for features to be added
to an application, whether by the original developer or by someone else.  In
fact, when you build an application using Envisage, the entire application
consists primarily of plug-ins.  In this respect, it is similar to the Eclipse
and Netbeans frameworks for Java applications.

Each plug-in is able to:

* Advertise where and how it can be extended (its "extension points").
* Contribute extensions to the extension points offered by other plug-ins.
* Create and share the objects that perform the real work of the application
  ("services").

The Envisage project provides the basic machinery of the plug-in framework as
well as GUI building tools (envisage.ui).  The workbench is the older way to
build GUIs from Envisage.  It is now recommended to use the Task framework. 


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Extensible application framework
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname}
Envisage is a Python-based framework for building extensible applications,
that is, applications whose functionality can be extended by adding
"plug-ins".  Envisage provides a standard mechanism for features to be added
to an application, whether by the original developer or by someone else.  In
fact, when you build an application using Envisage, the entire application
consists primarily of plug-ins.  In this respect, it is similar to the Eclipse
and Netbeans frameworks for Java applications.

Each plug-in is able to:

* Advertise where and how it can be extended (its "extension points").
* Contribute extensions to the extension points offered by other plug-ins.
* Create and share the objects that perform the real work of the application
  ("services").

The Envisage project provides the basic machinery of the plug-in framework as
well as GUI building tools (envisage.ui).  The workbench is the older way to
build GUIs from Envisage.  It is now recommended to use the Task framework. 


%package doc
Summary:        Documentation for %{name}
License:        BSD-3-Clause AND CC-BY-SA-1.0 AND CC-BY-SA-2.5 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0

%description doc
Documentation and examples for %{name}


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Fix line endings
sed -i -e 's/\r//' docs/source/envisage_core_documentation/*.rst
# Cleanup
find -name .gitignore -delete

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
xvfb-run %__python3 -m sphinx -b html docs/source docs/build
rm docs/build/.buildinfo
mv docs/build docs/html


%install
%pyproject_install
%pyproject_save_files %{srcname}
# Do not ship tests
find %{buildroot}%{python3_sitelib}/%{srcname} -name tests -type d -exec rm -r {} +
sed -i -e '\,/tests$,d' -e '\,/tests/,d' %{pyproject_files}


%check
xvfb-run %{__python3} -m unittest discover -v envisage

 
%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license *LICENSE*

%files doc
%license *LICENSE*
%doc docs/html examples


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Python Maint <python-maint@redhat.com> - 7.0.3-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 05 2023 Orion Poplawski <orion@nwra.com> - 7.0.3-1
- Update to 7.0.3

* Sat Mar 25 2023 Orion Poplawski <orion@nwra.com> - 7.0.1-1
- Update to 7.0.1
- Use SPDX License tag

* Thu Feb 16 2023 Orion Poplawski <orion@nwra.com> - 6.1.1-1
- Update to 6.1.1

* Sat Jan 21 2023 Scott Talbert <swt@techie.net> - 6.1.0-3
- Cleanup and re-enable tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Orion Poplawski <orion@nwra.com> - 6.1.0-1
- Update to 6.1.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Orion Poplawski <orion@nwra.com> - 6.0.1-1
- Update to 6.0.1
- Ignore test failures for now

* Fri Jul 01 2022 Python Maint <python-maint@redhat.com> - 5.0.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.0.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Orion Poplawski <orion@nwra.com> - 5.0.0-1
- Update to 5.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.9.2-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Orion Poplawski <orion@nwra.com> - 4.9.2-1
- Update to 4.9.2

* Sat Feb 15 2020 Orion Poplawski <orion@nwra.com> - 4.9.1-1
- Update to 4.9.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Orion Poplawski <orion@nwra.com> - 4.9.0-1
- Update to 4.9.0

* Tue Oct  8 2019 Orion Poplawski <orion@nwra.com> - 4.8.0-1
- Update to 4.8.0 (FTBFS py3.8 bugz#1746848)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.7.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 5 2019 Orion Poplawski <orion@nwra.com> - 4.7.2-1
- Update to 4.7.2

* Sat Feb 9 2019 Orion Poplawski <orion@nwra.com> - 4.7.1-2
- Run tests with nose like upstream
- Add upstream patch to fix some tests
- Ignore test failures for now - does not support 3.7
- Do not ship tests

* Sat Feb 2 2019 Orion Poplawski <orion@nwra.com> - 4.7.1-1
- Update to 4.7.1
- Run tests with xvfb-run

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-2
- Subpackage python2-envisage has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 20 2018 Orion Poplawski <orion@nwra.com> - 4.6.0-1
- Update to 4.6.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-8
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.5.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 2 2016 Orion Poplawski <orion@cora.nwra.com> - 4.5.0-1
- Update to 4.5.0
- Ship python2/3-envisage
- Modernize spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-1
- Update to 4.4.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-3
- Remove shipped egg-info and eggs

* Tue May 7 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-2
- Fix line-endings, cleanup some files
- Fix license tag

* Wed May 1 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Initial package
