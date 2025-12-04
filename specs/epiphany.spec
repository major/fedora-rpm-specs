%global glib2_version 2.74.0
%global gtk4_version 4.13.3
%global libadwaita_version 1.8~alpha
%global webkitgtk_version 2.43.4

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           epiphany
Epoch:          1
Version:        49.2
Release:        %autorelease
Summary:        Web browser for GNOME

License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Web
Source0:        https://download.gnome.org/sources/epiphany/49/%{name}-%{tarball_version}.tar.xz

# Fedora bookmarks
Patch0:         epiphany-default-bookmarks.patch

BuildRequires:  /usr/bin/rst2man
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  libappstream-glib-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(gtk4-unix-print) >= %{gtk4_version}
BuildRequires:  pkgconfig(hogweed)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkitgtk-6.0) >= %{webkitgtk_version}
BuildRequires:  pkgconfig(webkitgtk-web-process-extension-6.0) >= %{webkitgtk_version}

Requires: epiphany-runtime%{?_isa} = %{epoch}:%{version}-%{release}

%description
Epiphany is the web browser for the GNOME desktop. Its goal is to be
simple and easy to use. Epiphany ties together many GNOME components
in order to let you focus on the web content, instead of the browser
application.

%package runtime
Summary: Epiphany runtime suitable for web applications
Requires: gsettings-desktop-schemas
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gtk4%{?_isa} >= %{gtk4_version}
Requires: iso-codes
Requires: libadwaita%{?_isa} >= %{libadwaita_version}
Requires: webkitgtk6.0%{?_isa} >= %{webkitgtk_version}
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
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Epiphany.metainfo.xml

%files -f %{name}.lang
%{_datadir}/applications/org.gnome.Epiphany.desktop
%{_datadir}/dbus-1/services/org.gnome.Epiphany.SearchProvider.service
%{_metainfodir}/org.gnome.Epiphany.metainfo.xml
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
