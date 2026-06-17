# -*-Mode: rpm-spec -*-

Name:      azote
Version:   1.16.0
Release:   %autorelease
BuildArch: noarch
Summary:   Wallpaper and color manager for Sway, i3 and some other WMs

# GPLv3: main program
# BSD: colorthief.py
License:   GPL-3.0-only and BSD-1-Clause

URL:       https://github.com/nwg-piotr/azote
Source:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: gobject-introspection
BuildRequires: gtk3
BuildRequires: python3-cairo
BuildRequires: python3-devel
BuildRequires: python3-gobject
BuildRequires: python3-pillow
BuildRequires: python3-send2trash

Requires: gtk3
Requires: python3-cairo
Requires: python3-pillow
Requires: python3-gobject
Requires: ((feh and xrandr) if Xserver)
Requires: ((swaybg and wlr-randr) if wayfire)
Requires: python3-xlib

Recommends: python3-pillow-jxl-plugin
Recommends: python3-send2trash
Recommends: ImageMagick
Recommends: ((maim and slop) if Xserver)

Provides: bundled(python3-colorthief) = 0.2.1

%description
Azote is a GTK+3 - based picture browser and background setter, as the
front-end to the swaybg (sway/Wayland) and feh (X windows) commands. It
also includes several color management tools.

The program is confirmed to work on sway, i3, Openbox, Fluxbox and dwm
window managers, on Arch Linux, Void Linux, Debian and Fedora.

%prep
%autosetup -p1
for lib in %{name}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/applications dist/%{name}.desktop
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/%{name} dist/*.png dist/*.svg
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/pixmaps dist/azote.svg
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
%pyproject_check_import

%files -f %{pyproject_files}
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%doc README.md


%changelog
%autochangelog
