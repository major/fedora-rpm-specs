%global adwaita_version 1.5.0
%define bus_name org.gnome.Extensions

Name:          gnome-extensions-app
Version:       51~alpha
Release:       %autorelease
Summary:       Manage GNOME Shell extensions

License:       GPL-2.0-or-later
URL:           https://gitlab.gnome.org/GNOME/%{name}
Source0:       https://download.gnome.org/sources/%{name}/%{gnome_major_version}/%{name}-%{gnome_tarball_version}.tar.xz

%gnome_check_version

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: meson
BuildRequires: git-core

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: gjs
BuildRequires: desktop-file-utils
BuildRequires: appstream

Requires:      gjs%{_isa}
Requires:      libadwaita%{_isa} >= %{adwaita_version}

%description
GNOME Extensions is an application for configuring and removing
GNOME Shell extensions.


%prep
%autosetup -p1 -n %{name}-%{gnome_tarball_version}


%build
%meson
%meson_build

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/%{bus_name}.desktop


%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{bus_name}.desktop
%{_datadir}/dbus-1/services/%{bus_name}.service
%{_datadir}/glib-2.0/schemas/%{bus_name}.gschema.xml
%{_datadir}/metainfo/%{bus_name}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{bus_name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{bus_name}.Devel.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{bus_name}-symbolic.svg
%{_datadir}/%{name}/
%{_libdir}/%{name}/


%changelog
%autochangelog
