%undefine _hardened_build
#I think one of the bundled libraries needs to be static.
#Static libraries are fine as all of the libraries included are bundled.
%undefine _cmake_shared_libs
%define _gcc_lto_cflags -fno-lto

#See provides(bundled) below for more info:
%global bundled_libs Bochs_disasm cpp-optparse expr FatFs FreeSurround glslang gtest imgui implot rangeset soundtouch VulkanMemoryAllocator zlib-ng

#Dolphin uses gitsnapshots for its versions.
#See upstream release notes for this snapshot:
#https://dolphin-emu.org/download/dev/$commit
%global commit 423c7c58cd8fe78eb89a3ab434cfbc958a4eef07
%global snapnumber 19793
#We should try to use beta whenever possible
%global branch development

#JIT is only supported on x86_64 and aarch64:
%ifarch x86_64 aarch64
%global enablejit 1
%endif

Name:           dolphin-emu
Version:        5.0.%{snapnumber}
Release:        1%{?dist}
Summary:        GameCube / Wii / Triforce Emulator

Url:            https://dolphin-emu.org/
##The project is licensed under GPLv2+ with some notable exceptions
#Source/Core/Common/GL/GLExtensions/* is MIT
#Source/Core/Core/HW/Sram.h is zlib
#Source/Core/Common/GekkoDisassembler.* is BSD (2 clause)
##The following is BSD (3 clause):
#dolphin-5.0/Source/Core/Common/SDCardUtil.cpp
#dolphin-5.0/Source/Core/Common/BitField.h
#dolphin-5.0/Source/Core/Core/IPC_HLE/l2cap.h
#dolphin-5.0/Source/Core/Core/IPC_HLE/hci.h
#dolphin-5.0/Source/Core/VideoBackends/Software/Clipper.cpp
#dolphin-5.0/Source/Core/AudioCommon/aldlist.cpp
##Any code in Externals has a license break down in Externals/licenses.md
License:        GPLv2+ and BSD and MIT and zlib
Source0:        https://github.com/%{name}/dolphin/archive/%{commit}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
Source2:        https://github.com/google/googletest/archive/refs/tags/release-1.12.1.tar.gz#/gtest-1.12.1.tar.gz
Source3:        https://github.com/zlib-ng/zlib-ng/archive/refs/tags/2.1.3.tar.gz#/zlib-ng-2.1.3.tar.gz
Source4:        https://github.com/epezent/implot/archive/refs/tags/v0.14.tar.gz#/implot-0.14.tar.gz
Source5:        https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/refs/tags/v3.0.1.tar.gz#/VulkanMemoryAllocator-3.0.1.tar.gz

###Bundled code ahoy, I've added versions and upstream urls when known
##The following isn't in Fedora yet:
Provides:       bundled(cpp-argparse)
Provides:       bundled(expr)
Provides:       bundled(FatFs) = 0.14b
Provides:       bundled(FreeSurround)
Provides:       bundled(imgui) = 1.70
#https://github.com/epezent/implot
Provides:       bundled(implot) = 0.14
#https://github.com/AdmiralCurtiss/rangeset
Provides:       bundled(rangeset)
#https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator
Provides:       bundled(VulkanMemoryAllocator) = 3.0.1
##The hard to unbundle
#soundtouch cannot be unbundled easily, as it requires compile time changes:
Provides:       bundled(soundtouch) = 2.3.2
#This is hard to unbundle and is already a static only lib anyway:
Provides:       bundled(glslang)
#dolphin uses a very old bochs, which is incompatible with f35+'s bochs.
#We could rework dolphin to use latest, but this requires a lot of work.
#Furthermore, the dolphin gtest test cases that fail with f33/34 bochs
#My best guess is that this is 2.6.6, as dolphin does not specify
Provides:       bundled(bochs) = 2.6.6
##TODO unbundle me, shouldn't be too hard, but not trivial:
Provides:       bundled(gtest) = 1.12.1
Provides:       bundled(zlib-ng) = 2.1.3

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  cmake
BuildRequires:  cubeb-devel
BuildRequires:  enet-devel
BuildRequires:  fmt-devel >= 6.0.0
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
BuildRequires:  libzstd-devel
BuildRequires:  lzo-devel
BuildRequires:  mbedtls-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  minizip-ng-devel
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
%autosetup -p1 -n dolphin-%{commit}

