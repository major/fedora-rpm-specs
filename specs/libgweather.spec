%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_minor_version %%(echo %%{tarball_version} | cut -d "." -f 1-2)

Name:           libgweather
Version:        4.6.0
Release:        %autorelease
Summary:        A library for weather information

# libgweather/third-party/kdtree.c is BSD-3-Clause
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://wiki.gnome.org/Projects/LibGWeather
Source:         https://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{tarball_version}.tar.xz

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
BuildRequires:  pkgconfig(gweather-locations)
Requires:       gweather-locations

# Renamed in F40
Obsoletes:      libgweather4 < %{version}-%{release}
Provides:       libgweather4 = %{version}-%{release}
Provides:       libgweather4%{_isa} = %{version}-%{release}

%description
libgweather is a library to access weather information from online
services for numerous locations.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
# Renamed in F40
Obsoletes:      libgweather4-devel < %{version}-%{release}
Provides:       libgweather4-devel = %{version}-%{release}
Provides:       libgweather4-devel%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for development with %{name}
# Renamed in F40
Obsoletes:      libgweather4-devel-doc < %{version}-%{release}
Provides:       libgweather4-devel-doc = %{version}-%{release}
Provides:       libgweather4-devel-doc%{_isa} = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation for developing
applications that use %{name}.

%prep
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

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
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GWeather-4.0.typelib
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather4.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather4.gschema.xml

%files devel
%{_includedir}/libgweather-4.0/
%{_libdir}/libgweather-4.so
%{_libdir}/pkgconfig/gweather4.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GWeather-4.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gweather4.deps
%{_datadir}/vala/vapi/gweather4.vapi

%files doc
%license COPYING
%{_docdir}/libgweather-4.0/

%changelog
%autochangelog
