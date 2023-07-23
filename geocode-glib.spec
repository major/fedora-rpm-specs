%global json_glib_version 0.99.2

Name:           geocode-glib
Version:        3.26.4
Release:        %autorelease
Summary:        Geocoding helper library

License:        LGPLv2+
URL:            http://www.gnome.org/
Source0:        http://download.gnome.org/sources/%{name}/3.26/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires:  pkgconfig(libsoup-3.0)

Requires:       json-glib%{?_isa} >= %{json_glib_version}
Requires:       %{name}-data = %{version}-%{release}

%description
geocode-glib is a convenience library for the geocoding (finding longitude,
and latitude from an address) and reverse geocoding (finding an address from
coordinates). It uses Nominatim service to achieve that. It also caches
(reverse-)geocoding requests for faster results and to avoid unnecessary server
load.

%package        data
Summary:        Icon files for %{name}

%description    data
The %{name}-devel package contains icon files for applications that use %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     geocode-glib2
Summary:        Development files for %{name}
Requires:       json-glib%{?_isa} >= %{json_glib_version}
Requires:       %{name}-data = %{version}-%{release}

%description -n geocode-glib2
geocode-glib is a convenience library for the geocoding (finding longitude,
and latitude from an address) and reverse geocoding (finding an address from
coordinates). It uses Nominatim service to achieve that. It also caches
(reverse-)geocoding requests for faster results and to avoid unnecessary server
load.

This package contains version 2 of the API, which uses libsoup3 internally.

%package -n     geocode-glib2-devel
Summary:        Development files for %{name}
Requires:       geocode-glib2%{?_isa} = %{version}-%{release}

%description -n geocode-glib2-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%meson -Denable-installed-tests=false -Dsoup2=false
%meson_build

%install
%meson_install

%files data
%{_datadir}/icons/hicolor/scalable/places/*.svg

%files -n geocode-glib2
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/libgeocode-glib-2.so.0*
%{_libdir}/girepository-1.0/GeocodeGlib-2.0.typelib

%files -n geocode-glib2-devel
%{_includedir}/geocode-glib-2.0/
%{_libdir}/libgeocode-glib-2.so
%{_libdir}/pkgconfig/geocode-glib-2.0.pc
%{_datadir}/gir-1.0/GeocodeGlib-2.0.gir
%doc %{_datadir}/gtk-doc/

%changelog
%autochangelog
