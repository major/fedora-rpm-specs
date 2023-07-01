%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif

%if 0%{?rhel} && 0%{?rhel} == 7
%global with_python3 1
%global with_python2 1
%endif

%global pypi_name preprocess

Name: %{pypi_name}
Summary: A portable multi-language file Python2 preprocessor
Version: 2.0.0
Release: 8%{?dist}
License: MIT
URL: https://github.com/doconce/preprocess/
Source0: %{pypi_source}
BuildArch: noarch

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
%endif

%description
There are millions of templating systems out there
(most of them developed for the web).
This isn't one of those, though it does share some basics:
a markup syntax for templates that are processed to give resultant text output.
The main difference with preprocess.py is that its syntax is hidden in comments
(whatever the syntax for comments may be in the target file type)
so that the file can still have valid syntax.
A comparison with the C preprocessor is more apt.

preprocess.py is targeted at build systems that deal with many types of files.
Languages for which it works include: C++, Python, Perl, Tcl, XML, JavaScript,
CSS, IDL, TeX, Fortran, PHP, Java, Shell scripts (Bash, CSH, etc.) and C#.
Preprocess is usable both as a command line app and as a Python module.

%if 0%{?with_python2}
%package -n python2-%{name}
Summary: A portable multi-language file Python2 preprocessor

%{?python_provide:%python_provide python2-%{name}}

BuildRequires: python2-devel
BuildRequires: python2-future
BuildRequires: python2-setuptools
%if 0%{?el6}
Provides:  python2-%{name}
%endif

%description -n python2-%{name}
There are millions of templating systems out there
(most of them developed for the web).
This isn't one of those, though it does share some basics:
a markup syntax for templates that are processed to give resultant text output.
The main difference with preprocess.py is that its syntax is hidden in comments
(whatever the syntax for comments may be in the target file type)
so that the file can still have valid syntax.
A comparison with the C preprocessor is more apt.

preprocess.py is targeted at build systems that deal with many types of files.
Languages for which it works include: C++, Python, Perl, Tcl, XML, JavaScript,
CSS, IDL, TeX, Fortran, PHP, Java, Shell scripts (Bash, CSH, etc.) and C#.
Preprocess is usable both as a command line app and as a Python module.
%endif

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{name}
Summary: A portable multi-language file Python3 preprocessor

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-future
BuildRequires: python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Provides:  preprocess = 0:%{version}-%{release}
%if 0%{?fedora}
Obsoletes: python2-%{name} <= 0:1.2.3
Obsoletes: preprocess <= 0:1.2.3
%endif
%if 0%{?rhel}
Obsoletes: python34-%{name} <= 0:1.2.3
%endif

%description -n python%{python3_pkgversion}-%{name}
There are millions of templating systems out there
(most of them developed for the web).
This isn't one of those, though it does share some basics:
a markup syntax for templates that are processed to give resultant text output.
The main difference with preprocess.py is that its syntax is hidden in comments
(whatever the syntax for comments may be in the target file type)
so that the file can still have valid syntax.
A comparison with the C preprocessor is more apt.

preprocess.py is targeted at build systems that deal with many types of files.
Languages for which it works include: C++, Python, Perl, Tcl, XML, JavaScript,
CSS, IDL, TeX, Fortran, PHP, Java, Shell scripts (Bash, CSH, etc.) and C#.
Preprocess is usable both as a command line app and as a Python module.
%endif
# with_python3

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{name}
Summary: A portable multi-language file Python3 preprocessor

BuildRequires: python%{python3_other_pkgversion}-devel
BuildRequires: python%{python3_other_pkgversion}-future
BuildRequires: python%{python3_other_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{name}}

%description -n python%{python3_other_pkgversion}-%{name}
There are millions of templating systems out there
(most of them developed for the web).
This isn't one of those, though it does share some basics:
a markup syntax for templates that are processed to give resultant text output.
The main difference with preprocess.py is that its syntax is hidden in comments
(whatever the syntax for comments may be in the target file type)
so that the file can still have valid syntax.
A comparison with the C preprocessor is more apt.

preprocess.py is targeted at build systems that deal with many types of files.
Languages for which it works include: C++, Python, Perl, Tcl, XML, JavaScript,
CSS, IDL, TeX, Fortran, PHP, Java, Shell scripts (Bash, CSH, etc.) and C#.
Preprocess is usable both as a command line app and as a Python module.
%endif
# with_python3_other

%prep
%setup -qc

%if 0%{?with_python2}
cp -a preprocess-%{version} python2
pushd python2
find . -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python2}|'
popd
%endif

%if 0%{?with_python3}
cp -a preprocess-%{version} python3
find python3 -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|'
%endif
# with_python3

