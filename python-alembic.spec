Name:             python-alembic
Version:          1.8.1
Release:          3%{?dist}
Summary:          Database migration tool for SQLAlchemy

# SPDX
License:          MIT
URL:              https://pypi.io/project/alembic
Source0:          %{pypi_source alembic}

# Alembic fails with Python 3.10.0b2 due to DeprecationWarnings treated as an error.
# Downstream report: https://bugzilla.redhat.com/show_bug.cgi?id=1958159
Patch1:           0001-filter-out-DeprecationWarnings.patch

BuildArch:        noarch

BuildRequires:    help2man

BuildRequires:    python3-devel

%global _description %{expand:
Alembic is a database migrations tool written by the author of SQLAlchemy. A
migrations tool offers the following functionality:

• Can emit ALTER statements to a database in order to change the structure of
  tables and other constructs
• Provides a system whereby "migration scripts" may be constructed; each script
  indicates a particular series of steps that can "upgrade" a target database
  to a new version, and optionally a series of steps that can "downgrade"
  similarly, doing the same steps in reverse.
• Allows the scripts to execute in some sequential manner.

Documentation and status of Alembic is at https://alembic.sqlalchemy.org/}

%description %_description


%package -n python3-alembic
Summary:          %summary

%description -n python3-alembic %_description


%pyproject_extras_subpkg -n python3-alembic tz


%prep
%autosetup -p1 -n alembic-%{version}
# HTML documentation has bundled and pre-compiled/pre-minified JavaScript; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/JavaScript/.
rm -rvf docs/_static
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]]*(black|zimports))\b/# &/' tox.ini


%generate_buildrequires
%pyproject_buildrequires -t -x tz


%build
%pyproject_wheel

mkdir -p bin
echo '%{python3} -c "import alembic.config; alembic.config.main()" $*' > bin/alembic
chmod 0755 bin/alembic
help2man --version-string %{version} --no-info -s 1 bin/alembic > alembic.1


%install
install -d -m 0755 %{buildroot}%{_mandir}/man1

%pyproject_install
%pyproject_save_files alembic
mv %{buildroot}/%{_bindir}/alembic %{buildroot}/%{_bindir}/alembic-3
ln -s alembic-3 %{buildroot}/%{_bindir}/alembic-%{python3_version}
install -m 0644 alembic.1 %{buildroot}%{_mandir}/man1/alembic-3.1
ln -s alembic-3.1 %{buildroot}%{_mandir}/man1/alembic-%{python3_version}.1

ln -s alembic-%{python3_version} %{buildroot}/%{_bindir}/alembic
ln -s alembic-%{python3_version}.1 %{buildroot}%{_mandir}/man1/alembic.1


%check
%tox


%files -n python3-alembic -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with rpm -qL -p ...
%doc README.rst CHANGES
%{_bindir}/alembic
%{_mandir}/man1/alembic.1{,.*}
%{_bindir}/alembic-3
%{_mandir}/man1/alembic-3.1{,.*}
%{_bindir}/alembic-%{python3_version}
%{_mandir}/man1/alembic-%{python3_version}.1{,.*}


%changelog
* Sat Feb 04 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.8.1-3
- Drop conditionals for EPEL8 (which has setuptools too old for this version
  anyway)
- Drop obsolete spec file macros, and use appropriate newer ones
- Drop HTML documentation due to bundled/pre-minified JavaScript
- Confirm License is SPDX MIT
- Add metapackage for “tz” extra
- Port to pyproject-rpm-macros
- Stricter patterns to avoid listing man pages twice
- Update description text from upstream

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 29 2022 Kevin Fenzi <kevin@scrye.com> - 1.8.1-1
- Update to 1.8.1. Fixes rhbz#2092126

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.7.7-2
- Rebuilt for Python 3.11

* Sun May 29 2022 Kevin Fenzi <kevin@scrye.com> - 1.7.7-1
- Update to 1.7.7. Fixes rhbz#2049145

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 28 2021 Kevin Fenzi <kevin@scrye.com> - 1.7.5-1
- Update to 1.7.5. Fixes rhbz#2022454

