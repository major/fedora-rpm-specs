%global glib2_version 2.86.0
%global gtk3_version 3.20
%global mozjs140_version 140.6.0

Name:          cjs
# Epoch needed: version dropped from 1.34.0 to 1.9.1 during package revival
Epoch:         1
Version:       140.1
Release:       %autorelease
Summary:       Javascript Bindings for Cinnamon

License:       MIT AND BSD-3-Clause AND MPL-2.0 AND CC-BY-3.0 AND (MIT OR LGPL-2.0-or-later) AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later)
URL:           https://github.com/linuxmint/%{name}
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:   %{ix86}

BuildSystem:   meson
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(girepository-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(mozjs-140) >= %{mozjs140_version}
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(sysprof-capture-4)
# For GTK+ 3 tests
BuildRequires: gtk3
# For dbus tests
BuildRequires: dbus-daemon
# Required for checks
BuildRequires: dbus-x11
BuildRequires: mesa-dri-drivers
BuildRequires: mutter
BuildRequires: xwayland-run

Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gobject-introspection%{?_isa}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: mozjs140%{?_isa} >= %{mozjs140_version}

%description
Cjs allows using Cinnamon libraries from Javascript. It's based on the
Spidermonkey Javascript engine from Mozilla and the GObject introspection
framework.


%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{?epoch}:%{version}-%{release}

%description devel
Files for development with %{name}.


%package tests
Summary: Tests for the cjs package
Requires: %{name}%{?_isa} = %{?epoch}:%{version}-%{release}

%description tests
The cjs-tests package contains tests that can be used to verify
the functionality of the installed cjs package.


%prep
%autosetup -p1

%check
%{shrink:xwfb-run -c mutter -- %meson_test --timeout-multiplier=5}

%files
%doc NEWS README.md
%license COPYING
%{_bindir}/cjs
%{_bindir}/cjs-console
%{_libdir}/*.so.*
%{_libdir}/cjs/


%files devel
%doc examples/*
%{_includedir}/cjs-1.0/
%{_libdir}/pkgconfig/cjs-*1.0.pc
%{_libdir}/*.so
%{_datadir}/cjs-1.0/


%files tests
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/
%{_datadir}/glib-2.0/schemas/org.cinnamon.CjsTest.gschema.xml


%changelog
%autochangelog