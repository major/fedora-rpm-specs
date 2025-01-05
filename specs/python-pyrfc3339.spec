%global srcname pyrfc3339

Name:           python-pyrfc3339
Version:        2.0.1
Release:        1%{?dist}
Summary:        Generate and parse RFC 3339 timestamps

License:        MIT
URL:            https://pypi.python.org/pypi/pyRFC3339
Source0:        %{pypi_source}
# release tarballs do not contain unit tests (pyrfc3339/tests/tests.py)
# https://github.com/kurtraschke/pyRFC3339/blob/master/pyrfc3339/tests/test_all.py
# v2.0.1: git commit 53c2d1587d3a
Source1:        https://raw.githubusercontent.com/kurtraschke/pyRFC3339/53c2d1587d3aac1734ddd4d4006a815df2d80f36/pyrfc3339/tests/test_all.py

BuildArch:      noarch

BuildRequires:  python3-devel
# --- unit tests ---
# Specified manually because upstream release tarballs do not contain unit tests
BuildRequires:  python3-pytest

%description
This package contains a python library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.

%package     -n python3-pyrfc3339
Summary:        Generate and parse RFC 3339 timestamps
%{?python_provide:%python_provide python3-pyrfc3339}

%description -n python3-pyrfc3339
This package contains a Python 3 library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.

%generate_buildrequires
%pyproject_buildrequires


%prep
%autosetup -n %{srcname}-%{version} -N
cp -a %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyrfc3339

%check
%pytest -v test_all.py

%files -n python3-pyrfc3339 -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jan 03 2025 Felix Schwarz <fschwarz@fedoraproject.org> - 2.0.1-1
- update to 2.0.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1-19
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1-15
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1-12
- Rebuilt for Python 3.11

* Thu Apr 07 2022 Matthew Davis <fedoraproject@virtual.drop.net> - 1.1-11
- Converted tests from python-nose to pytest
- Removed Python 2 support
- Converted to pyproject macros

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1-5
- add python-setuptools to BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-4
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1-3
- also package+run unit tests
- build Python 3 subpackage also in EPEL 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Eli Young <elyscape@gmail.com> - 1.1-1
- Update to 1.1 (#1697425)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-12
- Subpackage python2-pyrfc3339 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 1.0-2
- epel7: Only build python2 package

* Tue Nov 10 2015 James Hogarth <james.hogarth@gmail.com>    - 1.0-1
- Add installed tests back as per review
- Update to new 1.0 PyPi release
- Add external license file
* Sun Nov 08 2015 James Hogarth <james.hogarth@gmail.com>    - 0.2-2
- Update to follow the python guidelines
* Wed Oct 28 2015 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2-1
- initial packaging
