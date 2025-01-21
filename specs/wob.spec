# -*-Mode: rpm-spec-mode; -*-

Name:     wob
Version:  0.15.1
Release:  7%{?dist}
Summary:  A lightweight overlay volume/backlight/progress/anything bar for Wayland
License:  ISC
URL:      https://github.com/francma/wob

Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1: %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
# francma publishes their public keys on github as
# wget https://keys.openpgp.org/vks/v1/by-fingerprint/5C6DA024DDE27178073EA103F4B432D5D67990E3
# gpg --import ~/tmp/5C6DA024DDE27178073EA103F4B432D5D67990E3.asc
# gpg2 --export --export-options export-minimal 5C6DA024DDE27178073EA103F4B432D5D67990E3 > 5C6DA024DDE27178073EA103F4B432D5D67990E3.gpg
Source2: 5C6DA024DDE27178073EA103F4B432D5D67990E3.gpg

BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: meson
BuildRequires: pkgconfig(libseccomp)
BuildRequires: scdoc
BuildRequires: libcmocka-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: inih-devel

Requires: inih

%description
A lightweight overlay volume/backlight/progress/anything bar for
Wayland.

%prep
%gpgverify -k 2 -s 1 -d 0
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}

%doc README.md
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}.ini.5.*

%license LICENSE

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Bob Hepple <bob.hepple@gmail.com> - 0.14.2-2
- added gpg keys

* Tue Nov 29 2022 Bob Hepple <bob.hepple@gmail.com> - 0.14.2-1
- new version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar 06 2022 Bob Hepple <bob.hepple@gmail.com> - 0.13-1
- new version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 07 2021 Bob Hepple <bob.hepple@gmail.com> - 0.11-1
- new version

* Sun Aug 09 2020 Bob Hepple <bob.hepple@gmail.com> - 0.10-1
- new version

* Sat Aug  8 2020 Bob Hepple <bob.hepple@gmail.com> - 0.9-2
- fix error in changelog

* Sat Aug  8 2020 Bob Hepple <bob.hepple@gmail.com> - 0.9-1
- new release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr  6 2020 Bob Hepple <bob.hepple@gmail.com> - 0.8-4
- fix license field to ISC

* Mon Apr  6 2020 Bob Hepple <bob.hepple@gmail.com> - 0.8-3
- rebuilt per RHBZ#1819554

* Wed Apr  1 2020 Bob Hepple <bob.hepple@gmail.com> - 0.8-2
- prep for review request

* Mon Mar  2 2020 Bob Hepple <bob.hepple@gmail.com> - 0.8-1
- latest release

* Mon Feb 17 2020 Bob Hepple <bob.hepple@gmail.com> - 0.6-1
- Initial version of the package
