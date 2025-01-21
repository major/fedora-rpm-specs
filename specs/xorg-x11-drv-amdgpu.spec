%global tarball xf86-video-amdgpu
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers

# Xorg cannot load hardened build
%undefine _hardened_build

Name:       xorg-x11-drv-amdgpu
Version:    23.0.0
Release:    7%{?dist}

Summary:    AMD GPU video driver
License:    MIT

URL:        https://www.x.org/wiki
Source:     https://www.x.org/archive/individual/driver/%{tarball}-%{version}.tar.xz

ExcludeArch: s390 s390x

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  kernel-headers
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm) >= 2.4.89
BuildRequires:  pkgconfig(libdrm_amdgpu) >= 2.4.76
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xorg-server) >= 1.13
BuildRequires:  xorg-x11-util-macros

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires: libdrm >= 2.4.89

%description
X.Org X11 AMDGPU driver

%prep
%autosetup -p1 -n %{tarball}-%{version}

%build
autoreconf -fiv
%configure --disable-static --enable-glamor
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files
%{driverdir}/amdgpu_drv.so
%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
%{_mandir}/man4/amdgpu.4*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 27 2024 Simone Caronni <negativo17@gmail.com> - 23.0.0-6
- Clean up SPEC file.
- Trim changelog.
- Do not disable debug stripping (caught by rpminspect) tests.

* Fri Sep 27 2024 Sérgio Basto <sergio@serjux.com> - 23.0.0-5
- Rebuild for rebase of xorg-server to versions 21.1.x

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Christopher Atherton <atherchris@gmail.com> - 23.0.0-1
- Update to 23.0.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 14 2022 Christopher Atherton <atherchris@gmail.com> - 22.0.0-1
- Update to 22.0.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
