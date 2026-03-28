Name:          gupnp-tools
Version:       0.12.2
Release:       %autorelease
Summary:       A collection of dev tools utilising GUPnP and GTK+

License:       GPL-2.0-or-later
URL:           https://wiki.gnome.org/Projects/GUPnP
Source0:       https://download.gnome.org/sources/%{name}/0.12/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: meson
BuildRequires: pkgconfig(gupnp-1.6)
BuildRequires: pkgconfig(gupnp-av-1.0)
BuildRequires: pkgconfig(gssdp-1.6)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtksourceview-4)
BuildRequires: pkgconfig(libsoup-3.0)

Requires: hicolor-icon-theme

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible. 

GUPnP-tools is a collection of developer tools utilising GUPnP and GTK+. 
It features a universal control point application as well as a sample 
DimmableLight v1.0 implementation. 

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/gupnp-av-cp.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/gupnp-network-light.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/gupnp-universal-cp.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/gupnp-tools/
%dir %{_datadir}/gupnp-tools/pixmaps/
%dir %{_datadir}/gupnp-tools/xml/
%{_bindir}/gssdp-discover
%{_bindir}/gupnp-av-cp
%{_bindir}/gupnp-event-dumper
%{_bindir}/gupnp-network-light
%{_bindir}/gupnp-universal-cp
%{_bindir}/gupnp-upload
%{_datadir}/applications/gupnp-av-cp.desktop
%{_datadir}/applications/gupnp-network-light.desktop
%{_datadir}/applications/gupnp-universal-cp.desktop
%{_datadir}/gupnp-tools/pixmaps/*.png
%{_datadir}/gupnp-tools/xml/*.xml
%{_datadir}/icons/hicolor/*/apps/av-cp.png
%{_datadir}/icons/hicolor/*/apps/network-light.png
%{_datadir}/icons/hicolor/*/apps/universal-cp.png

%changelog
%autochangelog
