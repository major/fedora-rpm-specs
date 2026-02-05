%global gjs_version 1.69.2
%global libadwaita_version 1.8~alpha
%global libshumate_version 1.5~alpha

%global tarball_version %%(echo %{version} | tr '~' '.')

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$

Name:           gnome-maps
Version:        50~beta
Release:        %autorelease
Summary:        Map application for GNOME

License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Maps
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  meson
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0) >= %{gjs_version}
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-1.0)
BuildRequires:  pkgconfig(shumate-1.0) >= %{libshumate_version}
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
# Required for tests.
BuildRequires:  libsecret
BuildRequires:  blueprint-compiler

Requires:       dbus
Requires:       gdk-pixbuf2%{?_isa}
Requires:       geoclue2-libs%{?_isa}
Requires:       geocode-glib2%{?_isa}
Requires:       gjs%{?_isa} >= %{gjs_version}
Requires:       gobject-introspection%{?_isa}
Requires:       gsettings-desktop-schemas%{?_isa}
Requires:       gtk4%{?_isa}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       libgweather4%{?_isa}
Requires:       libportal%{?_isa}
Requires:       libshumate%{?_isa} >= %{libshumate_version}
Requires:       libsoup3%{?_isa}
Requires:       rest%{?_isa}

%description
GNOME Maps is a simple map application for the GNOME desktop.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

# Remove unneeded development files
rm %{buildroot}%{_libdir}/gnome-maps/libgnome-maps.so

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Maps.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Maps.desktop
%meson_test


%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Maps.desktop
%{_datadir}/dbus-1/services/org.gnome.Maps.service
%{_datadir}/glib-2.0/schemas/org.gnome.Maps.gschema.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Maps.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Maps-symbolic.svg
%{_metainfodir}/org.gnome.Maps.metainfo.xml
%{_libdir}/%{name}/


%changelog
%autochangelog
