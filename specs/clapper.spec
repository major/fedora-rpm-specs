Name:           clapper
Version:        0.10.0
Release:        %autorelease
Summary:        Modern media player powered by GStreamer and GTK4

License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/Rafostar/clapper
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  graphviz
BuildRequires:  pkgconfig(gio-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.76.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.24.0
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.24.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.24.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.24.0
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 1.24.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.24.0
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4.0
BuildRequires:  pkgconfig(libcgraph)
BuildRequires:  pkgconfig(libgvc)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(microdns)
BuildRequires:  vala

Requires:       hicolor-icon-theme

%description
Clapper is a modern media player designed for simplicity and ease of
use. Powered by GStreamer and built for the GNOME desktop environment
using GTK4 toolkit, it has a clean and stylish interface that lets you
focus on enjoying your favorite videos.

%package        devel
Summary:        Header files and libraries for Clapper development
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The clapper-devel package contains header files and libraries needed to
develop programs that use Clapper.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang clapper-app
%find_lang clapper-gtk

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f clapper-app.lang -f clapper-gtk.lang
%license COPYING-GPL COPYING-LGPL
%doc README.md

%{_bindir}/clapper
%{_libdir}/libclapper-0.0.so.0{,.*}
%{_libdir}/libclapper-gtk-0.0.so.0{,.*}
%{_libdir}/libgstclapperglcontexthandler.so.0{,.*}
%{_libdir}/clapper-0.0/
%{_libdir}/girepository-1.0/Clapper{,Gtk}-0.0.typelib
%{_libdir}/gstreamer-1.0/libgstclapper.so
%{_datadir}/applications/com.github.rafostar.Clapper.desktop
%{_datadir}/dbus-1/services/com.github.rafostar.Clapper.service
%{_datadir}/glib-2.0/schemas/com.github.rafostar.Clapper.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.rafostar.Clapper{,-symbolic}.svg
%{_datadir}/metainfo/com.github.rafostar.Clapper.metainfo.xml
%{_datadir}/mime/packages/com.github.rafostar.Clapper.xml

%files devel
%{_includedir}/clapper-0.0/
%{_libdir}/libclapper-0.0.so
%{_libdir}/libclapper-gtk-0.0.so
%{_libdir}/libgstclapperglcontexthandler.so
%{_libdir}/pkgconfig/clapper-0.0.pc
%{_libdir}/pkgconfig/clapper-gtk-0.0.pc
%{_datadir}/gir-1.0/Clapper{,Gtk}-0.0.gir
%{_datadir}/vala/vapi/clapper{,-gtk}-0.0.{deps,vapi}

%changelog
%autochangelog
