%global srcname pudb

Name:          python-pudb
Version:       2024.1.3
Release:       2%{?dist}
Summary:       A full-screen, console-based Python debugger
License:       MIT
URL:           https://github.com/inducer/pudb
Source0:       %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-pytest-mock
BuildRequires: pyproject-rpm-macros

%global _description %{expand:
PuDB is a full-screen, console-based visual debugger for Python.

Its goal is to provide all the niceties of modern GUI-based debuggers in a more
lightweight and keyboard-friendly package. PuDB allows you to debug code right
where you write and test it--in a terminal. If you've worked with the excellent
(but nowadays ancient) DOS-based Turbo Pascal or C tools, PuDB's UI might look
familiar.}

%description %_description

%package -n python3-%{srcname}
Summary:       A full-screen, console-based Python debugger
%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

sed -i '1{\@^#! /usr/bin/env python@d}' pudb/debugger.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/pudb

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Lumír Balhar <lbalhar@redhat.com> - 2024.1.3-1
- Update to 2024.1.3 (rhbz#2319825)

* Mon Jul 22 2024 Lumír Balhar <lbalhar@redhat.com> - 2024.1.2-1
- Update to 2024.1.2 (rhbz#2299348)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Lumír Balhar <lbalhar@redhat.com> - 2024.1.1-1
- Update to 2024.1.1 (rhbz#2297894)

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2024.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Lumír Balhar <lbalhar@redhat.com> - 2024.1-1
- Update to 2024.1 (rhbz#2258664)

* Fri Oct 06 2023 Lumír Balhar <lbalhar@redhat.com> - 2023.1-1
- Update to 2023.1 (rhbz#2242541)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2022.1.3-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Lumír Balhar <lbalhar@redhat.com> - 2022.1.3-1
- Update to 2022.1.3
Resolves: rhbz#2139902

* Sun Aug 14 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 2022.1.2-2
- Cleaned up specfile

* Fri Jul 29 2022 Lumír Balhar <lbalhar@redhat.com> - 2022.1.2-1
- Update to 2022.1.2 and fix FTBFS
  Resolves: rhbz#2063449

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2022.1.1-2
- Rebuilt for Python 3.11

* Mon Mar 14 2022 Lumír Balhar <lbalhar@redhat.com> - 2022.1.1-1
- Update to 2022.1.1
  Resolves: rhbz#2063449

* Mon Jan 17 2022 Lumír Balhar <lbalhar@redhat.com> - 2022.1-1
- Update to 2022.1
  Resolves: rhbz#2018390

* Wed Oct 06 2021 Lumír Balhar <lbalhar@redhat.com> - 2021.1-1
- Update to 2021.1
  Resolves: rhbz#1582173

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2017.1.4-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2017.1.4-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2017.1.4-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2017.1.4-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Miro Hrončok <mhroncok@redhat.com> - 2017.1.4-5
- Removed python2-pudb (#1701957)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2017.1.4-2
- Rebuilt for Python 3.7

* Mon Mar 19 2018 Neal Gompa <ngompa13@gmail.com> - 2017.1.4-1
- Rebase to pudb-2017.1.4
- Clean up spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2015.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2015.3-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2015.3-8
- Python 2 binary package renamed to python2-pudb
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 14 2015 Dhiru Kholia <dhiru@openwall.com> - 2015.3-1
- update to pudb-2015.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2014.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Mar 15 2014 Dhiru Kholia <dhiru@openwall.com> - 2014.1-1
- update to pudb-2014.1

* Mon Dec 09 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.5.1-1
- update to pudb-2013.5.1

* Wed Nov 13 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.4-1
- update to pudb-2013.4

* Tue Sep 10 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.6-2
- replaced {python_sitelib} with {python2_sitelib}

* Fri Sep 06 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.6-1
- update to upstream release 2013.3.6

* Fri Sep 06 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.5-5
- replaced {__python} with {__python2}

* Thu Sep 05 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.5-4
- make layout of install section consistent with that of build section

* Thu Sep 05 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.5-3
- removed the unnecessary attr directive
- fixed the location of the sed command invocation

* Thu Sep 05 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.5-2
- implemented initial fixes suggested in BZ #1004257
- removed unused EL5 support, removed invalid BuildRoot, fixed BuildRequires

* Wed Sep 04 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.5-1
- initial version
