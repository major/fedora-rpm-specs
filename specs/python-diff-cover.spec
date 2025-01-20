%global desc Diff coverage is the percentage of new or modified lines that are covered by \
tests. This provides a clear and achievable standard for code review: If you \
touch a line of code, that line should be covered. Code coverage is *every* \
developer's responsibility! \
\
The diff-cover command line tool compares an XML coverage report with the \
output of git diff. It then reports coverage information for lines in the \
diff.

Name:           python-diff-cover
Version:        9.2.0
Release:        2%{?dist}
BuildArch:      noarch

License:        Apache-2.0
Summary:        Automatically find diff lines that need test coverage
URL:            https://github.com/Bachmann1234/diff-cover
Source0:        %{url}/archive/v%{version}/diff-cover-%{version}.tar.gz

BuildRequires: help2man
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-pytest-mock
BuildRequires: python3-pytest-datadir

%description
%{desc}

%package -n python3-diff-cover
Summary:        %{summary}
Requires:       git

%description -n python3-diff-cover
%{desc}

%prep
%autosetup -n diff_cover-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'diff-cover %{version}' \
        -o %{buildroot}%{_mandir}/man1/diff-cover.1 \
        %{buildroot}%{_bindir}/diff-cover

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'diff-quality %{version}' \
        -o %{buildroot}%{_mandir}/man1/diff-quality.1 \
        %{buildroot}%{_bindir}/diff-quality
%pyproject_save_files diff_cover

%check
# disable code quality checker tests, but run the rest.
%pytest -k 'not TestDiffQualityIntegration and not TestFlake8QualityReporterTest'

%files -n python3-diff-cover -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_mandir}/man1/diff-cover.1*
%{_mandir}/man1/diff-quality.1*
%{_bindir}/diff-cover
%{_bindir}/diff-quality

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 24 2024 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 9.2.0-1
- Update to 9.2.0 (rhbz#2162160)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 7.3.2-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 7.3.2-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Maxwell G <maxwell@gtmx.me> - 7.3.2-4
- Remove unused python3-mock test dependency

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 7.3.2-2
- Rebuilt for Python 3.12

* Mon Mar 06 2023 Miro Hrončok <mhroncok@redhat.com> - 7.3.2-1
- Update to 7.3.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Kevin Fenzi <kevin@scrye.com> - 7.3.0-1
- Update to 7.3.0. Fixes rhbz#2068325

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Adam Williamson <awilliam@redhat.com> - 6.5.0-1
- Update to 6.5.0
- Backport PR #280 to fix tests with pygments 2.12.0

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 6.4.4-4
- Rebuilt for Python 3.11

* Mon Feb 07 2022 Karolina Surma <ksurma@redhat.com> - 6.4.2-3
- Fix failing Pygments test. Fixes rhbz#2042301

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Kevin Fenzi <kevin@scrye.com> - 6.4.4-1
- Update to 6.4.4. Fixes rhbz#2028707

* Sun Nov 28 2021 Kevin Fenzi <kevin@scrye.com> - 6.4.2-1
- Update to 6.4.2. Fixes rhbz#1973851
- Disable quality checker tests

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Karolina Surma <ksurma@redhat.com> - 5.2.0-1
- Update to 5.2.0 Fixes rhbz#1967026, rhbz#1958734

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.0.0-2
- Rebuilt for Python 3.10

* Tue Mar 09 2021 Charalampos Stratakis <cstratak@redhat.com> - 5.0.0-1
- Update to 5.0.0 Fixes rhbz#1918488, rhbz#1931521

* Mon Feb 22 2021 Kevin Fenzi <kevin@scrye.com> - 4.2.1-1
- Update to 4.2.1. Fixes rhbz#1918488

* Fri Feb 05 2021 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-2
- BuildRequire chardet >= 4
- Don't ignore errors during build

* Thu Jan 28 2021 Kevin Fenzi <kevin@scrye.com> - 4.2.0-1
- Update to 4.2.0. Fixed rhbz#1918488

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Kevin Fenzi <kevin@scrye.com> - 4.1.0-1
- Update to 4.1.0. Fixes rhbz#1914008

* Tue Dec 29 2020 Kevin Fenzi <kevin@scrye.com> - 4.0.1-1
- Update to 4.0.1. RHBZ#1898113
- Fix FTBFS RHBZ#1898113

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Clément Verna <cverna@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0 RHBZ#1821943
- https://github.com/Bachmann1234/diff_cover/blob/v3.0.0/CHANGELOG

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0 (#1800860).
- https://github.com/Bachmann1234/diff_cover/blob/v2.6.0/CHANGELOG

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2 (#1783722).
- https://github.com/Bachmann1234/diff_cover/blob/v2.5.2/CHANGELOG

* Thu Nov 21 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1 (#1774828).
- https://github.com/Bachmann1234/diff_cover/blob/v2.4.1/CHANGELOG

* Fri Nov 15 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0 (#1762995).
- https://github.com/Bachmann1234/diff_cover/blob/V2.4.0/CHANGELOG

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Kevin Fenzi <kevin@scrye.com> - 2.3.0-1
- Update to 2.3.0. Fixes bug #1725493

* Tue Jun 18 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0 (#1720455).
- https://github.com/Bachmann1234/diff-cover/blob/v2.2.0/CHANGELOG

* Tue Jun 04 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0 (#1697689).
- https://github.com/Bachmann1234/diff-cover/blob/v2.1.0/CHANGELOG

* Wed Apr 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7 (#1689572).
- https://github.com/Bachmann1234/diff-cover/blob/v1.0.7/CHANGELOG

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5.

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.12-5
- Subpackage python2-diff-cover has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.12-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
