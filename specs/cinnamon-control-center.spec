%global _artwork_version 1.7.5

%global cinnamon_desktop_version 6.7.0
%global csd_version 6.7.0
%global cinnamon_menus_version 6.7.0
%global redhat_menus_version 1.8

%global upstream_version 6.7.2-unstable

Summary: Utilities to configure the Cinnamon desktop
Name:    cinnamon-control-center
Version: 6.7.2^unstable
Release: 2%{?dist}
License: GPL-2.0-or-later AND MIT
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz
Source1: http://packages.linuxmint.com/pool/main/m/mint-artwork/mint-artwork_%{_artwork_version}.tar.xz

ExcludeArch: %{ix86}

Requires: cinnamon-settings-daemon >= %{csd_version}
Requires: redhat-menus >= %{redhat_menus_version}
Requires: hicolor-icon-theme
Requires: cinnamon-translations
Requires: %{name}-filesystem%{?_isa} = %{version}-%{release}
# For the network panel
Requires: nm-connection-editor
# For the colour panel
Requires: gnome-color-manager

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(cinnamon-desktop) >= %{cinnamon_desktop_version}
BuildRequires: pkgconfig(libcinnamon-menu-3.0) >= %{cinnamon_menus_version}
BuildRequires: pkgconfig(gtk+-3.0) >= 3.16.0
BuildRequires: pkgconfig(glib-2.0) >= 2.44.0
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.44.0
BuildRequires: pkgconfig(libnotify) >= 0.7.3
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires: pkgconfig(upower-glib) >= 0.99.8
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(libnm) >= 1.2.0
BuildRequires: pkgconfig(libnma) >= 1.2.0
BuildRequires: pkgconfig(mm-glib) >= 0.7
BuildRequires: pkgconfig(colord)
BuildRequires: pkgconfig(libwacom)

%description
This package contains configuration utilities for the Cinnamon desktop, which
allow to configure accessibility options, desktop fonts, keyboard and mouse
properties, sound setup, desktop theme and background, user interface
properties, screen resolution, and other settings.


%package filesystem
Summary: Cinnamon Control Center directories
# NOTE: this is an "inverse dep" subpackage. It gets pulled in
# NOTE: by the main package an MUST not depend on the main package

%description filesystem
The Cinnamon control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for developing Muffin plugins. Also includes
utilities for testing Metacity/Muffin themes.

%prep
%autosetup -a1 -p1 -n %{name}-%{upstream_version}

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install                                  \
  --delete-original                                   \
  --dir %{buildroot}/%{_datadir}/applications/        \
  %{buildroot}/%{_datadir}/applications/*.desktop

# install sound files
mkdir -p %{buildroot}/%{_datadir}/cinnamon-control-center/sounds/
install -pm 0644 mint-artwork/%{_datadir}/mint-artwork/sounds/* %{buildroot}/%{_datadir}/cinnamon-control-center/sounds/

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/cinnamon-control-center
%{_datadir}/applications/*.desktop
%{_datadir}/cinnamon-control-center/panels/
%{_datadir}/cinnamon-control-center/sounds/*.og*
%{_datadir}/cinnamon-control-center/ui/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/glib-2.0/schemas/org.cinnamon.control-center.display.gschema.xml
# list all binaries explicitly, so we notice if one goes missing
%{_libdir}/libcinnamon-control-center.so.1*
%dir %{_libdir}/cinnamon-control-center-1/
%{_libdir}/cinnamon-control-center-1/panels/libcolor.so
%{_libdir}/cinnamon-control-center-1/panels/libdisplay.so
%{_libdir}/cinnamon-control-center-1/panels/libnetwork.so
%{_libdir}/cinnamon-control-center-1/panels/libwacom-properties.so


%files filesystem
%dir %{_datadir}/cinnamon-control-center/
%dir %{_datadir}/cinnamon-control-center/sounds/


%files devel
%{_includedir}/cinnamon-control-center-1/
%{_libdir}/libcinnamon-control-center.so
%{_libdir}/pkgconfig/libcinnamon-control-center.pc


%changelog
* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2^unstable-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jun 20 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.2^unstable-1
- Update to 6.7.2-unstable

* Sat May 23 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.1^unstable-1
- Update to 6.7.1-unstable

* Mon Apr 13 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.0^unstable-1
- Update to 6.7.0-unstable

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Nov 27 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.0-1
- Update to 6.6.0
