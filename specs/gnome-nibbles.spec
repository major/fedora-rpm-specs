%global app_id  org.gnome.Nibbles
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-nibbles
Version:        4.2~rc5
Release:        %autorelease
Summary:        GNOME Nibbles game
# Source code is under GPLv3+, help is under CC-BY-SA, Appdata is under CC0.
License:        GPL-3.0-or-later AND CC0-1.0 AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Nibbles
Source0:        https://download.gnome.org/sources/gnome-nibbles/4.2/gnome-nibbles-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.78.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.78.0
BuildRequires:  pkgconfig(gsound) >= 1.0.2
BuildRequires:  pkgconfig(gtk4) >= 4.13.4
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5.0
BuildRequires:  pkgconfig(libgnome-games-support-2) >= 2.0.0

%description
Pilot a worm around a maze trying to collect diamonds and at the same time
avoiding the walls and yourself. With each diamond your worm grows longer and
navigation becomes more and more difficult. Playable by up to four people.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}


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
%doc NEWS
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
