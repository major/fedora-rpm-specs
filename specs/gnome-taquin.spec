Name:           gnome-taquin
Version:        3.38.1
Release:        %autorelease
Summary:        Sliding-block puzzle game

License:        GPL-3.0-or-later AND CC-BY-SA-4.0
URL:            https://wiki.gnome.org/Apps/Taquin
Source0:        https://download.gnome.org/sources/gnome-taquin/3.38/gnome-taquin-%{version}.tar.xz

# couple upstream post 3.38.1 commits to help it build
Patch1:         0001-Don-t-alter-or-try-to-write-GtkChild-fields.patch
Patch2:         0001-Reference-of-GtkChild-fields-is-handled-by-GtkBuilde.patch

BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(gsound)

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala


%description
Taquin is a computer version of the 15-puzzle and other sliding puzzles.
The object of Taquin is to move tiles so that they reach their places, 
either indicated with numbers, or with parts of a great image.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Taquin.desktop

%files -f %{name}.lang
%doc AUTHORS NEWS README.md code-of-conduct.md
%license COPYING COPYING.sounds COPYING.themes
%{_bindir}/gnome-taquin
%{_datadir}/applications/org.gnome.Taquin.desktop
%{_datadir}/dbus-1/services/org.gnome.Taquin.service
%{_datadir}/glib-2.0/schemas/org.gnome.Taquin.gschema.xml
%{_datadir}/gnome-taquin
%{_datadir}/icons/*/*/apps/org.gnome.Taquin*
%{_datadir}/metainfo/org.gnome.Taquin.appdata.xml
%{_mandir}/man6/gnome-taquin.6*


%changelog
%autochangelog
