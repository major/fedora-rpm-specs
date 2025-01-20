# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%bcond_without bootstrap

%global modname pyface

Name:           python-%{modname}
Version:        8.0.0
Release:        6%{?dist}
Summary:        Generic User Interface objects

# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file.
License:        BSD-3-Clause AND EPL-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later and LicenseRef-Fedora-Public-Domain
URL:            https://github.com/enthought/pyface
# Current release is missing files
# https://github.com/enthought/pyface/issues/98
#Source0:        http://www.enthought.com/repo/ets/pyface-%{version}.tar.gz
Source0:        https://github.com/enthought/pyface/archive/%{version}/pyface-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  glibc-langpack-en

%description
Pyface enables programmers to interact with generic UI objects, such as
an "MDI Application Window", rather than with raw UI widgets. (Pyface is
named by analogy to JFace in Java.) Traits uses Pyface to implement
views and editors for displaying and editing Traits-based objects.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel >= 3.9

%description -n python%{python3_pkgversion}-%{modname}
Pyface enables programmers to interact with generic UI objects, such as
an "MDI Application Window", rather than with raw UI widgets. (Pyface is
named by analogy to JFace in Java.) Traits uses Pyface to implement
views and editors for displaying and editing Traits-based objects.

Python 3 version.

%package doc
Summary:        Documentation for pyface

%description doc
Documentation and examples for pyface.

%package -n python%{python3_pkgversion}-%{modname}-qt
Summary:        Qt backend placeholder for pyface
# These are not picked up automatically
BuildRequires:  python%{python3_pkgversion}-pillow-qt
BuildRequires:  python%{python3_pkgversion}-pyqt6
Requires:       python%{python3_pkgversion}-%{modname} = %{version}-%{release}
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
Provides:       python%{python3_pkgversion}-%{modname}-backend

%description -n python%{python3_pkgversion}-%{modname}-qt
Qt backend placeholder for pyface.

%prep
%autosetup -p1 -n pyface-%{version}
# Tests in test_python_shell lead to core dump. We need pyface for bootstrap
# sequence of Python 3.10, thus they are temporarily disabled
# This can be removed once fixed.
# Downstream report: https://bugzilla.redhat.com/show_bug.cgi?id=1902175
rm pyface/tests/test_python_shell.py

%if %{with bootstrap}
# remove tests using traitsui
rm pyface/workbench/tests/test_workbench_window.py
rm pyface/dock/tests/test_dock_sizer.py
%endif


# file not utf-8
for f in image_LICENSE_{Eclipse,OOo}.txt
do
  iconv -f iso8859-1 -t utf-8 ${f} > ${f}.conv && mv -f ${f}.conv ${f}
done
# Use the standard lib function in 3.9+
find -name \*.py -exec sed -i -e s/importlib_resources/importlib.resources/g {} +
sed -i -e '/"importlib-[^"]*",/d' pyface/__init__.py
sed -i -e /importlib./d etstool.py


%generate_buildrequires
%pyproject_buildrequires -x pillow -x pyqt5 -x pyqt6 %{!?with_bootstrap:-x traitsui} -x wx


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyface

%check
# Needed for wx tests
export LANG=en_US.UTF-8
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONUNBUFFERED=1
# Run in a separate directory so we only see the installed package
mkdir -p test
cd test
status=0
# pyside6 is not packaged
for toolkit in null pyqt5 pyqt6 wx # pyside6
do
  # By default, fail build if tests fail
  fail=1
  # Decent default, overridded later if needed
  export QT_API=$toolkit
  case $toolkit in
    pyside6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
    # pyqt5 test fails on s390x - https://github.com/enthought/pyface/issues/1247
    # pytq5 test fails - https://github.com/enthought/pyface/issues/1255
    pyqt5) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
    # pyqt6 is failing - https://github.com/enthought/pyface/issues/1248
    # https://github.com/enthought/pyface/issues/1250
    pyqt6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
    # wx and null currently failing - https://github.com/enthought/pyface/issues/1244
    wx) export ETS_TOOLKIT="wx"; unset QT_API; export EXCLUDE_TESTS="qt"; fail=0;;
    null) export ETS_TOOLKIT="null"; unset QT_API; export EXCLUDE_TESTS="(wx|qt)"; fail=0;;
  esac
  # Adding -f can be helpful to debug missing components or other issues when the test crashes
  xvfb-run %{__python3} -Xfaulthandler -s -m unittest discover -v pyface || status=$(( $status + $fail ))
done
exit $status
 
%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%license image_LICENSE*.txt LICENSE.txt
%doc CHANGES.txt README.rst

%files doc
%doc docs/DockWindowFeature.pdf examples

