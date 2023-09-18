%global tarball_version %%(echo %{version} | tr '~' '.')

Name:          polari
Version:       45.0
Release:       %autorelease
Summary:       Internet Relay Chat client for GNOME

# The package contains a private helper library licensed LGPLv2+,
# all program sources are GPLv2+
License:       GPLv2+ and LGPLv2+
URL:           https://wiki.gnome.org/Apps/Polari
Source0:       http://download.gnome.org/sources/%{name}/45/%{name}-%{tarball_version}.tar.xz

BuildRequires: meson
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gjs-1.0) >= 1.69.2
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(telepathy-glib)

# for file triggers
BuildRequires: glib2 >= 2.45.4-2
BuildRequires: desktop-file-utils >= 0.22-6

# for help
BuildRequires: itstool

# Bootstrap requirements
BuildRequires: gettext >= 0.19.6

# GObject-introspection imports at runtime
Requires: libsoup3%{?_isa}
Requires: libsecret%{?_isa}

# DBus services
Requires: telepathy-filesystem
Requires: telepathy-logger
Requires: telepathy-mission-control
Requires: telepathy-idle

# For color emoji support
Recommends: google-noto-emoji-fonts

%define bus_name org.gnome.Polari

%description
Polari is an Internet Relay Chat client for the GNOME desktop.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

# this would go into a polari-devel package if there was
# such a thing ... there isn't, so it's useless to us
rm -rf %{buildroot}/%{_datadir}/%{name}/gir-1.0

%check
%meson_test

%files -f %{name}.lang
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{bus_name}.desktop
%{_datadir}/metainfo/%{bus_name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{bus_name}.*
%{_datadir}/icons/hicolor/*/apps/%{bus_name}-symbolic.*
%{_datadir}/%{name}/
%{_datadir}/dbus-1/services/%{bus_name}.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Polari.service
%{_libdir}/%{name}/
%{_datadir}/glib-2.0/schemas/%{bus_name}.gschema.xml
%{_datadir}/telepathy/clients/Polari.client

%changelog
%autochangelog
