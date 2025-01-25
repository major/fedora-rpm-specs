%global pypi_name python-digitalocean
%global pkgname digitalocean

%bcond_without python3

Name:           python-%{pkgname}
Version:        1.17.0
Release:        15%{?dist}
Summary:        Easy access to Digital Ocean APIs to deploy droplets, images and more

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://pypi.python.org/pypi/python-digitalocean
Source0:        https://github.com/koalalorenzo/%{pypi_name}/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-responses

%description
Easy access to Digital Ocean APIs to deploy droplets, images and
more.

%package -n python3-%{pkgname}
Requires:       python3-jsonpickle
Requires:       python3-requests

Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
Easy access to Digital Ocean APIs to deploy droplets, images and
more.

This is the Python 3 version of the package.

%prep
%autosetup -p1
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check
%pytest -k "not TestFirewall"

%install
%pyproject_install
%pyproject_save_files -l %{pkgname}


%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.md

%changelog
* Thu Jan 23 2025 Felix Schwarz <fschwarz@fedoraproject.org> - 1.17.0-15
- use modern python packaging macros to get the tests running again

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.17.0-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.17.0-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 1.17.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 12 2022 Jonathan Wright <jonathan@almalinux.org> - 1.17.0-5
- Remove python-mock requirement

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.17.0-3
- rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.17.0-1
- update to 1.17.0 (#2010011)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.16.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.16.0-1
- update to 1.16.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-2
- Rebuilt for Python 3.9

* Tue Apr 28 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.15.0-1
- update to 1.15.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.14.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.14.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Eli Young <elyscape@gmail.com> - 1.14.0-1
- Update to 1.14.0
- Remove Python 2 package in Fedora 30+ (#1658538)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.13.2-4
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 1.13.2-3
- Add python2- prefix where possible

* Thu Feb 15 2018 Eli Young <elyscape@gmail.com> - 1.13.2-2
- Fix requires

* Wed Feb 14 2018 Eli Young <elyscape@gmail.com> - 1.13.2-1
- Initial package (#1544605)
