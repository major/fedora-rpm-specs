# Version of the .so library
%global abi_ver 9
%global compat_ver 0.14
%global compat_name wlroots

Name:           %{compat_name}%{compat_ver}
Version:        %{compat_ver}.1
Release:        5%{?dist}
Summary:        A modular Wayland compositor library

# Source files/overall project licensed as MIT, but
# - LGPLv2.1+
#   * protocol/idle.xml
#   * protocol/server-decoration.xml
# Those files are processed to C-compilable files by the
# `wayland-scanner` binary during build and don't alter
# the main license of the binaries linking with them by
# the underlying licenses.
License:        MIT
URL:            https://github.com/swaywm/%{compat_name}
Source0:        %{url}/releases/download/%{version}/%{compat_name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{compat_name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
# https://gitlab.freedesktop.org/wlroots/wlroots/-/issues/3189
Patch0:         output-don-t-leave-dangling-cursor_front_buffer.patch
# Revert initial size check of layer surface
# Requested by Mobility SIG to work around phosh compatibility issue
# https://gitlab.gnome.org/World/Phosh/phosh/-/issues/422
Patch1:         Revert-layer-shell-error-on-0-dimension-without-anchors.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm) >= 2.4.105
BuildRequires:  pkgconfig(libinput) >= 1.14.0
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libsystemd) >= 237
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.21
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
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.14.1-1
- Initialize compat wlroots0.14 package from wlroots@6e6fd85
