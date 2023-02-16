%global with_check 1
%global pypi_name biopython
%global module %{pypi_name}

Name:             python-%{pypi_name}
Version:          1.81
Release:          1%{?dist}
Summary:          Python tools for computational molecular biology
Source0:          %{pypi_source}

# Starting from biopython-1.69, BioPython is released under the
# "Biopython License Agreement"; it looks like a MIT variant
# rhbz #1440337
License:          MIT and BSD
URL:              https://biopython.org/
BuildRequires:    gcc

%description
A set of freely available Python tools for computational molecular
biology.

%package -n python3-%{module}
Summary: Python3 tools for computational molecular biology

%py_provides python3-%{module}

BuildRequires:    python3-devel
BuildRequires:    python3dist(setuptools)
BuildRequires:    python3dist(reportlab)
BuildRequires:    python3dist(numpy)
BuildRequires:    python3-mysqlclient
BuildRequires:    python3dist(psycopg2)
BuildRequires:    python3dist(rdflib)
BuildRequires:    mysql-connector-python3
Requires:         python3dist(networkx)
Requires:         python3dist(pygraphviz)
Requires:         mysql-connector-python3
Requires:         python3dist(reportlab)
Requires:         python3-mysqlclient
Requires:         python3dist(psycopg2)
Requires:         wise2%{?_isa}
Requires:         flex%{?_isa}
Requires:         python3dist(rdflib)

%description -n python3-%{module}
A set of freely available Python3 tools for computational molecular
biology.

%package doc
Summary: PDF and HTML documentation of %{module}
BuildArch: noarch
%description doc
PDF/HTML documentation of %{module}.

%prep
%setup -qc

pushd %{module}-%{version}
# remove all execute bits from documentation and fix line endings
find Scripts -type f -exec chmod -x {} 2>/dev/null ';'
find Doc -type f -exec chmod -x {} 2>/dev/null ';'
find Doc -type f -exec sed -i 's/\r//' {} 2>/dev/null ';'

# remove execute bits from Python modules
find Bio -type f -exec chmod -x {} 2>/dev/null ';'
# remove she-bang lines in .py files to keep rpmlint happy
find Bio -type f -name "*.py" -exec sed -i '/^#![ ]*\/usr\/bin\/.*$/ d' {} 2>/dev/null ';'
popd

cp -a %{module}-%{version} python3

%build
pushd python3
%py3_build
popd

%install
pushd python3
%{__python3} setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT --install-data=%{_datadir}/python-biopython

find Scripts -name '*.py' | xargs %{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}"
popd

%if 0%{?with_check}
%check

# See https://github.com/biopython/biopython/issues/855; https://github.com/biopython/biopython/issues/1889
pushd python3/Tests
find . -name 'run_tests.py' | xargs %{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}"
find ../ -name '__init__.py' | xargs rm -f
# See https://github.com/biopython/biopython/issues/2128; https://github.com/biopython/biopython/issues/2120
# and https://bugs.python.org/issue24214
%if 0%{?python3_version_nodots} == 310
for test in `ls test_*.py | grep -v Nexus | grep -v Phylo | grep -v Tutorial | grep -v bgzf | grep -v SearchIO_blast | grep -v pairwise_aligner | grep -v SubsMat | grep -v motifs`; do
%else
for test in `ls test_*.py | grep -v Nexus | grep -v Phylo | grep -v Tutorial | grep -v bgzf | grep -v SearchIO_blast | grep -v pairwise_aligner | grep -v SubsMat`; do
%endif
echo $LANG
export PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch}
%{__python3} run_tests.py --offline -v ${test}
done
popd
%endif
# with_check

