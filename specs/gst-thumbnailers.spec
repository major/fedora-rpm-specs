%global upstream_version %%(echo %{version} | tr '~' '.')

Name:           gst-thumbnailers
Version:        1.0~rc
Release:        %autorelease
Summary:        GStreamer Thumbnailers

SourceLicense:  GPL-3.0-or-later
# Rust dependencies:
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception
# BSD-3-Clause OR Apache-2.0
# GPL-3.0-or-later
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
    GPL-3.0-or-later
    AND Apache-2.0 WITH LLVM-exception
    AND MIT
    AND (Apache-2.0 OR MIT)
    AND (BSD-3-Clause OR Apache-2.0)
    AND (Unlicense OR MIT)
    AND (Zlib OR Apache-2.0 OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://gitlab.gnome.org/GNOME/gst-thumbnailers
Source:         %{url}/-/archive/%{upstream_version}/gst-thumbnailers-%{upstream_version}.tar.gz

Patch:          0001-meson-adapt-for-RPM-package-build-environment.patch
Patch:          0002-cargo-drop-benchmarks-and-benchmark-only-dependencie.patch

BuildRequires:  cargo-rpm-macros
BuildRequires:  meson >= 1.2

BuildRequires:  pkgconfig(glycin-2) >= 2.0.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.26.0

# GStreamer plugin dependencies (tests)
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  gstreamer1-plugins-good

# GStreamer plugin dependencies (runtime)
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good

%description
%{summary}.

%prep
%autosetup -n gst-thumbnailers-%{upstream_version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%meson
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%meson_install

%check
%ifnarch s390x
# https://gitlab.gnome.org/GNOME/gst-thumbnailers/-/issues/17
%meson_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%doc NEWS
%{_bindir}/gst-audio-thumbnailer
%{_bindir}/gst-video-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gst-audio-thumbnailer.thumbnailer
%{_datadir}/thumbnailers/gst-video-thumbnailer.thumbnailer

%changelog
%autochangelog
