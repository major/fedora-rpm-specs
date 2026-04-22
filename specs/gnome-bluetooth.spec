%global libadwaita_version 1.6~beta
%global gtk4_version 4.15.2

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:		gnome-bluetooth
Epoch:		1
Version:	47.2
Release:	%autorelease
Summary:	Bluetooth graphical utilities

License:	GPL-2.0-or-later
URL:		https://wiki.gnome.org/Projects/GnomeBluetooth
Source0:	https://download.gnome.org/sources/gnome-bluetooth/47/gnome-bluetooth-%{tarball_version}.tar.xz

%if 0%{?rhel}
ExcludeArch:	s390 s390x
%endif

BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	meson
BuildRequires:	pkgconfig(gsound)
BuildRequires:	pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:	pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	python3-dbusmock >= 0.25.0-1

Provides:	dbus-bluez-pin-helper

# Otherwise we might end up with mismatching version
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	bluez >= 5.0
Requires:	gtk4 >= %{gtk4_version}
Requires:	libadwaita >= %{libadwaita_version}
%ifnarch s390 s390x
Requires:	pulseaudio-module-bluetooth
Requires:	bluez-obexd
%endif

%description
The gnome-bluetooth package contains graphical utilities to setup,
monitor and use Bluetooth devices.

%package libs
Summary:	GTK+ Bluetooth device selection widgets
License:	LGPL-2.1-or-later

%description libs
This package contains libraries needed for applications that
want to display a Bluetooth device selection widget.

%package libs-devel
Summary:	Development files for %{name}-libs
License:	LGPL-2.1-or-later
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description libs-devel
This package contains the libraries and header files that are needed
for writing applications that require a Bluetooth device selection widget.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

%find_lang gnome-bluetooth-3.0

%files
%license COPYING
%doc README.md NEWS
%{_bindir}/bluetooth-sendto
%{_datadir}/applications/*.desktop
%{_datadir}/gnome-bluetooth-3.0/
%{_mandir}/man1/*

%files -f gnome-bluetooth-3.0.lang libs
%license COPYING.LIB
%{_libdir}/libgnome-bluetooth-3.0.so.*
%{_libdir}/libgnome-bluetooth-ui-3.0.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GnomeBluetooth-3.0.typelib

%files libs-devel
%{_includedir}/gnome-bluetooth-3.0/
%{_libdir}/libgnome-bluetooth-3.0.so
%{_libdir}/libgnome-bluetooth-ui-3.0.so
%{_libdir}/pkgconfig/gnome-bluetooth-3.0.pc
%{_libdir}/pkgconfig/gnome-bluetooth-ui-3.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GnomeBluetooth-3.0.gir
%{_datadir}/gtk-doc

%changelog
%autochangelog
