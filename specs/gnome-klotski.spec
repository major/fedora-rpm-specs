Name:           gnome-klotski
Version:        3.38.2
Release:        %autorelease
Summary:        GNOME Klotski game
License:        GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Klotski
Source0:        https://download.gnome.org/sources/%{name}/3.38/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  vala

%description
A series of sliding block puzzles. Try and solve them in the least number of
moves.


%prep
%setup -q


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
%{_bindir}/gnome-klotski
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.Klotski.service
%{_datadir}/glib-2.0/schemas/org.gnome.Klotski.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Klotski.*
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Klotski-symbolic.svg
%{_datadir}/metainfo/org.gnome.Klotski.appdata.xml
%{_mandir}/man6/gnome-klotski.6*


%changelog
%autochangelog
