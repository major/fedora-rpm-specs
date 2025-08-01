%global commit aa2b4b1c5814cc2f832898a9e4a1bdfc38e7ac8d
%global gittag 1.2.1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           sdrpp
Version:        1.2.1
Release:        3%{?dist}
Summary:        SDRPlusPlus bloat-free SDR receiver software

# Automatically converted from old format: GPLv3 and MIT and WTFPL and Public Domain - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-MIT AND WTFPL AND LicenseRef-Callaway-Public-Domain
URL:            https://github.com/AlexandreRouma/SDRPlusPlus/
Source0:        https://github.com/AlexandreRouma/SDRPlusPlus/archive/%{commit}/%{name}-%{version}.tar.gz
Source1:        org.sdrpp.SDRPlusPlus.metainfo.xml

# Changes to top-level and core CMakeLists.txt to complete the above changes.
# Set soname on libsdrpp_core.so
# Install libsdrpp_core.so in _libdir
Patch1:         cmake-top.patch
# Ensure libraries come from pkgconfig
Patch2:         add-libraries.patch
# Move the config file to libdir
#Patch3:         configfile-libdir.patch
# std::runtime_error requires <stdexcept>
# https://github.com/AlexandreRouma/SDRPlusPlus/issues/970
Patch5:         sdrpp-stdexcept.patch
# Do not use hardcoded paths in desktop file
Patch6:         desktop-file.patch

ExcludeArch:    i686

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  fftw-devel glew-devel volk-devel glfw-devel
BuildRequires:  portaudio-devel libiio-devel rtaudio-devel
BuildRequires:  spdlog-devel fmt-devel
# Need to BR -static packages for header-only libraries for tracking, per
BuildRequires:  rapidjson-devel rapidjson-static
BuildRequires:  json-devel json-static
BuildRequires:  libcorrect-devel
BuildRequires:  libzstd-devel
# Enforce the the minimum EVR to contain fixes for all of:
# CVE-2021-28021
# CVE-2021-42715
# CVE-2021-42716
# CVE-2022-28041
# CVE-2023-43898
# CVE-2023-45661
# CVE-2023-45662
# CVE-2023-45663
# CVE-2023-45664
# CVE-2023-45666
# CVE-2023-45667
BuildRequires:  stb_image-devel >= 2.28^20231011gitbeebb24-12
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize-devel stb_image_resize-static
BuildRequires:  stb_truetype-devel stb_truetype-static
BuildRequires:  SoapySDR-devel hackrf-devel rtl-sdr-devel
BuildRequires:  libcorrect-devel codec2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires: google-roboto-fonts

# Bundled libraries
# https://github.com/AlexandreRouma/SDRPlusPlus/issues/292
# https://github.com/ocornut/imgui
# MIT License
Provides: bundled(imgui) = 1.83
# imgui itself bundles stb_rect_pack and stb_textedit with changes that do not
# match upstream stb so we can't remove it in favor of library code. It is essentially
# a private fork of upstream stb.  stb_truetype matches upstream now, so that was unbundled.
#
# https://github.com/samhocevar/portable-file-dialogs
# WTFPL License
Provides: bundled(portable-file-dialogs) = 0.1.0
#
# https://github.com/discord/discord-rpc
# MIT License
# Note: this library is deprecated by upstream in favor of Discord's GameSDK. Therefore
# this should not be packaged into Fedora separately.
Provides: bundled(discord-rpc) = 3.4.0
# A local copy of libsddc is present in sddc_source but is not built.
# A local copy of libcorrect is present in falcon9_decoder but is not built.
# A local copy of nlohmann-json is present in the source and is deleted prior to building.
# A local copy of stb_image and stb_image_resize is present in the source and is deleted prior to building.
# A local copy of rapidjson is present in the source and is deleted prior to building.
# A local copy of spdlog is present in the source and is deleted prior to building.


%description
SDR++ is a cross-platform and open source SDR software
with the aim of being bloat free and simple to use.

Features
- Wide hardware support (both through SoapySDR and dedicated modules)
- SIMD accelerated DSP
- Full waterfall update when possible. Makes browsing signals
  easier and more pleasant


%prep
%autosetup -p1 -n SDRPlusPlus-%{commit}
# Install plugins to _lib
grep -rl 'lib/sdrpp/plugins' . | xargs sed -i -e 's:lib/sdrpp/plugins:%{_lib}/sdrpp/plugins:g'
# Delete local copy of spdlog. We're using the system library copy.
rm -rf core/src/spdlog
# Remove rapidjson in favor of system library
rm -rf misc_modules/discord_integration/discord-rpc/include/rapidjson
sed -i -e 's:#include "rapidjson/\(.*\)":#include <rapidjson/\1>:' misc_modules/discord_integration/discord-rpc/src/serialization.h
# Replace use of local nlohmann-json with library version
rm core/src/json.hpp
grep -l -r '#include <json.hpp>' . | xargs sed -i -e 's:#include <json.hpp>:#include <nlohmann/json.hpp>:'
# Replace use of local stb_image and stb_image_resize with library version
rm core/src/imgui/stb_image_resize.h
rm core/src/imgui/stb_image.h
sed -i -e 's:#include <imgui/stb_image.h>:#include <stb/stb_image.h>:' core/src/gui/icons.cpp
sed -i -e 's:#include <stb_image.h>:#include <stb/stb_image.h>:' \
    -e 's:#include <stb_image_resize.h>:#include <stb/stb_image_resize.h>:' core/src/core.cpp
