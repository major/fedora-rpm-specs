# Created by pyp2rpm-3.1.2
%global pypi_name pytest-spec
%global modname pytest_spec
%global desc Pytest plugin to display test execution output like a SPECIFICATION.\
Available features:\
- Format output to look like specification.\
- Group tests by classes and files\
- Failed, passed and skipped are marked and colored.\
- Remove test_ and underscores for every test.

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        2%{?dist}
Summary:        Pytest plugin to display test execution output like a SPECIFICATION

License:        GPL-2.0-or-later
URL:            https://github.com/pchomik/pytest-spec
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(mock)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
# Guidelines don't allow to run linting operations
rm -rf setup.cfg
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest -v test/*

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.txt README.md LICENSE.txt
%license LICENSE.txt

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 29 2024 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.0-1
- Update to latest upstream release (closes rhbz#2302747)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.0-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 3.2.0-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 3.2.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.2.0-1
- Update to new upstream version 3.2.0 (closes rhbz#1956337)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.10

* Fri Jan 15 2021 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.0-1
- Update to latest upstream release 3.1.0 (#1902396)

* Mon Nov 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.6-1
- Switch to pyproject macros
- Update to latest upstream release 3.0.6 (#1883030)

* Thu Oct 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.4-1
- Update to latest upstream release 3.0.4

* Wed Sep 23 2020 Lumír Balhar <lbalhar@redhat.com> - 3.0.0-1
- Update to 3.0.0 (#1881693)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Lumír Balhar <lbalhar@redhat.com> - 2.0.0-1
- New upstream version (#1784635)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Lumír Balhar <lbalhar@redhat.com> - 1.1.0-10
- Add a fix for [pytest] section name in setup.cfg

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Lumír Balhar <lbalhar@redhat.com> - 1.1.0-8
- Remove Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuild for Python 3.6

* Wed Dec 07 2016 Lumir Balhar <lbalhar@redhat.com> - 1.1.0-1
- New upstream release

* Wed Jul 20 2016 Lumir Balhar <lbalhar@redhat.com> - 1.0.1-1
- Initial package.
