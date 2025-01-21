# -*-Mode: rpm-spec -*-

%global commit e8bfc78f08ebdd1316daae59ecc77e62bba68b2b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global _hardened_build 1

Name:     wshowkeys
Version:  0
Release:  14.20200727git%{shortcommit}%{?dist}
Summary:  Displays key presses on screen on supported Wayland compositors
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:  GPL-3.0-only
#URL:      https://git.sr.ht/~sircmpwn/wshowkeys
URL:      https://github.com/ammgws/wshowkeys
#Source0:  %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Source0:  %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: libinput-devel
BuildRequires: libudev-devel
BuildRequires: meson
BuildRequires: pango-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: wayland-protocols-devel

%description
Displays key presses on screen on supported Wayland compositors
(requires wlr_layer_shell_v1 support eg sway).

Usage

wshowkeys [-b|-f|-s #RRGGBB[AA]] [-F font] [-t timeout]
    [-a top|left|right|bottom] [-m margin] [-o output]

    -b #RRGGBB[AA]: set background color
    -f #RRGGBB[AA]: set foreground color
    -s #RRGGBB[AA]: set color for special keys
    -F font: set font (Pango format, e.g. 'monospace 24')
    -t timeout: set timeout before clearing old keystrokes
    -a top|left|right|bottom: anchor the keystrokes to an edge.
       May be specified twice.
    -m margin: set a margin (in pixels) from the nearest edge
    -o output: request wshowkeys is shown on the specified
       output (unimplemented)

%prep
%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%attr (4711,root,root) %{_bindir}/%{name}

%doc README.md

%license LICENSE

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20200727gite8bfc78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0-13.20200727gite8bfc78
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20200727gite8bfc78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.20200727gite8bfc78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20200727gite8bfc78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20200727gite8bfc78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20200727gite8bfc78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20200727gite8bfc78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 01 2021 Bob Hepple <bob.hepple@gmail.com> - 0-6.20210802gite8bfc78
- bugfix for wlroots-1.13 (f34) and above. f33 has wlroots-1.11
- the fix is in a new repo as original author has moved on

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20200727git6388a49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20200727git6388a49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Bob Hepple <bob.hepple@gmail.com> - 0-3.20200727git6388a49
- rebuilt

* Wed Jul 29 2020 Bob Hepple <bob.hepple@gmail.com> - 0-2.20200727git6388a49
- rebuilt

* Mon Jul 27 2020 Bob Hepple <bob.hepple@gmail.com> - 1.20200727git6388a49
- Initial version of the package
