%global glib2_version 2.80
%global gtk4_version 4.17.3
%global gtksourceview_version 5.15.0
%global enchant_version 2.2.0
%global libadwaita_version 1.6.0
%global libspelling_version 0.4.0

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:		gnome-text-editor
Version:	50~rc
Release:	%autorelease
Summary:	A simple text editor for the GNOME desktop

# Code is GPL-3.0-or-later and the Appdata is CC0-1.0
License:	GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:		https://gitlab.gnome.org/GNOME/gnome-text-editor
Source0:	https://download.gnome.org/sources/%{name}/50/%{name}-%{tarball_version}.tar.xz

BuildRequires:	pkgconfig(editorconfig)
BuildRequires:	pkgconfig(enchant-2) >= %{enchant_version}
BuildRequires:	pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:	pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:	pkgconfig(gtksourceview-5) >= %{gtksourceview_version}
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:	pkgconfig(libspelling-1) >= %{libspelling_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	itstool
BuildRequires:	meson
BuildRequires:	/usr/bin/appstream-util

Requires:	glib2%{?_isa} >= %{glib2_version}
Requires:	enchant2%{?_isa} >= %{enchant_version}
Requires:	gtk4%{?_isa} >= %{gtk4_version}
Requires:	gtksourceview5%{?_isa} >= %{gtksourceview_version}
Requires:	libadwaita%{?_isa} >= %{libadwaita_version}
Requires:	libspelling%{?_isa} >= %{libspelling_version}

%description
GNOME Text Editor is a simple text editor that focuses on session management.
It works hard to keep track of changes and state even if you quit the application.
You can come back to your work even if you've never saved it to a file.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson -Ddevelopment=false
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.TextEditor.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.TextEditor.desktop


%files -f %{name}.lang
%doc README.md NEWS
%license COPYING
%{_bindir}/gnome-text-editor
%{_metainfodir}/org.gnome.TextEditor.metainfo.xml
%{_datadir}/applications/org.gnome.TextEditor.desktop
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/org.gnome.TextEditor.service
%{_datadir}/glib-2.0/schemas/org.gnome.TextEditor.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg


%changelog
%autochangelog
