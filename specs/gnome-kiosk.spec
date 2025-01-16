%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %(echo -n %{tarball_version} | sed 's/[.].*//')

%global gettext_version                         0.19.6
%global gnome_desktop_version                   44.0
%global glib2_version                           2.68.0
%global gtk4_version                            3.24.27
%global mutter_version                          48~alpha
%global gsettings_desktop_schemas_version       40~rc
%global ibus_version                            1.5.24
%global gnome_settings_daemon_version           40~rc

Name:           gnome-kiosk
Version:        48~alpha
Release:        %{autorelease}
Summary:        Window management and application launching for GNOME

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-kiosk
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

Provides:       firstboot(windowmanager) = %{name}

BuildRequires:  dconf
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext >= %{gettext_version}
BuildRequires:  git
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gnome-desktop-4) >= %{gnome_desktop_version}
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(ibus-1.0) >= %{ibus_version}
BuildRequires:  pkgconfig(libmutter-16) >= %{mutter_version}

Requires:       gnome-settings-daemon%{?_isa} >= %{gnome_settings_daemon_version}
Requires:       gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}

%description
GNOME Kiosk provides a desktop enviroment suitable for fixed purpose, or
single application deployments like wall displays and point-of-sale systems.

%package search-appliance
Summary:        Example search application application that uses GNOME Kiosk
Requires:       %{name} = %{version}-%{release}
Requires:       firefox
Requires:       gnome-session
BuildArch:      noarch

%description search-appliance
This package provides a full screen firefox window pointed to google.

%package script-session
Summary:        Basic session used for running kiosk application from shell script
Requires:       %{name} = %{version}-%{release}
Recommends:     gedit
Requires:       gnome-session
BuildArch:      noarch

%description script-session
This package generates a shell script and the necessary scaffolding to start that shell script within a kiosk session.

%prep
%autosetup -S git -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Kiosk.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Kiosk.SearchApp.desktop

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/gnome-kiosk
%{_datadir}/applications/org.gnome.Kiosk.desktop
%{_datadir}/dconf/profile/gnomekiosk
%{_datadir}/gnome-kiosk/gnomekiosk.dconf.compiled
%{_userunitdir}/org.gnome.Kiosk.target
%{_userunitdir}/org.gnome.Kiosk@wayland.service
%{_userunitdir}/org.gnome.Kiosk@x11.service

%files -n gnome-kiosk-search-appliance
%{_datadir}/applications/org.gnome.Kiosk.SearchApp.desktop
%{_datadir}/gnome-session/sessions/org.gnome.Kiosk.SearchApp.session
%{_datadir}/xsessions/org.gnome.Kiosk.SearchApp.Session.desktop
%{_datadir}/wayland-sessions/org.gnome.Kiosk.SearchApp.Session.desktop

%files -n gnome-kiosk-script-session
%{_bindir}/gnome-kiosk-script
%{_userunitdir}/gnome-session@gnome-kiosk-script.target.d/session.conf
%{_userunitdir}/org.gnome.Kiosk.Script.service
%{_datadir}/applications/org.gnome.Kiosk.Script.desktop
%{_datadir}/gnome-session/sessions/gnome-kiosk-script.session
%{_datadir}/wayland-sessions/gnome-kiosk-script-wayland.desktop
%{_datadir}/xsessions/gnome-kiosk-script-xorg.desktop

%changelog
%autochangelog
