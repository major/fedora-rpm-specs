%global forgeurl	https://github.com/Hjdskes/cage

Name:			cage
Version:		0.1.4
Release:		7%{?dist}
Summary:		A Wayland kiosk

%forgemeta

License:		MIT
URL:			https://www.hjdskes.nl/projects/cage
Source0:		%{forgesource}
Source1:		https://github.com/Hjdskes/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# http://keys.gnupg.net/pks/lookup?op=get&fingerprint=on&search=0x37C445296EBC43B1
Source2:		gpgkey-6EBC43B1.gpg

BuildRequires:	gcc
BuildRequires:	gnupg2
BuildRequires:	meson
BuildRequires:	scdoc
BuildRequires:	(pkgconfig(wlroots) >= 0.14 and pkgconfig(wlroots) < 0.15)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.14

%description
This is Cage, a Wayland kiosk. A kiosk runs a single, maximized application.

This README is only relevant for development resources and instructions. For a
description of Cage and installation instructions for end-users, please see its
project page and the Wiki.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%forgeautosetup


%build
%meson -Dxwayland=true
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Lyes Saadi <fedora@lyes.eu> - 0.1.4-5
- Fixing the pkgconfig dependency version.
- Fixing the date for my last changelog entry (it's 2022, already!).

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Lyes Saadi <fedora@lyes.eu> - 0.1.4-3
- Updating BuildRequires to use pkgconfig instead of packages to better utilize
  compat packages and using a hard version requirement since wlroots breaks at
  each update.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Lyes Saadi <fedora@lyes.eu> - 0.1.4-1
- Updating to 0.1.4 (Fix #1976482)

* Tue Apr 20 2021 Lyes Saadi <fedora@lyes.eu> - 0.1.3-1
- Updating to 0.1.3 (Fix #1950582)

* Wed Apr 07 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.1.2.1-4
- Rebuild for wlroots 0.13.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Lyes Saadi <fedora@lyes.eu> - 0.1.2.1-2
- Rebuilding for wlroots 0.12

* Thu Sep 03 2020 Lyes Saadi <fedora@lyes.eu> - 0.1.2.1-1
- Initial package
