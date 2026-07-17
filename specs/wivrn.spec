# Build features, default off
%bcond_with x264

%global forgeurl0      https://github.com/WiVRn/WiVRn
%global tag0           v%{version}

# WiVRn is based on Monado, we need the full source
# Monado base source (find in monado-rev file)
%global forgeurl1      https://gitlab.freedesktop.org/monado/monado
%global commit1        1b526bb3a0ff326ecd05af4c2c541407f53c6d4b
%global monado_version 25.1.0

%forgemeta

Name:           wivrn
Version:        26.6.2
Release:        %autorelease
Summary:        An OpenXR streaming application to a standalone headset

License:        %{shrink:
    Apache-2.0
    AND BSD-2-Clause
    AND BSD-3-Clause
    AND BSL-1.0
    AND CC-BY-4.0
    AND CC0-1.0
    AND CECILL-C
    AND GPL-2.0-or-later
    AND GPL-3.0-or-later
    AND MIT
    AND MIT-Khronos-old
    AND OFL-1.1
    AND Unlicense
    AND Zlib
}
# For a per-file license breakdown see LicenseBreakdown.
URL:            %{forgeurl0}
Source0:        %{forgesource0}
# License: GPL-3.0-or-later
Source1:        %{forgeurl1}/-/archive/%{commit1}/monado-src-%{commit1}.tar.bz2

# Check for new/removed patches when updating: https://github.com/WiVRn/WiVRn/tree/master/patches/monado/ (check the tag)
# Make sure to re-pull the patches every release. They are rebased and need to be updated!
# downstream-only - WiVRn specific Monado patches
Patch0001:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0001-c-multi-early-wake-of-compositor.patch
# downstream-only - WiVRn specific Monado patches
Patch0002:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0002-Use-extern-socket-fd.patch
# downstream-only - WiVRn specific Monado patches
Patch0003:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0003-change-environment-blend-mode-selection-logic.patch
# downstream-only - WiVRn specific Monado patches
Patch0004:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0004-st-oxr-forward-0-refresh-rate.patch
# downstream-only - WiVRn specific Monado patches
Patch0005:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0005-d-steamvr_lh-prevent-crash-on-vive-pro2-WiVRn.patch
# downstream-only - WiVRn specific Monado patches
Patch0006:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0006-st-oxr-push-XrEventDataInteractionProfileChanged-whe.patch
# downstream-only - WiVRn specific Monado patches
Patch0007:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0007-don-t-verify-GL-stuff.patch
# downstream-only - WiVRn specific Monado patches
Patch0008:      https://raw.githubusercontent.com/WiVRn/WiVRn/refs/tags/%{tag0}/patches/monado/0008-configure-u_git_tag-in-WiVRn.patch


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
BuildRequires:  kf6-kirigami-addons-devel
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
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6qml(org.kde.desktop)
BuildRequires:  spirv-tools
BuildRequires:  systemd-rpm-macros

Requires:       android-tools
Requires:       firewalld-filesystem
Requires:       opencomposite
Requires:       openxr

Recommends:     %{name}-dashboard

Provides:       bundled(monado) = %{monado_version}

# no big-endian support, vulkan 32bit headers broken, android-tools not available on ppc64le
# https://github.com/WiVRn/WiVRn/issues/271
# https://src.fedoraproject.org/rpms/android-tools/c/38eea7154cb5930259f7a3ae59cdb123fb7d2862?branch=rawhide
ExcludeArch:    s390x %{ix86} ppc64le

%description
WiVRn wirelessly connects a standalone VR headset to a Linux computer.
You can then play PCVR games on the headset while processing is done
on the computer.

Supports a wide range of headsets such as:

Meta Quest 1, 2, 3, 3S, pro
Pico Neo 4
HTC Vive Focus 3, XR Elite
Samsung Galaxy XR
and most other Android based headsets


%package -n %{name}-dashboard
Summary:        WiVRn dashboard
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       kf6-kirigami-addons
Requires:       qt6qml(org.kde.desktop)

%description -n %{name}-dashboard
WiVRn dashboard is a GUI for configuring and controlling WiVRn.

It is used to manage the server configuration, client installation,
and to assist in pairing the headset with the server.


%prep
%setup -q -n WiVRn-%{version}

# Extract libraries that are bundled
mkdir -p _deps/monado-src
tar -xvf %{SOURCE1} --strip-components 1 -C _deps/monado-src
# Apply WiVRn downstream Monado patches
pushd _deps/monado-src
%patch -P0001 -p1
%patch -P0002 -p1
%patch -P0003 -p1
%patch -P0004 -p1
%patch -P0005 -p1
%patch -P0006 -p1
%patch -P0007 -p1
%patch -P0008 -p1
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
  -DGIT_COMMIT=v%{version} \
  -DOVR_COMPAT_SEARCH_PATH=%{_libdir}/opencomposite/runtime:%{_libdir}/xrizer/runtime:/opt/opencomposite:/opt/xrizer \
  -DWIVRN_BUILD_CLIENT=OFF \
  -DWIVRN_BUILD_DASHBOARD=ON \
  -DWIVRN_BUILD_DISSECTOR=OFF \
  -DWIVRN_BUILD_SERVER=ON \
  -DWIVRN_BUILD_WIVRNCTL=ON \
  -DWIVRN_FEATURE_STEAMVR_LIGHTHOUSE=ON \
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

# Import the WiVRn OpenXR runtime into Steam's pressure-vessel container
install -m 0755 -vd %{buildroot}%{_environmentdir}
echo "PRESSURE_VESSEL_IMPORT_OPENXR_1_RUNTIMES=1" > %{buildroot}%{_environmentdir}/%{name}.conf

%find_lang %{name}-dashboard

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.wivrn.wivrn.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files -f %{name}-dashboard.lang
%license COPYING LICENSE-OFL-1.1 _deps/monado-src/LICENSES/*
%doc README.md docs/
%{_bindir}/wivrn-server
%{_bindir}/wivrnctl
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libopenxr_wivrn.so
%{_libdir}/%{name}/libmonado_wivrn.so
%{_libdir}/%{name}/libmonado_wivrn.so.25
%{_libdir}/%{name}/libmonado_wivrn.so.25.1.0
%{_datarootdir}/openxr/1/openxr_wivrn.json
%{_userunitdir}/wivrn.service
%{_prefix}/lib/firewalld/services/wivrn.xml
%{_metainfodir}/io.github.wivrn.wivrn.metainfo.xml
%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%{_environmentdir}/%{name}.conf

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