%if 0%{?with_python3_other}
cp -a preprocess-%{version} python%{python3_other_pkgversion}
find python%{python3_other_pkgversion} -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|'
%endif
# with_python3_other

%build
%if 0%{?with_python3}
pushd python3
%py3_build
popd
%endif
# with_python3

%if 0%{?with_python3_other}
pushd python%{python3_other_pkgversion}
%py3_other_build
popd
%endif
# with_python3_other

%if 0%{?with_python2}
pushd python2
%py2_build
popd
%endif

%install

%if 0%{?rhel} && 0%{?rhel} == 7
%if 0%{?with_python3}
pushd python3
%py3_install
mv $RPM_BUILD_ROOT%{_bindir}/preprocess $RPM_BUILD_ROOT%{_bindir}/python%{python3_version}-preprocess

for i in preprocess-3 preprocess-%{python3_version}; do
  touch -r $RPM_BUILD_ROOT%{_bindir}/python%{python3_version}-preprocess $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python3_version}-preprocess $RPM_BUILD_ROOT%{_bindir}/$i
done
popd

## Fix non-executable script errors
find $RPM_BUILD_ROOT%{python3_sitelib} -name '*.py' | xargs chmod a+x
%endif
%if 0%{?with_python2}
pushd python2
%py2_install
cp -pr $RPM_BUILD_ROOT%{_bindir}/preprocess $RPM_BUILD_ROOT%{_bindir}/python%{python2_version}-preprocess

for i in preprocess-%{python2_version}; do
  touch -r $RPM_BUILD_ROOT%{_bindir}/python%{python2_version}-preprocess $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python2_version}-preprocess $RPM_BUILD_ROOT%{_bindir}/$i
done
popd

## Fix non-executable script errors
find $RPM_BUILD_ROOT%{python2_sitelib} -name '*.py' | xargs chmod a+x
%endif
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
%if 0%{?with_python2}
mv $RPM_BUILD_ROOT%{_bindir}/preprocess $RPM_BUILD_ROOT%{_bindir}/python%{python2_version}-preprocess

for i in preprocess-%{python2_version}; do
  touch -r $RPM_BUILD_ROOT%{_bindir}/python%{python2_version}-preprocess $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python2_version}-preprocess $RPM_BUILD_ROOT%{_bindir}/$i
done
popd

## Fix non-executable script errors
find $RPM_BUILD_ROOT%{python2_sitelib} -name '*.py' | xargs chmod a+x
%endif

%if 0%{?with_python3}
pushd python3
%py3_install
cp -pr $RPM_BUILD_ROOT%{_bindir}/preprocess $RPM_BUILD_ROOT%{_bindir}/python%{python3_version}-preprocess

for i in preprocess-%{python3_version}; do
  touch -r $RPM_BUILD_ROOT%{_bindir}/python%{python3_version}-preprocess $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python3_version}-preprocess $RPM_BUILD_ROOT%{_bindir}/$i
done
popd

## Fix non-executable script errors
find $RPM_BUILD_ROOT%{python3_sitelib} -name '*.py' | xargs chmod a+x
%endif
%endif

%if 0%{?with_python3_other}
pushd python%{python3_other_pkgversion}
%py3_other_install
mv $RPM_BUILD_ROOT%{_bindir}/preprocess $RPM_BUILD_ROOT%{_bindir}/python%{python3_other_version}-preprocess

for i in preprocess-%{python3_other_version}; do
  touch -r $RPM_BUILD_ROOT%{_bindir}/python%{python3_other_version}-preprocess $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python3_other_version}-preprocess $RPM_BUILD_ROOT%{_bindir}/$i
done
popd

##Fix non-executable script errors
find $RPM_BUILD_ROOT%{python3_other_sitelib} -name '*.py' | xargs chmod a+x
%endif

%check
%if 0%{?with_python3}
pushd python3/test
find . -name '*.pyc' -delete
%{__python3} test.py test python cpln -v
popd
%endif

%if 0%{?with_python3_other}
pushd python%{python3_other_pkgversion}/test
find . -name '*.pyc' -delete
%{__python3} test.py test python cpln -v
popd
%endif

%if 0%{?with_python2}
pushd python2
find . -name '*.pyc' -delete
cd test
%{__python2} test.py test python cpln -v
popd
%endif

