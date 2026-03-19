%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-todo
Version:        43.0
Release:        %autorelease
Summary:        Personal task manager for GNOME

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/Endeavour/
Source0:        https://gitlab.gnome.org/World/Endeavour/-/archive/%{tarball_version}/Endeavour-%{tarball_version}.tar.bz2
Patch0:         endeavour-girepository.patch
Patch1:         endeavour-fix-tests-build.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(girepository-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libecal-2.0) >= 3.33.2
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui4-1.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%description
GNOME To Do is a small application to manage your personal tasks. It
uses GNOME technologies, and so it has complete integration with the
GNOME desktop environment.

%package devel
Summary:        Development files needed to write plugins for GNOME To Do

%description devel
%{summary}.

%prep
%autosetup -p1 -n Endeavour-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang endeavour --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Todo.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Todo.appdata.xml

%files -f endeavour.lang
%license COPYING
%doc README.md
%{_bindir}/endeavour
%{_datadir}/applications/org.gnome.Todo.desktop
%{_datadir}/metainfo/org.gnome.Todo.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Todo.service
%{_datadir}/glib-2.0/schemas/org.gnome.todo.*.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Todo*.svg
%{_datadir}/icons/hicolor/symbolic/actions/*.svg
%{_libdir}/girepository-1.0/Gtd-1.0.typelib

%files devel
%{_includedir}/endeavour/
%{_libdir}/pkgconfig/endeavour.pc
%{_datadir}/gir-1.0/Gtd-1.0.gir

%changelog
%autochangelog