%files -n python%{python3_pkgversion}-%{modname}-qt

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Orion Poplawski <orion@nwra.com> - 8.0.0-2
- Disable bootstrap

* Sun Aug 13 2023 Orion Poplawski <orion@nwra.com> - 8.0.0-2
- Enable bootstrap for Python 3.12
- Drop pyside2 tests - pyside2 is no longer maintained
- pytq5 tests are failing, ignore for now
- Fix FTBFS bz #2226292

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 11 2023 Orion Poplawski <orion@nwra.com> - 8.0.0-1
- Update to 8.0.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Orion Poplawski <orion@nwra.com> - 7.4.4-1
- Update to 7.4.4

* Sat Nov 19 2022 Orion Poplawski <orion@nwra.com> - 7.4.3-1
- Update to 7.4.3

* Mon Aug 15 2022 Orion Poplawski <orion@nwra.com> - 7.4.2-1
- Update to 7.4.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Python Maint <python-maint@redhat.com> - 7.4.1-3
- Rebuilt for Python 3.11

* Fri Jul 01 2022 Python Maint <python-maint@redhat.com> - 7.4.1-2
- Bootstrap for Python 3.11

* Sun Feb 27 2022 Orion Poplawski <orion@nwra.com> - 7.4.1-1
- Update to 7.4.1
- Rework test execution

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Orion Poplawski <orion@nwra.com> - 7.3.0-3
- Fix removal of importlib dependencies

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.3.0-2
- Rebuilt for Python 3.10

* Wed Feb 24 2021 Orion Poplawski <orion@nwra.com> - 7.3.0-1
- Update to 7.3.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Orion Poplawski <orion@nwra.com> - 7.2.0-2
- Fix importlib dependencies (bz#1919478)

* Tue Jan 19 2021 Orion Poplawski <orion@nwra.com> - 7.2.0-1
- Update to 7.2.0

* Tue Oct 20 2020 Orion Poplawski <orion@nwra.com> - 7.1.0-1
- Update to 7.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Orion Poplawski <orion@nwra.com> - 7.0.1-1
- Update to 7.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.0-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Orion Poplawski <orion@nwra.com> - 7.0.0-1
- Update to 7.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 1 2019 Orion Poplawski <orion@nwra.com> - 6.1.2-2
- Upstream patch for PyQt4 4.12.2 support (bugz#1753414)
- Switch to Qt5 for Fedora 32+

* Thu Aug 22 2019 Orion Poplawski <orion@nwra.com> - 6.1.2-1
- Update to 6.1.2
- Enable bootstrap
- Require PyQt4-webkit

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May  8 2019 Orion Poplawski <orion@nwra.com> - 6.1.0-1
- Update to 6.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Add BR/R on python3-sip for PyQt4 backend
- Allow tests to fail build again

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-2
- Subpackages python2-pyface, python2-pyface-qt, python2-pyface-wx have been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 20 2018 Orion Poplawski <orion@nwra.com> - 6.0.0-1
- Update to 6.0.0

* Sun Jul 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.1.0-10
- De-bootstrap

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
- Bootstrap

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-8
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.1.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.0-2
- Disable bootstrap

* Tue Dec 20 2016 Orion Poplawski <orion@cora.nwra.com> - 5.1.0-1
- Update to 5.1.0
- Add bootstrap, and enable it for python 3.6 build

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-11
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Robert Kuska <rkuska@redhat.com> - 5.0.0-8
- Rebuilt with traitsui

* Wed Nov 11 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Nov 9 2015 Orion Poplawski <orion@cora.nra.com> - 5.0.0-6
- Restore doc sub-package, fix doc installs

* Mon Nov 9 2015 Orion Poplawski <orion@cora.nra.com> - 5.0.0-5
- Add %%python_provides to qt/wx sub-packages
- Use sub-dirs for build

* Sat Nov 07 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 5.0.0-4
- Rebuild against traitsui

* Sat Nov 07 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 5.0.0-3
- Fix BR/Rs

* Fri Nov 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 5.0.0-2
- Return back to PyQt4
- Add python3-subpackages (only qt backend supported)
- Fix license a bit

* Thu Nov 5 2015 Orion Poplawski <orion@cora.nwra.com> - 5.0.0-1
- Update to 5.0.0
- Switch qt requires to pyside

* Thu Nov 5 2015 Orion Poplawski <orion@cora.nwra.com> - 4.5.2-1
- Update to 4.5.2
- Add BR/R on python-pygments

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Orion Poplawski <orion@cora.nwra.com> - 4.4.0-1
- Update to 4.4.0

* Mon Sep 16 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-4
- Create dummy backend packages to express dependencies

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-2
- Fix non-UTF-8 files
- Add doc sub-package
- Be more explicit with files

* Tue Apr 23 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Initial package
