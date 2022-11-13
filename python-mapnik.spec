%global srcname mapnik

%global commit 7da019cf9eb12af8f8aa88b7d75789dfcd1e901b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global testcommit dd0c41c3f9f5dc98291a727af00bb42734d2a8c0
%global visualcommit 1f20cf257f35224d3c139a6015b1cf70814b0d24

%global mapnik_version 3.0.23

Name:           python-%{srcname}
Version:        3.0.23
Release:        20.20200224git%{shortcommit}%{?dist}
Summary:        Python bindings for Mapnik

License:        LGPL-2.1-only
URL:            https://github.com/mapnik/python-mapnik
Source0:        https://github.com/mapnik/python-mapnik/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        https://github.com/mapnik/test-data/archive/%{testcommit}/test-data-%{testcommit}.tar.gz
Source2:        https://github.com/mapnik/test-data-visual/archive/%{visualcommit}/test-data-visual-%{visualcommit}.tar.gz
# Stop setup.py trying to fiddle with compiler flags
Patch0:         python-mapnik-flags.patch
# Allow more variation in comparisons
Patch1:         python-mapnik-precision.patch
# Remove test that relies on WKT data missing from Fedora's gdal
Patch2:         python-mapnik-gdal.patch
# Disable some failing tests
Patch3:         python-mapnik-compositing.patch
# https://github.com/mapnik/python-mapnik/commit/708290aff1ecbc2de080cab5588019caea1a02e1
Patch4:         python-mapnik-buffer.patch
# Update for new proj API support
Patch5:         python-mapnik-proj.patch

# Exclude big endian architectures as mapnik does not support them
# https://github.com/mapnik/mapnik/issues/2313
# https://bugzilla.redhat.com/show_bug.cgi?id=1395208
ExcludeArch:    ppc ppc64 s390 s390x

BuildRequires:  gcc-c++
BuildRequires:  sqlite-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-PyPDF2

BuildRequires:  mapnik-devel >= %{mapnik_version}
BuildRequires:  mapnik-static >= %{mapnik_version}
BuildRequires:  mapnik-utils >= %{mapnik_version}

BuildRequires:  git-core
BuildRequires:  boost-devel boost-python3-devel
BuildRequires:  python3-cairo-devel
BuildRequires:  postgresql-test-rpm-macros postgis

%description
%{summary}.


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -p 1 -n %{name}-%{commit}
tar --directory=test/data --strip-components=1 --gunzip --extract --file=%{SOURCE1} 
tar --directory=test/data-visual --strip-components=1 --gunzip --extract --file=%{SOURCE2} 


%build
export PYCAIRO=true
export BOOST_PYTHON_LIB=boost_python%{python3_version_nodots}
%py3_build


%install
export BOOST_PYTHON_LIB=boost_python%{python3_version_nodots}
%py3_install


%check
# start a postgres instance for the tests to use
PGTESTS_LOCALE="C.UTF-8" %postgresql_tests_run
createdb template_postgis
psql -c "CREATE EXTENSION postgis" template_postgis
# run the tests
rm test/data/broken_maps/duplicate_stylename.xml
rm test/data/good_maps/layer_scale_denominator.xml
rm test/python_tests/pdf_printing_test.py
rm test/python_tests/projection_test.py
PGHOST="$PWD" LANG="C.UTF-8" BOOST_PYTHON_LIB=boost_python%{python3_version_nodots} %{__python3} setup.py test


