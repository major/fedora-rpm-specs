Name:           glib2
Version:        2.83.2
Release:        %autorelease
Summary:        A library of handy utility functions

License:        LGPL-2.1-or-later
URL:            https://www.gtk.org
Source:         https://download.gnome.org/sources/glib/2.83/glib-%{version}.tar.xz

# Required for RHEL core crypto components policy. Good for Fedora too.
# https://bugzilla.redhat.com/show_bug.cgi?id=1630260
# https://gitlab.gnome.org/GNOME/glib/-/merge_requests/903
Patch:          gnutls-hmac.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2192204
Patch:          default-terminal.patch

# https://gitlab.gnome.org/GNOME/glib/-/merge_requests/4459
Patch:          revert-gcancellable-changes.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  perl-interpreter
BuildRequires:  glibc-devel
BuildRequires:  libattr-devel
BuildRequires:  libselinux-devel
BuildRequires:  meson
BuildRequires:  systemtap-sdt-devel
BuildRequires:  systemtap-sdt-dtrace
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/g-ir-scanner
BuildRequires:  /usr/bin/rst2man

# Dependencies for tests
BuildRequires:  shared-mime-info
BuildRequires:  /usr/bin/dbus-daemon
BuildRequires:  /usr/bin/update-desktop-database

# For gnutls-hmac.patch. We now dlopen libgnutls.so.30 so that we can build a
# static glib2 without depending on a static build of GnuTLS as well. This will
# ensure we notice if the GnuTLS soname bumps, so that we can update our patch.
BuildRequires:  gnutls
%if 0%{?__isa_bits} == 64
Requires: libgnutls.so.30()(64bit)
%else
Requires: libgnutls.so.30
%endif

Provides: bundled(cmph)
Provides: bundled(dirent)
Provides: bundled(gnulib)
Provides: bundled(gvdb)
Provides: bundled(libcharset)
Provides: bundled(xdgmime)

# glib typelib files moved from gobject-introspection to glib2 in F40
Conflicts: gobject-introspection < 1.79.1

%description
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality
as an event loop, threads, dynamic loading, and an object system.

%package devel
Summary: A library of handy utility functions
Requires: %{name}%{?_isa} = %{version}-%{release}
# Required by gdbus-codegen
Requires: python3-packaging
# glib gir files moved from gobject-introspection-devel to glib2-devel in F40
Conflicts: gobject-introspection-devel < 1.79.1

%description devel
The glib2-devel package includes the header files for the GLib library.

%package doc
Summary: A library of handy utility functions
Requires: %{name}%{?_isa} = %{version}-%{release}

%description doc
The glib2-doc package includes documentation for the GLib library.

%package static
Summary: glib static
Requires: %{name}-devel = %{version}-%{release}
Requires: pcre2-static
Requires: sysprof-capture-static
Requires: libatomic-static

%description static
The %{name}-static subpackage contains static libraries for %{name}.

%package tests
Summary: Tests for the glib2 package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The glib2-tests package contains tests that can be used to verify
the functionality of the installed glib2 package.

%prep
%autosetup -n glib-%{version} -p1

%build
%meson \
    -Dglib_debug=disabled \
    -Ddocumentation=true \
    -Dinstalled_tests=true \
    -Dgnutls=true \
    --default-library=both \
    %{nil}
%meson_build

%install
%meson_install

# Perform byte compilation manually on paths outside the usual locations
%py_byte_compile %{python3} %{buildroot}%{_datadir}

mv %{buildroot}%{_bindir}/gio-querymodules %{buildroot}%{_bindir}/gio-querymodules-%{__isa_bits}
sed -i -e "/^gio_querymodules=/s/gio-querymodules/gio-querymodules-%{__isa_bits}/" %{buildroot}%{_libdir}/pkgconfig/gio-2.0.pc

mkdir -p %{buildroot}%{_libdir}/gio/modules
touch %{buildroot}%{_libdir}/gio/modules/giomodule.cache

%find_lang glib20

%transfiletriggerin -- %{_libdir}/gio/modules
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :

%transfiletriggerpostun -- %{_libdir}/gio/modules
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :

%transfiletriggerin -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%transfiletriggerpostun -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%check
%meson_test

