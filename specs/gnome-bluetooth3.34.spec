Name:		gnome-bluetooth3.34
Version:	3.34.5
Release:	9%{?dist}
Summary:	Bluetooth graphical utilities

License:	GPL-2.0-or-later
URL:		https://wiki.gnome.org/Projects/GnomeBluetooth
Source0:	https://download.gnome.org/sources/gnome-bluetooth/3.34/gnome-bluetooth-%{version}.tar.xz
# Fix build for newer versions of meson
Patch0:         0001-Fix-build-newer-meson.patch

%if 0%{?rhel}
ExcludeArch:	s390 s390x
%endif

BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk3-devel
BuildRequires:	gtk-doc
BuildRequires:	meson
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	systemd-devel
BuildRequires:	python3-dbusmock >= 0.22.0-3

# Otherwise we might end up with mismatching version
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	bluez >= 5.0
%ifnarch s390 s390x
Requires:	pulseaudio-module-bluetooth
%endif

%description
The gnome-bluetooth3.34 package contains graphical utilities to setup,
monitor and use Bluetooth devices using the old 3.34 gnome-bluetooth API.

%package libs
Summary:	GTK+ Bluetooth device selection widgets
License:	LGPLv2+

%description libs
This package contains libraries needed for applications that
want to display a Bluetooth device selection widget using the old 3.34
gnome-bluetooth API.

%package libs-devel
Summary:	Development files for %{name}-libs
License:	LGPLv2+
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description libs-devel
This package contains the libraries and header files that are needed
for writing applications that require a Bluetooth device selection widget.

%prep
%autosetup -p1 -n gnome-bluetooth-%{version}

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

# These are in the gnome-bluetooth package.
rm $RPM_BUILD_ROOT/%{_bindir}/bluetooth-sendto \
  $RPM_BUILD_ROOT/%{_datadir}/applications/bluetooth-sendto.desktop \
  $RPM_BUILD_ROOT/%{_mandir}/man1/bluetooth-sendto.1*

%find_lang gnome-bluetooth2

#%%check
#%%meson_test

%files
%license COPYING
%doc README.md NEWS
%{_datadir}/gnome-bluetooth/

%files -f gnome-bluetooth2.lang libs
%license COPYING.LIB
%{_libdir}/libgnome-bluetooth.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GnomeBluetooth-1.0.typelib
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/status/*

%files libs-devel
%{_includedir}/gnome-bluetooth/
%{_libdir}/libgnome-bluetooth.so
%{_libdir}/pkgconfig/gnome-bluetooth-1.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GnomeBluetooth-1.0.gir
%{_datadir}/gtk-doc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.34.5-5
- Migrate to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 16 2022 David King <amigadave@amigadave.com> - 3.34.5-1
- Initial import (#2039855)
