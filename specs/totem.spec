%global gst_plugins_base_version 1.6.0
%global gtk3_version 3.19.4

%global tarball_version %%(echo %{version} | tr '~' '.')

Name: totem
Epoch: 1
Version: 43.2
Release: %autorelease
Summary: Movie player for GNOME

# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License: LicenseRef-Callaway-GPLv2+-with-exceptions
URL: https://wiki.gnome.org/Apps/Videos
Source0: https://download.gnome.org/sources/%{name}/43/%{name}-%{tarball_version}.tar.xz

# For PyGObject 3.52 transition. Drop after update to totem 44 or higher.
Patch:         girepository-2.0.patch

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0) >= %{gst_plugins_base_version}
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(libportal-gtk3)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libpeas-gtk-1.0)
BuildRequires: pkgconfig(totem-plparser)
BuildRequires: pkgconfig(x11)

# Needed for the videoscale element.
BuildRequires: gstreamer1-plugins-good
# For the gtkglsink element.
BuildRequires: gstreamer1-plugins-good-gtk

BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gtk-doc
BuildRequires: itstool
BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: vala
BuildRequires: /usr/bin/appstream-util
BuildRequires: /usr/bin/desktop-file-validate

# Work-around for fontconfig bug https://bugzilla.redhat.com/show_bug.cgi?id=480928
BuildRequires: liberation-sans-fonts

# For plugins
BuildRequires: pkgconfig(grilo-0.3)
BuildRequires: pkgconfig(grilo-pls-0.3)

Requires: %{name}-video-thumbnailer%{?_isa} = %{epoch}:%{version}-%{release}

# For all the Python plugins
Requires: libpeas-loader-python3%{?_isa}
Requires: python3-gobject

Requires: iso-codes
Requires: gstreamer1%{?_isa}
Requires: gstreamer1-plugins-base%{?_isa} >= %{gst_plugins_base_version}
Requires: gstreamer1-plugins-good%{?_isa}
Requires: gstreamer1-plugins-good-gtk%{?_isa}
%if ! 0%{?flatpak}
Requires: gvfs-fuse%{?_isa}
%endif
# Disabled until ported to GStreamer 1.0
# Requires: gnome-dvb-daemon
Requires: grilo-plugins%{?_isa}
Requires: gsettings-desktop-schemas%{?_isa}
Requires: gtk3%{?_isa} >= %{gtk3_version}

Recommends: gstreamer1-plugin-openh264%{?_isa}
Recommends: gstreamer1-plugins-bad-free%{?_isa}
Recommends: gstreamer1-plugins-ugly-free%{?_isa}

# Removed in F30
Obsoletes: totem-nautilus < 1:3.31.91
# Removed in F31
Obsoletes: totem-lirc < 1:3.33.0

%description
Totem is simple movie player for the GNOME desktop. It features a
simple playlist, a full-screen mode, seek and volume controls, as well as
a pretty complete keyboard navigation.

Totem is extensible through a plugin system.

%package video-thumbnailer
Summary: Totem video thumbnailer
# split out from totem package in F34
Conflicts: totem < 1:3.38.0-4

%description video-thumbnailer
This package contains the Totem video thumbnailer.

%package devel
Summary: Plugin writer's documentation for totem
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
The %{name}-devel package contains API documentation for
developing developing plugins for %{name}.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson -Denable-gtk-doc=true
# -j1 to work-around https://github.com/mesonbuild/meson/issues/1994
%meson_build -j1

%install
%meson_install
%find_lang %{name} --with-gnome

%py_byte_compile %{python3} %{buildroot}%{_libdir}/totem/plugins/

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.Totem.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Totem.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/totem
%{_libdir}/libtotem.so.*
%{_libdir}/girepository-1.0/Totem-1.0.typelib
%{_datadir}/applications/org.gnome.Totem.desktop
%{_datadir}/dbus-1/services/org.gnome.Totem.service
%{_datadir}/metainfo/org.gnome.Totem.appdata.xml
%dir %{_libdir}/totem
%dir %{_libdir}/totem/plugins
# Python plugins
%if 0%{?fedora} || 0%{?rhel} > 7
%{_libdir}/totem/plugins/opensubtitles
%{_libdir}/totem/plugins/pythonconsole
%endif
%{_libdir}/totem/plugins/autoload-subtitles
%{_libdir}/totem/plugins/im-status
%{_libdir}/totem/plugins/open-directory
%{_libdir}/totem/plugins/recent
%{_libdir}/totem/plugins/rotation
%{_libdir}/totem/plugins/screensaver
%{_libdir}/totem/plugins/skipto
%{_libdir}/totem/plugins/properties
%{_libdir}/totem/plugins/mpris
%{_libdir}/totem/plugins/screenshot
%{_libdir}/totem/plugins/save-file
%{_libdir}/totem/plugins/variable-rate
%{_libexecdir}/totem-gallery-thumbnailer
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Totem.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Totem-symbolic.svg
%{_datadir}/icons/hicolor/symbolic/apps/totem-tv-symbolic.svg
%{_mandir}/man1/totem.1*
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.xml

%files video-thumbnailer
%license COPYING
%{_bindir}/totem-video-thumbnailer
%{_mandir}/man1/totem-video-thumbnailer.1*
%{_datadir}/thumbnailers/totem.thumbnailer

%files devel
%{_datadir}/gtk-doc/html/totem
%{_includedir}/totem
%{_libdir}/libtotem.so
%{_libdir}/pkgconfig/totem.pc
%{_datadir}/gir-1.0/Totem-1.0.gir

%changelog
%autochangelog
