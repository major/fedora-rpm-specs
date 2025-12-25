# Version of the .so library
%global abi_ver 0.18
%global compat_ver %{abi_ver}
# libliftoff does not bump soname on API changes
%global liftoff_ver 0.5.0

Name:           wlroots%{compat_ver}
Version:        %{compat_ver}.3
Release:        %autorelease
Summary:        A modular Wayland compositor library

# Source files/overall project licensed as MIT, but
# - HPND-sell-variant
#   * protocol/drm.xml
#   * protocol/wlr-data-control-unstable-v1.xml
#   * protocol/wlr-foreign-toplevel-management-unstable-v1.xml
#   * protocol/wlr-gamma-control-unstable-v1.xml
#   * protocol/wlr-input-inhibitor-unstable-v1.xml
#   * protocol/wlr-layer-shell-unstable-v1.xml
#   * protocol/wlr-output-management-unstable-v1.xml
# - LGPL-2.1-or-later
#   * protocol/server-decoration.xml
# Those files are processed to C-compilable files by the
# `wayland-scanner` binary during build and don't alter
# the main license of the binaries linking with them by
# the underlying licenses.
License:        MIT
URL:            https://gitlab.freedesktop.org/wlroots/wlroots
Source0:        %{url}/-/releases/%{version}/downloads/wlroots-%{version}.tar.gz
Source1:        %{url}/-/releases/%{version}/downloads/wlroots-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

# Upstream patches
# https://gitlab.freedesktop.org/wlroots/wlroots/-/merge_requests/5203
Patch:          Fix-discarded-const-qualifier.patch

# Fedora patches
# Following patch is required for phoc.
Patch:          Revert-layer-shell-error-on-0-dimension-without-anch.patch

BuildRequires:  gcc
BuildRequires:  glslang
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.59.0

BuildRequires:  (pkgconfig(libliftoff) >= %{liftoff_ver} with pkgconfig(libliftoff) < 0.6)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm) >= 2.4.122
BuildRequires:  pkgconfig(libinput) >= 1.21.0
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1) >= 0.42.0
BuildRequires:  pkgconfig(vulkan) >= 1.2.182
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.35
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.23
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
# libliftoff does not bump soname on API changes
Requires:       libliftoff%{?_isa} >= %{liftoff_ver}

%description
%{summary}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}
# not required per se, so not picked up automatically by RPM
Recommends:     pkgconfig(xcb-icccm)
# Conflicts with other wlroots-devel packages
Conflicts:      pkgconfig(wlroots)

%description    devel
Development files for %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -N -n wlroots-%{version}
# apply unconditional patches (0..99)
%autopatch -p1 -M99
# apply conditional patches (100..)


%build
MESON_OPTIONS=(
    # Disable options requiring extra/unpackaged dependencies
    -Dexamples=false
)

%{meson} "${MESON_OPTIONS[@]}"
%{meson_build}


%install
%{meson_install}


%check
%{meson_test}


%files
%license LICENSE
%doc README.md
%{_libdir}/libwlroots-%{abi_ver}.so


%files  devel
%{_includedir}/wlroots-%{abi_ver}/wlr
%{_libdir}/pkgconfig/wlroots-%{abi_ver}.pc


%changelog
%autochangelog
