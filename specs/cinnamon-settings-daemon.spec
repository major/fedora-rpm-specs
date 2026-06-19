%global cinnamon_desktop_version 6.7.0

%global upstream_version 6.7.1-unstable

Name:           cinnamon-settings-daemon
Version:        6.7.1^unstable
Release:        1%{?dist}
Summary:        The daemon sharing settings from CINNAMON to GTK+/KDE applications

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz

ExcludeArch:    %{ix86}

# add hard cinnamon-desktop required version due logind schema
Requires:       cinnamon-desktop%{?_isa} >= %{cinnamon_desktop_version}
Requires:       colord%{?_isa}
Requires:       iio-sensor-proxy%{?_isa}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
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
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(pango) >= 1.20.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  pkgconfig(libpulse) >= 0.9.16
BuildRequires:  pkgconfig(upower-glib) >= 0.9.11
%ifnarch s390 s390x %{?rhel:ppc ppc64}
BuildRequires:  pkgconfig(libwacom) >= 0.7
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.36.2
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(lcms2) >= 2.2
BuildRequires:  pkgconfig(libsystemd)

%description
A daemon to share settings from CINNAMON to other applications. It also
handles global keybindings, and many of desktop-wide settings.

%prep
%autosetup -p1 -n %{name}-%{upstream_version}

%build
%meson \
 -Duse_smartcard=disabled \
 -Dgtk_layer_shell=true \
%ifarch s390 s390x %{?rhel:ppc ppc64}
 -Duse_wacom=disabled
%endif

%meson_build

%install
%meson_install

desktop-file-install --delete-original           \
  --dir %{buildroot}%{_sysconfdir}/xdg/autostart/  \
  %{buildroot}%{_sysconfdir}/xdg/autostart/*

# Remove script
rm -rf %{buildroot}%{_datadir}/cinnamon-settings-daemon-3.0/

# Delete csd symlinks
rm -rf %{buildroot}%{_libdir}/cinnamon-settings-daemon/


%files
%doc AUTHORS
%license COPYING COPYING.LIB
%{_bindir}/csd-*
%config %{_sysconfdir}/xdg/autostart/*
%{_libexecdir}/csd-a11y-settings
%{_libexecdir}/csd-automount
%{_libexecdir}/csd-background
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
%ifnarch s390 s390x %{?rhel:ppc ppc64}
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
* Wed Jun 17 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.1^unstable-1
- Update to 6.7.1-unstable

* Tue Apr 14 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.0^unstable-2
- Enable gtk_layer_shell

* Mon Apr 13 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.0^unstable-1
- Update to 6.7.0-unstable

* Thu Feb 12 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.3-1
- Update to 6.6.3

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jan 08 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Thu Dec 11 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.1-1
- Update to 6.6.1

* Thu Nov 27 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 20 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Tue Dec 10 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.1-2
- Add requires colord, it is needed for nightlight

* Mon Dec 02 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.1-1
- Update t0 6.4.1

* Wed Nov 27 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Thu Nov 14 2024 Leigh Scott <leigh123linux@gmail.com> - 6.3.0^20241114git1b36b7a-1
- Update to git snapshot

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 6.2.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-3
- Fix compile issue

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 19 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-1
- Update to 6.0.0 release
