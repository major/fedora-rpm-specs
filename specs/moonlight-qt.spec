%global         forgeurl0 https://github.com/moonlight-stream/moonlight-qt

# TODO: Debundle these once the build-system can do that
%global         forgeurl1 https://github.com/moonlight-stream/moonlight-common-c
%global         forgeurl2 https://github.com/cgutman/qmdnsengine
%global         forgeurl3 https://github.com/gabomdq/SDL_GameControllerDB
%global         forgeurl4 https://github.com/cgutman/enet
%global         forgeurl5 https://github.com/sleepybishop/nanors

%global         version0  6.2.0
%global         date      20261105
%global         commit    3fead131a6cb21f27d50bf9eb543b004d4a44f1f

%global         commit1   04053843c90c4268583f2496b997d54d59f03957
%global         commit2   920c097ffa742e2968290f15d4dde6693aec02e5
%global         commit3   8d9fefd7b810f2541f78cc7a8ccbd185bc84c7a5
%global         commit4   aca87840b57f045a1f7f9299e4b1b9b8e2a5e2f1
%global         commit5   b1e3c22ca0cdc0bb83e3cd6ed1a2fc77869ed99a

Provides:       bundled(moonlight-common-c) = 0~git%{commit1}
Provides:       bundled(qmdnsengine) = 0.1.0^git%{commit2}
Provides:       bundled(SDL_GameControllerDB) = 0~git%{commit3}
Provides:       bundled(h264bitstream)
Provides:       bundled(enet) = 1.3.17^git%{commit4}
Provides:       bundled(nanors) = 0~git%{commit5}

Name:           moonlight-qt
Release:        %autorelease
%forgemeta -a
Version:        %forgeversion
Summary:        GameStream client for PCs

# License breakdown:
# - Main project: GPL-3.0-or-later
# - moonlight-common-c/moonlight-common-c: GPL-3.0-or-later
# - qmdnsengine/qmdnsengine: MIT
# - app/SDL_GameControllerDB: Zlib
# - h264bitstream/h264bitstream: LGPL-2.1-or-later
# - moonlight-common-c/moonlight-common-c/enet: MIT
# - moonlight-common-c/moonlight-common-c/nanors: MIT

License:        GPL-3.0-or-later AND MIT AND Zlib AND LGPL-2.1-or-later
URL:            %forgeurl0
Source0:        %forgesource0
Source1:        %forgesource1
Source2:        %forgesource2
Source3:        %forgesource3
Source4:        %forgesource4
Source5:        %forgesource5

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libavcodec) >= 60
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libplacebo) >= 7.349.0
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)

# Directory ownership
Requires: hicolor-icon-theme

%description
Moonlight is an open-source game-streaming client for Sunshine and NVIDIA
GameStream hosts. This package tracks the upstream master branch and is built
entirely from source, including its pinned Git submodules.


%prep
%forgeautosetup -p1
tar -xf %{SOURCE1} --strip-components=1 -C moonlight-common-c/moonlight-common-c
tar -xf %{SOURCE2} --strip-components=1 -C qmdnsengine/qmdnsengine
tar -xf %{SOURCE3} --strip-components=1 -C app/SDL_GameControllerDB
tar -xf %{SOURCE4} --strip-components=1 -C moonlight-common-c/moonlight-common-c/enet
tar -xf %{SOURCE5} --strip-components=1 -C moonlight-common-c/moonlight-common-c/nanors

cp qmdnsengine/qmdnsengine/LICENSE.txt LICENSE-qmdnsengine
cp app/SDL_GameControllerDB/LICENSE LICENSE-SDL_GameControllerDB
cp moonlight-common-c/moonlight-common-c/enet/LICENSE LICENSE-enet
cp moonlight-common-c/moonlight-common-c/nanors/LICENSE LICENSE-nanors
cp h264bitstream/LICENSE LICENSE-h264bitstream


%conf
%qmake_qt6 \
  "PREFIX=%{_prefix}"


%build
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}


%check
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/com.moonlight_stream.Moonlight.desktop
appstreamcli validate --no-net \
    %{buildroot}%{_datadir}/metainfo/com.moonlight_stream.Moonlight.appdata.xml


%files
%license LICENSE LICENSE-qmdnsengine LICENSE-SDL_GameControllerDB LICENSE-h264bitstream LICENSE-enet LICENSE-nanors
%doc README.md
%{_bindir}/moonlight
%{_datadir}/applications/com.moonlight_stream.Moonlight.desktop
%{_datadir}/icons/hicolor/scalable/apps/moonlight.svg
%{_datadir}/metainfo/com.moonlight_stream.Moonlight.appdata.xml


%changelog
%autochangelog
