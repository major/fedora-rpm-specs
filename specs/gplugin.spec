%bcond_without check

Name:           gplugin
Version:        0.44.2
Release:        %autorelease
Summary:        GObject based library that implements a reusable plugin system

License:        LGPL-2.0-or-later
URL:            https://keep.imfreedom.org/gplugin/gplugin
Source0:        https://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.xz.asc
Source2:        https://keybase.io/grim/pgp_keys.asc

# Downstream-only: do not pass --fatal-warnings to gi-docgen
#
# This is too strict for downstream packaging.
Patch:          gplugin-0.43.1-gi-docgen-no-fatal-warnings.patch

BuildRequires:  gnupg2
BuildRequires:  meson >= 0.61.0
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  /usr/bin/help2man
BuildRequires:  pkgconfig(glib-2.0) >= 2.70.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  gettext
%if %{with check}
BuildRequires:  /usr/bin/gtester
%endif
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
GPlugin is a GObject based library that implements a reusable plugin system
which supports loading plugins in other languages via loaders.
It relies heavily on GObject Introspection to expose its API to the other
languages.

It has a very simple API which makes it very simple to use in your application.

%package        libs
Summary:        Library for %{name}

%description    libs
%{summary}.

%package        gtk4
Summary:        GTK4 applications for %{name}
BuildRequires:  pkgconfig(gtk4) >= 4
Requires:       %{name}-gtk4-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    gtk4
%{summary}.

%package        gtk4-libs
Summary:        GTK4 libraries for %{name}
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    gtk4-libs
%{summary}.

%package        loader-lua
Summary:        Lua loader for %{name}
BuildRequires:  pkgconfig(lua) >= 5.1.0
BuildRequires:  lua-lgi
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       lua-lgi

%description    loader-lua
%{summary}.

%package        loader-python
Summary:        Python loader for %{name}
BuildRequires:  pkgconfig(python3-embed)
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0.0
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       pkgconfig(pygobject-3.0) >= 3.0.0

%description    loader-python
%{summary}.

%package        devel
Summary:        Development libraries and header files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends: gi-docgen-fonts

%description    devel
%{summary}.

%package        gtk4-devel
Summary:        Development libraries and header files for %{name}-gtk4-libs
Requires:       %{name}-gtk4-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends: gi-docgen-fonts

%description    gtk4-devel
%{summary}.

%package        vala
Summary:        Vala bindings for %{name}-libs
BuildRequires:  vala
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    vala
%{summary}.

%package        gtk4-vala
Summary:        Vala bindings for %{name}-gtk4-libs
Requires:       %{name}-vala%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    gtk4-vala
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# We install docs ourselves
sed -i -e '/install_data/,+1 d' meson.build
sed -i -e '/install_data/,+1 d' gplugin/share/valgrind/meson.build

%build
%meson
%meson_build

%install
%meson_install

%if %{with check}
%check
# Everything is tested during build process...
%meson_test
%endif

%files
%{_bindir}/gplugin-query
%{_mandir}/man1/gplugin-query.1*

%files libs
%license COPYING
%doc ChangeLog README.md
%{_libdir}/libgplugin.so.0
%{_libdir}/libgplugin.so.0.*
%dir %{_libdir}/gplugin/
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GPlugin-1.0.typelib

%files gtk4
%{_bindir}/gplugin-gtk4-viewer
%{_mandir}/man1/gplugin-gtk4-viewer.1*

%files gtk4-libs
%{_libdir}/libgplugin-gtk4.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GPluginGtk4-1.0.typelib

%files loader-lua
%{_libdir}/gplugin/gplugin-lua.so

%files loader-python
%{_libdir}/gplugin/gplugin-python3.so

%files devel
%doc gplugin/share/valgrind/gplugin.supp
%doc %{_docdir}/gplugin
%{_libdir}/libgplugin.so
%dir %{_includedir}/gplugin-1.0/
%{_includedir}/gplugin-1.0/gplugin/
%{_includedir}/gplugin-1.0/gplugin.h
%{_includedir}/gplugin-1.0/gplugin-native.h
%{_libdir}/pkgconfig/gplugin.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GPlugin-1.0.gir

%files gtk4-devel
%doc %{_docdir}/gplugin-gtk4
%{_libdir}/libgplugin-gtk4.so
%{_includedir}/gplugin-gtk4-1.0/
%{_libdir}/pkgconfig/gplugin-gtk4.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GPluginGtk4-1.0.gir

%files vala
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gplugin.deps
%{_datadir}/vala/vapi/gplugin.vapi

%files gtk4-vala
%{_datadir}/vala/vapi/gplugin-gtk4.deps
%{_datadir}/vala/vapi/gplugin-gtk4.vapi

%changelog
%autochangelog
