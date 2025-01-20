%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
# Disable python2 build by default
%bcond_with python2
%else
%bcond_with python3
%bcond_without python2
%endif


%global srcname docker

Name:           python-%{srcname}
Version:        7.1.0
Release:        5%{?dist}
Summary:        A Python library for the Docker Engine API
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
It lets you do anything the docker command does, but from within Python apps –
run containers, manage containers, manage Swarms, etc.

%if %{with python2}
%package -n python2-%{srcname}
Summary:        A Python library for the Docker Engine API
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python%{?fedora:2}-setuptools
Obsoletes:      python-docker-py < 1:2

%description -n python2-%{srcname}
It lets you do anything the docker command does, but from within Python apps –
run containers, manage containers, manage Swarms, etc.
%endif # with python2

%if %{with python3}
%package -n python3-%{srcname}
Summary:        A Python library for the Docker Engine API
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
Obsoletes:      python3-docker-py < 1:2

%description -n python3-%{srcname}
It lets you do anything the docker command does, but from within Python apps –
run containers, manage containers, manage Swarms, etc.
%endif # with_python3

%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{srcname} -i %{python3_sitelib}/*.dist-info ssh}

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{srcname}-%{version}
rm -fr docker.egg-info

%build
%if %{with python2}
%py2_build
%endif # with python2

%if %{with python3}
%pyproject_wheel
%endif # with_python3

%install
%if %{with python2}
%py2_install
%endif # with python2

%if %{with python3}
%pyproject_install
%pyproject_save_files docker
%endif # with_python3

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*
%endif # with python2

%if %{with python3}
%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%endif # with_python3

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 7.1.0-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 7.1.0-2
- Rebuilt for Python 3.13

* Thu May 23 2024 Packit <hello@packit.dev> - 7.1.0-1
- New upstream release 7.1.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Packit <hello@packit.dev> - 6.1.3-1
- New upstream release 6.1.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.0.3-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Tomas Tomecek <ttomecek@redhat.com> - 5.0.3-1
- New upstream release 5.0.3

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.0.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Tomas Tomecek <ttomecek@redhat.com> - 5.0.2-1
- New upstream release 5.0.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.0.0-2
- Rebuilt for Python 3.10

* Tue Apr 13 2021 Tomas Tomecek <ttomecek@redhat.com> - 5.0.0-1
- New upstream release 5.0.0

* Fri Mar 05 2021 Tomas Tomecek <ttomecek@redhat.com> - 4.4.4-1
- New upstream release 4.4.4

* Mon Feb 22 2021 Tomas Tomecek <ttomecek@redhat.com> - 4.4.3-1
- New upstream release 4.4.3

* Wed Feb 17 2021 Tomas Tomecek <ttomecek@redhat.com> - 4.4.2-1
- New upstream release 4.4.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Tomas Tomecek <ttomecek@redhat.com> - 4.4.1-1
- New upstream release 4.4.1

* Wed Nov 25 13:38:59 CET 2020 Tomas Tomecek <ttomecek@redhat.com> - 4.4.0-1
- new upstream release: 4.4.0

* Mon Sep 14 2020 Tomas Tomecek <ttomecek@redhat.com> - 4.3.1-1
- new upstream release: 4.3.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-2
- Add docker[ssh] subpackage
- Drop all manual requires

* Thu Jun 18 2020 Tomas Tomecek <ttomecek@redhat.com> - 4.2.1-1
- new upstream release: 4.2.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-2
- Rebuilt for Python 3.9

* Tue Mar 24 2020 Tomas Tomecek <ttomecek@redhat.com> - 4.2.0-1
- New upstream release 4.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Tomas Tomecek <ttomecek@redhat.com> - 4.0.2-2
- drop env markers patch

* Fri Sep 13 2019 Tomas Tomecek <ttomecek@redhat.com> - 4.0.2-1
- new upstream release: 4.0.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Frantisek Lachman <flachman@redhat.com> - 4.0.1-1
- New upstream release 4.0.1

* Fri May 24 2019 Frantisek Lachman <flachman@redhat.com> - 4.0.0-1
- New upstream release 4.0.0

* Mon Feb 25 2019 Yatin Karel <ykarel@redhat.com> - 3.7.0-2
- Enable python2 build for el7

* Tue Feb 05 2019 Tomas Tomecek <ttomecek@redhat.com> - 3.7.0-1
- New upstream release 3.7.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Tomas Tomecek <ttomecek@redhat.com> - 3.5.0-1
- New upstream release 3.5.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.1-2
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Tomas Tomecek <ttomecek@redhat.com> - 3.4.1-1
- New upstream release 3.4.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-2
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Tomas Tomecek <ttomecek@redhat.com> - 3.4.0-1
- New upstream release 3.4.0

* Wed May 02 2018 Tomas Tomecek <ttomecek@redhat.com> - 3.3.0-1
- New upstream release 3.3.0

* Tue Apr 03 2018 Tomas Tomecek <ttomecek@redhat.com> - 3.2.1-1
- New upstream release 3.2.1

* Wed Mar 21 2018 Tomas Tomecek <ttomecek@redhat.com> - 3.1.4-1
- New upstream release 3.1.4

* Wed Mar 21 2018 Tomas Tomecek <ttomecek@redhat.com> - 3.1.3-1
- New upstream release 3.1.3

* Thu Mar 15 2018 Charalampos Stratakis <cstratak@redhat.com> - 3.1.1-2
- Don't build Python 2 subpackage on EL > 7

* Tue Mar 06 2018 Tomas Tomecek <ttomecek@redhat.com> - 3.1.1-1
- New upstream release 3.1.1

* Fri Feb 23 2018 Tomas Tomecek <ttomecek@redhat.com> - 3.1.0-1
- New upstream release 3.1.0

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.1-2
- Escape macros in %%changelog

* Wed Feb 07 2018 Tomas Tomecek <ttomecek@redhat.com> - 3.0.1-1
- New upstream release 3.0.1

* Wed Dec 27 2017 Carl George <carl@george.computer> - 2.7.0-1
- Latest upstream rhbz#1527712
- Drop patch1, requirements.txt does not affect final installation
- Drop unnecessary coverage and flake8 build requirements

* Tue Nov 28 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.6.1-2
- Package tests

* Thu Nov 09 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.6.1-1
- new upstream release: 2.6.1

* Wed Nov 08 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.6.0-1
- new upstream release: 2.6.0

* Tue Sep 05 2017 Carl George <carl@george.computer> - 2.5.1-2
- Add patch3 to remove pip dependency
- Rewrite patch2 to conditionally apply extra dependencies
- Update dependencies to be RHEL-compatible
- Don't provide python-docker-py
- Update obsoletes to be RHEL-compatible

* Wed Aug 23 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.5.1-1
- new upstream release: 2.5.1

* Mon Aug 21 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.5.0-1
- new upstream release: 2.5.0

* Tue Aug 01 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.4.2-3
- fix provides of version 1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.4.2-1
- new upstream release: 2.4.2

* Wed Jun 28 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.4.0-1
- new upstream release: 2.4.0

* Wed May 17 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.3.0-1
- new upstream release: 2.3.0

* Fri Apr 07 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.2.1-1
- new upstream release: 2.2.1

* Mon Feb 20 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.1.0-1
- new upstream release: 2.1.0

* Fri Feb 10 2017 Tomas Tomecek <ttomecek@redhat.com> - 2.0.2-1
- new upstream release: 2.0.2, new review:
 - remove remote inspection patch:
   https://github.com/projectatomic/atomic/issues/898
 - doesn't provide python-docker-py (not bacwards compat)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.10.6-2
- Rebuild for Python 3.6

* Mon Nov 28 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.10.6-1
- new upstream release: 1.10.6

* Tue Oct 18 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.10.4-1
- new upstream release: 1.10.4

* Wed Oct 05 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.10.3-1
- new upstream release: 1.10.3

* Fri Jul 29 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.9.0-1
- new upstream release: 1.9.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-0.2.rc2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.9.0-0.1.rc2
- update to 1.9.0rc2

* Fri Jun 17 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.9.0-0.1.rc1
- update to 1.9.0rc1

* Tue May 03 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.8.1-1
- new upstream release: 1.8.1

* Tue Apr 19 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.8.0-3
- remove "py2-ipaddress" as a dependency since it's not available,
  use python-ipaddress instead

* Mon Apr 11 2016 Colin Walters <walters@redhat.com> - 1.8.0-2
- Use bcond, make it easier to build on CentOS 7 for
  https://lists.projectatomic.io/projectatomic-archives/atomic-devel/2016-April/msg00004.html

* Thu Apr 07 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.8.0-1
- new upstream release: 1.8.0

* Fri Mar 04 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.7.2-1
- new upstream release: 1.7.2
- modernized specfile
- fixed URL

* Mon Feb 08 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.7.0.0-1
- new upstream release: 1.7.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.7.0rc2-1
- new upstream release: 1.7.0rc2

* Fri Jan 08 2016 Tomas Tomecek <ttomecek@redhat.com> - 1.6.0-2
- new downstream patch: remote inspection

* Wed Dec 02 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.6.0-1
- new upstream release: 1.6.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 13 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.5.0-1
- new upstream release: 1.5.0

* Fri Sep 11 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.4.0-1
- new upstream release: 1.4.0

* Tue Jul 28 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.3.1-1
- new upstream release: 1.3.1

* Fri Jul 10 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.3.0-1
- new upstream release: 1.3.0

* Fri Jun 19 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.2.3-1
- new upstream release: 1.2.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.2.2-1
- new upstream release: 1.2.2

* Thu Apr 30 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.2.1-1
- new upstream release: 1.2.1

* Wed Mar 18 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.1.0-2
- docker-py 1.1.0 requires requests>=2.5.2

* Fri Mar 13 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.1.0-1
- new upstream release: 1.1.0
- use latest python-requests
- run unit test during build

* Wed Feb 25 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-1
- update to upstream 1.0.0
- Resolves: rhbz#1195627 - don't (B)R docker
- use github url instead of pypi
- run tests in check if /run/docker.sock exists

* Wed Jan 14 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.7.1-1
- Resolves: rhbz#1182003 - Update to 0.7.1

* Thu Dec 25 2014 Igor Gnatenko <ignatenko@mirantis.com> - 0.7.0-1
- Update to 0.7.0 (RHBZ #1176950)

* Mon Dec 01 2014 Tomas Radej <tradej@redhat.com> - 0.6.0-2
- Added Python 3 subpackage

* Fri Nov 21 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.6.0-1
- Resolves: rhbz#1160293 - update to 0.6.0

* Thu Oct 23 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-2
- Resolves: rhbz#1145895
- versioned python-requests req only for f21+

* Wed Oct 22 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-1
- Resolves: rhbz#1153991 - update to 0.5.3

* Tue Sep 23 2014 Tom Prince <tom.prince@clusterhq.com> - 0.5.0-2
- Specify depedencies to match those in setup.py

* Mon Sep 22 2014 Tom Prince <tom.prince@clusterhq.com> - 0.5.0-1
- Resolves: rhbz#1145511 - version bump to 0.5.0

* Tue Aug 26 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.4.0-3
- correct bogus date

* Tue Aug 26 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.4.0-2
- rewrite BR&R conditionals for docker/docker-io

* Thu Aug 21 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.4.0-1
- update to 0.4.0
- Resolves: rhbz#1132604 (epel7 only)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.3.2-1
- version bump to 0.3.2
- Resolves: rhbz#1097415

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-8
- Bug 1063369 - Fix APIError for python-requests-1.1 on rhel6

* Sat Feb 08 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-7
- Bug 1048667 - disable debug package cause archful

* Fri Feb 07 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-6
- doesn't need python-mock at runtime

* Thu Jan 09 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-5
- python3 to be added after python3-websocket-client (BZ 1049424)

* Tue Jan 07 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-4
- double '%%' to comment macros
- check section not considered for now
- python3- description in python3- subpackage conditional

* Tue Jan 07 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-3
- Everything goes in main package
- python3 package requires corrected
- package name python-docker-py
- both packages require docker-io

* Mon Jan 06 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-2
- python3 subpackage
- upstream uses PyPI
- package owns directories it creates
- build and runtime deps updated

* Sun Jan 05 2014 Lokesh Mandvekar <lsm5@redhat.com> 0.2.3-1
- Initial fedora package
