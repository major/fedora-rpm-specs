%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-mines
Version:        48.1
Release:        %autorelease
Summary:        GNOME Mines Sweeper game

License:        GPL-3.0-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Mines
Source0:        https://download.gnome.org/sources/gnome-mines/48/gnome-mines-%{tarball_version}.tar.xz

BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgnome-games-support-2)
BuildRequires:  pkgconfig(librsvg-2.0)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala

%description
The popular logic puzzle minesweeper. Find mines on a grid 
using hints from squares you have already cleared.


%prep
%autosetup -p1 -n gnome-mines-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Mines.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/gnome-mines
%{_datadir}/applications/org.gnome.Mines.desktop
%{_datadir}/dbus-1/services/org.gnome.Mines.service
%{_datadir}/glib-2.0/schemas/org.gnome.Mines.gschema.xml
%{_datadir}/gnome-mines/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Mines*svg
%{_datadir}/metainfo/org.gnome.Mines.metainfo.xml
%{_mandir}/man6/gnome-mines.6*


%changelog
%autochangelog