# Extract bundled submodules:
gzip -dc %{SOURCE2} | tar -C Externals/gtest --strip-components=1 -xof -
gzip -dc %{SOURCE3} | tar -C Externals/zlib-ng/zlib-ng --strip-components=1 -xof -
gzip -dc %{SOURCE4} | tar -C Externals/implot/implot --strip-components=1 -xof -
gzip -dc %{SOURCE5} | tar -C Externals/VulkanMemoryAllocator --strip-components=1 -xof -

#Allow building with cmake macro
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

#Font license, drop the install directory into thie file
echo "%{_datadir}/%{name}/Sys/GC:" > font-licenses.txt
cat Data/Sys/GC/font-licenses.txt >> font-licenses.txt

#Fix for minizip install path
sed -i 's|<unzip.h>|<minizip/unzip.h>|' \
    Source/Core/*/*.h \
    Source/Core/*/*.cpp \
    Source/Core/*/*/*.cpp

#Fix for newer vulkan
sed -i "s/VK_PRESENT_MODE_RANGE_SIZE_KHR/(VkPresentModeKHR)("`
    `"VK_PRESENT_MODE_FIFO_RELAXED_KHR - VK_PRESENT_MODE_IMMEDIATE_KHR + 1)/" \
    Source/Core/VideoBackends/Vulkan/VKSwapChain.h

###Remove Bundled:
cd Externals
#Keep what we need...
for d in *; do
    if ! echo " %{bundled_libs} " | grep " $d "; then
        rm -rf "$d"
    fi
done
#Fix newer gcc issue
sed -i '/#include <cstdint>/a #include <cstdio>' \
	VulkanMemoryAllocator/include/vk_mem_alloc.h
#Copy in system picojson
mkdir picojson
#In master, picojson has build option "PICOJSON_NOEXCEPT", but for now:
sed "s/throw std::.*;/std::abort();/g" %{_includedir}/picojson.h > \
	picojson/picojson.h


%build
#Script to find xxhash is not implemented, just tell cmake it was found
#Note some items are disabled to avoid bundling
#Set USE_SYSTEM_LIBS to safe guard against bundling, but it's not fool proof
%cmake \
       -DUSE_SYSTEM_LIBS=ON \
       -DXXHASH_FOUND=ON \
       -DUSE_MGBA=OFF \
       %{?!enablejit:-DENABLE_GENERIC=ON} \
       -DENABLE_ANALYTICS=OFF \
       -DENCODE_FRAMEDUMPS=OFF \
       -DUSE_DISCORD_PRESENCE=OFF \
       -DUSE_RETRO_ACHIEVEMENTS=OFF \
       -DDOLPHIN_WC_DESCRIBE=5.0-%{snapnumber} \
       -DDOLPHIN_WC_REVISION=%{commit} \
       -DDOLPHIN_WC_BRANCH=%{branch}
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
* Tue Jul 11 2023 Jeremy Newton <alexjnewt AT hotmail DOT com> - 5.0.19793-1
- Update to 5.0-19793

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.16380-9
- Rebuilt due to fmt 10 update.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.16380-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Sandro Mani <manisandro@gmail.com> - 5.0.16380-7
- Rebuild (minizip-ng)

* Thu Nov 10 2022 Jeremy Newton <alexjnewt AT hotmail DOT com> - 5.0.16380-6
- Build against static cubeb

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.16380-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.16380-4
- Backport upstream fix for supporting fmt-9

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.16380-3
- Rebuild (qt5)

* Sat May 21 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.16380-2
- Rebuild (qt5)

* Tue May 17 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.16380-1
- Update to 5.0-16380
- Update bundled soundtouch to 2.3.1

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.15993-3
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.15993-2
- Rebuild (qt5)

* Thu Feb 17 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.15993-1
- Update to 5.0-15993

* Wed Jan 26 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.15920-1
- Update to 5.0-15920 to fix FTBFS on Fedora 35+ (fmt 8.1)
- Add new dolphin tool package
- Move minizip patch to using sed in prep

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.15445-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.15445-1
- Update to 5.0-15445

