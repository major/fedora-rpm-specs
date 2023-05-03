%global app_id  org.gnome.Nibbles

Name:           gnome-nibbles
Version:        3.38.3
Release:        %autorelease
Summary:        GNOME Nibbles game
License:        GPL-3.0-or-later AND BSD-2-Clause AND GFDL-1.1-no-invariants-or-later
URL:            https://wiki.gnome.org/Apps/Nibbles
Source0:        https://download.gnome.org/sources/gnome-nibbles/3.38/gnome-nibbles-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(clutter-1.0) >= 1.22.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gsound) >= 1.0.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libgnome-games-support-1) >= 1.7.1

Obsoletes: gnome-games-extra < 1:3.7.4
Obsoletes: gnome-games-gnibbles < 1:3.7.4

%description
Pilot a worm around a maze trying to collect diamonds and at the same time
avoiding the walls and yourself. With each diamond your worm grows longer and
navigation becomes more and more difficult. Playable by up to four people.

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
%{_bindir}/gnome-nibbles
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/*/%{app_id}*
%{_metainfodir}/%{app_id}.appdata.xml
%{_mandir}/man6/gnome-nibbles.6*


%changelog
%autochangelog
