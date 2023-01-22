%{?!_without_bzr:%global with_bzr 0%{?_with_bzr:1} || !(0%{?rhel} >= 8 || 0%{?fedora} >= 37)}

%global srcname wstool

Name:           python-%{srcname}
Version:        0.1.18
Release:        11%{?dist}
Summary:        Tool for managing a workspace of multiple heterogeneous SCM repositories

License:        BSD
URL:            http://www.ros.org/wiki/%{srcname}
Source0:        https://github.com/vcstools/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Patch to remove a duplicate installed file.  Not submitted upstream
Patch0:         %{srcname}-0.1.9-fedora.patch

BuildArch:      noarch

%if 0%{?with_bzr}
BuildRequires:  bzr
%endif
BuildRequires:  git
BuildRequires:  mercurial
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  subversion

%global _description\
wstool provides commands to manage several local SCM repositories (supports\
git, mercurial, subversion, bazaar) based on a single workspace definition file\
(.rosinstall).\
\
wstool replaces the rosws tool for catkin workspaces. As catkin workspaces\
create their own setup file and environment, wstool is reduced to version\
control functions only. So wstool does not have a "regenerate" command, and\
does not allow adding non-version controlled elements to workspaces. In all\
other respects, it behaves the same as rosws.

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-vcstools >= 0.1.38
%if 0%{?with_bzr}
Requires:       bzr
%endif
Requires:       git
Requires:       mercurial
Requires:       subversion
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Obsoletes:      python2-%{srcname} < 0.1.17-14

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-vcstools >= 0.1.38
%endif

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Drop test coverage
sed -i '/^coverage/d' requirements-test.txt


%build
%py3_build


%install
%py3_install


%check
export BZR_EMAIL="Foo Bar <foo@example.com>"
export GIT_AUTHOR_EMAIL="foo@example.com"
export GIT_AUTHOR_NAME="Foo Bar"
export GIT_COMMITTER_EMAIL="foo@example.com"
export GIT_COMMITTER_NAME="Foo Bar"

%if !(0%{?with_bzr})
%global pytest_skip_tests test_wstool_.*bzr.*|test_rosinstall_detailed_locapath_info|test_unmanaged|test_multi_.*
%endif

%{__python3} -m nose test %{?pytest_skip_tests:-e "^(%{pytest_skip_tests})$"}


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst doc/changelog.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/%{srcname}
%{_mandir}/man1/%{srcname}.1.gz
# bash completion
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{srcname}-completion.bash
# zsh completion
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_wstool


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Scott K Logan <logans@cottsay.net> - 0.1.18-9
- Drop bzr for Fedora 37 and EPEL 8 (rhbz#2099145)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.18-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.18-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Scott K Logan <logans@cottsay.net> - 0.1.18-1
- Update to 0.1.18 (rhbz#1754688)

* Tue Sep 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.17-14
- Remove the Python 2 subpackage, the Python 3 package provides the CLI now

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.17-13
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Scott K Logan <logans@cottsay.net> - 0.1.17-12
- Add upstream patches for newer PyYAML compatibility (rhbz#1712544)
- Drop test coverage
- Handle automatic dependency generation (f30+)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Scott K Logan <logans@cottsay.net> - 0.1.17-9
- Remove rosinstall requriement entirely (not needed after 0.1.1)
- Switch from {commit} to {version} for source archive
- Align spec with python templates

* Mon Nov 12 2018 Scott K Logan <logans@cottsay.net> - 0.1.17-8
- Require python3-rosinstall for /usr/bin/rosinstall (PR #2)

* Tue Jul 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.17-7
- Correct macro usage

* Fri Jul 20 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.17-6
- Rebuild for https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.17-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.17-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 11 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.17-1
- Update to latest release (rhbz#1533303)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.13-5
- Python 2 binary package renamed to python2-wstool
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.13-2
- Rebuild for Python 3.6

* Sun Aug 28 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.13-1
- Update to lastest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 20 2015 Rich Mattes <richmattes@gmail.com> - 0.1.12-1
- Update to release 0.1.12 (rhbz#1271029)

* Wed Sep 16 2015 Rich Mattes <richmattes@gmail.com> - 0.1.10-1
- Update to release 0.1.10 (rhbz#1261684)

* Sun Sep 13 2015 Rich Mattes <richmattes@gmail.com> - 0.1.9-1
- Update to release 0.1.9 (rhbz#1261684)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 04 2015 Rich Mattes <richmattes@gmail.com> - 0.1.6-1
- Update to release 0.1.6 (rhbz#1195537)

* Sun Dec 14 2014 Scott K Logan <logans@cottsay.net> - 0.1.5-1
- Update to 0.1.5
- Update to python packaging guidelines
- Add check section

* Thu Jul 31 2014 Scott K Logan <logans@cottsay.net> - 0.1.4-1
- Update to 0.1.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon May 19 2014 Scott K Logan <logans@cottsay.net> - 0.1.3-1
- Update to 0.1.3
- Add depend on PyYAML

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Jan 12 2014 Rich Mattes <richmattes@gmail.com> - 0.1.1-1
- Update to 0.1.1

* Mon Aug 26 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.0.3-1
- Rename python3 bin script

* Sun Aug 25 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.0.3-1
- Update source to github source
- Add py3 support

* Sat Mar 16 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.0.3-1
- Initial rpmbuild

