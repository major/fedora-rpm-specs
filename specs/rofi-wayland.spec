# Use themes from the main rofi package by default
# Leave bcond for the case when things go wrong and we'll need rofi-wayland-themes
%bcond themes 0
%bcond devel  0

Name:    rofi-wayland
%global  base_ver 1.7.7
Version: %{base_ver}+wayland1
Release: 2%{?dist}
Summary: Fork of rofi with Wayland support

# lexer/theme-parser.[ch]:
# These files are generated from lexer/theme-parser.y and licensed with GPLv3+
# with Bison exception.
# As the source file is licensed with MIT, according to the Bison exception,
# the shipped files are considered to be MIT-licensed.
# See also
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/C4VVT54Z4WFGJPPD5X54ILKRF6X2IFLZ/
#
# protocols/wlr-layer-shell-unstable-v1.xml:
# The file is licensed under HPND-sell-variant; it is processed to C-compilable
# files by the `wayland-scanner` binary during build and doesn't alter the main
# license of the binaries.
License: MIT
URL:     https://github.com/lbonn/rofi
Source:  %{URL}/releases/download/%{version}/rofi-%{version}.tar.xz

BuildRequires: pkgconfig
BuildRequires: gcc
BuildRequires: bison
BuildRequires: desktop-file-utils
BuildRequires: flex
BuildRequires: meson
BuildRequires: pandoc
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-xcb)
BuildRequires: pkgconfig(check) >= 0.11.0
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-imdkit)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-xinerama)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)

# https://github.com/sardemff7/libgwater
Provides:      bundled(libgwater)
# https://github.com/sardemff7/libnkutils
Provides:      bundled(libnkutils)
# Satisfy dependency on rofi
Provides:      rofi = %{base_ver}
# `rofi` package contains the same binaries
Conflicts:     rofi

%if %{with themes}
Requires:      %{name}-themes = %{version}-%{release}
%else
# Allow slight mismatch of the theme package version
Requires:      (rofi-themes >= %{base_ver} with rofi-themes < 1.8)
%endif
Requires:      hicolor-icon-theme


%description
Rofi is a dmenu replacement. Rofi, like dmenu, will provide the user with a
textual list of options where one or more can be selected. This can either be,
running an application, selecting a window or options provided by an external
script.

This is a fork of Rofi with added support for Wayland via the layer shell
protocol, expected to work with wlroots-based compositors (Sway).

%if %{with devel}
%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%endif

%if %{with themes}
%package        themes
Summary:        Themes for %{name}
BuildArch:      noarch
# `rofi-themes` and `rofi-wayland-themes` built from the same release will
# contain identical files, allowing parallel installation.
# Forbid that explicitly.
Conflicts:      rofi-themes

%description    themes
The %{name}-themes package contains themes for %{name}.
%endif

%prep
%autosetup -p1 -n rofi-%{version}


%build
%meson
%meson_build


%install
%meson_install
%if %{without devel}
# Drop -devel files: rofi-devel should be used to build the plugins.
# The plugin api is quite stable and the headache from having two providers
# of pkgconfig(rofi) is not worth it.
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/pkgconfig
%endif
%if %{without themes}
rm -rf %{buildroot}%{_datadir}/rofi
%endif


%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/rofi*.desktop


%files
%doc README.md
%license COPYING
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%{_datadir}/applications/rofi.desktop
%{_datadir}/applications/rofi-theme-selector.desktop
%{_datadir}/icons/hicolor/scalable/apps/rofi.svg
%{_mandir}/man1/rofi*
%{_mandir}/man5/rofi*

%if %{with themes}
%files themes
%license COPYING
%{_datarootdir}/rofi
%endif

%if %{with devel}
%files devel
%{_includedir}/rofi
%{_libdir}/pkgconfig/rofi.pc
%endif


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7+wayland1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 05 2025 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.7+wayland1-1
- Update to 1.7.7+wayland1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5+wayland3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 05 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.5+wayland3-1
- Update to 1.7.5+wayland3

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5+wayland2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5+wayland2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 23 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.5+wayland2-1
- Update to 1.7.5+wayland2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5+wayland1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 26 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.5+wayland1-3
- Backport Wayland support for window mode.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5+wayland1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 27 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.5+wayland1-1
- Initial import (#2121653)
