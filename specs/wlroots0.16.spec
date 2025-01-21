# Version of the .so library
%global abi_ver 11
%global compat_ver 0.16
%global compat_name wlroots

Name:           %{compat_name}%{compat_ver}
Version:        %{compat_ver}.2
Release:        4%{?dist}
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
#   * protocol/idle.xml
#   * protocol/server-decoration.xml
# Those files are processed to C-compilable files by the
# `wayland-scanner` binary during build and don't alter
# the main license of the binaries linking with them by
# the underlying licenses.
License:        MIT
URL:            https://gitlab.freedesktop.org/wlroots/wlroots
Source0:        %{url}/-/releases/%{version}/downloads/%{compat_name}-%{version}.tar.gz
Source1:        %{url}/-/releases/%{version}/downloads/%{compat_name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

# Upstream patches
Patch0:         %{url}/-/commit/f3ba14e491333d6bbba8c60328c4dbfd20571182.patch#/wlroots-0.16.2-render-vulkan-remove-hardcoded-validation-layers.patch
# https://gitlab.freedesktop.org/wlroots/wlroots/-/commit/f3e1f7b2a70a500b740bfc406e893eba0852699a
Patch1:         wlroots-0.16.2-backend-fix-build-against-upcoming-gcc-14.patch

# Fedora patches
# Following patch is required for phoc.
Patch10:        Revert-layer-shell-error-on-0-dimension-without-anch.patch

BuildRequires:  gcc
BuildRequires:  glslang
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdrm) >= 2.4.113
BuildRequires:  pkgconfig(libinput) >= 1.21.0
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.27
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.21
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)

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
%autosetup -N -n %{compat_name}-%{version}
# apply unconditional patches
%autopatch -p1 -M19
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
%{_libdir}/lib%{compat_name}.so.%{abi_ver}*


%files  devel
%{_includedir}/wlr
%{_libdir}/lib%{compat_name}.so
%{_libdir}/pkgconfig/%{compat_name}.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 06 2023 Aleksei Bavshin <alebastr89@gmail.com> - 0.16.2-1
- Initialize wlroots0.16 package from rpms/wlroots@0a1c111
