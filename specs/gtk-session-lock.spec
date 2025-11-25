Name: gtk-session-lock
Version: 0.2.0
Release: %autorelease
Summary: Library to use GTK 3 to build screen lockers

License: GPL-3.0-or-later AND MIT
URL: https://github.com/Cu3PO42/gtk-session-lock
Source: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires: pkgconfig(vapigen)
BuildRequires: pkgconfig(wayland-client) >= 1.10.0
BuildRequires: pkgconfig(wayland-protocols) >= 1.10.0
BuildRequires: pkgconfig(wayland-scanner) >= 1.10.0
BuildRequires: pkgconfig(wayland-server) >= 1.16
BuildRequires: gcc
BuildRequires: meson

%description
A library to use GTK 3 to build screen lockers using the secure 
ext-session-lock-v1 protocol.

This library is compatible with C, C++, and any language that 
supports GObject introspection files (Python, Vala, etc.).

This library only works on Wayland, and only on Wayland compositors 
that support the ext-session-lock-v1 protocol. Session lock is supported on:

- wlroots based compositors
- Mir-based compositors

%package devel
Summary: Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files, libraries, and other files used for developing 
with %{name}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc CHANGELOG.md
%license LICENSE_GPL.txt LICENSE_MIT.txt
%{_libdir}/girepository-1.0/GtkSessionLock-0.1.typelib
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_datadir}/gir-1.0/GtkSessionLock-0.1.gir
%{_datadir}/vala/vapi/%{name}-0.*
%{_includedir}/%{name}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}-0.pc

%changelog
* Sun Nov 23 2025 Joshua Strobl <joshua@buddiesofbudgie.org> - 0.2.0-1
- Initial inclusion of gtk-session-lock
