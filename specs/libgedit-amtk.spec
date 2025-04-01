Name:           libgedit-amtk
Version:        5.9.0
Release:        %autorelease
Summary:        Gedit Technology - Actions, Menus and Toolbars Kit
License:        LGPL-3.0-or-later
URL:            https://gedit-text-editor.org/
Source:         https://download.gnome.org/sources/libgedit-amtk/5.9/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

# renamed upstream except for the gobject-introspection
Obsoletes:      amtk < 5.8.0

%description
Amtk is the acronym for “Actions, Menus and Toolbars Kit”. It is a basic
GtkUIManager replacement based on GAction. It is suitable for both a
traditional UI or a modern UI with a GtkHeaderBar.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# renamed upstream except for the gobject-introspection
Obsoletes:      amtk-devel < 5.8.0

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -Dgtk_doc=true
%meson_build


%install
%meson_install

%find_lang %{name}-5


%check
%meson_test


%files -f %{name}-5.lang
%license LICENSES/LGPL-3.0-or-later.txt
%doc NEWS README.md
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Amtk-5.typelib
%{_libdir}/libgedit-amtk-5.so.0{,.*}

%files devel
%{_includedir}/libgedit-amtk-5/
%{_libdir}/libgedit-amtk-5.so
%{_libdir}/pkgconfig/libgedit-amtk-5.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Amtk-5.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libgedit-amtk-5/


%changelog
%autochangelog
