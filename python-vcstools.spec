%{?!_without_bzr:%global with_bzr 0%{?_with_bzr:1} || !(0%{?rhel} >= 8 || 0%{?fedora} >= 37)}
%{?!_without_python2:%global with_python2 0%{?_with_python2:1} || !(0%{?rhel} >= 8 || 0%{?fedora} >= 32)}
%{?!_without_python3:%global with_python3 0%{?_with_python3:1} || !0%{?rhel} || 0%{?rhel} >= 7}

%global srcname vcstools

Name:           python-%{srcname}
Version:        0.1.42
Release:        15%{?dist}
Summary:        Version Control System tools for Python

License:        BSD
URL:            http://www.ros.org/wiki/vcstools
Source0:        https://github.com/%{srcname}/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Submitted upstream as vcstool/vcstools#163
Patch0:         %{name}-0.1.42-isAlive.patch
# Switch from yaml.load to yaml.safe_load
# Not submitted upstream (project is archived on github)
Patch1:         %{name}-0.1.42-yamlload.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  git
BuildRequires:  mercurial
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  subversion

%if 0%{?with_bzr}
BuildRequires:  bzr
%endif

%description
The vcstools module provides a Python API for interacting with different
version control systems (VCS/SCMs). The VcsClient class provides an API
for seamless interacting with Git, Mercurial (Hg), Bzr and SVN. The focus
of the API is manipulating on-disk checkouts of source-controlled trees.
Its main use is to support the rosinstall tool.


%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-dateutil
BuildRequires:  python2-devel
BuildRequires:  python2-mock
BuildRequires:  python2-nose
BuildRequires:  python2-pyyaml
BuildRequires:  python2-setuptools
Requires:       python2-dateutil
Requires:       python2-pyyaml
%{?python_provide:%python_provide python2-%{srcname}}

%if 0%{?rhel} && 0%{?rhel} < 8
Requires:       git
Requires:       mercurial
Requires:       subversion
%if 0%{?with_bzr}
Requires:       bzr
%endif
%else
Recommends:     git
Recommends:     mercurial
Recommends:     subversion
%if 0%{?with_bzr}
Recommends:     bzr
%endif
%endif

%description -n python2-%{srcname}
The vcstools module provides a Python API for interacting with different
version control systems (VCS/SCMs). The VcsClient class provides an API
for seamless interacting with Git, Mercurial (Hg), Bzr and SVN. The focus
of the API is manipulating on-disk checkouts of source-controlled trees.
Its main use is to support the rosinstall tool.
%endif


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-PyYAML
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if 0%{?rhel} && 0%{?rhel} < 8
Requires:       git
Requires:       mercurial
Requires:       subversion
%if 0%{?with_bzr}
Requires:       bzr
%endif
%else
Recommends:     git
Recommends:     mercurial
Recommends:     subversion
%if 0%{?with_bzr}
Recommends:     bzr
%endif
%endif

%description -n python%{python3_pkgversion}-%{srcname}
The vcstools module provides a Python API for interacting with different
version control systems (VCS/SCMs). The VcsClient class provides an API
for seamless interacting with Git, Mercurial (Hg), Bzr and SVN. The focus
of the API is manipulating on-disk checkouts of source-controlled trees.
Its main use is to support the rosinstall tool.
%endif


%prep
%autosetup -p1 -n %{srcname}-%{version}

sed -i 's/haiku/default/' doc/conf.py
sed -i 's/:special-members://' doc/vcstools.rst

# Drop the test requirements from the setup.py
# The conditionals in it break with older setuptools (RHEL 7)
sed -i "s/\\w*tests_require=test_required,//" setup.py
sed -i "s/\\w*'test': test_required//" setup.py


%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

%make_build -C doc html man SPHINXBUILD=sphinx-build-%{python3_version}
rm doc/_build/html/.buildinfo


%install
%if 0%{?with_python2}
%py2_install
install -p -D -m 0644 doc/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1
%endif

%if 0%{?with_python3}
%py3_install
install -p -D -m 0644 doc/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/python3-%{srcname}.1
%endif


%check
# Some tests REQUIRE Python 2 to use unicode
%if 0%{?rhel}
export LANG=en_US.UTF-8
%else
export LANG=C.UTF-8
%endif

%if !(0%{?with_bzr})
%global pytest_skip_bzr |test_bzr
%endif

# Exclude 5 tests which access remote data
# Exclude a test with a bad unicode conversion on python2.6 machines (Github vcstools/vcstools#77)
%global pytest_skip_tests test_git_subm|test_url_matches_with_shortcut|test_checkout|test_checkout_dir_exists|test_checkout_version|test_get_url_by_reading%{?pytest_skip_bzr}

