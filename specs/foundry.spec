%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           foundry
Version:        1.1~alpha
Release:        %autorelease
Summary:        IDE library and command-line companion tool

# foundry: LGPL-2.1-or-later
# bundled eggbitset / timsort: Apache-2.0
License:        LGPL-2.1-or-later AND Apache-2.0

URL:            https://gitlab.gnome.org/GNOME/foundry
Source:         https://download.gnome.org/sources/foundry/1.1/foundry-%{tarball_version}.tar.xz

ExcludeArch:    %{ix86}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  libappstream-glib

Buildrequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(jsonrpc-glib-1.0)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libdex-1) >= 1.1
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(template-glib-1.0)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(readline)

Requires:       libfoundry%{?_isa} = %{version}-%{release}

%global _description %{expand:
This tool aims to extract much of what makes GNOME Builder an IDE into a
library and companion command-line tool.}

%description %{_description}

%package      -n libfoundry
Summary:        IDE library and command-line companion tool (shared library)

%description  -n libfoundry %{_description}
This package contains the shared library.

%package     -n libfoundry-gtk
Summary:        IDE library and command-line companion tool (GTK integration)
Requires:       libfoundry%{?_isa} = %{version}-%{release}

%description -n libfoundry-gtk %{_description}
This package contains the shared library for GTK integration.

%package     -n libfoundry-devel
Summary:        IDE library and command-line companion tool (development files)
Requires:       libfoundry%{?_isa} = %{version}-%{release}

%description -n libfoundry-devel %{_description}
This package contains the development headers for libfoundry.

%package     -n libfoundry-gtk-devel
Summary:        IDE library and command-line companion tool (development files)
Requires:       libfoundry-gtk%{?_isa} = %{version}-%{release}

%description -n libfoundry-gtk-devel %{_description}
This package contains the development headers for libfoundry-gtk.

%prep
%autosetup -n foundry-%{tarball_version} -p1 

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test
appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT/%{_datadir}/metainfo/app.devsuite.Foundry.metainfo.xml

%files
%{_bindir}/foundry
%{_datadir}/metainfo/app.devsuite.Foundry.metainfo.xml
%{bash_completions_dir}/foundry

%files -n libfoundry
%doc README.md
%doc NEWS
%doc %{_mandir}/man1/*
%license COPYING
%{_libdir}/libfoundry-1.so.1{,.0.0}
%{_libdir}/libfoundry-adw-1.so*
%{_libdir}/girepository-1.0/Foundry-1.typelib
%{_libdir}/girepository-1.0/FoundryAdw-1.typelib
%dir %{_datadir}/foundry
%{_datadir}/foundry/language-defaults
%{_datadir}/glib-2.0/schemas/app.devsuite.foundry{,.*}.gschema.xml

%files -n libfoundry-gtk
%{_libdir}/libfoundry-gtk-1.so.1{,.0.0}
%{_libdir}/girepository-1.0/FoundryGtk-1.typelib

%files -n libfoundry-devel
%dir %{_includedir}/libfoundry-1
%{_includedir}/libfoundry-1/*.h
%{_includedir}/libfoundry-adw-1/*.h
%{_libdir}/libfoundry-1.so
%dir %{_libdir}/libfoundry-1
%dir %{_libdir}/libfoundry-1/include
%{_libdir}/libfoundry-1/include/libfoundry-config.h
%{_libdir}/pkgconfig/libfoundry-1.pc
%{_libdir}/pkgconfig/libfoundry-adw-1.pc
%{_datadir}/gir-1.0/Foundry-1.gir
%{_datadir}/gir-1.0/FoundryAdw-1.gir

%files -n libfoundry-gtk-devel
%dir %{_includedir}/libfoundry-gtk-1
%{_includedir}/libfoundry-gtk-1/*.h
%{_libdir}/libfoundry-gtk-1.so
%{_libdir}/pkgconfig/libfoundry-gtk-1.pc
%{_datadir}/gir-1.0/FoundryGtk-1.gir

%changelog
%autochangelog
