%global cinnamon_desktop_version 6.7.3

%global upstream_version 6.7.4-unstable

Name:           cinnamon-settings-daemon
Version:        6.7.4^unstable
Release:        %autorelease
Summary:        The daemon sharing settings from CINNAMON to GTK+/KDE applications

License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND MIT
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz

ExcludeArch:    %{ix86}

BuildSystem:   meson
BuildOption(conf): -Duse_smartcard=disabled
BuildOption(conf): -Dgtk_layer_shell=true
%ifarch s390 s390x
BuildOption(conf): -Duse_wacom=disabled
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires:  pkgconfig(colord) >= 0.1.27
BuildRequires:  pkgconfig(cups) >= 1.4
BuildRequires:  pkgconfig(cvc) >= %{cinnamon_desktop_version}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libnotify) >= 0.7.3
BuildRequires:  pkgconfig(pango) >= 1.20.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  pkgconfig(libpulse) >= 0.9.16
BuildRequires:  pkgconfig(upower-glib) >= 0.99.11
%ifnarch s390 s390x
BuildRequires:  pkgconfig(libwacom) >= 0.7
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.36.2
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(lcms2) >= 2.2
BuildRequires:  pkgconfig(libsystemd)

# add hard cinnamon-desktop required version due logind schema
Requires:       cinnamon-desktop%{?_isa} >= %{cinnamon_desktop_version}
Requires:       colord%{?_isa}
Requires:       iio-sensor-proxy%{?_isa}

%description
A daemon to share settings from CINNAMON to other applications. It also
handles global keybindings, and many of desktop-wide settings.

%prep
%autosetup -p1 -n %{name}-%{upstream_version}

%install -a
desktop-file-install --delete-original           \
  --dir %{buildroot}%{_sysconfdir}/xdg/autostart/  \
  %{buildroot}%{_sysconfdir}/xdg/autostart/*

# Remove script
rm -rf %{buildroot}%{_datadir}/cinnamon-settings-daemon-3.0/

# Delete csd symlinks
rm -rf %{buildroot}%{_libdir}/cinnamon-settings-daemon/


%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/*.desktop

%files
%doc AUTHORS
%license COPYING COPYING.LIB
%{_bindir}/csd-*
%config(noreplace) %{_sysconfdir}/xdg/autostart/*
%{_libexecdir}/csd-a11y-settings
%{_libexecdir}/csd-automount
%{_libexecdir}/csd-backlight-helper
%{_libexecdir}/csd-clipboard
%{_libexecdir}/csd-color
%{_libexecdir}/csd-datetime-mechanism
%{_libexecdir}/csd-housekeeping
%{_libexecdir}/csd-input-helper
%{_libexecdir}/csd-keyboard
%{_libexecdir}/csd-media-keys
%{_libexecdir}/csd-power
%{_libexecdir}/csd-printer
%{_libexecdir}/csd-print-notifications
%{_libexecdir}/csd-screensaver-proxy
%{_libexecdir}/csd-settings-remap
%{_libexecdir}/csd-xsettings
%ifnarch s390 s390x
%{_libexecdir}/csd-wacom-oled-helper
%{_libexecdir}/csd-wacom-led-helper
%{_libexecdir}/csd-wacom
%endif
%{_datadir}/dbus-1/system.d/org.cinnamon.SettingsDaemon.DateTimeMechanism.conf
%{_datadir}/dbus-1/system-services/org.cinnamon.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/glib-2.0/schemas/org.cinnamon.settings-daemon*.xml
%{_datadir}/icons/hicolor/*/apps/csd-*
%{_datadir}/polkit-1/actions/org.cinnamon.settings*.policy

%changelog
%autochangelog