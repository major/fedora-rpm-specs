Name:           pysvn
Version:        1.9.21
Release:        8%{?dist}
Summary:        Pythonic style bindings for Subversion
License:        Apache-1.1
URL:            https://pysvn.sourceforge.io/
Source0:        http://pysvn.barrys-emacs.org/source_kits/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  subversion
BuildRequires:  subversion-devel
BuildRequires:  krb5-devel
BuildRequires:  neon-devel
BuildRequires:  apr-devel
BuildRequires:  openssl-devel
BuildRequires:  glibc-langpack-en

# Replace the usage of locale.getdefaultlocale() for python 3.11 support
Patch0001: initlocale.patch

%global _description\
Pythonic style bindings for Subversion\


%description %_description

%package -n python3-pysvn
Summary: Pythonic style bindings for Subversion
%{?python_provide:%python_provide python3-pysvn}
BuildRequires:    python3-devel
BuildRequires:    python3-pycxx-devel >= 7.1.8

%description -n python3-pysvn %_description


%prep
%autosetup -n %{name}-%{version} -p1

# Remove bundled libs
rm -rf Import


%build
pushd Source
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py configure \
    --enable-debug --verbose --fixed-module-name --norpath

echo "optflags %{optflags}"
%{__sed} -i -e 's@-Wall -fPIC -fexceptions -frtti@%{optflags} -fPIC -frtti@' Makefile
%{__make} %{?_smp_mflags}


%install
%{__install} -d -m 755 %{buildroot}%{python3_sitearch}/%{name}
%{__install} -p -m 644 Source/pysvn/__init__.py %{buildroot}%{python3_sitearch}/%{name}
%{__install} -p -m 755 Source/pysvn/_pysvn.so %{buildroot}%{python3_sitearch}/%{name}


%check
pushd Tests
# the tests expect a valid answer from locale.getdefaultlocale()
# C.UTF-8 does not work. Use en_US.utf-8.
LC_ALL=en_US.UTF-8 %{__make} -j1
popd

%files -n python3-pysvn
%doc Docs/pysvn.html Docs/pysvn_prog_guide.html Docs/pysvn_prog_ref.html
%doc Docs/pysvn_prog_ref.js
%doc Examples
%license LICENSE.txt
%{python3_sitearch}/%{name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.9.21-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 1.9.21-2
- Rebuilt for Python 3.12

* Sun Jun 18 2023 Barry A. Scott <barry@barrys-emacs.org> - 1.9.21-1
- Update to upstream 1.9.21 which includes support for python 3.12 beta 1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 22 2022 Barry A. Scott <barry@barrys-emacs.org> - 1.9.20-1
- Update to upstream 1.9.20 which includes support for python 3.12

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Stephen Gallagher <sgallagh@redhat.com> - 1.9.18-1
- Update to upstream release 1.9.18
- Replace usage of locale.getdefaultlocale() for py3.11 support

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.9.17-2
- Rebuilt for Python 3.11

* Sun Feb 13 2022 Barry A. Scott <barry@barrys-emacs.org> - 1.9.17-1
- Update to upstream release 1.9.17

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.12-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Barry Scott <barry@barrys-emacs.org> - 1.9.12-1
- Update to upstream 1.9.12 release
- Add support for subversion 1.14
- Tested with Python 3.9b1
- Add support for gpg-agent auth provider
- Fix problem building against svn 1.7 which is needed for Centos 7 support

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.11-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Barry Scott <barry@barrys-emacs.org> - 1.9.11-3
- revert the last change that introduced a problem with
  generated debug rpm

* Mon Dec 23 2019 Xavier Bachelot <xavier@bachelot.org> - 1.9.11-2
- Add py2 back and conditionalize py2/py3 build.
- Use %%license for LICENSE.txt.

* Sun Dec 15 2019 Barry Scott <barry@barrys-emacs.org> - 1.9.11-1
- Update to upstream 1.9.11 release

* Sun Sep 08 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.10-3
- Subpackage python2-pysvn has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.10-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Barry Scott <barry@barrys-emacs.org> - 1.9.10-1
- Update to 1.9.10 and build against PyCXX 7.1.3
- Fix memory leak for python3 strings from PyCXX

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.9-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Barry Scott <barry@barrys-emacs.org> - 1.9.9-1
- Update to 1.9.9 and build against PyCXX 7.1.2
- remove setup options that are the default

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.9.6-1
- Update to 1.9.6 and build against pyCXX 7.0.3

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.5-5
- Rebuilt for Python 3.7

* Sat May 05 2018 Miro Hrončok <mhroncok@redhat.com> - 1.9.5-4
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Avoid_usr_bin_python_in_RPM_Build)

