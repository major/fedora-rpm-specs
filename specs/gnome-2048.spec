Name:           gnome-2048
Version:        50.alpha
Release:        %autorelease
Summary:        A 2048 clone for GNOME

License:        GPL-3.0-or-later
URL:            https://wiki.gnome.org/Apps/2048
Source0:        https://download.gnome.org/sources/gnome-2048/50/gnome-2048-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

Provides:       bundled(libgnome-games-support)

%description
A GNOME clone of the popular game 2048
http://en.wikipedia.org/wiki/2048_(video_game)


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome
%find_lang gnome-2048_libgnome-games-support --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.TwentyFortyEight.desktop


%files -f %{name}.lang -f gnome-2048_libgnome-games-support.lang
%doc README.md code-of-conduct.md
%license COPYING
%{_bindir}/gnome-2048
%{_datadir}/applications/org.gnome.TwentyFortyEight.desktop
%{_datadir}/dbus-1/services/org.gnome.TwentyFortyEight.service
%{_datadir}/glib-2.0/schemas/org.gnome.TwentyFortyEight.gschema.xml
%{_datadir}/metainfo/org.gnome.TwentyFortyEight.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.TwentyFortyEight*
%{_mandir}/man6/gnome-2048*


%changelog
%autochangelog
