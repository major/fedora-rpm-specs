%global pypi_name datanommer.commands

Name:           datanommer-commands
Version:        1.0.3
Release:        5%{?dist}
Summary:        Console commands for datanommer

License:        GPLv3+
URL:            https://github.com/fedora-infra/datanommer
Source0:        %{pypi_source %{pypi_name}}
# Fix pyproject.toml's definition of included files and modules
# https://github.com/fedora-infra/datanommer/pull/815
Patch0:         0001-Fix-included-files-rediffed.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-postgresql
BuildRequires:  python3-datanommer-models >= 1.0.0
BuildRequires:  python3-bodhi-messages
BuildRequires:  python3-psycopg2
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server
# commands uses some database testing fixtures from models, which need
# timescaledb installed to work properly
BuildRequires:  timescaledb

%description
Console commands for datanommer.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove upstream egg-info so that it gets rebuilt.
rm -rf *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files datanommer

%check
%pyproject_check_import
%{pytest} -v

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/datanommer-create-db
%{_bindir}/datanommer-dump
%{_bindir}/datanommer-latest
%{_bindir}/datanommer-stats


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 16 2022 Adam Williamson <awilliam@redhat.com> - 1.0.3-3
- Backport part of PR #815 to fix installed files, simplify spec

* Thu Sep 15 2022 Adam Williamson <awilliam@redhat.com>
- Add BuildRequires: timescaledb to fix build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Aurelien Bompard <abompard@fedoraproject.org> - 1.0.3-1
- Version 1.0.3

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.7.2-15
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.2-12
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-2
- Rebuilt for Python 3.7

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.7.2-1
- Convert to python3.

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.7.1-1
- new version

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Ralph Bean <rbean@redhat.com> - 0.7.0-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Ralph Bean <rbean@redhat.com> - 0.4.6-4
- Fix rhel conditionals again.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 16 2014 Ralph Bean <rbean@redhat.com> - 0.4.6-2
- Fix rhel conditionals.

* Mon Jun 09 2014 Ralph Bean <rbean@redhat.com> - 0.4.6-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Ralph Bean <rbean@redhat.com> - 0.4.5-1
- Fixes to unit tests for new fedmsg.
- Update links to upstream source.

* Mon Apr 22 2013 Ralph Bean <rbean@redhat.com> - 0.4.3-1
- More random bugfixes.

* Thu Feb 14 2013 Ralph Bean <rbean@redhat.com> - 0.4.2-1
- Latest upstream with a bugfix to datanommer-latest.

* Thu Feb 07 2013 Ralph Bean <rbean@redhat.com> - 0.4.1-1
- Latest upstream from Jessica Anderson.
- Various enhancements and bugfixes.
- New datanommer-latest command.
- Tests now require python-mock.
- New dep on fedmsg.meta Fedora Infrastructure plugin.

* Mon Oct 22 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-4
- Remove explicit versioned Conflicts with old datanommer.

* Fri Oct 12 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-3
- Remove unnecessary CFLAGS definition.

* Thu Oct 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-2
- Remove upstream egg-info so that its gets rebuilt.

* Thu Oct 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-1
- Initial split out from the main datanommer package.
