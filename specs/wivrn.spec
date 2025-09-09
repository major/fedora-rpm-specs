# Build features, default off
%bcond_with x264

%global forgeurl0      https://github.com/WiVRn/WiVRn
%global wivrn_version  25.8
%global tag0           v%{wivrn_version}
%global date           20250810

# WiVRn is based on Monado, we need the full source
# Monado base source (find in monado-rev file)
%global forgeurl1      https://gitlab.freedesktop.org/monado/monado
%global commit1        5c137fe28b232fe460f9b03defa7749adc32ee48
%global monado_version 25.0.0

%forgemeta

Name:           wivrn
Version:        %{wivrn_version}
Release:        %autorelease
Summary:        An OpenXR streaming application to a standalone headset

License:        GPL-3.0-or-later AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CECILL-C AND CC0-1.0 AND CC-BY-4.0 AND MIT-Khronos-old AND Unlicense AND Zlib AND GPL-2.0-or-later AND MIT AND OFL-1.1
# CECILL-C
# _deps/monado-src/src/external/imgui/imgui/imconfig.h
# CC0-1.0 AND Apache-2.0
# _deps/monado-src/src/external/glad/*
# Unlicense
# _deps/monado-src/src/external/imgui/imgui/backends/imgui_impl_opengl3_loader.h
# Apache-2.0
# _deps/monado-src/gradle*
# _deps/monado-src/src/external/{flexkalman,glad,mermaid,nvpro_pyramid,openxr_includes}/*
# _deps/monado-src/src/xrt/auxiliary/math/m_quatexpmap.cpp
# gradle*
# resources/values/ic_wivrn_launcher_background.xml
# Apache-2.0 OR MIT
# _deps/monado-src/doc/doxygen-awesome-css/doxygen-awesome-*
# BSD-2-Clause
# _deps/monado-src/cmake/FindEigen3.cmake
# _deps/monado-src/src/external/hungarian/*
# _deps/monado-src/src/external/tracy/{client,common}/*
# _deps/monado-src/cmake/{FindEGL.cmake,FindSystemd.cmake,OptionWithDeps.cmake}
# _deps/monado-src/src/external/openvr_includes/*
# _deps/monado-src/src/external/tinyceres/*
# _deps/monado-src/src/external/tracy/libbacktrace/*
# _deps/monado-src/src/xrt/drivers/north_star/distortion_3d/*
# _deps/monado-src/src/xrt/tracking/hand/mercury/kine_lm/lm_rotations_ceres.inl
# BSD-3-Clause AND BSL-1.0
# _deps/monado-src/src/xrt/targets/steamvr_drv/*
# BSL-1.0
# _deps/monado-src/{CMakeLists.txt,CompilerFlags.cmake,build.gradel}
# _deps/monado-src/cmake/{CleanDirectoryList.cmake,FindHIDAPI.cmake,FindLeapV2.cmake,FindLibcheck.cmake,FindLibusb1.cmake,FindONNXRuntime.cmake,FindOpenGLES.cmake,FindOpenHMD.cmake,FindPercetto.cmake,Findbluetooth.cmake,FindcJSON.cmake,Findudev.cmake,GenerateKhrManifest.cmake,GenerateKhrManifestInternals.cmake.in,GenerateOpenXRRuntimeManifest.cmake,GenerateVulkanApiLayerManifest.cmake,GetGitRevisionDescription.cmake,GetGitRevisionDescription.cmake.in,PrefixListGlob.cmake,ProgramFilesGlob.cmake,SPIR-V.cmake,openxr_manifest.in.json.license}
# _deps/monado-src/src/external/{Catch2,android-jni-wrap,flexkalman,imgui,nvpro_pyramid,openxr_includes,solarxr,util-headers,vit_includes}
# _deps/monado-src/src/xrt/auxiliary/{android,bindings,d3d,gsteamer,math,ogl,os,tracking,util,vive,vk}/*
# _deps/monado-src/src/xrt/compositor/*
# _deps/monado-src/src/xrt/drivers/{android,arduino,daydream,depthai,euroc,hdk,ht,ht_ctrl_emu,hydra,illixr,multi_wrapper,north_star,ohmd,opengloves,psmv,qwerty,realsense,remote,rift_s,rokid,sample,simula,simulated,solarxr,steamvr_lh,survive,twrap,ultraleap_v2,v4l2,vf,vive,wmr,xreal_air}/*
# _deps/monado-src/src/xrt/include/tracking/t_hand_tracking.h
# _deps/monado-src/src/xrt/include/xrt/*
# _deps/monado-src/src/xrt/{ipc,state_trackers,targets,tracking}/*
# _deps/monado-src/tests/*
# server/{main.cpp,start_application.cpp,target_instance_wivrn.cpp}
# BSL-1.0 AND CC0-1.0
# _deps/monado-src/{doc,scripts}/*
# GPL-2.0-or-later
# tools/wireshark/dissector.cpp
# GPL-3.0-or-later
# {client,common,dashboard,server}/*
# MIT-Khronos-old
# _deps/monado-src/src/external/glad/include/KHR/khrplatform.h
# MIT
# _deps/monado-src/cmake/sanitizers/{FindASan.cmake,FindMSan.cmake,FindSanitizers.cmake,FindTSan.cmake,FindUBSan.cmake,asan-wrapper,sanitize-helpers.cmake}
# _deps/monado-src/doc/doxygen-awesome-css/*
# _deps/monado-src/src/external/{cjson,imgui,jnipp,mermaid,renderdoc_api,solarxr,stb,tracy,valve-file-vdf}/*
# _deps/monado-src/src/xrt/targets/android_common/src/main/res/raw/*
# external/{magic_enum.hpp,magic_enum_containers.hpp,vk_mem_alloc.h}
# Zlib
# _deps/monado-src/src/external/nanopb/*
URL:            %{forgeurl0}
Source0:        %{forgesource0}
# License: GPL-3.0-or-later
Source1:        %{forgeurl1}/-/archive/%{commit1}/monado-src-%{commit1}.tar.bz2

