%global tarball_version %%(echo %{version} | tr '~' '.')
%define major_version %(c=%{version}; echo $c | cut -d. -f1 | cut -d~ -f1)

Name:           quadrapassel
Version:        49.2.3
Release:        %autorelease
Summary:        GNOME Quadrapassel game

# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            https://wiki.gnome.org/Apps/Quadrapassel
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  blueprint-compiler
BuildRequires:  clutter-gtk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gsound-devel
BuildRequires:  gtk4-devel
BuildRequires:  itstool
BuildRequires:  libadwaita-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libgee-devel
BuildRequires:  libmanette-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

%description
The Russian game of falling geometric shapes.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome
%find_lang %{name}_libgnome-games-support --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Quadrapassel.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Quadrapassel.metainfo.xml


%files -f %{name}.lang -f %{name}_libgnome-games-support.lang
%license COPYING
%{_bindir}/quadrapassel
%{_datadir}/applications/org.gnome.Quadrapassel.desktop
%{_datadir}/dbus-1/services/org.gnome.Quadrapassel.service
%{_datadir}/glib-2.0/schemas/org.gnome.Quadrapassel.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Quadrapassel.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Quadrapassel-symbolic.svg
%{_datadir}/metainfo/org.gnome.Quadrapassel.metainfo.xml
%dir %{_datadir}/sounds/quadrapassel/ 
%{_datadir}/sounds/quadrapassel/*
%{_mandir}/man6/quadrapassel.6*


%changelog
%autochangelog