* Wed Feb 07 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.9.5-3
- Fix conditionals for older releases and EPEL 7

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.5-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Feb 05 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.9.5-1
- Update to 1.9.5
- Resolves: rhbz#1541765

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.2-8
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.2-7
- Python 2 binary package renamed to python2-pysvn
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 16 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.9.2-1
- Update to 1.9.2 to support subversion 1.9

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Stephen Gallagher <sgallagh@redhat.com> 1.8.0-1
- New upstream release 1.8.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jul 09 2015 Stephen Gallagher <sgallagh@redhat.com> 1.7.10-1
- Update to latest pysvn 1.7.10

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Aug 07 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.7.6-8
- Build python3 version as well

* Wed Aug 07 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.7.6-7
- Remove bundled copy of pyCXX
- Resolves: RHBZ#838249

* Mon Aug 05 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.7.6-6
- Drop build dependency on PyXML
- Fix bad changelog date

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.7.6-4
- Disable running tests during build. They have not been updated for use with
  subversion 1.7.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Caitlyn O'Hanna <ravenoak@virtualxistenz.com> - 1.7.6-1
- Update to newest, per request of upstream maintainer.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 26 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.7.5-1.2
- New upstream release 1.7.5
- Do not generate library with --rpath
- Apply upstream patch for test fixes against subversion 1.6.17

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 Caitlyn O'Hanna <ravenoak@virtualxistenz.com> - 1.7.2-1
- Update to newest

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.7.0-3
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Caitlyn O'Hanna <ravenoak@virtualxistenz.com> - 1.7.0-1
- Update to new version

* Wed Mar 04 2009 Caitlyn O'Hanna <ravenoak@virtualxistenz.com> - 1.6.3-2
- Remove the benchmark patch.  Changes included in this release.

* Tue Mar 03 2009 Caitlyn O'Hanna <ravenoak@virtualxistenz.com> - 1.6.3-1
- Update to 1.6.3

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.2-3
- rebuild with new openssl

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.6.2-2
- Rebuild for Python 2.6

* Tue Oct 28 2008 Caitlyn O'Hanna <ravenoak@virtualxistenz.com> - 1.6.2-1
- Upstream to 1.6.2, upstream provided some build fixes to remove patches
-   (Thanks Barry!).  Re-enabled testing with provided patch to fix whitespace

* Sat Oct 11 2008 Caitlyn O'Hanna <ravenoak@virtualxistenz.com> - 1.6.1-2
- Fixed lingering module versioning in __init__

* Mon Oct 06 2008 Caitlyn O'Hanna <ravenoak@virtualxistenz.com> - 1.6.1-1
- Update to 1.6.1, fix F10 FBFS
- Disabled tests, might be because of subversion 1.5

* Wed Feb 27 2008 Timothy Selivanow <timothy.selivanow@virtualxistenz.com> - 1.5.3-1
- Update to 1.5.3

* Thu Feb 14 2008 Timothy Selivanow <timothy.selivanow@virtualxistenz.com> - 1.5.2-6
- Clean up. Name change (back to upstream)

* Tue Feb 12 2008 Timothy Selivanow <timothy.selivanow@virtualxistenz.com> - 1.5.2-5
- Temporary fix for tests.  Need to work with upstream for permanent fix.

* Fri Feb 08 2008 Timothy Selivanow <timothy.selivanow@virtualxistenz.com> - 1.5.2-4
- Fixed build requires, libgssapi-devel was still in there (for EL5 support)

* Fri Jan 11 2008 Timothy Selivanow <timothy.selivanow@virtualxistenz.com> - 1.5.2-3
- Merged patches and spec changes by Terje Røsten <terje.rosten@ntnu.no>
- Fixed the test failures

* Fri Jan 04 2008 Timothy Selivanow <timothy.selivanow@virtualxistenz.com> - 1.5.2-2 
- Attempting to make the spec work with different versions of Python

* Mon Sep 03 2007 Timothy Selivanow <timothy.selivanow@virtualxistenz.com> - 1.5.2-1
- Update to 1.5.2
- Some spec clean up

* Fri Jan 12 2007 Timothy Selivanow <timothy.selivanow@virtualxistenz.com> - 1.5.0-1
- Initial spec creation
