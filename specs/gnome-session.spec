%if 0%{?fedora} || (0%{?rhel} >= 10)
%else
%global with_session_selector 1
%endif

%if 0%{?fedora} && 0%{?fedora} < 43
%bcond x11 1
%else
%bcond x11 0
%endif

%global major_version %%(echo %{version} | cut -d '.' -f1 | cut -d '~' -f 1)
%global tarball_version %%(echo %{version} | tr '~' '.')
%define po_package gnome-session-%{major_version}

Name:           gnome-session
Version:        49~beta
Release:        %autorelease
Summary:        GNOME session manager

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-session
Source:         https://download.gnome.org/sources/gnome-session/%{major_version}/%{name}-%{tarball_version}.tar.xz

# For https://fedoraproject.org/w/index.php?title=Changes/HiddenGrubMenu

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xtst)

# this is so the configure checks find /usr/bin/halt etc.
BuildRequires:  usermode

BuildRequires:  gettext
BuildRequires:  xmlto
BuildRequires:  /usr/bin/xsltproc

# an artificial requires to make sure we get dconf, for now
Requires: dconf

Requires: system-logos
# Needed for gnome-settings-daemon
Requires: control-center-filesystem

Requires: gsettings-desktop-schemas >= 0.1.7

Requires: dbus

# https://github.com/containers/composefs/pull/229#issuecomment-1838735764
%if 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif


%description
gnome-session manages a GNOME desktop or GDM login session. It starts up
the other core GNOME components and handles logout and saving the session.

%if %{with x11}
%package xsession
Summary: Desktop file for gnome-session
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: xorg-x11-server-Xorg%{?_isa}
Requires: gnome-shell
# The X11 session is deprecated and eventually will be removed
Provides: deprecated()

%description xsession
Desktop file to add GNOME to display manager session menu.
%endif

%package wayland-session
Summary: Desktop file for wayland based gnome session
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: xorg-x11-server-Xwayland%{?_isa} >= 1.20.99.1
Requires: gnome-shell
%if %{without x11}
Obsoletes: gnome-session-xsession < %{version}-%{release}
%endif

%description wayland-session
Desktop file to add GNOME on wayland to display manager session menu.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson \
%if 0%{?with_session_selector}
    -Dsession_selector=true \
%endif
%if %{without x11}
    -Dx11=false \
%endif
  %{nil}
%meson_build

%install
%meson_install

rm %{buildroot}%{_datadir}/applications/gnome-mimeapps.list

%find_lang %{po_package}

%ldconfig_scriptlets

%if %{with x11}
%files xsession
%{_datadir}/xsessions/*
%endif

%files wayland-session
%{_datadir}/wayland-sessions/*

%files -f %{po_package}.lang
%doc NEWS
%license COPYING
%{_bindir}/gnome-session*
%{_libexecdir}/gnome-session-ctl
%{_libexecdir}/gnome-session-service
%{_mandir}/man1/gnome-session*1.*
%{_datadir}/gnome-session/
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/gnome-portals.conf
%{_datadir}/doc/gnome-session/
%{_datadir}/glib-2.0/schemas/org.gnome.SessionManager.gschema.xml
%{_userunitdir}/gnome-session*
%{_userunitdir}/app-flatpak-.scope.d/override.conf
%{_userunitdir}/app-gnome-.scope.d/override.conf

%changelog
%autochangelog