%files -f glib20.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc NEWS README.md
%{_libdir}/libglib-2.0.so.0*
%{_libdir}/libgthread-2.0.so.0*
%{_libdir}/libgmodule-2.0.so.0*
%{_libdir}/libgobject-2.0.so.0*
%{_libdir}/libgio-2.0.so.0*
%{_libdir}/libgirepository-2.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GIRepository-3.0.typelib
%{_libdir}/girepository-1.0/GLib-2.0.typelib
%{_libdir}/girepository-1.0/GLibUnix-2.0.typelib
%{_libdir}/girepository-1.0/GModule-2.0.typelib
%{_libdir}/girepository-1.0/GObject-2.0.typelib
%{_libdir}/girepository-1.0/Gio-2.0.typelib
%{_libdir}/girepository-1.0/GioUnix-2.0.typelib
%dir %{_datadir}/bash-completion
%dir %{bash_completions_dir}
%{bash_completions_dir}/gapplication
%{bash_completions_dir}/gdbus
%{bash_completions_dir}/gio
%{bash_completions_dir}/gsettings
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%dir %{_libdir}/gio
%dir %{_libdir}/gio/modules
%ghost %{_libdir}/gio/modules/giomodule.cache
%{_bindir}/gio
%{_bindir}/gio-querymodules*
%{_bindir}/glib-compile-schemas
%{_bindir}/gsettings
%{_bindir}/gdbus
%{_bindir}/gapplication
%{_libexecdir}/gio-launch-desktop
%{_mandir}/man1/gio.1*
%{_mandir}/man1/gio-querymodules.1*
%{_mandir}/man1/glib-compile-schemas.1*
%{_mandir}/man1/gsettings.1*
%{_mandir}/man1/gdbus.1*
%{_mandir}/man1/gapplication.1*

%files devel
%{_libdir}/lib*.so
%{_libdir}/glib-2.0
%{_includedir}/*
%{_datadir}/aclocal/*
%{_libdir}/pkgconfig/*
%{_datadir}/glib-2.0/dtds
%{_datadir}/glib-2.0/gdb
%{_datadir}/glib-2.0/gettext
%{_datadir}/glib-2.0/schemas/gschema.dtd
%{_datadir}/glib-2.0/valgrind/glib.supp
%{bash_completions_dir}/gresource
%{_bindir}/glib-genmarshal
%{_bindir}/glib-gettextize
%{_bindir}/glib-mkenums
%{_bindir}/gi-compile-repository
%{_bindir}/gi-decompile-typelib
%{_bindir}/gi-inspect-typelib
%{_bindir}/gobject-query
%{_bindir}/gtester
%{_bindir}/gdbus-codegen
%{_bindir}/glib-compile-resources
%{_bindir}/gresource
%{_datadir}/glib-2.0/codegen
%attr (0755, root, root) %{_bindir}/gtester-report
%{_mandir}/man1/glib-genmarshal.1*
%{_mandir}/man1/glib-gettextize.1*
%{_mandir}/man1/glib-mkenums.1*
%{_mandir}/man1/gi-compile-repository.1*
%{_mandir}/man1/gi-decompile-typelib.1*
%{_mandir}/man1/gi-inspect-typelib.1*
%{_mandir}/man1/gobject-query.1*
%{_mandir}/man1/gtester-report.1*
%{_mandir}/man1/gtester.1*
%{_mandir}/man1/gdbus-codegen.1*
%{_mandir}/man1/glib-compile-resources.1*
%{_mandir}/man1/gresource.1*
%{_datadir}/gdb/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GIRepository-3.0.gir
%{_datadir}/gir-1.0/GLib-2.0.gir
%{_datadir}/gir-1.0/GLibUnix-2.0.gir
%{_datadir}/gir-1.0/GModule-2.0.gir
%{_datadir}/gir-1.0/GObject-2.0.gir
%{_datadir}/gir-1.0/Gio-2.0.gir
%{_datadir}/gir-1.0/GioUnix-2.0.gir
%{_datadir}/gettext/
%{_datadir}/systemtap/

%files doc
%{_datadir}/doc/gio-2.0/
%{_datadir}/doc/gio-unix-2.0/
%{_datadir}/doc/girepository-2.0/
%{_datadir}/doc/glib-2.0/
%{_datadir}/doc/glib-unix-2.0/
%{_datadir}/doc/gmodule-2.0/
%{_datadir}/doc/gobject-2.0/

%files static
%{_libdir}/libgio-2.0.a
%{_libdir}/libgirepository-2.0.a
%{_libdir}/libglib-2.0.a
%{_libdir}/libgmodule-2.0.a
%{_libdir}/libgobject-2.0.a
%{_libdir}/libgthread-2.0.a

%files tests
%{_libexecdir}/installed-tests
%{_datadir}/installed-tests

%changelog
%autochangelog
