%global tarball xf86-video-amdgpu
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers

# Xorg cannot load hardened build
%undefine _hardened_build

Name:       xorg-x11-drv-amdgpu
Version:    25.0.0
Release:    2%{?dist}

Summary:    AMD GPU video driver
License:    MIT

URL:        https://www.x.org/wiki
Source:     https://www.x.org/archive/individual/driver/%{tarball}-%{version}.tar.xz
Source:     https://www.x.org/archive/individual/driver/%{tarball}-%{version}.tar.xz.sig
Source:     0xF1111E4AAF984C9763795FFE4B25B5180522B8D9.gpg

ExcludeArch: s390 s390x

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  kernel-headers
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm) >= 2.4.121
BuildRequires:  pkgconfig(libdrm_amdgpu) >= 2.4.121
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xorg-server) >= 1.18
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto) >= 7.0.99.1
BuildRequires:  xorg-x11-util-macros

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires: libdrm >= 2.4.121

%description
X.Org X11 AMDGPU driver

%prep
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%autosetup -p1 -n %{tarball}-%{version}

%build
%meson \
    -D glamor=enabled \
    -D udev=enabled \

%meson_build

%install
%meson_install

%files
%{driverdir}/amdgpu_drv.so
%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
%{_mandir}/man4/amdgpu.4*

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 25.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Aug 15 2025 Dominik Mierzejewski <dominik@greysector.net> - 25.0.0-1
- Update to 25.0.0 (resolves rhbz#2384262)
- Download and validate GPG signature
- Switch to meson build system

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

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
