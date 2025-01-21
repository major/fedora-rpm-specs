%define tarball xf86-video-nouveau
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir %{moduledir}/drivers

%undefine _hardened_build

Summary:   Xorg X11 nouveau video driver for NVIDIA graphics chipsets
Name:      xorg-x11-drv-nouveau
# need to set an epoch to get version number in sync with upstream
Epoch:     1
Version:   1.0.17
Release:   12%{?dist}
URL:       http://www.x.org
License:   MIT

Source0: http://xorg.freedesktop.org/archive/individual/driver/xf86-video-nouveau-%{version}.tar.bz2

Patch1: remove-sarea.h.patch
# fixup driver for new X server ABI
Patch2: e80e73ced69b15662103d0fd6837db4ce6c6eb5b.patch
Patch3: 0001-Fixes-warning-nv_driver.c-1443-9-warning-implicit.patch

ExcludeArch: s390 s390x

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  mesa-libGL-devel
BuildRequires:  pkgconfig(xorg-server) >= 1.8
BuildRequires:  pkgconfig(libdrm) >= 2.4.60
BuildRequires:  pkgconfig(libdrm_nouveau) >= 2.4.25
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(libudev)

Requires:   Xorg %(xserver-sdk-abi-requires ansic)
Requires:   Xorg %(xserver-sdk-abi-requires videodrv)
Requires:   libdrm >= 2.4.33-0.1

%description 
X.Org X11 nouveau video driver.

%prep
%autosetup -p1 -n xf86-video-nouveau-%{version}

%build
autoreconf -v --install --force
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%files
%{driverdir}/nouveau_drv.so
%{_mandir}/man4/nouveau.4*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 29 2024 Simone Caronni <negativo17@gmail.com> - 1:1.0.17-11
- Clean up SPEC file.
- Trim changelog.

* Fri Sep 27 2024 Sérgio Basto <sergio@serjux.com> - 1:1.0.17-10
- Rebuild for rebase of xorg-server to versions 21.1.x

* Sun Sep 22 2024 Sérgio Basto <sergio@serjux.com> - 1:1.0.17-9
- Add compability with X11-server-21.1.x

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
