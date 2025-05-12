%global branch 1.28

Name:          eom
Version:       %{branch}.0
Release:       %autorelease
Summary:       Eye of MATE image viewer
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ 
URL:           http://mate-desktop.org 
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: exempi-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtk3-devel
BuildRequires: ImageMagick-devel
BuildRequires: lcms2-devel
BuildRequires: libexif-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpeas1-devel
BuildRequires: librsvg2-devel
BuildRequires: libxml2-devel
BuildRequires: mate-common
BuildRequires: make
BuildRequires: mate-desktop-devel
BuildRequires: zlib-devel

#fix rhbz (#1008249)
Requires:      mate-desktop-libs
Requires:      libpeas-loader-python3

%description
The Eye of MATE (eom) is the official image viewer for the
MATE desktop. It can view single image files in a variety of formats, as
well as large image collections.
Eye of Mate is extensible through a plugin system.

%package devel
Summary:  Support for developing plugins for the eom image viewer
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for eom


%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure \
   --with-x \
   --disable-schemas-compile \
   --enable-introspection=yes \
   --enable-thumbnailer \
   --without-gdk-pixbuf-thumbnailer
           
make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                               \
  --delete-original                                \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
$RPM_BUILD_ROOT%{_datadir}/applications/eom.desktop

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_mandir}/man1/*
%{_bindir}/eom
%{_bindir}/eom-thumbnailer
%dir %{_libdir}/eom
%dir %{_libdir}/eom/plugins
%{_libdir}/eom/plugins/*
%{_libdir}/girepository-1.0/Eom-1.0.typelib
%{_datadir}/applications/eom.desktop
%{_datadir}/eom/
%{_datadir}/icons/hicolor/*
%{_datadir}/glib-2.0/schemas/org.mate.eom.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.eom.enums.xml
%{_datadir}/metainfo/eom.appdata.xml
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/eom-thumbnailer.thumbnailer

%files devel
%{_libdir}/pkgconfig/eom.pc
%dir %{_includedir}/eom-2.20
%dir %{_includedir}/eom-2.20/eom
%{_includedir}/eom-2.20/eom/*.h
%{_datadir}/gtk-doc/html/eom/
%{_datadir}/gir-1.0/*.gir


%changelog
%autochangelog
