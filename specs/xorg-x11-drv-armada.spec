%global _configure_disable_silent_rules 1

# Hardening passws '-z now' to the linker, defeating lazy binding via PLT.
# Xorg's module loading, however, relies on loading modules with unresolved
# symbols that in turn dlopen their own dependencies (such as fb or
# etnadrm_gpu modules). Sigh.
%undefine _hardened_build

Name:           xorg-x11-drv-armada
# This is the version from the configure script.
Version:        0.0.0
# Built from unstable-devel branch that has the etnadrm backend
Release:        15.unstable.20180829git78e7116a5%{?dist}
Summary:        X.org graphics driver for KMS based systems with pluggable GPU backend

License:        MIT
URL:            http://git.arm.linux.org.uk/cgit/xf86-video-armada.git/

# git clone http://git.arm.linux.org.uk/cgit/xf86-video-armada.git/
# cd xf86-video-armada
# git archive --prefix=xf86-video-armada-0.0.0/ 78e7116a5 |
#    gzip -9 >xf86-video-armada-0.0.0.tar.gz
Source0:        xf86-video-armada-%{version}.tar.gz

# These were all sent to the upstream maintainer on 2019-03-26.
Patch0:         0001-all-add-the-missing-files-into-the-dist.patch
Patch1:         0002-build-default-to-enable-etnaviv-auto.patch
Patch2:         0003-build-fix-enable-etnadrm-handling.patch
Patch3:         0004-build-align-a-couple-of-configure-options-with-their.patch
Patch4:         0005-build-fix-present.h-detection.patch

BuildRequires:  gcc make
BuildRequires:  autoconf automake libtool

BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xorg-server) >= 1.9.99.1
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm) >= 2.4.47
BuildRequires:  pkgconfig(libdrm_armada) => 2.0.0
BuildRequires:  pkgconfig(dri2proto) >= 2.6
BuildRequires:  pkgconfig(dri3proto) >= 1.0
BuildRequires:  pkgconfig(presentproto) >= 1.0
BuildRequires:  etnaviv-headers

%description
The xf86-video-armada module is a 2D graphics driver for the X Window
System as implemented by X.org, supporting Freescale i.MX or Marvell Armada
display controllers with a Vivante Galcore GPU.


%prep
%setup -q -n xf86-video-armada-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1


%build
autoreconf -fi
%configure \
        --disable-vivante \
        --disable-etnaviv \
        --enable-etnadrm \
        --enable-dri2 \
        --enable-dri3 \
        --enable-present
make %{?_smp_mflags}


%install
%make_install


%files
%exclude %{_libdir}/xorg/modules/drivers/armada_drv.la
%exclude %{_libdir}/xorg/modules/drivers/etnadrm_gpu.la
%{_libdir}/xorg/modules/drivers/armada_drv.so
%{_libdir}/xorg/modules/drivers/etnadrm_gpu.so
%{_mandir}/man4/armada.4*
%license COPYING
%doc README FAQ
%doc conf/xorg-sample.conf


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-15.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-14.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 Lubomir Rintel <lkundrak@v3.sk> - 0.0.0-13.unstable.20180829git78e7116a5
- Fix build

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-12.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-11.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-10.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-9.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-8.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-7.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-6.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-5.unstable.20180829git78e7116a5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-4.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-3.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-2.unstable.20180829git78e7116a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.0.0-1.unstable.20180829git78e7116a5
- Initial packaging
