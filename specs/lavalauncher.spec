# -*-Mode: rpm-spec -*-

Name:     lavalauncher
Version:  2.1.1
Release:  11%{?dist}
Summary:  %{name} is a simple launcher for Wayland
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:  GPL-3.0-only
URL:      https://git.sr.ht/~leon_plickat/%{name}
Source0:  %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: cairo-devel
BuildRequires: meson
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: scdoc
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

%description
LavaLauncher is a simple launcher for Wayland.

It displays a dynamically sized bar with user defined buttons. Buttons
consist of an image, which is displayed as the button icon on the bar,
and at least one shell command, which is executed when the user
activates the button.

Buttons can be activated with pointer and touch events.

A single LavaLauncher instance can provide multiple such bars, across
multiple outputs.

The Wayland compositor must implement the Layer-Shell and XDG-Output
for LavaLauncher to work.

Beware: Unlike applications launchers which are similar in visual
design to LavaLauncher, which are often called "docks", LavaLauncher
does not care about .desktop files or icon themes nor does it keep
track running applications. Instead, LavaLaunchers approach of
manually defined buttons is considerably more flexible: You could have
buttons not just for launching applications, but for practically
anything you could do in your shell, like for ejecting your optical
drive, rotating your screen, sending your cat an email, playing a
funny sound, muting all audio, toggling your lamps and a lot more. Be
creative!

LavaLauncher is opinionated, yet remains configurable. The
configuration syntax is documented in the man page.

LavaLauncher has been successfully tested on sway, wayfire (Wayfire
currently does not respect subsurfaces ordering used by LavaLauncher),
river and hikari.

%prep
%setup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}

%doc README.md
%{_mandir}/man1/%{name}.1.*

%license LICENSE

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.1-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 15 2021 Bob Hepple <bob.hepple@gmail.com> - 2.1.1-2
- rebuilt

* Fri Oct 15 2021 Bob Hepple <bob.hepple@gmail.com> - 2.1.1-1
- new version

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Bob Hepple <bob.hepple@gmail.com> - 2.0.0-1
- new version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7-1
- new version

* Thu Apr 09 2020 Bob Hepple <bob.hepple@gmail.com> - 1.6-4
- rebuilt for fedora review

* Wed Feb 19 2020 Bob Hepple <bob.hepple@gmail.com> - 1.6-3
- correct license to GPL3

* Tue Feb 18 2020 Bob Hepple <bob.hepple@gmail.com> - 1.6-2
- correct license to GPL2

* Mon Feb 17 2020 Bob Hepple <bob.hepple@gmail.com> - 1.6-1
- Initial version of the package
