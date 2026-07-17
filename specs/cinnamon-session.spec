%global cinnamon_desktop_version 6.7.1

%global upstream_version 6.7.3-unstable

Summary: Cinnamon session manager
Name:    cinnamon-session
Version: 6.7.3^unstable
Release: 2%{?dist}
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz

ExcludeArch: %{ix86}

Requires: system-logos
# Needed for cinnamon-settings-daemon
Requires: cinnamon-control-center-filesystem

# pull in dbus-x11, see bug 209924
Requires: dbus-x11

# an artificial requires to make sure we get dconf, for now
Requires: dconf

Requires: cinnamon-desktop >= %{cinnamon_desktop_version}

BuildRequires: pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.37.3
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xapp) >= 1.4.6
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xtrans)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: meson
BuildRequires: gcc
BuildRequires: python3-packaging

%description
Cinnamon-session manages a Cinnamon desktop or GDM login session. It starts up
the other core components and handles logout and saving the session.

%prep
%autosetup -p1 -n %{name}-%{upstream_version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS README
%doc %{_mandir}/man*/*
%license COPYING
%{_bindir}/*
%{_libexecdir}/cinnamon-session-binary
%{_libexecdir}/cinnamon-session-check-accelerated
%{_libexecdir}/cinnamon-session-check-accelerated-helper
%{_datadir}/cinnamon-session/
%{_datadir}/icons/hicolor/*/apps/cinnamon-session-properties.png
%{_datadir}/icons/hicolor/scalable/apps/cinnamon-session-properties.svg
%{_datadir}/glib-2.0/schemas/org.cinnamon.SessionManager.gschema.xml
%{_userunitdir}/*.target

%changelog
* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.3^unstable-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jun 20 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.3^unstable-1
- Update to 6.7.3-unstable

* Tue Jun 16 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.2^unstable-1
- Update to 6.7.2-unstable

* Wed May 27 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.1^unstable-2
- Add patch to run graphical-session target

* Sat May 23 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.1^unstable-1
- Update to 6.7.1-unstable

* Mon Apr 13 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.0^unstable-1
- Update to 6.7.0-unstable

* Wed Feb 11 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.3-1
- Update to 6.6.3

* Wed Feb 11 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Dec 11 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.1-1
- Update to 6.6.1

* Thu Nov 27 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Wed Sep 03 2025 Leigh Scott <leigh123linux@gmail.com> - 6.4.0-4
- Fix systemd inhibitor issue

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 6.2.1-2
- convert license to SPDX

* Fri Jul 19 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.0-3
- Remove polkit-gnome requires

* Thu Jun 13 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.0-2
- Fix restart/shutdown

* Wed Jun 12 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Sat May 04 2024 Leigh Scott <leigh123linux@gmail.com> - 6.0.4-1
- Update to 6.0.4 release

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Leigh Scott <leigh123linux@gmail.com> - 6.0.1-3
- AAdd buildrequires python3-packaging

* Sat Jan 06 2024 Leigh Scott <leigh123linux@gmail.com> - 6.0.1-2
- Make sure wayland sessions get a login shell

* Tue Nov 28 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.1-1
- Update to 6.0.1 release

* Tue Nov 28 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-3
- Unset some environment variables on systemd

* Wed Nov 22 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-2
- Fix glib warning

* Sun Nov 19 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-1
- Update to 6.0.0 release
