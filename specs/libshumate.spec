%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           libshumate
Version:        1.4~beta
Release:        %autorelease
Summary:        GTK widget to display maps

# shumate/shumate-viewport.c and shumate/shumate-viewport.h are
# LGPL-2.0-or-later while the rest of the code is LGPL-2.1-or-later
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/libshumate
Source0:        https://download.gnome.org/sources/libshumate/1.4/libshumate-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  /usr/bin/gperf
# Support graphical tests in non-graphical environment
#BuildRequires:  /usr/bin/dbus-launch
#BuildRequires:  mesa-dri-drivers
#BuildRequires:  xorg-x11-server-Xvfb

%description
libshumate is a GTK widget displaying interactive maps. Various map
sources can be used together with the possibility to draw custom
overlays, markers and lines on top of the maps. Bindings to other
languages are provided using GObject Introspection.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation files for %{name}
# urlmap.js is LGPL-2.1-or-later, generated html docs are (Apache-2.0 OR
# GPL-3.0-or-later) and misc other files are MIT
License:        LGPL-2.1-or-later AND (Apache-2.0 OR GPL-3.0-or-later) AND MIT
BuildArch:      noarch

%description    doc
This package contains developer documentation for %{name}.


%prep
%autosetup -p1 -n libshumate-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang shumate1


# %check
# %{shrink:xvfb-run -w 10 -d %meson_test}


%files -f shumate1.lang
%license COPYING
%doc AUTHORS NEWS README.md
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Shumate-1.0.typelib
%{_libdir}/libshumate-1.0.so.1*

%files devel
%{_includedir}/shumate-1.0/
%{_libdir}/libshumate-1.0.so
%{_libdir}/pkgconfig/shumate-1.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Shumate-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/shumate-1.0.deps
%{_datadir}/vala/vapi/shumate-1.0.vapi

%files doc
%license COPYING
%{_docdir}/libshumate-1.0/


%changelog
%autochangelog
