%global tarball xf86-video-ati
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers

%undefine _hardened_build

Summary:   Xorg X11 ati video driver
Name:      xorg-x11-drv-ati
Version:   22.0.0
Release:   4%{?dist}
URL:       http://www.x.org
License:   MIT

Source0:   https://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.xz

ExcludeArch: s390 s390x

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(gbm) >= 10.6
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm) >= 2.4.89
BuildRequires:  pkgconfig(libdrm_radeon)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xorg-server) >= 1.16

Requires: libdrm >= 2.4.89
Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description 
X.Org X11 ati video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
autoreconf -iv
%configure --disable-static --enable-glamor
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%files
%{driverdir}/ati_drv.so
%{driverdir}/radeon_drv.so
%{_mandir}/man4/ati.4*
%{_mandir}/man4/radeon.4*
%{_datadir}/X11/xorg.conf.d/10-radeon.conf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 22.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 29 2024 Simone Caronni <negativo17@gmail.com> - 22.0.0-3
- Clean up SPEC file.
- Adjust build requirement.
- Trim changelog.

* Fri Sep 27 2024 Sérgio Basto <sergio@serjux.com> - 22.0.0-2
- Rebuild for rebase of xorg-server to versions 21.1.x

* Tue Sep 10 2024 Sérgio Basto <sergio@serjux.com> - 22.0.0-1
- Update xorg-x11-drv-ati to 22.0.0

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
