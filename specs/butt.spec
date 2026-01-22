%global rdnn de.danielnoethen.butt

Name:           butt
Version:        1.46.0
Release:        %autorelease
Summary:        Broadcast using this tool
# Entire source code is GPL-2.0-or-later except:
# src/opus_encode.cpp: GPL-2.0-or-later AND BSD-2-Clause
# src/cJSON.{cpp,h}: MIT
License:        GPL-2.0-or-later AND BSD-2-Clause AND MIT
URL:            https://danielnoethen.de/butt/
Source:         %{url}/release/%{version}/butt-%{version}.tar.gz

# Minimal fixes to build with FLTK 1.4. Please send upstream.
Patch0:         butt-headers.patch

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  gettext
BuildRequires:  gettext-devel

# https://danielnoethen.de/butt/manual.html#_install
BuildRequires:  fltk-devel
BuildRequires:  portaudio-devel
BuildRequires:  lame-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libogg-devel
BuildRequires:  flac-devel
BuildRequires:  opus-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  fdk-aac-free-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  portmidi-devel
BuildRequires:  libX11-devel

# for desktop-file-validate command
BuildRequires:  desktop-file-utils
# for appstream-util command
BuildRequires:  libappstream-glib
BuildRequires:  make

Requires:       hicolor-icon-theme


%description
butt (broadcast using this tool) is an easy to use, multi OS streaming tool.
It supports ShoutCast and IceCast and runs on Linux, MacOS and Windows.  The
main purpose of butt is to stream live audio data from your computers Mic or
Line input to an Shoutcast or Icecast server. Recording is also possible.  It
is NOT intended to be a server by itself or automatically stream a set of audio
files.


%prep
%autosetup -p 1


%build
autoreconf -ifv
%configure
%make_build


%install
%make_install

# desktop file
install -Dpm 0644 usr/share/applications/butt.desktop %{buildroot}%{_datadir}/applications/%{rdnn}.desktop

# icons
for size in 16 22 24 32 48 64 96 128 256 512; do
    path=icons/hicolor/${size}x${size}/apps/butt.png
    install -Dpm 0644 usr/share/$path %{buildroot}%{_datadir}/$path
done
install -Dpm 0644 usr/share/icons/hicolor/scalable/apps/butt.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/butt.svg

# pixmaps
for size in 16 32; do
    path=pixmaps/butt$size.xpm
    install -Dpm 0644 usr/share/$path %{buildroot}%{_datadir}/$path
done

# appdata
install -Dpm 0644 usr/share/metainfo/%{rdnn}.metainfo.xml %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml

# locales
%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/butt
%{_datadir}/applications/%{rdnn}.desktop
%{_datadir}/icons/hicolor/*/apps/butt.*
%{_datadir}/pixmaps/butt*.xpm
%{_metainfodir}/%{rdnn}.metainfo.xml


%changelog
%autochangelog
