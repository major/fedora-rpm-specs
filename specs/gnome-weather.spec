%global gobject_introspection_version 1.35.9
%global gtk4_version 4.5
%global gjs_version 1.71.0

%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %%(cut -d '.' -f 1 <<<%{tarball_version})

Name:		gnome-weather
Version:	50~beta
Release:	%autorelease
Summary:	A weather application for GNOME

License:	GPL-2.0-or-later AND BSD-3-Clause and CC-BY-3.0 and CC-BY-SA-3.0
URL:		https://wiki.gnome.org/Apps/Weather
Source0:	https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	python3-devel
BuildRequires:	pkgconfig(geoclue-2.0)
BuildRequires:	pkgconfig(gjs-1.0) >= %{gjs_version}
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires:	pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:	pkgconfig(gweather4)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:  typescript

Requires:	gdk-pixbuf2
Requires:	geoclue2-libs
Requires:	gjs >= %{gjs_version}
Requires:	glib2
Requires:	gobject-introspection >= %{gobject_introspection_version}
Requires:	gsettings-desktop-schemas
Requires:	gtk4 >= %{gtk4_version}
Requires:	libadwaita
Requires:	libgweather4

%description
gnome-weather is a weather application for GNOME

%prep
%autosetup -p1 -n %{name}-%{tarball_version}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} .

%build
%meson
%meson_build

%install
%meson_install

# Avoid RPM build warning:
#     absolute symlink: /usr/bin/gnome-weather -> /usr/share/org.gnome.Weather/org.gnome.Weather
rm %{buildroot}%{_bindir}/gnome-weather
ln -s ../share/org.gnome.Weather/org.gnome.Weather %{buildroot}%{_bindir}/gnome-weather

%find_lang org.gnome.Weather

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Weather.desktop

%files -f org.gnome.Weather.lang
%license COPYING.md
%doc NEWS data/CREDITS
%{_bindir}/gnome-weather
%{_datadir}/applications/org.gnome.Weather.desktop
%{_datadir}/dbus-1/services/org.gnome.Weather.service
%{_datadir}/dbus-1/services/org.gnome.Weather.BackgroundService.service
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.gschema.xml
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Weather*
%{_datadir}/icons/hicolor/scalable/status/*.svg
%{_datadir}/metainfo/org.gnome.Weather.metainfo.xml
%{_datadir}/org.gnome.Weather/

%changelog
%autochangelog
