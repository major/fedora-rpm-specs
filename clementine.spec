%define version_no_tilde() %{lua:
    ver = rpm.expand('%version')
    ver = ver:gsub('~', '')
    print(ver)
}

Name:           clementine
Version:        1.4.0~rc2
Release:        %autorelease
Summary:        A music player and library organizer

# 3rdparty/taglib, src/widgets/fancytabwidget and src/widgets/stylehelper: LGPLv2
# 3rdparty/utf8-cpp: Boost
License:        GPLv3+ and GPLv2+ and Boost and LGPLv2
URL:            https://www.clementine-player.org/
Source0:        https://github.com/clementine-player/Clementine/archive/%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz

# Use qt5 libraries (qtiocompressor)
Patch11:        clementine-qt5-libraries.patch

BuildConflicts: pkgconfig(gmock) >= 1.6
BuildConflicts: pkgconfig(gtest)
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  liblastfm-qt5-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cryptopp)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libmygpo-qt5)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libprojectM) >= 2.0.1-7
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsparsehash)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(QxtCore-qt5)
BuildRequires:  pkgconfig(sqlite3) >= 3.7
BuildRequires:  pkgconfig(taglib) >= 1.11
BuildRequires:  pkgconfig(udisks)
BuildRequires:  qt5-linguist
BuildRequires:  qtiocompressor-devel
BuildRequires:  qtsingleapplication-qt5-devel >= 2.6.1-2
BuildRequires:  qtsinglecoreapplication-qt5-devel
BuildRequires:  sha2-devel
%ifnarch s390 s390x
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libimobiledevice-1.0)
%endif

Requires:       gstreamer1-plugins-good
Requires:       hicolor-icon-theme
Requires:       qtiocompressor >= 2.3.1-17

Provides:       bundled(utf8-cpp)

%description
Clementine is a multi-platform music player. It is inspired by Amarok 1.4,
focusing on a fast and easy-to-use interface for searching and playing your
music.

%prep
%autosetup -p1 -n Clementine-%{version_no_tilde}

# Remove most 3rdparty libraries
# Unbundle taglib next release:
# https://github.com/taglib/taglib/issues/837#issuecomment-428389347
mv 3rdparty/{gmock,qocoa,qsqlite,utf8-cpp}/ .
rm -fr 3rdparty/*
mv {gmock,qocoa,qsqlite,utf8-cpp}/ 3rdparty/
# Not needed and fails build
sed -i "/add_dependencies(clementine_lib qtsingleapplication)/d" src/CMakeLists.txt
# Use system-wide qtiocompressor
sed -i 's|#include "3rdparty/qtiocompressor/qtiocompressor.h"|#include "qtiocompressor.h"|' src/internet/spotifywebapi/spotifywebapiservice.cpp
# Fix for GCC 12, to send upstream when root cause is determined
sed -i 's|local_server_name_ = qApp->applicationName().toLower();|local_server_name_ = QString(qApp->applicationName()).toLower();|' ext/libclementine-common/core/workerpool.h

%build
# QT applications need to avoid local binding and copy relocations.  Forcing them to build with
# -fPIC solves that problem
%global optflags %{optflags} -fPIC
%{cmake} \
  -DBUILD_WERROR:BOOL=OFF \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DUSE_SYSTEM_QTSINGLEAPPLICATION=1 \
  -DUSE_SYSTEM_PROJECTM=1 \
  -DUSE_SYSTEM_QXT=1
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.clementine_player.Clementine.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.clementine_player.Clementine.appdata.xml

%files
%license COPYING
%doc Changelog
%{_bindir}/clementine
%{_bindir}/clementine-tagreader
%{_metainfodir}/org.clementine_player.Clementine.appdata.xml
%{_datadir}/applications/org.clementine_player.Clementine.desktop
%{_datadir}/icons/hicolor/*/apps/org.clementine_player.Clementine.*
%{_datadir}/kservices5/clementine-*.protocol

%changelog
%autochangelog
