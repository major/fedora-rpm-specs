%global srcname attract
%global forgeurl https://github.com/mickelson/%{srcname}

%global build_flags prefix="%{_prefix}" FE_HWACCEL_VAAPI=1 FE_HWACCEL_VDPAU=1

Name:           attract-mode
Version:        2.7.0
Release:        %autorelease
Summary:        A graphical front-end for command line emulators

# attract-mode itself is GPLv3
# The other licenses cover the bundled libraries, see below for the breakdown
License:        GPL-3.0-or-later AND BSL-1.0 AND LicenseRef-Fedora-Public-Domain AND MIT AND zlib
URL:            https://attractmode.org
Source:         %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Fix missing include
Patch:          %{forgeurl}/commit/659b66c6dc0e5598546ce987319adaf59cf01a0b.patch
# Add compatibility with FFMPEG 7.0
# https://github.com/mickelson/attract/pull/756
Patch:          0001-Add-compatibility-with-FFMPEG-7.0.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make

BuildRequires:  curl-devel
BuildRequires:  expat-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  libarchive-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  openal-soft-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  rapidjson-devel
BuildRequires:  SFML-devel
# Enforce the the minimum EVR to contain fixes for all of:
# CVE-2021-28021 CVE-2021-42715 CVE-2021-42716 CVE-2022-28041 CVE-2023-43898
# CVE-2023-45661 CVE-2023-45662 CVE-2023-45663 CVE-2023-45664 CVE-2023-45666
# CVE-2023-45667
BuildRequires:  stb_image-devel >= 2.28^20231011gitbeebb24-12
# Header-only library: -static is for tracking per guidelines
BuildRequires:  stb_image-static
BuildRequires:  zlib-devel

Requires:       %{name}-data = %{version}-%{release}

# Recommend default font to ensure we can always start
Recommends:     gnu-free-sans-fonts

# Suggest supported emulators from config/emulators/script/db.nut
Recommends:     mame
Suggests:       atari800
Suggests:       dolphin-emu
Suggests:       dosbox-staging
# fbalpha isn't packaged
# fs-uae is in rpmfusion
# fusion isn't packaged
# gens is in rpmfusion
Suggests:       mednafen
Suggests:       mupen64plus
# Nestopia is in rpmfusion
# pcsx isn't packaged
# pcsx2 is in rpmfusion
Suggests:       scummvm
# snes9x is in rpmfusion
# steam is in rpmfusion
# stella is in rpmfusion
# supermodel isn't packaged
# vice is in rpmfusion
# virtualjaguar isn't packaged
# zsnes is in rpmfusion

# Imported in 783a48a2f741c2caf5d3f4c48fe3e064e0b42928 and modified
# License: Boost per code comments in extlibs/nowide
Provides:       bundled(boost-nowide) = 1.73.0.beta1
# Imported in 1304e98e513501ce36029b5fed6b3f5394321884 and modified
# License: Public Domain per code comments in extlibs/gameswf
# Reviewed in https://gitlab.com/fedora/legal/fedora-license-data/-/issues/236
Provides:       bundled(gameswf) = 20090808
# Imported in f98100438410fd6dec2ceed47a94011f76a69227 and modified
# License: MIT per extlibs/squirrel/COPYRIGHT
Provides:       bundled(squirrel-libs) = 3.0.4
# Imported in 1380e913da103a01c53f318b7c3a698dd2b85f3d and modified
# License: zlib per code comments in extlibs/sqrat
Provides:       bundled(sqrat) = 0.8.92
# Imported SFML's audio components in b74be8244b3e9af5c1e552369ee26fd7659a84d6
# and modified; the system SFML is used for the other components
# License: zlib per code comments in extlibs/audio
Provides:       bundled(SFML) = 2.0

%description
Attract-Mode is a graphical frontend for command line emulators such as MAME,
MESS, and Nestopia. It hides the underlying operating system and is intended
to be controlled with a joystick, gamepad or spin dial, making it ideal for
use in arcade cabinet setups.

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

%description    data
This package contains layouts, plugins and other data files for %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1

# remove unneeded bundled libraries
rm -r extlibs/{expat,nvapi} src/backward.{cpp,hpp}
# use system rapidjson
rm -r extlibs/rapidjson/include/rapidjson
ln -s %{_includedir}/rapidjson extlibs/rapidjson/include/
# bundled miniz is not used when building with system libarchive
rm extlibs/miniz/*
# use system stb_image
ln -sf %{_includedir}/stb_image.h src/

%build
export EXTRA_CXXFLAGS="%{optflags}"
%make_build %{build_flags} STRIP=/bin/true

%install
%make_install %{build_flags}

install -Dpm0644 -t %{buildroot}%{_datadir}/icons/hicolor/512x512/apps util/linux/%{name}.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications util/linux/%{name}.desktop

install -Dpm0644 -t %{buildroot}%{_metainfodir} util/linux/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license License.txt
%doc Readme.md Layouts.md
%{_bindir}/%{srcname}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%files data
%license License.txt
%{_datadir}/%{srcname}

%changelog
%autochangelog
