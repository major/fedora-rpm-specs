%global modname traitsui 
Name:           python-%{modname}
Version:        8.0.0
Release:        7%{?dist}
Summary:        User interface tools designed to complement Traits

# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file.
# All remaining source or image files are in BSD-3-clause license
License:        BSD-3-clause AND EPL-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only
URL:            https://github.com/enthought/traitsui
Source0:        https://github.com/enthought/traitsui/archive/%{version}/traitsui-%{version}.tar.gz
# https://github.com/enthought/traitsui/pull/2028
Patch0:         python-traitsui-pyqt6.patch

Obsoletes:      %{name}-doc <= 5.0.0-2
BuildArch:      noarch
ExcludeArch:    ppc64le
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  mesa-dri-drivers

%description
The TraitsUI package is a set of user interface tools designed to complement
Traits. In the simplest case, it can automatically generate a user interface
for editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a Model-
View-Controller (MVC) design pattern for Traits-based objects.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:  dejavu-fonts-all
BuildRequires:  liberation-fonts
BuildRequires:  python%{python3_pkgversion}-devel
# pyproject install python3-pyqt5-base instead, this is needed for PyQt5.QtSvg
BuildRequires:  python%{python3_pkgversion}-qt5

%description -n python%{python3_pkgversion}-%{modname}
The TraitsUI package is a set of user interface tools designed to complement
Traits. In the simplest case, it can automatically generate a user interface
for editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a Model-
View-Controller (MVC) design pattern for Traits-based objects.

Python 3 version.

%prep
%autosetup -p1 -n %{modname}-%{version}
rm examples/demo

%generate_buildrequires
%pyproject_buildrequires -x pyqt5 -x pyqt6 -x test -x wx

%build
%pyproject_wheel

%install
%pyproject_install

%check
# Needed for wx tests
export LANG=en_US.UTF-8
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONUNBUFFERED=1
pushd build/lib/traitsui/tests/
status=0
# pyside6 is not packaged
for toolkit in null pyqt5 pyqt6 wx # pyside6
do
  # By default, fail build if tests fail
  fail=1
  # Decent default, overridded later if needed
  export QT_API=$toolkit
  case $toolkit in
    null) export ETS_TOOLKIT="null"; unset QT_API; export EXCLUDE_TESTS="(wx|qt)"; fail=0;;
    pyside2) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
    pyside6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
    # pyqt5 test fails on s390x - https://github.com/enthought/traitsui/issues/2029
%ifarch s390x
    pyqt5) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
%else
    pyqt5) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
%endif
    # pyqt6 tests fail - https://github.com/enthought/traitsui/issues/2027
    # https://github.com/enthought/pyface/issues/1249
    pyqt6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
    # wx currently failling - https://github.com/enthought/traitsui/issues/2030
    wx) export ETS_TOOLKIT="wx"; unset QT_API; export EXCLUDE_TESTS="qt"; fail=0;;
  esac
  # Adding -f can be helpful to debug missing components when tests segfault or similar
  xvfb-run %__python3 -s -X faulthandler -W default -m unittest discover -v traitsui || status=$(( $status + $fail ))
done
exit $status

popd


%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE.txt image_LICENSE*.txt
%doc README.rst CHANGES.txt examples
%{python3_sitelib}/%{modname}*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Python Maint <python-maint@redhat.com> - 8.0.0-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 13 2023 Orion Poplawski <orion@nwra.com> - 8.0.0-2
- Build for Python 3.12
- Drop BR on shiboken2
- Drop pyside2 tests - no longer maintained

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 11 2023 Orion Poplawski <orion@nwra.com> - 8.0.0-1
- Update to 8.0.0

* Sat Jan 28 2023 Orion Poplawski <orion@nwra.com> - 7.4.3-3
- Switch to unittest instead of nosetest

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Orion Poplawski <orion@nwra.com> - 7.4.3-1
- Update to 7.4.3

* Mon Nov 07 2022 Orion Poplawski <orion@nwra.com> - 7.4.2-1
- Update to 7.4.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Orion Poplawski <orion@nwra.com> - 7.4.0-1
- Update to 7.4.0

* Fri Jul 01 2022 Python Maint <python-maint@redhat.com> - 7.3.1-2
- Rebuilt for Python 3.11

* Sun Jun 05 2022 Orion Poplawski <orion@nwra.com> - 7.3.1-1
- Update to 7.3.1
- Update tests to be more like upstream

* Wed Mar 09 2022 Orion Poplawski <orion@nwra.com> - 7.3.0-1
- Update to 7.3.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 09 2021 Orion Poplawski <orion@nwra.com> - 7.2.1-1
- Update to 7.2.1
- Add patch to force integer type where needed

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.1.1-4
- Rebuilt for Python 3.10

* Fri Apr 30 2021 Orion Poplawski <orion@nwra.com> - 7.1.1-3
- Remove broken demo symlink that breaks upgrades (bz#1955354)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Orion Poplawski <orion@nwra.com> - 7.1.1-1
- Update to 7.1.1

* Sat Oct 31 2020 Orion Poplawski <orion@nwra.com> - 7.1.0-1
- Update to 7.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Orion Poplawski <orion@nwra.com> - 7.0.1-1
- Update to 7.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.0-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Orion Poplawski <orion@nwra.com> - 7.0.0-1
- Update to 7.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Orion Poplawski <orion@nwra.com> - 6.1.3-1
- Update to 6.1.3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May  8 2019 Orion Poplawski <orion@nwra.com> - 6.1.0-1
- Update to 6.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-2
- Subpackage python2-traitsui has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 20 2018 Orion Poplawski <orion@nwra.com> - 6.0.0-1
- Update to 6.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.1.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.0-1
- Update to 5.1.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 5.0.0-2
- Add python3 subpackage

* Thu Nov 5 2015 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-1
- Update to 5.0.0

* Thu Nov 5 2015 Orion Poplawski <orion@cora.nwra.com> - 4.5.1-1
- Update to 4.5.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-1
- Update to 4.4.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 1 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-2
- Split documentation in to doc sub-package
- Add requires numpy
- More explicit file listing
- Drop sitelib macro

* Tue Apr 23 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Update to 4.3.0

* Tue Dec 18 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-5
- Change BR to python2-devel

* Wed Dec 5 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-4
- Add upstream patch to move to UTF-8 and remove hidden directories

* Sat Oct 6 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-3
- Add BR python-setuptools

* Sat Oct 6 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-2
- Drop CFLAGS comment
- Drop buildroot cleanup
- Add docs and examples to %%doc

* Wed Jun 6 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-1
- Initial package
