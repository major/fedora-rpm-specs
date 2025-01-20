%global srcname pyngus
%global commit 60b6f102e4dc2d976292aa974866c4acce492e27
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20200513

Name:          python-%{srcname}
# Uses the snapshot because the upstream does not provides the latest version from git.
# Please see: https://github.com/kgiusti/pyngus/issues/14
Version:       2.3.0^%{snapshotdate}git%{shortcommit}
Release:       7.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:       Callback API implemented over Proton

License:       Apache-2.0
URL:           https://github.com/kgiusti/%{srcname}
# Uses the commit because the upstream does not provides the latest version from git.
# Please see: https://github.com/kgiusti/pyngus/issues/14
Source:  https://github.com/kgiusti/pyngus/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz 

BuildArch:     noarch
BuildRequires: python3-devel
# Please see: https://bugzilla.redhat.com/show_bug.cgi?id=2245641
BuildRequires: python3dist(legacy-cgi)

# Explicitly requires.
Requires: python3dist(qpid-proton)

%global _description \
A connection oriented messaging framework using QPID Proton.\
It provides a callback-based API for message passing.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{commit} 

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%py3_shebang_fix setup.py
%pyproject_install
%py3_shebang_fix tests/test-runner tests/perf-test.py setup.py examples/perf-tool.py examples/rpc-server.py examples/server.py examples/send.py examples/recv.py examples/rpc-client.py

%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
%py3_test_envvars PYTHONPATH=%{buildroot}:%{buildroot}/tests
PYTHONPATH=.:tests tests/test-runner -i "unit_tests.connection.CyrusTest.test_cyrus_sasl_ok" -i "unit_tests.connection.CyrusTest.test_cyrus_sasl_fail"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0^20200513git60b6f10-7.20200513git60b6f10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0^20200513git60b6f10-6.20200513git60b6f10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.3.0^20200513git60b6f10-5.20200513git60b6f10
- Requires legacy-cgi as build dependency (Fedora#2245641)
- Removes python3-cgi dependency ad runtime

* Wed Jun 19 2024 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.3.0^20200513git60b6f10-4.20200513git60b6f10
- Explicitly require python3-cgi and qpid-proton at runtime

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.3.0^20200513git60b6f10-3.20200513git60b6f10
- Rebuilt for Python 3.13

* Fri Apr 12 2024 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.3.0-2.20200513git60b6f10
- Fixes the Source URL

* Sat Mar 30 2024 Hirotaka Wakabayashi <hiwkby@yahoo.com> - 2.3.0-1.20200513git60b6f10
- Untretire python-pyngus
- Updates python-pyngus

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Python Maint <python-maint@redhat.com> - 2.3.0-15
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Irina Boverman <iboverma@redhat.com> - 2.3.0-1
- Rebased to 2.3.0

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-4
- Subpackage python2-pyngus has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 Irina Boverman <iboverma@redhat.com> - 2.2.4-2
- Added python2-pyngus

* Tue Jul 24 2018 Irina Boverman <iboverma@redhat.com> - 2.2.4-1
- Rebased to 2.2.4
- Removed python2-pyngus

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-2
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Irina Boverman <iboverma@redhat.com> - 2.2.2-1
- Rebased to 2.2.2

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Irina Boverman <iboverma@redhat.com> - 2.2.1-3
- Rebuilt against qpid-proton 0.18.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Irina Boverman <iboverma@redhat.com> - 2.2.1-1
- Rebased to 2.2.1

* Mon Feb 20 2017 Irina Boverman <iboverma@redhat.com> - 2.1.4-1
- Rebased to 2.1.4
- Rebuilt against qpid-proton 0.17.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-3
- Rebuild for Python 3.6

* Thu Sep  8 2016 Irina Boverman <iboverma@redhat.com> - 2.1.2-2
- Rebuilt against qpid-proton 0.14.0

* Thu Sep 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Thu Sep 01 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Tue Aug  9 2016 Irina Boverman <iboverma@redhat.com> - 2.0.4-1
- Rebased to 2.0.4
- Rebuilt against proton 0.13.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 24 2016 Irina Boverman <iboverma@redhat.com> - 2.0.3-5
- Rebuilt against qpid-proton 0.13.0

* Mon May 16 2016 Philip Worrall <philip.worrall@googlemail.com> - 2.0.3-4
- Add python3 subpackage (http://fedora.portingdb.xyz/pkg/python-pyngus/)
- Edit spec to use the python2/3 specific installation macros
- Add global macros for package name and summary
- Add calls to run the testsuite
- Point the source url at the upstream github repository (for license files)

* Wed Mar 23 2016 Irina Boverman <iboverma@redhat.com> - 2.0.3-3
- Rebuilt against qpid-proton 0.12.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Irina Boverman <iboverma@redhat.com> - 2.0.3-1
- Rebased to 2.0.3

* Thu Sep  3 2015 Irina Boverman <iboverma@redhat.com> - 2.0.1-1
- Rebased to 2.0.1
- Rebuilt against proton 0.10

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Darryl L. Pierce <dpierce@redhat.com> - 1.2.0-1
- Rebased on Pyngus 1.2.0.

* Wed Oct  1 2014 Darryl L. Pierce <dpierce@redhat.com> - 1.1.0-1
- First official build.

* Mon Sep 29 2014 Darryl L. Pierce <dpierce@redhat.com> - 1.1.0-0.1
- Replaced the python-qpid-proton requirement.
- Added egg info to the list of docs for this package.

* Thu Sep 25 2014 Darryl L. Pierce <dpierce@redhat.com> - 1.1.0-0
- Initial build.
