Name:           gthumb
Epoch:          1
Version:        4.0~beta
Release:        %autorelease
Summary:        Image viewer, editor, organizer

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/gthumb
Source0:        https://download.gnome.org/sources/%{name}/%{gnome_major_minor_version}/%{name}-%{gnome_tarball_version}.tar.xz

%gnome_check_version

# the development files had been removed in the 4.0 series
Obsoletes:	%{name}-devel < %{version}

BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(colord) >= 1.3
BuildRequires:  pkgconfig(exiv2) >= 0.28
BuildRequires:  pkgconfig(glib-2.0) >= 2.84
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.26.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.26.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.26.0
BuildRequires:  pkgconfig(gtk4) >= 4.18.5
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8.0
BuildRequires:  pkgconfig(libheif) >= 1.11
BuildRequires:  pkgconfig(libjxl) >= 0.3.0
BuildRequires:  pkgconfig(libpng) >= 1.6
BuildRequires:  pkgconfig(libportal) >= 0.9
BuildRequires:  pkgconfig(libportal-gtk4) >= 0.9
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.34.0
BuildRequires:  pkgconfig(libwebp) >= 0.2.0
BuildRequires:  pkgconfig(zlib)
BuildRequires:  gcc gcc-c++
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  desktop-file-utils

Requires: hicolor-icon-theme

# Contains some files from the Independent JPEG Group's implementation of
# the libjpeg library.
Provides: bundled(libjpeg)

%description
gthumb is an application for viewing, editing, and organizing
collections of images.

%prep
%autosetup -p1 -n %{name}-%{gnome_tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%{_bindir}/gthumb
%{_libexecdir}/gthumb/
%{_libexecdir}/gthumb/video-thumbnailer
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb*
%{_datadir}/applications/org.gnome.gthumb.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.gthumb.png
%{_datadir}/icons/hicolor/*/apps/org.gnome.gthumb-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gthumb.svg
%{_metainfodir}/org.gnome.gthumb.metainfo.xml
%{_mandir}/man1/gthumb.1*

%changelog
%autochangelog
