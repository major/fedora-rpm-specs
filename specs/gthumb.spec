%global __provides_exclude_from ^%{_libdir}/gthumb/.*\\.so$
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/gthumb/ -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))

Name:           gthumb
Epoch:          1
Version:        3.12.9
Release:        %autorelease
Summary:        Image viewer, editor, organizer

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/gthumb
Source0:        https://download.gnome.org/sources/%{name}/3.12/%{name}-%{version}.tar.xz

%if %{defined el8}
# RHEL8 doesn't ship LibRaw-devel on s390x
ExcludeArch:    s390x
%endif

BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libbrasero-burn3)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  gcc gcc-c++
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  meson
BuildRequires:  desktop-file-utils
# For Web albums extension
BuildRequires:  bison flex

Requires: hicolor-icon-theme

# Contains some files from the Independent JPEG Group's implementation of
# the libjpeg library.
Provides: bundled(libjpeg)

%description
gthumb is an application for viewing, editing, and organizing
collections of images.

%package devel
Summary: Header files needed for developing gthumb extensions
Requires: %{name}%{_isa} = %{epoch}:%{version}-%{release}

%description devel
The gthumb-devel package includes header files for the gthumb
package.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%{_bindir}/gthumb
%{_libdir}/gthumb/
%{_libexecdir}/gthumb/
%{_datadir}/gthumb/
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb*
%{_datadir}/applications/org.gnome.gThumb.desktop
%{_datadir}/applications/org.gnome.gThumb.Import.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.gThumb.png
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gThumb-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gThumb.svg
%{_metainfodir}/org.gnome.gThumb.metainfo.xml
%{_mandir}/man1/gthumb.1*

%files devel
%{_includedir}/gthumb/
%{_libdir}/pkgconfig/gthumb.pc
%{_datadir}/aclocal/gthumb.m4

%changelog
%autochangelog
