%global gobject_introspection_version 1.35.9
%global gtk4_version 4.5.0
%global pygobject_version 3.36.1
%global tracker_sparql_version 2.99.3
%global grilo_version 0.3.13

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:          gnome-music
Summary:       Music player and management application for GNOME
Version:       44~rc
Release:       %autorelease

# The sources are under the GPLv2+ license, except for:
# - the gnome-music icon which is CC-BY-SA
#
# Also: https://bugzilla.gnome.org/show_bug.cgi?id=706457
License:       (GPLv2+ with exceptions) and CC-BY-SA
URL:           https://wiki.gnome.org/Apps/Music
Source0:       https://download.gnome.org/sources/%{name}/44/%{name}-%{tarball_version}.tar.xz

BuildArch:     noarch
BuildRequires: /usr/bin/appstream-util
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: itstool
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(goa-1.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires: pkgconfig(grilo-0.3) >= %{grilo_version}
BuildRequires: pkgconfig(grilo-plugins-0.3)
BuildRequires: pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libmediaart-2.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(py3cairo)
BuildRequires: pkgconfig(pygobject-3.0) >= %{pygobject_version}
BuildRequires: pkgconfig(tracker-sparql-3.0) >= %{tracker_sparql_version}
BuildRequires: python3-devel

Requires:      gdk-pixbuf2
Requires:      gnome-online-accounts
Requires:      gobject-introspection >= %{gobject_introspection_version}
Requires:      grilo >= %{grilo_version}
Requires:      grilo-plugins
Requires:      gstreamer1
Requires:      gstreamer1-plugins-base
Requires:      gtk4 >= %{gtk4_version}
Requires:      libmediaart
Requires:      libnotify >= 0.7.6
Requires:      libsoup3
Requires:      libtracker-sparql3 >= %{tracker_sparql_version}
Requires:      pango
Requires:      python3-cairo
Requires:      python3-gobject >= %{pygobject_version}

%description
Music player and management application for GNOME.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Music.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Music.desktop


%files -f %{name}.lang
%license LICENSE
%doc NEWS README.md
%{_bindir}/gnome-music
%{_datadir}/applications/org.gnome.Music.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Music.gschema.xml
%{_datadir}/org.gnome.Music/
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Music.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Music-symbolic.svg
%{_metainfodir}/org.gnome.Music.appdata.xml
%{python3_sitelib}/gnomemusic


%changelog
%autochangelog
