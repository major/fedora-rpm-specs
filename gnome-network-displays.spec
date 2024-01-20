Name:           gnome-network-displays
Version:        0.91.0
Release:        1%{?dist}
Summary:        Stream the desktop to Wi-Fi Display capable devices

# The icon is licensed CC-BY-SA
License:        GPLv3+ and CC-BY-SA
URL:            https://gitlab.gnome.org/GNOME/gnome-network-displays
Source0:        https://download.gnome.org/sources/%{name}/0.91/%{name}-%{version}.tar.xz

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
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnm) >= 1.15.1
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsoup-3.0)

# Versioned library deps
Requires: gnome-desktop3
Requires: gstreamer1-rtsp-server
Requires: gtk3
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
%{_datadir}/glib-2.0/schemas/org.gnome.NetworkDisplays.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.NetworkDisplays.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.NetworkDisplays-symbolic.svg
%{_metainfodir}/org.gnome.NetworkDisplays.appdata.xml
%{_prefix}/lib/firewalld/zones/P2P-WiFi-Display.xml

%changelog
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
