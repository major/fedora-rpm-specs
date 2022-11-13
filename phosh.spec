%global gvc_commit ae1a34aafce7026b8c0f65a43c9192d756fe1057
%global libcall_ui_commit 7e2f9e2db6515fb9c4650010c2a9ecb9796957e3
%global libgmobile_commit 3035e22ff124ca7b80ac5a21fe114be442e4dde6

Name:		phosh
Version:	0.22.0
Release:	2%{?dist}
Summary:	Graphical shell for mobile devices
License:	GPLv3+
URL:		https://gitlab.gnome.org/World/Phosh/phosh
Source0:	https://gitlab.gnome.org/World/Phosh/phosh/-/archive/v%{version}/%{name}-v%{version}.tar.gz

# This library doesn't compile into a DSO or ever has had any releases.
# Other projects, such as gnome-shell use it this way.
Source1:	https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/archive/%{gvc_commit}/libgnome-volume-control-%{gvc_commit}.tar.gz

# Similar sutiation as gvc
Source2:	https://gitlab.gnome.org/World/Phosh/libcall-ui/-/archive/%{libcall_ui_commit}/libcall-ui-%{libcall_ui_commit}.tar.gz

Source3:	https://gitlab.gnome.org/guidog/gmobile/-/archive/%{libgmobile_commit}/gmobile-%{libgmobile_commit}.tar.gz

Source4:	phosh

# Needed when not using the OSK package
Source5:	sm.puri.OSK0.desktop

# Tests failing
ExcludeArch:	i686

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	pam-devel
BuildRequires:	callaudiod-devel
BuildRequires:	feedbackd-devel
BuildRequires:	dbus-daemon
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(evince-document-3.0)
BuildRequires:	pkgconfig(gcr-3) >= 3.7.5
BuildRequires:	pkgconfig(gio-2.0) >= 2.58
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.58
BuildRequires:	pkgconfig(glib-2.0) >= 2.72.0
BuildRequires:	pkgconfig(gnome-desktop-3.0) >= 3.26
BuildRequires:	pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:	pkgconfig(gtk+-wayland-3.0) >= 3.22
BuildRequires:	pkgconfig(libhandy-1) >= 1.1.90
BuildRequires:	pkgconfig(libnm) >= 1.14
BuildRequires:	pkgconfig(libpulse) >= 2.0
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(libsystemd) >= 241
BuildRequires:	pkgconfig(polkit-agent-1) >= 0.105
BuildRequires:	pkgconfig(upower-glib) >= 0.99.1
BuildRequires:	pkgconfig(wayland-client) >= 1.14
BuildRequires:	pkgconfig(wayland-protocols) >= 1.12
BuildRequires:	pkgconfig(libfeedback-0.0)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libecal-2.0)
BuildRequires:	at-spi2-core
BuildRequires:	/usr/bin/xvfb-run
BuildRequires:	/usr/bin/xauth
BuildRequires:	desktop-file-utils
BuildRequires:	git-core
BuildRequires:	systemd-rpm-macros

Requires:	phoc >= 0.21.0
Requires:	iio-sensor-proxy
Requires:	gnome-session
Requires:	gnome-shell
Requires:	lato-fonts
Requires:	hicolor-icon-theme

Recommends:	squeekboard

%description
Phosh is a simple shell for Wayland compositors speaking the layer-surface
protocol. It currently supports

* a lockscreen
* brightness control and nighlight
* the gcr system-prompter interface
* acting as a polkit auth agent
* enough of org.gnome.Mutter.DisplayConfig to make gnome-settings-daemon happy
* a homebutton that toggles a simple favorites menu
* status icons for battery, wwan and wifi


%prep
%setup -a1 -a2 -a3 -q -n %{name}-v%{version}

rmdir subprojects/gvc
mv libgnome-volume-control-%{gvc_commit} subprojects/gvc

rmdir subprojects/libcall-ui
mv libcall-ui-%{libcall_ui_commit} subprojects/libcall-ui

rmdir subprojects/gmobile
mv gmobile-%{libgmobile_commit} subprojects/gmobile


%build
%meson -Dphoc_tests=disabled -Dsystemd=true
%meson_build

%install
install -d %{buildroot}%{_sysconfdir}/pam.d/
cp %{SOURCE4} %{buildroot}%{_sysconfdir}/pam.d/

install -d %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE5}

%meson_install
%find_lang %{name}

%{__install} -Dpm 0644 data/phosh.service %{buildroot}%{_unitdir}/phosh.service

%check
desktop-file-validate \
%{buildroot}%{_datadir}/applications/sm.puri.Phosh.desktop
LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test
SH

