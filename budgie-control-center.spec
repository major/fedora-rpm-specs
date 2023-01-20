%global cheese_version 3.28.0
%global glib2_version 2.64
%global gnome_online_accounts_version 3.44.0
%global gnome_stack 42.0
%global gtk3_version 3.24
%global polkit_version 0.105
%global upower_version 0.99.8
%global vala_version 0.52.5

Name:          budgie-control-center
Version:       1.1.1
Release:       7%{?dist}
Summary:       A fork of GNOME Control Center for the Budgie 10 Series

License:       GPLv2+ and CC-BY-SA
URL:           https://github.com/BuddiesOfBudgie/budgie-control-center
Source0:       %{url}/releases/download/v%{version}/budgie-control-center-%{version}.tar.xz

BuildRequires:  chrpath
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl libxslt
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese) >= %{cheese_version}
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_stack}
BuildRequires:  pkgconfig(gnome-settings-daemon) >= %{gnome_stack}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gnome_stack}
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm) >= 1.24
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.13
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
%ifnarch s390 s390x
BuildRequires:  pkgconfig(gnome-bluetooth-1.0) >= 3.34.0
BuildRequires:  pkgconfig(libwacom)
%endif

Requires: cheese-libs%{?_isa} >= %{cheese_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gnome-desktop3%{?_isa} >= %{gnome_stack}
Requires: gnome-online-accounts%{?_isa} >= %{gnome_online_accounts_version}
Requires: gnome-settings-daemon%{?_isa} >= %{gnome_stack}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gnome_stack}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: upower%{?_isa} >= %{upower_version}
%ifnarch s390 s390x
Requires: gnome-bluetooth%{?_isa}
%endif

# Need common
Requires: %{name}-common = %{version}-%{release}

# For user accounts
Requires: accountsservice
Requires: alsa-lib

# For the thunderbolt panel
Recommends: bolt

# For the color panel
Requires: colord

# For the printers panel
Requires: cups-pk-helper
Requires: dbus

# For the info/details panel
Requires: glx-utils
Recommends: switcheroo-control

# For the user languages
Requires: iso-codes

# For the network panel
Recommends: NetworkManager-wifi
Recommends: nm-connection-editor

# For parental controls support
Requires: malcontent
Requires: malcontent-control

# For Show Details in the color panel
Recommends: gnome-color-manager

# For the sharing panel
Recommends: gnome-remote-desktop

# For the power panel
Recommends: power-profiles-daemon

%description
A fork of GNOME Control Center for the Budgie 10 Series.

%package common
License:        GPLv2+ and CC-BY-SA
Summary: Common assets for %{name}
BuildArch: noarch

%description common
This package contains architecture-agnostic common assets for ${name}

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson \
    -Ddark_mode_distributor_logo=%{_datadir}/pixmaps/system-logo-white.png \
    -Ddocumentation=true \
    -Dmalcontent=true
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/budgie/wm-properties
rm -rf %{buildroot}%{_datadir}/budgie/autostart
rm -rf %{buildroot}%{_datadir}/budgie/cursor-fonts
chrpath --delete %{buildroot}%{_bindir}/%{name}
%find_lang %{name} --all-name --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/budgie-cc-remote-login-helper
%{_libexecdir}/%{name}-print-renderer
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.buddiesofbudgie.Settings-*.svg
%{_datadir}/metainfo/%{name}.appdata.xml

%files common -f %{name}.lang
%dir %{_datadir}/budgie
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/keybindings
%dir %{_datadir}/%{name}/pixmaps
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%dir %{_datadir}/icons
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/icons/hicolor/scalable/categories
%dir %{_datadir}/icons/hicolor/scalable/emblems
%dir %{_datadir}/icons/hicolor/scalable/status
%dir %{_datadir}/icons/hicolor/symbolic
%dir %{_datadir}/icons/hicolor/symbolic/apps
%dir %{_datadir}/pixmaps
%dir %{_datadir}/pixmaps/budgie-faces
%dir %{_datadir}/pixmaps/budgie-faces/legacy
%dir %{_datadir}/sounds/budgie
%dir %{_datadir}/sounds/budgie/default
%dir %{_datadir}/sounds/budgie/default/alerts
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/dbus-1/services/org.buddiesofbudgie.ControlCenter.service
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.ControlCenter.gschema.xml
%{_datadir}/budgie/wm-properties
%{_datadir}/pixmaps/budgie-faces/*.jpg
%{_datadir}/pixmaps/budgie-faces/*.png
%{_datadir}/pixmaps/budgie-faces/legacy/*.jpg
%{_datadir}/pixmaps/budgie-faces/legacy/*.png
%{_datadir}/pixmaps/budgie-logo.png
%{_datadir}/%{name}/keybindings/*.xml
%{_datadir}/%{name}/pixmaps/noise-texture-light.png
%{_datadir}/icons/hicolor/scalable/*/budgie-*.svg
%{_datadir}/icons/hicolor/scalable/apps/org.buddiesofbudgie.Settings.Devel.svg
%{_datadir}/icons/hicolor/scalable/apps/org.buddiesofbudgie.Settings.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.buddiesofbudgie.Settings-symbolic.svg
%{_datadir}/man/man1/%{name}.1*
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.*.policy
%{_datadir}/polkit-1/rules.d/%{name}.rules
%{_datadir}/sounds/budgie/default/alerts/*.ogg

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 13 2022 Joshua Strobl <me@joshuastrobl.com> - 1.1.1-6
- Updated to 1.1.1 release

* Sat Aug 06 2022 Joshua Strobl <me@joshuastrobl.com> - 1.1.0-5
- Updated to 1.1.0 release
- Fixes #2113132

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Joshua Strobl <me@joshuastrobl.com> - 1.0.2-3
- Added missing sources file

* Wed Jul 13 2022 Joshua Strobl <me@joshuastrobl.com> - 1.0.2-2
- Updated sources for koji build
- Build fixes for s390 and s390x architectures

* Tue Jul 12 2022 Joshua Strobl <me@joshuastrobl.com> - 1.0.2-1
- Initial packaging of Budgie Control Center
