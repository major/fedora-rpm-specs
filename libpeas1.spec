%bcond glade %[!(0%{?rhel} >= 10)]

%global apiver 1.0
%global tarball_name libpeas

Name:           libpeas1
Version:        1.36.0
Release:        %autorelease
Summary:        Plug-ins implementation convenience library, API version 1

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Libpeas
Source0:        https://download.gnome.org/sources/%{tarball_name}/1.36/%{tarball_name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
%if %{with glade}
BuildRequires:  pkgconfig(gladeui-2.0)
%endif
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel

# Conflict with the old libpeas version to avoid potential file conflicts on
# upgrade, but don't obsolete it so that the correct version (libpeas 2 or
# libpeas1) is pulled in through package dependencies.
Conflicts:      libpeas < 2.0

%description
libpeas1 is a convenience library making adding plug-ins support
to glib-based applications. For the version based on newer GLib, see the
libpeas package.

%package gtk
Summary:        GTK+ 3 plug-ins support for libpeas1
Requires:       %{name}%{?_isa} = %{version}-%{release}

# Handle the upgrade path for the -gtk subpackage that moved from libpeas
# package to libpeas1 compat package when the main libpeas package was updated
# to version 2.0. New libpeas 2.0 no longer provides the GTK API, which makes
# the upgrade path easier as this compat package can fully replace the old
# name.
Obsoletes:      libpeas-gtk < 2.0
Conflicts:      libpeas-gtk < 2.0
Provides:       libpeas-gtk = %{version}-%{release}
Provides:       libpeas-gtk%{?_isa} = %{version}-%{release}

%description gtk
libpeas1-gtk is a convenience library making adding plug-ins support
to GTK+ 3-based applications.

%package loader-python3
Summary:        Python 3 loader for libpeas1
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-gobject

# Handle the upgrade path for the -python3 subpackage that moved from libpeas
# package to libpeas1 compat package when the main libpeas package was updated
# to version 2.0. New libpeas 2.0 still provides a python loader, but it's now
# installed under 'libpeas-loader-python' name, which makes it convenient
# because libpeas1-loader-python3 can fully replace libpeas-loader-python3
# (note the python vs python3).
Obsoletes:      libpeas-loader-python3 < 2.0
Conflicts:      libpeas-loader-python3 < 2.0
Provides:       libpeas-loader-python3 = %{version}-%{release}
Provides:       libpeas-loader-python3%{?_isa} = %{version}-%{release}

%description loader-python3
This package contains the Python 3 loader that is needed to
run Python 3 plugins that use libpeas1.

%package devel
Summary:        Development files for libpeas1
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk%{?_isa} = %{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends:     gi-docgen-fonts

# Transition libpeas-devel 1.36 users to the compat package, and conflict with
# the old libpeas-devel version to avoid potential file conflicts on upgrade if
# dnf's obsoletes processing should be disabled.
Obsoletes:      libpeas-devel < 2.0
Conflicts:      libpeas-devel < 2.0

%description devel
This package contains development libraries and header files
that are needed to write applications that use libpeas1.

%prep
%autosetup -p1 -n %{tarball_name}-%{version}

%build
%meson \
  -Ddemos=false \
  %{!?with_glade:-Dglade_catalog=false} \
  -Dvapi=true \
  -Dgtk_doc=true

%meson_build

%install
%meson_install

%find_lang libpeas-%{apiver}

%files -f libpeas-%{apiver}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/libpeas-%{apiver}.so.0*
%dir %{_libdir}/libpeas-%{apiver}/
%dir %{_libdir}/libpeas-%{apiver}/loaders
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Peas-%{apiver}.typelib
%{_datadir}/icons/hicolor/*/actions/libpeas-plugin.*

%files gtk
%{_libdir}/libpeas-gtk-%{apiver}.so.0*
%{_libdir}/girepository-1.0/PeasGtk-%{apiver}.typelib

%files loader-python3
%{_libdir}/libpeas-%{apiver}/loaders/libpython3loader.so

%files devel
%{_includedir}/libpeas-%{apiver}/
%{_docdir}/libpeas-1.0
%{_docdir}/libpeas-gtk-1.0
%{_libdir}/libpeas-%{apiver}.so
%{_libdir}/libpeas-gtk-%{apiver}.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Peas-%{apiver}.gir
%{_datadir}/gir-1.0/PeasGtk-%{apiver}.gir
%{_libdir}/pkgconfig/libpeas-%{apiver}.pc
%{_libdir}/pkgconfig/libpeas-gtk-%{apiver}.pc
%if %{with glade}
%{_datadir}/glade/catalogs/libpeas-gtk.xml
%endif

%changelog
%autochangelog
