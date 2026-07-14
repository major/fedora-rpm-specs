%global commit      876018610f2c2909b66b3d37b1fc55975c11a7e5
%global date        20260711
%global shortcommit %{sub %{commit} 1 7}

%global libmonado_somajor 25
%global libmonado_sover   25.1.0

Name:           monado
Version:        25.1.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        The open source OpenXR runtime

License:        %{shrink:
                Apache-2.0 AND
                BSD-2-Clause AND
                BSD-3-Clause AND
                BSL-1.0 AND
                CC-BY-4.0 AND
                CC0-1.0 AND
                MIT AND
                Unlicense AND
                Zlib}
# License breakdown for the files that reach the binary packages:
#   Apache-2.0    src/external/glad, parts of src/xrt
#   BSD-2-Clause  src/external/hungarian
#   BSD-3-Clause  src/external/tinyceres, src/xrt/drivers/north_star,
#                 src/xrt/tracking/hand/mercury, SteamVR driver resources
#   BSL-1.0       most of src/xrt, src/external/{flexkalman,metrics}, doc/*.md
#   CC-BY-4.0     README.md, CONTRIBUTING.md
#   CC0-1.0       src/external/glad, doc/*.md
#   MIT           src/external/imgui, and src/external/glad/include/KHR/khrplatform.h,
#                 which is the Khronos variant of MIT using "Materials" for "Software"
#   Unlicense     src/external/stb and src/external/imgui/imstb*, both MIT OR Unlicense
#   Zlib          src/external/nanopb


URL:            https://gitlab.freedesktop.org/monado/monado
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz


BuildRequires:  cmake
BuildRequires:  systemd-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  glslc
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(basalt)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libcjson)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libonnxruntime)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libuvc)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(openhmd)
BuildRequires:  pkgconfig(openvr)
BuildRequires:  pkgconfig(openxr)
BuildRequires:  pkgconfig(percetto)
BuildRequires:  pkgconfig(realsense2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(survive)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-eglstream)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)

# Dlopened rather than linked, so they need a manual dependency.
Requires:       basalt-monado
Requires:       openxr

# Bundled copies under src/external that are compiled into the binaries.
Provides:       bundled(glad)
Provides:       bundled(hungarian)
Provides:       bundled(imgui) = 1.92.5
Provides:       bundled(nanopb) = 0.4.9.1
Provides:       bundled(stb)
Provides:       bundled(tinyceres)

# libopenxr_monado.so is a dlopen-only module with no SONAME. It only lands in the
# loader path because %%{_libdir}/%%{name} is there for libmonado's sake, which makes
# RPM advertise it as if it were a linkable library. Nothing links against it.
%global __provides_exclude ^libopenxr_monado\\.so

# Build on x86_64 and aarch64 only, missing dependencies on other architectures.
ExclusiveArch:  x86_64 aarch64


%description
Monado is an open-source package for interacting with virtual and
augmented reality (collectively known as XR) hardware and software.

This package provides a runtime that aims to be a complete and conforming
implementation of the OpenXR API from Khronos. When used with the
"simulated" device driver, this package is conforming to OpenXR 1.0.


%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary:  Development files for Monado

%description devel
Devel information for Monado.


%prep
%autosetup -n %{name}-%{commit} -p1


%build
%cmake -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_LIBDIR=%{_lib}/%{name} \

%cmake_build


%install
%cmake_install
# driver_monado.so is an arch-dependent ELF; move it to %%{_libdir} and
# leave a relative symlink so SteamVR can still find it at its expected path.
install -d %{buildroot}%{_libdir}/steamvr-monado/bin/linux64
mv %{buildroot}%{_datadir}/steamvr-monado/bin/linux64/driver_monado.so \
   %{buildroot}%{_libdir}/steamvr-monado/bin/linux64/driver_monado.so
chmod 0755 %{buildroot}%{_libdir}/steamvr-monado/bin/linux64/driver_monado.so
ln -sr %{buildroot}%{_libdir}/steamvr-monado/bin/linux64/driver_monado.so \
   %{buildroot}%{_datadir}/steamvr-monado/bin/linux64/driver_monado.so

# vrclient.so is an arch-dependent ELF; move it to %%{_libdir} and
# leave a relative symlink so SteamVR can still find it at its expected path.
install -d %{buildroot}%{_libdir}/st-openvr/bin/linux64
mv %{buildroot}%{_datadir}/st-openvr/bin/linux64/vrclient.so \
   %{buildroot}%{_libdir}/st-openvr/bin/linux64/vrclient.so
chmod 0755 %{buildroot}%{_libdir}/st-openvr/bin/linux64/vrclient.so
ln -sr %{buildroot}%{_libdir}/st-openvr/bin/linux64/vrclient.so \
   %{buildroot}%{_datadir}/st-openvr/bin/linux64/vrclient.so

# Configure to use the DSO linker for the runtime.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Unversioned_shared_objects/
install -m 0755 -vd %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf

# Update manifest to point at ABI-stable name.
sed -i -r \
  -e 's|("MND_libmonado_path": ").*(")|\1../../../%{_lib}/%{name}/libmonado.so.%{libmonado_somajor}\2|' \
  %{buildroot}%{_datadir}/openxr/1/openxr_monado.json


%check
cd %{_vpath_builddir}
ctest --output-on-failure

%post
%systemd_user_post monado.service monado.socket

%preun
%systemd_user_preun monado.service monado.socket

%postun
%systemd_user_postun_with_restart monado.service

%files
%license LICENSE LICENSES/*
%doc CONTRIBUTING.md README.md doc/*.md
%{_bindir}/monado-service
%{_bindir}/monado-cli
%{_bindir}/monado-ctl
%{_bindir}/monado-gui
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libmonado.so.%{libmonado_somajor}
%{_libdir}/%{name}/libmonado.so.%{libmonado_sover}
%{_libdir}/%{name}/libopenxr_monado.so
%{_libdir}/steamvr-monado/
%{_datadir}/steamvr-monado/
%{_libdir}/st-openvr/
%{_datadir}/st-openvr/
%{_userunitdir}/monado.service
%{_userunitdir}/monado.socket
%{_datadir}/openxr/1/openxr_monado.json
%{_sysconfdir}/ld.so.conf.d/%{name}.conf


%files devel
%{_libdir}/%{name}/libmonado.so
%dir %{_includedir}/monado
%{_includedir}/monado/monado.h


%changelog
%autochangelog
