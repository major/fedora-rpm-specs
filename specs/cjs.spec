%global glib2_version 2.86.0
%global gobject_introspection_version 1.66.0
%global gtk3_version 3.20
%global mozjs140_version 140.6.0

Name:          cjs
Epoch:         1
Version:       140.0
Release:       1%{?dist}
Summary:       Javascript Bindings for Cinnamon

License:       MIT AND BSD-3-Clause AND (MIT OR LGPL-2.0-or-later) AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later)
URL:           https://github.com/linuxmint/%{name}
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:   %{ix86}

BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: meson
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
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
Requires: gobject-introspection%{?_isa} >= %{gobject_introspection_version}
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

%build
%meson
%meson_build

%install
%meson_install

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
* Mon Apr 13 2026 Leigh Scott <leigh123linux@gmail.com> - 1:140.0-1
- Update to 140.0

* Wed Jan 21 2026 Leigh Scott <leigh123linux@gmail.com> - 1:128.1-4
- Add pkgconfig variable to export the appropriate API version of mozjs

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:128.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:128.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Dec 10 2025 Leigh Scott <leigh123linux@gmail.com> - 1:128.1-1
- Update to 128.1

* Fri Sep 12 2025 Leigh Scott <leigh123linux@gmail.com> - 1:128.0-3
- Backport fixes to support GLib 2.86.0 typelibs

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:128.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Mar 28 2025 Leigh Scott <leigh123linux@gmail.com> - 1:128.0-1
- Update to 128.0

* Wed Mar 26 2025 Leigh Scott <leigh123linux@gmail.com> - 1:6.4.0-3
- Switch to mozjs128

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Leigh Scott <leigh123linux@gmail.com> - 1:6.4.0-1
- Update to 6.4.0

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1:6.2.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Leigh Scott <leigh123linux@gmail.com> - 1:6.2.0-1
- Update to 6.2.0

* Tue May 14 2024 Leigh Scott <leigh123linux@gmail.com> - 1:6.0.0-4
- Port to mozjs115

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 16 2023 Leigh Scott <leigh123linux@gmail.com> - 1:6.0.0-1
- Update to 6.0.0 release
