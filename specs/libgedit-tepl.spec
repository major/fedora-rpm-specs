%global apiver 6

Name:           libgedit-tepl
Version:        6.14.0
Release:        %autorelease
Summary:        Text editor product line library
License:        LGPL-3.0-or-later
URL:            https://gedit-text-editor.org/
Source:         https://gitlab.gnome.org/World/gedit/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.74
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libgedit-amtk-5) >= 5.9
BuildRequires:  pkgconfig(libgedit-gfls-1) >= 0.3
BuildRequires:  pkgconfig(libgedit-gtksourceview-300) >= 299.6
BuildRequires:  pkgconfig(libhandy-1) >= 1.6
BuildRequires:  pkgconfig(icu-uc) pkgconfig(icu-i18n)
# test dependencies
BuildRequires:  xwayland-run
BuildRequires:  mutter
BuildRequires:  mesa-libEGL

# renamed upstream except for the gobject-introspection
Obsoletes:      tepl < 6.10.0

%description
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs. Tepl is the acronym for “Text editor product line”.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# renamed upstream except for the gobject-introspection
Obsoletes:      tepl-devel < 6.10.0

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%meson -Dgtk_doc=true
%meson_build


%install
%meson_install

%find_lang %{name}-%{apiver}


%check
%{shrink:xwfb-run -c mutter -- %meson_test}


%files -f %{name}-%{apiver}.lang
%license LICENSES/*
%doc NEWS README.md
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Tepl-%{apiver}.typelib
%{_libdir}/libgedit-tepl-%{apiver}.so.4{,.*}

%files devel
%{_includedir}/libgedit-tepl-%{apiver}/
%{_libdir}/libgedit-tepl-%{apiver}.so
%{_libdir}/pkgconfig/libgedit-tepl-%{apiver}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Tepl-%{apiver}.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libgedit-tepl-%{apiver}/


%changelog
%autochangelog
