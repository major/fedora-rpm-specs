%global forgeurl https://github.com/labwc/labwc
%global tag %{version}

Name:       labwc
Version:    0.8.4
%forgemeta
Release:    %autorelease
Summary:    A Wayland window-stacking compositor

License:    GPL-2.0-only
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildRequires: gcc
BuildRequires: meson >= 0.59.0
BuildRequires: cmake

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libinput) >= 1.14
BuildRequires: pkgconfig(librsvg-2.0) >= 2.46
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server) >= 0.19.0
BuildRequires: pkgconfig(wlroots-0.18) >= 0.18.1
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libsfdo-basedir)

Requires:      mesa-dri-drivers
Requires:      xorg-x11-server-Xwayland
Requires:      xdg-desktop-portal-wlr

Conflicts:     %{name} < 0.8.2-3
Obsoletes:     %{name} < 0.8.2-3

%description
Labwc stands for Lab Wayland Compositor, where lab can mean any of the
following:

  * sense of experimentation and treading new ground
  * inspired by BunsenLabs and ArchLabs
  * your favorite pet

Labwc is a wlroots-based window-stacking compositor for wayland, inspired by
openbox.

It is light-weight and independent with a focus on simply stacking windows
well and rendering some window decorations. It takes a no-bling/frills
approach and says no to features such as icons (except window buttons),
animations, decorative gradients and any other options not required to
reasonably render common themes. It relies on clients for panels, screenshots,
wallpapers and so on to create a full desktop environment.

Labwc tries to stay in keeping with wlroots and sway in terms of general
approach and coding style.

Labwc has no reliance on any particular Desktop Environment, Desktop Shell or
session. Nor does it depend on any UI toolkits such as Qt or GTK.

%package session
Summary:       A Wayland window-stacking compositor - session files
Requires:      %{name} = %{version}-%{release}
Requires:      hicolor-icon-theme
# Upstream recommendations
# https://github.com/labwc/labwc?tab=readme-ov-file#7-integration
# See integration[1] for further details.
# [1]: https://labwc.github.io/integration.html
Recommends:    bemenu                                %dnl # Launchers
Recommends:    swaylock                              %dnl # Screen locker
Suggests:      alacritty                             %dnl # Terminal. See: https://github.com/labwc/labwc?tab=readme-ov-file#6-usage
Suggests:      fuzzel wofi                           %dnl # Launchers
Suggests:      grim                                  %dnl # Screen-shooter
Suggests:      swaybg                                %dnl # Background image
Suggests:      waybar, yambar, lavalauncher, sfwbar  %dnl # Panel
Suggests:      wf-recorder                           %dnl # Screen recorder
Suggests:      wlopm, kanshi, wlr-randr              %dnl # Output managers
# Downstream useful stuff which already packaged in Fedora
Suggests:      foot                                  %dnl # Terminal
Suggests:      wdisplays                             %dnl # GUI display configurator for wlroots compositors

Conflicts:     %{name} < 0.8.2-3
Obsoletes:     %{name} < 0.8.2-3

BuildArch:     noarch

%description session
This package provides the labwc session files to run labwc as a
standalone environment.


%prep
%forgeautosetup -p1


%build
%meson \
    -Dxwayland=enabled \
    %{nil}
%meson_build


%install
%meson_install
%find_lang %{name}


%files -f %{name}.lang
%license LICENSE
%doc NEWS.md
%{_bindir}/%{name}
%{_docdir}/%{name}/*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_datadir}/xdg-desktop-portal/labwc-portals.conf

%files session
%{_datadir}/wayland-sessions/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}*.svg

%changelog
%autochangelog
