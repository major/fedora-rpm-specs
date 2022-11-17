## https://github.com/prody/ProDy/issues/266
ExcludeArch: ppc64 s390x

# Tests need internet connection;
# correctly executed in local.
%global with_check 0

##  Filtering of private libraries 
%global _privatelibs  ^%{python3_sitearch}/prody/.*\\.so$
%global __provides_exclude_from ^(%{_privatelibs})$
%global __requires_exclude_from ^(%{_privatelibs})$

Name: ProDy
Summary: Application for protein structure, dynamics and sequence analysis
Version: 2.3.1
Release: 1%{?dist}

# MIT is the main license for ProDy
# prody/utilities/tnt/* code --> 'Public domain' license
# CEalign module is distributed under BSD license
License: MIT and Public domain and BSD
URL: http://www.csb.pitt.edu/ProDy
Source0: https://github.com/prody/ProDy/archive/v%{version}/ProDy-%{version}.tar.gz

BuildRequires: gcc, gcc-c++

%description
ProDy is a free and open-source Python package for protein structure, dynamics,
and sequence analysis.  It allows for comparative analysis and modeling of 
protein structural dynamics and sequence co-evolution.  Fast and flexible ProDy
API is for interactive usage as well as application development.  ProDy also  
comes with several analysis applications and a graphical user interface for 
visual analysis. 
- Visit http://www.csb.pitt.edu/ProDy/ -

%package -n python3-%{name}
Summary: Application for protein structure, dynamics and sequence analysis
%{?python_provide:%python_provide python3-%{name}}
Provides: ProDy = 0:%{version}-%{release}

BuildRequires: python3-devel
BuildRequires: python3-nose
BuildRequires: python3-urllib3
BuildRequires: python3-scipy
BuildRequires: python3-numpy >= 1:1.10.0
BuildRequires: python3-matplotlib
BuildRequires: python3-biopython
BuildRequires: python3-setuptools

Requires: python3-scipy
Requires: python3-biopython
Requires: python3-ipython
Requires: python3-pyparsing
Requires: python3-numpy

## Explicit library require for using plotting functions
Requires: python3-matplotlib

%description -n python3-%{name}
This is ProDy Python3 package for protein structure, dynamics,
and sequence analysis.  It allows for comparative analysis and modeling of 
protein structural dynamics and sequence co-evolution.  Fast and flexible ProDy
API is for interactive usage as well as application development.  ProDy also  
comes with several analysis applications and a graphical user interface for 
visual analysis. 
- Visit http://www.csb.pitt.edu/ProDy/ -

%prep
%setup -qc

# Fix permissions
find %{name}-%{version}/prody/proteins/ccealign -name '*.h' -exec chmod 0644 '{}' \;
find %{name}-%{version}/prody/proteins/ccealign -name '*.cpp' -exec chmod 0644 '{}' \;

mv %{name}-%{version} python3

%build
pushd python3
%py3_build
popd

%install
pushd python3
%py3_install

mkdir -p $RPM_BUILD_ROOT%{_bindir}

