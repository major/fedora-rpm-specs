# -*-Mode: rpm-spec -*-

Name:     wlr-sunclock
Version:  1.0.0
Release:  9%{?dist}
Summary:  Show the sun's shadows on earth

# src/astro.[ch] are by John Walker in 1988 and placed in the Public Domain.
# Otherwise it's LGPLv3.
# Automatically converted from old format: LGPLv3 and Public Domain - review is highly recommended.
License:  LGPL-3.0-only AND LicenseRef-Callaway-Public-Domain

URL:      https://github.com/sentriz/wlr-sunclock
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: pkgconfig(gtk+-wayland-3.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: librsvg2-devel

%description

Wayland desktop widget to show the sun's shadows on earth. Uses
gtk-layer-shell and the layer shell protocol to render on your
desktop, behind your windows.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}

%doc README.md

%license LICENCE

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Bob Hepple <bob.hepple@gmail.com> - 1.0.0-1
- new version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-4
- rebuilt

* Wed Aug 26 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-3
- rebuilt per RHBZ#1867267

* Tue Aug 18 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-2
- rebuilt per RHBZ#1867267


* Sat Aug 08 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-1
- Initial version of the package
