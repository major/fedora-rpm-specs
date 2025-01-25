%bcond_without check

%bcond bundled_rust_deps %{defined:rhel}

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           loupe
Version:        47.4
Release:        %autorelease
Summary:        Image viewer

# loupe: GPL-3.0-or-later
# Rust dependencies:
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# GPL-3.0-or-later
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MPL-2.0 OR LGPL-2.1-or-later
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        GPL-3.0-or-later AND BSD-2-Clause AND ISC AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (MPL-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown
URL:            https://gitlab.gnome.org/GNOME/loupe
Source0:        https://download.gnome.org/sources/loupe/47/loupe-%{tarball_version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros
%endif
BuildRequires:  itstool
BuildRequires:  meson
%if %{with bundled_rust_deps}
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libseccomp)
%endif
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

# For /usr/share/dbus-1/services directory
Requires:       dbus
# Image loaders used by loupe
Requires:       glycin-loaders >= 1.1
# For hicolor icon theme directories
Requires:       hicolor-icon-theme

%description
An image viewer application written with GTK 4, Libadwaita and Rust.

Features:

- Fast GPU accelerated image rendering with tiled rendering for SVGs
- Extendable and sandboxed (expect SVG) image decoding
- Support for more than 15 image formats by default
- Extensive support for touchpad and touchscreen gestures
- Accessible presentation of the most important metadata
- Sleek but powerful interface developed in conjunction with GNOME Human
  Interface Guidelines


%prep
%autosetup -p1 -n loupe-%{tarball_version}

%if %{with bundled_rust_deps}
%cargo_prep -v vendor
%else
rm -rf vendor
sed -i -e '/Cargo.lock/d' meson.build
%cargo_prep
%endif


%if %{without bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires -f x11
%endif


%build
%meson
%meson_build

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if %{with bundled_rust_deps}
%cargo_vendor_manifest
%endif


%install
%meson_install

%find_lang loupe --with-gnome


%if %{with check}
%check
%meson_test

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.Loupe.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Loupe.desktop
%endif


%files -f loupe.lang
%license COPYING.md
%license LICENSE.dependencies
%if %{with bundled_rust_deps}
%license cargo-vendor.txt
%endif
%doc NEWS README.md
%{_bindir}/loupe
%{_datadir}/applications/org.gnome.Loupe.desktop
%{_datadir}/dbus-1/services/org.gnome.Loupe.service
%{_datadir}/glib-2.0/schemas/org.gnome.Loupe.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Loupe*.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Loupe-symbolic.svg
%{_metainfodir}/org.gnome.Loupe.metainfo.xml


%changelog
%autochangelog
