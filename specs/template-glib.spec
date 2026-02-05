Name:           template-glib
Version:        3.39.0
Release:        %autorelease
Summary:        A templating library for GLib

License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/template-glib/
Source0:        https://download.gnome.org/sources/%{name}/3.39/%{name}-%{version}.tar.xz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)


%description
Template-GLib is a templating library for GLib. It includes a simple template
format along with integration into GObject-Introspection for properties and
methods. It separates the parsing of templates and the expansion of templates
for faster expansion. You can also define scope, custom functions, and more
with the embedded expression language.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%meson -Ddocs=true
%meson_build


%install
%meson_install
%find_lang template-glib


%files -f template-glib.lang
%license COPYING
%doc NEWS README.md
%{_libdir}/libtemplate_glib-1.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Template-1.0.typelib

%files devel
%doc CONTRIBUTING.md examples
%dir %{_datadir}/doc/template-glib-1.0
%{_datadir}/doc/template-glib-1.0/*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Template-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/template-glib-1.0.*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/template-glib-1.0.pc


%changelog
%autochangelog
