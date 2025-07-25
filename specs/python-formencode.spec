%global srcname FormEncode

Name:           python-formencode
Version:        2.1.1
Release:        4%{?dist}
Summary:        HTML form validation, generation, and convertion package  
# Automatically converted from old format: Python - review is highly recommended.
License:        LicenseRef-Callaway-Python
URL:            http://formencode.org/
Source0:        %pypi_source formencode
BuildArch:      noarch

## For test suite
## Note that the test suite requires all kinds of network connectivity, so we
## can't run it in koji.
#BuildRequires: python3-nose
#BuildRequires: python3-dns

%description
FormEncode validates and converts nested structures. It allows for a 
declarative form of defining the validation, and decoupled processes 
for filling and generating forms.

%package -n python3-formencode
Summary: HTML form validation, generation, and convertion package

BuildRequires: python3-devel
BuildRequires: python3-docutils
BuildRequires: python3-wheel
BuildRequires: python3-pip
BuildRequires: python3-setuptools_scm
#BuildRequires: python3-setuptools_scm_git_archive

Requires: python3-setuptools
Requires: python-formencode-langpacks


%description -n python3-formencode
FormEncode validates and converts nested structures. It allows for a.
declarative form of defining the validation, and decoupled processes.
for filling and generating forms.

This package contains the python3 version of the module.

%package -n python-formencode-langpacks
Summary: Locale files for the python-formencode library

%description -n python-formencode-langpacks
The FormEncode library validates and converts nested structures.  This package
contains the locale files for localizing the message strings in code within the
library.

%prep
%autosetup -n formencode-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
# remove setuptools_scm_git_archive from setup requires
sed -i "s|'setuptools_scm_git_archive',||" setup.py
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l formencode

rm -rf $RPM_BUILD_ROOT%{python3_sitelib}/docs/
# packaged as license, remove this file with wrong path
rm -f $RPM_BUILD_ROOT%{_prefix}/LICENSE.txt


#%%check
## Note that the test suite requires all kinds of network connectivity, so we
## can't run it in koji.
#PYTHONPATH=$(pwd) nosetests-%%{python3_version}


%check
%pyproject_check_import


%files -n python3-formencode -f %{pyproject_files}
%doc docs
%license LICENSE.txt

%files -n python-formencode-langpacks

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 09 2025 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.1.1-3
- Migrate from py_build/py_install to pyproject macros (bz#2377724)

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 2.1.1-2
- Rebuilt for Python 3.14

* Fri Jan 31 2025 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.1.1-1
- Update to upstream.

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 06 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.1.0-1
- Update to upstream.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.1-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.1-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.0.1-3
- Remove useless dependency on setuptools_scm_git_archive

* Tue Oct 05 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.0.1-1
- Update to upstream
- Remove python3.10 patch

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 05 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.0.0-1
- Update to upstream and fix python 3.10 build
- BuildRequire python3-wheel
- BuildRequire python3-setuptools_scm_git_archive and python3-pip (just to be quiet)
- Added LICENSE.txt

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.1-15
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-10
- Subpackage python2-formencode has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 19 2017 Charalampos Stratakis <cstratak@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan  6 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.0-2
- Add python3 subpackage.
- Add a langpacks subpackage so that both python2 and python3 packages can make
  use of it.

* Fri Dec 11 2015 Ralph Bean <rbean@redhat.com> - 1.3.0-1
- new version

* Fri Dec 11 2015 Ralph Bean <rbean@redhat.com> - 1.2.6-5
- Disable the test suite for koji.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 26 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.6-1
- Update to new upstream version of formencode

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 07 2011 Jesse Keating <jkeating@redhat.com> - 1.2.2-5
- Add a macro for RHEL 5 and below

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.2-4
- Apply patch to fix unittests

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> -1.2.2-1
- Update to 1.2.2
- Conditionalize python-elementtree requirement

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.2-1
- Update to 1.2
- Run the test suite
- Remove formencode-translations-system.patch

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.1-3
- Rebuild for Python 2.6

* Thu Aug 28 2008 Toshio Kuratomi <toshio@fedoraproject.org> 1.0.1-2
- Clean up license tag
- Fix executable in %%doc
- Move translations to the proper directory

* Fri Jul 11 2008 Toshio Kuratomi <toshio@fedoraproject.org> 1.0.1-1
- Update to 1.0.1
- Fixes issue where chained_validators were silently ignored.  (bz#454988)
  Both of our patches are fixed upstream now.

* Tue Mar 18 2008 Luke Macken <lmacken@redhat.com> 1.0-1
- Update to 1.0

* Fri Feb 29 2008 Luke Macken <lmacken@redhat.com> 0.9-2
- Add a patch to not explicitly use python2.4

* Thu Feb 28 2008 Luke Macken <lmacken@redhat.com> 0.9-1
- Update to 0.9

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> 0.7.1-2
- Update for python-setuptools changes in rawhide

* Mon Apr  9 2007 Toshio Kuratomi <toshio@tiki-lounge.com> 0.7.1-1
- Upgrade to bugfix 0.7.1 release.

* Fri Apr  6 2007 Toshio Kuratomi <toshio@tiki-lounge.com> 0.7-3
- Require python-setuptools

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> 0.7-2
- Rebuild with newer badurl patch

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> 0.7-1
- 0.7

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> 0.6-3
- Rebuild for python 2.5

* Fri Nov  3 2006 Luke Macken <lmacken@redhat.com> 0.6-2
- Rebuild

* Fri Nov  3 2006 Luke Macken <lmacken@redhat.com> 0.6-1
- 0.6

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> 0.5.1-3
- Rebuild for FC6

* Sat Jul 29 2006 Luke Macken <lmacken@redhat.com> 0.5.1-2
- Rebuild

* Sat Jul 29 2006 Luke Macken <lmacken@redhat.com> 0.5.1-1
- 0.5.1

* Sat Feb  4 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.4-2
- Fix build on devel
- Switch to unmanaged egg

* Thu Dec 29 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.4-1
- Upstream update

* Sun Oct 23 2005 Oliver Andrich <oliver.andrich@gmail.com> 0.2.2-3
- fixed some minor packaging issues

* Thu Oct 13 2005 Oliver Andrich <oliver.andrich@gmail.com> 0.2.2-2
- fixed the too long description line
- add -O1 to the installation process
- %%ghost'ed the *.pyo files

* Thu Oct 06 2005 Oliver Andrich <oliver.andrich@gmail.com> 0.2.2-1
- update to upstream version 0.2.2

* Tue Sep 20 2005 Oliver Andrich <oliver.andrich@gmail.com> 0.2.1-2
- fixed some minor packaging issues for review.

* Tue Sep 20 2005 Oliver Andrich <oliver.andrich@gmail.com> 0.2.1-1
- initial creation
- Version 0.2.1
