%global tarball_version	%%(echo %{version} | tr '~' '.')

%global gtk_version 4.11.3
%global libadwaita_version 1.5

Name:		gnome-usage
Version:	48.0
Release:	%autorelease
Summary:	A GNOME app to view information about use of system resources

License:	GPL-3.0-or-later AND CC0-1.0
URL:		https://wiki.gnome.org/Apps/Usage
Source0:	https://download.gnome.org/sources/%{name}/48/%{name}-%{tarball_version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk4) >= %{gtk_version}
BuildRequires:	pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:	pkgconfig(tracker-sparql-3.0)
BuildRequires:	vala

Requires:	adwaita-icon-theme
Requires:	gtk4 >= %{gtk_version}
Requires:	libadwaita >= %{libadwaita_version}

%description
gnome-usage lets you easily visualize the use of system resources such as
CPU, memory, and storage.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Usage.desktop

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS README.md NEWS
%{_bindir}/gnome-usage
%{_datadir}/applications/org.gnome.Usage.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Usage.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Usage.svg
%{_metainfodir}/org.gnome.Usage.metainfo.xml

%changelog
%autochangelog
