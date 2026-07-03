%global appname org.gnome.Characters

%global gjs_version 1.50
%global gtk4_version 4.6
%global libadwaita_version 1.5~alpha

Name:		gnome-characters
Version:	50.0
Release:	%autorelease
Summary:	Character map application for GNOME
# Files from gtk-js-app are licensed under 3-clause BSD.
# Other files are GPL 2.0 or later.
License:	BSD-3-Clause AND GPL-2.0-or-later
URL:		https://wiki.gnome.org/Design/Apps/CharacterMap
Source0:	https://download.gnome.org/sources/%{name}/%{gnome_major_version}/%{name}-%{gnome_tarball_version}.tar.xz

%gnome_check_version

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	libappstream-glib
BuildRequires:	libunistring-devel
BuildRequires:	meson
BuildRequires:	pkgconfig(gjs-1.0) >= %{gjs_version}
BuildRequires:	pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:	pkgconfig(libadwaita-1) >= %{libadwaita_version}

Requires:	gjs >= %{gjs_version}
Requires:	gnome-desktop4%{_isa}
Requires:	gtk4%{_isa} >= %{gtk4_version}
Requires:	libadwaita%{?_isa} >= %{libadwaita_version}

%description
Characters is a simple utility application to find and insert unusual
characters.


%prep
%autosetup -p1 -n %{name}-%{gnome_tarball_version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{appname}


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{appname}.desktop


%files -f %{appname}.lang
%doc NEWS README.md
%license COPYING COPYINGv2
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/%{appname}
%{_datadir}/gnome-shell/search-providers/%{appname}.search-provider.ini
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appname}-symbolic.svg
%{_metainfodir}/%{appname}.metainfo.xml
%{_libdir}/%{appname}


%changelog
%autochangelog
