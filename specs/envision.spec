%bcond_without check
%global cargo_install_lib  0
%global envision_version   3.2.0
%global forgeurl           https://gitlab.com/gabmus/envision
%global tag                %{envision_version}
%global date               20250916
%forgemeta

# prevent library files from being installed
%global cargo_install_lib 0

Name:           envision
Version:        %{envision_version}
Release:        %autorelease
Summary:        UI for building, configuring, and running Monado/WiVRn

License:        AGPL-3.0-only AND (Apache-2.0 OR MIT OR BSD-3-Clause OR GPL-2.0-only WITH GCC-exception-2.0 OR ISC OR BSL-1.0 OR Zlib OR Unicode-DFS-2016 OR Unlicense) AND (Apache-2.0 WITH LLVM-exception OR BSD-2-Clause)

# (Apache-2.0 OR MIT) AND BSD-3-Clause: encoding_rs v0.8.35
# (MIT OR Apache-2.0) AND BSD-3-Clause AND GPL-2.0-only WITH GCC-exception-2.0 AND MIT: libgit2-sys v0.17.0
# (MIT OR Apache-2.0) AND Unicode-3.0: unicode-ident v1.0.19
# (MIT OR Apache-2.0) AND Unicode-DFS-2016: regex-syntax v0.8.6
# AGPL-3.0-or-later: envision v3.2.0
# Apache-2.0 OR BSL-1.0: ryu v1.0.20
# Apache-2.0 OR MIT: async-channel v2.5.0
# Apache-2.0 OR MIT: async-executor v1.13.3
# Apache-2.0 OR MIT: async-io v2.6.0
# Apache-2.0 OR MIT: async-lock v3.4.1
# Apache-2.0 OR MIT: async-process v2.5.0
# Apache-2.0 OR MIT: async-signal v0.2.13
# Apache-2.0 OR MIT: async-task v4.7.1
# Apache-2.0 OR MIT: atomic-waker v1.1.2
# Apache-2.0 OR MIT: blocking v1.6.2
# Apache-2.0 OR MIT: concurrent-queue v2.5.0
# Apache-2.0 OR MIT: equivalent v1.0.2
# Apache-2.0 OR MIT: event-listener v5.4.1
# Apache-2.0 OR MIT: event-listener-strategy v0.5.4
# Apache-2.0 OR MIT: fastrand v2.3.0
# Apache-2.0 OR MIT: flume v0.11.1
# Apache-2.0 OR MIT: fnv v1.0.7
# Apache-2.0 OR MIT: futures-lite v2.6.1
# Apache-2.0 OR MIT: idna_adapter v1.2.1
# Apache-2.0 OR MIT: indexmap v2.11.1
# Apache-2.0 OR MIT: parking v2.2.1
# Apache-2.0 OR MIT: pin-project-lite v0.2.16
# Apache-2.0 OR MIT: polling v3.11.0
# Apache-2.0 OR MIT: relm4 v0.9.1
# Apache-2.0 OR MIT: relm4-components v0.9.1
# Apache-2.0 OR MIT: relm4-css v0.9.0
# Apache-2.0 OR MIT: signal-hook-registry v1.4.6
# Apache-2.0 OR MIT: tracker v0.2.2
# Apache-2.0 OR MIT: utf8_iter v1.0.4
# Apache-2.0 OR MIT: uuid v1.18.1
# Apache-2.0 OR MIT: xdg v2.5.2
# Apache-2.0 OR MIT: zeroize v1.8.1
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: io-lifetimes v2.0.4
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: linux-raw-sys v0.11.0
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: rustix v1.1.2
# Apache-2.0: flagset v0.4.7
# Apache-2.0: fragile v2.0.1
# Apache-2.0: openssl v0.10.73
# Apache-2.0: sync_wrapper v1.0.2
# BSD-2-Clause OR Apache-2.0 OR MIT: zerocopy v0.8.26
# ISC: libloading v0.8.8
# LGPL-2.1-or-later: delicious-adwaita v0.3.1
# MIT OR Apache-2.0: anyhow v1.0.99
# MIT OR Apache-2.0: ash v0.38.0
# MIT OR Apache-2.0: async-broadcast v0.7.2
# MIT OR Apache-2.0: base64 v0.22.1
# MIT OR Apache-2.0: bitflags v2.9.3
# MIT OR Apache-2.0: block-buffer v0.10.4
# MIT OR Apache-2.0: cfg-if v1.0.3
# MIT OR Apache-2.0: cpufeatures v0.2.17
# MIT OR Apache-2.0: crossbeam-channel v0.5.15
# MIT OR Apache-2.0: crossbeam-utils v0.8.21
# MIT OR Apache-2.0: crypto-common v0.1.6
# MIT OR Apache-2.0: deranged v0.4.0
# MIT OR Apache-2.0: digest v0.10.7
# MIT OR Apache-2.0: enumflags2 v0.7.12
# MIT OR Apache-2.0: errno v0.3.14
# MIT OR Apache-2.0: field-offset v0.3.6
# MIT OR Apache-2.0: foreign-types v0.3.2
# MIT OR Apache-2.0: foreign-types-shared v0.1.1
# MIT OR Apache-2.0: form_urlencoded v1.2.2
# MIT OR Apache-2.0: futures v0.3.31
# MIT OR Apache-2.0: futures-channel v0.3.31
# MIT OR Apache-2.0: futures-core v0.3.31
# MIT OR Apache-2.0: futures-executor v0.3.31
# MIT OR Apache-2.0: futures-io v0.3.31
# MIT OR Apache-2.0: futures-sink v0.3.31
# MIT OR Apache-2.0: futures-task v0.3.31
# MIT OR Apache-2.0: futures-util v0.3.31
# MIT OR Apache-2.0: getrandom v0.2.16
# MIT OR Apache-2.0: getrandom v0.3.3
# MIT OR Apache-2.0: git2 v0.19.0
# MIT OR Apache-2.0: hashbrown v0.15.5
# MIT OR Apache-2.0: hex v0.4.3
# MIT OR Apache-2.0: http v1.3.1
# MIT OR Apache-2.0: httparse v1.10.1
# MIT OR Apache-2.0: hyper-tls v0.6.0
# MIT OR Apache-2.0: idna v1.1.0
# MIT OR Apache-2.0: ipnet v2.11.0
# MIT OR Apache-2.0: iri-string v0.7.8
# MIT OR Apache-2.0: itoa v1.0.15
# MIT OR Apache-2.0: keyvalues-parser v0.2.0
# MIT OR Apache-2.0: keyvalues-serde v0.2.2
# MIT OR Apache-2.0: lazy_static v1.5.0
# MIT OR Apache-2.0: libc v0.2.175
# MIT OR Apache-2.0: libssh2-sys v0.3.1
# MIT OR Apache-2.0: libz-sys v1.1.22
# MIT OR Apache-2.0: lock_api v0.4.13
# MIT OR Apache-2.0: log v0.4.28
# MIT OR Apache-2.0: mime v0.3.17
# MIT OR Apache-2.0: native-tls v0.2.14
# MIT OR Apache-2.0: notify-rust v4.11.7
# MIT OR Apache-2.0: num-conv v0.1.0
# MIT OR Apache-2.0: once_cell v1.21.3
# MIT OR Apache-2.0: openssl-probe v0.1.6
# MIT OR Apache-2.0: openxr v0.19.0
# MIT OR Apache-2.0: openxr-sys v0.11.0
# MIT OR Apache-2.0: ordered-stream v0.2.0
# MIT OR Apache-2.0: percent-encoding v2.3.2
# MIT OR Apache-2.0: pest v2.8.1
# MIT OR Apache-2.0: pin-utils v0.1.0
# MIT OR Apache-2.0: piper v0.2.4
# MIT OR Apache-2.0: powerfmt v0.2.0
# MIT OR Apache-2.0: ppv-lite86 v0.2.21
# MIT OR Apache-2.0: proc-macro2 v1.0.101
# MIT OR Apache-2.0: quote v1.0.40
# MIT OR Apache-2.0: rand v0.9.2
# MIT OR Apache-2.0: rand_chacha v0.9.0
# MIT OR Apache-2.0: rand_core v0.9.3
# MIT OR Apache-2.0: regex v1.11.2
# MIT OR Apache-2.0: regex-automata v0.4.10
# MIT OR Apache-2.0: reqwest v0.12.22
# MIT OR Apache-2.0: rustls-pki-types v1.12.0
# MIT OR Apache-2.0: scopeguard v1.2.0
# MIT OR Apache-2.0: semver v1.0.26
# MIT OR Apache-2.0: serde v1.0.219
# MIT OR Apache-2.0: serde_json v1.0.143
# MIT OR Apache-2.0: serde_urlencoded v0.7.1
# MIT OR Apache-2.0: serde_yaml v0.9.34
# MIT OR Apache-2.0: sha2 v0.10.9
# MIT OR Apache-2.0: smallvec v1.15.1
# MIT OR Apache-2.0: socket2 v0.6.0
# MIT OR Apache-2.0: stable_deref_trait v1.2.0
# MIT OR Apache-2.0: static_assertions v1.1.0
# MIT OR Apache-2.0: syn v2.0.106
# MIT OR Apache-2.0: thiserror v1.0.69
# MIT OR Apache-2.0: thiserror v2.0.16
# MIT OR Apache-2.0: thread_local v1.1.9
# MIT OR Apache-2.0: time v0.3.41
# MIT OR Apache-2.0: time-core v0.1.4
# MIT OR Apache-2.0: typenum v1.18.0
# MIT OR Apache-2.0: ucd-trie v0.1.7
# MIT OR Apache-2.0: url v2.5.4
# MIT: bytes v1.10.1
# MIT: cairo-rs v0.20.12
# MIT: cairo-sys-rs v0.20.10
# MIT: dlopen2 v0.7.0
# MIT: endi v1.1.0
# MIT: gdk-pixbuf v0.20.10
# MIT: gdk-pixbuf-sys v0.20.10
# MIT: gdk4 v0.9.6
# MIT: gdk4-sys v0.9.6
# MIT: generic-array v0.14.7
# MIT: gettext-rs v0.7.2
# MIT: gettext-sys v0.22.5
# MIT: gio v0.20.12
# MIT: gio-sys v0.20.10
# MIT: glib v0.20.12
# MIT: glib-sys v0.20.10
# MIT: gobject-sys v0.20.10
# MIT: graphene-rs v0.20.10
# MIT: graphene-sys v0.20.10
# MIT: gsk4 v0.9.6
# MIT: gsk4-sys v0.9.6
# MIT: gtk4 v0.9.7
# MIT: gtk4-sys v0.9.6
# MIT: h2 v0.4.12
# MIT: http-body v1.0.1
# MIT: http-body-util v0.1.3
# MIT: hyper v1.7.0
# MIT: hyper-util v0.1.17
# MIT: libadwaita v0.7.2
# MIT: libadwaita-sys v0.7.2
# MIT: libmonado v1.3.1
# MIT: libusb1-sys v0.7.0
# MIT: locale_config v0.3.0
# MIT: matchers v0.2.0
# MIT: memoffset v0.9.1
# MIT: mint v0.5.9
# MIT: mio v1.0.4
# MIT: nix v0.29.0
# MIT: nix v0.30.1
# MIT: nu-ansi-term v0.50.1
# MIT: openssl-sys v0.9.109
# MIT: pango v0.20.12
# MIT: pango-sys v0.20.10
# MIT: rusb v0.9.4
# MIT: sharded-slab v0.1.7
# MIT: slab v0.4.11
# MIT: spin v0.9.8
# MIT: tokio v1.47.1
# MIT: tokio-native-tls v0.3.1
# MIT: tokio-util v0.7.16
# MIT: tower v0.5.2
# MIT: tower-http v0.6.6
# MIT: tower-layer v0.3.3
# MIT: tower-service v0.3.3
# MIT: tracing v0.1.41
# MIT: tracing-appender v0.2.3
# MIT: tracing-core v0.1.34
# MIT: tracing-log v0.2.0
# MIT: tracing-serde v0.2.0
# MIT: tracing-subscriber v0.3.20
# MIT: try-lock v0.2.5
# MIT: unsafe-libyaml v0.2.11
# MIT: vte4 v0.8.0
# MIT: vte4-sys v0.8.0
# MIT: want v0.3.1
# MIT: winnow v0.7.13
# MIT: zbus v5.10.0
# MIT: zbus_names v4.2.0
# MIT: zvariant v5.7.0
# MIT: zvariant_utils v3.2.1
# Unicode-3.0: icu_collections v2.0.0
# Unicode-3.0: icu_locale_core v2.0.0
# Unicode-3.0: icu_normalizer v2.0.0
# Unicode-3.0: icu_normalizer_data v2.0.0
# Unicode-3.0: icu_properties v2.0.1
# Unicode-3.0: icu_properties_data v2.0.1
# Unicode-3.0: icu_provider v2.0.0
# Unicode-3.0: litemap v0.8.0
# Unicode-3.0: potential_utf v0.1.3
# Unicode-3.0: tinystr v0.8.1
# Unicode-3.0: writeable v0.6.1
# Unicode-3.0: yoke v0.8.0
# Unicode-3.0: zerofrom v0.1.6
# Unicode-3.0: zerotrie v0.2.2
# Unicode-3.0: zerovec v0.11.4
# Unlicense OR MIT: aho-corasick v1.1.3
# Unlicense OR MIT: memchr v2.7.5
# Zlib: nanorand v0.7.0

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
Requires:       pkgconfig(libarchive)
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
Requires:       pkgconfig(librsvg-2.0)
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


%package xrizer

Summary:        Xrizer Build Dependencies for Envision
Requires:       %{name} = %{version}-%{release}
# Sync with https://gitlab.com/gabmus/envision/-/blob/main/src/depcheck/xrizer_deps.rs
# until we have xrizer as a package
Requires:       clang19-devel
Requires:       libxcb-devel
Requires:       wayland-devel

%description xrizer
Build dependencies for xrizer. Install this to automatically
bring in all needed dependencies for building xrizer.


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

%files xrizer


%changelog
%autochangelog
