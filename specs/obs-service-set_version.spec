
%global service set_version

Name:           obs-service-%{service}
Version:        0.6.6
Release:        3%{?dist}
Summary:        An OBS source service: Update spec file version
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3dist(ddt)
BuildRequires:  python3dist(packaging)
Recommends:     python3dist(packaging)
Requires:       python3
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

Very simply script to update the version in .spec or .dsc files according to
a given version or to the existing files.

%prep
%autosetup -p1

%build
sed -i -e "1 s,#!/usr/bin/python$,#!%{__python3}," set_version

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 set_version %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 set_version.service %{buildroot}%{_prefix}/lib/obs/service

%check
%{__python3} -m unittest discover tests/

%files
%license COPYING
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 18 2024 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.6.6-1
- New upstream release 0.6.6, fixes rhbz#2298441

* Wed Jun 19 2024 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.6.5-1
- New upstream release 0.6.5, fixes rhbz#2279572

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep  1 2023 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.6.2-1
- New upstream release 0.6.2, fixes rhbz#1923237
- Add patch to fix imp removal of Python 3.12, fixes rhbz#2226037

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Neal Gompa <ngompa13@gmail.com> - 0.5.12-1
- Update to 0.5.12

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.10-1
- Update to 0.5.10
- Run unit tests
- Set sed properly as a build dependency

* Sat Mar 24 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.8-1
- Initial packaging

