# Version of the .so library
%global abi_ver 10
%global compat_ver 0.15
%global compat_name wlroots

Name:           %{compat_name}%{compat_ver}
Version:        %{compat_ver}.1
Release:        6%{?dist}
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

# Following 3 patches are required for phoc.
Patch0:         Revert-layer-shell-error-on-0-dimension-without-anch.patch
Patch1:         wlroots-0.15.1-wlr_output_layout_contains_point-handle-outputs-that.patch
Patch2:         wlroots-0.15.1-xdg-activation-Deduplicate-token-creation-code.patch
# wlroots/wlroots!3601
Patch3:         wlroots-0.15.1-wlr_output_commit_state-Make-sure-to-clear-the-back-.patch
# https://gitlab.freedesktop.org/wlroots/wlroots/-/commit/f3e1f7b2a70a500b740bfc406e893eba0852699a
Patch4:         wlroots-0.15.1-backend-fix-build-against-upcoming-gcc-14.patch

BuildRequires:  gcc
BuildRequires:  glslang
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.58.1
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(libinput) >= 1.14.0
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libsystemd) >= 237
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.19
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
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
%autosetup -p1 -n %{compat_name}-%{version}


%build
MESON_OPTIONS=(
    # Disable options requiring extra/unpackaged dependencies
    -Dexamples=false
    -Dxcb-errors=disabled
%ifarch s390x
    # Disable -Werror on s390x: https://github.com/swaywm/wlroots/issues/2018
    -Dwerror=false
%endif
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
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 22 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.15.1-5
- Apply patch for GCC 14 `-Werror=calloc-transposed-args` (rhbz#2261793)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.15.1-1
- Initialize wlroots0.15 package from rpms/wlroots@b335d4d
