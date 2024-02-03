%global api_version 300
%global glib_version 2.74
%global gtk_version 3.20

Name:           libgedit-gtksourceview
Version:        299.0.5
Release:        %autorelease
Summary:        Gedit Technology - Source code editing widget
License:        LGPL-2.1-or-later
URL:            https://gedit-technology.github.io/
Source:         https://github.com/gedit-technology/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# %%generate_buildrequires in RPM spec
Patch:          rpmspec.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk_version}
BuildRequires:  pkgconfig(libxml-2.0)

%description
libgedit-gtksourceview is a library that extends GtkTextView, the standard GTK
widget for multiline text editing. This library adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features typical
of a source code editor.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang libgedit-gtksourceview-%{api_version}


%files -f libgedit-gtksourceview-%{api_version}.lang
%license COPYING
%doc NEWS README
%{_libdir}/libgedit-gtksourceview-%{api_version}.so.0{,.*}
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/GtkSource-%{api_version}.typelib
%{_datadir}/libgedit-gtksourceview-%{api_version}/

%files devel
%{_includedir}/libgedit-gtksourceview-%{api_version}/
%{_libdir}/libgedit-gtksourceview-%{api_version}.so
%{_libdir}/pkgconfig/libgedit-gtksourceview-%{api_version}.pc
%dir %{_datadir}/gir-1.0/
%{_datadir}/gir-1.0/GtkSource-%{api_version}.gir
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/libgedit-gtksourceview-%{api_version}/


%changelog
%autochangelog
