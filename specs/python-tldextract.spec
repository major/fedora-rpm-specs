%global pypi_name tldextract

Name:           python-%{pypi_name}
Version:        5.1.3
Release:        2%{?dist}
Summary:        Accurately separate the TLD from the registered domain and subdomains of a URL

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/tldextract
Source0:        %{pypi_source %{pypi_name}}
# upstream uses setuptools_scm which picks up "tldextract/.tld_set_snapshot"
# as package data but the source tarball does not contain ".git" so "pip wheel"
# ignores the file by default.
# This patch declares the file as "package_data" explicitly.
# The code assumes this file is always present and uses it as a fallback.
Patch1:         python-tldextract-include-.tld_set_snapshot.patch

BuildArch:      noarch

BuildRequires:  python3-devel
# required for testing, pyproject.toml only contains a "testing" extra which
# contains many developer tools we do not need if we just want to run the test
# suite (e.g. mypy, ruff).
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-responses
BuildRequires:  python3-syrupy


%description
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

This is the Python 3 version of the package.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# test_log_snapshot_diff is an integration test and requires network access
# (additionally that test requires python3-pytest-mock which is not available
# in EPEL 7)
TEST_SELECTOR="not test_log_snapshot_diff"

%pytest -k "$TEST_SELECTOR"


%files -n python3-%{pypi_name} -f %{pyproject_files}
# "LICENSE" files is included in "pyproject_files"
%doc README.md
%{_bindir}/tldextract

%changelog
* Mon Jan 06 2025 Felix Schwarz <fschwarz@fedoraproject.org> - 5.1.3-2
- fix missing ".tld_set_snapshot" in RPM

* Sat Nov 23 2024 Ben Maconi <turboben@fedoraproject.org> - 5.1.3-1
- Update to 5.1.3

* Sat Aug 24 2024 Nick Bebout <nb@fedoraproject.org> - 5.1.2-1
- Update to 5.1.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.5.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 15 2023 Jonathan Wright <jonathan@almalinux.org> - 3.5.0-1
- Update to 3.5.0 rhbz#2237807

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 3.4.4-2
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Nick Bebout <nb@fedoraproject.org> - 3.4.4-1
- update to 3.4.4

* Thu Apr 27 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 3.4.1-1
- update to 3.4.1
- SPDX migration

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jonathan Wright <jonathan@almalinux.org> - 3.4.0-1
- update to 3.4.0 rhbz#2132165

* Tue Jul 26 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 3.3.1-1
- update to 3.3.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.2.1-2
- Rebuilt for Python 3.11

* Fri Apr 22 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 3.2.1-1
- update to 3.2.1

* Thu Mar 03 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 3.2.0-1
- update to 3.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 01 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 3.1.2-1
- update to 3.1.2

* Sat Aug 28 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 3.1.1-1
- update to 3.1.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.1.0-1
- update to 3.1.0

* Wed Nov 04 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.0.2-1
- update to 3.0.2

* Tue Aug 18 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.2.3-1
- update to 2.2.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-3
- Rebuilt for Python 3.9

* Sun May 17 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.2.2-2
- enable Python 3 tests for EPEL 7

* Tue Apr 28 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.2.2-1
- update to 2.2.2
- run tests in %%check
- add Python 3 subpackage in EPEL 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Eli Young <elyscape@gmail.com> - 2.2.1-5
- Support EPEL8 builds

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 Eli Young <elyscape@gmail.com> - 2.2.1-1
- Update to 2.2.1 (#1685688)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Eli Young <elyscape@gmail.com> - 2.2.0-5
- Remove Python 2 package in Fedora 30+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 2.2.0-2
- Add python2- prefix where possible

* Thu Feb 15 2018 Eli Young <elyscape@gmail.com> - 2.2.0-1
- Initial package (#1545951)
