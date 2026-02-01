Name:           libgexiv2_0.14
Version:        0.14.6
Release:        %autorelease
Summary:        Gexiv2 is a GObject-based wrapper around the Exiv2 library

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/gexiv2
Source0:        https://download.gnome.org/sources/gexiv2/0.14/gexiv2-%{version}.tar.xz

BuildRequires:  pkgconfig(exiv2)
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
BuildRequires:  gi-docgen

%description
libgexiv2 is a GObject-based wrapper around the Exiv2 library. 
It makes the basic features of Exiv2 available to GNOME applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

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
# Test failures on s390x, filled as https://bugzilla.redhat.com/show_bug.cgi?id=2435118
%ifnarch s390x
%meson_test
%endif

%files
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_libdir}/libgexiv2.so.2*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GExiv2-0.10.typelib

%files devel
%{_includedir}/gexiv2/
%{_libdir}/libgexiv2.so
%{_libdir}/pkgconfig/gexiv2.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GExiv2-0.10.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gexiv2/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gexiv2.deps
%{_datadir}/vala/vapi/gexiv2.vapi
# The GExiv2.py is part of the libgexiv2 package
%exclude %pycached %{python3_sitelib}/gi/overrides/GExiv2.py


%changelog
%autochangelog
