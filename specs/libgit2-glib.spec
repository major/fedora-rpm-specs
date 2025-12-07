%global libgit2_version 1.9.0
%global glib2_version 2.44.0

Name:           libgit2-glib
Version:        1.2.1
Release:        %autorelease
Summary:        Git library for GLib

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/Libgit2-glib
Source0:        https://download.gnome.org/sources/libgit2-glib/1.2/libgit2-glib-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(libgit2) >= %{libgit2_version}
BuildRequires:  libssh2-devel
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
BuildRequires:  vala

%description
libgit2-glib is a glib wrapper library around the libgit2 git access library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends:     gi-docgen-fonts

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson -Dgtk_doc=true \
       -Dpython=true

%meson_build

%install
%meson_install

%files
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/libgit2-glib-1.0.so.0{,.*}
%{_libdir}/girepository-1.0/Ggit-1.0.typelib
%dir %{python3_sitearch}/gi
%dir %{python3_sitearch}/gi/overrides
%{python3_sitearch}/gi/overrides/*

%files devel
%{_includedir}/libgit2-glib-1.0/
%{_libdir}/libgit2-glib-1.0.so
%{_libdir}/pkgconfig/libgit2-glib-1.0.pc
%{_datadir}/gir-1.0/Ggit-1.0.gir
%{_datadir}/vala/
%doc %{_datadir}/gtk-doc/

%changelog
%autochangelog
