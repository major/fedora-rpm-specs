%global apiver 15

Name:           weston
Version:        15.0.1
Release:        %autorelease
Summary:        A lightweight and functional Wayland compositor

License:        MIT and CC-BY-SA-3.0
URL:            https://wayland.pages.freedesktop.org/weston/
Source0:        https://gitlab.freedesktop.org/wayland/%{name}/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  glslang
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  lua-devel
BuildRequires:  pam-devel
# ninja-build is a dependency from meson
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(colord) >= 0.1.27
BuildRequires:  pkgconfig(dbus-1) >= 1.6
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freerdp3)
BuildRequires:  pkgconfig(gbm) >= 10.2
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-allocators-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdisplay-info) >= 0.1.1
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput) >= 0.8.0
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseat) >= 0.6.1
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(libudev) >= 136
# libunwind available only on selected arches
%ifarch %{arm} aarch64 hppa ia64 mips ppc %{power64} %{ix86} x86_64
BuildRequires:  libunwind-devel
%endif
BuildRequires:  pkgconfig(libva) >= 0.34.0
BuildRequires:  pkgconfig(libva-drm) >= 0.34.0
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
BuildRequires:  pkgconfig(mtdev) >= 1.1.0
BuildRequires:  (pkgconfig(neatvnc) >= 0.7.0 with pkgconfig(neatvnc) < 0.10.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1) >= 0.25.2
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client) >= 1.22.0
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.33
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.22
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)

Conflicts:      %{name} < 13.0.0-4
Obsoletes:      %{name} < 13.0.0-4
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       mesa-dri-drivers

%description
Weston is a Wayland compositor designed for correctness, reliability,
predictability, and performance.
Out of the box, Weston provides a very basic desktop, or a full-featured
environment for non-desktop uses such as automotive, embedded, in-flight,
industrial, kiosks, set-top boxes and TVs.

%package        session
Summary:        Weston desktop session
Conflicts:      %{name} < 13.0.0-4
Obsoletes:      %{name} < 13.0.0-4
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    session
Weston desktop session.

%package        libs
Summary:        Weston compositor libraries

%description    libs
This package contains Weston compositor libraries.

%package        demo
Summary:        Weston demo program files

%description    demo
This package contains Weston demo program files.

%package        devel
Summary:        Common headers for weston
# Automatically converted from old format: MIT - review is highly recommended.
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Common headers for weston

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
# may be standalone tests can be done
#%%meson_test

%files
%config(noreplace) %{_sysconfdir}/pam.d/weston-remote-access
%license COPYING
%doc README.md
%{_bindir}/weston
%{_bindir}/weston-debug
%{_bindir}/weston-screenshooter
%{_bindir}/weston-tablet
%{_bindir}/weston-terminal
%{_bindir}/wcap-decode
%dir %{_libdir}/weston
%{_libdir}/weston/desktop-shell.so
%{_libdir}/weston/hmi-controller.so
%{_libdir}/weston/ivi-shell.so
%{_libdir}/weston/lua-shell.so
%{_libdir}/weston/systemd-notify.so
%{_libdir}/weston/kiosk-shell.so
%{_libdir}/weston/libexec_weston.so*
%{_libexecdir}/weston-*
%{_libexecdir}/shell.lua
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%dir %{_datadir}/weston
%{_datadir}/weston/*.png
%{_datadir}/weston/wayland.svg

%files session
%{_datadir}/wayland-sessions/weston.desktop

%files libs
%license COPYING
%dir %{_libdir}/libweston-%{apiver}
%{_libdir}/libweston-%{apiver}/color-lcms.so
%{_libdir}/libweston-%{apiver}/drm-backend.so
%{_libdir}/libweston-%{apiver}/gl-renderer.so
%{_libdir}/libweston-%{apiver}/headless-backend.so
%{_libdir}/libweston-%{apiver}/pipewire-backend.so
%{_libdir}/libweston-%{apiver}/pipewire-plugin.so
%{_libdir}/libweston-%{apiver}/remoting-plugin.so
%{_libdir}/libweston-%{apiver}/rdp-backend.so
%{_libdir}/libweston-%{apiver}/vnc-backend.so
%{_libdir}/libweston-%{apiver}/vulkan-renderer.so
%{_libdir}/libweston-%{apiver}/wayland-backend.so
%{_libdir}/libweston-%{apiver}/x11-backend.so
%{_libdir}/libweston-%{apiver}/xwayland.so
%{_libdir}/libweston-%{apiver}.so.0*

%files demo
%license COPYING
%{_bindir}/weston-calibrator
%{_bindir}/weston-clickdot
%{_bindir}/weston-cliptest
%{_bindir}/weston-color
%{_bindir}/weston-constraints
%{_bindir}/weston-dnd
%{_bindir}/weston-editor
%{_bindir}/weston-eventdemo
%{_bindir}/weston-flower
%{_bindir}/weston-fullscreen
%{_bindir}/weston-image
%{_bindir}/weston-multi-resource
%{_bindir}/weston-presentation-shm
%{_bindir}/weston-resizor
%{_bindir}/weston-scaler
%{_bindir}/weston-simple-damage
%{_bindir}/weston-content_protection
%{_bindir}/weston-simple-dmabuf-egl
%{_bindir}/weston-simple-dmabuf-feedback
%{_bindir}/weston-simple-dmabuf-v4l
%{_bindir}/weston-simple-dmabuf-vulkan
%{_bindir}/weston-simple-egl
%{_bindir}/weston-simple-shm
%{_bindir}/weston-simple-timing
%{_bindir}/weston-simple-touch
%{_bindir}/weston-simple-vulkan
%{_bindir}/weston-smoke
%{_bindir}/weston-stacking
%{_bindir}/weston-subsurfaces
%{_bindir}/weston-touch-calibrator
%{_bindir}/weston-transformed

%files devel
%{_includedir}/libweston-%{apiver}/
%{_includedir}/weston/
%{_libdir}/pkgconfig/libweston-%{apiver}.pc
%{_libdir}/pkgconfig/weston.pc
%{_libdir}/libweston-%{apiver}.so
%{_datadir}/pkgconfig/libweston-%{apiver}-protocols.pc
%{_datadir}/libweston-%{apiver}/protocols/

%changelog
%autochangelog
