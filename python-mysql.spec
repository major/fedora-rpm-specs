%bcond_without python3_debug

Summary:  An interface to MySQL
Name:     python-mysql
Version:  1.4.6
Release:  14%{?dist}
License:  GPLv2+
URL:      https://github.com/PyMySQL/mysqlclient-python

Source0:  %pypi_source mysqlclient

BuildRequires: gcc
BuildRequires: python3-devel python3-setuptools
BuildRequires: mariadb-connector-c-devel openssl-devel zlib-devel
%if %{with python3_debug}
BuildRequires: python3-debug
%endif

# Write description once, use several times
%global _description %{expand:
Python interface to MySQL

MySQLdb is an interface to the popular MySQL database server for Python.
The design goals are:

-     Compliance with Python database API version 2.0
-     Thread-safety
-     Thread-friendliness (threads will not block each other)}

%description %_description

%package -n python3-mysql
Summary: An interface to MySQL
%{?python_provide:%python_provide python3-mysql}
# Can be dropped after https://src.fedoraproject.org/rpms/trytond/pull-request/2
Provides: MySQL-python3 = %{version}-%{release}

%description -n python3-mysql %_description

%if %{with python3_debug}
%package -n python3-mysql-debug
Summary:  An interface to MySQL, built for the CPython debug runtime
%{?python_provide:%python_provide python3-mysql-debug}
# Require the base package for the .py/.pyc files:
Requires: python3-mysql%{_isa} = %{version}-%{release}

%description -n python3-mysql-debug
Python3 interface to MySQL, built for the CPython debug runtime
%endif # with python3_debug


%prep
%autosetup -n mysqlclient-%{version} -p1

%build
%{set_build_flags}

%py3_build
%if %{with python3_debug}
%{__python3}-debug setup.py build
%endif


%install
%py3_install
%if %{with python3_debug}
%{__python3}-debug setup.py install -O1 --skip-build --root %{buildroot}
%endif


%check
# You need MySQL (or MariaDB) running
# and ~/.my.conf configured to have access rights
#
# cd tests/
# python -m unittest test_MySQLdb_capabilities
# python -m unittest test_MySQLdb_dbapi20
# python -m unittest test_MySQLdb_nonstandard

%files -n python3-mysql
%doc README.md doc/*
%license LICENSE
%dir %{python3_sitearch}/MySQLdb
%{python3_sitearch}/MySQLdb/_mysql.cpython-%{python3_version_nodots}-*.so
%{python3_sitearch}/MySQLdb/*.py
%dir %{python3_sitearch}/MySQLdb/__pycache__
%{python3_sitearch}/MySQLdb/__pycache__/*.pyc
%dir %{python3_sitearch}/MySQLdb/constants
%{python3_sitearch}/MySQLdb/constants/*.py
%dir %{python3_sitearch}/MySQLdb/constants/__pycache__
%{python3_sitearch}/MySQLdb/constants/__pycache__/*.pyc
%{python3_sitearch}/mysqlclient-%{version}-py3.*.egg-info

%if %{with python3_debug}
%files -n python3-mysql-debug
%{python3_sitearch}/MySQLdb/_mysql.cpython-%{python3_version_nodots}d-*.so
%endif # with debug

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.6-13
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.6-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.6-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.4.6-5
- Do not put debug version into the main package

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Michal Schorm <mschorm@redhat.com> - 1.4.6-1
- Rebase to 1.4.6

* Mon Nov 11 2019 Michal Schorm <mschorm@redhat.com> - 1.4.5-2
- Remove Python2 specific code

* Thu Nov 07 2019 Michal Schorm <mschorm@redhat.com> - 1.4.5-1
- Rebase to 1.4.5

* Thu Nov 07 2019 Michal Schorm <mschorm@redhat.com> - 1.4.4-1
- Rebase to 1.4.4

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.14-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Michal Schorm <mschorm@redhat.com> - 1.3.14-1
- Rebase to 1.3.14

* Mon Aug 26 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.13-5
- Drop python2-mysql-debug

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.13-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Michal Schorm <mschorm@redhat.com> - 1.3.13-1
- Rebase to 1.3.13

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.12-5
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.12-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 1.3.12-2
- build using mariadb-connector-c-devel instead of mysql-devel

* Sat Sep  2 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 1.3.12-4
- Update to 1.3.12

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Adam Williamson <awilliam@redhat.com> - 1.3.10-2
- Fix build with MariaDB 10.2 (patch backported from upstream master)

* Tue Mar  7 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 1.3.10-1
- Update to 1.3.10

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
