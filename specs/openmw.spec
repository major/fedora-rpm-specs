# Upstream gitlab
%global         forgeurl0 https://gitlab.com/OpenMW/openmw
# Bullet3 Physics Library -- needs double precision!
%global         forgeurl1 https://github.com/bulletphysics/bullet3/
# OpenSceneGraph OpenMW fork with optimizations
%global         forgeurl2 https://github.com/OpenMW/osg/
# RecastNavigation
%global         forgeurl3 https://github.com/recastnavigation/recastnavigation/

# Supported architectures: x86_64, x86, ARMArch64, MIPS
# x86 does not currently build https://gitlab.com/OpenMW/openmw/-/issues/8625
# Even if it did, we don't want to package another 32 bit package
# Fedora does not build MIPS packages anymore
# Therefore, we're only going to package x86_64 and ARM64
ExclusiveArch: %{x86_64} %{arm64}

Name:           openmw
Version:        0.49.0
Release:        %autorelease
Summary:        OpenMW is an open-source game engine

# Stable release source code
%global         tag0 %{name}-%{version}
# Latest bullet3 release tag
%global         tag1 3.25
# Latest OSG OpenMW fork commit tag
%global         commit2 43faf6fa88bd236e0911a5340bfbcbc25b3a98d9
# Preferred commit by upstream for recastnavigation
%global         commit3 c393777d26d2ff6519ac23612abf8af42678c9dd
%forgemeta -a

# Licenses for openmw and bundled libraries
# First line: openmw
# Second line: bullet3
# Third line: OpenSceneGraph
# Fourth line: miscellanious extern code, see below
# Fifth line: bundled fonts
License:        %{shrink:
                GPL-3.0-only AND 
                (Zlib AND MIT AND BSD-3-clause AND BSL-1.0 AND NTP) AND
                (GPL-2.0-only AND LGPL-2.0-or-later WITH WxWindows-exception-3.1) AND 
                MIT AND 
                OFL-1.1-RFN}
URL:            https://openmw.org/
Source0:        %{forgesource0}
Source1:        %{forgesource1}
Source2:        %{forgesource2}
Source3:        %{forgesource3}
# Fixes a unit test that can fail due to a static initialization order fiasco
# Merged upstream for future release https://gitlab.com/OpenMW/openmw/-/merge_requests/4807
Patch0:         4807.patch
# openmw-cs currently runs under wayland, but there's bugs that make it basically unusable
# this patches the default desktop file to add QT_QPA_PLATFORM=xcb
Patch1:         csxcb.patch
# Fixes build with Qt 6.10
# https://gitlab.com/OpenMW/openmw/-/merge_requests/4941
Patch2:         4941.patch

# OpenMW Build Dependencies
BuildRequires:  boost-devel
BuildRequires:  boost-filesystem
BuildRequires:  boost-iostreams
BuildRequires:  boost-program-options
BuildRequires:  boost-system
BuildRequires:  boost-thread
BuildRequires:  cmake
BuildRequires:  cmake(SDL2)
BuildRequires:  collada-dom-devel
BuildRequires:  dejavu-lgc-sans-mono-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg-free-devel
BuildRequires:  gcc
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  libXt-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libstdc++-devel
BuildRequires:  lua-devel
BuildRequires:  luajit-devel
BuildRequires:  lz4-devel
BuildRequires:  mygui-devel
BuildRequires:  ninja-build
BuildRequires:  openal-soft-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt-x11
BuildRequires:  sqlite-devel
BuildRequires:  tinyxml-devel
BuildRequires:  unshield-devel
BuildRequires:  yaml-cpp-devel

# Bullet3 Build Dependencies
BuildRequires:  freeglut-devel
BuildRequires:  libICE-devel
BuildRequires:  libglvnd-devel
BuildRequires:  tinyxml2-devel

# OSG Build Dependencies
BuildRequires:  asio-devel
BuildRequires:  fltk-devel
BuildRequires:  giflib-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblas-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libvncserver-devel
BuildRequires:  libxml2-devel
BuildRequires:  openal-soft-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gta)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkglext-x11-1.0)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.35
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(xrandr)

# We symlink the system version of this font into the game's data directory
Requires:       dejavu-lgc-sans-mono-fonts

# Below is an explanation of why we are statically linking libraries
# Statically linking bullet because we need double precision
# Fedora provided bullet is currently float precision
Provides:       bundled(bullet) = 3.25
# Statically linking OpenMW's fork of OSG as it has game-specific optimizations
Provides:       bundled(OpenSceneGraph-OpenMW) = 3.6
# Recastnavigation is currently not packaged. Godot also uses it and statically links it
# Recastnavigation is more or less dead and upstream prefers a specific commit due to regressions
# TODO: Package recastnavigation? Static linking will still be preferable due to upstream preference
Provides:       bundled(recastnavigation) = 1.6

# Below is an explanation of the code in the extern/ folder. 
# The OSG related ones are covered with OSG's license and Provides.
# sol3, solconfig, smhasher, oics and base64 are all MIT licensed
# smhasher is a library for hashes. One hash algorithm is here (https://github.com/rurban/smhasher)
# sol3 is a modified sol3 (https://github.com/ThePhD/sol2)
# Base64 is from here https://gist.github.com/tomykaira/f0fd86b6c73063283afe550bc5d77594
# oics is OGRE's input system modified for SDL2 https://sourceforge.net/projects/oics/
# Since only sol3 is included in full, only sol3 is listed as a Provides bundle, but
# the others are mentioned here in the comments for documentation purposes
Provides:       bundled(sol3)