%if 0%{?with_python2}
%files -n python2-%{name}
%doc python2/README.md python2/CONTRIBUTORS.txt python2/BUGS.txt python2/TODO.txt
%license python2/LICENSE.txt
%if 0%{?rhel} && 0%{?rhel} == 7
%{_bindir}/preprocess
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
%{_bindir}/preprocess-2
%endif
%{_bindir}/preprocess-%{python2_version}
%{_bindir}/python%{python2_version}-preprocess
%{python2_sitelib}/preprocess.py*
%{python2_sitelib}/*.egg-info
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{name}
%doc python3/README.md python3/CONTRIBUTORS.txt python3/BUGS.txt python3/TODO.txt
%license python3/LICENSE.txt
%if 0%{?rhel} && 0%{?rhel} == 7
%{_bindir}/preprocess-3
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
%{_bindir}/preprocess
%endif
%{_bindir}/preprocess-%{python3_version}
%{_bindir}/python%{python3_version}-preprocess
%{python3_sitelib}/preprocess.py*
%{python3_sitelib}/__pycache__/*.py*
%{python3_sitelib}/*.egg-info
%endif

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{name}
%doc python%{python3_other_pkgversion}/README.md python%{python3_other_pkgversion}/CONTRIBUTORS.txt python%{python3_other_pkgversion}/BUGS.txt python%{python3_other_pkgversion}/TODO.txt
%license python%{python3_other_pkgversion}/LICENSE.txt
%{_bindir}/preprocess-%{python3_other_version}
%{_bindir}/python%{python3_other_version}-preprocess
%{python3_other_sitelib}/preprocess.py*
%{python3_other_sitelib}/__pycache__/*.py*
%{python3_other_sitelib}/*.egg-info
%endif

%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2.0.0-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.10

* Fri Feb 19 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.0.0-1
- Release 2.0.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-0.18.20170318git6e868bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-0.17.20170318git6e868bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-0.16.20170318git6e868bc
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-0.15.20170318git6e868bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.2.3-0.14.20170318git6e868bc
- Rebuild for future-0.18.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-0.13.20170318git6e868bc
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-0.12.20170318git6e868bc
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.2.3-0.11.20170318git6e868bc
- Still needs fixes on EPEL7

* Tue Jul 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.2.3-0.10.20170318git6e868bc
- Fix builds on EPEL7

* Tue Jul 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.2.3-0.9.20170318git6e868bc
- Unversioned commands point to Python3 on Fedora
- Obsolete Python2 version on Fedora
- Explicit Provides of Python2 version on EPEL6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-0.8.20170318git6e868bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 29 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.2.3-0.7.20170318git6e868b
- Prepare SPEC file for deprecation of Python2 on fedora 30+
- Prepare SPEC file for Python3-modules packaging on epel7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-0.6.20170318git6e868b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-0.5.20170318git6e868b
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-0.4.20170318git6e868b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.2.3-0.3.20170318git6e868b
- Use versioned Python2 packages

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-0.2.20170318git6e868b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.2.3-0.1.20170318git6e868b
- New version
- Change upstream source (bz#1433605)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12.20150919gitd5ab9a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-11.20150919gitd5ab9a
- Rebuild for Python 3.6

* Tue Aug 16 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.2.2-10.20150919gitd5ab9a
- Rebuild for Python 3.5.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-9.20150919gitd5ab9a
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 16 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.2.2-8.20150919gitd5ab9a
- Fix bad shebang in Python3 package (bz#1342494)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7.20150919gitd5ab9a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.2.2-6.20150919gitd5ab9a
- Renamed Python2 package

* Thu Dec 10 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.2.2-5.20150919gitd5ab9a
- SPEC file adapted to recent guidelines for Python

* Sun Nov 15 2015 Antonio Trande <sagitter@fedoraproject.org> 1.2.2-4.20150919gitd5ab9a
- Rebuild again for Python3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3.20150919gitd5ab9a
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 06 2015 Antonio Trande <sagitter@fedoraproject.org> 1.2.2-2.20150919gitd5ab9a
- Added python-setuptools as BR on EPEL

* Tue Sep 29 2015 Antonio Trande <sagitter@fedoraproject.org> 1.2.2-1.20150919gitd5ab9a
- Update to 1.2.2

* Thu Sep 24 2015 Antonio Trande <sagitter@fedoraproject.org> 1.2.1-3.20150914gitb23422
- Added python_provide macro

* Tue Sep 15 2015 Antonio Trande <sagitter@fedoraproject.org> 1.2.1-2.20150914gitb23422
- Fixed 'non-executable script' errors

* Mon Sep 14 2015 Antonio Trande <sagitter@fedoraproject.org> 1.2.1-1.20150914gitb23422
- Update to 1.2.1 (commit #b234225fff4e79a66bdd8e2341ac9d67be1b3066)
- Some cleanups

* Tue Jul 28 2015 Antonio Trande <sagitter@fedoraproject.org> 1.2-1.20150629git30078c
- Initial build
