Name:           jsonrpc-glib
Version:        3.44.2
Release:        %autorelease
Summary:        A JSON-RPC library for GLib

License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/jsonrpc-glib
Source0:        https://download.gnome.org/sources/%{name}/3.44/%{name}-%{version}.tar.xz

BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)

%description
Jsonrpc-GLib is a JSON-RPC library for GLib. It includes support for
communicating as both a JSON-RPC client and server. Additionally,
supports upgrading connections to use GVariant for less runtime overhead.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends:     gi-docgen-fonts

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -D enable_gtk_doc=true
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libjsonrpc-glib-1.0.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Jsonrpc-1.0.typelib

%files devel
%doc CONTRIBUTING.md
%doc %{_pkgdocdir}
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Jsonrpc-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/jsonrpc-glib-1.0.*
%{_includedir}/jsonrpc-glib-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/jsonrpc-glib-1.0.pc


%changelog
%autochangelog
