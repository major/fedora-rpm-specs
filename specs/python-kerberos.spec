%global srcname kerberos
%global sum A high-level wrapper for Kerberos (GSSAPI) operations

Name:           python-%{srcname}
Version:        1.3.0
Release:        30%{?dist}
Summary:        %{sum}

License:        Apache-2.0
# SVN browser is at https://trac.calendarserver.org/browser/PyKerberos
URL:            https://pypi.python.org/pypi/kerberos
Source0:        https://pypi.python.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        LICENSE

# SystemError thrown with Python 3.10
# https://github.com/apple/ccs-pykerberos/issues/88
# https://bugzilla.redhat.com/2008899
Patch1:         PY_SSIZE_T_CLEAN.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2245868
Patch2:         include_unistd.patch

BuildRequires:  python3-devel
BuildRequires:  python3-requests
BuildRequires:  krb5-devel
BuildRequires:  gcc


%global desc This Python package is a high-level wrapper for Kerberos (GSSAPI) operations.\
The goal is to avoid having to build a module that wraps the entire\
Kerberos framework, and instead offer a limited set of functions that do what\
is needed for client/server Kerberos authentication based on\
<http://www.ietf.org/rfc/rfc4559.txt>.

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
install -m 644 $RPM_SOURCE_DIR/LICENSE LICENSE 
%{pyproject_install}
%pyproject_save_files -L '*'

%check
%pyproject_check_import

# Regression test for https://bugzilla.redhat.com/2008899
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{python3} -c 'import kerberos; kerberos.channelBindings(application_data=b"")'

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 08 2025 Rob Crittenden <rcritten@redhat.com> - 1.3.0-29
- Stop using deprecated python build/install macros (#2377840)

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.3.0-28
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.0-25
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 25 2023 Rob Crittenden <rcritten@redhat.com> - 1.3.0-22
- Python.h no longer includes <unistd.h> (#2245868)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.0-20
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Rob Crittenden <rcritten@redhat.com> - 1.3.0-19
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.0-16
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 29 2021 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-14
- Fix SystemError thrown with Python 3.10

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 1.3.0-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Rob Crittenden <rcritten@redhat.com> - 1.3.0-7
- Drop python 2 sub-packages (#1750421)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Rob Crittenden <rcritten@redhat.com> - 1.3.0-1
- Update to upstream 1.3.0

* Wed Feb 21 2018 Rob Crittenden <rcritten@redhat.com> - 1.2.5-7
- Add BuildRequires on gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-2
- Rebuild for Python 3.6

* Tue Jul 19 2016 Rob Crittenden <rcritten@redhat.com> - 1.2.5-1
- Update to upstream 1.2.5. Fixes single bug,
  http://www.calendarserver.org/changeset/15659
- Include LICENSE since upstream dropped it from the tarball

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 11 2016 Rob Crittenden <rcritten@redhat.com> - 1.2.4-2
- Accept principal=None in authGSSClientInit, upstream issue 942 (#1354334)

* Thu Feb 18 2016 Michal Schmidt <mschmidt@redhat.com> - 1.2.4-1
- Update to current upstream release.
- Build for both python2 and python3.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 15 2015 Rob Crittenden <rcritten@redhat.com> - 1.1-18
- Move LICENSE to the license tag instead of doc.
 
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Rob Crittenden <rcritten@redhat.com> - 1.1-14
- Fix calculation of username string length in authenticate_gss_client_wrap
  (#1057338)

* Fri Jan 17 2014 Rob Crittenden <rcritten@redhat.com> - 1.1-13
- Add patch to allow inquiring the current client credentials

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Rob Crittenden <rcritten@redhat.com> - 1.1-11
- Fix version in setup.py so egg information is correct (#975202)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.1-6.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Simo Sorce <ssorce@redhat.com> - 1.1-3.1
- Fix minor issue with delegation patch

* Fri Dec 12 2008 Simo Sorce <ssorce@redhat.com> - 1.1-3
- Add delegation patch

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-2
- Rebuild for Python 2.6

* Thu Nov 27 2008 Simo Sorce <ssorce@redhat.com> - 1.1-1
- New Upstream Release
- Remove patches as this version has them included already

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-6
- Autorebuild for GCC 4.3

* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-5
- Package the egg-info too

* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-4
- Switch from python_sitelib macro to python_sitearch
- Add python-setuptools to BuildRequires

* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-3
- Use the setup.py install target in order to generate debuginfo.

* Thu Jan  3 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-2
- Add krb5-devel to BuildRequires

* Wed Jan  2 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-1
- Change name to python-kerberos from PyKerberos
- Change license from "Apache License" to ASL 2.0 per guidelines
- Upstream released 1.0 which is equivalent to version 1541. Reverting
  to that.

* Tue Aug 28 2007 Rob Crittenden <rcritten@redhat.com> - 0.1735-2
- Include GSS_C_DELEG_FLAG in gss_init_sec_context() so the command-line
  tools can do kerberos ticket forwarding.

* Tue Jul 31 2007 Rob Crittenden <rcritten@redhat.com> - 0.1735-1
- Initial rpm version
