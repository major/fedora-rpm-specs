%global tarball xf86-video-vmware
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers

%undefine _hardened_build

Summary:    Xorg X11 vmware video driver
Name:       xorg-x11-drv-vmware
Version:    13.4.0
Release:    8%{?dist}
URL:        http://www.x.org
License:    MIT AND X11

Source0:    https://ftp.x.org/archive/individual/driver/%{tarball}-%{version}.tar.xz

ExclusiveArch: %{ix86} x86_64 ia64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libdrm) >= 2.4.96
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xatracker) >= 0.4.0
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-server) >= 1.12

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires: libxatracker >= 8.0.1-4

%description
X.Org X11 vmware video driver.

%prep
%autosetup -p1 -n %{tarball}-%{version}

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%files
%{driverdir}/vmware_drv.so
%{_mandir}/man4/vmware.4*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 13.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Simone Caronni <negativo17@gmail.com> - 13.4.0-7
- Clean up SPEC file.
- Trim changelog.

* Fri Sep 27 2024 Sérgio Basto <sergio@serjux.com> - 13.4.0-6
- Rebuild for rebase of xorg-server to versions 21.1.x

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 07 2023 José Expósito <jexposit@redhat.com> - 13.4.0-3
- SPDX Migration

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Peter Hutterer <peter.hutterer@redhat.com> - 13.4.0-1
- vmware 13.4.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Yaakov Selkowitz <yselkowi@redhat.com> - 13.3.0-1
- Update to 13.3.0 (#1579342, #2047133)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
