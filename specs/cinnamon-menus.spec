%global upstream_version 6.7.0-unstable

Summary: A menu system for the Cinnamon project
Name:    cinnamon-menus
Version: 6.7.0^unstable
Release: 1%{?dist}
License: LGPL-2.0-or-later
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz

ExcludeArch:   %{ix86}

BuildRequires: meson
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

%build
%meson \
 -Ddeprecated_warnings=false \
 -Denable_debug=false

%meson_build

%install
%meson_install

%ldconfig_scriptlets

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
* Mon Apr 13 2026 Leigh Scott <leigh123linux@gmail.com> - 6.7.0^unstable-1
- Update to 6.7.0-unstable

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Nov 27 2025 Leigh Scott <leigh123linux@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Leigh Scott <leigh123linux@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 6.2.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Leigh Scott <leigh123linux@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 19 2023 Leigh Scott <leigh123linux@gmail.com> - 6.0.0-1
- Update to 6.0.0 release