# Check for new/removed patches when updating: https://github.com/WiVRn/WiVRn/tree/master/patches/monado/ (check the tag)
# Make sure to re-pull the patches every release. They are rebased and need to be updated!
# For tagged releases: https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%%{tag0}/patches/monado/
# For commit releases: https://raw.githubusercontent.com/WiVRn/WiVRn/%%{commit0}/patches/monado/
# downstream-only - WiVRn specific Monado patches
Patch0001:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0001-c-multi-early-wake-of-compositor.patch
# downstream-only - WiVRn specific Monado patches
Patch0002:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0002-ipc-server-Always-listen-to-stdin.patch
# downstream-only - WiVRn specific Monado patches
Patch0003:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0003-Use-extern-socket-fd.patch
# downstream-only - WiVRn specific Monado patches
Patch0004:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0004-c-render-Add-storage-usage-to-distortion-mesh.patch
# downstream-only - WiVRn specific Monado patches
Patch0005:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0005-change-environment-blend-mode-selection-logic.patch
# downstream-only - WiVRn specific Monado patches
Patch0006:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0006-Convert-to-YCbCr-in-Monado.patch
# downstream-only - WiVRn specific Monado patches
Patch0007:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0007-store-alpha-channel-in-layer-1.patch
# downstream-only - WiVRn specific Monado patches
Patch0008:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0008-c-main-allow-custom-pacing-app-factory.patch
# downstream-only - WiVRn specific Monado patches
Patch0009:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0009-st-oxr-forward-0-refresh-rate.patch
# downstream-only - WiVRn specific Monado patches
Patch0010:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0010-Replace-distortion-with-pixel-aligned-foveation.patch
# downstream-only - WiVRn specific Monado patches
Patch0011:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0011-a-vk-Track-VK_KHR_video_maintenance1.patch
# downstream-only - WiVRn specific Monado patches
Patch0012:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0012-a-vk-Expose-video_maintenance_1-device-feature.patch
# downstream-only - WiVRn specific Monado patches
Patch0013:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0013-c-util-Request-video_maintenance_1-feature.patch


