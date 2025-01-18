%global major_minor_version %%(cut -d "." -f 1,2 <<<%{version})

Name:           gnome-network-displays
Version:        0.94.0
Release:        2%{?dist}
Summary:        Screencasting for GNOME

# The icon is licensed CC-BY-SA
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
URL:            https://gitlab.gnome.org/GNOME/gnome-network-displays
Source0:        https://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.14
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.14
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-rtsp-1.0) >= 1.14
BuildRequires:  pkgconfig(gstreamer-rtsp-server-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.14
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0.0
BuildRequires:  pkgconfig(libnm) >= 1.15.1
BuildRequires:  pkgconfig(libportal-gtk4) >= 0.7
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsoup-3.0)

# Versioned library deps
Requires: gnome-desktop3
Requires: gstreamer1-rtsp-server
Requires: gtk4
Requires: hicolor-icon-theme
Requires: NetworkManager-libnm > 1.16.0
%if !0%{?flatpak}
Requires: NetworkManager-wifi
Requires: pipewire-gstreamer
%endif

%description
GNOME Network Displays allows you to cast your desktop to a remote display.
Supports the Miracast and Chromecast protocols.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang %{name} --all-name --with-gnome

%post
%firewalld_reload

%postun
%firewalld_reload

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/gnome-network-displays
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.NetworkDisplays.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.NetworkDisplays-symbolic.svg
%{_metainfodir}/org.gnome.NetworkDisplays.appdata.xml
%{_prefix}/lib/firewalld/zones/P2P-WiFi-Display.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 13 2024 Packit <hello@packit.dev> - 0.94.0-1
- Update to version 0.94.0
- Resolves: rhbz#2303808

* Fri Aug 09 2024 Christian Glombek <lorbus@fedoraproject.org> - 0.93.0-1
- Update to v0.93.0
- Fix License string

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Christian Glombek <lorbus@fedoraproject.org> - 0.92.2-1
- Update to v0.92.2
- Resolve RHBZ#2279116
- Add downstream packit.dev configuration

* Sun Jan 28 2024 Christian Glombek <lorbus@fedoraproject.org> - 0.92.1-1
- Update to v0.92.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.91.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Christian Glombek <lorbus@fedoraproject.org> - 0.91.0-1
- Sort dependencies alphabetically
- Update to v0.91.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 27 2021 Benjamin Berg <bberg@redhat.com> - 0.90.5-1
- New upstream release 0.90.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Benjamin Berg <bberg@redhat.com> - 0.90.4-1
- New upstream release 0.90.4
- This adds firewalld integration

* Wed Jun 17 2020 Jérôme Parmentier <jerome@prmntr.me> - 0.90.3-2
- Add missing dependency on pipewire-gstreamer

* Wed Apr 29 2020 Benjamin Berg <bberg@redhat.com> - 0.90.3-1
- New upstream release 0.90.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Benjamin Berg <bberg@redhat.com> - 0.90.2-2
- Add patch to prevent timeout with certain sinks
  https://github.com/benzea/gnome-network-displays/issues/20

* Mon Dec 16 2019 Benjamin Berg <bberg@redhat.com> - 0.90.2-1
- New upstream release 0.90.2 with bugfixes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Benjamin Berg <bberg@redhat.com> - 0.90.1-0
- Initial package (#1721157)
