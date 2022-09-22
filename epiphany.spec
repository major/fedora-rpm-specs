%global glib2_version 2.67.4
%global gtk3_version 3.24.0
%global webkit2gtk_version 2.37.1

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:    epiphany
Epoch:   1
Version: 43.0
Release: %autorelease
Summary: Web browser for GNOME

License: GPLv3+ and CC-BY-SA
URL:     https://wiki.gnome.org/Apps/Web
Source0: https://download.gnome.org/sources/epiphany/43/%{name}-%{tarball_version}.tar.xz

# Fedora bookmarks
Patch0: epiphany-default-bookmarks.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: iso-codes-devel
BuildRequires: itstool
BuildRequires: libappstream-glib-devel
BuildRequires: meson
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(evince-document-3.0)
BuildRequires: pkgconfig(gcr-3)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gnome-desktop-3.0) >= %{glib2_version}
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(gtk+-unix-print-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(hogweed)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libdazzle-1.0)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libportal-gtk3) >= 0.5
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(webkit2gtk-4.1) >= %{webkit2gtk_version}
BuildRequires: pkgconfig(webkit2gtk-web-extension-4.1) >= %{webkit2gtk_version}

%description
Epiphany is the web browser for the GNOME desktop. Its goal is to be
simple and easy to use. Epiphany ties together many GNOME components
in order to let you focus on the web content, instead of the browser
application.

%package runtime            
Summary: Epiphany runtime suitable for web applications
Requires: gsettings-desktop-schemas
Requires: iso-codes
Provides: bundled(gvdb)
Provides: bundled(highlightjs)
Provides: bundled(readabilityjs)

%description runtime            
This package provides a runtime for web applications without actually            
installing the epiphany application itself.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%{_datadir}/applications/org.gnome.Epiphany.desktop
%{_datadir}/dbus-1/services/org.gnome.Epiphany.SearchProvider.service
%{_metainfodir}/org.gnome.Epiphany.appdata.xml
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/org.gnome.Epiphany.SearchProvider.ini
%{_libexecdir}/epiphany-search-provider

%files runtime
%license COPYING
%doc NEWS README.md
%{_bindir}/epiphany
%{_datadir}/epiphany
%{_datadir}/dbus-1/services/org.gnome.Epiphany.WebAppProvider.service
%{_datadir}/icons/hicolor/*/apps/org.gnome.Epiphany*
%{_datadir}/glib-2.0/schemas/org.gnome.epiphany.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Epiphany.enums.xml
%{_libdir}/epiphany/
%{_libexecdir}/epiphany/
%{_libexecdir}/epiphany-webapp-provider
%{_mandir}/man1/epiphany.1*

%changelog
%autochangelog
