%global pyname python-cloudflare
%global pypi_name cloudflare

Name:           python-%{pypi_name}
Version:        5.2.0
Release:        3%{?dist}
Summary:        The official Python library for the Cloudflare API

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}

# Relax the exact hatchling build-system pin (upstream pins ==1.26.3,
# Fedora ships a newer hatchling)
Patch0:         relax-hatchling-pin.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description
The official Python library for the Cloudflare API, providing convenient
access to the Cloudflare REST API from any Python 3.9+ application.

%package -n python3-%{pypi_name}

Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The official Python library for the Cloudflare API, providing convenient
access to the Cloudflare REST API from any Python 3.9+ application.

This is the Python 3 version of the package.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cloudflare


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Thu Jun 04 2026 Python Maint <python-maint@redhat.com> - 5.2.0-2
- Rebuilt for Python 3.15

* Sun May 31 2026 Jonathan Wright <jonathan@almalinux.org> - 5.2.0-1
- update to 5.2.0 rhbz#2330265

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 2.19.4-6
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 2.19.4-5
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 2.19.4-3
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 10 2024 Ben Maconi <turboben@fedoraproject.org> - 2.19.4-1
- Updated to Version 2.19.4 as to avoid messing with certbot

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.12.4-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 09 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 2.12.4-2
- drop unnecessary patch to remove shebangs (rhbz #2247294)

* Mon Oct 16 2023 Nick Bebout <nb@fedoraproject.org> - 2.12.4-1
- Update to 2.12.4

* Fri Sep 15 2023 Jonathan Wright <jonathan@almalinux.org> - 2.11.7-1
- Update to 2.11.7 rhbz#2232863

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.11.6-2
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Nick Bebout <nb@fedoraproject.org> - 2.11.6-1
- Update to 2.11.6

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.11.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jonathan Wright <jonathan@almalinux.org - 2.11.1-1
- Update to 2.11.1 rhbz#2143783

* Wed Nov 09 2022 Nick Bebout <nb@fedoraproject.org> - 2.10.4-1
- Update to 2.10.4

* Mon Nov 07 2022 Jonathan Wright <jonathan@almalinux.org> - 2.10.3-1
- update to 2.10.3 rhbz#2125087

* Thu Sep 01 2022 Jonathan Wright <jonathan@almalinux.org> - 2.9.12-1
- update to 2.9.12
- rhbz#2118035

* Tue Jul 26 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 2.9.11-1
- update to 2.9.11

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.8.15-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.8.15-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 2.8.15-1
- update to 2.8.15

* Tue Aug 18 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.8.13-1
- update to 2.8.13

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.8.3-1
- update to 2.8.3 (#1849241)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7.1-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.7.1-1
- update to 2.7.1

* Wed May 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.6.5-3
- fix man page

* Tue Apr 28 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.6.5-2
- add missing sources

* Tue Apr 28 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.6.5-1
- update to 2.6.5

* Tue Apr 28 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.6.0-2
- enable GPG verification of sources

* Fri Jan 31 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 2.6.0-1
- Update to 2.6.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Eli Young <elyscape@gmail.com> - 2.3.0-5
- Support EPEL8 builds

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Eli Young <elyscape@gmail.com> - 2.3.0-1
- Update to 2.3.0 (#1712059)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Eli Young <elyscape@gmail.com> - 2.1.0-11
- Remove Python 2 package in Fedora 30+ (#1658535)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Eli Young <elyscape@gmail.com> - 2.1.0-9
- Simplify example removal

* Fri Jun 29 2018 Eli Young <elyscape@gmail.com> - 2.1.0-8
- Remove unnecessary shebangs

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-7
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-6
- Rebuilt for Python 3.7

* Wed Apr 04 2018 Eli Young <elyscape@gmail.com> - 2.1.0-5
- Fix man page permissions

* Wed Apr 04 2018 Eli Young <elyscape@gmail.com> - 2.1.0-4
- Add cli4 man page

* Wed Apr 04 2018 Eli Young <elyscape@gmail.com> - 2.1.0-3
- Remove example scripts from egg info
- Remove unnecessary shebangs

* Wed Apr 04 2018 Eli Young <elyscape@gmail.com> - 2.1.0-2
- Fix python3 package dependencies (#1563427)

* Tue Mar 27 2018 Eli Young <elyscape@gmail.com> - 2.1.0-1
- Update to 2.1.0 (#1560758)

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 2.0.4-2
- Add python2- prefix where available

* Fri Feb 16 2018 Eli Young <elyscape@gmail.com> - 2.0.4-1
- Initial package (#1546297)
