%global tarball_version %%(echo %{version} | tr '~' '.')

%global libadwaita_version 1.5

Name:           gnome-chess
Version:        49.0
Release:        %autorelease
Summary:        GNOME Chess game

License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Chess
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(librsvg-2.0)

Requires: gnuchess
Requires: libadwaita%{?_isa} >= %{libadwaita_version}

%description
A chess game that supports several chess engines.

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
%license COPYING
%doc NEWS README.md
%config(noreplace) %{_sysconfdir}/gnome-chess/engines.conf
%{_bindir}/gnome-chess
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.Chess.service
%{_datadir}/glib-2.0/schemas/org.gnome.Chess.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Chess.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Chess-symbolic.svg
%{_metainfodir}/org.gnome.Chess.metainfo.xml
%{_mandir}/man6/gnome-chess.6*


%changelog
%autochangelog
