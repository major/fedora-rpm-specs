%global commit      65185023db95ec464970aeaeab766fe3ba26ae7d
%global shortcommit %{lua:print(macros.commit:sub(1,7))}

Name:           libspelling
Version:        0.1.0~^1.%{shortcommit}
Release:        %autorelease
Summary:        Spellcheck library for GTK 4
# main source is LGPL-2.1-or-later
# lib/egg-action-group.h is GPL-3.0-or-later
License:        LGPL-2.1-or-later AND GPL-3.0-or-later
URL:            https://gitlab.gnome.org/chergert/libspelling
Source:         %{url}/-/archive/%{commit}/libspelling-%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
# for vapigen
BuildRequires:  vala
BuildRequires:  gi-docgen


%description
A spellcheck library for GTK 4.  This library is heavily based upon GNOME Text
Editor and GNOME Builder's spellcheck implementation.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%autosetup -n libspelling-%{commit}


%build
%meson -Ddocs=false
%meson_build


%install
%meson_install


%files
%license COPYING
%{_libdir}/libspelling-1.so.1*
%{_libdir}/girepository-1.0/Spelling-1.typelib


%files devel
%{_includedir}/libspelling-1
%{_libdir}/libspelling-1.so
%{_libdir}/pkgconfig/libspelling-1.pc
%{_datadir}/gir-1.0/Spelling-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libspelling-1.deps
%{_datadir}/vala/vapi/libspelling-1.vapi


%changelog
%autochangelog
