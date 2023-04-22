%ifarch %{power64} s390x
# LuaJIT is not available for POWER and IBM Z
%bcond_with lua_scripting
%else
%bcond_without lua_scripting
%endif

# VLC is not yet in Fedora
%bcond_with vlc
# x264 is not in Fedora
%bcond_with x264

%if "%{__isa_bits}" == "64"
%global lib64_suffix ()(64bit)
%endif
%global openh264_soversion 7


%global obswebsocket_version 5.2.2

#global commit ad859a3f66daac0d30eebcc9b07b0c2004fb6040
#global snapdate 202303261743
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           obs-studio
Version:        29.1.0~beta4
Release:        2%{?dist}
Summary:        Open Broadcaster Software Studio

# OBS itself is GPL-2.0-or-later, while various plugin dependencies are of various other licenses
# The licenses for those dependencies are captured with the bundled provides statements
License:        GPL-2.0-or-later and ISC and MIT and BSD-1-Clause and BSD-2-Clause and BSD-3-Clause and BSL-1.0 and LGPL-2.1-or-later and CC0-1.0 and (CC0-1.0 or OpenSSL or Apache-2.0) and LicenseRef-Fedora-Public-Domain and (BSD-3-Clause or GPL-2.0-only)
URL:            https://obsproject.com/
%if 0%{?snapdate}
Source0:        https://github.com/obsproject/obs-studio/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:        https://github.com/obsproject/obs-studio/archive/%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz
%endif
Source1:        https://github.com/obsproject/obs-websocket/archive/%{obswebsocket_version}/obs-websocket-%{obswebsocket_version}.tar.gz

# Backports from upstream

# Proposed upstream
## From: https://github.com/obsproject/obs-studio/pull/8529
Patch0101:      0001-UI-Consistently-reference-the-software-H264-encoder-.patch
Patch0102:      0002-obs-ffmpeg-Add-initial-support-for-the-OpenH264-H.26.patch
Patch0103:      0003-UI-Add-support-for-OpenH264-as-the-worst-case-fallba.patch
## From: https://github.com/obsproject/obs-studio/pull/8763
Patch0104:      obs-studio-PR8763.patch


# Downstream Fedora patches
## Use system qrcodegencpp
Patch1001:      obs-studio-websocket-use-system-qrcodegencpp.patch
## Add license declarations for bundled deps
Patch9001:      obs-studio-deps-Add-license-declaration-files.patch
## Add license declaration for obs-qsv11
Patch9002:      obs-studio-obs-qsv11-Add-license-declaration-file.patch


BuildRequires:  gcc
BuildRequires:  cmake >= 3.16
BuildRequires:  ninja-build
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

BuildRequires:  alsa-lib-devel
BuildRequires:  asio-devel
BuildRequires:  fdk-aac-free-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  jansson-devel >= 2.5
BuildRequires:  json-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdrm-devel
BuildRequires:  libGL-devel
BuildRequires:  libglvnd-devel
BuildRequires:  librist-devel
BuildRequires:  srt-devel
BuildRequires:  libuuid-devel
BuildRequires:  libv4l-devel
BuildRequires:  libva-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libxkbcommon-devel
%if %{with lua_scripting}
BuildRequires:  luajit-devel
%endif
BuildRequires:  mbedtls-devel
BuildRequires:  pciutils-devel
BuildRequires:  pipewire-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-devel
BuildRequires:  libqrcodegencpp-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  speexdsp-devel
BuildRequires:  swig
BuildRequires:  systemd-devel
%if %{with vlc}
BuildRequires:  vlc-devel
%endif
BuildRequires:  wayland-devel
BuildRequires:  websocketpp-devel
%if %{with x264}
BuildRequires:  x264-devel
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# Ensure that we have the full ffmpeg suite installed
Requires:       ffmpeg-free
# We dlopen() openh264, so weak-depend on it...
## Note, we can do this because openh264 is provided in a default-enabled
## third party repository provided by Cisco.
Recommends:     libopenh264.so.%{openh264_soversion}%{?lib64_suffix}
%if %{with x264}
Requires:       x264
%endif

