Name:           libva-intel-hybrid-driver
Version:        1.0.2
Release:        25%{?dist}
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
* Tue Mar 21 2023 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-25
- rebuilt

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 01:19:34 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-17
- Fix compatibility with GCC 10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-13
- Minor correction to the previous patch to find the correct library

* Wed Jun 27 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-12
- Add patch to fix #1567582

* Sun May 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-11
- Fix typo in License
- Fixes bug #1577586

* Wed Mar 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-10
- Add missing BR for gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-6
- Backport upstream patch

* Mon Jan 15 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.0.2-5
- Rebuilt for libva-2.0.0

* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.0.2-4
- Remove unneeded /sbin/ldconfig

* Tue Jul 25 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.0.2-3
- Added patch to replace the obsolete AC_PROG_LIBTOOL

* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.0.2-2
- Update to Fedora Packaging Guidelines specification

* Wed Jul 19 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.0.2-1
- First RPM release
