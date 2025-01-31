%define gettext_package gnome-terminal

%global gettext_version 0.19.8
%define glib2_version 2.52.0
%define gtk3_version 3.24.0
%define libhandy_version 1.6.0
%define vte_version 0.74.0
%define desktop_file_utils_version 0.2.90

Name:    gnome-terminal
Version: 3.54.3
Release: %autorelease
Summary: Terminal emulator for GNOME

License: GPL-3.0-or-later AND GFDL-1.3-only
URL:     https://wiki.gnome.org/Apps/Terminal
Source0: https://gitlab.gnome.org/GNOME/%{name}/-/archive/%{version}/%{name}-%{version}.tar.xz
Source1: org.gnome.Terminal.gschema.override

BuildRequires: pkgconfig(dconf)
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(libhandy-1) >= %{libhandy_version}
BuildRequires: pkgconfig(libnautilus-extension-4)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(vte-2.91) >= %{vte_version}
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: docbook-style-xsl
BuildRequires: gettext-devel >= %{gettext_version}
BuildRequires: gcc-c++
BuildRequires: gnome-shell
BuildRequires: itstool
BuildRequires: libxslt
BuildRequires: meson
BuildRequires: systemd-rpm-macros
BuildRequires: yelp-tools
BuildRequires: /usr/bin/appstream-util

Requires: dbus
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gsettings-desktop-schemas
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: libhandy%{?_isa} >= %{libhandy_version}
Requires: vte291%{?_isa} >= %{vte_version}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
gnome-terminal is a terminal emulator for GNOME. It features the ability to use
multiple terminals in a single window (tabs) and profiles support.

%package nautilus
Summary: GNOME Terminal extension for Nautilus
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides: nautilus-open-terminal = %{version}-%{release}
Obsoletes: nautilus-open-terminal < 0.20-8

%description nautilus
This package provides a Nautilus extension that adds the 'Open in Terminal'
option to the right-click context menu in Nautilus.

%prep
%autosetup -p1

%build
%meson \
    -Ddebug=true \
    -Ddocs=true \
    -Dnautilus_extension=true \
    -Dsearch_provider=true

%meson_build

%install
%meson_install

install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/glib-2.0/schemas

%find_lang %{gettext_package} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Terminal*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Terminal.desktop
%meson_test

%files -f %{gettext_package}.lang
%license COPYING COPYING.GFDL
%doc README.md
%{_bindir}/gnome-terminal
%{_datadir}/applications/org.gnome.Terminal.desktop
%{_datadir}/applications/org.gnome.Terminal.Preferences.desktop
%{_libexecdir}/gnome-terminal-preferences
%{_libexecdir}/gnome-terminal-server
%{_datadir}/dbus-1/services/org.gnome.Terminal.service
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.override
%{_datadir}/gnome-shell
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Terminal.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Terminal-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Terminal.Preferences.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Terminal.Preferences-symbolic.svg
%dir %{_datadir}/xdg-terminals
%{_datadir}/xdg-terminals/org.gnome.Terminal.desktop
%dir %{_libdir}/gnome-terminal
%{_libdir}/gnome-terminal/gschemas.compiled
%{_mandir}/man1/gnome-terminal.1*
%{_metainfodir}/org.gnome.Terminal.metainfo.xml
%{_userunitdir}/gnome-terminal-server.service

%files nautilus
%{_libdir}/nautilus/extensions-4/libterminal-nautilus.so
%{_metainfodir}/org.gnome.Terminal.Nautilus.metainfo.xml

%autochangelog
