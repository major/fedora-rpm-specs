%global forgeurl https://github.com/%{name}/%{name}
%global tag %{version}

Name:       labwc
Version:    0.7.0
Release:    %autorelease
Summary:    Openbox alternative for Wayland

%forgemeta

License:    GPL-2.0-only
URL:        %{forgeurl}
Source0:    %{forgesource}

# Backport pipemenus support
Patch0:     https://github.com/labwc/labwc/pull/1216.patch#/labwc-PR1216.patch

BuildRequires: gcc
BuildRequires: meson >= 0.59.0

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
BuildRequires: (pkgconfig(wlroots) >= 0.17.0 with pkgconfig(wlroots) < 0.18.0)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)

Requires:   xorg-x11-server-Xwayland
Requires:   xdg-desktop-portal-wlr

# Upstream recommendations
# https://github.com/labwc/labwc#6-integration
Recommends: bemenu                      %dnl # Launchers
Recommends: swaylock                    %dnl # Screen locker
Suggests:   fuzzel wofi                 %dnl # Launchers
Suggests:   grim                        %dnl # Screen-shooter
Suggests:   kanshi wlr-randr            %dnl # Output managers
Suggests:   swaybg                      %dnl # Background image
Suggests:   lavalauncher waybar yambar  %dnl # Panel

# Downstream usefull stuff which already packaged in Fedora
Suggests:   wdisplays                   %dnl # GUI display configurator for wlroots compositors


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
%{_datadir}/wayland-sessions/%{name}.desktop
%{_docdir}/%{name}/*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*


%changelog
%autochangelog
