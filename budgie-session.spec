%define po_package budgie-session-0

Name:           budgie-session
Version:        0.9.1
Release:        %autorelease
Summary:        Budgie Desktop session manager

License:        GPL-2.0-or-later
URL:            https://github.com/BuddiesOfBudgie/budgie-session
Source:         %{url}/releases/download/v{verson}/%{name}-v%{version}.tar.xz

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

BuildRequires:  /usr/bin/xsltproc
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson
# this is so the configure checks find /usr/bin/halt etc.
BuildRequires:  usermode
BuildRequires:  xmlto

Requires: dconf
Requires: system-logos
Requires: gsettings-desktop-schemas >= 0.1.7
Requires: dbus

%description
Budgie Session is a softish fork of gnome-session, designed to
provide a stable session manager for Budgie 10.x

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson -Dsystemd=true -Dsystemd_journal=true -Dsystemd_session="default"
%meson_build

%install
%meson_install

%find_lang %{po_package}

%files -f %{po_package}.lang
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/budgie-session*
%{_libexecdir}/budgie-session-binary
%{_libexecdir}/budgie-session-check-accelerated
%{_libexecdir}/budgie-session-check-accelerated-gl-helper
%{_libexecdir}/budgie-session-check-accelerated-gles-helper
%{_libexecdir}/budgie-session-ctl
%{_libexecdir}/budgie-session-failed
%{_mandir}/man1/budgie-session*1.*
%{_datadir}/budgie-session/hardware-compatibility
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.SessionManager.gschema.xml

%changelog
%autochangelog
