%global archive_name ansible-lint
%global lib_name ansiblelint

Name:           %{archive_name}
Epoch:          1
Version:        25.7.0
Release:        1%{?dist}
Summary:        Best practices checker for Ansible

# README file says its just GPLv3
License:        GPL-3.0-only
URL:            https://github.com/ansible/ansible-lint
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{archive_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:	pyproject-rpm-macros
# for check section
BuildRequires:  python3dist(pytest)

%description
Checks playbooks for practices and behavior that could potentially be improved.

%package -n python3-%{archive_name}
Summary:        %{summary}
Obsoletes:      python2-%{archive_name} < 3.4.23-6
Provides:       %{archive_name} = %{version}-%{release}

# Finally fixing this https://bugzilla.redhat.com/show_bug.cgi?id=1949362
Requires:       /usr/bin/ansible

%description  -n python3-%{archive_name}
Python3 module for ansible-lint.

%prep
%autosetup -n %{archive_name}-%{version}

# There's nothing special in setuptools 63.0 that's needed here.
# Fedora 36's setuptools version is actually too old;
# it does not support PEP 621.
%if %{defined fc37}
sed 's|setuptools >= 63.0.0|setuptools >= 62.0.0|' -i pyproject.toml
grep -F 'setuptools >= 62.0.0' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# On newer releases, which only have Python 3, you will get:
#   ansible-lint => Python 3
#   ansible-lint-3 => Python 3 (to avoid breaking anyone's scripts)
ln -sr %{buildroot}%{_bindir}/%{name}{,-3}
%pyproject_save_files %{lib_name}

%check
%pyproject_check_import

%files -n python3-%{archive_name} -f %{pyproject_files}
%doc README.md examples
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-3

%changelog
* Thu Jul 31 2025 Parag Nemade <pnemade AT redhat DOT com> - 1:25.7.0-1
- Update to 25.7.0 version (#2384332)

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:25.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jun 11 2025 Python Maint <python-maint@redhat.com> - 1:25.5.0-2
- Rebuilt for Python 3.14

* Wed May 28 2025 Parag Nemade <pnemade AT redhat DOT com> - 1:25.5.0-1
- Update to 25.5.0 version (#2368544)

* Tue Apr 29 2025 Parag Nemade <pnemade AT redhat DOT com> - 1:25.4.0-1
- Update to 25.4.0 version (#2362691)

* Fri Apr 04 2025 Parag Nemade <pnemade AT redhat DOT com> - 1:25.2.1-1
- Update to 25.2.1 version (#2356936)

* Thu Feb 20 2025 Parag Nemade <pnemade AT redhat DOT com> - 1:25.1.3-1
- Update to 25.1.3 version (#2346298)

* Sat Feb 08 2025 Parag Nemade <pnemade AT redhat DOT com> - 1:25.1.2-1
- Update to 25.1.2 version (#2342561)

* Tue Jan 21 2025 Parag Nemade <pnemade AT redhat DOT com> - 1:25.1.0-1
- Update to 25.1.0 version (#2339029)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 15 2024 Parag Nemade <pnemade AT redhat DOT com> - 1:24.12.2-1
- Update to 24.12.2 version (#2331387)

* Fri Nov 15 2024 Parag Nemade <pnemade AT redhat DOT com> - 1:24.10.0-1
- Update to 24.10.0 version (#2326168)

* Wed Sep 25 2024 Parag Nemade <pnemade AT redhat DOT com> - 1:24.9.2-1
- Update to 24.9.2 version (#2313862)

* Mon Sep 16 2024 Parag Nemade <pnemade AT redhat DOT com> - 1:24.9.0-1
- Update to 24.9.0 version (#2277993)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 13 2024 Parag Nemade <pnemade AT redhat DOT com> - 1:24.7.0-1
- Update to 24.7.0 version (#2277993)

* Wed Jul 10 2024 Python Maint <python-maint@redhat.com> - 1:24.2.2-2
- Rebuilt for Python 3.13

* Wed Apr 10 2024 Parag Nemade <pnemade AT redhat DOT com> - 1:24.2.2-1
- Update to 24.2.2 version (#2274219)

* Thu Mar 14 2024 Parag Nemade <pnemade AT redhat DOT com> - 1:24.2.1-1
- Update to 24.2.1 version (#2269495)

* Thu Feb 08 2024 Parag Nemade <pnemade AT redhat DOT com> - 1:24.2.0-1
- Update to 24.2.0 version (#2263278)

* Tue Feb 06 2024 Parag Nemade <pnemade AT redhat DOT com> - 1:6.22.2-2
- Remove the relaxed requests module requirement from %%prep section

* Fri Feb 02 2024 Parag Nemade <pnemade AT redhat DOT com> - 1:6.22.2-1
- Update to 6.22.2 version (#2259057)

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.22.1-1
- Update to 6.22.1 version (#2252310)

* Sun Nov 12 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.22.0-1
- Update to 6.22.0 version (#2245219)

* Sun Oct 08 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.20.3-1
- Update to 6.20.3 version (#2239869)

* Thu Sep 07 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.19.0-1
- Update to 6.19.0 version (#2237822)

* Tue Aug 22 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.18.0-1
- Update to 6.18.0 version (#2233333)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.17.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Python Maint <python-maint@redhat.com> - 1:6.17.2-2
- Rebuilt for Python 3.12

* Fri Jun 23 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.17.2-1
- Update to 6.17.2 version (#2216901)

* Fri Jun 16 2023 Maxwell G <maxwell@gtmx.me> - 1:6.17.1-1
- Update to 6.17.1. Fixes rhbz#2211403.

* Tue May 30 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.16.2-1
- Update to 6.16.2 version (#2207538)

* Wed May 10 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.16.0-1
- Update to 6.16.0 version (#2196454)

* Fri Apr 28 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.15.0-1
- Update to 6.15.0 version (#2183982)

* Wed Mar 29 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.14.3-1
- Update to 6.14.3 version (#2181582)

* Mon Mar 20 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.14.2-1
- Update to 6.14.2 version (#2176343)

* Tue Mar 07 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.14.0-1
- Update to 6.14.0 version (#2175372)

* Wed Feb 22 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.13.1-1
- Update to 6.13.1 version (#2170117)

* Sun Feb 12 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.12.2-1
- Update to 6.12.2 version (#2166418)

* Mon Jan 23 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.11.0-1
- Update to 6.11.0 version (#2161931)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.10.2-1
- Update to 6.10.2 version (#2157933)

* Mon Jan 02 2023 Parag Nemade <pnemade AT redhat DOT com> - 1:6.10.1-1
- Update to 6.10.1 version (#2157189)

* Wed Dec 14 2022 Maxwell G <gotmax@e.email> - 1:6.10.0-1
- Update to 6.10.0.

* Sun Dec 04 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.9.1-1
- Update to 6.9.1 version (#2147469)

* Tue Nov 22 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.8.7-1
- Update to 6.8.7 version (#2144357)

* Thu Nov 10 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.8.6-1
- Update to 6.8.6 version (#2138333)

* Thu Oct 27 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.8.3-1
- Update to 6.8.3 version (#2138029)

* Sat Oct 15 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.8.2-1
- Update to 6.8.2 version (#2134594)

* Tue Oct 11 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.8.1-1
- Update to 6.8.1 version (#2133564)

* Sun Sep 25 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.7.0-1
- Update to 6.7.0 version (#2129457)

* Wed Sep 21 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.6.1-1
- Update to 6.6.1 version (#2128027)

* Fri Sep 02 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.5.2-1
- Update to 6.5.2 version (#2123638)

* Fri Aug 26 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.5.1-1
- Update to 6.5.1 version (#2121398)

* Thu Aug 25 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.5.0-2
- Add explicit BR: python3-pytest
- change license to use SPDX format

* Tue Aug 23 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.5.0-1
- Update to 6.5.0 version (#2120214)

* Mon Aug 01 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.4.0-1
- Update to 6.4.0 version (#2111880)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.3.0-2
- Drop lowering of jsonschema requirement
- add minimal %%check to ensure to catch newly added requirements

* Fri Jun 17 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.3.0-1
- Update to 6.3.0 version (#2095420)

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1:6.2.2-2
- Rebuilt for Python 3.11

* Tue May 31 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.2.2-1
- Update to 6.2.2 version (#2091576)

* Fri May 13 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.1.0-1
- Update to 6.1.0 version (#2083644)
- Requires: /usr/bin/ansible (#1949362)

* Mon Mar 28 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.0.2-1
- Update to 6.0.2 version (#2067984)

* Wed Mar 23 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:6.0.1-1
- Update to 6.0.1 version (#2065857)
- License changed from MIT to GPLv3

* Sun Feb 13 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:5.4.0-1
- Update to 5.4.0 version (#2053887)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Parag Nemade <pnemade AT redhat DOT com> - 1:5.3.2-1
- Update to 5.3.2 version (#2039168)

* Mon Dec 13 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.3.1-1
- Update to 5.3.1 version (#2030304)

* Mon Dec 06 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.3.0-1
- Update to 5.3.0 version (#2028259)

* Wed Oct 20 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.2.1-1
- Update to 5.2.1 version (#2015831)

* Fri Oct 01 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.2.0-1
- Update to 5.2.0 version (#2009767)

* Thu Sep 02 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.1.3-1
- Update to 5.1.3 version (#1999888)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.1.2-1
- Update to 5.1.2 version (#1983170)

* Tue Jun 08 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.0.12-1
- Update to 5.0.12 version (#1967909)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:5.0.11-2
- Rebuilt for Python 3.10

* Fri May 28 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.0.11-1
- Update to 5.0.11 version (#1963877)

* Fri May 21 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.0.10-1
- Update to 5.0.10 version (#1963149)

* Fri May 21 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.0.9-1
- Update to 5.0.9 version (#1962218)

* Tue May 04 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.0.8-1
- Update to 5.0.8 version (#1956328)

* Wed Apr 07 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.0.7-1
- Update to 5.0.7 version (#1947042)

* Thu Mar 25 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.0.6-1
- Update to 5.0.6 version (#1942976)

* Tue Mar 23 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.0.4-1
- Update to 5.0.4 version (#1940710)

* Thu Mar 18 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.0.2-1
- Update to 5.0.2 version (#1913796)

* Thu Feb 18 2021 Parag Nemade <pnemade AT redhat DOT com> - 1:5.0.1-1
- Update to 5.0.1 version (#1913796)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 09:45:28 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 1:4.3.7-1
- Update to 4.3.7 version (#1894320)

* Sun Nov  1 08:13:14 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 1:4.3.6-1
- Update to 4.3.6 version (#1893489)

* Sat Sep 19 11:10:37 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 1:4.3.5-1
- Update to 4.3.5 version (#1880470)

* Wed Sep  2 07:01:22 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 1:4.3.4-1
- Update to 4.3.4 version (#1874590)

* Fri Aug 28 2020 Parag Nemade <pnemade AT redhat DOT com> - 1:4.3.3-1
- Update to 4.3.3 version (#1872628)

* Fri Aug 21 2020 Parag Nemade <pnemade AT redhat DOT com> - 1:4.3.1-1
- Update to 4.3.1 version (#1821916)

* Thu Aug 20 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1:4.3.0-1
- Update to 4.3.0

* Mon Aug 03 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1:4.2.0-6
- Bump epoch to fix upgradepath

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-4
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Parag Nemade <pnemade AT redhat DOT com> - 4.2.0-3
- Update to 4.2.0 GA release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0a1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Parag Nemade <pnemade AT redhat DOT com> - 4.2.0a1-1
- Update to 4.2.0a1 version (#1776487)

* Tue Nov 12 2019 Parag Nemade <pnemade AT redhat DOT com> - 4.1.1a5-1
- Update to 4.1.1a5 version (#1771098)

* Tue Nov 05 2019 Parag Nemade <pnemade AT redhat DOT com> - 4.1.1a3-2
- Fix test run in %%check

* Tue Nov 05 2019 Parag Nemade <pnemade AT redhat DOT com> - 4.1.1a3-1
- Update to 4.1.1a3 version (#1765630)

* Sat Nov 02 2019 Parag Nemade <pnemade AT redhat DOT com> - 4.1.1a0-4
- Fix dependency ansible-python3 to ansible

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.1a0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.1a0-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Parag Nemade <pnemade AT redhat DOT com> - 4.1.1a0-1
- Update to 4.1.1a0 version (#1742505)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Parag Nemade <pnemade AT redhat DOT com> - 4.1.0-1
- Update to 4.1.0 version (#1674307)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.4.23-7
- Add back Provides: ansible-lint

* Sun Oct 07 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.4.23-6
- Fix the upgrade path (rh#1634352)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.23-4
- Rebuilt for Python 3.7

* Mon Jun 25 2018 Dan Callaghan <dcallagh@redhat.com> - 3.4.23-3
- python3-ansible-lint conflicts with python2-ansible-lint because
  /usr/bin/ansible-lint moved between subpackages

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.23-2
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.4.23-1
- Update to 3.4.23 version (#1592159)

* Sun Jun 17 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.4.22-1
- Update to 3.4.22 version (#1559645)

* Tue Apr 03 2018 Dan Callaghan <dcallagh@redhat.com> - 3.4.21-2
- no longer building Python 2 bits in releases which have dropped Python 2
- added missing requirements on PyYAML and six

* Wed Mar 14 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.4.21-1
- Update to 3.4.21 version (#1555095)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.20-1
- Update to 3.4.20 version (#1528085)

* Thu Dec 14 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.19-3
- Fix the test/TestCommandLineInvocationSameAsConfig.py execution for python3

* Wed Dec 13 2017 Jan Beran <jberan@redhat.com> - 3.4.19-2
- Python 2 binary package renamed to python2-ansible-lint
- Python 3 subpackage

* Mon Dec 11 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.19-1
- Update to 3.4.19 version (#1524156)

* Sun Oct 22 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.17-1
- Update to 3.4.17 version (#1505124)

* Tue Oct 03 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.16-1
- Update to 3.4.16 version (#1497872)

* Sat Sep 02 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.15-1
- Update to 3.4.15 version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.13-1
- Update to 3.4.13 version

* Mon Mar 20 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.12-1
- Update to 3.4.12 version

* Mon Feb 13 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.11-1
- Update to 3.4.11

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.10-1
- Update to 3.4.10

* Thu Dec 22 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.9-1
- Update to 3.4.9

* Fri Dec 16 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.8-1
- Update to 3.4.8

* Mon Dec 05 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.7-1
- Update to 3.4.7

* Tue Nov 15 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.4-1
- Update to 3.4.4

* Tue Nov 08 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.3-1
- Update to 3.4.3

* Fri Oct 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.1-1
- Update to 3.4.1

* Fri Sep 30 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.3.3-1
- Update to 3.3.3

* Fri Sep 30 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.3.2-1
- Update to 3.3.2

* Thu Jul 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.5-1
- Update to 3.2.5

* Thu Jul 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.4-1
- Update to 3.2.4

* Wed Jul 27 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.1-1
- Upstream release 3.2.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 18 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.0-1
- Upstream release 3.2.0

* Fri Jul 15 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.3-1
- Upstream release 3.1.3

* Thu Jul 07 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.2-1
- Upstream release 3.1.2

* Thu Jun 30 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.1-1
- Upstream release 3.1.1

* Wed Jun 29 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.0-1
- Upstream release 3.1.0

* Fri Jun 24 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-2
- Fixed typo in previous changelog entry

* Fri Jun 24 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-1
- Update to 3.0.1 release

* Thu Jun 23 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0.0-1
- Update to 3.0.0 release

* Tue May 10 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.6.2-1
- Update to 2.6.2 release

* Sat Mar 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.4.1-1
- Update to 2.4.1 release

* Wed Mar 16 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.4.0-1
- Update to 2.4.0 release

* Thu Mar 03 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.9-1
- Update to 2.3.9 release

* Fri Feb 26 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.8-1
- Update to 2.3.8 release

* Sat Feb 06 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.5-1
- Update to 2.3.5 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.3-1
- Update to 2.3.3 release

* Fri Jan 15 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.1-1
- Update to 2.3.1 release

* Fri Jan 15 2016 Parag Nemade <pnemade AT redhat DOT com> - 2.3.0-1
- Update to 2.3.0 release

* Mon Dec 21 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.2.0-1
- Update to 2.2.0

* Tue Nov 24 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.1.0-1
- Update to 2.1.0

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 08 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.0.3-1
- Update to 2.0.3

* Fri Dec 05 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.1-1
- Update to 2.0.1

* Mon Oct 27 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.4-1
- rename to ansible-lint
- new upstream 1.0.4 release which added LICENSE file.

* Sat Oct 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-2
- Better add upstream LICENSE file, not present in tarball

* Wed Sep 24 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-1
- Initial packaging