%files -f %{name}.lang
%{_bindir}/phosh
%{_libexecdir}/phosh
%{_libexecdir}/phosh-calendar-server
%{_datadir}/applications/sm.puri.Phosh.desktop
%{_datadir}/glib-2.0/schemas/sm.puri.phosh.gschema.xml
%{_datadir}/glib-2.0/schemas/sm.puri.phosh.enums.xml
%{_datadir}/glib-2.0/schemas/00_sm.puri.Phosh.gschema.override
%{_datadir}/glib-2.0/schemas/sm.puri.phosh.plugins.ticket-box.gschema.xml
%{_datadir}/gnome-session/sessions/phosh.session
%{_datadir}/wayland-sessions/phosh.desktop
%{_datadir}/phosh
%{_sysconfdir}/pam.d/phosh
%{_unitdir}/phosh.service
%{_userunitdir}/gnome-session@phosh.target.d/session.conf
%{_userunitdir}/sm.puri.Phosh.service
%{_userunitdir}/sm.puri.Phosh.target
%{_datadir}/applications/sm.puri.OSK0.desktop
%{_datadir}/xdg-desktop-portal/portals/phosh.portal
%{_libdir}/phosh/plugins/libphosh-plugin-calendar.so
%{_libdir}/phosh/plugins/calendar.plugin
%{_libdir}/phosh/plugins/libphosh-plugin-upcoming-events.so
%{_libdir}/phosh/plugins/upcoming-events.plugin
%{_libdir}/phosh/plugins/libphosh-plugin-ticket-box.so
%{_libdir}/phosh/plugins/ticket-box.plugin
%{_datadir}/icons/hicolor/symbolic/apps/sm.puri.Phosh-symbolic.svg
%{_datadir}/dbus-1/services/sm.puri.Phosh.CalendarServer.service

%doc README.md
%license COPYING

%changelog
* Fri Nov 11 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.22.0-2
- Requires gnome-shell

* Mon Nov 07 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.22.0-1
- Update to 0.22.0

* Wed Sep 28 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.21.1-1
- Update to 0.21.1

* Thu Sep 01 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.21.0-1
- Update to 0.21.0

* Mon Aug 08 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.20.0-1
- Update to 0.20.0

* Sat Jul 30 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.20.0~beta3-1
- Update to 0.20.0 beta 3

* Fri Jul 29 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.20.0~beta2-3
- Add 0000-polkit-version-fix.diff to fix polkit versioning lookup

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0~beta2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.20.0_beta2-1
- Update to 0.20.0_beta2
- Update libcallui

* Sun Jun 26 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.20.0_beta1-1
- Update to 0.20.0_beta1

* Fri Mar 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.17.0-1
- Update to 0.17.0

* Fri Feb 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.16.0-1
- Update to 0.16.0
- Update libcall-ui to acfbb136bbf74514e0b9801ce6c1e8acf36350b6
- Remove phosh-osk-stub (upstream change)

* Tue Jan 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.15.0-1
- Update to 0.15.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.14.1-1
- Update to 0.14.1

* Thu Oct 28 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0

* Tue Aug 31 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1

* Wed Aug 25 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.0-3
- Requires phosh-osk-stub

* Wed Aug 25 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.0-2
- Move phosh-osk-stub to subpackage

* Tue Aug 10 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0
- Add libcall-ui like gvc

* Fri Jul 23 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.10.2-1
- Update to 0.10.2

* Mon Apr 12 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.10.1-2
- Complete the wlroots 0.12.0 patch

* Mon Apr 12 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.10.1-1
- Update to 0.10.1

* Wed Mar 31 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Wed Mar 03 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0
- Revert GVC to downstream subproject version

* Wed Feb 17 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.8.1-2
- Patch for glib2 > 2.67.1

* Fri Feb 12 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.8.1-1
- Update to phosh 0.8.1
- Update gvc to latest.

* Wed Feb 03 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.8.0-3
- Update phosh pam file to fix gnome keyring

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.8.0-1
- Update to phosh 0.8.0

* Fri Dec 18 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.7.1-1
- Update to phosh 0.7.1

* Thu Dec 10 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.7.0-1
- Update to phosh 0.7.0

* Fri Nov 20 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.0-2
- Patch for wlroots 0.12

* Sun Nov 15 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.6.0-1
- Update to phosh 0.6.0

* Wed Nov 04 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.1-1
- Update to phosh 0.5.1

* Tue Nov 03 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.0-2
- Requires git-core instead of git

* Wed Oct 28 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.5.0-1
- Update to phosh 0.5.0

* Sun Oct 11 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.5-1
- Update to phosh 0.4.5

* Mon Sep 21 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.4-1
- Update to phosh 0.4.4

* Tue Aug 18 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.3-3
- Require hicolor icon theme

* Fri Aug 07 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.3-2
- Patch for 32 bit builds

* Mon Aug 03 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.3-1
- Update to phosh 0.4.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.2-1
- Update to phosh 0.4.2

* Tue Jul 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.1-1
- Update to phosh 0.4.1

* Wed Jul 01 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.4.0-1
- Update to phosh 0.4.0
- Now depends on phoc

* Mon Jun 29 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.1-3
- Revert libgnome-volume-control to align with phosh source dependency version
- Move phosh.service to systemd unitdir

* Fri Jun 26 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.1-2
- Update libgnome-volume-control to latest commit

* Tue Jun 23 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.1-1
- Update to phosh 0.3.1
- Adding dbus-daemon

* Tue May 19 2020 Nikhil Jha <hi@nikhiljha.com> - 0.3.0-1
- Update to phosh 0.3.0

* Thu Mar 05 2020 Nikhil Jha <hi@nikhiljha.com> - 0.2.1-1
- Update to phosh 0.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 0.1.0-3
- Rebuilt for libgnome-desktop soname bump

* Wed Oct 02 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-2
- Fixes from review (thanks Robert-André Mauchin):
- Corrected the License tag
- Validate the Desktop Entry file

* Tue Oct 01 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-1
- Initial packaging

