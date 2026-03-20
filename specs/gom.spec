Name:           gom
Version:        0.5.6
Release:        %autorelease
Summary:        GObject to SQLite object mapper library

# documentation is GFDL-1.1-or-later
License:        LGPL-2.1-or-later AND GFDL-1.1-or-later
URL:            https://wiki.gnome.org/Projects/Gom
Source0:        https://download.gnome.org/sources/gom/0.5/gom-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
BuildRequires:  /usr/bin/gi-docgen

%description
Gom provides an object mapper from GObjects to SQLite. It helps you write
applications that need to store structured data as well as make complex queries
upon that data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson -Denable-gtk-doc=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS README
%{_libdir}/girepository-1.0/Gom-1.0.typelib
%{_libdir}/libgom-1.0.so.0*
%dir %{python3_sitelib}/gi
%dir %{python3_sitelib}/gi/overrides
%{python3_sitelib}/gi/overrides/Gom.py
%dir %{python3_sitelib}/gi/overrides/__pycache__
%{python3_sitelib}/gi/overrides/__pycache__/Gom.cpython-*.pyc

%files devel
%{_includedir}/gom-1.0/
%{_libdir}/libgom-1.0.so
%{_libdir}/pkgconfig/gom-1.0.pc
%{_datadir}/gir-1.0/Gom-1.0.gir
%doc %{_docdir}/gom-1.0/

%changelog
%autochangelog
