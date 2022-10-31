%global libical_version 3.0.5
%global gsettings_desktop_schemas_version 3.21.2
%global edataserver_version 3.45.1
%global glib2_version 2.67.5
%global gtk4_version 4.6.0

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-calendar
Version:        43.1
Release:        %autorelease
Summary:        Simple and beautiful calendar application designed to fit GNOME 3

License:        GPLv3+
URL:            https://wiki.gnome.org/Apps/Calendar
Source0:        https://download.gnome.org/sources/%{name}/43/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gsettings_desktop_schemas_version}
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libadwaita-1)
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
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Calendar.appdata.xml

%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gnome-calendar
%{_datadir}/applications/org.gnome.Calendar.desktop
%{_datadir}/dbus-1/services/org.gnome.Calendar.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Calendar*.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Calendar*-symbolic.svg
%{_metainfodir}/org.gnome.Calendar.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.gschema.xml
# co-own these directories
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Calendar.search-provider.ini

%changelog
%autochangelog
