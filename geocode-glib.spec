%global json_glib_version 0.99.2

Name:           geocode-glib
Version:        3.26.4
Release:        %autorelease
Summary:        Geocoding helper library

# icons/maki/* are BSD-3-Clause
License:        LGPL-2.0-or-later AND BSD-3-Clause
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

# Renamed/Obsoleted in F39
Obsoletes:      geocode-glib-data < %{version}-%{release}
Obsoletes:      geocode-glib2 < %{version}-%{release}
Provides:       geocode-glib2 = %{version}-%{release}
Provides:       geocode-glib2%{?_isa} = %{version}-%{release}

%description
geocode-glib is a convenience library for the geocoding (finding longitude,
and latitude from an address) and reverse geocoding (finding an address from
coordinates). It uses Nominatim service to achieve that. It also caches
(reverse-)geocoding requests for faster results and to avoid unnecessary server
load.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Renamed/Obsoleted in F39
Obsoletes:      geocode-glib2-devel < %{version}-%{release}
Provides:       geocode-glib2-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%meson -Denable-installed-tests=false -Dsoup2=false
%meson_build

%install
%meson_install

%files
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/libgeocode-glib-2.so.0*
%{_libdir}/girepository-1.0/GeocodeGlib-2.0.typelib
%{_datadir}/icons/hicolor/scalable/places/*.svg

%files devel
%{_includedir}/geocode-glib-2.0/
%{_libdir}/libgeocode-glib-2.so
%{_libdir}/pkgconfig/geocode-glib-2.0.pc
%{_datadir}/gir-1.0/GeocodeGlib-2.0.gir
%doc %{_datadir}/gtk-doc/

%changelog
%autochangelog
