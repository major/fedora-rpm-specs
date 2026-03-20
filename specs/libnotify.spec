%define glib2_version 2.38.0

Name:           libnotify
Version:        0.8.8
Release:        %autorelease
Summary:        Desktop notification library

License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/libnotify
Source0:        https://download.gnome.org/sources/libnotify/0.8/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  docbook-xsl-ns
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  xmlto
BuildRequires:  /usr/bin/xsltproc

Requires:       glib2%{?_isa} >= %{glib2_version}

%description
libnotify is a library for sending desktop notifications to a notification
daemon, as defined in the freedesktop.org Desktop Notifications spec. These
notifications can be used to inform the user about an event or display some
form of information without getting in the user's way.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files needed for
development of programs using %{name}.

%prep
%autosetup -p1

%build
%meson -Dtests=false
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS AUTHORS README.md
%{_bindir}/notify-send
%{_libdir}/libnotify.so.*
%{_libdir}/girepository-1.0/Notify-0.7.typelib
%{_mandir}/man1/notify-send.1*

%files devel
%dir %{_includedir}/libnotify
%{_includedir}/libnotify/*
%{_libdir}/libnotify.so
%{_libdir}/pkgconfig/libnotify.pc
%{_datadir}/gir-1.0/Notify-0.7.gir
%{_docdir}/libnotify-0/
%doc %{_docdir}/libnotify/spec/

%changelog
%autochangelog
