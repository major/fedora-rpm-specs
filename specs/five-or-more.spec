%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           five-or-more
Version:        48.1
Release:        %autorelease
Summary:        GNOME "Five or More" game

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:            https://wiki.gnome.org/Apps/Five%20or%20more
Source0:        https://download.gnome.org/sources/%{name}/48/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  vala

Obsoletes: gnome-games-glines < 1:3.7.92
Obsoletes: gnome-games-extra < 1:3.7.92
Obsoletes: gnome-games-extra-data < 3.2.0-6

%description
Move balls around the grid and try and form lines. Once you form five in a
row, the line disappears. Unfortunately more balls keep dropping in.

%prep
%autosetup -n five-or-more-%{tarball_version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.five-or-more.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_bindir}/five-or-more
%{_datadir}/applications/org.gnome.five-or-more.desktop
%{_datadir}/dbus-1/services/org.gnome.five-or-more.service
%{_datadir}/five-or-more
%{_datadir}/glib-2.0/schemas/org.gnome.five-or-more.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.five-or-more.*
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.five-or-more-symbolic.svg
%{_datadir}/metainfo/org.gnome.five-or-more.metainfo.xml
%{_mandir}/man6/five-or-more.6*


%changelog
%autochangelog
