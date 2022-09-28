Name:    glib2
Version: 2.74.0
Release: %autorelease
Summary: A library of handy utility functions

License: LGPLv2+
URL:     https://www.gtk.org
Source0: https://download.gnome.org/sources/glib/2.72/glib-%{version}.tar.xz

# Required for RHEL core crypto components policy. Good for Fedora too.
# https://bugzilla.redhat.com/show_bug.cgi?id=1630260
# https://gitlab.gnome.org/GNOME/glib/-/merge_requests/903
Patch0: gnutls-hmac.patch

# Backported from upstream
# https://gitlab.gnome.org/GNOME/glib/-/merge_requests/2921
Patch1: 2921.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gtk-doc
BuildRequires: perl-interpreter
# for sys/inotify.h
BuildRequires: glibc-devel
BuildRequires: libattr-devel
BuildRequires: libselinux-devel
BuildRequires: meson
# for sys/sdt.h
BuildRequires: systemtap-sdt-devel
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(sysprof-capture-4)
BuildRequires: pkgconfig(zlib)
BuildRequires: python3-devel
BuildRequires: /usr/bin/marshalparser

# For gnutls-hmac.patch. We now dlopen libgnutls.so.30 so that we can build a
# static glib2 without depending on a static build of GnuTLS as well. This will
# ensure we notice if the GnuTLS soname bumps, so that we can update our patch.
%if 0%{?__isa_bits} == 64
Requires: libgnutls.so.30()(64bit)
%else
Requires: libgnutls.so.30
%endif

# Remove gamin dependency
Obsoletes: glib2-fam < 2.67.1-3

Provides: bundled(gnulib)
Provides: bundled(gvdb)
Provides: bundled(libcharset)
Provides: bundled(xdgmime)

%description
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality
as an event loop, threads, dynamic loading, and an object system.


%package devel
Summary: A library of handy utility functions
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The glib2-devel package includes the header files for the GLib library.

%package doc
Summary: A library of handy utility functions
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
The glib2-doc package includes documentation for the GLib library.

%package static
Summary: glib static
Requires: %{name}-devel = %{version}-%{release}
Requires: pcre2-static
Requires: sysprof-capture-static

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
    -Dman=true \
    -Ddtrace=true \
    -Dsystemtap=true \
    -Dsysprof=enabled \
    -Dglib_debug=disabled \
    -Dgtk_doc=true \
    -Dinstalled_tests=true \
    -Dgnutls=true \
    --default-library=both \
    %{nil}

%meson_build

%install
%meson_install

# We need reproducible .pyc files across architectures to support multilib installations
# https://bugzilla.redhat.com/show_bug.cgi?id=2008912
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_Appendix/#_byte_compilation_reproducibility
%global py_reproducible_pyc_path %{buildroot}%{_datadir}

# Since this is a generated .py file, set it to a known timestamp
# because the source timestamp is baked into the .pyc file
# Also copy the timestamp for other .py files, because meson doesn't
# do this, see https://github.com/mesonbuild/meson/issues/5027.
touch -r gio/gdbus-2.0/codegen/config.py.in %{buildroot}%{_datadir}/glib-2.0/codegen/*.py

# Perform byte compilation manually to avoid issues with
# irreproducibility of the default invalidation mode, see
# https://www.python.org/dev/peps/pep-0552/ and
# https://bugzilla.redhat.com/show_bug.cgi?id=1686078
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

%files -f glib20.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc NEWS README.md
%{_libdir}/libglib-2.0.so.0*
%{_libdir}/libgthread-2.0.so.0*
%{_libdir}/libgmodule-2.0.so.0*
%{_libdir}/libgobject-2.0.so.0*
%{_libdir}/libgio-2.0.so.0*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/gapplication
%{_datadir}/bash-completion/completions/gdbus
%{_datadir}/bash-completion/completions/gio
%{_datadir}/bash-completion/completions/gsettings
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
%{_datadir}/glib-2.0/gdb
%{_datadir}/glib-2.0/gettext
%{_datadir}/glib-2.0/schemas/gschema.dtd
%{_datadir}/glib-2.0/valgrind/glib.supp
%{_datadir}/bash-completion/completions/gresource
%{_bindir}/glib-genmarshal
%{_bindir}/glib-gettextize
%{_bindir}/glib-mkenums
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
%{_mandir}/man1/gobject-query.1*
%{_mandir}/man1/gtester-report.1*
%{_mandir}/man1/gtester.1*
%{_mandir}/man1/gdbus-codegen.1*
%{_mandir}/man1/glib-compile-resources.1*
%{_mandir}/man1/gresource.1*
%{_datadir}/gdb/
%{_datadir}/gettext/
%{_datadir}/systemtap/

%files doc
%{_datadir}/gtk-doc/

%files static
%{_libdir}/libgio-2.0.a
%{_libdir}/libglib-2.0.a
%{_libdir}/libgmodule-2.0.a
%{_libdir}/libgobject-2.0.a
%{_libdir}/libgthread-2.0.a

%files tests
%{_libexecdir}/installed-tests
%{_datadir}/installed-tests

%changelog
%autochangelog
