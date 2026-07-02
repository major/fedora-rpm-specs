Name:           gnome-font-viewer
Version:        50.0
Release:        %autorelease
Summary:        Utility for previewing fonts for GNOME

License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://gitlab.gnome.org/GNOME/gnome-font-viewer
Source0:        https://download.gnome.org/sources/%{name}/%{gnome_major_version}/%{name}-%{gnome_tarball_version}.tar.xz

%gnome_check_version

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%description
Use gnome-font-viewer, the Font Viewer, to preview fonts and display
information about a specified font. You can use the Font Viewer to display the
name, style, type, size, version and copyright of the font.

%prep
%autosetup -p1 -n %{name}-%{gnome_tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.font-viewer.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.font-viewer.metainfo.xml

%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_bindir}/gnome-thumbnail-font
%{_datadir}/applications/org.gnome.font-viewer.desktop
%{_datadir}/dbus-1/services/org.gnome.font-viewer.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.font-viewer.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.font-viewer-symbolic.svg
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_metainfodir}/org.gnome.font-viewer.metainfo.xml

%changelog
%autochangelog
