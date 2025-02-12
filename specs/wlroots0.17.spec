# Version of the .so library
%global abi_ver 12
%global compat_ver 0.17
# libliftoff does not bump soname on API changes
%global liftoff_ver %[0%{?fedora} >= 41 ? "0.5.0" : "0.4.1" ]

Name:           wlroots%{compat_ver}
Version:        %{compat_ver}.4
Release:        3%{?dist}
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

# Fedora patches
# Following patch is required for phoc.
Patch:          Revert-layer-shell-error-on-0-dimension-without-anch.patch

BuildRequires:  gcc
BuildRequires:  glslang
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.59.0

BuildRequires:  (pkgconfig(libdisplay-info) >= 0.1.1 with pkgconfig(libdisplay-info) < 0.3)
BuildRequires:  (pkgconfig(libliftoff) >= %{liftoff_ver} with pkgconfig(libliftoff) < 0.6)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdrm) >= 2.4.114
BuildRequires:  pkgconfig(libinput) >= 1.21.0
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1) >= 0.42.0
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.32
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.22
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
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
# apply unconditional patches
%autopatch -p1 -M99
# apply conditional patches


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
%{_libdir}/libwlroots.so.%{abi_ver}*


%files  devel
%{_includedir}/wlr
%{_libdir}/libwlroots.so
%{_libdir}/pkgconfig/wlroots.pc


%changelog
* Mon Feb 10 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.17.4-3
- Rebuild for libdisplay-info 0.2.0

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.17.4-1
- Initialize wlroots0.17 package from rpms/wlroots@17b823e
