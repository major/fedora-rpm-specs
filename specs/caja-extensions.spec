
Name:          caja-extensions
Summary:       Set of extensions for caja file manager
Version:       1.28.0
Release:       %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Source1:       caja-share-setup-instructions
Source2:       caja-share-smb.conf.example

BuildRequires: make
BuildRequires: mate-common
BuildRequires: caja-devel
BuildRequires: mate-desktop-devel
BuildRequires: dbus-glib-devel
BuildRequires: gstreamer1-plugins-bad-free-devel
BuildRequires: gtk3-devel
BuildRequires: gupnp-devel
BuildRequires: dbus-glib-devel

%if 0%{?rhel} <= 7 || 0%{?fedora}
# temporarily disabled
# BuildRequires:  gajim
%endif

%description
Extensions for the caja file-browser, open-terminal,
image-converter, sendto and share

%package common
Summary:    Common files for %{name}
BuildArch:  noarch

%description common
%{summary}.

%package -n caja-audio-video-properties
Summary:    MATE file manager audio-video-properties extension
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-audio-video-properties
The caja-audio-video-properties extension allows you to
view audio and video properties in Caja.

%package -n caja-image-converter
Summary:    MATE file manager image converter extension
Requires:   %{name}-common = %{version}-%{release}
Requires:   ImageMagick

%description -n caja-image-converter
The caja-image-converter extension allows you to
re-size/rotate images from Caja.

%package -n caja-open-terminal
Summary:    Mate-file-manager extension for an open terminal shortcut
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-open-terminal
The caja-open-terminal extension provides a right-click "Open
Terminal" option for mate-file-manager users who prefer that option.

%package -n caja-sendto
Summary:    MATE file manager sendto
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-sendto
The caja-sendto extension provides 'send to' functionality
to the MATE Desktop file-manager, Caja.

%package -n caja-sendto-devel
Summary:    Development libraries and headers for caja-sendto
Requires:   %{name}-common = %{version}-%{release}
Requires:   caja-sendto%{?_isa} = %{version}-%{release}

%description -n caja-sendto-devel
Development libraries and headers for caja-sendto

%package -n caja-share
Summary:    Easy sharing folder via Samba (CIFS protocol)
Requires:   %{name}-common = %{version}-%{release}
Requires:   samba

%description -n caja-share
Caja extension designed for easier folders 
sharing via Samba (CIFS protocol) in *NIX systems.

%package -n caja-beesu
Summary:    MATE file manager beesu
Requires:   %{name}-common = %{version}-%{release}
Requires:   beesu

%description -n caja-beesu
Caja beesu extension for open files as superuser

%package -n caja-wallpaper
Summary:    MATE file manager wallpaper
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-wallpaper
Caja wallpaper extension, allows to quickly set wallpaper.

%package -n caja-xattr-tags
Summary:    MATE file manager xattr-tags
Requires:   %{name}-common = %{version}-%{release}

%description -n caja-xattr-tags
Caja xattr-tags extension, allows to quickly set xattr-tags.


%prep
%autosetup -p1

cp %{SOURCE1} SETUP

#NOCONFIGURE=1 ./autogen.sh

%build
%configure \
     --disable-schemas-compile \
     --enable-image-converter  \
     --enable-open-terminal    \
     --enable-sendto           \
%if 0%{?rhel} > 7
     --with-sendto-plugins=emailclient,caja-burn,pidgin,removable-devices,upnp \
%else
     --with-sendto-plugins=emailclient,caja-burn,pidgin,removable-devices,upnp \
%endif
     --enable-share            \
     --enable-totem-properties \
     --enable-gksu             \
     --enable-wallpaper        \
     --enable-totem-properties \
     --disable-static

make %{?_smp_mflags} V=1

%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

mkdir -p %{buildroot}/%{_sysconfdir}/samba/
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/samba/

%find_lang %{name} --with-gnome --all-name


%files common -f %{name}.lang
%doc AUTHORS COPYING README SETUP
%dir %{_datadir}/caja-extensions

%files -n caja-audio-video-properties
%{_libdir}/caja/extensions-2.0/libcaja-av.so
%{_datadir}/caja/extensions/libcaja-av.caja-extension

%files -n caja-image-converter
%{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja/extensions/libcaja-image-converter.caja-extension

%files -n caja-open-terminal
%{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml
%{_datadir}/caja/extensions/libcaja-open-terminal.caja-extension

%files -n caja-sendto
%{_bindir}/caja-sendto
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%{_libdir}/caja-sendto/plugins/libnstburn.so
%{_libdir}/caja-sendto/plugins/libnstemailclient.so
%{_libdir}/caja-sendto/plugins/libnstpidgin.so
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_libdir}/caja-sendto/plugins/libnstupnp.so
%if 0%{?rhel} <= 7 || 0%{?fedora}
# temporarily disabled
#%{_libdir}/caja-sendto/plugins/libnstgajim.so
%endif
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/caja/extensions/libcaja-sendto.caja-extension
%dir %{_datadir}/gtk-doc/html/caja-sendto
%{_datadir}/gtk-doc/html/caja-sendto/*
%{_mandir}/man1/caja-sendto.1.gz

%files -n caja-sendto-devel
%dir %{_includedir}/caja-sendto
%{_includedir}/caja-sendto/caja-sendto-plugin.h
%{_libdir}/pkgconfig/caja-sendto.pc

%files -n caja-share
%config %{_sysconfdir}/samba/caja-share-smb.conf.example
%{_libdir}/caja/extensions-2.0/libcaja-share.so
%{_datadir}/caja-extensions/share-dialog.ui
%{_datadir}/caja/extensions/libcaja-share.caja-extension

%files -n caja-beesu
%{_libdir}/caja/extensions-2.0/libcaja-gksu.so
%{_datadir}/caja/extensions/libcaja-gksu.caja-extension

%files -n caja-wallpaper
%{_libdir}/caja/extensions-2.0/libcaja-wallpaper.so
%{_datadir}/caja/extensions/libcaja-wallpaper.caja-extension

%files -n caja-xattr-tags
%{_libdir}/caja/extensions-2.0/libcaja-xattr-tags.so
%{_datadir}/caja/extensions/libcaja-xattr-tags.caja-extension


%changelog
%autochangelog
