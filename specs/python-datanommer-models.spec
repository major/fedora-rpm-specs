%global modname datanommer.models
%global pkgname datanommer-models
%global pypi_version 1.0.4

Name:           python-%{pkgname}
Version:        %{pypi_version}
Release:        5%{?dist}
Summary:        SQLAlchemy data model for datanommer

License:        GPLv3+
URL:            https://github.com/fedora-infra/datanommer
Source0:        %{pypi_source %{modname}}

BuildArch:      noarch

%description
SQLAlchemy models for datanommer.

%package -n python3-%{pkgname}
Summary: %summary

%py_provides python3-%{pkgname}

# datanommer-config is no longer a subpackage
Obsoletes:      datanommer-config < 1.0.0

BuildRequires:  libpq-devel
BuildRequires:  postgresql-server
BuildRequires:  python-pytest-postgresql
BuildRequires:  python3-bodhi-messages
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-setuptools
BuildRequires:  timescaledb

%description -n python3-%{pkgname}
SQLAlchemy models for datanommer.

%prep
%autosetup -n %{modname}-%{pypi_version}

# Remove upstream egg-info so that it gets rebuilt.
rm -rf *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files datanommer

# DB upgrade/downgrade scripts
%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{pkgname}

install -m 644 alembic.ini %{buildroot}%{_sysconfdir}/%{pkgname}/alembic.ini

%check
%pyproject_check_import -e datanommer.models.alembic.env
%{pytest} -v

%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%config(noreplace) %{_sysconfdir}/%{pkgname}/alembic.ini

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Lenka Segura <lsegura@redhat.com> - 1.0.4-3
- Fix upgrade path from 0.9.1

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.0.4-2
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.1-15
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-7
- Subpackage python2-datanommer-models has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-4
- Rebuilt for Python 3.7

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.9.1-3
- Copy namespace file explicitly for python3.

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.9.1-2
- Python3 subpackage.

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.9.1-1
- new version

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.0-2
- Python 2 binary package renamed to python2-datanommer-models
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Tue Dec 12 2017 Ralph Bean <rbean@redhat.com> - 0.9.0-1
- new version

* Wed Oct 04 2017 Ralph Bean <rbean@redhat.com> - 0.8.2-1
- new version

* Fri Aug 11 2017 Ralph Bean <rbean@redhat.com> - 0.8.1-1
- new version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Ralph Bean <rbean@redhat.com> - 0.8.0-1
- new version

* Fri Mar 03 2017 Ralph Bean <rbean@redhat.com> - 0.7.0-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Ralph Bean <rbean@redhat.com> - 0.6.5-2
- Fix rhel conditional again..

* Mon Mar 16 2015 Ralph Bean <rbean@redhat.com> - 0.6.5-1
- new version

* Wed Jul 09 2014 Ralph Bean <rbean@redhat.com> - 0.6.4-2
- Fix rhel conditional for epel7.

* Tue Jun 10 2014 Ralph Bean <rbean@redhat.com> - 0.6.4-1
- Latest upstream with a bugfix to the optimized inserts stuff.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Ralph Bean <rbean@redhat.com> - 0.6.3-1
- Optimized inserts.

* Fri Feb 21 2014 Ralph Bean <rbean@redhat.com> - 0.6.1-2
- Added a new test dependency on python-fedmsg-meta-fedora-infrastructure

* Fri Feb 21 2014 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- Expanded Message.grep API.

* Wed Sep 11 2013 Ian Weller <iweller@redhat.com> - 0.6.0-2
- Modernize old git messages
- Handle UUIDs/msg_ids from fedmsg

* Mon Aug 26 2013 Ralph Bean <rbean@redhat.com> - 0.5.0-2
- Disable the consumer by default.
- Use an in-memory database by default.

* Mon Aug 12 2013 Ralph Bean <rbean@redhat.com> - 0.5.0-1
- Added source_name and source_version columns.
- Added possibility to disable paging in calls to .grep().

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Ralph Bean <rbean@redhat.com> - 0.4.6-1
- Latest upstream.
- Added optional "defer" argument to the `grep` method.

* Thu May 16 2013 Ralph Bean <rbean@redhat.com> - 0.4.5-1
- Fix links to upstream source.
- Allow queries to 'grep' with no timespan.

* Tue May 14 2013 Ralph Bean <rbean@redhat.com> - 0.4.4-1
- Added an 'order' argument to the 'grep' method.

* Mon Apr 22 2013 Ralph Bean <rbean@redhat.com> - 0.4.3-1
- Bugfixes to category assignment.
- New convenience classmethods on Message, User, and Package.
- Removed old BuildRequires on bunch, argparse, and orderedict.

* Thu Feb 14 2013 Ralph Bean <rbean@redhat.com> - 0.4.2-1
- Latest upstream with improved alembic migration.

* Thu Feb 07 2013 Ralph Bean <rbean@redhat.com> - 0.4.1-1
- Latest upstream contributed by Jessica Anderson.
- Included alembic upgrade scripts in /usr/share/datanommer.models/

* Thu Nov 08 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-6
- Patch setup.py to pull in the correct sqlalchemy for el6.
- Add BR for python-argparse and python-ordereddict.

* Thu Nov 08 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-5
- Added temporary BR on python-bunch to get around an old moksha issue.

* Mon Oct 22 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-4
- Remove explicit versioned Conflicts with old datanommer.

* Fri Oct 12 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-3
- Remove unneccessary CFLAGS definition.

* Thu Oct 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-2
- Remove upstream egg-info so that its gets rebuilt.

* Thu Oct 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-1
- Initial split out from the main datanommer package.