# Ensure QtWayland is installed when libwayland-client is installed
Requires:      (qt6-qtwayland%{?_isa} if libwayland-client%{?_isa})
# For icon folder heirarchy
Requires:      hicolor-icon-theme

# These are modified sources that can't be easily unbundled
## License: MIT and CC0-1.0
## Newer version in Fedora with the same licensing
## Request filed upstream for fixing it: https://github.com/simd-everywhere/simde/issues/999
Provides:      bundled(simde) = 0.7.1
## License: BSL-1.0
Provides:      bundled(decklink-sdk)
## License: CC0-1.0 or OpenSSL or Apache-2.0
Provides:      bundled(blake2)
## License: MIT
Provides:      bundled(json11)
## License: MIT
Provides:      bundled(libcaption)
## License: ISC
Provides:      bundled(libff)
## License: BSD-1-Clause
Provides:      bundled(uthash)
## License: BSD-3-Clause
Provides:      bundled(rnnoise)
## License: LGPL-2.1-or-later and LicenseRef-Fedora-Public-Domain
Provides:      bundled(librtmp)
## License: MIT
Provides:      bundled(libnsgif)
## License: MIT
## Windows only dependency
## Support for Linux will also unbundle it
## Cf. https://github.com/obsproject/obs-studio/pull/8327
Provides:      bundled(intel-mediasdk)


%description
Open Broadcaster Software is free and open source
software for video recording and live streaming.

%package libs
Summary: Open Broadcaster Software Studio libraries
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description libs
Library files for Open Broadcaster Software

%package devel
Summary: Open Broadcaster Software Studio header files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Header files for Open Broadcaster Software


%prep
%setup -q -n %{name}-%{?snapdate:%{commit}}%{!?snapdate:%{version_no_tilde}}
# Prepare plugins/obs-websocket
tar -xf %{SOURCE1} -C plugins/obs-websocket --strip-components=1
%autopatch -p1

# rpmlint reports E: hardcoded-library-path
# replace OBS_MULTIARCH_SUFFIX by LIB_SUFFIX
sed -e 's|OBS_MULTIARCH_SUFFIX|LIB_SUFFIX|g' -i cmake/Modules/ObsHelpers.cmake

# Kill rpath settings
sed -e '\|set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/${OBS_LIBRARY_DESTINATION}")|d' -i cmake/Modules/ObsHelpers_Linux.cmake

# touch the missing submodules
touch plugins/obs-browser/CMakeLists.txt

%if ! %{with x264}
# disable x264 plugin
mv plugins/obs-x264/CMakeLists.txt plugins/obs-x264/CMakeLists.txt.disabled
touch plugins/obs-x264/CMakeLists.txt
%endif

# remove -Werror flag to mitigate FTBFS with ffmpeg 5.1
sed -e 's|-Werror-implicit-function-declaration||g' -i cmake/Modules/CompilerConfig.cmake
sed -e '/-Werror/d' -i cmake/Modules/CompilerConfig.cmake

# Removing unused third-party deps
rm -rf deps/w32-pthreads
rm -rf deps/ipc-util
rm -rf deps/jansson

# Remove unneeded EGL/KHR files
rm -rf deps/glad/include/{EGL,KHR}
sed -e 's|include/EGL/eglplatform.h||g' -i deps/glad/CMakeLists.txt

