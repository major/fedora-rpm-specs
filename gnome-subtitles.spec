%global debug_package %{nil}

Name:           gnome-subtitles
Version:        1.8
Release:        %autorelease
Summary:        Subtitle editor for Gnome

#Files under src/External/NCharDet are MPLv1.1 or GPLv2+ or LGPLv2+
License:        GPLv2+ and (MPLv1.1 or GPLv2+ or LGPLv2+)
URL:            https://gnomesubtitles.org/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        https://gstreamer.freedesktop.org/src/gstreamer-sharp/gstreamer-sharp-1.20.3.tar.xz
Source2:        https://github.com/GLibSharp/GtkSharp/archive/3.22.2/GtkSharp-3.22.2.tar.gz
Source3:        https://github.com/GLibSharp/bindinator/archive/13cdbcdb9bd9e05666e56e7e374027fa719acda4/bindinator-13cdbcd.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
#https://gitlab.gnome.org/GNOME/gnome-subtitles/-/issues/199
#BuildRequires:  pkgconfig(gtk-sharp-3.0)
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  mono-web
BuildRequires:  perl(XML::Parser)
#pulled in by bundled gstreamer-sharp
BuildRequires:  pkgconfig(gstreamer-webrtc-1.0)
BuildRequires:  pkgconfig(gst-editing-services-1.0)

Requires:       enchant
Requires:       gstreamer1-plugins-good-gtk
Requires:       hicolor-icon-theme
Requires:       mono-locale-extras

Provides:       bundled(gstreamer1-sharp) = 1.20.3

# Mono only available on these:
ExclusiveArch: %mono_arches

%global _privatelibs mono\\(gstreamer-sharp\\).*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%description
Gnome Subtitles is a subtitle editor for the GNOME desktop. It supports the
most common text-based subtitle formats and allows for subtitle editing,
translation and synchronization.

%prep
%autosetup -p1
%autosetup -T -D -a 1
%autosetup -T -D -a 2
%autosetup -T -D -a 3
mv gstreamer-sharp-1.20.3 subprojects/gstreamer-sharp
mv GtkSharp-3.22.2 subprojects/gtk-sharp
mv bindinator-13cdbcdb9bd9e05666e56e7e374027fa719acda4 subprojects/bindinator


%build
%meson -Dinstall_gtk_sharp=false -Dgstreamer-sharp:tests=disabled
%meson_build


%install
%meson_install
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.GnomeSubtitles.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml

%find_lang org.gnome.GnomeSubtitles


%files -f org.gnome.GnomeSubtitles.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/org.gnome.GnomeSubtitles.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.GnomeSubtitles.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/org.gnome.GnomeSubtitles.appdata.xml


%changelog
%autochangelog
