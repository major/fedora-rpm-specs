%global glib2_version 2.80.0

Name:           gobject-introspection
Version:        1.82.0
Release:        %autorelease
Summary:        Introspection system for GObject-based libraries

License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause
URL:            https://wiki.gnome.org/Projects/GObjectIntrospection
Source:         https://download.gnome.org/sources/%{name}/1.82/%{name}-%{version}.tar.xz
# This fixes some FTBFS when building some package with Clang 19 in Fedora 42+
# For example: https://bugzilla.redhat.com/show_bug.cgi?id=2341532
# https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/519
# https://gitlab.gnome.org/GNOME/gobject-introspection/-/merge_requests/515
Patch:          https://gitlab.gnome.org/GNOME/gobject-introspection/-/commit/2812471365c75ab51347a9101771128f8ab283ab.patch

# Workaround for Python 3.12 compatibility
# https://bugzilla.redhat.com/show_bug.cgi?id=2208966
Patch:          workaround.patch

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-markdown
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(libffi)

Requires:       glib2%{?_isa} >= %{glib2_version}

%description
GObject Introspection can scan C header and source files in order to
generate introspection "typelib" files.  It also provides an API to examine
typelib files, useful for creating language bindings among other
things.

%package devel
Summary:        Libraries and headers for gobject-introspection
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Not always, but whatever, it's a tiny dep to pull in
Requires:       libtool
# For g-ir-doctool
Requires:       python3-mako
Requires:       python3-markdown
# This package only works with the Python version it was built with
# https://bugzilla.redhat.com/show_bug.cgi?id=1691064
Requires:       (python(abi) = %{python3_version} if python3)
# The package uses distutils which is no longer part of Python 3.12+ standard library
# https://bugzilla.redhat.com/show_bug.cgi?id=2135406
Requires:       (python3-setuptools if python3 >= 3.12)

%description devel
Libraries and headers for gobject-introspection

%prep
%autosetup -p1
mv giscanner/ast.py giscanner/gio_ast.py

%build
%meson -Ddoctool=enabled -Dgtk_doc=true -Dpython=%{__python3}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc NEWS README.rst
%license COPYING COPYING.GPL COPYING.LGPL
%{_libdir}/libgirepository-1.0.so.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_libdir}/libgirepository-1.0.so
%{_libdir}/gobject-introspection/
%{_libdir}/pkgconfig/gobject-introspection-1.0.pc
%{_libdir}/pkgconfig/gobject-introspection-no-export-1.0.pc
%{_includedir}/gobject-introspection-1.0/
%{_bindir}/g-ir-*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gir-1.0/gir-1.2.rnc
%{_datadir}/gobject-introspection-1.0/
%{_datadir}/aclocal/introspection.m4
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gi/
%{_mandir}/man1/g-ir-compiler.1*
%{_mandir}/man1/g-ir-doc-tool.1*
%{_mandir}/man1/g-ir-generate.1*
%{_mandir}/man1/g-ir-scanner.1*

%changelog
%autochangelog
