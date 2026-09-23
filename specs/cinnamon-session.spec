%global cinnamon_desktop_version 6.7.1

%global upstream_version 6.7.5-unstable

Summary: Cinnamon session manager
Name:    cinnamon-session
Version: 6.7.5^unstable
Release: %autorelease
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz

ExcludeArch: %{ix86}

BuildSystem:   meson
BuildRequires: pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.37.3
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xapp) >= 1.4.6
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xtrans)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(systemd)
BuildRequires: gcc
BuildRequires: python3-packaging

Requires: system-logos
# Needed for cinnamon-settings-daemon
Requires: cinnamon-control-center-filesystem

# pull in dbus-x11, see bug 209924
Requires: dbus-x11

# an artificial requires to make sure we get dconf, for now
Requires: dconf

Requires: cinnamon-desktop >= %{cinnamon_desktop_version}

%description
Cinnamon-session manages a Cinnamon desktop or GDM login session. It starts up
the other core components and handles logout and saving the session.

%prep
%autosetup -p1 -n %{name}-%{upstream_version}

%files
%doc AUTHORS README
%doc %{_mandir}/man*/*
%license COPYING
%{_bindir}/*
%{_libexecdir}/cinnamon-session-binary
%{_libexecdir}/cinnamon-session-check-accelerated
%{_libexecdir}/cinnamon-session-check-accelerated-helper
%{_datadir}/cinnamon-session/
%{_datadir}/icons/hicolor/*/apps/cinnamon-session-properties.png
%{_datadir}/icons/hicolor/scalable/apps/cinnamon-session-properties.svg
%{_datadir}/glib-2.0/schemas/org.cinnamon.SessionManager.gschema.xml
%{_userunitdir}/*.target

%changelog
%autochangelog