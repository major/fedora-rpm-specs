%global branch 1.28

Name:        caja
Summary:     File manager for MATE
Version:     %{branch}.0
Release:     %autorelease
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:     GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:         http://mate-desktop.org
Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

Patch1:      caja_0001-caja-file-operations-fix-caption-button-in-destinati.patch
Patch2:      caja_0003-wayland-background-use-mate-appearance-properties-if.patch
Patch3:      caja_0004-build-remove-configure-dependency-on-perl-1789.patch
Patch4:      caja_0005-wayland-ensure-windows-can-be-moved-if-compositor-is.patch
Patch5:      caja_0009-caja-file-operations-fix-estimate-for-queued-copy-17.patch
Patch6:      caja_0010-caja-file-operations-restart-timer-also-for-moves.patch

BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: exempi-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-layer-shell-devel
BuildRequires: cairo-gobject-devel
BuildRequires: libexif-devel
BuildRequires: libselinux-devel
BuildRequires: libSM-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: pango-devel
BuildRequires: startup-notification-devel
BuildRequires: libnotify-devel

Requires:   filesystem
Requires:   redhat-menus
Requires:   gvfs
# >= f43 , see rhbz (#2411809)
%if 0%{?fedora} && 0%{?fedora} >= 43
Requires:   glycin-thumbnailer
%endif

# the main binary links against libcaja-extension.so
# don't depend on soname, rather on exact version
Requires:       %{name}-core-extensions%{?_isa} = %{version}-%{release}

# needed for using mate-text-editor as stanalone in another DE
Requires:       %{name}-schemas%{?_isa} = %{version}-%{release}

%description
Caja (mate-file-manager) is the file manager and graphical shell
for the MATE desktop,
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote file systems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the MATE desktop.

%package core-extensions
Summary:  Mate-file-manager extensions library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description core-extensions
This package provides the libraries used by caja extensions.

# needed for using mate-text-editor (pluma) as stanalone in another DE
%package schemas
Summary:  Mate-file-manager schemas
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:  LicenseRef-Callaway-LGPLv2+

%description schemas
This package provides the gsettings schemas for caja.

%package devel
Summary:  Support for developing mate-file-manager extensions
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides libraries and header files needed
for developing caja extensions.


%prep
%autosetup -p1

# disable startup notification
sed -i s/StartupNotify=true/StartupNotify=false/g data/caja-computer.desktop.in.in
sed -i s/StartupNotify=true/StartupNotify=false/g data/caja-home.desktop.in.in

#Patch2
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
        --disable-static \
        --disable-schemas-compile \
        --disable-update-mimedb \
        --enable-wayland

#drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags} V=1

%install
%{make_install}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/.icon-theme.cache

mkdir -p $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0

desktop-file-install                              \
    --delete-original                             \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
$RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

# Avoid prelink to mess with caja - rhbz (#1228874)
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/prelink.conf.d
cat << EOF > ${RPM_BUILD_ROOT}%{_sysconfdir}/prelink.conf.d/caja.conf
-b %{_libdir}/caja/
-b %{_libdir}/libcaja-extension.so.*
-b %{_libexecdir}/caja-convert-metadata
-b %{_bindir}/caja
-b %{_bindir}/caja-autorun-software
-b %{_bindir}/caja-connect-server
-b %{_bindir}/caja-file-management-properties
EOF

%find_lang %{name} --with-gnome --all-name


%files
%doc AUTHORS COPYING COPYING.LIB NEWS README
%{_bindir}/*
%{_datadir}/caja
%{_libdir}/caja/
%{_sysconfdir}/prelink.conf.d/caja.conf
%{_datadir}/pixmaps/caja/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/emblems/emblem-note.png
%{_mandir}/man1/*
%{_datadir}/metainfo/caja.appdata.xml
%{_datadir}/mime/packages/caja.xml
%{_datadir}/dbus-1/services/org.mate.freedesktop.FileManager1.service

%files core-extensions
%{_libdir}/libcaja-extension.so.*
%{_libdir}/girepository-1.0/*.typelib

%files schemas -f %{name}.lang
%{_datadir}/glib-2.0/schemas/org.mate.*.gschema.xml

%files devel
%{_includedir}/caja/
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libcaja-extension


%changelog
%autochangelog
