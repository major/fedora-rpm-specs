%{?mingw_package_header}

Name:           mingw-libusbx
Version:        1.0.24
Release:        13%{?dist}
Summary:        MinGW library which allows userspace access to USB devices

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://libusb.info
Source0:        https://github.com/libusb/libusb/releases/download/v%{version}/libusb-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc


%description
This package provides a way for applications to access USB devices.

%package -n mingw32-libusbx
Summary:        MinGW library which allows userspace access to USB devices
Requires:       pkgconfig

%description -n mingw32-libusbx
This package contains the header files and libraries needed to develop
applications that use libusbx.

%package -n mingw32-libusbx-static
Summary:        MinGW static library which allows userspace access to USB devices
Requires:       mingw32-libusbx = %{version}-%{release}

%description -n mingw32-libusbx-static 
This package contains the static libraries needed to develop
applications that use libusbx.

%package -n mingw64-libusbx
Summary:        MinGW library which allows userspace access to USB devices
Requires:       pkgconfig

%description -n mingw64-libusbx
This package contains the header files and libraries needed to develop
applications that use libusbx.

%package -n mingw64-libusbx-static
Summary:        MinGW static library which allows userspace access to USB devices
Requires:       mingw64-libusbx = %{version}-%{release}

%description -n mingw64-libusbx-static
This package contains the static libraries needed to develop
applications that use libusbx.

%{?mingw_debug_package}


%prep
%setup -q -n libusb-%{version}


%build
%mingw_configure
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete


%files -n mingw32-libusbx
%doc AUTHORS COPYING README NEWS
%{mingw32_bindir}/libusb-1.0.dll
%{mingw32_includedir}/libusb-1.0/
%{mingw32_libdir}/libusb-1.0.dll.a
%{mingw32_libdir}/pkgconfig/libusb-1.0.pc

%files -n mingw32-libusbx-static
%{mingw32_libdir}/libusb-1.0.a

%files -n mingw64-libusbx
%doc AUTHORS COPYING README NEWS
%{mingw64_bindir}/libusb-1.0.dll
%{mingw64_includedir}/libusb-1.0/
%{mingw64_libdir}/libusb-1.0.dll.a
%{mingw64_libdir}/pkgconfig/libusb-1.0.pc

%files -n mingw64-libusbx-static
%{mingw64_libdir}/libusb-1.0.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.24-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.0.24-5
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep  7 2021 Daniel P. Berrangé <berrange@redhat.com> - 1.0.24-3
- Update URL to point to a working website

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 11 2021 Victor Toso <victortoso@redhat.com> - 1.0.24-1
- Update to 1.0.24

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.0.22-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Victor Toso <victortoso@redhat.com> - 1.0.22-1
- Update to 1.0.22

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Pavel Grunt <pgrunt@redhat.com> - 1.0.21-1
- Update to 1.0.21 and enable UsbDk

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 19 2014 Richard Hughes <richard@hughsie.com> - 1.0.19-1
- Update to 1.0.19

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.0.15-1
- Updated to match with f19. rhbz#974701

* Mon May 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.12-2
- Bump to fix broken upgrade path from f17 to f18

* Sun Nov 18 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.0.12-1
- Update to upstream 1.0.12

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.0.9-1
- Initial packaging
