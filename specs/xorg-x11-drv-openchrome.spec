%global commit0 857d892b668b4737d41ef1b7f58fd45eac84d552
%global date 20230328
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

%define tarball xf86-video-openchrome
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir %{moduledir}/drivers

%if 0%{?fedora}
%define with_xvmc 0
%else
%define with_xvmc 1
%endif

%undefine _hardened_build

Summary:        Xorg X11 openchrome video driver
Name:           xorg-x11-drv-openchrome
Version:        0.6.604%{!?tag:^%{date}git%{shortcommit0}}
Release:        2%{?dist}
URL:            http://www.freedesktop.org/wiki/Openchrome/
License:        MIT

%if 0%{?tag:1}
Source0:        http://xorg.freedesktop.org/archive/individual/driver/%{tarball}-%{version}.tar.bz2
%else
Source0:        %{tarball}-%{shortcommit0}.tar.bz2
%endif
Source1:        make-git-snapshot.sh

ExclusiveArch:  %{ix86} x86_64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  pkgconfig(libdrm) >= 2.2
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(xorg-server)
%if %{with_xvmc}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xvmc)
%endif

Requires:       Xorg %(xserver-sdk-abi-requires ansic)
Requires:       Xorg %(xserver-sdk-abi-requires videodrv)
Requires:       xorg-x11-server-wrapper

Obsoletes:      %{name}-devel < %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description
X.Org X11 openchrome video driver.

%prep
%if 0%{?tag:1}
%autosetup -p1 -n %{tarball}-%{version}
%else
%autosetup -p1 -n %{tarball}-%{commit0}
%endif

%build
autoreconf -vif
%configure --disable-static --enable-viaregtool
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete
# Remove unversioned XvMC libraries
rm -f %{buildroot}%{_libdir}/libchromeXvMC*.so

%files
%doc NEWS README
%license COPYING
%{driverdir}/openchrome_drv.so
%if %{with_xvmc}
%{_libdir}/libchromeXvMC.so.1
%{_libdir}/libchromeXvMC.so.1.0.0
%{_libdir}/libchromeXvMCPro.so.1
%{_libdir}/libchromeXvMCPro.so.1.0.0
%endif
%{_mandir}/man4/openchrome.4.gz
%{_sbindir}/via_regs_dump


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.604^20230328git857d892-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Simone Caronni <negativo17@gmail.com> - 0.6.604^20230328git857d892-1
- Update to latest snapshot.
- Clean up SPEC file.
- Trim changelog.
- Drop devel subpackage (no headers?).

* Fri Sep 27 2024 Sérgio Basto <sergio@serjux.com> - 0.6.400-9.20210215git5dbad06
- Rebuild for rebase of xorg-server to versions 21.1.x

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.400-8.20210215git5dbad06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.400-7.20210215git5dbad06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.400-6.20210215git5dbad06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.400-5.20210215git5dbad06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.400-4.20210215git5dbad06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.400-3.20210215git5dbad06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
