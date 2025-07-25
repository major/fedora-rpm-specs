Name:           python-smbpasswd
Version:        1.0.2
Release:        23%{?dist}
Summary:        Python SMB Password Hash Generator Module

License:        GPL-2.0-only
URL:            https://github.com/barryp/py-smbpasswd/
#               http://barryp.org/software/py-smbpasswd/
#               https://github.com/barryp/py-smbpasswd/releases
# Source0:      http://barryp.org/software/py-smbpasswd/files/py-smbpasswd-%%{version}.tar.gz
Source0:        https://github.com/barryp/py-smbpasswd/archive/%{version}.tar.gz#/py-smbpasswd-%{version}.tar.gz
Patch1:         python-smbpasswd-1.0.1-py3.patch

# For python3 the modules using # format needs to define PY_SSIZE_T_CLEAN
Patch2:         python-smbpasswd-1.0.2-py3.10.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc

%global _description\
This package contains a python module, which is able to generate LANMAN and\
NT password hashes suitable to us with Samba.

%description %_description

%package -n python3-smbpasswd
Summary:        %{summary} for Python 3
%{?python_provide:%python_provide python3-smbpasswd}

%description -n python3-smbpasswd
This package contains a python module, which is able to generate LANMAN and
NT password hashes suitable to us with Samba.

This is a ported release for python 3.

%prep
%autosetup -n py-smbpasswd-%{version}

%build
%py3_build

%install
%py3_install

%check
# there are no tests, let's do some sanity check ourselves
%{py3_test_envvars} %{python3} -c '
import smbpasswd
lmhash = "316AEBE722192264AAD3B435B51404EE"
nthash = "B16315C81C204B3CB1E9D00A34C13103"
assert smbpasswd.lmhash("check") == lmhash
assert smbpasswd.nthash("check") == nthash
assert smbpasswd.hash("check") == (lmhash, nthash)'

%files -n python3-smbpasswd
%license COPYING.txt
%doc README.txt
%{python3_sitearch}/smbpasswd.cpython-3*.so
%{python3_sitearch}/*egg-info/

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 1.0.2-22
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.2-19
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-16
- adding %%check to prevent building non-working library

* Thu Oct 05 2023 Michal Ambroz <rebus at_ seznam.cz> - 1.0.2-15
- python 3.10 fix for PY_SSIZE_T_CLEAN s# formatting

* Thu Oct 05 2023 Michal Ambroz <rebus at_ seznam.cz> - 1.0.2-14
- fix dependencies

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.2-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.2-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.2-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 19 2019 Michal Ambroz <rebus at_ seznam.cz> - 1.0.2-1
- update to 1.0.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-42
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-39
- Remove Python 2 subpackage (#1627305)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-37
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.1-35
- Python 2 binary package renamed to python2-smbpasswd
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-31
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-30
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.0.1-21
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Thu Jul 26 2012 David Malcolm <dmalcolm@redhat.com> - 1.0.1-20
- generalize file globbing to ease transition to Python 3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010  David Malcolm <dmalcolm@redhat.com> - 1.0.1-16
- rework python3-smbpasswd manifest for PEP 3149, and rebuild for the newer
python3

* Sun Aug 22 2010 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-15
- Rebuild to fix brocken dependencies on rawhide

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Feb  2 2010 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-13
- Port for python-3

* Mon Aug  3 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-12
- Rebuild for python-2.6.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.1-9
- Rebuild for Python 2.6

* Sun Feb 10 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-8
- Rebuild for gcc-4.3

* Sun Jan  6 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-7
- Add .egg-info file into package

* Wed Aug  8 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-6
- Changing license tag

* Mon Dec 11 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-5
- New Build to solve broken deps

* Sun Sep  3 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-4
- Rebuild for FC-6

* Mon Jul 24 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-3
- Change Permissions of smbwasswd.c

* Sun Jul 23 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-2
- Remove Python(ABI) Require.

* Tue Jun 27 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.0.1-1
- Initial RPM
