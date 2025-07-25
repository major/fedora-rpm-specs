%ifarch %{power64} s390x riscv64
# LuaJIT is not available for POWER and IBM Z
%bcond lua_scripting 0
%else
%bcond lua_scripting 1
%endif

%ifarch x86_64
# VPL/QSV is only available on x86_64
%bcond vpl 1
%else
%bcond vpl 0
%endif

# x264 is not in Fedora
%bcond x264 0

%if ! (0%{?fedora} >= 42)
# CEF is only available in F42+
%bcond cef 0
%else
%ifarch %{x86_64} %{arm64}
# CEF is only available on x86_64 and aarch64
%bcond cef 1
%else
%bcond cef 0
%endif
%endif

%if "%{__isa_bits}" == "64"
%global lib64_suffix ()(64bit)
%endif
%global libvlc_soversion 5


%global obswebsocket_version 5.6.2
%global obsbrowser_commit bdabf8300ecefeb566b81f4a7ff75f8a8e21f62b

# Upstream does not declare this yet. Arbitrarily pick 137.0 since it works
# and it works around a CEF versioning teething issue:
# https://github.com/chromiumembedded/cef/issues/3959
%global cef_api_version 13700

#global commit ad859a3f66daac0d30eebcc9b07b0c2004fb6040
#global snapdate 202303261743
#global shortcommit %%(c=%%{commit}; echo ${c:0:7})

Name:           obs-studio
Version:        31.1.1
Release:        2%{?dist}
Summary:        Open Broadcaster Software Studio

# OBS itself is GPL-2.0-or-later, while various plugin dependencies are of various other licenses
# The licenses for those dependencies are captured with the bundled provides statements
License:        GPL-2.0-or-later and MIT and BSD-2-Clause and BSD-3-Clause and BSL-1.0 and LGPL-2.1-or-later and CC0-1.0 and (CC0-1.0 or OpenSSL or Apache-2.0) and LicenseRef-Fedora-Public-Domain and (BSD-3-Clause or GPL-2.0-only)
URL:            https://obsproject.com/
%if 0%{?snapdate}
Source0:        https://github.com/obsproject/obs-studio/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:        https://github.com/obsproject/obs-studio/archive/%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz
%endif
Source1:        https://github.com/obsproject/obs-websocket/archive/%{obswebsocket_version}/obs-websocket-%{obswebsocket_version}.tar.gz
Source2:        https://github.com/obsproject/obs-browser/archive/%{obsbrowser_commit}/obs-browser-%{obsbrowser_commit}.tar.gz

# Backports from upstream

# Proposed upstream
## From: https://github.com/obsproject/obs-studio/pull/12326
Patch0101:      0101-frontend-Consider-settings-changed-if-an-output-sett.patch
Patch0102:      0102-frontend-Allow-invalid-recording-encoder-if-quality-.patch
## From: https://github.com/obsproject/obs-studio/pull/8529
Patch0103:      0103-UI-Add-support-for-OpenH264-as-the-worst-case-fallba.patch

# Downstream Fedora patches
## Use fdk-aac by default
Patch1001:      obs-studio-UI-use-fdk-aac-by-default.patch
## Fix error: passing argument 4 of ‘query_dmabuf_modifiers’ from
##            incompatible pointer type [-Wincompatible-pointer-types]
Patch1003:      obs-studio-fix-incompatible-pointer-type.patch

BuildRequires:  gcc
BuildRequires:  cmake >= 3.22
BuildRequires:  ninja-build
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

BuildRequires:  alsa-lib-devel
BuildRequires:  asio-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdk-aac-free-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  jansson-devel >= 2.5
BuildRequires:  json-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdatachannel-devel >= 0.20
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
BuildRequires:  nv-codec-headers
%if %{with vpl}
BuildRequires:  libvpl-devel
%endif
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
BuildRequires:  rnnoise-devel
BuildRequires:  speexdsp-devel
BuildRequires:  swig
BuildRequires:  systemd-devel
BuildRequires:  uthash-devel
BuildRequires:  wayland-devel
BuildRequires:  websocketpp-devel
%if %{with x264}
BuildRequires:  x264-devel
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# Ensure that we have the full ffmpeg suite installed
Requires:       /usr/bin/ffmpeg
# Try to ensure openh264 is installed
## Note, we can do this because openh264 is provided in a default-enabled
## third party repository provided by Cisco.
Recommends:     openh264%{?_isa}

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

%if ! %{with cef}
# When the plugin is not available, obsolete it
Obsoletes:     %{name}-plugin-browser < %{version}-%{release}
%endif

%description
Open Broadcaster Software is free and open source
software for video recording and live streaming.

