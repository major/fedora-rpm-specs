%bcond check    1
%bcond heif     %{undefined rhel}
%bcond jpegxl   %{undefined rhel}

%bcond bundled_rust_deps %{defined:rhel}

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           glycin
Version:        2.0~alpha.6
Release:        %autorelease
Summary:        Sandboxed image rendering

SourceLicense:  MPL-2.0 OR LGPL-2.1-or-later
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND IJG
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# GPL-3.0-or-later
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0 OR LGPL-2.1-or-later
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    (MPL-2.0 OR LGPL-2.1-or-later) AND
    BSD-3-Clause AND
    GPL-3.0-or-later AND
    IJG AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://gitlab.gnome.org/GNOME/glycin
Source0:        https://download.gnome.org/sources/glycin/2.0/glycin-%{tarball_version}.tar.xz

# fixup for issue that makes "cargo tree" fail to parse tests/Cargo.toml
Patch:          0001-fix-invalid-crate-manifest-for-tests-workspace-membe.patch
# https://gitlab.gnome.org/GNOME/glycin/-/issues/101
# https://gitlab.gnome.org/GNOME/glycin/-/merge_requests/143
Patch:          0002-Update-glycin-jxl-to-0.11.1.patch
Patch:          0003-loaders-relax-jpegxl-rs-dependency-from-0.11.1-to-0..patch
# partial revert of https://gitlab.gnome.org/GNOME/glycin/-/commit/f637a7e
Patch:          0004-Replace-serde_yaml_ng-with-equivalent-serde_yaml-dep.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros
%endif

BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0) >= 2.60
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.12
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.52.0
BuildRequires:  pkgconfig(lcms2) >= 2.14
BuildRequires:  pkgconfig(libseccomp) >= 2.5.0

%if %{with heif}
BuildRequires:  pkgconfig(libheif) >= 1.17.0
%endif
%if %{with jpegxl}
BuildRequires:  pkgconfig(libjxl) >= 0.11.0
%endif

%description
Sandboxed and extendable image decoding.


%package        loaders
Summary:        Sandboxed image rendering (image loading backends)

%description    loaders
Sandboxed and extendable image decoding.

This package contains the different image loading backends.

%package        thumbnailer
Summary:        Sandboxed image rendering (thumbnailer)
Requires:       glycin-loaders%{_isa} = %{version}-%{release}

%description    thumbnailer
Sandboxed and extendable image decoding.

This package contains the thumbnailer implementation.

%package        libs
Summary:        Sandboxed image rendering (C library)
Requires:       glycin-loaders%{_isa} = %{version}-%{release}

%description    libs
Sandboxed and extendable image decoding.

This package contains a shared library interface for glycin.

%package        gtk4-libs
Summary:        Sandboxed image rendering (GTK4 integration)
Requires:       glycin-libs%{_isa} = %{version}-%{release}

%description    gtk4-libs
Sandboxed and extendable image decoding.

This package contains a shared library interface for glycin
which provides integration with GDK / GTK4.

%package        devel
Summary:        Sandboxed image rendering (development files)
Requires:       glycin-libs%{_isa} = %{version}-%{release}

%description    devel
Sandboxed and extendable image decoding.

This package contains files for developing against libglycin.

%package        gtk4-devel
Summary:        Sandboxed image rendering (GTK4 development files)
Requires:       glycin-devel%{_isa} = %{version}-%{release}
Requires:       glycin-gtk4-libs%{_isa} = %{version}-%{release}

%description    gtk4-devel
Sandboxed and extendable image decoding.

This package contains files for developing against libglycin-gtk4.


%prep
%autosetup -n glycin-%{tarball_version} -N

%if %{with bundled_rust_deps}
%autopatch -p1 -M 0
%cargo_prep -v vendor
%else
%autopatch -p1
rm -rf vendor
%cargo_prep
%endif

# drop glycin-raw loader (missing dependencies, not enabled by default)
rm -r loaders/glycin-raw


%if %{without bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires -a
%endif


%build
%meson \
    -Dloaders=%{?with_heif:glycin-heif,}glycin-image-rs,%{?with_jpegxl:glycin-jxl,}glycin-svg \
    -Dtest_skip_install=true \
    %{nil}

%meson_build

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%if %{with bundled_rust_deps}
%cargo_vendor_manifest
%endif


%install
%meson_install


%if %{with check}
%check
# tests don't work - fail with "error: NoLoadersConfigured" in build environment
%meson_test || :
%endif


%files loaders
%license LICENSE
%license LICENSE-LGPL-2.1
%license LICENSE-MPL-2.0
%license LICENSE.dependencies
%if %{with bundled_rust_deps}
%license cargo-vendor.txt
%endif

%doc README.md
%doc NEWS
%{_libexecdir}/glycin-loaders/
%{_datadir}/glycin-loaders/

%files thumbnailer
%{_bindir}/glycin-thumbnailer
%dir %{_datadir}/thumbnailers/
%{_datadir}/thumbnailers/*.thumbnailer

%files libs
%{_libdir}/libglycin-2.so.0{,.*}
%{_libdir}/girepository-1.0/Gly-2.typelib

%files gtk4-libs
%{_libdir}/libglycin-gtk4-2.so.0{,.*}
%{_libdir}/girepository-1.0/GlyGtk4-2.typelib

%files devel
%{_includedir}/glycin-2/
%{_libdir}/libglycin-2.so
%{_libdir}/pkgconfig/glycin-2.pc
%{_datadir}/gir-1.0/Gly-2.gir
%{_datadir}/vala/vapi/glycin-2.{deps,vapi}

%files gtk4-devel
%{_includedir}/glycin-gtk4-2/
%{_libdir}/libglycin-gtk4-2.so
%{_libdir}/pkgconfig/glycin-gtk4-2.pc
%{_datadir}/gir-1.0/GlyGtk4-2.gir
%{_datadir}/vala/vapi/glycin-gtk4-2.{deps,vapi}


%changelog
%autochangelog
