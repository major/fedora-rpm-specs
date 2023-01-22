%global srcname pygsl
%global sum GNU Scientific Library Interface for python

Name:          pygsl
Version:       2.3.0
Release:       21%{?dist}
Summary:       %{sum}

# The package is mostly GPL+ but there are two scripts
# GLPv2+: pygsl/odeiv.py and examples/siman_tsp.py
License:       GPLv2+
Url:           http://pygsl.sourceforge.net
Source0:       http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:        pygsl-swig-c99.patch
BuildRequires: gcc
BuildRequires: gsl-devel

BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-numpy-f2py
BuildRequires: python3-setuptools

# Only need if the generated sources are different from the version used in source
# BuildRequires: swig

Requires:      python3-%{srcname} = %{version}-%{release}

%description
This project provides a python interface for the GNU scientific library (gsl)


%package -n python3-%{srcname}
Summary:       %{sum}
Requires:      python3-numpy
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This project provides a python interface for the GNU scientific library (gsl)


%package devel
Summary:       Development files for pygsl
Requires:      python3-%{srcname}-devel = %{version}-%{release}

%description devel
Development files for pygsl


%package -n python3-%{srcname}-devel
Summary:       Development files for pygsl
Requires:      python3-%{srcname} = %{version}-%{release}
Requires:      python3-devel
%{?python_provide:%python_provide python3-%{srcname}-devel}

%description -n python3-%{srcname}-devel
Development files for pygsl


%prep
%autosetup -p1

%build
# Only need if the generated sources are different from the version used in source
# rm -f swig_src/gslwrap_wrap.c
%__python3 setup.py config
%py3_build

%install
%py3_install

%files

%files devel

%files -n python3-%{srcname}
%license COPYING
%doc ChangeLog README CREDITS
%doc examples/  doc/index.html doc/README.html doc/TODO.html
%{python3_sitearch}/*

%files -n python3-%{srcname}-devel
%{_includedir}/python%{python3_version}*/%{srcname}
%doc testing tests

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec  3 2022 Florian Weimer <fweimer@redhat.com> - 2.3.0-20
- Avoid implicit function declarations in SWIG-generated code

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.0-19
- Rebuild for gsl-2.7.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.0-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 José Matos <jamatos@fedoraproject.org> - 2.3.0-11
- Require at build time python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-7
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.0-6
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Subpackages python2-pygsl, python2-pygsl-devel have been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 José Matos <jamatos@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0 (#1504422)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr  19 2016 José Matos <jamatos@fedoraproject.org> - 2.2.0-1
- update to 2.2.0

* Sat Mar  5 2016 José Matos <jamatos@fedoraproject.org> - 2.1.1-4
- rebuild for gsl 2.1
- Use swig to regenerate the wrappers.

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1.1-3
- Rebuild for gsl 2.1

* Sun Feb 14 2016 José Matos <jamatos@fedoraproject.org> - 2.1.1-2
- fix requirements (typos)

* Sat Feb 13 2016 José Matos <jamatos@fedoraproject.org> - 2.1.1-1
- update to 2.1.1
- remove included license
- add python2 and python3 subpackages, preserving the upgrade path

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 José Matos <jamatos@fedoraproject.org> - 0.9.5-8
- Clean spec file (thanks to Jussi #528515)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May  9 2011 José Matos <jamatos@fedoraproject.org> - 0.9.5-5
- Rebuild for a newer gsl (F16+)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 10 2010 José Matos <jamatos@fc.up.pt> - 0.9.5-2
- Rebuild for new gsl version (F14+).

* Thu Apr  8 2010 José Matos <jamatos@fc.up.pt> - 0.9.5-1
- Bug fix release. A memory leak was fixed for all modules using
  gsl_functions: integrate, min, roots, deriv.
- Include more original documentation.
- Remove patch applied upstream.

* Thu Nov 19 2009 José Matos <jamatos@fc.up.pt> - 0.9.4-7
- Revert to local patch as upstream one does not work.

* Thu Nov 19 2009 José Matos <jamatos@fc.up.pt> - 0.9.4-6
- Request build with the upstream patch.

* Thu Nov 19 2009 José Matos <jamatos@fc.up.pt> - 0.9.4-5
- Fix typo in -devel Summary. (#504881)

* Tue Sep 15 2009 José Matos <jamatos@fc.up.pt> - 0.9.4-4
- Remove gsm units taken away in gsl-1.13.

* Tue Sep 15 2009 José Matos <jamatos@fc.up.pt> - 0.9.4-3
- Rebuild for new upstream gsl version (F12+).

* Thu Jul 30 2009 José Matos <jamatos[AT]fc.up.pt> - 0.9.4-2
- Add missing BR numpy-f2py

* Thu Jul 30 2009 José Matos <jamatos[AT]fc.up.pt> - 0.9.4-1
- New upstream bugfix release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 José Matos <jamatos@fc.up.pt> - 0.9.3-3
- Rebuild for new gsl (F11+).

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.3-2
- Rebuild for Python 2.6

* Tue Jun 17 2008 José Matos <jamatos[AT]fc.up.pt> - 0.9.3-1
- New upstream release.

* Fri Feb 22 2008 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-8
- Add egg-info file to package (F9+).

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.1-7
- Autorebuild for GCC 4.3

* Fri Sep 21 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-6
- License clarification.
- Use swig to regenerate the wrappers.
- Rebuild with gsl-1.10.
- Add explicit dependency on gsl version.

* Thu Aug 30 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-5
- Fix typo in Requires for subpackage devel.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-4
- Remove docs from documentation as it not carried anymore, add a devel subpackage.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-3
- Corrected the reference to numpy.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-2
- Rebuild with the correct source.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-1
- New upstream version.
- Change from numeric to numpy.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-8
- License fix, rebuild for devel (F8).

* Mon Dec 11 2006 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-7
- Rebuild for python 2.5.

* Mon Sep 11 2006 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-6
- Rebuild for FC6.

* Thu Feb 16 2006 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-5
- Rebuild for FC-5.

* Sat Jul  2 2005 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-4
- Add license file from cvs.

* Fri Jul  1 2005 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-3
- Remove duplicated "setup" entry.

* Fri Jul  1 2005 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-2
- Clean spec file.

* Thu Jun 30 2005 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-1
- New version.
