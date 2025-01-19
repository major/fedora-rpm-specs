%bcond_with gtk4

Name:           gthree
Version:        0.9.0
Release:        13%{?dist}
Summary:        Gthree is a GObject/Gtk+ port of three.js

License:        MIT
URL:            https://github.com/alexlarsson/gthree
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    i686

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson

BuildRequires:  pkgconfig(epoxy) >= 1.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.43.2
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(graphene-1.0) >= 1.10.2
BuildRequires:  pkgconfig(graphene-gobject-1.0) >= 1.10.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0
%if %{with gtk4}
BuildRequires:  pkgconfig(gtk4) >= 3.96
%endif

Recommends:     %{name}-gtk3%{?_isa}
%if %{with gtk4}
Recommends:     %{name}-gtk4%{?_isa}
%endif

Suggests:       %{name}-examples

%description
Gthree is a port of three.js to GObject and Gtk3. The code is a partial copy of
three.js, and the API is very similar, although it only supports OpenGL.

For information about three.js, see: http://threejs.org


# Devel package
%package        devel
Summary:        Devel files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk3%{?_isa} = %{version}-%{release}
%if %{with gtk4}
Requires:       %{name}-gtk4%{?_isa} = %{version}-%{release}
%endif

%description    devel
Devel files for %{name}.


# Examples package
%package        examples
Summary:        Example files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    examples
Example files for %{name}.


# GTK3 package
%package        gtk3
Summary:        GTK 3 supprort for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtk3
GTK 3 supprort for %{name}.


%if %{with gtk4}
# GTK4 package
%package        gtk4
Summary:        GTK 4 supprort for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gtk4
GTK 4 supprort for %{name}.
%endif


%prep
%autosetup


%build
%if %{with gtk4}
%meson \
    -Dgtk4=true \
    -Dgtk_doc=true
%else
%meson \
    -Dgtk_doc=true
%endif

%meson_build


%install
%meson_install


%files
%license COPYING
%doc README NEWS
%{_libdir}/girepository-1.0/Gthree-1.0.typelib
%{_libdir}/libgthree-1.so.0*

%files devel
%{_datadir}/gir-1.0/Gthree-1.0.gir
%{_datadir}/gir-1.0/GthreeGtk3-1.0.gir
%{_datadir}/gtk-doc/html/%{name}-gtk3/
%{_datadir}/gtk-doc/html/%{name}/
%{_includedir}/%{name}-1.0
%{_includedir}/%{name}-gtk3-1.0/%{name}/gthreearea.h
%{_libdir}/libgthree-1.so
%{_libdir}/libgthree-gtk3-1.so
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_libdir}/pkgconfig/%{name}-gtk3-1.0.pc


%files gtk3
%{_libdir}/libgthree-gtk3-1.so.0*
%{_libdir}/girepository-1.0/GthreeGtk3-1.0.typelib

%if %{with gtk4}
%files gtk4
# DUMMY
%endif

%files examples
%{_datadir}/%{name}-examples/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.0-4
- build: With docs. Partial fix for rh#1968254

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.0-1
- Update to 0.9.0
- No longer exclude 'armv7hl' arch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-2
- Add temporary 'ExcludeArch' for armv7hl and i686

* Mon Sep 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Mon Sep 02 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20190825git400d8bb
- Update to latest git snapshot

* Wed Jun 05 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-9.20190808gita38a231
- Initial package
