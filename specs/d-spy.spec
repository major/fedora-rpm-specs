Name:           d-spy
Version:        47.0
Release:        2%{?dist}
Summary:        D-Bus explorer

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/d-spy
Source0:        https://download.gnome.org/sources/d-spy/47/d-spy-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
D-Spy is a tool to explore and test end-points and interfaces on the System or
Session D-Bus. You can also connect to D-Bus peers by address. D-Spy was
originally part of GNOME Builder.


%package        libs
Summary:        Libraries for %{name}
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later

%description    libs
The %{name}-libs package contains %{name} shared libraries.


%package        devel
Summary:        Development files for %{name}
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang d-spy


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.dspy.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.dspy.desktop


%files -f d-spy.lang
%license COPYING
%doc NEWS
%{_bindir}/d-spy
%{_datadir}/applications/org.gnome.dspy.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.dspy.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.dspy*.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.dspy-symbolic.svg
%{_datadir}/metainfo/org.gnome.dspy.appdata.xml

%files libs
%license COPYING.lgpl3
%{_libdir}/libdspy-1.so.1*

%files devel
%{_includedir}/dspy-1/
%{_libdir}/libdspy-1.so
%{_libdir}/pkgconfig/dspy-1.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 03 2024 Nieves Montero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 1.8.0-1
- Update to 1.8.0
- Package translations

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Thu Aug 25 2022 Kalev Lember <klember@redhat.com> - 1.2.1-2
- Correct -devel subpackage license to match -libs (rhbz#2120418)

* Mon Aug 22 2022 Kalev Lember <klember@redhat.com> - 1.2.1-1
- Initial Fedora packaging (rhbz#2120418)
