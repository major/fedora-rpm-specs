%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/*/.*\\.so$

Name:           gnote
Version:        50.1
Release:        %autorelease
Summary:        Note-taking application

License:        GPL-3.0-or-later AND GFDL-1.1-only AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Gnote
Source0:        https://download.gnome.org/sources/%{name}/%{gnome_major_version}/%{name}-%{gnome_tarball_version}.tar.xz

%gnome_check_version

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(giomm-2.68)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(uuid)

%description
Gnote is a desktop note-taking application which is simple and easy to use.
It lets you organize your notes intelligently by allowing you to easily link
ideas together with Wiki style interconnects. It is a port of Tomboy to C++ 
and consumes fewer resources.

%prep
%autosetup -p1 -n %{name}-%{gnome_tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Gnote.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Gnote.appdata.xml

%files -f %{name}.lang
%license COPYING COPYING-DOCS
%doc AUTHORS NEWS README.md
%{_bindir}/gnote
%{_libdir}/gnote/
%exclude %{_libdir}/libgnote-*.so
%{_libdir}/libgnote-*.so.*
%{_datadir}/applications/org.gnome.Gnote.desktop
%{_datadir}/gnote/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Gnote.png
%{_datadir}/icons/hicolor/*/apps/org.gnome.Gnote.svg
%{_datadir}/dbus-1/services/org.gnome.Gnote.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnote.gschema.xml
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/org.gnome.Gnote.search-provider.ini
%{_mandir}/man1/gnote.1*
%{_metainfodir}/org.gnome.Gnote.appdata.xml

%changelog
%autochangelog
