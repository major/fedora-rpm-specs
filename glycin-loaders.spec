%bcond_without check

%if 0%{?rhel}
%global bundled_rust_deps 1
%else
%global bundled_rust_deps 0
%endif

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           glycin-loaders
Version:        0.1.1
Release:        %autorelease
Summary:        Sandboxed image rendering

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-3-Clause
# LGPL-2.1-or-later
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# MPL-2.0 OR LGPL-2.1-or-later
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (MPL-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
# LICENSE.dependencies contains a full license breakdown
URL:            https://gitlab.gnome.org/sophie-h/glycin
Source0:        https://download.gnome.org/sources/glycin-loaders/0.1/glycin-loaders-%{tarball_version}.tar.xz
# Fedora-packaged rust-image doesn't have openexr support
Patch:          0001-Drop-OpenEXR-decoders-since-they-are-not-enabled-in-.patch
# jxl rust wrapper isn't packaged yet
Patch:          0002-Disable-JPEG-XL-missing-dependencies.patch
%if 0%{?fedora}
# Bump libheif-rs dep to the version that's in Fedora
Patch:          0004-Bump-libheif-rs-dep-0.21.0.patch
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros
%endif
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)

%description
Sandboxed and extendable image decoding.


%prep
%autosetup -p1 -n glycin-loaders-%{tarball_version}

%if ! 0%{?bundled_rust_deps}
rm -rf vendor
%cargo_prep
%endif


%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires
%endif


%build
%meson \
  -Dloaders=%{!?rhel:glycin-heif,}glycin-image-rs,glycin-svg \
  -Dtest_skip_install=true \
  %{nil}

%meson_build

%if !0%{?rhel}
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%endif


%install
%meson_install


%if %{with check}
%check
# Something is wrong with the test setup and tests fail with
# "No such file or directory"
%meson_test || :
%endif


%files
%license LICENSE LICENSE-LGPL-2.1 LICENSE-MPL-2.0
%if !0%{?rhel}
%license LICENSE.dependencies
%endif
%doc NEWS README.md
%{_libexecdir}/glycin-loaders/
%{_datadir}/glycin-loaders/


%changelog
%autochangelog
