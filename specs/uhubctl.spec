Name:           uhubctl
Version:        2.6.0
Release:        2%{?dist}
Summary:        USB hub per-port power control

License:        GPL-2.0-only
URL:            https://github.com/mvp/%{name}
Source0:        https://github.com/mvp/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libusbx-devel
BuildRequires:  make
BuildRequires:  pkgconfig

%description
uhubctl is utility to control USB power per-port on smart USB hubs. Smart hub
is defined as one that implements per-port power switching.


%prep
%autosetup -p1


%build
%make_build


%install
%make_install


%check
%{buildroot}%{_sbindir}/%{name} --version


%files
%license COPYING LICENSE
%doc README.md
%{_sbindir}/%{name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Scott K Logan <logans@cottsay.net> - 2.6.0-1
- Update to 2.6.0 (rhbz#2309678)
- Add a smoke test to the package

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.0-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 02 2022 Scott K Logan <logans@cottsay.net> - 2.5.0-1
- Update to 2.5.0 (rhbz#2139373)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Scott K Logan <logans@cottsay.net> - 2.4.0-2
- Switch pkg-config dep to more widely-available 'pkgconfig'

* Wed Aug 25 2021 Scott K Logan <logans@cottsay.net> - 2.4.0-1
- Update to 2.4.0 (rhbz#1907252)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Scott K Logan <logans@cottsay.net> - 2.2.0-1
- Initial package (rhbz#1840296)