%files -n python3-%{srcname}
%doc README.md AUTHORS.md CHANGELOG.md CONTRIBUTING.md
%license COPYING
%{python3_sitearch}/*


%changelog
* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.0.23-20.20200224git7da019c
- Rebuilt for ICU 71.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.23-19.20200224git7da019c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.23-18.20200224git7da019c
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 3.0.23-17.20200224git7da019c
- Rebuilt for Boost 1.78

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.23-16.20200224git7da019c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 3.0.23-15.20200224git7da019c
- Rebuilt for Boost 1.76

* Thu Jul 29 2021 Tom Hughes <tom@compton.nu> - 3.0.23-13.20200224git%(c=%{commit}; echo ${c:0:7})%{?dist}
- Add upstream patch to support new proj API

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.23-13.20200224git7da019c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.23-12.20200224git7da019c
- Rebuilt for Python 3.10

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 3.0.23-11.20200224git7da019c
- Rebuild for ICU 69

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.23-10.20200224git7da019c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.0.23-9.20200224git7da019c
- Rebuilt for Boost 1.75

* Sat Jan  9 2021 Tom Hughes <tom@compton.nu> - 3.0.23-8.20200224git7da019c
- Rebuild for mapnik 3.1.0

* Mon Nov 23 2020 Tom Hughes <tom@compton.nu> - 3.0.23-7.20200224git7da019c
- Add patch for python 3.10 compatibility

* Mon Oct  5 2020 Tom Hughes <tom@compton.nu> - 3.0.23-6.20200224git7da019c
- Require setuptools

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.23-5.20200224git7da019c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun  2 2020 Tom Hughes <tom@compton.nu> - 3.0.23-4.20200224git7da019c
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.23-3.20200224git7da019c
- Rebuilt for Python 3.9

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 3.0.23-2.20200224git7da019c
- Rebuild for ICU 67

* Tue Mar  3 2020 Tom Hughes <tom@compton.nu> - 3.0.23-1.20200224git7da019c
- Update to new upstream snapshot

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-50.20180723git588fc90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-49.20180723git588fc90
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-48.20180723git588fc90
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-47.20180723git588fc90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Tom Hughes <tom@compton.nu> - 0.1-46.20180723git588fc90
- Update to new shapshot
- Fix various python 3.8 warnings

* Tue Feb  5 2019 Tom Hughes <tom@compton.nu> - 0.1-45.20180411gitfe47aa1
- Rebuilt for proj 5

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-44.20180411gitfe47aa1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Tom Hughes <tom@compton.nu> - 0.1-43.20180411gitfe47aa1
- Rebuilt for Boost 1.69

* Tue Nov  6 2018 Tom Hughes <tom@compton.nu> - 0.1-42.20180411gitfe47aa1
- Replace en_US.UTF-8 with C.UTF-8

* Mon Sep 17 2018 Tom Hughes <tom@compton.nu> - 0.1-41.20180411gitfe47aa1
- Drop python2 subpackage

* Tue Aug 28 2018 Tom Hughes <tom@compton.nu> - 0.1-40.20180411gitfe47aa1
- Use new postgres test macro

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-39.20180411gitfe47aa1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0.1-38.20180411gitfe47aa1
- Rebuild for ICU 62

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-37.20180411gitfe47aa1
- Rebuilt for Python 3.7

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0.1-36.20180411gitfe47aa1
- Rebuild for ICU 61.1

* Sat Apr 28 2018 Tom Hughes <tom@compton.nu> - 0.1-35.20180411gitfe47aa1
- Update to new snapshot

* Fri Apr 27 2018 Tom Hughes <tom@compton.nu> - 0.1-34.20170614git1635afe
- Update boost-python and pycairo dependencies

* Sun Apr 22 2018 Tom Hughes <tom@compton.nu> - 0.1-33.20170614git1635afe
- Rebuild against mapnik 3.0.20

* Sun Apr 22 2018 Tom Hughes <tom@compton.nu> - 0.1-32.20170614git1635afe
- Rebuild against mapnik 3.0.20

* Tue Mar  6 2018 Tom Hughes <tom@compton.nu> - 0.1-31.20170614git1635afe
- Rebuild against mapnik 3.0.19

* Sun Feb 18 2018 Tom Hughes <tom@compton.nu> - 0.1-30.20170614git1635afe
- Require gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-29.20170614git1635afe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Tom Hughes <tom@compton.nu> - 0.1-28.20170614git1635afe
- Rebuild against mapnik 3.0.18

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.1-27.20170614git1635afe
- Rebuilt for Boost 1.66

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 0.1-26.20170614git1635afe
- Rebuild for ICU 60.1

* Thu Nov 30 2017 Tom Hughes <tom@compton.nu> - 0.1-25.20170614git1635afe
- Rebuild against mapnik 3.0.17

* Tue Nov 21 2017 Tom Hughes <tom@compton.nu> - 0.1-24.20170614git1635afe
- Rebuild against mapnik 3.0.16

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.1-23.20170614git1635afe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22.20170614git1635afe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21.20170614git1635afe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.1-20.20170614git1635afe
- Rebuilt for Boost 1.64

* Fri Jun 16 2017 Tom Hughes <tom@compton.nu> - 0.1-19.20170614git1635afe
- Rebuild against mapnik 3.0.15

* Wed Jun 14 2017 Tom Hughes <tom@compton.nu> - 0.1-18.20170614git1635afe
- Update to new snapshot
- Rebuild against mapnik 3.0.14

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-17.20170214git8139e5c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu May  4 2017 Tom Hughes <tom@compton.nu> - 0.1-16.20170214git8139e5c
- Rebuild for ARM ABI fix

* Tue Feb 14 2017 Tom Hughes <tom@compton.nu> - 0.1-15.20170214git8139e5c
- Update to new snapshot
- Rebuild against current mapnik

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14.20160909git541fd96
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 0.1-13.20160909git541fd96
- Rebuild (libwebp)

* Wed Jan 25 2017 Tom Hughes <tom@compton.nu> - 0.1-12.20160909git541fd96
- Rebuild for proj 4.9.3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-11.20160909git541fd96
- Rebuild for Python 3.6

* Wed Nov 16 2016 Tom Hughes <tom@compton.nu> - 0.1-10.20160909git541fd96
- Exclude big endian architectures as mapnik does not support them

* Fri Sep  9 2016 Tom Hughes <tom@compton.nu> - 0.1-9.20160909git541fd96
- Update to new snapshot
- Rebuild against current mapnik

* Tue Jul 26 2016 Tom Hughes <tom@compton.nu> - 0.1-8.20160202git1cb6851
- Update to new snapshot
- Rebuild against current mapnik

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7.20151209gitdb7c1fd
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6.20151209gitdb7c1fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Tom Hughes <tom@compton.nu> - 0.1-5.20151209gitdb7c1fd
- Update to new snapshot
- Patch some boost 1.60.0 issues

* Fri Jan 22 2016 Tom Hughes <tom@compton.nu> - 0.1-5.20151209gitf81d5f8
- Rebuild for boost 1.60.0

* Wed Dec  9 2015 Tom Hughes <tom@compton.nu> - 0.1-4.20151209gitf81d5f8
- Update to new snapshot with license fix
- Bump epoch on mapnik-python provide
- Patch out setting of rpath
- Update to latest test data

* Sun Dec  6 2015 Tom Hughes <tom@compton.nu> - 0.1-3.20151127gitfae6388
- Update to new upstream snapshot

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 0.1-2.20151125gitff364e1
- Provide a postgres instance for the tests
- Enable cairo support

* Mon Nov 30 2015 Tom Hughes <tom@compton.nu> - 0.1-1.20151125gitff364e1
- Rebuild against mapnik 3.0.9

* Wed Nov 25 2015 Tom Hughes <tom@compton.nu> - 0-0.1.20151125gitff364e1
- Initial build