# There are two fonts we do not package that are provided by OpenMW. These are fonts specific to OpenMW.
Provides:       bundled(fonts(MysticCards))
Provides:       bundled(fonts(DemonicLetters))

%description
OpenMW is an open-source game engine focused on 3D role-playing games

%package        cs
Summary:        The OpenMW Construction Set
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    cs
OpenMW-CS is a construction kit for making games in the OpenMW engine

%package        tools
Summary:        Utility programs for OpenMW.
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
Various utility tools for developing and debugging with OpenMW

%prep
# Unpack the main source archive and the secondary sources
# into separate directories in %%{_builddir}.
# Then, switch into the unpacked Source0 directory.
%setup -q %{forgesetupargs0} -b1 -b2 -b3
%autopatch -p1

%conf
# Prepare the cmake
# topdir<number> is set for each source by %%forgemeta.
%cmake -G Ninja \
    -DBUILD_OPENMW_TESTS:BOOL=ON \
    -DBULLET_STATIC:BOOL=ON \
    -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON \
    -DFETCHCONTENT_SOURCE_DIR_BULLET:PATH=%{_builddir}/%{topdir1} \
    -DFETCHCONTENT_SOURCE_DIR_OSG:PATH:PATH=%{_builddir}/%{topdir2} \
    -DFETCHCONTENT_SOURCE_DIR_RECASTNAVIGATION:PATH=%{_builddir}/%{topdir3} \
    -DGLOBAL_DATA_PATH:PATH=%{_datadir} \
    -DOPENMW_USE_SYSTEM_BULLET:BOOL=OFF \
    -DOPENMW_USE_SYSTEM_GOOGLETEST:BOOL=ON \
    -DOPENMW_USE_SYSTEM_OSG:BOOL=OFF \
    -DOSG_STATIC:BOOL=ON

%build
# Now, we build OpenMW.
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_datadir}/openmw/resources/vfs/fonts/DejaVuLGCSansMono.ttf
# Symlink system dejavu font
ln -sr %{buildroot}%{_datadir}/fonts/dejavu-lgc-sans-mono-fonts/DejaVuLGCSansMono.ttf %{buildroot}%{_datadir}/openmw/resources/vfs/fonts/DejaVuLGCSansMono.ttf

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.openmw.launcher.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.openmw.cs.desktop
# OpenMW's provided unit tests
./%{_vpath_builddir}/openmw-tests

%files
%license LICENSE
%doc README.md
%doc AUTHORS.md
%doc CHANGELOG.md
%dir %{_sysconfdir}/openmw
%dir %{_datadir}/openmw
%dir %{_datadir}/openmw/resources
%dir %{_datadir}/openmw/resources/vfs
%dir %{_datadir}/openmw/resources/vfs/fonts
%{_bindir}/openmw
%{_bindir}/openmw-launcher
%{_bindir}/openmw-bulletobjecttool
%{_bindir}/openmw-iniimporter
%{_bindir}/openmw-essimporter
%{_bindir}/openmw-navmeshtool
%{_bindir}/openmw-wizard
%{_datadir}/pixmaps/openmw.png
%{_datadir}/applications/org.openmw.launcher.desktop
%{_datadir}/openmw/resources/openmw.png
%{_datadir}/openmw/resources/defaultfilters
%{_datadir}/openmw/resources/version
%{_datadir}/openmw/resources/lua_api
%{_datadir}/openmw/resources/lua_libs
%{_datadir}/openmw/resources/shaders
%{_datadir}/openmw/resources/translations
%{_datadir}/openmw/resources/vfs-mw
%{_datadir}/openmw/resources/vfs/builtin.omwscripts
%{_datadir}/openmw/resources/vfs/animations
%{_datadir}/openmw/resources/vfs/l10n
%{_datadir}/openmw/resources/vfs/mygui
%{_datadir}/openmw/resources/vfs/openmw_aux
%{_datadir}/openmw/resources/vfs/scripts
%{_datadir}/openmw/resources/vfs/shaders
%{_datadir}/openmw/resources/vfs/textures
%{_datadir}/openmw/resources/vfs/fonts/DejaVuLGCSansMono.ttf
%{_datadir}/openmw/resources/vfs/fonts/DejaVuFontLicense.txt
%{_datadir}/openmw/resources/vfs/fonts/DejaVuLGCSansMono.omwfont
%{_datadir}/openmw/resources/vfs/fonts/DemonicLettersFontLicense.txt
%{_datadir}/openmw/resources/vfs/fonts/DemonicLetters.omwfont
%{_datadir}/openmw/resources/vfs/fonts/DemonicLetters.ttf
%{_datadir}/openmw/resources/vfs/fonts/MysticCardsFontLicense.txt
%{_datadir}/openmw/resources/vfs/fonts/MysticCards.omwfont
%{_datadir}/openmw/resources/vfs/fonts/MysticCards.ttf
%{_datadir}/metainfo/openmw.appdata.xml
%{_sysconfdir}/openmw/defaults.bin
%{_sysconfdir}/openmw/defaults-cs.bin
%{_sysconfdir}/openmw/gamecontrollerdb.txt
%{_sysconfdir}/openmw/openmw.cfg

%files cs
%{_bindir}/openmw-cs
%{_datadir}/applications/org.openmw.cs.desktop
%{_datadir}/pixmaps/openmw-cs.png

%files tools
%{_bindir}/bsatool
%{_bindir}/esmtool
%{_bindir}/niftest

%changelog
%autochangelog
