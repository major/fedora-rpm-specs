Name:           libgexiv2
Version:        0.15.1
Release:        %autorelease
Summary:        Gexiv2 is a GObject-based wrapper around the Exiv2 library

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/gexiv2
Source0:        https://download.gnome.org/sources/gexiv2/0.15/gexiv2-%{version}.tar.xz

BuildRequires:  pkgconfig(exiv2)
BuildRequires:  gcc-c++
BuildRequires:  gi-docgen
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base

%description
libgexiv2 is a GObject-based wrapper around the Exiv2 library. 
It makes the basic features of Exiv2 available to GNOME applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     python3-gexiv2
Summary:        Python3 bindings for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       python3-gobject-base-noarch

%description -n python3-gexiv2
This package contains the python3 bindings for %{name}

%prep
%autosetup -p1 -n gexiv2-%{version}

%build
%meson \
  -Dgtk_doc=true \
  -Dtests=true \
  %{nil}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_libdir}/libgexiv2.so.4*
%{_libdir}/girepository-1.0/GExiv2-0.16.typelib
%{_datadir}/doc/gexiv2-0.16/reference/

%files devel
%{_libdir}/libgexiv2.so
%dir %{_includedir}/gexiv2-0.16/gexiv2
%{_includedir}/gexiv2-0.16/gexiv2/*.h
%{_libdir}/pkgconfig/gexiv2-0.16.pc
%{_datadir}/gir-1.0/GExiv2-0.16.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gexiv2-0.16.deps
%{_datadir}/vala/vapi/gexiv2-0.16.vapi

%files -n python3-gexiv2
%pycached %{python3_sitelib}/gi/overrides/GExiv2.py

%changelog
%autochangelog