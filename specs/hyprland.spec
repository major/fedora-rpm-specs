Name:           hyprland
Version:        0.49.0
Release:        %autorelease
Summary:        Dynamic tiling Wayland compositor that doesn't sacrifice on its looks

# hyprland: BSD-3-Clause
# ./subprojects/udis86: BSD-2-Clause
# ./protocols/kde-server-decoration.xml: LGPL-2.1-or-later
# ./protocols/wayland-drm.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-data-control-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-foreign-toplevel-management-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-gamma-control-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-layer-shell-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-output-management-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/frog-color-management-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/xx-color-management-v4.xml: HPND-sell-variant and/or ntp_disclaimer
License:        BSD-3-Clause AND BSD-2-Clause AND LGPL-2.1-or-later AND HPND-sell-variant
URL:            https://github.com/hyprwm/Hyprland
Source:         %{url}/releases/download/v%{version}/source-v%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  pkgconfig(aquamarine)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(hyprcursor)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
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
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)

# udis86 is packaged in Fedora, but the copy bundled here is actually a
# modified fork.
Provides:       bundled(udis86) = 1.7.2^1.git5336633

Requires:       xorg-x11-server-Xwayland%{?_isa}
Requires:       xdg-desktop-portal%{?_isa}
Requires:       aquamarine%{?_isa} >= 0.8.0
Requires:       hyprcursor%{?_isa} >= 0.1.9
Requires:       hyprutils%{?_isa} >= 0.7.0
Requires:       hyprgraphics%{?_isa} >= 0.1.3

# Used in the default configuration
Recommends:     kitty
Recommends:     wofi
Recommends:     playerctl
Recommends:     brightnessctl
# Lack of graphical drivers may hurt the common use case
Recommends:     mesa-dri-drivers
# Logind needs polkit to create a graphical session
Recommends:     polkit

Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)

%description
Hyprland is a dynamic tiling Wayland compositor that doesn't sacrifice
on its looks. It supports multiple layouts, fancy effects, has a
very flexible IPC model allowing for a lot of customization, a powerful
plugin system and more.

%package        devel
Summary:        Meta package to install dependencies for hyprpm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
Requires:       cpio
Requires:       gcc-c++
Requires:       meson
Requires:       ninja-build
Requires:       pkgconfig(aquamarine)
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(gbm)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(hwdata)
Requires:       pkgconfig(hyprcursor)
Requires:       pkgconfig(hyprgraphics)
Requires:       pkgconfig(hyprlang)
Requires:       pkgconfig(hyprutils)
Requires:       pkgconfig(hyprwayland-scanner)
Requires:       pkgconfig(libdisplay-info)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libinput)
Requires:       pkgconfig(libliftoff)
Requires:       pkgconfig(libseat)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(pango)
Requires:       pkgconfig(pangocairo)
Requires:       pkgconfig(pixman-1)
Requires:       pkgconfig(tomlplusplus)
Requires:       pkgconfig(uuid)
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-protocols)
Requires:       pkgconfig(wayland-server)
Requires:       pkgconfig(xcb-composite)
Requires:       pkgconfig(xcb-dri3)
Requires:       pkgconfig(xcb-errors)
Requires:       pkgconfig(xcb-ewmh)
Requires:       pkgconfig(xcb-icccm)
Requires:       pkgconfig(xcb-present)
Requires:       pkgconfig(xcb-render)
Requires:       pkgconfig(xcb-renderutil)
Requires:       pkgconfig(xcb-res)
Requires:       pkgconfig(xcb-shm)
Requires:       pkgconfig(xcb-util)
Requires:       pkgconfig(xcb-xfixes)
Requires:       pkgconfig(xcb-xinput)
Requires:       pkgconfig(xcb)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xkbcommon)
Requires:       pkgconfig(xwayland)
Recommends:     git-core

%description    devel
%{summary}.


%prep
%autosetup -n %{name}-source -p1
rm -rf subprojects/{tracy,hyprland-protocols}
# don't run generateVersion.sh, release tarballs have pregenerated version.h
sed -i '/scripts\/generateVersion.sh/d' meson.build

cp -p subprojects/udis86/LICENSE LICENSE-udis86


%build
%meson
%meson_build


%install
%meson_install
rm %{buildroot}%{_userunitdir}/hyprland-session.service \
   %{buildroot}%{_datadir}/wayland-sessions/hyprland-systemd.desktop
rm -rf %{buildroot}%{_includedir}/%{name}
rm -rf %{buildroot}%{_datadir}/pkgconfig/%{name}.pc


%files
%license LICENSE LICENSE-udis86
%{_bindir}/hyprctl
%{_bindir}/Hyprland
%{_bindir}/hyprpm
%{_datadir}/hypr/
%{_datadir}/wayland-sessions/%{name}.desktop
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf
%{_mandir}/man1/hyprctl.1*
%{_mandir}/man1/Hyprland.1*
%{bash_completions_dir}/hypr*
%{fish_completions_dir}/hypr*.fish
%{zsh_completions_dir}/_hypr*

%files devel


%changelog
%autochangelog
