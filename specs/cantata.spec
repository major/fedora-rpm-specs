%global forgeurl https://github.com/nullobsi/cantata/
%global commit e5df8a52df7345380fa189bd0bb3be1dfd2c831e

Name:    cantata
Summary: Music Player Daemon (MPD) graphical client
Version: 3.3.1
Release: %autorelease
License: GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT

%{forgemeta}

Url:            %{forgeurl}
Source0:        %{forgesource}
Patch0:         %{name}-debn-font-p0.patch
Patch1:         %{name}-debn-qtio-p1.patch
Patch2:         %{name}-drop-qtio-p2.patch

BuildRequires:  kf6-kitemviews-devel
BuildRequires:  kf6-karchive-devel
BuildRequires:  gcc-c++


BuildRequires:  fdupes
BuildRequires:  media-player-info
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils
Requires:       media-player-info
Requires:       hicolor-icon-theme
Requires:       font(fontawesome6brands)
Requires:       font(fontawesome6free)


%description
Cantata is a graphical client for the music player daemon (MPD).

%prep
%forgesetup
# Remove unused bundled libraries — confirmed inactive in Fedora build
rm -rf \
  3rdparty/ebur128-not-used \
  3rdparty/qtsingleapplication-not-used-linux \
  3rdparty/solid-lite-not-used \
  3rdparty/qxt-not-used-linux \
  3rdparty/kcategorizedview-debundle \
  3rdparty/qtiocompressor-removed

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DCMAKE_PREFIX_PATH=%{_libdir}/cmake/Qt6Solutions_IOCompressor \
  -DENABLE_CATEGORIZED_VIEW=OFF \
  -DBUILD_PLUGIN_DEBUG=OFF \
  -DENABLE_DEVICES_SUPPORT=ON \
  -DENABLE_REMOTE_DEVICES=OFF \
  -DENABLE_UDISKS2=OFF \
  -DINSTALL_UBUNTU_ICONS=OFF \
  -DENABLE_SIMPLE_MPD_SUPPORT=ON \
  -DENABLE_AVAHI=ON \
  -DENABLE_SCROBBLING=ON \
  -DENABLE_PROXY_CONFIG=ON \
  -DENABLE_HTTP_SERVER=ON \
  -DENABLE_LIBVLC=OFF \
  -DENABLE_HTTP_STREAM_PLAYBACK=ON
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-qt
%fdupes %{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/dog.unix.cantata.Cantata.desktop

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/Cantata/icons/*
%{_datadir}/Cantata/scripts/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/icons/hicolor/scalable/apps/dog.unix.cantata.Cantata.svg
%{_datadir}/icons/hicolor/symbolic/apps/dog.unix.cantata.Cantata-symbolic.svg
%{_datadir}/icons/hicolor/*x*/apps/dog.unix.cantata.Cantata.png
%dir %{_datadir}/Cantata
%dir %{_datadir}/Cantata/icons
%dir %{_datadir}/Cantata/scripts

%autochangelog
