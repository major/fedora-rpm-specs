%bcond_without check

# https://github.com/rust-lang/rust/issues/47714
%undefine _strict_symbol_defs_build

# We want verbose builds
%global _configure_disable_silent_rules 1

# Use bundled deps as we don't ship the exact right versions for all the
# required rust libraries
%if 0%{?rhel}
%global bundled_rust_deps 1
%else
%global bundled_rust_deps 0
%endif

%global cairo_version 1.16.0

Name:           librsvg2
Summary:        An SVG library based on cairo
Version:        2.57.0
Release:        %autorelease

# librsvg itself is LGPL-2.1-or-later
SourceLicense:  LGPL-2.1-or-later
# ... and its crate dependencies are:
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR MIT
# BSD-3-Clause
# LGPL-2.1-or-later
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND Unicode-DFS-2016 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://wiki.gnome.org/Projects/LibRsvg
Source0:        https://download.gnome.org/sources/librsvg/2.57/librsvg-%{version}.tar.xz
# upstream dropped vendoring since 2.55.0 (GNOME/librsvg#718), to create:
#   tar xf librsvg-%%{version}.tar.xz ; pushd librsvg-%%{version} ; \
#   cargo vendor && tar Jcvf ../librsvg-%%{version}-vendor.tar.xz vendor/ ; popd
Source1:        librsvg-%{version}-vendor.tar.xz

%if ! 0%{?bundled_rust_deps}
# Patches to build with Fedora-packaged rust crates
Patch:          0001-Fedora-Drop-dependencies-required-for-benchmarking.patch
%endif

# Fix self tests with newer pango
Patch:          0001-1019-Fix-small-caps-and-bump-the-version-of-Pango-re.patch

BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  make
BuildRequires:  pkgconfig(cairo) >= %{cairo_version}
BuildRequires:  pkgconfig(cairo-gobject) >= %{cairo_version}
BuildRequires:  pkgconfig(cairo-png) >= %{cairo_version}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  vala
BuildRequires:  /usr/bin/rst2man
%if 0%{?bundled_rust_deps}
BuildRequires:  rust-toolset
%else
BuildRequires:  rust-packaging
%endif

Requires:       cairo%{?_isa} >= %{cairo_version}
Requires:       cairo-gobject%{?_isa} >= %{cairo_version}
Requires:       rsvg-pixbuf-loader

%description
An SVG library based on cairo.

%package devel
Summary:        Libraries and include files for developing with librsvg
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop with librsvg.

%package -n rsvg-pixbuf-loader
Summary:        SVG image loader for gdk-pixbuf
Requires:       gdk-pixbuf2%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n rsvg-pixbuf-loader
This package provides a gdk-pixbuf plugin for loading SVG images in GTK apps.

%package tools
Summary:        Extra tools for librsvg
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
This package provides extra utilities based on the librsvg library.

%prep
%autosetup -n librsvg-%{version} -p1
%if 0%{?bundled_rust_deps}
# Use the bundled deps
%cargo_prep -V 1
%else
# No bundled deps
rm -vrf vendor .cargo Cargo.lock
sed -i Makefile.am -e 's/$(CARGO) --locked/$(CARGO)/'
%cargo_prep
%endif

%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires
%endif

%build
export CARGO="%__cargo"
%configure --disable-static  \
           --enable-gtk-doc \
           --docdir=%{_pkgdocdir} \
           --enable-introspection \
           --enable-vala
%make_build

%if %{undefined rhel}
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%endif

%install
%make_install
find %{buildroot} -type f -name '*.la' -print -delete

# Remove lib64 rpaths
chrpath --delete %{buildroot}%{_bindir}/rsvg-convert
chrpath --delete %{buildroot}%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-svg.so

# Not useful in this package.
rm -f %{buildroot}%{_pkgdocdir}/COMPILING.md

%if %{with check}
%ifnarch s390x
%check
%make_build check
%endif
%endif

%files
%doc code-of-conduct.md NEWS README.md
%license COPYING.LIB
%if %{undefined rhel}
%license LICENSE.dependencies
%endif
%{_libdir}/librsvg-2.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Rsvg-2.0.typelib

%files devel
%{_libdir}/librsvg-2.so
%{_includedir}/librsvg-2.0/
%{_libdir}/pkgconfig/librsvg-2.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Rsvg-2.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/librsvg-2.0.vapi
%{_docdir}/Rsvg-2.0

%files -n rsvg-pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-svg.so
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/librsvg.thumbnailer

%files tools
%{_bindir}/rsvg-convert
%{_mandir}/man1/rsvg-convert.1*

%changelog
%autochangelog
