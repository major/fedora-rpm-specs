%global glib2_version 2.76.0
%global gtk4_version  4.12.0
%global api_version 1
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:		libmks
Version:	0.1.5
Release:	%autorelease
Summary:	Mouse, Keyboard, and Screen to QEMU
License:	LGPL-2.1-or-later
URL:		https://gitlab.gnome.org/GNOME/libmks
Source0:	https://download.gnome.org/sources/%{name}/0.1/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(gi-docgen)
BuildRequires:	pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:	pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:	pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:	pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	vala
Requires:		glib2%{?_isa} >= %{glib2_version}
Requires:		gtk4%{?_isa} >= %{gtk4_version}
%if 0%{?rhel} >= 9
Recommends:		qemu-kvm-ui-dbus
Recommends:		qemu-kvm-ui-opengl
%else
Recommends:		qemu-ui-dbus
Recommends:		qemu-ui-opengl
%endif

%description
This library provides a "Mouse, Keyboard, and Screen" to QEMU using the
D-Bus device support in QEMU and GTK 4.

%package devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}
Recommends:		%{name}-doc = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed
for writing applications using %{name}.

%package doc
Summary:		Documentation files for %{name}
BuildArch:		noarch

Recommends:		%{name}-devel = %{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends:		gi-docgen-fonts

%description doc
Documentation files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson -Dinstall-tools=true -Ddocs=true -Dintrospection=enabled
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md NEWS
%{_libdir}/%{name}-%{api_version}.so.0*
%{_bindir}/mks
%{_bindir}/mks-connect
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Mks-%{api_version}.typelib

%files devel
%{_libdir}/%{name}-%{api_version}.so
%{_includedir}/%{name}-%{api_version}/
%{_libdir}/pkgconfig/%{name}-%{api_version}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Mks-%{api_version}.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/%{name}-%{api_version}.deps
%{_datadir}/vala/vapi/%{name}-%{api_version}.vapi

%files doc
%{_datadir}/doc/%{name}%{api_version}/

%changelog
%autochangelog
