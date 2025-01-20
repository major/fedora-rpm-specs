%global        pypi_name terminaltables
%global        commit 8020b8cb8ae859891a999620085d34c8d8bfe1a3
Summary:       Generate tables in terminals from list of strings
Name:          python-terminaltables
Version:       3.1.10
Release:       15%{?dist}
License:       MIT
URL:           https://github.com/matthewdeanmartin/terminaltables
Source0:       https://github.com/matthewdeanmartin/terminaltables/archive/%{commit}.tar.gz
Patch0:        python-terminaltables-reqs.patch
Patch1:        python-terminaltables-fix-version.patch
BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
%global _description \
Easily draw tables in terminal/console applications (written in\
Python) from a list of lists of strings. Supports multi-line rows.
%description %_description

%package     -n python3-terminaltables
Summary:        %summary
%description -n python3-terminaltables %_description

%prep
%autosetup -n terminaltables-%{commit}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%tox || :

%files -n python3-terminaltables -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.1.10-13
- Rebuilt for Python 3.13

* Thu Apr 25 2024 Terje Rosten <terje.rosten@ntnu.no> - 3.1.10-12
- Use download from commit as both pypi and git release download is borken

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.1.10-8
- Rebuilt for Python 3.12

* Mon Mar 27 2023 Terje Rosten <terje.rosten@ntnu.no> - 3.1.10-7
- Use upstream patch to do poetry-core switch

* Thu Feb 02 2023 Terje Rosten <terje.rosten@ntnu.no> - 3.1.10-6
- Fix reqs

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 3.1.10-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Terje Rosten <terje.rosten@ntnu.no> - 3.1.10-1
- 3.1.10

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.0-22
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-19
- Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-15
- Fix test stuff (rhbz#1716534)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-11
- Remove Python 2 subpackage in rawhide

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-9
- Rebuilt for Python 3.7

* Mon May 07 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-8
- Remove unused build dependency on tox

* Mon Feb 12 2018 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-7
- Clean up

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-3
- Add trailing /
- Testing enabled

* Mon May 15 2017 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-2
- Minor tweaks

* Sun Apr 23 2017 Dick Marinus <dick@mrns.nl> - 3.1.0-1
- Initial package