# If BuildRequires change, be sure to update envision-wivrn Requires
# https://src.fedoraproject.org/rpms/envision/blob/rawhide/f/envision.spec
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  glslc
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools
BuildRequires:  ninja-build
BuildRequires:  openxr-devel >= 1.0.29
BuildRequires:  python
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(CLI11)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcjson)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libuvc)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(openhmd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(openvr)
# Perfetto only supports these architectures
%ifarch aarch64 x86_64
BuildRequires:  pkgconfig(percetto)
%endif
BuildRequires:  pkgconfig(Qt6)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(realsense2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-eglstream)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
%if %{with x264}
BuildRequires:  pkgconfig(x264)
%endif
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  qcoro-qt6-devel
BuildRequires:  qt6qml(org.kde.desktop)
BuildRequires:  systemd-rpm-macros

Requires:       android-tools
Requires:       firewalld-filesystem
Requires:       opencomposite
Requires:       openxr

Recommends:     %{name}-dashboard

Provides:       bundled(monado) = %{monado_version}

# no big-endian support, vulkan 32bit headers broken
# https://github.com/WiVRn/WiVRn/issues/271
ExcludeArch:    s390x %{ix86}

%description
WiVRn wirelessly connects a standalone VR headset to a Linux computer.
You can then play PCVR games on the headset while processing is done
on the computer.

Supports a wide range of headsets such as:

Quest 1 / 2 / Pro / 3 / 3S
Pico Neo 4
HTC Vive Focus 3 / HTC Vive XR elite
and most other Android based headsets


%package -n %{name}-dashboard
Summary:        WiVRn dashboard
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       qt6qml(org.kde.desktop)

%description -n %{name}-dashboard
WiVRn dashboard is a GUI for configuring and controlling WiVRn.

It is used to manage the server configuration, client installation,
and to assist in pairing the headset with the server.


%prep
%forgesetup

# Extract libraries that are bundled
mkdir -p _deps/monado-src
tar -xvf %{SOURCE1} --strip-components 1 -C _deps/monado-src
# Apply WiVRn downstream patches
pushd _deps/monado-src
%patch -P0001 -p1
%patch -P0002 -p1
%patch -P0003 -p1
%patch -P0004 -p1
%patch -P0005 -p1
%patch -P0006 -p1
%patch -P0007 -p1
%patch -P0008 -p1
%patch -P0009 -p1
%patch -P0010 -p1
%patch -P0011 -p1
%patch -P0012 -p1
%patch -P0013 -p1
popd


%build
%cmake -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON \
  -DCMAKE_PROJECT_VERSION=%{monado_version} \
  -DENABLE_COLOURED_OUTPUT=OFF \
  -DFETCHCONTENT_BASE_DIR="_deps" \
  -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
  -DGIT_DESC=v%{version} \
  -DOVR_COMPAT_SEARCH_PATH=%{_libdir}/opencomposite/runtime \
  -DWIVRN_BUILD_CLIENT=OFF \
  -DWIVRN_BUILD_DASHBOARD=ON \
  -DWIVRN_BUILD_DISSECTOR=OFF \
  -DWIVRN_BUILD_SERVER=ON \
  -DWIVRN_BUILD_WIVRNCTL=ON \
  -DWIVRN_USE_NVENC=ON \
  -DWIVRN_USE_PIPEWIRE=ON \
  -DWIVRN_USE_PULSEAUDIO=OFF \
  -DWIVRN_USE_SYSTEMD=ON \
  -DWIVRN_USE_VAAPI=ON \
%if %{with x264}
  -DWIVRN_USE_X264=ON \
%else
  -DWIVRN_USE_X264=OFF \
%endif

%cmake_build


%install
%cmake_install

# Configure to use the DSO linker for the runtime
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Unversioned_shared_objects/
install -m 0755 -vd %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf

%find_lang %{name}-dashboard

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.wivrn.wivrn.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files -f %{name}-dashboard.lang
%license COPYING LICENSE-OFL-1.1 _deps/monado-src/LICENSES/*
%doc README.md docs/
%caps(cap_sys_nice=ep) %{_bindir}/wivrn-server
%{_bindir}/wivrnctl
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libopenxr_wivrn.so
%{_libdir}/%{name}/libmonado_wivrn.so
%{_libdir}/%{name}/libmonado_wivrn.so.25
%{_libdir}/%{name}/libmonado_wivrn.so.25.0.0
%{_datarootdir}/openxr/1/openxr_wivrn.json
%{_userunitdir}/wivrn.service
%{_prefix}/lib/firewalld/services/wivrn.xml
%{_metainfodir}/io.github.wivrn.wivrn.metainfo.xml
%{_sysconfdir}/ld.so.conf.d/%{name}.conf

%files -n %{name}-dashboard
%{_bindir}/wivrn-dashboard
%{_datarootdir}/applications/io.github.wivrn.wivrn.desktop
%{_datarootdir}/icons/hicolor/scalable/apps/io.github.wivrn.wivrn.svg


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service


%changelog
%autochangelog
