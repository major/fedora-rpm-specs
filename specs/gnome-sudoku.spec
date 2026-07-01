Name:           gnome-sudoku
Epoch:          1
Version:        51~alpha
Release:        %autorelease
Summary:        GNOME Sudoku game

License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Sudoku
Source0:        https://download.gnome.org/sources/%{name}/%{gnome_major_version}/%{name}-%{gnome_tarball_version}.tar.xz

%gnome_check_version

BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(qqwing)

BuildRequires:  gcc gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala

%description
GNOME version of the popular Sudoku Japanese logic game.


%prep
%autosetup -p1 -n %{name}-%{gnome_tarball_version}

%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Sudoku.desktop


%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gnome-sudoku
%{_datadir}/applications/org.gnome.Sudoku.desktop
%{_datadir}/dbus-1/services/org.gnome.Sudoku.service
%{_datadir}/glib-2.0/schemas/org.gnome.Sudoku.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Sudoku*
%{_metainfodir}/org.gnome.Sudoku.metainfo.xml
%{_mandir}/man6/gnome-sudoku.6*


%changelog
%autochangelog
