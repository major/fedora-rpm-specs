%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %(echo -n %{tarball_version} | sed 's/[.].*//')

%global gettext_version                         0.19.6
%global gnome_desktop_version                   40~rc
%global glib2_version                           2.68.0
%global gtk4_version                            3.24.27
%global mutter_version                          44~beta
%global gsettings_desktop_schemas_version       40~rc
%global ibus_version                            1.5.24
%global gnome_settings_daemon_version           40~rc

Name:           gnome-kiosk
Version:        44.0
Release:        1%{?dist}
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
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_desktop_version}
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(ibus-1.0) >= %{ibus_version}
BuildRequires:  pkgconfig(libmutter-12) >= %{mutter_version}

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
* Tue Mar 21 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Mon Mar 06 2023 David King <amigadave@amigadave.com> - 44~rc-1
- Update to 44.rc

* Wed Feb 15 2023 Adam Williamson <awilliam@redhat.com> - 44~beta-1
- Update to 44-beta, rebuild against new libmutter

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Adam Williamson <awilliam@redhat.com> - 42.0-2
- Bump mutter requirements and rebuild against mutter 43

* Tue Mar 22 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Mon Jan 24 2022 David King <amigadave@amigadave.com> - 42~alpha-1
- Update to 42.alpha

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 David King <amigadave@amigadave.com> - 41.0-2
- Build against mutter 42 (#2040955)

* Thu Sep 23 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Wed Aug 18 2021 Ray Strode <rstrode@redhat.com> - 41~beta-1
- Update to 41.beta

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Ray Strode <rstrode@redhat.com> - 40.0-1
- Update to 40.0
  Related: #1950042

* Wed May 12 2021 Ray Strode <rstrode@redhat.com> - 40~alpha-9
- Fix crash
  Resolves: #1957754

* Thu May 06 2021 Ray Strode <rstrode@redhat.com> - 40~alpha-8
- Fix window ordering bug
  Resolves: #1957863

* Tue Apr 27 2021 Ray Strode <rstrode@redhat.com> - 40~alpha-7
- Fix desktop file
  Resolves: #1954285

* Fri Apr 23 2021 Ray Strode <rstrode@redhat.com> - 40~alpha-6
- Add vprovides so initial-setup can use this

* Wed Apr 21 2021 Ray Strode <rstrode@redhat.com> - 40~alpha-5
- Fix keyboard layouts getting out of sync in anaconda

* Tue Apr 20 2021 Ray Strode <rstrode@redhat.com> - 40~alpha-4
- Fix infinite loop

* Mon Apr 19 2021 Ray Strode <rstrode@redhat.com> - 40~alpha-3
- Fix crash

* Sun Apr 18 2021 Ray Strode <rstrode@redhat.com> - 40~alpha-2
- Work with 3rd party keyboard layout selectors
- Be less aggressive about fullscreening windows

* Mon Apr 12 2021 Ray Strode <rstrode@redhat.com> - 40~alpha-1
- Initial import

