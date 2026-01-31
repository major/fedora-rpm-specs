%global glib2_version 2.70.0

%global with_mingw 0

%if 0%{?fedora}
%global with_mingw 1
%endif

Name:    libsoup3
Version: 3.6.5
Release: %autorelease
Summary: Soup, an HTTP library implementation

License: LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://wiki.gnome.org/Projects/libsoup
Source0: https://download.gnome.org/sources/libsoup/3.6/libsoup-%{version}.tar.xz

# https://bugzilla.redhat.com/show_bug.cgi?id=2367183
Patch:   CVE-2025-4948.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2359343
Patch:   CVE-2025-32908.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2359342
Patch:   CVE-2025-32907.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2367552
Patch:   CVE-2025-4969.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2367175
Patch:   CVE-2025-4945.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2366513
Patch:   CVE-2025-4476.patch
Patch:   475.patch
Patch:   0c8c8795f08abb95161c610a0a6dff22d45742d4.patch
Patch:   0001-tld-test-update-after-changes-in-the-public-suffix-l.patch

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

%if %{with_mingw}
BuildRequires: mingw32-filesystem >= 107
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gcc
BuildRequires: mingw32-glib2
BuildRequires: mingw32-brotli
BuildRequires: mingw32-libpsl
BuildRequires: mingw32-sqlite
BuildRequires: mingw32-libnghttp2

BuildRequires: mingw64-filesystem >= 107
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils
BuildRequires: mingw64-glib2
BuildRequires: mingw64-brotli
BuildRequires: mingw64-libpsl
BuildRequires: mingw64-sqlite
BuildRequires: mingw64-libnghttp2
%endif

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

%if %{with_mingw}

%package -n mingw32-libsoup3
Summary: MinGW library for HTTP functionality
Recommends: mingw32-glib-networking

%description -n mingw32-libsoup3
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of libsoup3

%package -n mingw64-libsoup3
Summary: MinGW library for HTTP functionality
Recommends: mingw64-glib-networking

%description -n mingw64-libsoup3
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

This is the MinGW build of libsoup3

%{?mingw_debug_package}

%endif

%prep
%autosetup -p1 -n libsoup-%{version}

%build
%meson -Ddocs=enabled -Dautobahn=disabled
%meson_build

%if %{with_mingw}
%mingw_meson \
    -Ddocs=disabled \
    -Dintrospection=disabled \
    -Dtests=false \
    -Dtls_check=false \
    -Dvapi=disabled
%endif

%install
%meson_install
install -m 644 -D tests/libsoup.supp %{buildroot}%{_datadir}/libsoup-3.0/libsoup.supp

%if %{with_mingw}
%mingw_ninja_install
%mingw_find_lang libsoup-3.0
%mingw_debug_install_post
%endif

%find_lang libsoup-3.0

%ifnarch s390x
%check
%meson_test
%endif

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

%if %{with_mingw}
%files -n mingw32-libsoup3 -f mingw32-libsoup-3.0.lang
%license COPYING
%doc README NEWS AUTHORS
%{mingw32_bindir}/libsoup-3.0-0.dll
%{mingw32_includedir}/libsoup-3.0
%{mingw32_libdir}/libsoup-3.0.dll.a
%{mingw32_libdir}/pkgconfig/libsoup-3.0.pc

%files -n mingw64-libsoup3 -f mingw64-libsoup-3.0.lang
%license COPYING
%doc README NEWS AUTHORS
%{mingw64_bindir}/libsoup-3.0-0.dll
%{mingw64_includedir}/libsoup-3.0
%{mingw64_libdir}/libsoup-3.0.dll.a
%{mingw64_libdir}/pkgconfig/libsoup-3.0.pc
%endif

%changelog
%autochangelog
