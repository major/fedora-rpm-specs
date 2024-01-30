%global apiver 6

Name:           tepl
Version:        6.8.0
Release:        %autorelease
Summary:        Text editor product line library
License:        LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/swilmet/tepl
Source0:        https://download.gnome.org/sources/tepl/6.8/tepl-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(amtk-5)
BuildRequires:  pkgconfig(glib-2.0) >= 2.62
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
#BuildRequires:  pkgconfig(libgedit-amtk-5)
BuildRequires:  pkgconfig(libgedit-gtksourceview-300)
BuildRequires:  pkgconfig(icu-uc) pkgconfig(icu-i18n)

%description
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs. Tepl is the acronym for “Text editor product line”.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup

# renamed with no API changes
sed -i -e 's|libgedit-amtk|amtk|g' meson.build docs/reference/meson.build


%build
%meson -Dgtk_doc=true
%meson_build


%install
%meson_install

%find_lang tepl-%{apiver}


%files -f tepl-%{apiver}.lang
%license LICENSES/*
%doc NEWS README.md
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Tepl-%{apiver}.typelib
%{_libdir}/libtepl-%{apiver}.so.4{,.*}

%files devel
%{_includedir}/tepl-%{apiver}/
%{_libdir}/libtepl-%{apiver}.so
%{_libdir}/pkgconfig/tepl-%{apiver}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Tepl-%{apiver}.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/tepl-%{apiver}/


%changelog
%autochangelog
