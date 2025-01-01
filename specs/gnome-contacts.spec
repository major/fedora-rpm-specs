%global gtk4_version 4.15.3

Name:           gnome-contacts
Version:        47.1.1
Release:        %autorelease
Summary:        Contacts manager for GNOME

%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %%(cut -d "." -f 1 <<<%{tarball_version})

# Sources are GPL-2.0-or-later, Appdata is CC0-1.0, icon is CC-BY-SA-4.0.
License:        GPL-2.0-or-later AND CC0-1.0 AND CC-BY-SA-4.0
URL:            https://apps.gnome.org/Contacts
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  /usr/bin/appstreamcli
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(folks-eds)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libqrencode)

Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       hicolor-icon-theme
# Camera support for avatar
Requires:       gstreamer1-plugin-gtk4
Requires:       pipewire-gstreamer

%description
%{name} is a standalone contacts manager for GNOME desktop.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install
appstreamcli metainfo-to-news %{buildroot}/%{_metainfodir}/org.gnome.Contacts.appdata.xml NEWS
%find_lang %{name}

%check
appstreamcli validate --no-net %{buildroot}/%{_metainfodir}/org.gnome.Contacts.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Contacts.desktop

%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gnome-contacts
%{_libexecdir}/gnome-contacts/
%{_libexecdir}/gnome-contacts-search-provider
%{_datadir}/applications/org.gnome.Contacts.desktop
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Contacts*.svg
%{_metainfodir}/org.gnome.Contacts.appdata.xml
%{_mandir}/man1/gnome-contacts.1*

%changelog
%autochangelog
