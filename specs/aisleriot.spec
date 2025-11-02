Name:    aisleriot
Epoch:   1
Version: 3.22.35
Release: %autorelease
Summary: A collection of card games

# Automatically converted from old format: GPLv3+ and LGPLv3+ and GFDL - review is highly recommended.
License: GPL-3.0-or-later AND LGPL-3.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://wiki.gnome.org/Apps/Aisleriot
Source0: https://gitlab.gnome.org/GNOME/${name}/-/archive/%{version}/%{name}-%{version}.tar.xz
Patch0:  aisleriot-3.22.19-appdata-namespace.patch

BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(guile-3.0)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: appdata-tools
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: yelp-tools

%description
Aisleriot is a collection of over 80 card games programmed in scheme.

%prep
%autosetup -p1

%build
%meson \
       -Dtheme_kde=false
%meson_build

%install
%meson_install

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots %{buildroot}%{_datadir}/metainfo/sol.metainfo.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/sol/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/sol/b.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/sol/c.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/sol/d.png 

# Omit the valgrind suppression file; only for use during development
rm %{buildroot}%{_libdir}/valgrind/aisleriot.supp

%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/sol.desktop

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING.GPL3 COPYING.LGPL3 COPYING.GFDL
%{_bindir}/*
%{_libdir}/aisleriot
%{_libexecdir}/aisleriot/
%{_datadir}/aisleriot
%{_datadir}/applications/sol.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/symbolic/apps/gnome-aisleriot-symbolic.svg
%{_datadir}/metainfo/sol.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%{_mandir}/man6/sol.6*

%changelog
%autochangelog
