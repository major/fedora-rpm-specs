%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           cheese
Epoch:          2
Version:        44.1
Release:        %autorelease
Summary:        Application for taking pictures and movies from a webcam

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Cheese
Source0:        https://download.gnome.org/sources/%{name}/44/%{name}-%{tarball_version}.tar.xz
Patch0: cheese-c99.patch
# https://gitlab.gnome.org/GNOME/cheese/-/merge_requests/73
# https://gitlab.gnome.org/GNOME/cheese/-/issues/183
# https://bugzilla.redhat.com/show_bug.cgi?id=2315884
# Fix crash on startup due to invalid JSON
Patch1: 73.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gtk-doc
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libXtst-devel
BuildRequires:  vala
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.27.90
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc

Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: gstreamer1-plugins-good%{?_isa}
Requires: gstreamer1-plugins-bad-free%{?_isa}
Requires: gnome-video-effects

%description
Cheese is a Photobooth-inspired GNOME application for taking pictures and
videos from a webcam. It can also apply fancy graphical effects.

%package libs
Summary:        Webcam display and capture widgets
License:        GPL-2.0-or-later
# Camera service was removed upstream in 3.25.90
Obsoletes: cheese-camera-service < 2:3.25.90

%description libs
This package contains libraries needed for applications that
want to display a webcam in their interface.

%package libs-devel
Summary:        Development files for %{name}-libs
License:        GPL-2.0-or-later
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description libs-devel
This package contains the libraries and header files that are needed
for writing applications that require a webcam display widget.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}
# Trigger recompilation of all Vala sources.
find -name '*.vala' -exec touch {} \;

%build
%meson -Dtests=false
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Cheese.desktop
%meson_test


%files
%doc AUTHORS README
%{_bindir}/cheese
%{_datadir}/applications/org.gnome.Cheese.desktop
%{_datadir}/metainfo/org.gnome.Cheese.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Cheese.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Cheese.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Cheese-symbolic.svg
%{_mandir}/man1/cheese.1*

%files -f %{name}.lang libs
%license COPYING
%{_libdir}/libcheese.so.8*
%{_libdir}/libcheese-gtk.so.25*
%{_datadir}/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
%{_libdir}/girepository-1.0/Cheese-3.0.typelib

%files libs-devel
%{_libdir}/libcheese.so
%{_libdir}/libcheese-gtk.so
%{_includedir}/cheese/
%{_datadir}/gtk-doc/
%{_libdir}/pkgconfig/cheese.pc
%{_libdir}/pkgconfig/cheese-gtk.pc
%{_datadir}/gir-1.0/Cheese-3.0.gir


%changelog
%autochangelog