%files -n python3-%{module}
%doc python3/Scripts
%doc python3/CONTRIB.rst python3/DEPRECATED.rst python3/NEWS.rst python3/README.rst
%license python3/LICENSE.rst
%{python3_sitearch}/*egg-info
%{python3_sitearch}/Bio/
%{python3_sitearch}/BioSQL/

%files doc
%doc %{module}-%{version}/Doc
%license %{module}-%{version}/LICENSE.rst

%changelog
* Tue Feb 14 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.81-1
- Release 1.81

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 24 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.80-3
- Use python3-mysqlclient

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.80-2
- Use canonical dependency names

* Thu Nov 24 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.80-1
- Release 1.80

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.79-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.79-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.79-1
- Release 1.79

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.78-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.78-2
- Remove __init__.py before testing

* Fri Sep 04 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.78-1
- Release 1.78

* Sat Aug 22 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.77-5
- Remove flex as BR dependency (rhbz#1871093)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.77-3
- BuildRequires python3-setuptools explicitly

* Fri May 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.77-2
- Rebuilt for Python 3.9
- Remove obsolete Python3.9 patch

* Mon May 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.77-1
- Release 1.77

* Sat Feb 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.76-3
- Patched for Python-3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Luis Bazan <lbazan@fedoraprojcet.org> - 1.76-1
- Update to 1.76

* Thu Nov 07 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.75-2
- Exclude pairwise_aligner

* Thu Nov 07 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.75-1
- Update to 1.75

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.74-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.74-8
- Override bad release (https://src.fedoraproject.org/rpms/python-biopython/c/8354965f9df55504ca87e3e999d2d537dab519c7?branch=master)

* Sun Aug 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.74-7
- Override bad release (https://src.fedoraproject.org/rpms/python-biopython/c/8354965f9df55504ca87e3e999d2d537dab519c7?branch=master)

* Sun Aug 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.74-6
- Override bad release (https://src.fedoraproject.org/rpms/python-biopython/c/8354965f9df55504ca87e3e999d2d537dab519c7?branch=master)

* Sun Aug 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.74-5
- Override bad release (https://src.fedoraproject.org/rpms/python-biopython/c/8354965f9df55504ca87e3e999d2d537dab519c7?branch=master)

* Sun Aug 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.74-4
- Override bad release (https://src.fedoraproject.org/rpms/python-biopython/c/8354965f9df55504ca87e3e999d2d537dab519c7?branch=master)

* Sun Aug 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.74-3
- Override bad release (https://src.fedoraproject.org/rpms/python-biopython/c/8354965f9df55504ca87e3e999d2d537dab519c7?branch=master)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.74-2
- Rebuilt for Python 3.8
- Exclude tests using Python 3.8

* Fri Aug 16 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 1.74-1
- Update to 1.74

* Thu Aug 15 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.73-7
- Not recommended to have unversioned Obsoletes

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.73-5
- Disable failed tests on Python-3.8

* Fri Jun 14 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.73-4
- Reorganize Requires packages for EPEL7

* Thu Jun 13 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.73-3
- Rebuild for python-reportlab-3.5.23

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.73-1
- Release 1.73

* Sun Sep 30 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.72-3
- Deprecate Python2 on fedora 30+
- Prepare SPEC file for Python3-modules packaging on epel7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.72-1
- Update to 1.72

* Fri Jun 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.71-5
- Enable additional tests (upstream bug #855)
- Enable DSSP test with Python2
- Disable bgzf test with Python3

* Thu Jun 21 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.71-4
- Patched for AlignIO test failure (python-3.7 issue)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.71-3
- Rebuilt for Python 3.7

* Fri Apr 27 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.71-2
- Conform Python3 builds to coming RHEL major release

* Wed Apr 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.71-1
- Update to 1.71 (bz#1563655)

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.70-11
- Add gcc BR

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.70-10
- Fix Python2 mysql-connector packages on fedora

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.70-9
- Fix Python2 required package on rhel

* Fri Feb 16 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.70-8
- Remove %%sum macro
- Use %%py2_prefix
- Required 'numpy' on rhel (without prefix)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.70-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.70-6
- Fix dependencies

* Sun Jan 14 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.70-5
- Use versioned Python packages

* Wed Jan 03 2018 Luis Bazan <lbazan@fedoraproject.org> - 1.70-4
- Fix directory ownership

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.70-1
- Update to 1.70 (bz#1440337)

* Wed Apr 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.69-1
- Update to 1.69

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hronok <mhroncok@redhat.com> - 1.68-2
- Rebuild for Python 3.6

* Sat Aug 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.68-1
- Update to 1.68
- Drop old patch

* Wed Aug 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.67-3
- Rebuild for Python 3.5.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.67-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.67-1
- Update to 1.67

* Mon Feb 15 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.66-6
- Typo fixed

* Mon Feb 15 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.66-5
- Created a python2- package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.66-3
- SPEC file adapted to recent guidelines for Python

* Wed Dec 09 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.66-2
- Built with Python3
- Some cleanups
- Set --cflags
- Fixed MySQL dependencies in Fedora

* Tue Dec 08 2015 Luis Bazan <lbazan@fedoraproject.org> - 1.66-1
- new upstream version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 08 2015 Luis Bazan <lbazan@fedoraproject.org> - 1.65-1
- New upstream version

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Luis Bazan <lbazan@fedoraproject.org> - 1.64-1
- New Upstream Version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.60-1
- Update to latest upstream (#835434)
- Drop flex-related patch, no longer needed

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  9 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.59-1
- Update to latest upstream (1.59) (#797872)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.58-1
- Update to upstream 1.58

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.55-0.2.b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.55-0.1.b
- Update to 1.55 beta
- BuildRequires: flex-static, libraries are now split out

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri May 21 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.54-1
- Update to upstream 1.54

* Tue Apr  6 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.54-0.1.b
- Update to 1.54 beta

* Tue Dec 15 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.53-1
- Update to upstream 1.53

* Thu Oct 15 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.52-1
- Update to latest upstream (1.52)

* Tue Aug 18 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.51-1
- Update to upstream 1.51
- Drop mx {Build}Requires, no longer used upstream
- Remove Martel modules, no longer distributed upstream
- Add flex to BuildRequires, patch setup to build
  Bio.PDB.mmCIF.MMCIFlex as per upstream:
  http://bugzilla.open-bio.org/show_bug.cgi?id=2619

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  1 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.49-1
- Update to latest upstream (1.49) uses numpy and new API for psycopg2
- [Build]Requires python-numeric -> numpy 
- [Build]Requires python-psycopg -> python-psycopg2
- Remove interactive question hack, no longer needed

* Sun Nov 30 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.48-3
- Temporarily disable python-psycopg dependency until it is rebuilt
  for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.48-2
- Rebuild for Python 2.6

* Mon Sep 29 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.48-1
- Update to latest upstream (1.48)

* Fri Jul  4 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.47-1
- Update to latest upstream (1.47)

* Sun Mar 23 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.45-1
- Update to latest upstream (1.45)

* Sat Feb  9 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.44-4
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Thu Dec 13 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.44-3
- Include eggs in file list for F9+

* Sun Oct 28 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.44-2
- Drop patch to setup.py, applied upstream

* Sun Oct 28 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.44-1
- Update to latest upstream (1.44).

* Mon Aug 27 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.43-5
- Used "MIT" as short license name as the "Biopython License
  Agreement" is the same as the CMU MIT variant.

* Wed Apr 25 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.43-4
- Add wise2 Requires since the Wise biopython module uses the
  command-line behind-the-scenes.

* Tue Apr 17 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.43-3
- Use python_sitearch macro to enable x86_64 builds work.

* Mon Apr 16 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.43-2
- Fix Source0 URL as per suggestion from Parag AN on #235989.

* Mon Apr 02 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.43-1
- Initial Fedora package.


