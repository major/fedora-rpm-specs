%global commit  727368976518ce70d941d535ef334245ecbe1c9d

Name:           g4music
Version:        4.4
Release:        %autorelease
Summary:        Fast fluent lightweight music player written in GTK4

# GPL-3.0-or-later: the project as a whole
# GPL-2.0-or-later: src/gst/ape-demux.c
# CC0-1.0: The metainfo file
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC0-1.0
URL:            https://gitlab.gnome.org/neithern/g4music
VCS:            git:%{url}.git
Source:         %{url}/-/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  vala

Requires:       dbus-common
Requires:       hicolor-icon-theme

# Provide the new name
Provides:       gapless = %{version}-%{release}
Provides:       gapless%{?_isa} = %{version}-%{release}

%description
G4Music is a fast fluent lightweight music player written in GTK4, with
a beautiful and adaptive user interface.  It focuses on high performance
for large music collections.

Features:
- Supports most music file types, samba and any other remote protocol
  (depends on GIO and GStreamer).
- Fast loading and parsing thousands of music files in a few seconds,
  monitors local changes.
- Low memory usage for large music collections with album covers
  (embedded and external), no thumbnail caches to store.
- Groups and sorts by album/artist/title, shuffle list, full-text
  searching.
- Gaussian blurred cover as background, follows GNOME light/dark mode.
- Drag-drop from GNOME Files, showing music in Files.
- Supports audio peaks visualizer.
- Supports gapless playback.
- Supports normalizing volume with ReplayGain.
- Supports pipewire and other audio sinks.
- Supports MPRIS control.

%prep
%autosetup -n %{name}-v%{version}-%{commit}

%build
%meson --buildtype=release
%meson_build

%install
%meson_install
%find_lang %{name}

%check
# Note that the tests run both desktop-file-validate and appstream-util
# validation
%meson_test

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/g4music
%{_datadir}/applications/com.github.neithern.g4music.desktop
%{_datadir}/dbus-1/services/com.github.neithern.g4music.service
%{_datadir}/glib-2.0/schemas/com.github.neithern.g4music.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.github.neithern.g4music.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.github.neithern.g4music-symbolic.svg
%{_metainfodir}/com.github.neithern.g4music.metainfo.xml

%changelog
%autochangelog
