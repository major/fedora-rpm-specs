%global glib2_version 2.68.0
%global libgit2_glib_version 1.2.0
%global libpeas1_version 1.36.0-11
%global commit f7501bc827f1d4476336b0db0791335cf8a613c4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20250512
%global git 1

Name:           gitg
Version:        45~%{gitdate}git%{shortcommit}
Release:        %autorelease
Summary:        GTK+ graphical interface for the git revision control system

# most code is under GPL-2.0-or-later, except:
# contrib/ide/ide*: GPL-3.0-or-later
# contrib/xml/xml-reader.{c,h}: LGPL-2.0-or-later
# vapi/gpg-error.vapi: MIT
# vapi/gpgme.vapi: MIT
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND MIT
URL:            https://wiki.gnome.org/Apps/Gitg
%if 0%{?git}
Source0:        https://gitlab.gnome.org/GNOME/gitg/-/archive/%{commit}/gitg-%{commit}.tar.bz2
Patch0:         gitg-norpath.patch
# fixes build with libpeas1-1.36.0-11 (gir-2.0 port)
Patch1:         gitg-gir-2.0.patch
%else
Source0:        https://download.gnome.org/sources/%{name}/44/%{name}-%{version}.tar.xz
%endif

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

BuildRequires:  gettext
BuildRequires:  meson

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= %{libgit2_glib_version}
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  libpeas1-devel >= %{libpeas1_version}
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  python3-devel
BuildRequires:  vala

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# PeasGtk typelib required by the plugins engine
Requires:       libpeas-gtk%{?_isa} >= %{libpeas1_version}

%global __provides_exclude_from ^%{_libdir}/gitg/plugins/.*\\.so$

%description
gitg is the GNOME GUI client to view git repositories.


%package libs
Summary:        Backend Library for gitg
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       libgit2-glib%{?_isa} >= %{libgit2_glib_version}

%description libs
libgitg is a GObject based library that provides an easy access to git methods
through GObject based methods


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.


%prep
%autosetup -p1 -n gitg-%{commit}


%build
%meson \
        -Dpython=true

%meson_build


%install
%meson_install
%py_byte_compile %{python3} %{buildroot}%{python3_sitelib}/gi/overrides/GitgExt.py


%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.gitg.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/org.gnome.gitg.appdata.xml




%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/gitg
%{_datadir}/applications/org.gnome.gitg.desktop
%{_datadir}/gitg/
%{_datadir}/glib-2.0/schemas/org.gnome.gitg.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gitg.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gitg-symbolic.svg
%{_metainfodir}/org.gnome.gitg.appdata.xml
%{_mandir}/man1/gitg.1*

%files libs
%license COPYING
%{_libdir}/libgitg{,-ext}-1.0.so.0{,.0.0}
%dir %{_libdir}/gitg
%dir %{_libdir}/gitg/plugins
%{_libdir}/gitg/plugins/{diff,files}.plugin
%{_libdir}/gitg/plugins/lib{diff,files}.so
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gitg{,Ext}-1.0.typelib
%pycached %{python3_sitelib}/gi/overrides/GitgExt.py

%files devel
%{_includedir}/libgitg{,-ext}-1.0/
%{_libdir}/libgitg{,-ext}-1.0.so
%{_libdir}/pkgconfig/libgitg{,-ext}-1.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gitg{,Ext}-1.0.gir
%dir %{_datadir}/glade
%dir %{_datadir}/glade/catalogs
%{_datadir}/glade/catalogs/gitg-glade.xml
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgitg{,-ext}-1.0.vapi


%changelog
%autochangelog
