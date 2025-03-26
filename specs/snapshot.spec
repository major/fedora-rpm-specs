%bcond_without check

%if 0%{?rhel}
%global bundled_rust_deps 1
%else
%global bundled_rust_deps 0
%endif

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           snapshot
Version:        48.0.1
Release:        %autorelease
Summary:        Take pictures and videos

# snapshot: GPL-3.0-or-later
# Rust dependencies:
# (MIT OR Apache-2.0) AND ISC
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# GPL-3.0-or-later
# ISC
# MIT
# MIT OR Apache-2.0
# MPL-2.0 OR LGPL-2.1-or-later
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    GPL-3.0-or-later AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MPL-2.0 OR LGPL-2.1-or-later) AND
    (Unlicense OR MIT) AND
    (Zlib OR Apache-2.0 OR MIT)
}
# LICENSE.dependencies contains a full license breakdown
URL:            https://gitlab.gnome.org/GNOME/snapshot
Source:         https://download.gnome.org/sources/snapshot/48/snapshot-%{tarball_version}.tar.xz

# Downstream patch to disable linting as part of self tests
Patch:          0001-Disable-cargo-clippy-test.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros
%endif
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

# For camerabin GStreamer element
Requires:       gstreamer1-plugins-bad-free%{_isa}
# For gtk4 GStreamer element
Requires:       gstreamer1-plugin-gtk4%{_isa}
# Image loaders used by snapshot
Requires:       glycin-loaders >= 1.1
# For hicolor icon theme directories
Requires:       hicolor-icon-theme

Provides:       bundled(crate(aperture)) = 0.7.0

%description
Take pictures and videos on your computer, tablet, or phone.


%prep
%autosetup -p1 -n snapshot-%{tarball_version}

%if 0%{?bundled_rust_deps}
%cargo_prep -v vendor
%else
rm -rf vendor
%cargo_prep
%endif


%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires -a
cd aperture
%cargo_generate_buildrequires -a
cd ~-
%endif


%build
%meson
%meson_build

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif


%install
%meson_install

%find_lang snapshot --with-gnome


%if %{with check}
%check
%meson_test \
%ifarch riscv64
    --timeout-multiplier 10 \
%endif
    %{nil}

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.Snapshot.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Snapshot.desktop
%endif


%files -f snapshot.lang
%license LICENSE
%license LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%license cargo-vendor.txt
%endif
%doc README.md
%{_bindir}/snapshot
%{_datadir}/applications/org.gnome.Snapshot.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Snapshot.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Snapshot*.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Snapshot-symbolic.svg
%{_datadir}/snapshot/
%{_metainfodir}/org.gnome.Snapshot.metainfo.xml


%changelog
%autochangelog