%if 0%{?with_python2}
%{__python2} -m nose test -e "^(%{pytest_skip_tests})$" --verbose
%endif

%if 0%{?with_python3}
%{__python3} -m nose test -e "^(%{pytest_skip_tests})$" --verbose
%endif


%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc doc/_build/html
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info/
%{_mandir}/man1/%{srcname}.1.gz
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc doc/_build/html
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_mandir}/man1/python3-%{srcname}.1.gz
%endif


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.1.42-14
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Scott K Logan <logans@cottsay.net> - 0.1.42-11
- Drop bzr for Fedora 37 (rhbz#2099140)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.1.42-10
- Rebuilt for Python 3.11

* Sat Feb 12 2022 Rich Mattes <richmattes@gmail.com> - 0.1.42-9
- Add patch to use yaml safe_load (rhbz#2046918)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.42-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.42-4
- Rebuilt for Python 3.9

* Thu May 21 2020 Scott K Logan <logans@cottsay.net> - 0.1.42-3
- Add patch for Python 3.8 compatibility

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Scott K Logan <logans@cottsay.net> - 0.1.42-1
- Update to 0.1.42 (rhbz#1742573)
- Drop RHEL 6 conditionals from spec
- Drop bzr for EPEL 8

* Thu Sep 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.40-7
- Subpackage python2-vcstools has been removed on Fedora 32+
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.40-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Scott K Logan <logans@cottsay.net> - 0.1.40-4
- Move SCM packages from Requires to Recommends
- Drop test coverage from %%check
- Clean up spec file
- Add Python 3 subpackage for EPEL7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.40-2
- Add BR:glibc-langpack-en
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Mon Jul 23 2018 Rich Mattes <richmattes@gmail.com> - 0.1.40-1
- Update to release 0.1.40 (rhbz#1532912)
- Disable broken unit test (rhbz#1556280)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.39-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.39-7
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.39-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.39-2
- Rebuild for Python 3.6

* Thu Oct 20 2016 Rich Mattes <richmattes@gmail.com> - 0.1.39-1
- Update to 0.1.39 (rhbz#1376312)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.38-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 20 2015 Rich Mattes <richmattes@gmail.com> - 0.1.38-1
- Update to release 0.1.38 (rhbz#1271028)

* Sun Sep 13 2015 Rich Mattes <richmattes@gmail.com> - 0.1.37-1
- Update to release 0.1.37 (rhbz#1259100)
- Remove upstreamed patch

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 14 2014 Scott K Logan <logans@cottsay.net> - 0.1.36-1
- Update to release 0.1.36
- Update to python packaging guidelines
- Add check section
- Add patch for test fixes
- Add bzr, git, mercurial and subversion to Requires

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.35-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon May 19 2014 Scott K Logan <logans@cottsay.net> - 0.1.35-1
- Update to release 0.1.35

* Sun Feb 09 2014 Rich Mattes <richmattes@gmail.com> - 0.1.32-2
- Added python 3 support

* Sat Feb 08 2014 Rich Mattes <richmattes@gmail.com> - 0.1.32-1
- Update to release 0.1.32

* Mon Aug 19 2013 Rich Mattes <richmattes@gmail.com> - 0.1.31-1
- Update to release 0.1.31
- Update to github sourceurl guidelines

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.30-2.20130318git963c121
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Rich Mattes <richmattes@gmail.com> - 0.1.30-1.20130318git963c121
- Update to release 0.1.30
- Updated upstream URL

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.26-2.20130102gitd41568f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 02 2013 Rich Mattes <richmattes@gmail.com> - 0.1.26-1.20130102gitd41568f
- Update to release 0.1.26
* Fri Oct 26 2012 Rich Mattes <richmattes@gmail.com> - 0.1.24-1.20121026gitba30262
- Update to release 0.1.24

* Tue Aug 28 2012 Rich Mattes <richmattes@gmail.com> - 0.1.21-1.20120828hg0fba0588
- Update to release 0.1.21

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-4.20120606hg6205f4fc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Rich Mattes <richmattes@gmail.com> - 0.1.17-3.20120606hg6205f4fc
- Added el6 support
- Enabled unit tests

* Wed Jun 06 2012 Rich Mattes <richmattes@gmail.com> - 0.1.17-2.20120606hg6205f4fc
- Update package release to include hg checkout info
- Remove el5 specific RPM_BUILD_ROOT removal from install section

* Tue Jun 05 2012 Rich Mattes <richmattes@gmail.com> - 0.1.17-1
- Update to release 0.1.17

* Wed Apr 25 2012 Rich Mattes <richmattes@gmail.com> - 0.1.4-1
- Initial package
