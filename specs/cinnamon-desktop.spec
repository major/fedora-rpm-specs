%global forgeurl https://github.com/linuxmint/cinnamon-desktop
%global tagver   6.7.6
%global tag      %{tagver}-unstable

Summary: Shared code among cinnamon-session, nemo, etc
Name:    cinnamon-desktop
Version: %{tagver}^unstable
Release: %{autorelease}
%{forgemeta}
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND MIT
URL:     %{forgeurl}
Source0: %{forgesource}
Source1: x-cinnamon-mimeapps.list
Patch0:  set_font_defaults.patch

ExcludeArch: %{ix86}

BuildSystem:   meson
BuildOption(conf): -Dalsa=true
BuildOption(conf): -Ddeprecation_warnings=false
%ifarch x86_64 aarch64
BuildOption(conf): -Dbubblewrap=enabled
%else
BuildOption(conf): -Dbubblewrap=disabled
%endif

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.3.16
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= 2.22.0
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)  >= 2.70
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libseccomp)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(xrandr)
BuildRequires: gcc
BuildRequires: python3-packaging

Requires: redhat-menus

# Make sure to update libgnome schema when changing this
%if 0%{?fedora}
Requires: system-backgrounds-gnome
%endif

%description
The cinnamon-desktop package contains an internal library
(libcinnamon-desktop) used to implement some portions of the CINNAMON
desktop, and also some data files and other shared components of the
CINNAMON user environment.

%package devel
Summary:  Libraries and headers for libcinnamon-desktop
License:  GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for the CINNAMON-internal private library
libcinnamon-desktop.

%prep
%forgeautosetup -p1

%install -a
mkdir -p %{buildroot}%{_datadir}/applications/
install -m 644 %SOURCE1 %buildroot%{_datadir}/applications/x-cinnamon-mimeapps.list

%find_lang cinnamon-desktop-3.0 --all-name --with-gnome

%files -f cinnamon-desktop-3.0.lang
%doc AUTHORS README
%license COPYING COPYING.LIB
%{_datadir}/glib-2.0/schemas/org.cinnamon.*.xml
%{_datadir}/applications/x-cinnamon-mimeapps.list
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/C*.typelib

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/cinnamon-desktop/
%{_datadir}/gir-1.0/C*.gir

%changelog
%autochangelog