* Sat Oct 02 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.15105-1
- Update to 5.0-15105

* Wed Aug 04 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.14790-1
- Update to 5.0-14790

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.14344-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Richard Shaw <hobbes1069@gmail.com> - 5.0.14344-2
- Rebuild for new fmt version.

* Mon Jun 07 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.14344-1
- Update to 5.0-14344

* Tue Apr 06 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.13963-1
- Update to 5.0-113963

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 5.0.13603-3
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Feb 16 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.13603-2
- Add ppc64le build support (dolphin should work on any 64bit LE cpu)

* Mon Feb 15 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.13603-1
- Update to 5.0-13603
- Rebundle glslang, it seems I was originally right, but only for 5.0-13178+

* Fri Feb 05 2021 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.12716-5
- Unbundle glslang, it seems I had the wrong impression, reverting this change

* Thu Feb 04 2021 Jeremy Newton <alexjnewt at hotmail dot com>
- Bundle glslang, this is too difficult to keep unbundled with little benefit

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.12716-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 17 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.12716-3
- Disable LTO explicitly, this causes segfaults (RHBZ#1897376)

* Wed Nov 11 2020 Jeff Law <law@redhat.com> - 5.0.12716-2
- Fix missing #includes for gcc-11

* Mon Oct 05 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.12716-1
- Update to latest beta version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.12247-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.12247-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.12247-1
- Update to latest beta version

* Tue May 05 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11991-1
- Update to latest beta version

* Wed Apr 29 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11824-1
- Unbundle cubeb
- Update to latest beta version

* Mon Apr 13 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11819-5
- Forgot shebang in wrapper
- Symlink manpage for dolphin-emu-x11

* Mon Apr 13 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11819-4
- Fix permissions of wrapper script

* Mon Apr 13 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11819-3
- Add wrapper script for xwayland, fixes RH#1823234

* Sun Apr 05 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11819-2
- Update bundled soundtouch to 2.1.2

* Fri Mar 27 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11819-1
- Update to 5.0-11819

* Wed Mar 25 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11817-1
- Update to 5.0-11817

* Wed Mar 18 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11782-1
- Update to 5.0-11782

* Wed Mar 18 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11713-3
- Unbundle glslang

* Thu Mar 12 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11713-2
- Unbundle picojson

* Wed Mar 11 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.11713-1
- Update to 5.0-11713

* Wed Mar 11 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.10474-1
- Update to 5.0-10474

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Kalev Lember <klember@redhat.com> - 5.0-27
- Rebuilt for miniupnpc soname bump

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Morten Stevens <mstevens@fedoraproject.org> - 5.0-25
- Rebuilt for mbed TLS 2.13.0

* Mon Aug 20 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-24
- Fix for soundtouch 2.0.0-5 onwards

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Robert Scheck <robert@fedoraproject.org> - 5.0-22
- Rebuilt for mbed TLS 2.9.0 (libmbedcrypto.so.2)

* Wed Mar 07 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-21
- Unbundle xxhash

* Mon Feb 19 2018 Robert Scheck <robert@fedoraproject.org> - 5.0-20
- Rebuilt for mbed TLS 2.7.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0-18
- Remove obsolete scriptlets

* Sun Oct 15 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-17
- Rebuild with gtk2, since it's been merged into wxGTK3
- Cleanup unnecessary walyand script due to gtk2, closer to upstream now

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 8 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-14
- Rework and rebuild for bochs 2.6.9

* Sun May 7 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-13
- Fix launcher script issues

* Wed Feb 15 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-12
- Rebuilt SFML 2.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 4 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-10
- Add launch scripts for seemless xwayland support
- Revert workaround in desktop file
- Use check macro
- Enable LTO

* Tue Jan 3 2017 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-9
- Workaround for wayland (force x11 for GUI)

* Thu Dec 22 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-8
- Appdata fixes

* Fri Dec 9 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-7
- Add appdata

* Tue Dec 6 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-6
- License fixes with added breakdown
- Split out common data into data subpackage

* Mon Dec 5 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-5
- Revert patch for curl 7.50
- Spec cleanup and fixes
- Add a patch for f26+

* Mon Jul 25 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-4
- Patch for curl 7.50

* Mon Jul 25 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-3
- Added systemd-devel as build require
- Rebuild for miniupnpc-2.0

* Thu Jul 7 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-2
- Added patch for building with mbedtls 2.3+

* Fri Jun 24 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-1
- Update to 5.0

* Thu Mar 24 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-0.2rc
- Update manpages to upstream
- Disable hardened build (breaks dolphin)

* Thu Mar 3 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0-0.1rc
- Update to 5.0rc
- Updated manpage

* Thu Nov 12 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-10
- Patch for mbedtls updated for 2.0+ (f23+)

* Thu Nov 12 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-9
- Patch for X11 for f22+
- Patch for mbedtls (used to be polarssl, fixes check)
- Changed the source download link (migrated to github)

* Mon Jul 20 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-8
- Disabling polarssl check, as its not working on buildsys

* Sun Jun 14 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-7
- Patching for the rename of polarssl

* Tue Dec 9 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-6
- Patching for GCC 4.9

* Sat Dec 6 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-5
- Line got deleted by accident, build fails

* Mon Oct 27 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-4
- Change in wxGTK3-devel file
- Remove unnecessary CG requirement

* Thu Oct 2 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-3
- Use polarssl 1.3 (fedora 21+) to avoid bundling
- patch to use entropy functionality in SSL instead of havege

* Thu Oct 2 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-2
- Bundle polarssl (temporary fix, only for F19/20)

* Mon Mar 3 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 4.0-1
- Update to dolphin 4.0.2
- Removed any unnecessary patches
- Added new and updated some old patches
- Removed exclusive arch, now builds on arm

* Wed Jan 1 2014 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-6
- Build for SDL2 (Adds vibration support)

* Mon Nov 18 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-5
- Added patch for SFML, thanks to Hans de Goede

* Sat Jul 27 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-4
- Updated for SFML compat

* Fri Jul 26 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-3
- GCC 4.8 Fix (Fedora 19 and onwards)

* Tue Feb 19 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-2
- Fixed date typos in SPEC

* Tue Feb 19 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.5-1
- Updated to latest stable: removed GCC patch, updated CLRun patch
- Added patch to build on wxwidgets 2.8 (temporary workaround)

* Sat Feb 16 2013 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-12
- Removed patch for libav and disabled ffmpeg, caused rendering issues
- Minor consistency fixes to SPEC file

* Fri Dec 14 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-11
- Added patch for recent libav api change in fc18, credit to Xiao-Long Chen
- Renamed patch 1 for consistency

* Mon Jun 25 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-10
- Changed CLRun buildrequire package name
- Renamed GCC 4.7 patch to suit fedora standards
- Added missing hicolor-icon-theme require

* Sat Jun 02 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 3.0-9
- Add patch to fix build with gcc 4.7.0 in fc17

* Thu Apr 5 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-8
- Removed bundled CLRun

* Tue Mar 13 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-7
- Removed bundled bochs
- Fixed get-source-from-git.sh: missing checkout 3.0

* Fri Feb 24 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-6
- Removed purposeless zerolength file
Lots of clean up and additions, thanks to Xiao-Long Chen:
- Added man page
- Added script to grab source
- Added copyright file
- Added ExclusiveArch
- Added Some missing dependencies

* Thu Feb 23 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-5
- Fixed Licensing
- Split sources and fixed source grab commands

* Fri Jan 27 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-4
- Tweaked to now be able to encode frame dumps

* Sun Jan 22 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-3
- Building now uses cmake macro
- Turned off building shared libs
- Removed unnecessary lines
- Fixed debuginfo-without-sources issue
- Reorganization of the SPEC for readability

* Thu Jan 12 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-2
- Fixed up spec to Fedora Guidelines
- Fixed various trivial mistakes
- Added SOIL and SFML to dependancies
- Removed bundled SOIL and SFML from source spin

* Sun Dec 18 2011 Jeremy Newton <alexjnewt at hotmail dot com> - 3.0-1
- Initial package SPEC created
