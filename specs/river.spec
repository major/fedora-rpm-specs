%global zig_pixman_ver 0.3.0
%global zig_wayland_ver 0.5.0
%global zig_wlroots_ver 0.20.0
%global zig_xkbcommon_ver 0.4.0

Name:           river
Version:        0.4.2
Release:        %autorelease
Summary:        Non-monolithic Wayland compositor

# river: GPL-3.0-only
# common/*.zig: 0BSD
# contrib/river.desktop: 0BSD
# doc/river.1.scd: CC-BY-SA-4.0
# logo/*.svg: CC-BY-SA-4.0
# protocol/river-*.xml: MIT
# protocol/upstream/wlr-layer-shell-unstable-v1.xml: HPND-sell-variant
# protocol/upstream/wlr-output-power-management-unstable-v1.xml: MIT
# deps/zig-pixman: MIT
# deps/zig-wayland: MIT
# deps/zig-wlroots: MIT
# deps/zig-xkbcommon: MIT
License:        GPL-3.0-only AND 0BSD AND CC-BY-SA-4.0 AND HPND-sell-variant AND MIT
URL:            https://codeberg.org/river/river
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# Isaac Freund <mail@isaacfreund.com>
Source2:        https://isaacfreund.com/public_key.txt#/gpgkey-86DED400DDFD7A11.gpg
Source3:        %{name}.desktop
Source4:        https://codeberg.org/ifreund/zig-pixman/archive/v%{zig_pixman_ver}.tar.gz#/zig-pixman-%{zig_pixman_ver}.tar.gz
Source5:        https://codeberg.org/ifreund/zig-wayland/archive/v%{zig_wayland_ver}.tar.gz#/zig-wayland-%{zig_wayland_ver}.tar.gz
Source6:        https://codeberg.org/ifreund/zig-wlroots/archive/v%{zig_wlroots_ver}.tar.gz#/zig-wlroots-%{zig_wlroots_ver}.tar.gz
Source7:        https://codeberg.org/ifreund/zig-xkbcommon/archive/v%{zig_xkbcommon_ver}.tar.gz#/zig-xkbcommon-%{zig_xkbcommon_ver}.tar.gz

ExclusiveArch:  %{zig_arches}

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  scdoc
BuildRequires:  (zig >= 0.15.2 with zig < 0.16)
BuildRequires:  zig-rpm-macros

BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.20)
BuildRequires:  pkgconfig(xkbcommon) >= 1.12.0

# Right now there is no established way of managing Zig dependencies systemwide
# so for the time being they are bundled as part of the project.
Provides:       bundled(zig-pixman) = %{zig_pixman_ver}
Provides:       bundled(zig-wayland) = %{zig_wayland_ver}
Provides:       bundled(zig-wlroots) = %{zig_wlroots_ver}
Provides:       bundled(zig-xkbcommon) = %{zig_xkbcommon_ver}

# Lack of graphical drivers may hurt the common use case
Recommends:     mesa-dri-drivers
# Logind needs polkit to create a graphical session
Recommends:     polkit
# Compatibility layer for X11 applications
Recommends:     xorg-x11-server-Xwayland

%description
River is a non-monolithic Wayland compositor.
Unlike other Wayland compositors, river does not combine the compositor
and window manager into one program. Instead, river defers all window
management policy to a separate window manager implementing the
river-window-management-v1 protocol. This includes window position/size,
pointer/keyboard bindings, focus management, window decorations,
desktop shell graphics, and more.

River itself provides frame perfect rendering, good performance,
support for many Wayland protocol extensions, robust Xwayland support,
the ability to hot-swap window managers, and more.

%package        protocols-devel
Summary:        Protocol files for river, a non-monolithic Wayland compositor
License:        MIT

%description    protocols-devel
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -a 4 -a 5 -a 6 -a 7

%zig_fetch zig-pixman
%zig_fetch zig-wayland
%zig_fetch zig-wlroots
%zig_fetch zig-xkbcommon


%build
%zig_build \
    -Dpie  \
    -Dxwayland


%install
%zig_install \
    -Dpie    \
    -Dxwayland
install -D -m644 -pv %{SOURCE3} %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop


%check
%zig_test


%files
%license LICENSES/0BSD.txt
%license LICENSES/CC-BY-SA-4.0.txt
%license LICENSES/GPL-3.0-only.txt
%license LICENSES/MIT.txt
%doc README.md
%{_bindir}/river
%{_mandir}/man1/river.1*
%{_datadir}/wayland-sessions/%{name}.desktop

%files protocols-devel
%{_datadir}/pkgconfig/river-protocols.pc
%dir %{_datadir}/river-protocols
%dir %{_datadir}/river-protocols/stable
%{_datadir}/river-protocols/stable/*.xml

%changelog
%autochangelog
