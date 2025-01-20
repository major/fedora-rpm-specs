%bcond_without check

%global srcname astropy

Name: python-%{srcname}
Version: 7.0.0
Release: 2%{?dist}
Summary: A Community Python Library for Astronomy
# File _strptime.py is under Python-2.0.1
# jquery is MIT
License: BSD-3-Clause AND CFITSIO AND Python-2.0.1 AND MIT

URL: http://astropy.org
Source: %{pypi_source %{srcname}}
Source: astropy-README.dist
# To build with gcc 14
Patch: python-astropy-313tests.patch
Patch: python-astropy-system-configobj.patch
Patch: python-astropy-system-ply.patch

# Backport upstream patch for Numpy >=2.2
Patch: effccc8.patch

BuildRequires: gcc
BuildRequires: expat-devel
BuildRequires: wcslib-devel >= 8.2.2
BuildRequires: python3-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global _description %{expand:
The Astropy project is a common effort to develop a single core package
for Astronomy. Major packages such as PyFITS, PyWCS, vo, and asciitable
already merged in, and many more components being worked on. In
particular, we are developing imaging, photometric, and spectroscopic
functionality, as well as frameworks for cosmology, unit handling, and
coordinate transformations.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
# Unbundled
BuildRequires: %{py3_dist configobj}
BuildRequires: %{py3_dist ply}
Requires: %{py3_dist configobj}
Requires: %{py3_dist ply}
# Bundled
Provides: bundled(cfitsio) = 4.5.0
Provides: bundled(jquery) = 3.60
Provides: bundled(wcslib) = 8.3

# Drop doc subpackage, is empty 

%description -n python3-%{srcname}
%_description

Provides: python3-%{srcname}-doc = %{version}-%{release}
Obsoletes: python3-%{srcname}-doc < 6.0.1-1

%package -n %{srcname}-tools
Summary: Astropy utility tools
BuildArch: noarch
Requires: python3-%{srcname} = %{version}-%{release} 

%description -n %{srcname}-tools
Utilities provided by Astropy.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -rf astropy/extern/configobj
rm -rf astropy/extern/ply
rm -rf cextern/expat

# Apparently, --current-env doesn't like {list_dependencies_command}
sed -i 's/{list_dependencies_command}/python -m pip freeze --all/g' tox.ini

export ASTROPY_USE_SYSTEM_ALL=1
%generate_buildrequires
%if %{with check}
%pyproject_buildrequires -t -x test
%else
%pyproject_buildrequires 
%endif

%build
export ASTROPY_USE_SYSTEM_ALL=1
# Search for headers in subdirs
export CPATH="/usr/include/wcslib"
%pyproject_wheel

%install
export ASTROPY_USE_SYSTEM_ALL=1
# Search for headers in subdirs
export CPATH="/usr/include/wcslib"
%pyproject_install

%pyproject_save_files -l astropy

%check
%if %{with check}
# some tests are broken with Numpy 2.x
# see https://github.com/astropy/astropy/issues/17124
# upstream commit effccc8 doesn't fix that entirely
pytest_args=(
 --verbosity=0
 -k "not (test_coverage or test_basic_testing_completeness or test_all_included)"
# Some doctest are failing because of different output in big/little endian
%ifarch s390x
 --ignore ../../docs/io/fits/index.rst
 --ignore ../../docs/io/fits/usage/image.rst
 --ignore ../../docs/io/fits/usage/unfamiliar.rst
%endif
)

%tox -- --parallel 0 -- "${pytest_args[@]}"

%else
%pyproject_check_import -t
%endif


%files -n %{srcname}-tools
%{_bindir}/*

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst 

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 24 2024 Mattia Verga <mattia.verga@proton.me> - 7.0.0-1
- Update to 7.0.0 for Numpy 2.x

* Fri Nov 15 2024 Orion Poplawski <orion@nwra.com> - 6.1.6-1
- Update to 6.1.6

* Thu Aug 08 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 6.0.1-5
- Write the test macro correctly

* Sun Aug 04 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 6.0.1-4
- Block failed test in s309x

* Wed Jul 31 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 6.0.1-3
- Fix python 3.13 incompatibility in tests

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 6.0.1-1
- New upstream source 6.0.1
- Drop doc subpackge, it was empty anyway
- Drop i686

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 5.3.2-10
- Bootstrap for Python 3.13

* Wed Mar 06 2024 Sandro <devel@penguinpee.nl> - 5.3.2-9
- Drop dependency on pandas for i686
- Make doc subpackage noarch

* Wed Feb 21 2024 Songsong Zhang <U2FsdGVkX1@gmail.com> - 5.3.2-8
- Add riscv64 support

* Sat Feb 03 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 5.3.2-7
- Add patch to fix FTBS

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 14 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 5.3.2-4
- Add patch to fix test error

* Tue Jan 09 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 5.3.2-3
- Rebuilt with wcslib 8

* Mon Aug 28 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 5.3.2-2
- New upstream source 5.3.2
- SPDX migration, license is BSD-3-Clause AND CFITSIO
- Include the sources

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 5.3.1-2
- Rebuilt for Python 3.12

* Fri Jul 07 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 5.3.1-1
- New upstream source 5.3.1
- cfitsio is not bundled, only some files need for FITS decompression

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.2.2-2
- Bootstrap for Python 3.12

* Wed Mar 29 2023 Christian Dersch <lupinix@fedoraproject.org> - 5.2.2-1
- new version
- enable astropy/visualization/wcsaxes/tests/test_misc.py::test_contour_empty (fixed upstream)

* Tue Mar 28 2023 Christian Dersch <lupinix@fedoraproject.org> - 5.2.1-1
- new version, required for numpy 1.24 compat
- reenable some tests
- disable test astropy/visualization/wcsaxes/tests/test_misc.py::test_contour_empty

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 5.2-2
- Skip two tests in aarch64

* Fri Jan 06 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 5.2-1
- New upstream source 5.2

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 5.1-4
- Rebuild for cfitsio 4.2

* Thu Aug 25 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 5.1-3
- New upstream source 5.1
- Deselect some tests failling with Python 3.11 (https://github.com/astropy/astropy/issues/13522)
- Deselect test failling in i686

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Python Maint <python-maint@redhat.com> - 5.0.4-3
- Rebuilt for Python 3.11

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 5.0.4-2
- Bootstrap for Python 3.11

* Thu Mar 31 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 5.0.4-1
- Update to 5.0.4 (#2019531)

* Wed Feb 16 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 5.0.3-1
- New upstream source 5.0.3
- Add pytest-mpl for testing

* Wed Feb 16 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 5.0.1-1
- New upstream source 5.0.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 26 2021 Christian dersch <lupinix@fedoraproject.org> - 5.0-1
- new version

* Fri Sep 10 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 4.3.1-1
- New upstream source 4.3.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 4.2.1-3
- Disable test broken in 3.10 (gh #11821)
- Disable broken test in s390x

* Fri Jun 04 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 4.2.1-1
- New upstream source 4.2.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.2-4
- Rebuilt for Python 3.10

* Tue Feb 16 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 4.2-3
- Exclude test failling in armv7hl

* Tue Feb 16 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 4.2-2
- New upstream source 4.2
- Cleanup specfile

* Tue Feb 02 2021 Christian Dersch <lupinix@mailbox.org> - 4.0.1.post1-6
- Rebuilt for libcfitsio.so.7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.post1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.post1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.1.post1-3
- Rebuilt for Python 3.9

* Sat May 23 2020 Orion Poplawski <orion@nwra.com> - 4.0.1.post1-2
- Drop old pyfits-tools obsoletes/provides
- Build with system wcslib on EL8

* Thu May 07 2020 Orion Poplawski <orion@nwra.com> - 4.0.1.post1-1
- Update to 4.0.1.post1

* Fri Mar 20 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 4.0-3
- Rebuildt for wcslib 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 4.0-1
- New upstream version (4.0)

* Thu Nov 07 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.2.3-1
- New upstream version (3.2.3), fixes problem with IERS data download

* Wed Oct 09 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.2.2-1
- New upstream version (3.2.2)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.2.1-1
- New upstream version (3.2.1)
- Remove patches included upsteam

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Christian Dersch <lupinix@fedoraproject.org> - 3.1.2-2
- Imported upstream fix for PyYAML 5.x

* Mon Mar 04 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 3.1.2-1
- New version (3.1.2)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 21 2018 Christian Dersch <lupinix@mailbox.org> - 3.0.5-1
- new version

* Mon Aug 13 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-2
- Enable s390x (#1610996)

* Fri Aug 03 2018 Christian Dersch <lupinix.fedora@gmail.com> - 3.0.4-1
- new version (3.0.4)
- reenable tests
- ExcludeArch s390x until #1610996 is fixed

* Sun Jul 15 2018 Christian Dersch <lupinix@fedoraproject.org> - 3.0.3-5
- BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Christian Dersch <lupinix@fedoraproject.org> - 3.0.3-3
- Disable tests until we have the pyyaml fix
  https://github.com/yaml/pyyaml/pull/181

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.3-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 3.0.3-1
- New release (3.0.3)

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 3.0.2-1
- new version

* Sat Mar 17 2018 Christian Dersch <lupinix@mailbox.org> - 3.0.1-1
- new version
- cleaned up excluded tests, adapted patch from Debian for known failures
- removed Python 2 bits (in new package python2-astropy), astropy moved to
  Python 3 only

* Wed Mar 14 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.5-1
- new version
- enabled fixed tests

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.4-3
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.4-2
- Provide and Obsolete python-wcsaxes, which has been merged into astropy

* Tue Feb 13 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.4-1
- update to bugfix release 2.0.4
- fixes FTBFS on rawhide (due to fixes for newer numpy etc.)
- disabled tests on s390x as they hang sometimes (same as with scipy)
- removed python-astropy-fix-hdf5-test.patch (applied upstream)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 09 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 2.0.2-2
- Use system erfa

* Sun Oct 08 2017 Christian Dersch <lupinix@mailbox.org> - 2.0.2-1
- new version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Christian Dersch <lupinix@mailbox.org> - 1.3.3-1
- new version

* Sun Apr 02 2017 Christian Dersch <lupinix@mailbox.org> - 1.3.2-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 5 2017 Orion Poplawski <orion@cora.nwra.com> - 1.3-1
- Update to 1.3

* Wed Dec 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3-0.1.rc1
- Update to 1.3rc1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-6
- Rebuild for Python 3.6

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-5
- Use bundled erfa and wcslib where necessary (bug #1396601)
- Specify scipy version requirements
- Use cairo matplotlib backend due to ppc64 segfault
- Add BR on pandas for tests

* Sun Nov 06 2016 Björn Esser <fedora@besser82.io> - 1.2.1-4
- Rebuilt for ppc64

* Fri Sep 30 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.2.1-3
- Fix wrong provides of python3-astropy in python2-astropy (bz #1380135)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.2.1-1
- New upstream (1.2.1)

* Thu Apr 14 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1.2-1
- New upstream (1.1.2)
- Uses wcslib 5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Orion Poplawski <orion@cora.nwra.com> - 1.1.1-2
- Modernize spec
- Prepare for python3 in EPEL

* Sun Jan 10 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1.1-1
- New upstream (1.1.1)

* Wed Jan 06 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1-1.post2
- New upstream (1.1.post2)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.6-2
- Enabled again tests that failed with numpy 1.10

* Wed Oct 28 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.6-1
- New upstream (1.0.6), with better support of numpy 1.10

* Fri Oct 09 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.5-2
- Fixes test problem https://github.com/astropy/astropy/issues/4226

* Tue Oct 06 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.5-1
- New upstream (1.0.5)

* Mon Sep 14 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.4-2
- Disable some tests that fail with numpy 1.10

* Thu Sep 03 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.4-1
- New upstream (1.0.4)

* Tue Jun 30 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.3-4
- Reenable tests
- Handle changes regarding python3 and pyfits-tools in fedora >= 22

* Mon Jun 29 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.3-3
- Obsolete pyfits-tools (fixes bz #1236562)
- astropy-tools requires python3

* Tue Jun 16 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.3-1
- New upstream (1.0.3), with 2015-06-30 leap second

* Tue Apr 21 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.2-1
- New upstream (1.0.2)

* Thu Feb 19 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0-1
- New upstream (1.0)

* Thu Jan 22 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.4-1
- New upstream (0.4.4)

* Fri Jan 16 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.3-1
- New upstream (0.4.3)

* Tue Dec 09 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.2-5
- Disable tests for the moment

* Tue Dec 09 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.2-4
- Update patch for bug 2516

* Mon Dec 08 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.2-3
- Mark problematic tests as xfail via patch

* Fri Dec 05 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.2-2
- Fix to use configobj 5
- Patches reorganized

* Thu Sep 25 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.2-1
- New upstream (0.4.2)

* Mon Sep 01 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.4.1-1
- New upstream (0.4.1)
- Unbundling patches modified
- No checks for the moment

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> - 0.3.2-5
- Rebuild for Python 3.4

* Thu May 22 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.2-4
- Build with wcslib 4.23
- Skip test, bug 2171

* Thu May 22 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.2-3
- Astropy bundles jquery
- Unbundle plpy

* Thu May 22 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.2-2
- Add missing patches

* Mon May 19 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.2-1
- New upstream (0.3.2)
- Enable checks
- Patch to fix upstream bug 2171
- Disable problematic test (upstream 2516)

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Mar 25 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.1-2
- Disable checks until https://github.com/astropy/astropy/issues/2171 is fixed
- Patch to fix https://github.com/astropy/astropy/pull/2223

* Wed Mar 05 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.1-1
- New upstream version (0.3.1)
- Remove require python(3)-matplotlib-qt4 (bug #1030396 fixed)
- Run the tests on the installed files
- Add patch to run with six 1.5.x

* Mon Jan 27 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-7
- Add missing requires python3-six

* Sat Jan 18 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-6
- Do not exclude hidden file, it breaks tests

* Thu Jan 16 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-5
- Remove split -devel subpackage, it does not make much sense

* Fri Jan 10 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-4
- Disable noarch for doc subpackages to avoid name colision

* Fri Jan 10 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-3
- Enable HDF5 version check (fixed in h5py)
- Patch for failing test with wcslib 4.20
- Require python(3)-matplotlib-qt4 due to bug #1030396

* Sun Jan 05 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-2
- Disable HDF5 version check

* Mon Nov 25 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-1
- New upstream (0.3)

* Tue Nov 19 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-0.3.rc1
- New upstream, first release candidate Testing 0.3rc1

* Wed Nov 06 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-0.2.b1
- Split utility scripts in subpackage

* Tue Nov 05 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3-0.1.b1
- Testing 0.3 (0.3b1)

* Mon Oct 28 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.5-1
- New upstream version (0.2.5)

* Tue Oct 22 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.4-4
- Split header files into devel subpackages

* Mon Oct 21 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.4-3
- Disable tests in Rawhide

* Thu Oct 10 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.4-3
- Add a patch to build with cfitsio 3.35

* Wed Oct 02 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.4-1
- Initial spec