%files
%doc README.rst
%license frontend/data/license/gplv2.txt
%license COPYING
%{_bindir}/obs
%{_bindir}/obs-ffmpeg-mux
%ifarch %{x86_64}
%{_bindir}/obs-nvenc-test
%endif
%{_datadir}/metainfo/com.obsproject.Studio.metainfo.xml
%{_datadir}/applications/com.obsproject.Studio.desktop
%{_datadir}/icons/hicolor/*/apps/com.obsproject.Studio.*
%{_datadir}/obs/
%exclude %{_datadir}/obs/obs-plugins/vlc-video/
%if %{with cef}
%exclude %{_datadir}/obs/obs-plugins/obs-browser*
%endif

# --------------------------------------------------------------------------

%package libs
Summary: Open Broadcaster Software Studio libraries

%description libs
Library files for Open Broadcaster Software

%files libs
%license COPYING
%license .fedora-rpm/licenses/*
%dir %{_libexecdir}/obs-plugins
%{_libdir}/obs-plugins/
%if %{with cef}
%exclude %{_libdir}/obs-plugins/obs-browser*
%endif
%exclude %{_libdir}/obs-plugins/vlc-video.so
%{_libdir}/obs-scripting/
# unversioned so files packaged for third-party plugins (cf. rfbz#5999)
%{_libdir}/*.so
%{_libdir}/*.so.*

# --------------------------------------------------------------------------

%package devel
Summary: Open Broadcaster Software Studio header files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Header files for Open Broadcaster Software

%files devel
%{_libdir}/cmake/libobs/
%{_libdir}/cmake/obs-frontend-api/
%{_libdir}/cmake/obs-websocket-api/
%{_libdir}/pkgconfig/libobs.pc
%{_libdir}/pkgconfig/obs-frontend-api.pc
%{_includedir}/obs/

# --------------------------------------------------------------------------

%if %{with cef}
%package plugin-browser
Summary:        Open Broadcaster Software Studio - CEF-based browser plugin
BuildRequires:  cef-devel

# Filter out bogus libcef.so requires as this is handled manually
# with an explicit dependency
%global __requires_exclude ^libcef\\.so.*$

# Require the correct CEF API support
%{?_cef_api_requires:%_cef_api_requires %{cef_api_version}}
Requires:       obs-studio%{?_isa} = %{version}-%{release}
Supplements:    obs-studio%{?_isa}

%description plugin-browser
Open Broadcaster Software is free and open source software
for video recording and live streaming.

This package contains the plugin for integrated web-based overlays in
a video stream or recording using the Chromium Embedded Framework (CEF).

%files plugin-browser
%{_libdir}/obs-plugins/obs-browser*
%{_datadir}/obs/obs-plugins/obs-browser*
%endif

# --------------------------------------------------------------------------

%package plugin-vlc-video
Summary:        Open Broadcaster Software Studio - VLC-based video plugin
BuildRequires:  vlc-devel
# We dlopen() libvlc
Requires:       libvlc.so.%{libvlc_soversion}%{?lib64_suffix}
Requires:       obs-studio%{?_isa} = %{version}-%{release}
Supplements:    obs-studio%{?_isa}

%description plugin-vlc-video
Open Broadcaster Software is free and open source software
for video recording and live streaming.

This package contains the plugin for using VLC to embed video
as an overlay in a video stream or recording.

%files plugin-vlc-video
%{_libdir}/obs-plugins/vlc-video.so
%{_datadir}/obs/obs-plugins/vlc-video/

# --------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{?snapdate:%{commit}}%{!?snapdate:%{version_no_tilde}}
# Prepare plugins/obs-websocket
tar -xf %{SOURCE1} -C plugins/obs-websocket --strip-components=1
tar -xf %{SOURCE2} -C plugins/obs-browser --strip-components=1
%autopatch -p1

# This is provided by cef-devel systemwide
rm cmake/finders/FindCEF.cmake

# Fix obs-browser rpath setting
sed -e 's,INSTALL_RPATH ".*",INSTALL_RPATH "%{_libdir}/cef/",' -i plugins/obs-browser/cmake/os-linux.cmake

%if ! %{with x264}
# disable x264 plugin
mv plugins/obs-x264/CMakeLists.txt plugins/obs-x264/CMakeLists.txt.disabled
touch plugins/obs-x264/CMakeLists.txt
%endif

%if ! %{with vpl}
# disable unusable qsv plugin
mv plugins/obs-qsv11/CMakeLists.txt plugins/obs-qsv11/CMakeLists.txt.disabled
touch plugins/obs-qsv11/CMakeLists.txt
%endif

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
cp deps/blake2/LICENSE.blake2 .fedora-rpm/licenses/deps/
cp libobs/graphics/libnsgif/LICENSE.libnsgif .fedora-rpm/licenses/deps/
cp libobs/util/simde/LICENSE.simde .fedora-rpm/licenses/deps/
cp plugins/decklink/LICENSE.decklink-sdk .fedora-rpm/licenses/deps
cp plugins/obs-qsv11/obs-qsv11-LICENSE.txt .fedora-rpm/licenses/plugins/


%build
# libcef_wrapper needs to be built static
%undefine _cmake_shared_libs
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DOBS_VERSION_OVERRIDE=%{version_no_tilde} \
       -DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
       -DUNIX_STRUCTURE=1 -GNinja \
%if ! %{with cef}
       -DENABLE_BROWSER=OFF \
%else
       -DENABLE_BROWSER=ON \
       -DCEF_API_VERSION=%{cef_api_version} \
%endif
       -DENABLE_JACK=ON \
       -DENABLE_LIBFDK=ON \
       -DENABLE_AJA=OFF \
%if ! %{with lua_scripting}
       -DENABLE_SCRIPTING_LUA=OFF \
%endif
       -DOpenGL_GL_PREFERENCE=GLVND
%cmake_build


%install
%cmake_install

# Work around broken libobs.pc file...
# Cf. https://github.com/obsproject/obs-studio/issues/7972
sed -e 's|^Cflags: .*|Cflags: -I${includedir} -DHAVE_OBSCONFIG_H|' -i %{buildroot}%{_libdir}/pkgconfig/libobs.pc

# Create libexecdir for obs-plugins
mkdir -p %{buildroot}%{_libexecdir}/obs-plugins

# Delete useless files
find %{buildroot} -name ".keepme" -delete
find %{buildroot} -name ".gitkeep" -delete


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.obsproject.Studio.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 31.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jul 12 2025 Neal Gompa <ngompa@fedoraproject.org> - 31.1.1-1
- Update to 31.1.1

* Tue Jul 08 2025 Neal Gompa <ngompa@fedoraproject.org> - 31.1.0-1
- Update to 31.1.0 final
- Update obs-websocket to 5.6.2
- Update obs-browser to 033a23befe01

* Sun Jul 06 2025 Asahi Lina <lina@asahilina.net> - 31.1.0~rc1-3
- Switch CEF API to 13700 (works around crash)

* Fri Jul 04 2025 Neal Gompa <ngompa@fedoraproject.org> - 31.1.0~rc1-2
- Rebuild for libdatachannel 0.23.1

* Tue Jul 01 2025 Asahi Lina <lina@asahilina.net> - 31.1.0~rc1-1
- Update obs-studio to 31.1.0~rc1
- Rebase patches after upstream rework
- Update obs-websocket to 5.6.1
- Update obs-browser to 9ffe3828da5
- Re-enable CEF support

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 31.0.3-3
- Rebuilt for Python 3.14

* Wed Apr 23 2025 David Abdurachmanov <davidlt@rivosinc.com> - 31.0.3-2
- Disable LuaJIT on riscv64 (not supported)

* Wed Apr 09 2025 Sérgio M. Basto <sergio@serjux.com> - 31.0.3-1
- Update obs-studio to 31.0.3
- Resolves: rhbz#2309473

* Tue Apr 01 2025 Michael J Gruber <mjg@fedoraproject.org> - 31.0.2-6
- fix v4loopback usage

* Fri Mar 28 2025 Jan Grulich <jgrulich@redhat.com> - 31.0.2-5
- Rebuild (qt6)

* Tue Mar 25 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 31.0.2-4
- Rebuild for mbedtls 3.6

* Tue Mar 25 2025 Jan Grulich <jgrulich@redhat.com> - 31.0.2-3
- Rebuild (qt6)

* Wed Mar 19 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 31.0.2-2
- Rebuild for mbedtls 3.6

* Thu Mar 13 2025 Sérgio Basto <sergio@serjux.com> - 31.0.2-1
- Update obs-studio to 31.0.2
- Resolves: rhbz#2338791
- Fix FTBFS
- Resolves: rhbz#2340952
- Update obs-websocket to 5.5.5

* Thu Feb 20 2025 Neal Gompa <ngompa@fedoraproject.org> - 31.0.1-1
- Update to 31.0.1

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 31.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 13 2024 Neal Gompa <ngompa@fedoraproject.org> - 31.0.0-1
- Update to 31.0.0 final

* Sun Nov 24 2024 Neal Gompa <ngompa@fedoraproject.org> - 31.0.0~rc1-1
- Update to 31.0.0~rc1

* Tue Oct 22 2024 Richard W.M. Jones <rjones@redhat.com> - 31.0.0~beta1-4
- Rebuild for Jansson 2.14
  (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/3PYINSQGKQ4BB25NQUI2A2UCGGLAG5ND/)

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 31.0.0~beta1-3
- Rebuild (qt6)

* Sat Oct 05 2024 Neal Gompa <ngompa@fedoraproject.org> - 31.0.0~beta1-2
- Directly recommend the openh264 package

* Sat Oct 05 2024 Neal Gompa <ngompa@fedoraproject.org> - 31.0.0~beta1-1
- Update to 31.0.0~beta1

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 30.2.2-3
- Rebuild for ffmpeg 7

* Tue Sep 03 2024 Morten Stevens <mstevens@fedoraproject.org> - 30.2.2-2
- Rebuilt for mbedTLS 3.6.1

* Wed Jul 31 2024 Neal Gompa <ngompa@fedoraproject.org> - 30.2.2-1
- Update to 30.2.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 30.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 30.1.1-3
- Rebuilt for Python 3.13

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 30.1.1-2
- Rebuild (qt6)

* Tue Apr 02 2024 Neal Gompa <ngompa@fedoraproject.org> - 30.1.1-1
- Update to 30.1.1

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 30.0.0-9
- Rebuild (qt6)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 30.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 30.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 28 2023 Neal Gompa <ngompa@fedoraproject.org> - 30.0.0-6
- Drop broken obsoletes+provides for vlc plugin
- Drop redundant dependency on libvlc in main package

* Fri Dec 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 30.0.0-5
- Enable VLC video plugin
- Split out browser plugin as a subpackage
- Restructure spec and conditionals

* Mon Dec 11 2023 Neal Gompa <ngompa@fedoraproject.org> - 30.0.0-4
- Filter out bogus libcef.so automatic dependency

* Sun Dec 10 2023 Asahi Lina <lina@asahilina.net> - 30.0.0-3
- Add obs-browser support using obs-cef

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 30.0.0-2
- Rebuild (qt6)

* Mon Nov 13 2023 Neal Gompa <ngompa@fedoraproject.org> - 30.0.0-1
- Update to 30.0.0 final

* Thu Nov 02 2023 Neal Gompa <ngompa@fedoraproject.org> - 30.0.0~rc2-1
- Update to 30.0.0~rc2

* Wed Oct 18 2023 Jan Grulich <jgrulich@redhat.com> - 30.0.0~rc1-2
- Rebuild (qt6)

* Fri Oct 13 2023 Neal Gompa <ngompa@fedoraproject.org> - 30.0.0~rc1-1
- Update to 30.0.0~rc1

* Fri Oct 13 2023 Jan Grulich <jgrulich@redhat.com> - 30.0.0~beta3-4
- Rebuild (qt6)

* Thu Oct 05 2023 Jan Grulich <jgrulich@redhat.com> - 30.0.0~beta3-3
- Rebuild (qt6)

* Fri Sep 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 30.0.0~beta3-2
- Add patch to downgrade CMake dependency to >= 3.20
- Rebuild against libdatachannel for fixed soname dependency

* Mon Sep 11 2023 Neal Gompa <ngompa@fedoraproject.org> - 30.0.0~beta3-1
- Rebase to 30.0.0~beta3

* Fri Sep 08 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.3-4
- Add obs-plugins libexecdir to libs subpackage

* Mon Jul 24 2023 Jan Grulich <jgrulich@redhat.com> - 29.1.3-3
- Rebuild (qt6)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 29.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.3-1
- Update to 29.1.3

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 29.1.2-4
- Rebuild for qtbase private API version change

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 29.1.2-3
- Rebuild for qtbase private API version change

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 29.1.2-2
- Rebuilt for Python 3.12

* Tue May 30 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.2-1
- Update to 29.1.2

* Tue May 30 2023 Jan Grulich <jgrulich@redhat.com> - 29.1.1-2
- Rebuild (qt6)

* Tue May 23 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.1-1
- Update to 29.1.1

* Fri May 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0-3
- Rebuild for Qt 6.5.0

* Thu May 04 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0-2
- Add patch to use FDK-AAC by default

* Tue May 02 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0-1
- Update to 29.1.0 final

* Wed Apr 26 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~rc1-1
- Update to 29.1.0~rc1

* Mon Apr 24 2023 Neal Gompa <ngompa@fedoraproject.org> - 29.1.0~beta4-3
- Switch ffmpeg-free dependency to /usr/bin/ffmpeg

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
