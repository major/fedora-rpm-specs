%global apiver 2

Name:           libpeas
Version:        2.0.7
Release:        %autorelease
Summary:        Plug-ins implementation convenience library

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Libpeas
Source0:        https://download.gnome.org/sources/%{name}/2.0/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(mozjs-128)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python3-embed)
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/vapigen
BuildRequires:  /usr/bin/xmllint

%description
libpeas is a convenience library making adding plug-ins support
to glib-based applications.

%package loader-gjs
Summary:        GJS loader for libpeas
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description loader-gjs
This package contains the GJS loader that is needed to
run JavaScript plugins that use libpeas.

%package loader-python
Summary:        Python loader for libpeas
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-gobject

%description loader-python
This package contains the Python loader that is needed to
run Python plugins that use libpeas.

%package devel
Summary:        Development files for libpeas
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development libraries and header files
that are needed to write applications that use libpeas.

%prep
%autosetup -p1

%build
%meson \
  -Dgtk_doc=true \
  -Dlua51=false \
  -Dvapi=true

%meson_build

%check
%ifnarch aarch64
%meson_test
%endif

%install
%meson_install

%find_lang libpeas-%{apiver}

%files -f libpeas-%{apiver}.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_libdir}/libpeas-%{apiver}.so.0*
%dir %{_libdir}/libpeas-%{apiver}/
%dir %{_libdir}/libpeas-%{apiver}/loaders
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Peas-%{apiver}.typelib

%files loader-gjs
%{_libdir}/libpeas-%{apiver}/loaders/libgjsloader.so

%files loader-python
%{_libdir}/libpeas-%{apiver}/loaders/libpythonloader.so

%files devel
%{_includedir}/libpeas-%{apiver}/
%{_docdir}/libpeas-%{apiver}
%{_libdir}/libpeas-%{apiver}.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Peas-%{apiver}.gir
%{_datadir}/vala/
%{_libdir}/pkgconfig/libpeas-%{apiver}.pc

%changelog
%autochangelog
