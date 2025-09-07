Name:           gdk-pixbuf2-modules-extra
Version:        2.43.5
Release:        %autorelease
Summary:        Extra image loaders for gdk-pixbuf2

License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gdk-pixbuf
Source0:        https://download.gnome.org/sources/gdk-pixbuf/2.43/gdk-pixbuf-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  meson
# gdk-pixbuf does a configure time check which uses the GIO mime
# layer; we need to actually have the mime type database.
BuildRequires:  shared-mime-info

Requires:       gdk-pixbuf2%{?_isa} > 2.43.0

%description
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
clutter.

This package contains modules for loading ANI, ICNS, QTIF, XBM, and XPM
images.

%prep
%autosetup -n gdk-pixbuf-%{version} -p1

%build
%meson \
       -Dpng=disabled \
       -Dtiff=disabled \
       -Djpeg=disabled \
       -Dgif=disabled \
       -Dglycin=disabled \
       -Dandroid=disabled \
       -Dothers=enabled \
       -Dbuiltin_loaders=none \
       -Ddocumentation=false \
       -Dintrospection=disabled \
       -Dman=false \
       -Dinstalled_tests=false \
       -Dthumbnailer=disabled \
       %{nil}

%global _smp_mflags -j1
%meson_build

%check
%meson_test

%install
%meson_install
rm -r $RPM_BUILD_ROOT%{_bindir}
# gdk-pixbuf2 package includes locale data for our modules
rm -r $RPM_BUILD_ROOT%{_datadir}/locale
rm -r $RPM_BUILD_ROOT%{_includedir}
rm    $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-{bmp,ico,pnm,tga}.so
rm    $RPM_BUILD_ROOT%{_libdir}/libgdk_pixbuf-2.0*
rm -r $RPM_BUILD_ROOT%{_libdir}/pkgconfig

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.so

%changelog
%autochangelog
