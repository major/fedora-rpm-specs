%if %{defined fedora}
# EL9 missing mysql-connector-python3
%bcond_without mysql_tests
# EL9 missing postgresql-test-rpm-macros
%bcond_without postgres_tests
%endif

Name:           python-peewee
Version:        3.17.8
Release:        2%{?dist}
Summary:        A simple and small ORM

License:        MIT
URL:            https://github.com/coleifer/peewee
# PyPI tarball doesn't have tests
Source:         %{url}/archive/%{version}/peewee-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  sqlite-devel

# documentation
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

# tests
BuildRequires:  python3-apsw
%if %{with mysql_tests}
BuildRequires:  mysql-connector-python3
%endif
%if %{with postgres_tests}
BuildRequires:  python3-psycopg2
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  postgresql-contrib
%endif


%global _description %{expand:
Peewee is a simple and small ORM. It has few (but expressive) concepts, making
it easy to learn and intuitive to use.}


%description %{_description}


%package -n python3-peewee
Summary:        %{summary}


%description -n python3-peewee %{_description}


%package docs
Summary:        Documentation for %{name}
Conflicts:      python3-peewee < 3.15.1-3


%description docs
Documentation for %{name}.


%prep
%autosetup -n peewee-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Test suite requires an in-place build of the compiled extensions.
# https://github.com/coleifer/peewee/blob/3.15.2/.github/workflows/tests.yaml#L49
%{set_build_flags}
%{python3} %{py_setup} %{?py_setup_args} build_ext --inplace

# Build the documentation
sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files peewee playhouse pwiz
mv %{buildroot}%{_bindir}/{pwiz.py,pwiz}


%check
%if %{with postgres_tests}
export PGTESTS_LOCALE="C.UTF-8"
%postgresql_tests_run
createdb peewee_test
psql -c "CREATE EXTENSION hstore" peewee_test
%endif
%{python3} runtests.py


%files -n python3-peewee -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%{_bindir}/pwiz


