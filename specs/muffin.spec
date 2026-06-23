%global upstream_version 6.7.3-unstable

Name:          muffin
Version:       6.7.3^unstable
Release:       2%{?dist}
Summary:       Window and compositing manager based on Clutter

License:       GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT AND SGI-B-2.0
URL:           https://github.com/linuxmint/%{name}
Source0:       %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz

ExcludeArch:   %{ix86}

BuildRequires: meson
BuildRequires: gcc
BuildRequires: cvt
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gmodule-no-export-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(cinnamon-desktop) >= 6.7.0
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-res)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(xwayland)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gl)
BuildRequires: mesa-libEGL-devel
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pangoft2)
BuildRequires: zenity

Requires: dbus-x11
Requires: zenity
Recommends: xorg-x11-server-Xwayland

%description
Muffin is a window and compositing manager that displays and manages
your desktop via OpenGL. Muffin combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

Muffin is very extensible via plugins, which
are used both to add fancy visual effects and to rework the window
management behaviors to meet the needs of the environment.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: mesa-libEGL-devel


%description devel
Header files and libraries for developing Muffin plugins. Also includes
utilities for testing Metacity/Muffin themes.

%prep
%autosetup -p1 -n %{name}-%{upstream_version}

%build
%meson
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_bindir}/
rm -rf %{buildroot}%{_mandir}/man1/
rm -rf %{buildroot}%{_datadir}/applications/

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md NEWS
%license COPYING
%{_libdir}/libmuffin.so.*
%{_libdir}/muffin/
%{_libexecdir}/muffin-restart-helper
%exclude %{_libdir}/muffin/*.gir
%{_datadir}/glib-2.0/schemas/org.cinnamon.muffin.*.xml
%{_udevrulesdir}/61-muffin.rules

%files devel
%{_includedir}/muffin/
%{_libdir}/libmuffin.so
%{_libdir}/muffin/*.gir
%{_libdir}/pkgconfig/*

%changelog
* Sun Jun 21 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.3^unstable-2
- Fix license, that will teach me for copying from mutter spec

* Sat Jun 20 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.3^unstable-1
- Update to 6.7.3-unstable

* Wed Jun 17 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.2^unstable-1
- Update to 6.7.2-unstable

* Tue Jun 02 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.1^unstable-2
- Add patch to fix desktop stacking issue

* Sat May 23 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.1^unstable-1
- Update to 6.7.1-unstable

* Mon Apr 13 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.0^unstable-1
- Update to 6.7.0-unstable

* Wed Mar 11 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.3-2
- Add patch to fix nvidia refresh rate

* Wed Feb 11 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.3-1
- Update to 6.6.3

* Fri Jan 16 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Fri Jan 09 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.1-1
- Update to 6.6.1

* Thu Dec 11 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 02 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.1-1
- Update t0 6.4.1

* Tue Nov 26 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 6.2.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Leigh Scott <leigh123linux@gmail.com> - 6.0.1-3
- Fix compile issue

* Sun Jan 07 2024 Leigh Scott <leigh123linux@gmail.com> - 6.0.1-2
- Fix f38 build issue

* Thu Dec 28 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.1-1
- Update to 6.0.1 release

* Mon Dec 04 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-2
- Drop eglstreams support

* Sun Nov 19 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-1
- Update to 6.0.0 release