# Collect license files
mkdir -p .fedora-rpm/licenses/deps
mkdir -p .fedora-rpm/licenses/plugins
cp plugins/obs-filters/rnnoise/COPYING .fedora-rpm/licenses/deps/rnnoise-COPYING
cp plugins/obs-websocket/LICENSE .fedora-rpm/licenses/plugins/obs-websocket-LICENSE
cp plugins/obs-outputs/librtmp/COPYING .fedora-rpm/licenses/deps/librtmp-COPYING
cp deps/json11/LICENSE.txt .fedora-rpm/licenses/deps/json11-LICENSE.txt
cp deps/libcaption/LICENSE.txt .fedora-rpm/licenses/deps/libcaption-LICENSE.txt
cp plugins/obs-qsv11/QSV11-License-Clarification-Email.txt .fedora-rpm/licenses/plugins/QSV11-License-Clarification-Email.txt
cp deps/uthash/uthash/LICENSE .fedora-rpm/licenses/deps/uthash-LICENSE
cp deps/blake2/LICENSE.blake2 .fedora-rpm/licenses/deps/
cp deps/libff/LICENSE.libff .fedora-rpm/licenses/deps/
cp libobs/graphics/libnsgif/LICENSE.libnsgif .fedora-rpm/licenses/deps/
cp libobs/util/simde/LICENSE.simde .fedora-rpm/licenses/deps/
cp plugins/decklink/LICENSE.decklink-sdk .fedora-rpm/licenses/deps
cp plugins/obs-qsv11/obs-qsv11-LICENSE.txt .fedora-rpm/licenses/plugins/


%build
%cmake -DOBS_VERSION_OVERRIDE=%{version_no_tilde} \
       -DUNIX_STRUCTURE=1 -GNinja \
       -DCMAKE_SKIP_RPATH=1 \
       -DBUILD_BROWSER=OFF \
%if ! %{with vlc}
       -DENABLE_VLC=OFF \
%endif
       -DENABLE_JACK=ON \
       -DENABLE_LIBFDK=ON \
       -DENABLE_AJA=OFF \
%if ! %{with lua_scripting}
       -DDISABLE_LUA=ON \
%endif
       -DOpenGL_GL_PREFERENCE=GLVND
%cmake_build


%install
%cmake_install

# Add missing files to enable the build of obs-ndi
install -Dm644 UI/obs-frontend-api/obs-frontend-api.h %{buildroot}%{_includedir}/obs/
install -Dm644 cmake/external/ObsPluginHelpers.cmake %{buildroot}%{_libdir}/cmake/libobs/

# Work around broken libobs.pc file...
# Cf. https://github.com/obsproject/obs-studio/issues/7972
sed -e 's|^Cflags: .*|Cflags: -I${includedir} -DHAVE_OBSCONFIG_H|' -i %{buildroot}%{_libdir}/pkgconfig/libobs.pc

