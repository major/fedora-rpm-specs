%global upstream_version 6.7.1-unstable

Summary: A menu system for the Cinnamon project
Name:    cinnamon-menus
Version: 6.7.1^unstable
Release: %autorelease
License: LGPL-2.0-or-later
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz

ExcludeArch:   %{ix86}

BuildSystem:   meson
BuildOption(conf): -Ddeprecated_warnings=false
BuildOption(conf): -Denable_debug=false
BuildRequires: gcc
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: python3

%description
cinnamon-menus is an implementation of the draft "Desktop
Menu Specification" from freedesktop.org. This package
also contains the Cinnamon menu layout configuration files,
.directory files and assorted menu related utility programs,
Python bindings, and a simple menu editor.

%package devel
Summary: Libraries and include files for the Cinnamon menu system
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the necessary development libraries for
writing applications that use the Cinnamon menu system.

%prep
%autosetup -p1 -n %{name}-%{upstream_version}

%files
%doc AUTHORS NEWS
%license COPYING COPYING.LIB
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/CMenu-3.0.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/cinnamon-menus-3.0
%{_datadir}/gir-1.0/CMenu-3.0.gir

%changelog
%autochangelog