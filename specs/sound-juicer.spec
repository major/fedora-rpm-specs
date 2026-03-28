Name:           sound-juicer
Version:        3.40.0
Release:        %autorelease
Summary:        Clean and lean CD ripper

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/SoundJuicer
Source0:        https://download.gnome.org/sources/%{name}/3.40/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libbrasero-media3)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libdiscid)
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  /usr/bin/appstream-util

ExcludeArch:    s390 s390x

Requires:       gstreamer1-plugins-good

%description
GStreamer-based CD ripping tool. Saves audio CDs to Ogg/vorbis.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

# These are installed to the correct location with the doc macro down below
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/AUTHORS
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/COPYING
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/NEWS
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/README.md

%find_lang sound-juicer --with-gnome

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.SoundJuicer.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.SoundJuicer.desktop

%files -f sound-juicer.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/sound-juicer
%{_datadir}/sound-juicer
%{_datadir}/applications/org.gnome.SoundJuicer.desktop
%{_datadir}/dbus-1/services/org.gnome.SoundJuicer.service
%{_datadir}/GConf/gsettings/sound-juicer.convert
%{_datadir}/glib-2.0/schemas/org.gnome.sound-juicer.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.SoundJuicer.png
%{_datadir}/metainfo/org.gnome.SoundJuicer.metainfo.xml
%{_mandir}/man1/*

%changelog
%autochangelog
