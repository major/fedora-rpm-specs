%undefine _hardened_build
#I think one of the bundled libraries needs to be static.
#Static libraries are fine as all of the libraries included are bundled.
%undefine _cmake_shared_libs
%define _gcc_lto_cflags -fno-lto

#See provides(bundled) below for more info:
%global bundled_libs Bochs_disasm cpp-optparse expr FatFs FreeSurround glslang imgui implot mbedtls rangeset soundtouch tinygltf
#My best guess is that bochs is 2.6.6, as dolphin does not specify
%global bochs_version 2.6.6
%global FatFs_version 0.14b
%global imgui_version 1.70
%global implot_version 0.16
%global mbedtls_version 2.28.9
%global soundtouch_version 2.3.2
%global tinygltf_version 2.9.5

#JIT is only supported on x86_64 and aarch64:
%ifarch x86_64 aarch64
%global enablejit 1
%endif

Name:           dolphin-emu
Version:        2503a
Release:        %autorelease
Summary:        GameCube / Wii / Triforce Emulator

Url:            https://dolphin-emu.org/
##The project is licensed under GPLv2+ with some notable exceptions
#Externals/glslang is BSD-2-Clause AND BSD-3-Clause AND GPL-3.0+ AND Apache-2.0
#Externals/mbedtls is Apache-2.0
##The following is MIT:
#Source/Core/Common/GL/GLExtensions/*
#Externals/tinygltf/*
#Externals/cpp-optparse/*
#Externals/imgui/*
##The following is Zlib:
#Source/Core/Core/HW/Sram.h
#Source/Core/Core/HW/DSPHLE/UCodes/AESnd.cpp
##The following is BSD-2-Clause:
#Source/Core/Common/GekkoDisassembler.*
##The following is BSD-3-Clause:
#Source/Core/Common/BitField.natvis
#Source/UnitTests/Core/DSP/HermesBinary.cpp
#Source/UnitTests/Core/DSP/HermesText.cpp
#Externals/FreeSurround/*
##Any code in Externals has a license break down in Externals/licenses.md
# Automatically converted from old format: GPLv2+ and BSD and MIT and zlib - review is highly recommended.
License:        GPL-2.0-or-later AND MIT AND BSD-3-Clause AND BSD-2-Clause AND Apache-2.0 AND GPL-3.0-or-later AND Zlib
Source0:        https://github.com/%{name}/dolphin/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Source4:        https://github.com/epezent/implot/archive/refs/tags/v%{implot_version}.tar.gz#/implot-%{implot_version}.tar.gz
Source5:        https://github.com/syoyo/tinygltf/archive/refs/tags/v%{tinygltf_version}.tar.gz#/tinygltf-%{tinygltf_version}.tar.gz

# Update bundled mbedtls:
# https://github.com/dolphin-emu/dolphin/pull/13443
Patch0:         0001-Update-mbedtls-to-2.28.9.patch

###Bundled code ahoy, I've added my best guess for versions and upstream urls
##The following isn't in Fedora yet:
#https://github.com/weisslj/cpp-optparse
Provides:       bundled(cpp-argparse)
Provides:       bundled(expr)
#http://elm-chan.org/fsw/ff/00index_e.html
Provides:       bundled(FatFs) = %{FatFs_version}
Provides:       bundled(FreeSurround)
#https://github.com/ocornut/imgui
Provides:       bundled(imgui) = %{imgui_version}
#https://github.com/AdmiralCurtiss/rangeset
Provides:       bundled(rangeset)
##These are not in fedora, but are easy to keep up to date (see sources):
#https://github.com/epezent/implot
Provides:       bundled(implot) = %{implot_version}
#https://github.com/syoyo/tinygltf
Provides:       bundled(tinygltf) = %{tinygltf_version}
##The hard to unbundle
#soundtouch cannot be unbundled easily, as it requires compile time changes:
Provides:       bundled(soundtouch) = %{soundtouch_version}
#This is hard to unbundle and is already a static only lib anyway:
Provides:       bundled(glslang)
#dolphin uses a very old bochs, which is incompatible with f35+'s bochs.
#We could rework dolphin to use latest, but this requires a lot of work.
#Furthermore, the dolphin gtest test cases that fail with f33/34 bochs
Provides:       bundled(bochs) = %{bochs_version}
# mbedtls has dropped TLS v1.1, which dolphin-emu needs:
# https://github.com/dolphin-emu/dolphin/pull/12246
Provides:       bundled(mbedtls) = %{mbedtls_version}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  cmake
BuildRequires:  cubeb-devel
BuildRequires:  enet-devel >= 1.3.18
BuildRequires:  fmt-devel >= 8
BuildRequires:  gtest-devel
BuildRequires:  hidapi-devel
BuildRequires:  libao-devel
BuildRequires:  libcurl-devel
BuildRequires:  libevdev-devel
BuildRequires:  libpng-devel
BuildRequires:  libspng-devel
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libXi-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libzstd-devel >= 1.4.0
BuildRequires:  lzo-devel
BuildRequires:  lz4-devel >= 1.8
BuildRequires:  mesa-libGL-devel
BuildRequires:  minizip-ng-compat-devel >= 3.0.0
BuildRequires:  miniupnpc-devel
BuildRequires:  openal-soft-devel
BuildRequires:  picojson-static
BuildRequires:  pugixml-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  portaudio-devel
BuildRequires:  SDL2-devel
BuildRequires:  SFML-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools
BuildRequires:  spirv-tools-devel
BuildRequires:  systemd-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  vulkan-headers
BuildRequires:  VulkanMemoryAllocator-devel
BuildRequires:  xxhash-devel
BuildRequires:  zlib-ng-devel
BuildRequires:  xz-devel

BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  hicolor-icon-theme
BuildRequires:  /usr/bin/env

#Only the following architectures are supported:
ExclusiveArch:  x86_64 aarch64

Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}

#Most of below is taken bundled spec file in source#
%description
Dolphin is a Gamecube, Wii and Triforce (the arcade machine based on the
Gamecube) emulator, which supports full HD video with several enhancements such
as compatibility with all PC controllers, turbo speed, networked multi player,
and more.
Most games run perfectly or with minor bugs.

%package nogui
Summary:        Dolphin Emulator without a graphical user interface
Requires:       %{name}-data = %{version}-%{release}

%description nogui
Dolphin Emulator without a graphical user interface.

%package tool
Summary:        Dolphin Emulator CLI utility

%description tool
This package provides "dolphin-tool", which is a CLI-based utility for
functions such as managing disc images.

%package data
Summary:        Dolphin Emulator data files
BuildArch:      noarch

%description data
This package provides the data files for dolphin-emu.

####################################################

%prep
%autosetup -p1 -n dolphin-%{version}

# Extract bundled git submodules:
gzip -dc %{SOURCE4} | tar -C Externals/implot/implot --strip-components=1 -xof -
gzip -dc %{SOURCE5} | tar -C Externals/tinygltf/tinygltf --strip-components=1 -xof -

#Allow building with cmake macro
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

#Use system zlib (upstream doesn't like this for performance reasons):
sed -i 's/add_subdirectory(\(.*zlib\)/dolphin_find_optional_system_library_pkgconfig(ZLIB zlib-ng ZLIB::ZLIB \1/' CMakeLists.txt
sed -i 's/ZLIB::ZLIB/ZLIB::ZLIB z/' Source/Core/*/CMakeLists.txt

#Font license, drop the install directory into thie file
echo "%{_datadir}/%{name}/Sys/GC:" > font-licenses.txt
cat Data/Sys/GC/font-licenses.txt >> font-licenses.txt

###Remove Bundled:
cd Externals
#Keep what we need...
for d in *; do
    if ! echo " %{bundled_libs} " | grep " $d "; then
        rm -rf "$d"
    fi
done
#Copy in system picojson
mkdir picojson
#In master, picojson has build option "PICOJSON_NOEXCEPT", but for now:
sed "s/throw std::.*;/std::abort();/g" /usr/include/picojson.h > \
    picojson/picojson.h


%build
#Script to find xxhash is not implemented, just tell cmake it was found
#Note some items are disabled to avoid bundling
#Set USE_SYSTEM_LIBS to safe guard against bundling, but it's not fool proof
%cmake \
       -DUSE_SYSTEM_LIBS=ON \
       -DXXHASH_FOUND=ON \
       -DUSE_MGBA=OFF \
       -DUSE_SYSTEM_MBEDTLS=OFF \
       %{?!enablejit:-DENABLE_GENERIC=ON} \
       -DENABLE_ANALYTICS=OFF \
       -DENCODE_FRAMEDUMPS=OFF \
       -DUSE_DISCORD_PRESENCE=OFF \
       -DUSE_RETRO_ACHIEVEMENTS=OFF
%cmake_build

%install
%cmake_install

#Install udev rules
mkdir -p %{buildroot}%{_udevrulesdir}
install -m 0644 Data/51-usb-device.rules %{buildroot}%{_udevrulesdir}/51-dolphin-usb-device.rules

#Create shell wrapper; dolphin doesn't work on wayland yet, but the QT GUI
#tries to use it. For now, force xwayland. Also fixes bodhi test warning
mv %{buildroot}/%{_bindir}/%{name} %{buildroot}/%{_bindir}/%{name}-x11
echo -e '#!/usr/bin/bash\nQT_QPA_PLATFORM=xcb %{name}-x11 "$@"' \
  > %{buildroot}/%{_bindir}/%{name}
#Remove workaround in desktop:
sed -i "s/^Exec=.*/Exec=dolphin-emu/g" \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop
#Symlink manpage
ln -s %{name}.6 %{buildroot}/%{_mandir}/man6/%{name}-x11.6

#Install appdata.xml
install -p -D -m 0644 %{SOURCE1} \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
%find_lang %{name}

%check
%cmake_build --target unittests
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%doc Readme.md
%license Data/license.txt
%attr(755, root, root) %{_bindir}/%{name}
%{_bindir}/%{name}-x11
%{_mandir}/man6/%{name}.*
%{_mandir}/man6/%{name}-x11.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/sys/Resources/
%{_datadir}/%{name}/sys/Themes/
%{_datadir}/appdata/*.appdata.xml

%files nogui
%doc Readme.md
%license Data/license.txt
%{_bindir}/%{name}-nogui
%{_mandir}/man6/%{name}-nogui.*

%files data
%doc Readme.md docs/gc-font-tool.cpp
%license Data/license.txt font-licenses.txt
#For the gui package:
%exclude %{_datadir}/%{name}/sys/Resources/
%exclude %{_datadir}/%{name}/sys/Themes/
#Already packaged:
%exclude %{_datadir}/%{name}/sys/GC/font-licenses.txt
%{_datadir}/%{name}
%{_udevrulesdir}/51-dolphin-usb-device.rules

%files tool
%doc Readme.md
%license Data/license.txt
%{_bindir}/dolphin-tool

%changelog
%autochangelog
