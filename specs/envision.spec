%bcond_without check
%global cargo_install_lib  0
%global envision_version   3.1.0
%global forgeurl           https://gitlab.com/gabmus/envision
%global tag                %{envision_version}
%global date               20250408
%forgemeta

# prevent library files from being installed
%global cargo_install_lib 0

Name:           envision
Version:        %{envision_version}
Release:        %autorelease
Summary:        UI for building, configuring, and running Monado/WiVRn

License:        AGPL-3.0-only AND (Apache-2.0 OR MIT OR BSD-3-Clause OR GPL-2.0-only WITH GCC-exception-2.0 OR ISC OR BSL-1.0 OR Zlib OR Unicode-DFS-2016 OR Unlicense) AND (Apache-2.0 WITH LLVM-exception OR BSD-2-Clause)

# (Apache-2.0 OR MIT) AND BSD-3-Clause: encoding_rs v0.8.35
# (MIT OR Apache-2.0) AND Unicode-3.0: unicode-ident v1.0.17
# (MIT OR Apache-2.0) AND Unicode-DFS-2016: regex-syntax v0.6.29
# (MIT OR Apache-2.0) AND Unicode-DFS-2016: regex-syntax v0.8.5
# AGPL-3.0-or-later: envision v3.0.0
# Apache-2.0 OR BSL-1.0: ryu v1.0.18
# Apache-2.0 OR ISC OR MIT: rustls-pemfile v2.2.0
# Apache-2.0 OR MIT: async-channel v2.3.1
# Apache-2.0 OR MIT: async-executor v1.13.1
# Apache-2.0 OR MIT: async-fs v2.1.2
# Apache-2.0 OR MIT: async-io v2.4.0
# Apache-2.0 OR MIT: async-lock v3.4.0
# Apache-2.0 OR MIT: async-process v2.3.0
# Apache-2.0 OR MIT: async-signal v0.2.10
# Apache-2.0 OR MIT: async-task v4.7.1
# Apache-2.0 OR MIT: atomic-waker v1.1.2
# Apache-2.0 OR MIT: blocking v1.6.1
# Apache-2.0 OR MIT: concurrent-queue v2.5.0
# Apache-2.0 OR MIT: equivalent v1.0.2
# Apache-2.0 OR MIT: event-listener v5.4.0
# Apache-2.0 OR MIT: event-listener-strategy v0.5.3
# Apache-2.0 OR MIT: fastrand v2.3.0
# Apache-2.0 OR MIT: flume v0.11.1
# Apache-2.0 OR MIT: fnv v1.0.7
# Apache-2.0 OR MIT: futures-lite v2.6.0
# Apache-2.0 OR MIT: indexmap v2.7.1
# Apache-2.0 OR MIT: parking v2.2.1
# Apache-2.0 OR MIT: pin-project-lite v0.2.16
# Apache-2.0 OR MIT: polling v3.7.4
# Apache-2.0 OR MIT: relm4 v0.9.1
# Apache-2.0 OR MIT: relm4-components v0.9.1
# Apache-2.0 OR MIT: relm4-css v0.9.0
# Apache-2.0 OR MIT: signal-hook-registry v1.4.2
# Apache-2.0 OR MIT: tracker v0.2.2
# Apache-2.0 OR MIT: uuid v1.13.2
# Apache-2.0 OR MIT: xdg v2.5.2
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: io-lifetimes v2.0.4
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: linux-raw-sys v0.4.15
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: rustix v0.38.44
# Apache-2.0: flagset v0.4.6
# Apache-2.0: fragile v2.0.0
# Apache-2.0: openssl v0.10.70
# Apache-2.0: sync_wrapper v1.0.2
# BSD-2-Clause OR Apache-2.0 OR MIT: zerocopy v0.7.35
# BSD-2-Clause OR Apache-2.0 OR MIT: zerocopy v0.8.14
# ISC: libloading v0.8.6
# MIT OR Apache-2.0 OR Zlib: tinyvec_macros v0.1.1
# MIT OR Apache-2.0: anyhow v1.0.96
# MIT OR Apache-2.0: ash v0.38.0
# MIT OR Apache-2.0: async-broadcast v0.7.2
# MIT OR Apache-2.0: base64 v0.22.1
# MIT OR Apache-2.0: bitflags v2.8.0
# MIT OR Apache-2.0: block-buffer v0.10.4
# MIT OR Apache-2.0: cfg-if v1.0.0
# MIT OR Apache-2.0: cpufeatures v0.2.17
# MIT OR Apache-2.0: crossbeam-channel v0.5.14
# MIT OR Apache-2.0: crossbeam-utils v0.8.21
# MIT OR Apache-2.0: crypto-common v0.1.6
# MIT OR Apache-2.0: deranged v0.3.11
# MIT OR Apache-2.0: digest v0.10.7
# MIT OR Apache-2.0: enumflags2 v0.7.11
# MIT OR Apache-2.0: errno v0.3.10
# MIT OR Apache-2.0: field-offset v0.3.6
# MIT OR Apache-2.0: foreign-types v0.3.2
# MIT OR Apache-2.0: foreign-types-shared v0.1.1
# MIT OR Apache-2.0: form_urlencoded v1.2.1
# MIT OR Apache-2.0: futures v0.3.31
# MIT OR Apache-2.0: futures-channel v0.3.31
# MIT OR Apache-2.0: futures-core v0.3.31
# MIT OR Apache-2.0: futures-executor v0.3.31
# MIT OR Apache-2.0: futures-io v0.3.31
# MIT OR Apache-2.0: futures-sink v0.3.31
# MIT OR Apache-2.0: futures-task v0.3.31
# MIT OR Apache-2.0: futures-util v0.3.31
# MIT OR Apache-2.0: getrandom v0.2.15
# MIT OR Apache-2.0: getrandom v0.3.1

URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  clippy
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3
BuildRequires:  g++
BuildRequires:  gdb-gdbserver
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  glslang
BuildRequires:  glslc
BuildRequires:  gtk4-devel
BuildRequires:  gtksourceview5-devel
BuildRequires:  libappstream-glib
BuildRequires:  libadwaita-devel
BuildRequires:  libdrm
BuildRequires:  libgudev-devel
BuildRequires:  libusb1-devel
BuildRequires:  libXrandr-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  openxr-devel
BuildRequires:  rustc
BuildRequires:  rustfmt
BuildRequires:  vte291-gtk4-devel
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-loader-devel

Requires:       hicolor-icon-theme
Requires:       patch
Suggests:       android-tools


%description
UI for building, configuring, and running Monado, the open source 
OpenXR runtime.

This is still highly experimental software, while it's unlikely that 
anything bad will happen, it's still unstable and there is no guarantee 
that it will work on your system, with your particular hardware. If you 
encounter any problems while using the app, make sure to open an issue.

Also consider that due to the unstable nature of the app, it's possible 
to encounter unexpected behavior that while in VR might cause motion 
sickness or physical injury. Be very careful while in VR using this app!


%package wivrn

Summary:        WiVRn Build Dependencies for Envision
Requires:       %{name} = %{version}-%{release}
# Sync with https://src.fedoraproject.org/rpms/wivrn/raw/rawhide/f/wivrn.spec
Requires:       boost-devel
Requires:       cmake
Requires:       desktop-file-utils
Requires:       extra-cmake-modules
Requires:       gcc-c++
Requires:       gettext-devel
Requires:       git
Requires:       glslc
Requires:       kf6-kcoreaddons-devel
Requires:       kf6-ki18n-devel
Requires:       kf6-kiconthemes-devel
Requires:       kf6-kirigami-devel
Requires:       libappstream-glib
Requires:       librsvg2-tools
Requires:       ninja-build
Requires:       openxr-devel
Requires:       python
Requires:       pkgconfig(avahi-client)
Requires:       pkgconfig(avahi-glib)
Requires:       pkgconfig(bluez)
Requires:       pkgconfig(CLI11)
Requires:       pkgconfig(dbus-1)
Requires:       pkgconfig(eigen3)
Requires:       pkgconfig(glslang)
Requires:       pkgconfig(gstreamer-1.0)
Requires:       pkgconfig(gstreamer-app-1.0)
Requires:       pkgconfig(gstreamer-video-1.0)
Requires:       pkgconfig(hidapi-libusb)
Requires:       pkgconfig(libavcodec)
Requires:       pkgconfig(libavfilter)
Requires:       pkgconfig(libavutil)
Requires:       pkgconfig(libbsd)
Requires:       pkgconfig(libcap)
Requires:       pkgconfig(libcjson)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libnotify)
Requires:       pkgconfig(libpipewire-0.3)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(libusb-1.0)
Requires:       pkgconfig(libuvc)
Requires:       pkgconfig(libswscale)
Requires:       pkgconfig(libva)
Requires:       pkgconfig(nlohmann_json)
Requires:       pkgconfig(opencv)
Requires:       pkgconfig(openhmd)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(openvr)
Requires:       pkgconfig(Qt6)
Requires:       pkgconfig(Qt6Linguist)
Requires:       pkgconfig(Qt6Quick)
Requires:       pkgconfig(realsense2)
Requires:       pkgconfig(sdl2)
Requires:       pkgconfig(vulkan)
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-eglstream)
Requires:       pkgconfig(wayland-protocols)
Requires:       pkgconfig(wayland-scanner)
Requires:       pkgconfig(xrandr)
Requires:       qcoro-qt6-devel
Requires:       qt6qml(org.kde.desktop)
Requires:       android-tools
Requires:       firewalld-filesystem
Requires:       hicolor-icon-theme
Requires:       qt6qml(org.kde.desktop)

