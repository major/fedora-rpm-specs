%bcond_without check

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           glycin-loaders
Version:        0.1~beta.2
Release:        %autorelease
Summary:        Sandboxed image rendering

# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-3-Clause
# CC0-1.0
# LGPL-2.1-only
# LGPL-2.1-or-later
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
# LICENSE.dependencies contains a full license breakdown
URL:            https://gitlab.gnome.org/sophie-h/glycin
Source0:        https://download.gnome.org/sources/glycin-loaders/0.1/glycin-loaders-%{tarball_version}.tar.xz
# Fedora-packaged rust-image doesn't have openexr and qoi support
Patch:          image-rs-missing-decoders.patch

BuildRequires:  cargo-rpm-macros
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)

%description
Sandboxed and extendable image decoding.


%prep
%autosetup -p1 -n glycin-loaders-%{tarball_version}

rm -rf vendor
%cargo_prep

# libheif and jxl rust wrappers aren't packaged yet
sed -i -e '/glycin-heif/d' -e '/glycin-jxl/d' Cargo.toml


%generate_buildrequires
%cargo_generate_buildrequires


%build
%meson -Dloaders=glycin-image-rs,glycin-svg
%meson_build

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies


%install
%meson_install


%if %{with check}
%check
%meson_test
%endif


%files
%license LICENSE
%license LICENSE.dependencies
%doc NEWS README.md
%{_libexecdir}/glycin-loaders/
%{_datadir}/glycin-loaders/


%changelog
%autochangelog
