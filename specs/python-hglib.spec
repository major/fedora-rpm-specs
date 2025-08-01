Summary:        Mercurial Python library
Name:           python-hglib
Version:        2.6.2
Release:        20%{?dist}
License:        MIT
URL:            http://selenic.com/repo/python-hglib
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch:          0001-hglib-tests-migrate-away-from-unmaintained-nose.patch
Patch:          0001-hglib-tests-remove-deprecated-constructions.patch
Patch:          0001-Use-raw-string-to-avoid-invalid-escape-sequence.patch
BuildArch:      noarch
BuildRequires:  mercurial
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
%description
python-hglib is a library with a fast, convenient interface to
Mercurial. It uses Mercurials command server for communication with
hg.

%package     -n python3-hglib
Summary:        Mercurial Python library
%{?python_provide:%python_provide python3-hglib}
%description -n python3-hglib
python-hglib is a library with a fast, convenient interface to
Mercurial. It uses Mercurials command server for communication with
hg.

%prep
%autosetup -p1

%build
%{py3_build}

%install
%{py3_install}

%check
%pytest

%files -n python3-hglib
%license LICENSE
%{python3_sitelib}/hglib
%{python3_sitelib}/python_hglib-*-py*egg-info

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 2.6.2-19
- Rebuilt for Python 3.14

* Sun Mar 30 2025 Terje Rosten <terjeros@gmail.com> - 2.6.2-18
- Lift some test fixes from https://foss.heptapod.net/mercurial/python-hglib

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 29 2024 Terje Rosten <terjeros@gmail.com> - 2.6.2-16
- Remove legacy Python 2 parts

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.6.2-14
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2.6.2-10
- Rebuilt for Python 3.12

* Wed May 03 2023 Terje Rosten <terje.rosten@ntnu.no> - 2.6.2-9
- Add patch to pass tests with Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.6.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Terje Rosten <terje.rosten@ntnu.no> - 2.6.2-1
- 2.6.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-11
- Rebuilt for Python 3.9

* Sat Feb 01 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.6.1-10
- Add mercurial 5.2 compat patch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.6.1-5
- Remove Python 2 subpackage on Fedora 31+ and el8+

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-2
- Rebuilt for Python 3.7

* Mon May 21 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.6.1-1
- 2.6.1

* Thu Apr 26 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.6-1
- 2.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.5-1
- 2.5

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.4-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.4-1
- 2.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.3-1
- 2.3

* Wed Dec 28 2016 Adam Williamson <awilliam@redhat.com> - 2.2-1
- 2.2 (should fix issue between tests and recent hg)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.0-1
- 2.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 03 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.9-1
- 1.9

* Wed Sep 02 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.8-1
- 1.8

* Sun Aug 02 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.7-1
- 1.7

* Wed Jun 24 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.6-2
- use license macro (bz #1231330)

* Fri Jun 12 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.6-1
- initial package