# replace use of local stb_truetype with library version
sed -i -e 's:#include "imstb_truetype.h":#include<stb/stb_truetype.h>:' core/src/imgui/imgui_draw.cpp

# remove local libcorrect copy
rm -rf core/libcorrect/

# Use system-provided roboto font
sed -i -e 's:resDir + "/fonts/Roboto-Medium.ttf":"%{_datadir}/fonts/google-roboto/Roboto-Medium.ttf":'   core/src/gui/style.cpp


%build
# For compatibility with CMake 4.0
export CMAKE_POLICY_VERSION_MINIMUM=3.5

# Not building Falcon9 decoder as it requires ffplay which is in rpmfusion
# Not building hardware support which does not have libraries in Fedora
# Building for new PortAudio
%cmake -DOPT_BUILD_AIRSPY_SOURCE=OFF -DOPT_BUILD_AIRSPYHF_SOURCE=OFF \
       -DOPT_BUILD_BLADERF_SOURCE=OFF \
       -DOPT_BUILD_PLUTOSDR_SOURCE=OFF \
       -DOPT_BUILD_NEW_PORTAUDIO_SINK=ON \
       -DOPT_BUILD_M17_DECODER=ON \
	   -DUSE_INTERNAL_LIBCORRECT=OFF \
	   -DOPT_BUILD_SOAPY_SOURCE=ON \
       -DBUILD_SHARED_LIBS=0

%cmake_build


%install
%cmake_install
rm %{buildroot}%{_libdir}/libsdrpp_core.so
rm -rf %{buildroot}%{_datadir}/%{name}/fonts

# Install desktop icon
install -D -p -m644 root/res/icons/sdrpp.png \
  %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

# Install AppStream metainfo file
install -D -p -m644 %{SOURCE1} %{buildroot}%{_metainfodir}/org.sdrpp.SDRPlusPlus.metainfo.xml


%check
# upstream has no tests for ctest except in unbuilt libsddc
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/org.sdrpp.SDRPlusPlus.metainfo.xml


%files
%license license misc_modules/discord_integration/discord-rpc/LICENSE
%doc readme.md contributing.md
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_libdir}/lib%{name}_core.so.%{version}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_bindir}/%{name}
%{_metainfodir}/*


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jun 21 2025 Richard Shaw <hobbes1069@gmail.com> - 1.2.1-2
- Add CMake option to build with SoapySDR.

* Thu Mar 13 2025 Richard Shaw <hobbes1069@gmail.com> - 1.2.1-1
- Update to 1.2.1.

* Mon Mar 10 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2.0-5
- Rebuilt for new volk

* Tue Jan 28 2025 Daniel Rusek <mail@asciiwolf.com> - 1.2.0-4
- Add AppStream metadata
- Install desktop icon in standard location
- Do not use hardcoded paths in desktop file

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 František Zatloukal <fzatlouk@redhat.com> - 1.2.0-2
- Rebuilt for spdlog 1.15.0

* Sun Oct 20 2024 Richard Shaw <hobbes1069@gmail.com> - 1.2.0-1
- Update to 1.2.0.

* Fri Oct 18 2024 Richard Shaw <hobbes1069@gmail.com> - 1.0.4-24
- Rebuild for new rtaudio.

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.4-23
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 František Zatloukal <fzatlouk@redhat.com> - 1.0.4-21
- Rebuilt for spdlog 1.14.1

* Tue Apr 09 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.4-20
- Rebuilt for new rtl-sdr

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.4-18
- Rebuilt for new volk

* Wed Oct 25 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0.4-17
- Ensure stb_image contains the latest CVE patches

* Sat Aug 05 2023 Richard Shaw <hobbes1069@gmail.com> - 1.0.4-16
- Rebuild for codec2.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.4-14
- Rebuilt due to spdlog 1.12 update.

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.4-13
- Rebuilt due to fmt 10 update.

* Sun Feb 26 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0.4-12
- Update min. stb_image version for nullptr deref. bug

* Fri Jan 20 2023 Richard Shaw <hobbes1069@gmail.com> - 1.0.4-11
- Rebuild for volk.

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.4-10
- Rebuilt due to spdlog update.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-8
- Rebuild for fmt-9

* Sat Jul 09 2022 Richard Shaw <hobbes1069@gmail.com> - 1.0.4-7
- Rebuild for codec2 1.0.4.

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 1.0.4-6
- Rebuild for glew 2.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Richard Shaw <hobbes1069@gmail.com> - 1.0.4-4
- Rebuild for codec2 1.0.1.

* Sat Oct 23 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0.4-3
- Rebuild with updated stb_image to patch CVE-2021-28021, CVE-2021-42715, and
  CVE-2021-42716
- Add -static BR’s required by guidelines for tracking of header-only libraries

* Tue Oct 19 2021 Matt Domsch <matt@domsch.com> - 1.0.4-2
- Upstream 1.0.4
- drop patches now included in upstream
- use sed where possible instead of patches to avoid
  build breaking on version upgrades
- Upstream now appends compiler options it wants
- Drop bundled libcorrect
- Enable beta M17 decoder
- Build discourse-rpc as a static library linked into discourse_integration

* Sat Sep 18 2021 Matt Domsch <matt@domsch.com> - 1.0.3-2
- Package updates based on review feedback

* Sun Sep 12 2021 Matt Domsch <matt@domsch.com> - 1.0.3-1
- Initial package per Fedora Packaging Guidelines


