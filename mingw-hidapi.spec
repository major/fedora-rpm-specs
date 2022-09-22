%{?mingw_package_header}

%global nativename hidapi

Name:           mingw-%{nativename}
Version:        0.11.2
Release:        4%{?dist}
Summary:        Library for communicating with USB and Bluetooth HID devices

License:        GPLv3 or BSD
URL:            https://github.com/libusb/hidapi
Source0:        https://github.com/libusb/hidapi/archive/%{nativename}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

%description
HIDAPI is a multi-platform library which allows an application to interface
with USB and Bluetooth HID-class devices on Windows, Linux, FreeBSD and Mac OS
X.  On Linux, either the hidraw or the libusb back-end can be used. There are
trade-offs and the functionality supported is slightly different.


# Win32
%package -n mingw32-%{nativename}
Summary:        Library for communicating with USB and Bluetooth HID devices

%description -n mingw32-%{nativename}
HIDAPI is a multi-platform library which allows an application to interface
with USB and Bluetooth HID-class devices on Windows, Linux, FreeBSD and Mac OS
X.  On Linux, either the hidraw or the libusb back-end can be used. There are
trade-offs and the functionality supported is slightly different.

%package -n mingw32-%{nativename}-static
Summary:        Static libraries for mingw32-hidapi development
Requires:       mingw32-%{nativename} = %{version}-%{release}

%description -n mingw32-%{nativename}-static
The mingw32-hidapi-static package contains static library for mingw32-hidapi
development.


# Win64
%package -n mingw64-%{nativename}
Summary:        Library for communicating with USB and Bluetooth HID devices

%description -n mingw64-%{nativename}
HIDAPI is a multi-platform library which allows an application to interface
with USB and Bluetooth HID-class devices on Windows, Linux, FreeBSD and Mac OS
X.  On Linux, either the hidraw or the libusb back-end can be used. There are
trade-offs and the functionality supported is slightly different.

%package -n mingw64-%{nativename}-static
Summary:        Static libraries for mingw64-hidapi development
Requires:       mingw64-%{nativename} = %{version}-%{release}

%description -n mingw64-%{nativename}-static
The mingw64-hidapi-static package contains static library for mingw64-hidapi
development.


%{?mingw_debug_package}


%prep
%autosetup -n %{nativename}-%{nativename}-%{version}


%build
autoreconf -vif
%mingw_configure --disable-testgui
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=%{buildroot}

# Remove files we don't need
find %{buildroot} -name "*.la" -delete
rm -r %{buildroot}%{mingw32_datadir}/*
rm -r %{buildroot}%{mingw64_datadir}/*


%files -n mingw32-%{nativename}
%doc AUTHORS.txt README.md LICENSE*.txt
%{mingw32_bindir}/libhidapi-0.dll
%{mingw32_libdir}/libhidapi.dll.a
%{mingw32_libdir}/pkgconfig/hidapi.pc
%{mingw32_includedir}/hidapi

%files -n mingw32-%{nativename}-static
%{mingw32_libdir}/libhidapi.a

%files -n mingw64-%{nativename}
%doc AUTHORS.txt README.md LICENSE*.txt
%{mingw64_bindir}/libhidapi-0.dll
%{mingw64_libdir}/libhidapi.dll.a
%{mingw64_libdir}/pkgconfig/hidapi.pc
%{mingw64_includedir}/hidapi

%files -n mingw64-%{nativename}-static
%{mingw64_libdir}/libhidapi.a


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.11.2-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Scott Talbert <swt@techie.net> - 0.11.2-1
- Update to new upstream release 0.11.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 27 2021 Scott Talbert <swt@techie.net> - 0.10.1-2
- Fix FTBFS with autoconf 2.70 (#1943078)

* Sat Mar 27 2021 Scott Talbert <swt@techie.net> - 0.10.1-1
- Update to new upstream release 0.10.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Scott Talbert <swt@techie.net> - 0.10.0-1
- Update to new upstream release 0.10.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Scott Talbert <swt@techie.net> - 0.9.0-1
- Switch to new upstream at libusb organization

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.8.d17db57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.7.d17db57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.6.d17db57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.5.d17db57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.4.d17db57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.3.d17db57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.2.d17db57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 01 2015 Scott Talbert <swt@techie.net> - 0.8.0-0.1.d17db57
- Update to latest upstream commit d17db57
- Remove patch as it has been incorporated upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5.a88c724
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4.a88c724
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Scott Talbert <swt@techie.net> - 0.7.0-3.a88c724
- Add patch for increasing the input report buffer size

* Mon Nov 4 2013 Scott Talbert <swt@techie.net> - 0.7.0-2.a88c724
- Incorporate fixes from package review

* Tue Oct 22 2013 Scott Talbert <swt@techie.net> - 0.7.0-1.a88c724
- Initial packaging of mingw-hidapi library
