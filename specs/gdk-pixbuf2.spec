%global glib2_version 2.56.0
%ifarch i686
%global with_glycin 0
%else
%global with_glycin 1
%endif

Name:           gdk-pixbuf2
Version:        2.43.3
Release:        %autorelease
Summary:        An image loading library

License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gdk-pixbuf
Source0:        https://download.gnome.org/sources/gdk-pixbuf/2.43/gdk-pixbuf-%{version}.tar.xz

BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
%if %{with_glycin}
BuildRequires:  pkgconfig(glycin-2)
%endif
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
# gdk-pixbuf does a configure time check which uses the GIO mime
# layer; we need to actually have the mime type database.
BuildRequires:  shared-mime-info
BuildRequires:  /usr/bin/rst2man

Requires: glib2%{?_isa} >= %{glib2_version}
# We also need MIME information at runtime
Requires: shared-mime-info

%description
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
clutter.

%package modules
Summary: GIF and TIFF modules for gdk-pixbuf2
Requires: %{name}%{?_isa} = %{version}-%{release}
# Recommend external pixbuf loaders for popular image formats only.
# Please do not recommend obscure image formats here.
%if ! 0%{?rhel}
# these are not shipped in RHEL
Recommends: avif-pixbuf-loader
Recommends: jxl-pixbuf-loader
Recommends: webp-pixbuf-loader
%endif
Recommends: rsvg-pixbuf-loader

%description modules
This package contains the additional modules that are needed to load GIF and
TIFF images.

%package devel
Summary: Development files for gdk-pixbuf2
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa} >= %{glib2_version}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends: gi-docgen-fonts

%description devel
This package contains the libraries and header files that are needed
for writing applications that are using gdk-pixbuf2.

%package tests
Summary: Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%autosetup -n gdk-pixbuf-%{version} -p1

%build
%meson \
       -Ddocumentation=true \
       -Dman=true \
       -Dandroid=disabled \
%if !%{with_glycin}
       -Dglycin=disabled \
%endif
       %{nil}

%global _smp_mflags -j1
%meson_build

%install
%meson_install

touch $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache

# Rename gdk-pixbuf-query-loaders
(cd $RPM_BUILD_ROOT%{_bindir}
 mv gdk-pixbuf-query-loaders gdk-pixbuf-query-loaders-%{__isa_bits}
)
# ... and fix up gdk-pixbuf-query-loaders reference in the .pc file
sed -i -e 's/gdk-pixbuf-query-loaders/gdk-pixbuf-query-loaders-%{__isa_bits}/' \
    $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gdk-pixbuf-2.0.pc

%find_lang gdk-pixbuf

%transfiletriggerin -- %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
gdk-pixbuf-query-loaders-%{__isa_bits} --update-cache

%transfiletriggerpostun -- %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
gdk-pixbuf-query-loaders-%{__isa_bits} --update-cache

%files -f gdk-pixbuf.lang
%license COPYING
%doc NEWS README.md
%{_libdir}/libgdk_pixbuf-2.0.so.*
%{_libdir}/girepository-1.0
%dir %{_libdir}/gdk-pixbuf-2.0
%dir %{_libdir}/gdk-pixbuf-2.0/2.10.0
%dir %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
%ghost %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
%{_bindir}/gdk-pixbuf-query-loaders-%{__isa_bits}
%{_bindir}/gdk-pixbuf-thumbnailer
%{_mandir}/man1/gdk-pixbuf-query-loaders.1*
%{_datadir}/thumbnailers/

%files modules
%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/*.so

%files devel
%dir %{_includedir}/gdk-pixbuf-2.0
%{_includedir}/gdk-pixbuf-2.0/gdk-pixbuf
%{_libdir}/libgdk_pixbuf-2.0.so
%{_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{_bindir}/gdk-pixbuf-csource
%{_bindir}/gdk-pixbuf-pixdata
%{_datadir}/gir-1.0/
%{_mandir}/man1/gdk-pixbuf-csource.1*
%doc %{_datadir}/doc/gdk-pixbuf/
%doc %{_datadir}/doc/gdk-pixdata/

%files tests
%{_libexecdir}/installed-tests
%{_datadir}/installed-tests

%changelog
%autochangelog