* Sat Nov 06 2021 Kevin Fenzi <kevin@scrye.com> - 1.7.4-1
- Update to 1.7.4. Fixes rhbz#2011425

* Sat Sep 25 2021 Kevin Fenzi <kevin@scrye.com> - 1.7.3-1
- Update to 1.7.3. Fixes rhbz#2005403

* Fri Sep 17 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.7.1-3
- Drop redundant manually specified dependencies

* Thu Sep 16 2021 Joel Capitao <jcapitao@redhat.com> - 1.7.1-2
- Add the dist tag again

* Mon Sep 13 2021 Joel Capitao <jcapitao@redhat.com> - 1.7.1-1
- Update to 1.7.1. Fixes rhbz#1999176

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 12 2021 Kevin Fenzi <kevin@scrye.com> - 1.6.5-1
- Update to 1.6.5. Fixes rhbz#1964163

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.3-2
- Rebuilt for Python 3.10

* Sat May 22 2021 Kevin Fenzi <kevin@scrye.com> - 1.6.3-1
- Update to 1.6.3. Fixes rhbz#1957878

* Tue May 04 2021 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Update to 1.6.0. Fixes rhbz#1956482

* Sat Mar 27 2021 Kevin Fenzi <kevin@scrye.com> - 1.5.8-1
- Update to 1.5.8. Fixes rhbz#1935790

* Mon Feb 22 2021 Kevin Fenzi <kevin@scrye.com> - 1.5.5-1
- Update to 1.5.5. Fixes rhbz#1931142

* Fri Feb 12 2021 Kevin Fenzi <kevin@scrye.com> - 1.5.3-1
- Update to 1.5.3. Fixes rhbz#1922496

* Thu Jan 28 2021 Kevin Fenzi <kevin@scrye.com> - 1.5.0-1
- Update to 1.5.0. Fixes rhbz#1917596

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Joel Capitao <jcapitao@redhat.com> - 1.4.3-1
- Update to 1.4.3 (rhbz#1878203)

* Thu Aug 20 2020 Merlin Mathesius <mmathesi@redhat.com> - 1.4.2-5
- Correct macro usage to fix Rawhide and ELN FTBFS errors

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.9

* Sun Mar 22 2020 Carl George <carl@george.computer> - 1.4.2-1
- Latest upstream rhbz#1808866

* Wed Feb 19 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1784129).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.4.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1 (#1767518).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.3.1

* Fri Sep 27 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1 (#1754016).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.2.1

* Tue Sep 17 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.0-2
- Drop python2-alembic (#1751088).

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.0-1
- Upgrade to 1.1.0 (#1747053).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.1.0

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.11-3
- Rebuilt for Python 3.8

* Mon Jul 22 2019 Petr Viktorin <pviktori@redhat.com> - 1.0.11-2
- Make /usr/bin/alembic point to alembic-3 on Fedora 31+
  See https://fedoraproject.org/wiki/Changes/Python_means_Python3
- Avoid absolute symlinks
- Conditionalize the Python 2/Python 3 parts with bcond

* Sun Jun 30 2019 Kevin Fenzi <kevin@scrye.com> - 1.0.11-1
- Update to 1.0.11. Fixes bug #1723981

* Wed Jun 19 2019 Troy Dawson <tdawson@redhat.com> - 1.0.10-1.1
- Make python2 optional
- Do not build python2 on RHEL8

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10 (#1700050).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.0.10

* Thu Mar 28 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8 (#1685262).
- https://alembic.sqlalchemy.org/en/latest/changelog.html#change-1.0.8

* Tue Feb 05 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.0.7-1
- Update to 1.0.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-6
- Rebuilt for Python 3.7

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-5
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.7-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.9.7-3
- The python3-alembic package now provides only alembic-3 and alembic-3.y.
- The python2-alembic package now provides alembic, alembic-2, and alembic-2.y.

* Sat Jan 27 2018 Ralph Bean <rbean@redhat.com> - 0.9.7-2
- The python3-alembic package now provides the alembic executable.

* Thu Jan 18 2018 Ralph Bean <rbean@redhat.com> - 0.9.7-1
- new version
- New dependency on python-dateutil.
