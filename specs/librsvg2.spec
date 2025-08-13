%bcond_without check

# Use bundled deps as we don't ship the exact right versions for all the
# required rust libraries
%if 0%{?rhel}
%global bundled_rust_deps 1
%else
%global bundled_rust_deps 0
%endif

%global cairo_version 1.18.0

Name:           librsvg2
Summary:        An SVG library based on cairo
Version:        2.60.0
Release:        %autorelease

# librsvg itself is LGPL-2.1-or-later
SourceLicense:  LGPL-2.1-or-later
# ... and its crate dependencies are:
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# LGPL-2.1-or-later
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        LGPL-2.1-or-later AND Apache-2.0 AND BSD-3-Clause AND MIT AND MPL-2.0 AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)
URL:            https://wiki.gnome.org/Projects/LibRsvg
Source0:        https://download.gnome.org/sources/librsvg/2.60/librsvg-%{version}.tar.xz
# upstream dropped vendoring since 2.55.0 (GNOME/librsvg#718), to create:
#   tar xf librsvg-%%{version}.tar.xz ; pushd librsvg-%%{version} ; \
#   cargo vendor --versioned-dirs && tar Jcvf ../librsvg-%%{version}-vendor.tar.xz vendor/ ; popd
Source1:        librsvg-%{version}-vendor.tar.xz

Source2:        filters-composite-04-f-ref.png
Source3:        filters-conv-02-f-ref.png
Source4:        filters-conv-04-f-ref.png

# Patches to build with Fedora-packaged rust crates
Patch:          0001-Fedora-Drop-dependencies-required-for-benchmarking.patch
Patch:          0002-bump-dependencies-to-markup5ever-0.14-xml5ever-0.20.patch

BuildRequires:  gcc
BuildRequires:  meson >= 1.2.0
BuildRequires:  cargo-c >= 0.9.19
BuildRequires:  gi-docgen
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(cairo) >= %{cairo_version}
BuildRequires:  pkgconfig(cairo-gobject) >= %{cairo_version}
BuildRequires:  pkgconfig(cairo-png) >= %{cairo_version}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  vala
BuildRequires:  /usr/bin/rst2man
%if 0%{?bundled_rust_deps}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros
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

%package     -n rsvg-pixbuf-loader
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
%if ! 0%{?bundled_rust_deps}
# use packaged Rust dependencies
%autosetup -p1 -n librsvg-%{version}
%cargo_prep
%else
# use vendored Rust dependencies
%autosetup -N -n librsvg-%{version} -a1
%cargo_prep -v vendor
%endif

# Ensure we build without --locked, as %%cargo_prep removes
# the lock file (Cargo.lock), allowing more wiggle room when
# providing Rust dependencies.
sed -i 's/, "--locked"//g' meson/cargo_wrapper.py

%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
# cargo-c requires all optional dependencies to be available
%cargo_generate_buildrequires -a
%endif

%if ! 0%{?bundled_rust_deps}
cp %{SOURCE2} rsvg/tests/fixtures/reftests/svg1.1/filters-composite-04-f-ref.png
cp %{SOURCE3} rsvg/tests/fixtures/reftests/svg1.1/filters-conv-02-f-ref.png
cp %{SOURCE4} rsvg/tests/fixtures/reftests/svg1.1/filters-conv-04-f-ref.png
%endif

%build
%meson %{?rhel:-Davif=disabled}
%meson_build

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif

%install
%meson_install

# Not useful in this package.
rm -f %{buildroot}%{_pkgdocdir}/COMPILING.md

%if %{with check}
%check
%meson_test
%endif

%files
%doc code-of-conduct.md NEWS README.md
%license COPYING.LIB
%license LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%license cargo-vendor.txt
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
%{_datadir}/vala/vapi/librsvg-2.0.deps
%{_docdir}/Rsvg-2.0

%files -n rsvg-pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader_svg.so
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/librsvg.thumbnailer

%files tools
%{_bindir}/rsvg-convert
%{_mandir}/man1/rsvg-convert.1*

%changelog
%autochangelog
