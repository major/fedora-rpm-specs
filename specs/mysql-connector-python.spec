# spec file for mysql-connector-python
#
# Copyright (c) 2011-2014 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#

# Tests only run on manual build --with tests
# Tests rely on MySQL version 5.6
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}

Name:           mysql-connector-python
Version:        8.0.21
Release:        16%{?dist}
Summary:        MySQL Connector for Python 3

# Automatically converted from old format: GPLv2 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            http://dev.mysql.com/doc/connector-python/en/index.html
# Upstream has a mirror redirector for downloads, so the URL is hard to
# represent statically.  You can get the tarball by following a link from
# http://dev.mysql.com/downloads/connector/python/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel >= 3
BuildRequires:  python3-setuptools
%if %{with_tests}
# for unittest
BuildRequires:  mysql-server
%endif


%global _description\
MySQL Connector/Python is implementing the MySQL Client/Server protocol\
completely in Python. No MySQL libraries are needed, and no compilation\
is necessary to run this Python DB API v2.0 compliant driver.\
\
Documentation: http://dev.mysql.com/doc/connector-python/en/index.html\


%description %_description

%package -n mysql-connector-python3
Summary: MySQL Connector for Python 3
%{?python_provide:%python_provide python3-mysql-connector}

%description -n mysql-connector-python3
MySQL Connector/Python is implementing the MySQL Client/Server protocol
completely in Python. No MySQL libraries are needed, and no compilation
is necessary to run this Python DB API v2.0 compliant driver.

Documentation: http://dev.mysql.com/doc/connector-python/en/index.html


%prep
%setup -q -n %{name}-%{version}
chmod -x examples/*py

%build
# nothing to build


%install
%{__python3} setup.py install --root %{buildroot}



%check
%if %{with_tests}
# known failed tests
# bugs.BugOra14201459.test_error1426

%{__python3} unittests.py \
    --with-mysql=%{_prefix} \
    --verbosity=1
%else
: echo test suite disabled, need '--with tests' option
%endif


%files -n mysql-connector-python3
%doc CHANGES.txt README* docs
%doc examples
%license LICENSE.txt
%{python3_sitelib}/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 8.0.21-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 8.0.21-13
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 8.0.21-9
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 8.0.21-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 8.0.21-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Michal Schorm <mschorm@redhat.com> - 8.0.21-1
- Rebase to 8.0.21

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.0.20-2
- Rebuilt for Python 3.9

* Tue May 05 2020 Michal Schorm <mschorm@redhat.com> - 8.0.20-1
- Rebase to 8.0.20
- Upstream stopped to hardcode required protobuf version, patch can be removed
  Resolves: #1830662

* Fri Feb 07 2020 Michal Schorm <mschorm@redhat.com> - 8.0.19-3
- Rebuilt for newer protobuf version
  Resolves: #1797297

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Michal Schorm <mschorm@redhat.com> - 8.0.19-1
- Rebase to 8.0.19

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 8.0.16-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 8.0.16-4
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Miro Hrončok <mhroncok@redhat.com> - 8.0.16-3
- Drop python2-mysql-connector (#1731660)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Honza Horak <hhorak@redhat.com> - 8.0.16-1
- Rebase to 8.0.16
  Resolves: #1390718

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-13
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.6-11
- Python 2 binary package renamed to python2-mysql-connector
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 16 2014 Remi Collet <remi@fedoraproject.org> - 1.1.6-1
- version 1.1.6 GA
  http://dev.mysql.com/doc/relnotes/connector-python/en/news-1-1-6.html

* Tue Feb  4 2014 Remi Collet <remi@fedoraproject.org> - 1.1.5-1
- version 1.1.5 GA
  http://dev.mysql.com/doc/relnotes/connector-python/en/news-1-1-5.html

* Tue Dec 17 2013 Remi Collet <remi@fedoraproject.org> - 1.1.4-1
- version 1.1.4 GA
  http://dev.mysql.com/doc/relnotes/connector-python/en/news-1-1.html
- add link to documentation in package description
- raise dependency on python 2.6

* Mon Aug 26 2013 Remi Collet <remi@fedoraproject.org> - 1.0.12-1
- version 1.0.12 GA

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul  3 2013 Remi Collet <remi@fedoraproject.org> - 1.0.11-1
- version 1.0.11 GA

* Wed May  8 2013 Remi Collet <remi@fedoraproject.org> - 1.0.10-1
- version 1.0.10 GA
- archive is now free (no more doc to strip)

* Wed Feb 27 2013 Remi Collet <remi@fedoraproject.org> - 1.0.9-1
- version 1.0.9 GA
- disable test suite in mock, fix FTBFS #914203

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 29 2012 Remi Collet <remi@fedoraproject.org> - 1.0.8-1
- version 1.0.8 GA

* Wed Oct  3 2012 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- version 1.0.7 GA

* Sat Sep 15 2012 Remi Collet <remi@fedoraproject.org> - 1.0.6-2.b2
- version 1.0.6b2

* Fri Sep  7 2012 Remi Collet <remi@fedoraproject.org> - 1.0.6-1.b1
- version 1.0.6 (beta)
- remove non GPL documentation
- disable test_network and test_connection on EL-5

* Fri Aug 10 2012 Remi Collet <remi@fedoraproject.org> - 1.0.5-2
- disable test_bugs with MySQL 5.1 (EL-6)

* Wed Aug  8 2012 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- version 1.0.5 (beta)
- move from launchpad (devel) to dev.mysql.com

* Fri Aug 03 2012 David Malcolm <dmalcolm@redhat.com> - 0.3.2-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 20 2011 Remi Collet <Fedora@famillecollet.com> 0.3.2-2
- run unittest during %%check
- fix License
- add python3 sub package

* Wed Mar 09 2011 Remi Collet <Fedora@famillecollet.com> 0.3.2-1
- first RPM

