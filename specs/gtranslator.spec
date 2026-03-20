%global app_id	org.gnome.Gtranslator

Name:		gtranslator
Version:	50.0
Release:	%autorelease
Summary:	Gettext po file editor for GNOME

# Sources are GPL-2.0-or-later and GPL-3.0-or-later, help is CC-BY-SA-3.0 and
# AppData is CC0-1.0.
License:	GPL-2.0-or-later AND GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:		https://wiki.gnome.org/Apps/Gtranslator
Source0:	https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	itstool
BuildRequires:	libappstream-glib
BuildRequires:	meson
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk4) >= 4.12.0
BuildRequires:	pkgconfig(gtksourceview-5)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libadwaita-1) >= 1.7.99
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libspelling-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)

Requires:	hicolor-icon-theme
Requires:	gsettings-desktop-schemas

%description
gtranslator is an enhanced gettext po file editor for the GNOME
desktop environment. It handles all forms of gettext po files and
features many comfortable everyday usage features like find and
replace functions, auto translation, and translation learning,

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_bindir}/gtranslator
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/icons/hicolor/*/apps/%{app_id}*.svg
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gtranslator.plugins.translation-memory.gschema.xml
%{_datadir}/gtksourceview-5/language-specs/gtranslator.lang
%{_datadir}/gtranslator/
%{_metainfodir}/%{app_id}.appdata.xml
%{_mandir}/man1/gtranslator.1*

%changelog
%autochangelog
