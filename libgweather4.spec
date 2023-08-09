%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           libgweather4
Version:        4.3.2
Release:        1%{?dist}
Summary:        A library for weather information

License:        GPLv2+
URL:            https://wiki.gnome.org/Projects/LibGWeather
Source0:        https://download.gnome.org/sources/libgweather/4.3/libgweather-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  python3-gobject-base
BuildRequires:  vala

%description
libgweather is a library to access weather information from online
services for numerous locations.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel-doc
Summary:        Documentation files for development with %{name}

%description    devel-doc
The %{name}-devel-doc package contains documentation for developing
applications that use %{name}.

%prep
%autosetup -p1 -n libgweather-%{tarball_version}

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc CONTRIBUTING.md NEWS README.md
%license COPYING
%{_libdir}/libgweather-4.so.0*
%{_libdir}/girepository-1.0/GWeather-4.0.typelib
%dir %{_libdir}/libgweather-4
%{_libdir}/libgweather-4/Locations.bin
%dir %{_datadir}/libgweather-4
%{_datadir}/libgweather-4/Locations.xml
%{_datadir}/libgweather-4/locations.dtd
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather4.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather4.gschema.xml

%files devel
%{_includedir}/libgweather-4.0
%{_libdir}/libgweather-4.so
%{_libdir}/pkgconfig/gweather4.pc
%{_datadir}/gir-1.0/GWeather-4.0.gir
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/gweather4.deps
%{_datadir}/vala/vapi/gweather4.vapi

%files devel-doc
%license COPYING
%{_docdir}/libgweather-4.0

%changelog
* Mon Aug 07 2023 Kalev Lember <klember@redhat.com> - 4.3.2-1
- Update to 4.3.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 4.2.0-1
- Update to 4.2.0

* Tue Sep 06 2022 Kalev Lember <klember@redhat.com> - 4.1.1-1
- Update to 4.1.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Kalev Lember <klember@redhat.com> - 4.1.0-1
- Update to 4.1.0
- Switch to libsoup3

* Fri Mar 18 2022 David King <amigadave@amigadave.com> - 4.0.0-1
- Update to 4.0.0

* Fri Mar 04 2022 David King <amigadave@amigadave.com> - 3.99.0-1
- Update to 3.99.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.91.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 David King <amigadave@amigadave.com> - 3.91.0-1
- Update to 3.91.0

* Sun Jan 09 2022 David King <amigadave@amigadave.com> - 3.90.0-1
- Initial import (#2038730)
