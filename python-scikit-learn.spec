%bcond_without check

%global srcname scikit-learn

%global _description %{expand: 
Scikit-learn integrates machine learning algorithms in the tightly-knit 
scientific Python world, building upon numpy, scipy, and matplotlib. 
As a machine-learning module, it provides versatile tools for data mining 
and analysis in any field of science and engineering. It strives to be 
simple and efficient, accessible to everybody, and reusable 
in various contexts.}

Name: python-scikit-learn
Version: 1.3.0
Release: 1%{?dist}
Summary: Machine learning in Python
# sklearn/externals/_arff.py is MIT
# sklearn/src/liblinear is BSD
# sklearn/src/libsvm is BSD
License: BSD and MIT

URL: http://scikit-learn.org/
Source0: %{pypi_source}

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: %{py3_dist Cython}
BuildRequires: %{py3_dist numpy} >= 1.17.3
BuildRequires: %{py3_dist scipy} >= 1.5.0
# Testing
%if %{with check}
BuildRequires: python3-pytest >= 7.1.2
BuildRequires: %{py3_dist joblib} >= 1.1.1
BuildRequires: python3-threadpoolctl >= 2.0.0
%endif

%{?python_provide:%python_provide python3-sklearn}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
# check collection crashes in armv7hl
# https://koji.fedoraproject.org/koji/taskinfo?taskID=74494216
%ifarch armv7hl
%py3_check_import sklearn
%else
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}%{python3_sitearch}
  pytest -v -x \
  --deselect "sklearn/datasets/tests/test_openml.py::test_fetch_openml_verify_checksum[True-liac-arff]" \
  --deselect "sklearn/datasets/tests/test_openml.py::test_fetch_openml_verify_checksum[False-liac-arff]" \
  --deselect "sklearn/datasets/tests/test_openml.py::test_fetch_openml_verify_checksum[True-pandas]" \
  --deselect "sklearn/datasets/tests/test_openml.py::test_fetch_openml_verify_checksum[False-pandas]" \
%ifarch ppc64le
  --deselect "neural_network/tests/test_mlp.py::test_mlp_regressor_dtypes_casting" \
%endif
  sklearn 
popd
%endif
%py3_check_import sklearn
%endif

%files -n python3-%{srcname}
%doc examples/
%license COPYING sklearn/svm/src/liblinear/COPYRIGHT
%{python3_sitearch}/sklearn
%{python3_sitearch}/scikit_learn-*.egg-info

%changelog
* Sat Jul 08 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 1.3.0-1
- New upstream source (1.3.0)

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.12

* Tue May 02 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 1.2.2-1
- New upstream source (1.2.2)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1.2-1
- New upstream source (1.1.2)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul  3 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-4
- Kill failing tests on ppc64le for now

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 1.0.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.2-1
- New upstream source (1.0.2)

* Wed Oct 06 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0-1
- New upstream source (1.0)

* Wed Aug 25 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.24.2-2
- Fix FTBFS (#1987890)
- Skip tests in armv7hl, collection causes core dumpep

* Mon Aug 23 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.24.2-1
- New upstream source (0.24.2)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.24.1-5
- Enabled testing 

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.24.1-4
- Rebuilt for Python 3.10

* Tue Feb 16 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.24.1-3
- New upstream source (0.24.1)
- Disable testing (too long)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.24.0-1
- New upstream source (0.24.0)

* Wed Aug 26 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.23.2-1
- New upstream source (0.23.2)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.23.1-1
- New upstream source (0.23.1)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-3
- Rebuilt for Python 3.9

* Sun May 24 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.23.0-2
- Add missing dependency on threadpoolctl (bz #1836744)

* Sun May 17 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.23.0-1
- New upstream source (0.23.0)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.22.1
- New upstream source (0.22.1)

* Sat Jan 11 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.22-1
- New upstream source (0.22)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.21.3-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.21.3-1
- New upstream source (0.21.3)
- Add a patch to fix detection of openmp

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.19.1-6
- Subpackage python2-scikit-learn has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jul 17 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.19.1-5
- BuildRequires: gcc gcc-c++

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.19.1-3
- Rebuilt for Python 3.7
- Recythonize the .c/.cpp files to fix FTBFS on Python 3.7
- Use python2-Cython, not Cython

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 03 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.19.1-1
- New upstream (0.19.1)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.18.1-1
- New upstream (0.18.1)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.18-3
- Rebuild for Python 3.6

* Sun Nov  6 2016 Orion Poplawski <orion@cora.nwra.com> - 0.18-2
- Rebuild for ppc64

* Thu Oct 27 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.18-1
- New upstream (0.18)
- Updatd patch blas-name
- Removed patch sklearn-np11 (already in upstream)

* Sat Oct 15 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 0.17.1-6
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 30 2016 Björn Esser <fedora@besser82.io> - 0.17.1-4
- add Provides for python(2|3)-sklearn

* Wed Mar 30 2016 Björn Esser <fedora@besser82.io> - 0.17.1-3
- add proper Provides and Obsoletes

* Wed Mar 30 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.17.1-2.1
- Skip tests for the moment

* Tue Mar 29 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.17.1-2
- New upstream (0.17.1)
- Provide python2-scikit-learn
- Add patch for numpy1.11
- New style macros

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.17-1
- Update to latest version
- Force linking to atlas

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.1-1
- New upstream (0.16.1), bugfix

* Thu Apr 09 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.0-2
- Readd provides filter
- Increase joblib minimum version
- New upstream (0.16.0)

* Tue Sep 16 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-2
- Remove patch for broken test (fixed in scipy 0.14.1)

* Tue Sep 16 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-1
- New upstream (0.15.2), bugfix

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.1-1
- New upstream (0.15.1), bugfix

* Tue Jul 15 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.0-1
- New upstream (0.15.0), final

* Wed Jul 02 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.0-0.5.b2
- New upstream (0.15.0b2), beta release

* Tue Jun 24 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.0-0.4.b1
- Add COPYING to docs
- Spec cleanup

* Mon Jun 23 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.0-0.3.b1
- New upstream (0.15.0b1), beta release
- Add tarball
- Disable tests for the moment

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Jun 02 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.1-7
- Rerun Cython3 on broken files
- Disable tests for the moment

* Thu May 29 2014 Björn Esser <bjoern.esser@gmail.com> - 0.14.1-6
- rebuilt for Python3 3.4

* Wed Jan 15 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.1-5
- Enable checks
- Regenerate C files from patched cython code
- Use python2 style macros

* Sat Oct 26 2013 Björn Esser <bjoern.esser@gmail.com> - 0.14.1-4
- rebuilt for atlas-3.10.1-7

* Mon Sep 16 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.1-3
- Unbundle six

* Wed Sep 11 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.1-2
- Update cblas patch
- Update EVR to build with new numpy (1.8.0-0.3b2)

* Wed Aug 28 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.1-1
- New upstream source (0.14.1)
- Add python3 support
- Unbundle joblib and cblas

* Wed Jul 10 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.13.1-3
- Reorder buildrequires and requires
- Dropped doc, it does not build

* Tue Jun 25 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.13.1-2
- Changed package name
- Tests do not need recompile

* Thu Apr 18 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 0.13.1-1
- Initial spec file
