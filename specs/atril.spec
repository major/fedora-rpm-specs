
Name:          atril
Version:       1.28.1
Release:       %autorelease
Summary:       Document viewer
# Automatically converted from old format: GPLv2+ and LGPLv2+ and MIT - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: gtk3-devel
BuildRequires: poppler-glib-devel
BuildRequires: libarchive-devel
BuildRequires: libXt-devel
BuildRequires: libsecret-devel
BuildRequires: libtiff-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libspectre-devel
BuildRequires: desktop-file-utils
BuildRequires: gobject-introspection-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: cairo-gobject-devel
BuildRequires: yelp-tools

# for the xps back-end
BuildRequires: libgxps-devel
# for the caja properties page
BuildRequires: caja-devel
# for the dvi back-end
BuildRequires: texlive-lib-devel
# for the djvu back-end
BuildRequires: djvulibre-devel
# for epub back-end
BuildRequires: webkit2gtk4.1-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
#  fix (#974791)
Requires:       mate-desktop-libs
Requires:       mathjax

%description
Mate-document-viewer is simple document viewer.
It can display and print Portable Document Format (PDF),
PostScript (PS), Encapsulated PostScript (EPS), DVI, DJVU, epub and XPS files.
When supported by the document format, mate-document-viewer
allows searching for text, copying text to the clipboard,
hypertext navigation, table-of-contents bookmarks and editing of forms.


%package libs
Summary: Libraries for the mate-document-viewer

%description libs
This package contains shared libraries needed for mate-document-viewer.


%package devel
Summary: Support for developing back-ends for the mate-document-viewer
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files needed for
mate-document-viewer back-ends development.


%package caja
Summary: Mate-document-viewer extension for caja
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: caja

%description caja
This package contains the mate-document-viewer extension for the
caja file manager.
It adds an additional tab called "Document" to the file properties dialog.

%package thumbnailer
Summary: Atril thumbnailer extension for caja
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: caja

%description thumbnailer
This package contains the atril extension for the
caja file manager.


%prep
%autosetup -p1
#NOCONFIGURE=1 ./autogen.sh

%build
%configure \
        --disable-static \
        --disable-schemas-compile \
        --enable-introspection \
        --enable-comics \
        --enable-dvi=yes \
        --enable-djvu=yes \
        --enable-t1lib=no \
        --enable-pixbuf \
        --enable-xps \
        --enable-epub \
        --enable-synctex

# remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1


%install
%{make_install}

%find_lang %{name} --with-gnome --all-name

find $RPM_BUILD_ROOT -name '*.la' -exec rm -fv {} ';'


%check
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/atril.desktop


%files -f %{name}.lang
%doc README.md COPYING NEWS AUTHORS
%{_bindir}/*
%dir %{_datadir}/atril
%{_datadir}/atril/*
%{_datadir}/applications/atril.desktop
%{_datadir}/icons/hicolor/*/apps/atril.*
%{_libexecdir}/atrild
%{_datadir}/dbus-1/services/org.mate.atril.Daemon.service
%{_datadir}/glib-2.0/schemas/org.mate.Atril.gschema.xml
%{_datadir}/metainfo/atril.appdata.xml
%{_mandir}/man1/atril-*.1.*
%{_mandir}/man1/atril.1.*

%files libs
%{_libdir}/libatrilview.so.*
%{_libdir}/libatrildocument.so.*
%{_libdir}/atril/3/backends/
%{_libdir}/girepository-1.0/AtrilDocument-1.5.0.typelib
%{_libdir}/girepository-1.0/AtrilView-1.5.0.typelib

%files caja
%{_libdir}/caja/extensions-2.0/libatril-properties-page.so
%{_datadir}/caja/extensions/libatril-properties-page.caja-extension

%files thumbnailer
%{_datadir}/thumbnailers/atril.thumbnailer

%files devel
%dir %{_includedir}/atril/
%{_includedir}/atril/1.5.0/
%{_libdir}/libatrilview.so
%{_libdir}/libatrildocument.so
%{_libdir}/pkgconfig/atril-view-1.5.0.pc
%{_libdir}/pkgconfig/atril-document-1.5.0.pc
%{_datadir}/gir-1.0/AtrilDocument-1.5.0.gir
%{_datadir}/gir-1.0/AtrilView-1.5.0.gir
%{_datadir}/gtk-doc/html/libatrildocument-1.5.0/
%{_datadir}/gtk-doc/html/libatrilview-1.5.0/
%{_datadir}/gtk-doc/html/atril/


%changelog
%autochangelog