# Delete useless files
find %{buildroot} -name ".keepme" -delete
find %{buildroot} -name ".gitkeep" -delete


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.obsproject.Studio.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%doc README.rst
%license UI/data/license/gplv2.txt
%license COPYING
%{_bindir}/obs
%{_bindir}/obs-ffmpeg-mux
%{_datadir}/metainfo/com.obsproject.Studio.appdata.xml
%{_datadir}/applications/com.obsproject.Studio.desktop
%{_datadir}/icons/hicolor/*/apps/com.obsproject.Studio.*
%{_datadir}/obs/

%files libs
%license COPYING
%license .fedora-rpm/licenses/*
%{_libdir}/obs-plugins/
%{_libdir}/obs-scripting/
# unversioned so files packaged for third-party plugins (cf. rfbz#5999)
%{_libdir}/*.so
%{_libdir}/*.so.*

%files devel
%{_libdir}/cmake/libobs/
%{_libdir}/cmake/obs-frontend-api/
%{_libdir}/pkgconfig/libobs.pc
%{_includedir}/obs/


%changelog
* Thu Apr 20 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta4-2
- Ensure ffmpeg-free and OpenH264 are expressed as dependencies

* Tue Apr 18 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta4-1
- Initial build for Fedora

* Tue Apr 18 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta4-0.5
- Capture more licenses

* Sun Apr 16 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta4-0.4
- Backport fix for RHEL 9 builds

* Sun Apr 16 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta4-0.3
- Add license declaration files for bundled deps

* Sun Apr 16 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta4-0.2
- Ensure system EGL headers are used

* Sat Apr 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta4-0.1
- Update to 29.1.0~beta4

* Wed Apr 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta3-0.1
- Update to 29.1.0~beta3

* Wed Apr 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta2-0.1
- Update to 29.1.0~beta2

* Sun Apr 02 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta1-0.2
- Get rid of RPATHs
- Backport upstream fix to fix EPEL 9 build
- Drop old cruft

* Wed Mar 29 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta1-0.1
- Upgrade to v29.1.0~beta1

* Wed Mar 29 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~git202303261743.ad859a3-0.4
- Refresh patches for OpenH264 support

* Tue Mar 28 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~git202303261743.ad859a3-0.3
- Refresh patches for OpenH264 support

* Tue Mar 28 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~git202303261743.ad859a3-0.2
- Refresh patches for OpenH264 support

* Mon Mar 27 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~git202303261743.ad859a3-0.1
- Update to git snapshot

* Sun Mar 26 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~git202303260813.94bf325-0.1
- Update to git snapshot
- Add patches for OpenH264 support

* Sat Feb 18 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.0.2-0.1
- Update to 29.0.2
- Drop patch about encoder references to x264

* Sat Jan 07 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.0.0-0.1
- Update to v29.0.0 final
- Add patch for adjusting encoder reference for x264

* Mon Jan 02 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.0.0~beta3-4
- Ensure QtWayland is installed when libwayland-client is installed

* Sun Jan 01 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.0.0~beta3-3
- Make ffmpeg dependency agnostic to packaging

* Wed Dec 28 2022 Neal Gompa <ngompa@fedoraproject.org> - 29.0.0~beta3-2
- Work around broken libobs.pc file

* Tue Dec 27 2022 Neal Gompa <ngompa@fedoraproject.org> - 29.0.0~beta3-1
- Rebase to v29.0.0~beta3
- Enable vst plugin
- Enable websocket plugin
- Disable x264 plugin

* Thu Nov 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 28.1.2-2
- Rebuilt due to Qt update.

* Sun Nov 06 2022 Leigh Scott <leigh123linux@gmail.com> - 28.1.2-1
- Update to 28.1.2

* Thu Nov 03 2022 Leigh Scott <leigh123linux@gmail.com> - 28.1.1-1
- Update to 28.1.1

* Tue Nov 01 2022 Leigh Scott <leigh123linux@gmail.com> - 28.1.0-1
- Update to 28.1.0

* Mon Oct 03 2022 Leigh Scott <leigh123linux@gmail.com> - 28.0.3-1
- Update to 28.0.3

* Mon Sep 26 2022 Leigh Scott <leigh123linux@gmail.com> - 28.0.2-1
- Update to 28.0.2
- Enable jack (rfbz#6419)

* Tue Sep 13 2022 Leigh Scott <leigh123linux@gmail.com> - 28.0.1-4
- Use qt6 for rawhide only

* Tue Sep 13 2022 Leigh Scott <leigh123linux@gmail.com> - 28.0.1-3
- Fix wrong svg names

* Tue Sep 13 2022 Leigh Scott <leigh123linux@gmail.com> - 28.0.1-2
- touch the missing sub-modules instead

* Tue Sep 13 2022 Leigh Scott <leigh123linux@gmail.com> - 28.0.1-1
- Update to 28.0.1
- Remove vst sub-module as it's qt5 only
- Add browser and websocket sub-modules so the source compiles
  Upstream can fix their own mess!

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 27.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Sat Jul 23 2022 Leigh Scott <leigh123linux@gmail.com> - 27.2.4-4
- Rebuild for new qt5

* Sat Jun 25 2022 Robert-André Mauchin <zebob.m@gmail.com> - 27.2.4-3
- Rebuilt for Python 3.11

* Sun Jun 12 2022 Sérgio Basto <sergio@serjux.com> - 27.2.4-2
- Mass rebuild for x264-0.164

* Mon Apr 11 2022 Leigh Scott <leigh123linux@gmail.com> - 27.2.4-1
- Update to 27.2.4

* Thu Mar 31 2022 Leigh Scott <leigh123linux@gmail.com> - 27.2.1-2
- Rebuild for new qt

* Sat Feb 26 2022 Neal Gompa <ngompa@fedoraproject.org> - 27.2.1-1
- Update to 27.2.1
- Disable Lua scripting for POWER to fix ppc64le build
- Drop legacy Fedora and EL8 stuff

* Mon Feb 14 2022 Neal Gompa <ngompa@fedoraproject.org> - 27.2.0-1
- Update to 27.2.0 final

* Tue Feb 08 2022 Neal Gompa <ngompa@fedoraproject.org> - 27.2.0~rc4-1
- Update to 27.2.0~rc4

* Mon Feb 07 2022 Leigh Scott <leigh123linux@gmail.com> - 27.2.0~rc1-1
- Update to 27.2.0~rc1

* Wed Dec 01 2021 Nicolas Chauvet <kwizart@gmail.com> - 27.1.3-2
- Rebuilt

* Tue Oct 05 2021 Neal Gompa <ngompa@fedoraproject.org> - 27.1.3-1
- Update to 27.1.3

* Tue Sep 28 2021 Neal Gompa <ngompa@fedoraproject.org> - 27.1.1-1
- Bump to 27.1.1 final

* Sat Sep 18 2021 Neal Gompa <ngompa@fedoraproject.org> - 27.1.0~rc3-2
- Backport fix for PipeWire screencasting on F35+

* Sat Sep 18 2021 Neal Gompa <ngompa@fedoraproject.org> - 27.1.0~rc3-1
- Update to 27.1.0~rc3

* Sat Sep 11 2021 Neal Gompa <ngompa@fedoraproject.org> - 27.1.0~rc2-1
- Update to 27.1.0~rc2

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 27.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Sérgio Basto <sergio@serjux.com> - 27.0.1-3
- Mass rebuild for x264-0.163

* Sat Jun 26 2021 Neal Gompa <ngompa13@gmail.com> - 27.0.1-2
- Backport fix for cursor positioning in Wayland screencasting

* Sat Jun 12 2021 Neal Gompa <ngompa13@gmail.com> - 27.0.1-1
- Update to 27.0.1

* Tue Jun 01 2021 Neal Gompa <ngompa13@gmail.com> - 27.0.0-1
- Bump to 27.0.0 final
- Move unversioned so files to -libs for third-party plugins (rfbz#5999)
- Make build for EL8
- Drop legacy EL7 stuff

* Mon May 24 2021 Neal Gompa <ngompa13@gmail.com> - 27.0.0~rc6-1
- Bump to 27.0.0~rc6

* Thu May 20 2021 Neal Gompa <ngompa13@gmail.com> - 27.0.0~rc5-1
- Bump to 27.0.0~rc5
- Drop upstreamed patch for building jack plugin

* Wed May 05 2021 Neal Gompa <ngompa13@gmail.com> - 27.0.0~rc3-2
- Fix detecting pipewire-libjack so jack plugin is built

* Wed May 05 2021 Neal Gompa <ngompa13@gmail.com> - 27.0.0~rc3-1
- Bump to 27.0.0~rc3

* Thu Apr 22 2021 Leigh Scott <leigh123linux@gmail.com> - 27.0.0~rc2-2
- Rebuild for libftl issue (rfbz5978)

* Sat Apr 17 2021 Neal Gompa <ngompa13@gmail.com> - 27.0.0~rc2-1
- Bump to 27.0.0~rc2

* Wed Feb 10 2021 Nicolas Chauvet <kwizart@gmail.com> - 26.1.2-3
- Add obs-vst plugins
- Build for all arches (armv7hl, aarch64, ppc64le)
- Re-order build dependencies

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 26.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Martin Gansser <martinkg@fedoraproject.org> - 26.1.2-1
- Update to 26.1.2

* Tue Jan 19 2021 Martin Gansser <martinkg@fedoraproject.org> - 26.1.1-1
- Update to 26.1.1

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 26.1.0-2
- Rebuilt for new ffmpeg snapshot

* Sat Dec 26 2020 Momcilo Medic <fedorauser@fedoraproject.org> - 26.1.0-1
- Updated to 26.1.0

* Fri Nov 27 2020 Sérgio Basto <sergio@serjux.com> - 26.0.2-3
- Mass rebuild for x264-0.161

* Wed Oct 14 2020 Momcilo Medic <fedorauser@fedoraproject.org> - 26.0.2-2
- Bumped release for setting developer toolset version

* Wed Oct 14 2020 Momcilo Medic <fedorauser@fedoraproject.org> - 26.0.2-1
- Removed doxygen bits as upstream removed it
- Updated to 26.0.2

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 25.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Aug 06 2020 Leigh Scott <leigh123linux@gmail.com> - 25.0.8-4
- Improve compatibility with new CMake macro

* Tue Jul 07 2020 Sérgio Basto <sergio@serjux.com> - 25.0.8-3
- Mass rebuild for x264

* Sat May 30 2020 Leigh Scott <leigh123linux@gmail.com> - 25.0.8-2
- Rebuild for python-3.9

* Tue Apr 28 2020 Leigh Scott <leigh123linux@googlemail.com> - 25.0.8-1
- Updated to 25.0.8

* Thu Apr 16 2020 Leigh Scott <leigh123linux@gmail.com> - 25.0.6-1
- Updated to 25.0.6

* Mon Apr 06 2020 Momcilo Medic <fedorauser@fedoraproject.org> - 25.0.4-1
- Updated to 25.0.4

* Tue Mar 31 2020 Momcilo Medic <fedorauser@fedoraproject.org> - 25.0.3-1
- Updated to 25.0.3

* Fri Mar 20 2020 Martin Gansser <martinkg@fedoraproject.org> - 25.0.1-1
- Update to 25.0.1

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 24.0.6-2
- Rebuild for ffmpeg-4.3 git

* Fri Feb 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 24.0.6-1
- Update to 24.0.6

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 24.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 24.0.5-1
- Updated to 24.0.5

* Tue Dec 17 2019 Leigh Scott <leigh123linux@gmail.com> - 24.0.3-3
- Mass rebuild for x264

* Sun Oct 13 2019 Momcilo Medic <fedorauser@fedoraproject.org> - 24.0.3-2
- Switched BR gcc-objc to gcc to unify SPEC file across builds

* Sat Oct 12 2019 Momcilo Medic <fedorauser@fedoraproject.org> - 24.0.3-1
- Updated to 24.0.3

* Sun Sep 22 2019 Momcilo Medic <fedorauser@fedoraproject.org> - 24.0.1-1
- Updated to 24.0.1

* Sat Aug 24 2019 Leigh Scott <leigh123linux@gmail.com> - 23.2.1-3
- Rebuild for python-3.8

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 23.2.1-2
- Rebuild for new ffmpeg version

* Tue Jun 18 2019 Momcilo Medic <fedorauser@fedoraproject.org> - 23.2.1-1
- Updated to 23.2.1

* Mon Apr 08 2019 Momcilo Medic <fedorauser@fedoraproject.org> - 23.1.0-1
- Updated to 23.1.0

* Sun Apr 07 2019 Martin Gansser <martinkg@fedoraproject.org> - 23.0.2-4
- Add obs-frontend-api.h to devel subpkg, to enable build of obs-ndi
- Add ObsPluginHelpers.cmake to devel subpkg, to enable build of obs-ndi

* Mon Mar 18 2019 Xavier Bachelot <xavier@bachelot.org> - 23.0.2-3
- Fix BR: on speex/speexdsp for EL7.
- Fix BR: on python for EL7.

* Tue Mar 12 2019 Sérgio Basto <sergio@serjux.com> - 23.0.2-2
- Mass rebuild for x264

* Sun Mar 10 2019 Momcilo Medic <fedorauser@fedoraproject.org> - 23.0.2-1
- Updated to 23.0.2

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 23.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Feb 25 2019 Momcilo Medic <fedorauser@fedoraproject.org> - 23.0.0-1
- Updated to 23.0.0

* Wed Jan 9 2019 Momcilo Medic <fedorauser@fedoraproject.org> - 22.0.3-3
- Fixed missing dependencies
- Enabled scripting support

* Thu Oct 04 2018 Sérgio Basto <sergio@serjux.com> - 22.0.3-2
- Mass rebuild for x264 and/or x265

* Fri Sep 7 2018 Momcilo Medic <fedorauser@fedoraproject.org> - 22.0.3-1
- Updated to 22.0.3

* Wed Aug 22 2018 Momcilo Medic <fedorauser@fedoraproject.org> - 22.0.1-1
- Updated to 22.0.1

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 21.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Miro Hrončok <mhroncok@redhat.com> - 21.1.2-2
- Rebuilt for Python 3.7

* Wed May 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 21.1.2-1
- Update to 21.1.2
- Fix requires

* Sat Mar 31 2018 Leigh Scott <leigh123linux@googlemail.com> - 21.1.1-1
- Update to 21.1.1

* Mon Mar 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 21.1.0-1
- Update to 21.1.0

* Fri Mar 09 2018 Martin Gansser <martinkg@fedoraproject.org> - 21.0.3-1
- Update to 21.0.3
- Add BR python3-devel
- Add bytecompile with Python 3 %%global __python %%{__python3}A

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 21.0.2-4
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 21.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 08 2018 Leigh Scott <leigh123linux@googlemail.com> - 21.0.2-2
- Fix scriptlets
- Use ninja to build

* Wed Feb 07 2018 Momcilo Medic <fedorauser@fedoraproject.org> - 21.0.2-1
- Updated to 21.0.2

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 20.1.3-3
- Rebuilt for ffmpeg-3.5 git

* Sun Dec 31 2017 Sérgio Basto <sergio@serjux.com> - 20.1.3-2
- Mass rebuild for x264 and x265

* Fri Dec 08 2017 Leigh Scott <leigh123linux@googlemail.com> - 20.1.3-1
- Updated to 20.1.3

* Tue Oct 17 2017 Martin Gansser <martinkg@fedoraproject.org> - 20.0.1-1
- Updated to 20.0.1

* Thu Aug 10 2017 Momcilo Medic <fedorauser@fedoraproject.org> - 20.0.0-1
- Updated to 20.0.0

* Sat Jul 08 2017 Martin Gansser <martinkg@fedoraproject.org> - 19.0.3-1
- Updated to 19.0.3

* Mon May 22 2017 Momcilo Medic <fedorauser@fedoraproject.org> - 19.0.2-1
- Updated to 19.0.2

* Wed May 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 18.0.2-2
- Rebuild for ffmpeg update

* Sat May 6 2017 Momcilo Medic <fedorauser@fedoraproject.org> - 18.0.2-1
- Updated to 18.0.2

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 18.0.1-3
- Rebuild for ffmpeg update

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 18.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 8 2017 Momcilo Medic <fedorauser@fedoraproject.org> - 18.0.1-1
- Updated to 18.0.1

* Wed Mar 1 2017 Momcilo Medic <fedorauser@fedoraproject.org> - 18.0.0-1
- Updated to 18.0.0

* Mon Jan 30 2017 Momcilo Medic <fedorauser@fedoraproject.org> - 17.0.2-2
- Reintroduced obs-ffmpeg-mux.patch
- Fixes #4436

* Wed Jan 18 2017 Momcilo Medic <fedorauser@fedoraproject.org> - 17.0.2-1
- Updated to 17.0.2

* Tue Jan 03 2017 Momcilo Medic <fedorauser@fedoraproject.org> - 17.0.0-1
- Upstream fixed arch-dependent-file-in-usr-share
- Removed obs-ffmpeg-mux.patch
- Updated to 17.0.0

* Sun Nov 27 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.16.6-1
- Updated to 0.16.6

* Tue Nov 08 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.16.5-1
- Updated to 0.16.5

* Tue Oct 18 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.16.2-2.20161018git4505d5a
- Updated to git to resolve unversioned shared object
- Identified speexdsp-devel as a dependency

* Sat Oct 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.16.2-1
- Updated to 0.16.2
- Build doxygen html documentation
- Added BR doxygen

* Fri Aug 26 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.15.4-3
- Actually define FFMPEG_MUX_FIXED (fixes 'command not found' when trying to record)

* Sat Aug 13 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.15.4-2
- Disable build for ARM (Arm gcc has no xmmintrin.h file)

* Fri Aug 12 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.15.4-1
- Fix release tag (0.x release is for git releases)

* Mon Aug 08 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.15.4-0.1
- Updated to 0.15.4

* Fri Aug 05 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.15.2-0.5
- Added alsa-devel as BR for ALSA plugin.
- Added vlc-devel as BR for VLC plugin.
- Added systemd-devel as BR for Udev V4L.

* Wed Aug 03 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.15.2-0.4
- Fix source tag (spectool now downloads in n-v format)
- Remove surplus ldconfig from postun (no public .so files in main package)
- Update scriptlets to meet guidelines (need full path)

* Wed Jul 20 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.15.2-0.3
- Added license file gplv2.txt

* Mon Jul 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.15.2-0.2
- Fixed arch-dependent-file-in-usr-share
- Added obs-ffmpeg-mux.patch
- Added libs subpkg
- Call ldconfig in post(un) scripts for the shared library

* Sat Jul 16 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.15.2-0.1
- Updated to 0.15.2

* Sun Jul 10 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.15.1-0.1
- Updated to 0.15.1

* Sat Jul 09 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.15.0-0.1
- Updated to 0.15.0

* Mon May 16 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.14.2-0.1
- Updated to 0.14.2

* Mon Apr 25 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.14.1-0.1
- Updated to 0.14.1

* Sun Apr 24 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.14.0-0.1
- Updated to 0.14.0

* Tue Mar 22 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.13.4-0.1
- Updated to 0.13.4

* Sun Mar 20 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.13.3-0.1
- Updated to 0.13.3

* Tue Feb 23 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.13.2-0.1
- Updated to 0.13.2

* Sat Feb 06 2016 Momcilo Medic <fedorauser@fedoraproject.org> - 0.13.1-0.1
- Updated to 0.13.1

* Sun Dec 20 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.12.4-0.2
- replace OBS_MULTIARCH_SUFFIX by LIB_SUFFIX

* Sat Dec 12 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.12.4-0.1
- Updated to 0.12.4

* Sat Dec 05 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.12.3-0.1
- Updated to 0.12.3

* Sat Nov 21 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.12.2-0.1
- Updated to 0.12.2

* Thu Nov 19 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.12.1-0.1
- Updated to 0.12.1

* Thu Sep 24 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.12.0-0.1
- Updated to 0.12.0

* Mon Aug 17 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.11.4-0.1
- Added OBS_VERSION_OVERRIDE to correct version in compilation
- Updated to 0.11.4

* Sat Aug 08 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.11.3-0.1
- Updated to 0.11.3

* Thu Jul 30 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.11.2-0.1
- Updated to 0.11.2

* Fri Jul 10 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.11.1-0.1
- Updated to 0.11.1

* Wed May 27 2015 Momcilo Medic <fedorauser@fedoraproject.org> - 0.10.1-0.1
- Initial .spec file