%description wivrn
Build dependencies for WiVRn. Install this to automatically
bring in all needed dependencies for building WiVRn.


%package monado

Summary:        Monado Build Dependencies for Envision
Requires:       %{name} = %{version}-%{release}
# Sync with https://jsteffan.fedorapeople.org/imrsv/monado.spec
Requires:       cmake
Requires:       gcc-c++
Requires:       glslc
Requires:       ninja-build
Requires:       pkgconfig(bluez)
Requires:       pkgconfig(dbus-1)
Requires:       pkgconfig(dri)
Requires:       pkgconfig(eigen3)
Requires:       pkgconfig(glslang)
Requires:       pkgconfig(gstreamer-1.0)
Requires:       pkgconfig(gstreamer-app-1.0)
Requires:       pkgconfig(gstreamer-video-1.0)
Requires:       pkgconfig(hidapi-libusb)
Requires:       pkgconfig(libavcodec)
Requires:       pkgconfig(libbsd)
Requires:       pkgconfig(libcjson)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libjpeg)
# ONNX only for x86_64, ppc64le and aarch64
%ifnarch s390x %{arm} %{ix86}
Requires:       pkgconfig(libonnxruntime)
%endif
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(libusb-1.0)
Requires:       pkgconfig(libuvc)
Requires:       pkgconfig(opencv)
Requires:       pkgconfig(openhmd)
Requires:       pkgconfig(openvr)
Requires:       pkgconfig(openxr)
Requires:       pkgconfig(realsense2)
Requires:       pkgconfig(sdl2)
Requires:       pkgconfig(vulkan)
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-eglstream)
Requires:       pkgconfig(wayland-protocols)
Requires:       pkgconfig(wayland-scanner)
Requires:       pkgconfig(xrandr)
Requires:       pkgconfig(zlib)

%description monado
Build dependencies for Monado. Install this to automatically
bring in all needed dependencies for building Monado.


%prep
%forgeautosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires


%build
%meson -D profile=release
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
%meson_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gabmus.envision.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%if %{with check}
%meson_test
%endif


%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/envision
%{_datarootdir}/envision/
%{_datarootdir}/applications/org.gabmus.envision.desktop
%{_datarootdir}/icons/hicolor/scalable/apps/org.gabmus.envision.svg
%{_datarootdir}/icons/hicolor/symbolic/apps/org.gabmus.envision-symbolic.svg
%{_metainfodir}/org.gabmus.envision.appdata.xml

%files wivrn

%files monado


%changelog
%autochangelog
