%global commit      110de905cbb89313ecae7ffd2dfacd8f8d2a3f7a
%global date        20260709
%global shortcommit %{sub %{commit} 1 7}

Name:           monado
Version:        25.1.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        The open source OpenXR runtime

License:        %{shrink:
                GPL-3.0-or-later AND
                Apache-2.0 AND
                BSD-2-Clause AND
                BSD-3-Clause AND
                BSL-1.0 AND
                CC-BY-4.0 AND
                CC0-1.0 AND
                MIT AND
                Unlicense AND
                Zlib}
# For a per-file license breakdown see LicenseBreakdown.


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

# VIT-compatible SLAM plugin
Requires:       basalt-monado
Requires:       openxr

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
  -DDRIVER_HANDTRACKING:BOOL=ON \

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

# Configure to use the DSO linker for the runtime
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Unversioned_shared_objects/
install -m 0755 -vd %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf


%check
cd %{_vpath_builddir}
# tests_comp_client_vulkan requires a Vulkan device (no GPU in mock).
# tests_comp_client_opengl requires a live display / GLX context.
# All other tests are headless and run cleanly.
ctest --output-on-failure \
      --exclude-regex '^tests_comp_client_(vulkan|opengl)$'

%post
%systemd_user_post monado.service monado.socket

%preun
%systemd_user_preun monado.service monado.socket

%postun
%systemd_user_postun_with_restart monado.service

%files
%license LICENSE LICENSES/*
%doc CONTRIBUTING.md README.md doc/*.md
%caps(cap_sys_nice=eip) %{_bindir}/monado-service
%{_bindir}/monado-cli
%{_bindir}/monado-ctl
%{_bindir}/monado-gui
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libmonado.so.25
%{_libdir}/%{name}/libmonado.so.25.1.0
%{_libdir}/%{name}/libopenxr_monado.so
%{_libdir}/steamvr-monado/
%{_userunitdir}/monado.service
%{_userunitdir}/monado.socket
%{_datadir}/openxr/1/openxr_monado.json
%dir %{_datadir}/steamvr-monado
%{_datadir}/steamvr-monado/*
%dir %{_datadir}/st-openvr
%{_datadir}/st-openvr/*
%{_sysconfdir}/ld.so.conf.d/%{name}.conf


%files devel
%{_libdir}/%{name}/libmonado.so
%dir %{_includedir}/monado
%{_includedir}/monado/monado.h


%changelog
%autochangelog
