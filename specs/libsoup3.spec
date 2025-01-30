%global glib2_version 2.70.0

Name:    libsoup3
Version: 3.6.4
Release: %autorelease
Summary: Soup, an HTTP library implementation

License: LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://wiki.gnome.org/Projects/libsoup
Source0: https://download.gnome.org/sources/libsoup/3.6/libsoup-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: glib-networking >= %{glib2_version}
BuildRequires: gi-docgen >= 2021.1
BuildRequires: krb5-devel
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(libnghttp2)
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(sysprof-capture-4)
BuildRequires: /usr/bin/ntlm_auth

Recommends: glib-networking%{?_isa} >= %{glib2_version}

%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it), but the SOAP parts were removed
long ago.

%package devel
Summary: Header files for the Soup library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Libsoup is an HTTP library implementation in C. This package allows
you to develop applications that use the libsoup library.

%package doc
Summary: Documentation files for %{name}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends: gi-docgen-fonts
BuildArch: noarch

%description doc
This package contains developer documentation for %{name}.

%prep
%autosetup -p1 -n libsoup-%{version}

%build
%meson -Ddocs=enabled -Dautobahn=disabled
%meson_build

%install
%meson_install
install -m 644 -D tests/libsoup.supp %{buildroot}%{_datadir}/libsoup-3.0/libsoup.supp

%check
%meson_test

%find_lang libsoup-3.0

%files -f libsoup-3.0.lang
%license COPYING
%doc README NEWS AUTHORS
%{_libdir}/libsoup-3.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Soup-3.0.typelib

%files devel
%{_includedir}/libsoup-3.0
%{_libdir}/libsoup-3.0.so
%{_libdir}/pkgconfig/libsoup-3.0.pc
%dir %{_datadir}/libsoup-3.0
%{_datadir}/libsoup-3.0/libsoup.supp
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Soup-3.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libsoup-3.0.deps
%{_datadir}/vala/vapi/libsoup-3.0.vapi

%files doc
%{_docdir}/libsoup-3.0/

%changelog
%autochangelog
