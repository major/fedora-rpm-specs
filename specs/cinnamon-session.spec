%global forgeurl https://github.com/linuxmint/cinnamon-session
%global tagver   6.7.6
%global tag      %{tagver}-unstable

%global cinnamon_desktop_version 6.7.1

Summary: Cinnamon session manager
Name:    cinnamon-session
Version: %{tagver}^unstable
Release: %{autorelease}
%{forgemeta}
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     %{forgeurl}
Source0: %{forgesource}
Patch0:  start_oo7-daemon.patch

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

# Needed for cinnamon-session.target wants
Requires: oo7-daemon

Requires: cinnamon-desktop >= %{cinnamon_desktop_version}

%description
Cinnamon-session manages a Cinnamon desktop or GDM login session. It starts up
the other core components and handles logout and saving the session.

%prep
%forgeautosetup -p1

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
%{_userunitdir}/app-cinnamon-.scope.d/
%{_userunitdir}/dbus.service.d/


%changelog
%autochangelog