%global gtk3_version 3.20.0
%global libdmapsharing_version 3.9.11
%global libsecret_version 0.18

%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*/.*\\.so.*$

Name:    rhythmbox
Version: 3.4.8
Release: %autorelease
Summary: Music Management Application

# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License: LicenseRef-Callaway-GPLv2+-with-exceptions AND GFDL-1.1-no-invariants-or-later
URL:     https://wiki.gnome.org/Apps/Rhythmbox
Source0: https://download.gnome.org/sources/rhythmbox/3.4/%{name}-%{version}.tar.xz
Patch0:  libpeas1_pygobject352.patch

BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.10.0
BuildRequires: pkgconfig(grilo-0.3) >= 0.3.1
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libbrasero-media3)
BuildRequires: pkgconfig(libdmapsharing-4.0) >= %{libdmapsharing_version}
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: pkgconfig(libgpod-1.0)
%endif
BuildRequires: pkgconfig(libmtp)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libpeas-gtk-1.0)
BuildRequires: pkgconfig(libsecret-1) >= %{libsecret_version}
BuildRequires: pkgconfig(libsoup-3.0) >= 3.0.7
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(tdb)
BuildRequires: pkgconfig(totem-plparser) >= 3.2.0
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: kernel-headers
BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: yelp-tools
BuildRequires: vala

ExcludeArch:    s390 s390x

Requires: gtk3%{?_isa} >= %{gtk3_version}
%if 0%{?fedora} || 0%{?rhel} >= 9
Recommends: gvfs-afc
%endif
Requires: libdmapsharing4%{?_isa} >= %{libdmapsharing_version}
Requires: libpeas-loader-python3%{?_isa}
Requires: libsecret%{?_isa} >= %{libsecret_version}
Requires: media-player-info
Requires: python3-gobject
Requires: python3-mako
Requires: gstreamer1-plugins-good
Suggests: zeitgeist-libs%{?_isa}

Obsoletes: rhythmbox-upnp < %{version}-%{release}
Provides: rhythmbox-upnp = %{version}-%{release}
Obsoletes: rhythmbox-lirc < %{version}-%{release}
Provides: rhythmbox-lirc = %{version}-%{release}

%description
Rhythmbox is an integrated music management application based on the powerful
GStreamer media framework. It has a number of features, including an easy to
use music browser, searching and sorting, comprehensive audio format support
through GStreamer, Internet Radio support, playlists and more.

Rhythmbox is extensible through a plugin system.

%package devel
Summary: Development files for Rhythmbox plugins
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files necessary to create
a Rhythmbox plugin.

%prep
%autosetup -p1

%build
%meson \
    -Ddaap=enabled \
    -Dlirc=disabled
%meson_build

%install
%meson_install

# Byte-compile Python plugins that are outside the standard Python paths
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/rhythmbox

%find_lang %name --with-gnome

# Don't include header files for plugins
rm -rf %{buildroot}%{_libdir}/rhythmbox/plugins/*/*.h

# Context plugin is disabled, so do not install the files.
rm -rf %{buildroot}%{_libdir}/rhythmbox/plugins/context

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Rhythmbox3*.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md NEWS
%{_bindir}/*
%{_datadir}/rhythmbox/
%{_datadir}/applications/org.gnome.Rhythmbox3.desktop
%{_datadir}/applications/org.gnome.Rhythmbox3.device.desktop
%{_datadir}/dbus-1/services/org.gnome.Rhythmbox3.service
%{_datadir}/glib-2.0/schemas/org.gnome.rhythmbox.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Rhythmbox3.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Rhythmbox3-symbolic.svg
%{_metainfodir}/org.gnome.Rhythmbox3.appdata.xml
%{_libdir}/librhythmbox-core.so*
%dir %{_libdir}/rhythmbox
%dir %{_libdir}/rhythmbox/plugins
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/rhythmbox/plugins/android/
%{_libdir}/rhythmbox/plugins/artsearch/
%{_libdir}/rhythmbox/plugins/audiocd/
%{_libdir}/rhythmbox/plugins/audioscrobbler/
%{_libdir}/rhythmbox/plugins/cd-recorder/
%{_libdir}/rhythmbox/plugins/daap/
%{_libdir}/rhythmbox/plugins/dbus-media-server/
%{_libdir}/rhythmbox/plugins/fmradio/
%{_libdir}/rhythmbox/plugins/generic-player/
%{_libdir}/rhythmbox/plugins/grilo/
%{_libdir}/rhythmbox/plugins/im-status/
%{_libdir}/rhythmbox/plugins/ipod/
%{_libdir}/rhythmbox/plugins/iradio/
%{_libdir}/rhythmbox/plugins/listenbrainz/
%{_libdir}/rhythmbox/plugins/lyrics/
%{_libdir}/rhythmbox/plugins/magnatune/
%{_libdir}/rhythmbox/plugins/mpris/
%{_libdir}/rhythmbox/plugins/mtpdevice/
%{_libdir}/rhythmbox/plugins/notification/
%{_libdir}/rhythmbox/plugins/power-manager/
%{_libdir}/rhythmbox/plugins/python-console/
%{_libdir}/rhythmbox/plugins/rb/
%{_libdir}/rhythmbox/plugins/rbzeitgeist/
%{_libdir}/rhythmbox/plugins/replaygain/
%{_libdir}/rhythmbox/plugins/webremote/
%{_libexecdir}/rhythmbox-metadata
%{_mandir}/man1/rhythmbox*.1*

%files devel
%{_includedir}/rhythmbox/
%{_libdir}/pkgconfig/rhythmbox.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/

%changelog
%autochangelog
