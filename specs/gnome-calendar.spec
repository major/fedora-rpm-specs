%global libical_version 3.0.5
%global gsettings_desktop_schemas_version 3.21.2
%global edataserver_version 3.45.1
%global glib2_version 2.80.0
%global gtk4_version 4.15.2
%global libadwaita_version 1.8~alpha

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-calendar
Version:        49.0.1
Release:        %autorelease
Summary:        Simple and beautiful calendar application designed to fit GNOME 3

# Sources are GPL-3.0-or-later, Appdata is CC0-1.0.
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Calendar
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{tarball_version}.tar.xz

BuildRequires:  blueprint-compiler
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gsettings_desktop_schemas_version}
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libecal-2.0) >= %{edataserver_version}
BuildRequires:  pkgconfig(libedataserver-1.2) >= %{edataserver_version}
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libical) >= %{libical_version}
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils

Requires:       evolution-data-server%{?_isa} >= %{edataserver_version}
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       libical%{?_isa} >= %{libical_version}

%description
Calendar is a simple and beautiful calendar application designed to fit
GNOME 3.
Features:
* Week, month and year views
* Basic editing of events
* Evolution Data Server integration
* Search support

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install
%{find_lang} %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Calendar.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Calendar.metainfo.xml

%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gnome-calendar
%{_datadir}/applications/org.gnome.Calendar.desktop
%{_datadir}/dbus-1/services/org.gnome.Calendar.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Calendar*.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Calendar*-symbolic.svg
%{_metainfodir}/org.gnome.Calendar.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.gschema.xml
# co-own these directories
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Calendar.search-provider.ini

%changelog
%autochangelog
