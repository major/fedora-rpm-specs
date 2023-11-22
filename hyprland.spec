Name:           hyprland
Version:        0.32.3
Release:        %autorelease
Summary:        Dynamic tiling Wayland compositor that doesn't sacrifice on its looks

# hyprland: BSD-3-Clause
# subprojects/hyprland-protocols: BSD-3-Clause
# subprojects/wlroots: MIT
# subproject/udis86: BSD-2-Clause
# protocols/ext-workspace-unstable-v1.xml: HPND-sell-variant
# protocols/wlr-foreign-toplevel-management-unstable-v1.xml: HPND-sell-variant
# protocols/wlr-layer-shell-unstable-v1.xml: HPND-sell-variant
# protocols/idle.xml: LGPL-2.1-or-later
License:        BSD-3-Clause AND MIT AND BSD-2-Clause AND HPND-sell-variant AND LGPL-2.1-or-later
URL:            https://github.com/hyprwm/Hyprland
Source:         %{url}/releases/download/v%{version}/source-v%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  jq
BuildRequires:  meson

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput) >= 1.23.0
BuildRequires:  pkgconfig(libliftoff) >= 0.4.1
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1) >= 0.42.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.22.0
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-dri3)
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

# Upstream insists on always building against very current snapshots of
# wlroots, and doesn't provide a method for building against a system copy.
# https://github.com/hyprwm/Hyprland/issues/302
Provides:       bundled(wlroots) = 0.17.0~^1.git5de9e1a

# udis86 is packaged in Fedora, but the copy bundled here is actually a
# modified fork.
Provides:       bundled(udis86) = 1.7.2^1.git5336633

Requires:       xorg-x11-server-Xwayland%{?_isa}
Requires:       xdg-desktop-portal%{?_isa}

# Both are used in the default configuration
Recommends:     kitty
Recommends:     wofi
# Lack of graphical drivers may hurt the common use case
Recommends:     mesa-dri-drivers
# Logind needs polkit to create a graphical session
Recommends:     polkit

Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)

%description
Hyprland is a dynamic tiling Wayland compositor based on wlroots that doesn't
sacrifice on its looks. It supports multiple layouts, fancy effects, has a
very flexible IPC model allowing for a lot of customization, a powerful
plugin system and more.

%package        devel
Summary:        Header files for %{name}
License:        BSD-3-Clause AND MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(gbm)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(hwdata)
Requires:       pkgconfig(hyprland-protocols)
Requires:       pkgconfig(libdisplay-info)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libinput) >= 1.23.0
Requires:       pkgconfig(libliftoff) >= 0.4.1
Requires:       pkgconfig(libseat)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(pango)
Requires:       pkgconfig(pangocairo)
Requires:       pkgconfig(pixman-1) >= 0.42.0
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-protocols)
Requires:       pkgconfig(wayland-scanner)
Requires:       pkgconfig(wayland-server) >= 1.22.0
Requires:       pkgconfig(xcb)
Requires:       pkgconfig(xcb-composite)
Requires:       pkgconfig(xcb-dri3)
Requires:       pkgconfig(xcb-icccm)
Requires:       pkgconfig(xcb-present)
Requires:       pkgconfig(xcb-render)
Requires:       pkgconfig(xcb-renderutil)
Requires:       pkgconfig(xcb-res)
Requires:       pkgconfig(xcb-shm)
Requires:       pkgconfig(xcb-xfixes)
Requires:       pkgconfig(xcb-xinput)
Requires:       pkgconfig(xkbcommon)
Requires:       pkgconfig(xwayland)

%description    devel
%{summary}.


%prep
%autosetup -n %{name}-source -p1
rm -rf subprojects/{tracy,hyprland-protocols}

cp -p subprojects/udis86/LICENSE LICENSE-udis86
cp -p subprojects/wlroots/LICENSE LICENSE-wlroots


%build
%meson \
       -Dwlroots:examples=false \
       -Dwlroots:xcb-errors=disabled
%meson_build


%install
%meson_install
rm %{buildroot}%{_libdir}/libwlroots.a
rm %{buildroot}%{_libdir}/pkgconfig/wlroots.pc
mkdir -p %{buildroot}%{_includedir}/%{name}/wlroots/wlr
mv %{buildroot}%{_includedir}/wlr %{buildroot}%{_includedir}/%{name}/wlroots


%check
desktop-file-validate %{buildroot}/%{_datadir}/wayland-sessions/%{name}.desktop


%files
%license LICENSE LICENSE-udis86 LICENSE-wlroots
%{_bindir}/Hyprland
%{_bindir}/hyprctl
%{_mandir}/man1/Hyprland.1*
%{_mandir}/man1/hyprctl.1*
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/%{name}.desktop
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf

%files devel
%{_includedir}/%{name}/
%{_datadir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
