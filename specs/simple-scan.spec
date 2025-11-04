%global         desktop_id org.gnome.SimpleScan

Name:           simple-scan
Version:        49.1
Release:        %autorelease
Summary:        Simple scanning utility
# Sources are under GPLv3+, icon and help are under CC-BY-SA.
License:        GPL-3.0-or-later AND CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/simple-scan

%global         gittag %{version}
Source0:        %{url}/-/archive/%{gittag}/%{name}-%{gittag}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(gusb) >= 0.2.7
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2.0
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(zlib)

%if ! 0%{?flatpak}
BuildRequires:  pkgconfig(packagekit-glib2) >= 1.1.5
%endif

Requires:       xdg-utils

%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep
%autosetup -p1 -n %{name}-%{gittag}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-man --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{desktop_id}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{desktop_id}.desktop

%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{desktop_id}.desktop
%{_datadir}/glib-2.0/schemas/%{desktop_id}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{desktop_id}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{desktop_id}-symbolic.svg
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{desktop_id}.metainfo.xml

%changelog
%autochangelog