%files docs
%doc html


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Viliam Krizan <vkrizan@redhat.com> - 3.17.8-1
- Update to 3.17.8 (#2296140)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Viliam Krizan <vkrizan@redhat.com> - 3.17.5-1
- Update to 3.17.5 (#2275289)

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.17.1-2
- Rebuilt for Python 3.13

* Fri Feb 16 2024 Viliam Krizan <vkrizan@redhat.com> - 3.17.1-1
- Update to 3.17.1 (#2263094)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 25 2023 Viliam Krizan <vkrizan@redhat.com> - 3.17.0-1
- Update to 3.17.0 (#2244151)

* Tue Aug 15 2023 Viliam Krizan <vkrizan@redhat.com> - 3.16.3-1
- new version

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 3.16.2-2
- Rebuilt for Python 3.12 (fix RHBZ#2220402)

* Tue Jun 27 2023 Viliam Krizan <vkrizan@redhat.com> - 3.16.2-1
- Update to 3.16.2 (#2187944)

* Tue Apr 04 2023 Viliam Krizan <vkrizan@redhat.com> - 3.16.0-2
- Add patch to fix sqlite timeouts in test runs on the build system

* Mon Apr 03 2023 Viliam Krizan <vkrizan@redhat.com> - 3.16.0-1
- new version rhbz#2174257

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Viliam Krizan <vkrizan@redhat.com> - 3.15.4-1
- Update to 3.15.4 (#2142291)

* Fri Sep 23 2022 Carl George <carl@george.computer> - 3.15.3-1
- Latest upstream, resolves rhbz#2129202

* Wed Sep 21 2022 Carl George <carl@george.computer> - 3.15.2-1
- Latest upstream, resolves rhbz#2121865
- Convert to pyproject macros
- Move docs to separate subpackage
- Re-enable tests on ppc64le
- Enable mysql tests
- Enable postgresql tests
- Enable sqlite extension tests

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Viliam Krizan <vkrizan@redhat.com> - 3.15.1-1
- Update to 3.15.1 (#2098350)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.14.10-2
- Rebuilt for Python 3.11

* Tue Mar 08 2022 Viliam Krizan <vkrizan@redhat.com> - 3.14.10-1
- Update to 3.14.10 (#2054830)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 03 2021 Viliam Krizan <vkrizan@redhat.com> - 3.14.8-1
- Update to 3.14.8 (#2017730)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.14.4-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Charalampos Stratakis <cstratak@redhat.com> - 3.14.4-1
- Update to 3.14.4 (#1941088)

* Fri Mar 19 2021 Charalampos Stratakis <cstratak@redhat.com> - 3.14.3-1
- Update to 3.14.3 (#1935568)

* Fri Feb 19 2021 Viliam Krizan <vkrizan@redhat.com> - 3.14.1-1
- Update to 3.14.1 (#1926031)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 Viliam Krizan <vkrizan@redhat.com> - 3.14.0-1
- Update to 3.14.0 (#1895638)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Viliam Krizan <vkrizan@redhat.com> - 3.13.3-3
- Replaced Python version globs with macros to support 3.10

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.13.3-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Viliam Krizan <vkrizan@redhat.com> - 3.13.3-1
- Update to 3.13.2 (#1827517)

* Fri Apr 03 2020 Viliam Krizan <vkrizan@redhat.com> - 3.13.2-1
- Update to 3.13.2 (#1818146)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Viliam Krizan <vkrizan@redhat.com> - 3.13.1-1
- Update to 3.13.1 (#1776044)

* Fri Sep 27 2019 Viliam Krizan <vkrizan@redhat.com> - 3.11.2-1
- Update to 3.11.2 (#1742474)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.9.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Viliam Krizan <vkrizan@redhat.com> - 3.9.6-1
- Update to 3.9.6 (#1703665)

* Fri Apr 26 2019 Viliam Krizan <vkrizan@redhat.com> - 3.9.4-1
- Update to 3.9.4 (#1692015)

* Mon Mar 11 2019 Viliam Krizan <vkrizan@redhat.com> - 3.9.2-1
- Update to 3.9.2 (#1685885)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Viliam Krizan <vkrizan@redhat.com> - 3.7.1-1
- Update to 3.7.1 (#1539964)

* Fri Oct 05 2018 Viliam Krizan <vkrizan@redhat.com> - 2.10.2-8
- Removal of python2 subpackage as part of
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
  (RHBZ #1634869)

* Mon Jul 30 2018 Viliam Krizan <vkrizan@redhat.com> - 2.10.2-7
- skip check for PPC architecture (#1606807)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Viliam Krizan <vkrizan@redhat.com> - 2.10.2-5
- fix StopIteration raises for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.10.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Lumír Balhar <lbalhar@redhat.com> - 2.10.2-2
- Fix directory ownership

* Tue Jan 02 2018 Viliam Krizan <vkrizan@redhat.com> - 2.10.2-1
- Update to 2.10.2

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 2.10.1-4
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.10.1-1
- Update to 2.10.1 (#1448980)

* Mon Apr 10 2017 Viliam Krizan <vkrizan@redhat.com> - 2.9.2-1
- Update to 2.9.2

* Fri Mar 03 2017 Viliam Krizan <vkrizan@redhat.com> - 2.8.8-1
- Update to 2.8.8

* Tue Feb 07 2017 Viliam Krizan <vkrizan@redhat.com> - 2.8.5-2
- Backport upstream fix to force limit and offset to be numeric

* Mon Jan 09 2017 Charalampos Stratakis <cstratak@redhat.com> - 2.8.5-1
- Update to 2.8.5

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.8.2-4
- Rebuild for Python 3.6

* Thu Nov 10 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.8.2-3
- Make pskel script install under usr/bin/
- Remove bytecompiled pwiz files

* Fri Nov 04 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.8.2-2
- Change runtime requirement from python2-simplejson to python-simplejson

* Wed Nov 02 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.8.2-1
- Update to 2.8.2
- Changed the installation directories to be arch dependent as the package
is now compiled using Cython

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.3.2-5
- Fix shebangs so python 2 is not dragged with the python 3 subpackage
- Build documentation

* Thu Jun 02 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.3.2-4
- Provide Python 3 subpackage
- Move binaries to Python 3 subpackage
- Modernize SPEC

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 29 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.3.2-1
- Update to 2.3.2

* Wed Aug 27 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.3.1-1
- Update to 2.3.1

* Mon Jun 09 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.2.4-1
- Update to 2.2.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Matej Stuchlik <mstuchli@redhat.com> - 2.1.7-1
- Update to 2.1.7

* Tue Aug 13 2013 Matej Stuchlik <mstuchli@redhat.com> - 2.1.4-2
- Added patch increasing timeout in concurrency test

* Wed Aug 07 2013 Matej Stuchlik <mstuchli@redhat.com> - 2.1.4-1
- Updated to 2.1.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Matej Stuchlik <mstuchli@redhat.com> - 2.0.9-2
- Review fixes

* Fri Mar 29 2013 mstuchli <mstuchli@redhat.com> - 2.0.9-1
- Initial spec
