%global gtk3_version    %(pkg-config --modversion gtk+-3.0 2>/dev/null || echo bad)
%global gtk4_version    %(pkg-config --modversion gtk4 2>/dev/null || echo bad)
%global glib2_version   %(pkg-config --modversion glib-2.0 2>/dev/null || echo bad)
%global nm_version      1:1.16.0
%global libnma_version  1.8.27
%global obsoletes_ver   1:0.9.7

%if 0%{?fedora} || 0%{?rhel} < 9
%bcond_without appindicator
%bcond_without dbusmenu
%else
%bcond_with appindicator
%bcond_with dbusmenu
%endif

Name:    network-manager-applet
Summary: A network control and status applet for NetworkManager
Version: 1.36.0
Release: %autorelease
License: GPL-2.0-or-later
URL:     http://www.gnome.org/projects/NetworkManager/
Source:  https://download.gnome.org/sources/network-manager-applet/1.36/%{name}-%{version}.tar.xz
Patch1:  0001-nm-applet-no-notifications.patch

BuildSystem: meson
BuildOption(conf): -Dselinux=true
%if %{with appindicator}
BuildOption(conf): -Dappindicator=auto
%else
BuildOption(conf): -Dappindicator=no
%endif

BuildRequires: NetworkManager-libnm-devel >= %{nm_version}
BuildRequires: libappstream-glib
BuildRequires: libnma-devel >= %{libnma_version}
BuildRequires: ModemManager-glib-devel >= 1.0
BuildRequires: glib2-devel >= 2.32
BuildRequires: gtk3-devel >= 3.10
BuildRequires: gtk4-devel >= 3.96
BuildRequires: gobject-introspection-devel >= 0.10.3
BuildRequires: gettext-devel
BuildRequires: pkgconfig
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: desktop-file-utils
BuildRequires: iso-codes-devel
BuildRequires: libsecret-devel >= 0.12
BuildRequires: jansson-devel
BuildRequires: gcr-devel
BuildRequires: libselinux-devel
BuildRequires: mobile-broadband-provider-info-devel
%if %{with appindicator}
BuildRequires: libappindicator-gtk3-devel
%endif
%if %{with dbusmenu}
BuildRequires: libdbusmenu-gtk3-devel
%endif

%if ! 0%{?flatpak}
Requires:  NetworkManager >= %{nm_version}
%endif
Requires:  nm-connection-editor%{?_isa} = %{version}-%{release}
Requires:  libnma%{?_isa} >= %{libnma_version}
Obsoletes: NetworkManager-gnome < %{obsoletes_ver}

%description
This package contains a network control and status notification area applet
for use with NetworkManager.

%package -n nm-connection-editor
Summary:  A network connection configuration editor for NetworkManager
Requires: libnma%{?_isa} >= %{libnma_version}

%description -n nm-connection-editor
This package contains a network configuration editor and Bluetooth modem
utility for use with NetworkManager.

%package -n nm-connection-editor-desktop
Summary:  The desktop file for nm-connection-editor
Requires: nm-connection-editor%{?_isa} = %{version}-%{release}

%description -n nm-connection-editor-desktop
This package contains the desktop file and appdata for nm-connection-editor.
Without it, the nm-connection-editor cannot be started from the desktop
environment.

%prep
%autosetup -p1

%install -a
mkdir -p %{buildroot}%{_datadir}/gnome-vpn-properties

%find_lang nm-applet
cat nm-applet.lang >> %{name}.lang

%check
%meson_test
# validate .desktop, autostart and appdatafiles
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/nm-applet.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/nm-connection-editor.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/nm-connection-editor.appdata.xml

%files
%doc NEWS CONTRIBUTING
%license COPYING
%{_bindir}/nm-applet
%config(noreplace) %{_sysconfdir}/xdg/autostart/nm-applet.desktop
%{_datadir}/applications/nm-applet.desktop
%{_datadir}/icons/hicolor/22x22/apps/nm-adhoc.png
%{_datadir}/icons/hicolor/22x22/apps/nm-insecure-warn.png
%{_datadir}/icons/hicolor/22x22/apps/nm-mb-roam.png
%{_datadir}/icons/hicolor/22x22/apps/nm-secure-lock.png
%{_datadir}/icons/hicolor/22x22/apps/nm-signal-*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-stage*-connecting*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-tech-*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-vpn-active-lock.png
%{_datadir}/icons/hicolor/22x22/apps/nm-vpn-connecting*.png
%{_datadir}/icons/hicolor/22x22/apps/nm-wwan-tower.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
%{_datadir}/GConf/gsettings/nm-applet.convert
%{_mandir}/man1/nm-applet*

# Yes, lang files for the applet go in nm-connection-editor RPM since it
# is the RPM that everything else depends on
%files -n nm-connection-editor -f %{name}.lang
%{_bindir}/nm-connection-editor
%dir %{_datadir}/gnome-vpn-properties
%{_datadir}/icons/hicolor/*/apps/nm-device-*.*
%{_datadir}/icons/hicolor/*/apps/nm-no-connection.*
%{_datadir}/icons/hicolor/16x16/apps/nm-vpn-standalone-lock.png
%{_mandir}/man1/nm-connection-editor*

%files -n nm-connection-editor-desktop
%{_datadir}/applications/nm-connection-editor.desktop
%{_metainfodir}/nm-connection-editor.appdata.xml

%changelog
%autochangelog