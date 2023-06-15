%global srcname texttable
%global _description %{expand:
Python module to generate a formatted text table, using ASCII characters.}

Name:           python-%{srcname}
Version:        1.6.4
Release:        5%{?dist}
Summary:        Python module for creating simple ASCII tables
License:        MIT
URL:            https://github.com/foutaise/%{srcname}
Source:         %{pypi_source}
BuildArch:      noarch


%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pytest tests.py


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.4-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.4-2
- Rebuilt for Python 3.11

* Mon May 09 2022 Carl George <carl@george.computer> - 1.6.4-1
- Latest upstream
- Convert to pyproject macros

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.2-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Carl George <carl@george.computer> - 1.6.2-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Carl George <carl@george.computer> - 1.4.0-1
- Latest upstream rhbz#1594444
- Disable python2 subpackage on F30+ rhbz#1629791

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Carl George <carl@george.computer> - 1.3.0-1
- Latest upstream
- Use shared docdir for both py2 and py3 packages

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Carl George <carl@george.computer> - 1.1.1-1
- Latest upstream

* Mon Oct 23 2017 Carl George <carl@george.computer> - 1.1.0-1
- Latest upstream

* Fri Oct 20 2017 Carl George <carl@george.computer> - 1.0.0-1
- Latest upstream

* Tue Oct 10 2017 Carl George <carl@george.computer> - 0.9.1-1
- Latest upstream
- Enable python34 subpackage on EPEL

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 Carl George <carl.george@rackspace.com> - 0.9.0-1
- Latest upstream
- Drop python*-tools build requirement, 2to3 is no longer used
- Run test suite
- Correct license
- Add EL7 compatibility

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-2
- Rebuild for Python 3.6

* Mon Jul 25 2016 Dominika Krejci <dkrejci@redhat.com> - 0.8.4-1
- Add Python 3
- Update to 0.8.4

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 12 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.8.1-4
- Patch to remove "__main__" and /usr/bin/env from non-executable library

* Mon Aug 11 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.8.1-3
- Fix description for rpmlin errors, fix files listing

* Fri Aug 08 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.8.1-2
- Fixed __python vs __python2 macros, BuildArch: noarch

* Wed Jul 23 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.8.1-1
- Initial package for Fedora
