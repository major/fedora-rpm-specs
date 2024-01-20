%define po_package gnome-session-45

%if 0%{?fedora}
%else
%global with_session_selector 1
%endif

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-session
Version:        45.0
Release:        %autorelease
Summary:        GNOME session manager

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-session
Source:         https://download.gnome.org/sources/gnome-session/45/%{name}-%{tarball_version}.tar.xz

# Blacklist NV30: https://bugzilla.redhat.com/show_bug.cgi?id=745202
Patch:          gnome-session-3.3.92-nv30.patch
Patch:          gnome-session-3.6.2-swrast.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=772421
Patch:          0001-check-accelerated-gles-Use-eglGetPlatformDisplay-EXT.patch
# For https://fedoraproject.org/w/index.php?title=Changes/HiddenGrubMenu
# This should go upstream once systemd has a generic interface for this
Patch:          0001-Fedora-Set-grub-boot-flags-on-shutdown-reboot.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
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
BuildRequires:  intltool
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

%package xsession
Summary: Desktop file for gnome-session
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: xorg-x11-server-Xorg%{?_isa}
Requires: gnome-shell

%description xsession
Desktop file to add GNOME to display manager session menu.

%package wayland-session
Summary: Desktop file for wayland based gnome session
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: xorg-x11-server-Xwayland%{?_isa} >= 1.20.99.1
Requires: gnome-shell

%description wayland-session
Desktop file to add GNOME on wayland to display manager session menu.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson                                                          \
%if 0%{?with_session_selector}
           -Dsession_selector=true                              \
%endif
           -Dsystemd=true                                       \
           -Dsystemd_journal=true
%meson_build

%install
%meson_install

%find_lang %{po_package}

%ldconfig_scriptlets

%files xsession
%{_datadir}/xsessions/*

%files wayland-session
%{_datadir}/wayland-sessions/*

%files -f %{po_package}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/gnome-session*
%{_libexecdir}/gnome-session-binary
%{_libexecdir}/gnome-session-check-accelerated
%{_libexecdir}/gnome-session-check-accelerated-gl-helper
%{_libexecdir}/gnome-session-check-accelerated-gles-helper
%{_libexecdir}/gnome-session-ctl
%{_libexecdir}/gnome-session-failed
%{_mandir}/man1/gnome-session*1.*
%{_datadir}/gnome-session/
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/gnome-portals.conf
%{_datadir}/doc/gnome-session/
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gnome-session.convert
%{_datadir}/glib-2.0/schemas/org.gnome.SessionManager.gschema.xml
%{_userunitdir}/gnome-session*
%{_userunitdir}/gnome-launched-.scope.d/

%changelog
%autochangelog