rm -f $RPM_BUILD_ROOT%{_bindir}/*

cd scripts
cp -pr ./prody ./python%{python3_version}-prody
cp -pr ./evol  ./python%{python3_version}-evol
# Fix shebangs
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' \
 ./prody \
 ./evol \
 ./python%{python3_version}-prody \
 ./python%{python3_version}-evol

for i in prody-%{python3_version}; do
  touch -r ./python%{python3_version}-prody $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  install -p ./prody $RPM_BUILD_ROOT%{_bindir}
  install -p ./python%{python3_version}-prody $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python3_version}-prody $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in evol-%{python3_version}; do
  touch -r ./python%{python3_version}-evol $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  install -p ./evol $RPM_BUILD_ROOT%{_bindir}
  install -p ./python%{python3_version}-evol $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python3_version}-evol $RPM_BUILD_ROOT%{_bindir}/$i
done
cd ..

%if 0%{?with_check}
%check
pushd python3/scripts
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch} nosetests-%{python3_version} --verbosity=2 \
 -w $RPM_BUILD_ROOT%{python3_sitearch}/prody/tests --tests prody -a '!slow'
popd
%endif

%files -n python3-%{name}
%license python3/LICENSE.rst
%doc python3/README.rst
%{_bindir}/prody
%{_bindir}/prody-%{python3_version}
%{_bindir}/python%{python3_version}-prody
%{_bindir}/evol
%{_bindir}/evol-%{python3_version}
%{_bindir}/python%{python3_version}-evol
%{python3_sitearch}/prody/
%{python3_sitearch}/%{name}-*.egg-info

%changelog
* Tue Nov 15 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.3.1-1
- Release 2.3.1

* Sun Nov 13 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-1
- Release 2.3.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.0-4
- Rebuilt for pyparsing-3.0.9

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.11

* Wed May 25 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-2
- Do not restrict to Biopython<=1.76

* Sun May 22 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-1
- Release 2.2.0

* Fri Apr 29 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.1.2-1
- Release 2.1.2

* Tue Apr 19 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.1.1-1
- Release 2.1.1

* Fri Apr 15 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.1.0-1
- Release 2.1.0

* Thu Feb 17 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.0.2-1
- Release 2.0.2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.0.1-1
- Release 2.0.1
- Remove Python instructions

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0-2
- Rebuilt for Python 3.10

* Wed Feb 24 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.0-1
- Release 2.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.11-1
- Release 1.11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.10-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.10.10-8
- BuildRequires python3-setuptools explicitly

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.10-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.10.10-5
- Remove dependency on unittest2 (#1789200)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.10-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.10-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.10.10-1
- Release 1.10.10
- Unversioned commands point to Python3 on Fedora and EPEL8+
- Unversioned commands point to Python2 on EPEL7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.10.8-1
- Release 1.10.8

* Thu Aug 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.10.6-5
- Build with Python3 on fedora and rhel 8+

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.6-3
- Rebuilt for Python 3.7

* Fri May 25 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.10.6-2
- Fix numpy epoch

* Fri May 18 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.10.6-1
- Release 1.10.6

* Tue May 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.10.3-1
- Release 1.10.3

* Thu May 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.10.2-1
- Release 1.10.2

* Sat Mar 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.9.4-0.1
- Pre-release 1.9.4

* Wed Feb 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.9.3-5.final
- Release 1.9 final (1.9.3 post-release)

* Mon Feb 19 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.9.3-4
- Fix python3 shebang

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.3-2
- Remove useless Python 2 build-time requirements for Fedora

* Sat Nov 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.9.3-1
- Update to 1.9.3
- Obsolete old patch

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.8.2-10
- Rebuild for ipython-6.0.0
- Drop python2-ProDy for missing python2-ipython on fedora <27

* Fri Apr 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.8.2-9
- Rebuild for biopython-1.69

* Fri Feb 17 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.8.2-8
- Fix bug (upstream ticket #363)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.8.2-6
- Exclude architectures ppc64 s390 (upstream bug #266)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.8.2-5
- Rebuild for Python 3.6

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.8.2-4
- rebuilt for matplotlib-2.0.0

* Tue Aug 16 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.8.2-3
- Rebuild for Python 3.5.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 11 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2

* Sat May 14 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1
- Drop old patch

* Sun Feb 14 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.7.1-6
- Rebuilt after GCC6 update
- Test enabled

* Sun Feb 14 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.7.1-5
- Python2 package renamed
- Test disabled

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.7.1-3
- SPEC file adapted to recent guidelines for Python

* Sun Nov 22 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.7.1-2
- Original Python2 'prody' and 'evol' binary files preserved
- Skip tests that are slow

* Fri Nov 13 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1
- Added scipy as BR package
- Set CFLAGS for hardened builds

* Sun Sep 27 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.6.1-1
- Version changed to 1.6.1
- Some tests excluded on EPEL6
- Tests not entirely ready for Python3

* Sat Sep 26 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.6-2
- Fixed python2_version on EL6

* Fri Sep 25 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.6-1
- Update to 1.6
- Performed tests

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.5.1-7
- PPC64 excluded

* Mon May 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.5.1-6
- Fixed License tag
- Python3 disabled because of missing BR package

* Mon May 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.5.1-5
- Rebuild

* Sun May 03 2015 Antonio Trande <sagitter@fedoraproject.org> - 1.5.1-4
- Built with Python3
- Built on EPEL6

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Antonio Trande <sagitter@fedoraproject.org> 1.5.1-1
- Update to 1.5.1

* Mon Nov 25 2013 Antonio Trande <sagitter@fedoraproject.org> 1.4.10-1
- Update to 1.4.10

* Sat Nov 16 2013 Antonio Trande <sagitter@fedoraproject.org> 1.4.9-1
- Update to 1.4.9
- Remove 'cpairwise2.c' file

* Wed Nov 06 2013 Antonio Trande <sagitter@fedoraproject.org> 1.4.8-1
- Re-defined required packages for EPEL
- Update to 1.4.8

* Thu Oct 24 2013 Antonio Trande <sagitter@fedoraproject.org> 1.4.6-2
- Defined a python2 macro only for Fedora

* Wed Oct 23 2013 Antonio Trande <sagitter@fedoraproject.org> 1.4.6-1
- Update to 1.4.6
- Defined python-argparse required package for EPEL
- Spec file renamed ProDy 
- Defined a python2 macro only for Fedora 

* Sun Sep 15 2013 Antonio Trande <sagitter@fedoraproject.org> 1.4.4-3
- Bundled files removed
- Add new required packages (pyparsing, python-biopython)

* Mon Aug 12 2013 Antonio Trande <sagitter@fedoraproject.org> 1.4.4-2
- Added python-matplotlib and python-ipython as Requires
- Perform filtering private libraries 
- Fix some 'non-executable-script' warnings
- Add a Python shebang

* Mon Aug 12 2013 Antonio Trande <sagitter@fedoraproject.org> 1.4.4-1
- Initial build
