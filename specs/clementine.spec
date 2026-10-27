%global tag     1.4.3-5-g7e2131d44

Name:           clementine
Version:        1.4.3
Release:        %autorelease
Summary:        A music player and library organizer

# BSD-3-clause:
#   - 3rdparty/cast_channel
#   - 3rdparty/qxt
# GPL-2.0-or-later:
#   - src/engines/gstengine.cpp
#   - src/engines/gstengine.h
#   - src/widgets/sliderwidget.cpp
#   - src/widgets/sliderwidget.h
# LGPL-2.0-or-later:
#   - gst/moodbar/gstfastspectrum.cpp
#   - gst/moodbar/gstfastspectrum.h
# LGPL-2.1-only:
#   - src/widgets/stylehelper:
# LGPL-2.1-or-later:
#   - 3rdparty/libprojectm
# LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only:
#   - 3rdparty/qsqlite/clementinesqlcachedresult.cpp
#   - 3rdparty/qsqlite/clementinesqlcachedresult.h
#   - 3rdparty/qsqlite/qsql_sqlite.cpp
#   - 3rdparty/qsqlite/qsql_sqlite.h
#   - 3rdparty/qtiocompressor/qtiocompressor.cpp
#   - 3rdparty/qtiocompressor/qtiocompressor.h
# LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR LGPL-3.0-only WITH Qt-LGPL-exception-1.1:
# but Qt-LGPL-exception-1.1 refers to nonexistent file so we can ignore this exception so it is:
# LGPL-2.1-only OR LGPL-3.0-only
#   - 3rdparty/qsqlite/smain.cpp
#   - 3rdparty/qsqlite/smain.h
# MIT: 3rdparty/qocoa
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND Apache-2.0 AND BSD-3-Clause AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:            https://www.clementine-player.org/
VCS:            https://github.com/clementine-player/Clementine
Source:         %vcs/archive/%{tag}/%{name}-%{tag}.tar.gz

# Use system libraries (qtiocompressor)
Patch:          0001-Use-QtIoCompressor-from-Qt6.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libmygpo-qt6)
#BuildRequires:  pkgconfig(libprojectM) >= 4.2
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsparsehash)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sqlite3) >= 3.7
BuildRequires:  pkgconfig(taglib) >= 1.11
BuildRequires:  qtiocompressor-devel
BuildRequires:  qtsingleapplication-qt6-devel
BuildRequires:  qtsinglecoreapplication-qt6-devel

Requires:       gstreamer1-plugins-good
Requires:       hicolor-icon-theme

Provides:       bundled(cast_channel)
Provides:       bundled(libprojectM) = 4.2.0
Provides:       bundled(libqxt) = 0.7.0
Provides:       bundled(qocoa)
Provides:       bundled(qsqlite)

%description
Clementine is a modern music player and library organiser.
It is inspired by Amarok 1.4, focusing on a fast and easy-to-use interface for
searching and playing your music.

Features include:
  * Search and play your local music library
  * Listen to internet radio from Last.fm, SomaFM, IntergalacticFM, Magnatune,
    Jamendo and Icecast
  * Create smart playlists and dynamic playlists
  * Tabbed playlists, import and export M3U, XSPF, PLS and ASX
  * Visualisations from projectM
  * Lyrics and artist biographies and photos
  * Transcode music into MP3, Ogg Vorbis, Ogg Speex, FLAC or AAC
  * Edit tags on MP3 and OGG files, organise your music
  * Download missing album cover art from Last.fm
  * Cross-platform - works on Windows, Mac OS X and Linux
  * Native desktop notifications on Linux (libnotify) and Mac OS X (Growl)
  * Remote control using a Wii Remote, MPRIS or the command-line
  * Copy music to your iPod, iPhone, MTP or mass-storage USB player
  * Queue manager

%prep
%autosetup -p1 -n Clementine-%{tag}

# fix dependency naming for Fedora
sed -i -e '/pkg_check_modules.*LIBMYGPO_QT/s/qt5/qt6/' CMakeLists.txt

# Remove most 3rdparty libraries
mv 3rdparty/{cast_channel,libprojectm,qocoa,qsqlite,qxt}/ .
rm -rfv 3rdparty/*
mv {cast_channel,libprojectm,qocoa,qsqlite,qxt}/ 3rdparty/

%build
%cmake \
  -DBUILD_WERROR:BOOL=OFF \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
  -DFORCE_GIT_REVISION:STRING=%{tag} \
  -DUSE_SYSTEM_PROJECTM:BOOL=OFF \
  -DUSE_SYSTEM_QTSINGLEAPPLICATION:BOOL=ON \
  -DUSE_SYSTEM_TAGLIB:BOOL=ON
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.clementine_player.Clementine.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.clementine_player.Clementine.appdata.xml

%files
%license COPYING
%doc Changelog README.md
%{_bindir}/clementine
%{_bindir}/clementine-tagreader
%{_datadir}/applications/org.clementine_player.Clementine.desktop
%{_datadir}/icons/hicolor/*/apps/org.clementine_player.Clementine.*
%{_datadir}/kservices5/clementine-*.protocol
%{_metainfodir}/org.clementine_player.Clementine.appdata.xml

%changelog
%autochangelog
