%global forgeurl https://github.com/linuxmint/xdg-desktop-portal-xapp
%global tagver   1.1.5
%global tag      %{tagver}-unstable

Name:           xdg-desktop-portal-xapp
Version:        %{tagver}^unstable
Release:        %{autorelease}
%{forgemeta}
Summary:        Backend implementation for xdg-desktop-portal using Xapp

License:        LGPL-2.1-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildSystem:    meson
BuildOption(conf): -Dsystemduserunitdir=%{_userunitdir}
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(xdg-desktop-portal) >= 1.7.1
BuildRequires:  systemd-rpm-macros

Requires:       dbus-x11
Requires:       dbus-common
Requires:       xapps >= 2.5.0
Requires:       xdg-desktop-portal >= 1.7.1
Requires:       xdg-desktop-portal-gtk
Supplements:    cinnamon

%description
Xapp's Cinnamon, MATE and XFCE backends for xdg-desktop-portal.
This allows sandboxed applications to request services and information from
outside the sandbox in the MATE, XFCE and Cinnamon environments.

%prep
%forgeautosetup -p1

%install -a
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license COPYING
%doc README.md
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.xapp.service
%{_datadir}/xdg-desktop-portal/portals/xapp.portal
%{_datadir}/xdg-desktop-portal/portals/xapp-gnome-keyring.portal
%{_userunitdir}/xdg-desktop-portal-xapp.service

%changelog
%autochangelog