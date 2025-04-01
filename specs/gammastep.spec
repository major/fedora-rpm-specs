Name:           gammastep
Version:        2.0.11
Release:        %autorelease
Summary:        Adjusts the color temperature of your screen according to time of day

# src/gamma-control.xml is licensed under HPND-sell-variant
License:        GPL-3.0-or-later AND HPND-sell-variant
URL:            https://gitlab.com/chinstrap/gammastep
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0) >= 2.26
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner) >= 1.15.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  python3-devel >= 3.2
BuildRequires:  systemd-rpm-macros

Requires:       hicolor-icon-theme

%description
Gammastep adjusts the color temperature of your screen according to your
surroundings. This may help your eyes hurt less if you are working in front
of the screen at night.

The color temperature is set according to the position of the sun. A different
color temperature is set during night and daytime. During twilight and early
morning, the color temperature transitions smoothly from night to daytime
temperature to allow your eyes to slowly adapt.

Gammastep supports wlr-gamma-control-unstable-v1 protocol for wlroots-based
wayland compositors.

%package        indicator
Summary:        GTK indicator applet for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3
Requires:       libappindicator-gtk3
Requires:       python3dist(pygobject)
Requires:       python3dist(pyxdg)

%description    indicator
This package provides a status icon for %{name} that allows the user
to control color temperature.


%prep
%autosetup -p1 -n %{name}-v%{version}


%build
./bootstrap
%configure \
    --with-systemduserunitdir=%{_userunitdir}
%make_build


%install
%make_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
%systemd_user_post %{name}.service

%post indicator
%systemd_user_post %{name}-indicator.service

%preun
%systemd_user_preun %{name}.service

%preun indicator
%systemd_user_preun %{name}-indicator.service


%files -f %{name}.lang
%license COPYING
%doc README.md %{name}.conf.sample
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_userunitdir}/%{name}.service

%files indicator
%{_bindir}/%{name}-indicator
%{_datadir}/applications/%{name}-indicator.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}-status-*.svg
%{_metainfodir}/%{name}-indicator.appdata.xml
%{_userunitdir}/%{name}-indicator.service
%{python3_sitelib}/%{name}_indicator/


%changelog
%autochangelog
