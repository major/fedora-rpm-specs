%global gtk3_version     3.16.0
%global glib2_version    2.37.3
%global po_package       cinnamon-desktop-3.0

%global upstream_version 6.7.2-unstable

Summary: Shared code among cinnamon-session, nemo, etc
Name:    cinnamon-desktop
Version: 6.7.2^unstable
Release: 2%{?dist}
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz
Source1: x-cinnamon-mimeapps.list

ExcludeArch: %{ix86}

Patch0:   set_font_defaults.patch

Requires: redhat-menus

# Make sure to update libgnome schema when changing this
%if 0%{?fedora}
Requires: system-backgrounds-gnome
%endif

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)  >= %{glib2_version}
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(xrandr)
BuildRequires: meson
BuildRequires: gcc
BuildRequires: python3-packaging

%description
The cinnamon-desktop package contains an internal library
(libcinnamon-desktop) used to implement some portions of the CINNAMON
desktop, and also some data files and other shared components of the
CINNAMON user environment.

%package devel
Summary:  Libraries and headers for libcinnamon-desktop
License:  LGPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for the CINNAMON-internal private library
libcinnamon-desktop.

%prep
%autosetup -p1 -n %{name}-%{upstream_version}

%build
%meson \
 -Dalsa=true \
%ifarch ppc64le s390x
 -Dbubblewrap=disabled \
%endif
 -Ddeprecation_warnings=false
%meson_build

%install
%meson_install

mkdir -p %buildroot%{_datadir}/applications/
install -m 644 %SOURCE1 %buildroot%{_datadir}/applications/x-cinnamon-mimeapps.list

%find_lang %{po_package} --all-name --with-gnome


%ldconfig_scriptlets


%files -f %{po_package}.lang
%doc AUTHORS README
%license COPYING COPYING.LIB
%{_datadir}/glib-2.0/schemas/org.cinnamon.*.xml
%{_datadir}/applications/x-cinnamon-mimeapps.list
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/C*.typelib

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/cinnamon-desktop/
%{_datadir}/gir-1.0/C*.gir

%changelog
* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2^unstable-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Thu Jul 02 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.2^unstable-1
- Update to 6.7.2-unstable

* Sat May 23 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.1^unstable-2
- Enable alsa

* Sat May 23 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.1^unstable-1
- Update to 6.7.1-unstable

* Mon Apr 13 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.0^unstable-1
- Update to 6.7.0-unstable

* Wed Feb 25 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-8
- Update gvc patch

* Sun Feb 08 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-7
- Bump spec

* Sun Feb 08 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-6
- Fix cvc patch

* Fri Feb 06 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-5
- Update cvc patch

* Thu Feb 05 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-4
- Add upstream pull request to fix cvc issues

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jan 08 2026 Leigh Scott <leigh123linux@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Tue Dec 16 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.1-1
- Update to 6.6.1

* Thu Nov 27 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Mon Aug 18 2025 Leigh Scott <leigh123linux@gmail.com> - 6.4.1-4
- Drop require gnome-themes-standard, gtk2 apps can handle their own theme
  requires

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 02 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.1-1
- Update t0 6.4.1

* Tue Nov 26 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Thu Nov 14 2024 Leigh Scott <leigh123linux@gmail.com> - 6.3.0^20241114git4ff8433-1
- Update to git snapshot

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 6.2.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-2
- AAdd buildrequires python3-packaging

* Sun Nov 19 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-1
- Update to 6.0.0 release
