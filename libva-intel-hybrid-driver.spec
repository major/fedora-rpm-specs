Name:           libva-intel-hybrid-driver
Version:        1.0.2
Release:        %autorelease
Summary:        VA driver for Intel G45 & HD Graphics family

# Everything under MIT, except vp9hdec/intel_hybrid_hostvld_vp9*, 
# vp9hdec/decode_hybrid_vp9.cpp, src/media_drv_kernels*, 
# src/vp9hdec/intel_hybrid_vp9_kernel under BSD
# and src/wayland-drm-client-protocol.h, src/wayland/wayland-drm.xml
# under NTP
License:        MIT and BSD and NTP
URL:            https://github.com/01org/intel-hybrid-driver
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Build script uses obsolete macro AC_PROG_LIBTOOL, replace it with LT_INIT
Patch0:         libva-intel-hybrid-driver-1.0.2_replace_obsolete_AC_PROG_LIBTOOL.patch
Patch1:         Update-the-dependency-to-libva-2.0.patch
# Fixes https://github.com/01org/intel-hybrid-driver/issues/25 and RHBZ#1567582
# https://patch-diff.githubusercontent.com/raw/01org/intel-hybrid-driver/pull/26
Patch2:         libva-intel-hybrid-driver-1.0.2-load_libva-x11_for_any_ABI_version.patch
# https://github.com/intel/intel-hybrid-driver/issues/27
Patch3:         0001-Mark-global-variables-as-extern.patch

#obviously only for intel platform
ExclusiveArch:  %{ix86} x86_64 ia64

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(libdrm) >= 2.4.45
BuildRequires:  pkgconfig(libva) >= 1.0.0
BuildRequires:  pkgconfig(libcmrt) >= 0.10.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires: make


%description
libva-intel-hybrid-driver is the VA-API implementation for Intel G45 chipsets
and Intel HD Graphics for Intel Core processor family.

It allows to accelerate VP9 videos on Skylake and Kabylake architectures.


%prep
%autosetup -p1 -n intel-hybrid-driver-%{version}


%build
autoreconf -vif
%configure
%make_build


%install
%make_install 
find %{buildroot} -name "*.la" -delete


%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/dri/hybrid_drv_video.so


%changelog
%autochangelog
