%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d. -f1)

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$
%global __requires_exclude ^libgnome-photos\\.so.*$

%global cairo_version 1.14.0
%global dazzle_version 3.26.0
%global gdk_pixbuf_version 2.36.8
%global gegl_version 0.4.0
%global gettext_version 0.19.8
%global gexiv2_version 0.10.8
%global glib2_version 2.62.0
%global goa_version 3.8.0
%global gtk3_version 3.22.16
%global handy_version 1.1.90
%global tracker_miners_version 3.0.0

Name:          gnome-photos
Version:       44.0
Release:       %autorelease
Summary:       Access, organize and share your photos on GNOME

# GNOME Photos itself is GPLv3+, but the bundled libgd is LGPLv2+
License:       GPL-3.0-or-later AND LGPL-2.1-or-later
URL:           https://wiki.gnome.org/Apps/Photos
Source0:       https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

Patch1:        0001-wip-item-manager-Handle-collection-COLUMNS_URNs-with.patch

BuildRequires: /usr/bin/appstream-util
BuildRequires: desktop-file-utils
BuildRequires: docbook-style-xsl
BuildRequires: gcc
BuildRequires: gettext >= %{gettext_version}
BuildRequires: itstool
BuildRequires: libxslt
BuildRequires: meson
BuildRequires: pkgconfig(babl-0.1)
BuildRequires: pkgconfig(cairo) >= %{cairo_version}
BuildRequires: pkgconfig(cairo-gobject) >= %{cairo_version}
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= %{gdk_pixbuf_version}
BuildRequires: pkgconfig(gegl-0.4) >= %{gegl_version}
BuildRequires: pkgconfig(geocode-glib-2.0)
BuildRequires: pkgconfig(gexiv2) >= %{gexiv2_version}
BuildRequires: pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gobject-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(goa-1.0) >= %{goa_version}
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(libdazzle-1.0) >= %{dazzle_version}
BuildRequires: pkgconfig(libhandy-1) >= %{handy_version}
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(libportal-gtk3)
BuildRequires: pkgconfig(tracker-sparql-3.0)

Requires:      gdk-pixbuf2%{?_isa} >= %{gdk_pixbuf_version}
Requires:      gegl04%{?_isa} >= %{gegl_version}
Requires:      glib2%{?_isa} >= %{glib2_version}
Requires:      gtk3%{?_isa} >= %{gtk3_version}
Requires:      libdazzle%{?_isa} >= %{dazzle_version}
Requires:      libgexiv2%{?_isa} >= %{gexiv2_version}
Requires:      libhandy%{?_isa} >= %{handy_version}
Requires:      tracker-miners >= %{tracker_miners_version}

# These are started/contacted over D-Bus
Recommends:    baobab
Recommends:    gnome-settings-daemon
%if 0%{?fedora} || 0%{?rhel} < 9
Recommends:    dleyna-renderer
%endif

# libgd is not meant to be installed as a system-wide shared library.
# It is just a way for GNOME applications to share widgets and other common
# code on an ad-hoc basis.
Provides: bundled(libgd)


%description
Access, organize and share your photos on GNOME. A simple and elegant
replacement for using a file manager to deal with photos. Enhance, crop
and edit in a snap. Seamless cloud integration is offered through GNOME
Online Accounts.


%package       tests
Summary:       Tests for %{name}

%if 0%{?fedora} || 0%{?rhel} < 9
Requires:      python3-dogtail
%endif


%description   tests
This package contains the installable tests for %{name}.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
# never enable -Dflatpak=true, the files it installs are meant to be provided
# by a flatpak build of tracker-miners
%meson \
  --buildtype=plain \
%if 0%{?fedora} || 0%{?rhel} < 9
  -Ddogtail=true \
%else
  -Ddogtail=false \
%endif
  -Dflatpak=false \
  -Dinstalled_tests=true \
  -Dmanuals=true \

%meson_build


%install
%meson_install

# Upstream doesn't install with desktop-file-install, so let's check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Photos.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%find_lang %{name} --with-gnome


%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Photos.desktop
%{_datadir}/dbus-1/services/org.gnome.Photos.service
%{_datadir}/glib-2.0/schemas/org.gnome.photos.gschema.xml
%{_datadir}/gnome-shell/
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Photos.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Photos-symbolic.svg
%{_docdir}/%{name}

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libgnome-photos.so

%{_libexecdir}/%{name}-thumbnailer

%{_mandir}/man1/%{name}.1*
%{_metainfodir}/org.gnome.Photos.appdata.xml

%files tests
%{_libexecdir}/installed-tests/%{name}
%{_datadir}/installed-tests


%changelog
%autochangelog
