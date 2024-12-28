%global srcname astral

Name:           python-%{srcname}
Version:        3.2
Release:        7%{?dist}
Summary:        Calculations for the position of the sun and moon

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://astral.readthedocs.io
Source0:        https://github.com/sffjunkie/astral/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

# Remove spurious pytest-runner dependency from tox.ini
# https://github.com/sffjunkie/astral/pull/98
Patch:          https://github.com/sffjunkie/astral/pull/98.patch

%global _description %{expand:
astral is a Python module which calculates including:

- Times for various positions of the sun: dawn, sunrise, solar noon,
  sunset, dusk, solar elevation, solar azimuth and rahukaalam.
- The phase of the moon.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(freezegun)

%description -n python3-%{srcname}
astral is a Python module which calculates including:

- Times for various positions of the sun: dawn, sunrise, solar noon,
  sunset, dusk, solar elevation, solar azimuth and rahukaalam.
- The phase of the moon.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{srcname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%doc ReadMe.md
%license LICENSE

%changelog
* Tue Dec 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 3.2-7
- Remove spurious pytest-runner dependency from tox.ini

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 3.2-1
- Update to latest upstream release 3.2 (closes rhbz#2133094)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.2-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2-2
- Add python3-setuptools as BR

* Fri May 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2-1
- Update to new upstream version 2.2 (rhbz#1838169)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-2
- Rebuilt for Python 3.9

* Sat Feb 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1-1
- Update to new upstream version 2.1 (rhbz#1801223)

* Mon Feb 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.1-1
- Enable tests
- Update files section
- Update to new upstream version 2.0.1 (rhbz#1801223)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.1-5
- Stop BuildRequiring python2-pytz

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.10.1-1
- Update to latest upstream release 1.10.1

* Thu Jan 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.2-1
- Update to latest upstream release 1.9.2

* Tue Jan 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.1-1
- Update to latest upstream release 1.9.1

* Sat Jan 26 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.8-1
- Update to latest upstream release 1.8

* Thu Nov 01 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.1-1
- Update to latest upstream release 1.7.1

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.1-4
- Subpackage python2-astral has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-2
- Rebuilt for Python 3.7

* Fri May 04 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-1
- Update to latest upstream release 1.6.1 (rhbz#1574748)

* Fri Feb 23 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.6-1
- Update to latest upstream release 1.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-1
- Update to latest upstream release 1.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 12 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-1
- Update to latest upstream release 1.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 05 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.4-1
- Update to latest upstream release 1.3.4

* Sat Jan 21 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.3-1
- Update to latest upstream release 1.3.3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-3
- Rebuild for Python 3.6

* Mon Nov 21 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2-2
- Add license to py2 as well
- Update variable

* Mon Nov 21 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2-1
- Add license file
- Run test without third party interaction
- Update to latest upstream release 1.3.2

* Mon Nov 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.0-1
- Initial version
