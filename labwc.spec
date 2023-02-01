Name:       labwc
Version:    0.6.1
Release:    %autorelease
Summary:    Openbox alternative for Wayland

License:    GPLv2
URL:        https://github.com/labwc/labwc
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}.desktop

BuildRequires: gcc
BuildRequires: meson >= 0.59.0

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libinput) >= 1.14
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server) >= 0.19.0
BuildRequires: pkgconfig(wlroots) >= 0.16.0
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)

# Upstream recommendations
# https://github.com/johanmalm/labwc#6-integrate
Recommends: bemenu              %dnl # Launchers
Recommends: swaylock            %dnl # Screen locker
Suggests:   fuzzel wofi         %dnl # Launchers
Suggests:   grim                %dnl # Screen-shooter
Suggests:   kanshi wlr-randr    %dnl # Output managers
Suggests:   swaybg              %dnl # Background image
Suggests:   waybar              %dnl # Panel

# Downstream usefull stuff which already packaged in Fedora
Suggests:   wdisplays           %dnl # GUI display configurator for wlroots compositors
  

%description
Labwc is a wlroots-based stacking compositor for Wayland.

It has the following aims:

  * Be light-weight, small and fast.
  * Use openbox-3.4 specification for configuration and themes.
  * Keep feature set small (ca 40% of openbox).
  * Where practicable, use clients for wall-paper, panel, screenshots, and so
    on.
  * Stay in keeping with wlroots and sway in terms of approach and coding
    style.


%prep
%autosetup -p1


%build
%meson \
    -Dxwayland=enabled \
    %{nil}
%meson_build


%install
%meson_install
install -Dpm 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/wayland-sessions/
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
