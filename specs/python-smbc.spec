%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

Summary:       Python bindings for libsmbclient API from Samba
Name:          python-smbc
Version:       1.0.25.1
Release:       13%{?dist}
URL:           https://github.com/hamano/pysmbc
Source:        %{URL}/archive/%{version}/pysmbc-%{version}.tar.gz
License:       GPL-2.0-or-later

# gcc is no longer in buildroot by default
BuildRequires: gcc
# uses autosetup
BuildRequires: git-core

BuildRequires: python3-devel
BuildRequires: libsmbclient-devel >= 3.2

%generate_buildrequires
%pyproject_buildrequires

%description
This package provides Python bindings for the libsmbclient API
from Samba, known as pysmbc. It was written for use with
system-config-printer, but can be put to other uses as well.

%package -n python3-smbc
Summary:       Python3 bindings for libsmbclient API from Samba
%{?python_provide:%python_provide python3-smbc}

%description -n python3-smbc
This package provides Python 3 bindings for the libsmbclient API
from Samba, known as pysmbc. It was written for use with
system-config-printer, but can be put to other uses as well.

%package doc
Summary:       Documentation for python-smbc

%description doc
Documentation for python-smbc.

%prep
%autosetup -n pysmbc-%{version} -S git

%build
%pyproject_wheel

%install
%pyproject_install
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{_bindir}/pydoc3 -w smbc
%{_bindir}/mkdir html
%{_bindir}/mv smbc.html html

%files -n python3-smbc
%doc README.md NEWS
%license COPYING
%{python3_sitearch}/*

%files doc
%doc html


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 09 2025 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.25.1-12
- remove deprecated python macros (fedora#2378212)

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 1.0.25.1-11
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.25.1-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 23 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.25.1-5
- SPDX migration, spec update

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.25.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.25.1-1
- 1.0.25.1, fixes #2155419

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.23-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.23-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.23-1
- 1.0.23

* Tue Aug 04 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.15.4-27
- use versioned python3 sitearch

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.15.4-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.15.4-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.15.4-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.15.4-18
- 1630335 - python-smbc: Remove (sub)packages from Fedora 30+: python2-smbc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.15.4-16
- Rebuilt for Python 3.7

* Thu Apr 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.15.4-15
- make python2 subpackage optional
- fix documentation

* Mon Feb 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.15.4-14
- gcc is no longer in buildroot by default

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.15.4-10
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.15.4-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15.4-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.15.4-5
- python2 subpackage

* Fri Nov 20 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.15.4-4
- don't use py3dir, use python_provide

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.15.4-2
- Rebuilt for Python3.5 rebuild

* Fri Sep 25 2015 Tim Waugh <twaugh@redhat.com> - 1.0.15.4-1
- New upstream release (and location).

* Tue Aug 11 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.13-13
- %%py_build && %%py_install

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Tim Waugh <twaugh@redhat.com> - 1.0.13-6
- Use pkg-config for smbclient include_dirs, fixing rebuild failure.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.0.13-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 1.0.13-4
- add with_python3 conditionals

* Thu Jul 26 2012 David Malcolm <dmalcolm@redhat.com> - 1.0.13-3
- generalize file globbing to ease transition to Python 3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 15 2012 Tim Waugh <twaugh@redhat.com> - 1.0.13-1
- 1.0.13.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 20 2011 Tim Waugh <twaugh@redhat.com> - 1.0.11-1
- 1.0.11.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.10-3
- rework python3 DSO name for PEP 3149, and rebuild for newer python3

* Wed Nov 17 2010 Jiri Popelka <jpopelka@redhat.com> - 1.0.10-2
- Fixed rpmlint errors/warnings (#648987)
- doc subpackage

* Mon Nov 01 2010 Jiri Popelka <jpopelka@redhat.com> - 1.0.10-1
- Initial RPM spec file
