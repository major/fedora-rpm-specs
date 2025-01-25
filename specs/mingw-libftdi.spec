%?mingw_package_header

%global name1 libftdi
Name:           mingw-%{name1}
Version:        1.5
Release:        1%{?dist}
Summary:        MinGW library to program and control the FTDI USB controller

# Automatically converted from old format: LGPLv2 and GPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2 AND GPL-2.0-only
URL:            https://www.intra2net.com/en/developer/libftdi/
Source0:        https://www.intra2net.com/en/developer/%{name1}/download/%{name1}1-%{version}.tar.bz2
# http://developer.intra2net.com/git/?p=libftdi;a=commitdiff;h=cdb28383402d248dbc6062f4391b038375c52385;hp=5c2c58e03ea999534e8cb64906c8ae8b15536c30
Patch0:         libftdi-1.5-fix_pkgconfig_path.patch
# http://developer.intra2net.com/mailarchive/html/libftdi/2023/msg00003.html
Patch1:         libftdi-1.5-no-distutils.patch
# http://developer.intra2net.com/mailarchive/html/libftdi/2023/msg00005.html
Patch2:         libftdi-1.5-cmake-deps.patch
# Fix for SWIG 4.3.0
# https://bugzilla.redhat.com/show_bug.cgi?id=2319133
# http://developer.intra2net.com/mailarchive/html/libftdi/2024/msg00024.html
Patch3:         libftdi-1.5-swig-4.3.patch
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-boost
BuildRequires:  mingw32-libusbx
BuildRequires:  mingw32-libconfuse
BuildRequires:  mingw64-boost
BuildRequires:  mingw64-libusbx
BuildRequires:  mingw64-libconfuse
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  swig

%description
A library (using libusb) to talk to FTDI's FT2232C,
FT232BM and FT245BM type chips including the popular bitbang mode.

%package -n mingw32-%{name1}
Summary:        MinGW library to program and control the FTDI USB controller

%description -n mingw32-%{name1}
A library (using libusb) to talk to FTDI's FT2232C,
FT232BM and FT245BM type chips including the popular bitbang mode.

%package -n mingw64-%{name1}
Summary:        MinGW library to program and control the FTDI USB controller

%description -n mingw64-%{name1}
A library (using libusb) to talk to FTDI's FT2232C,
FT232BM and FT245BM type chips including the popular bitbang mode.

%{?mingw_debug_package}

%prep
%autosetup -p1 -n %{name1}1-%{version}


%build
%mingw_cmake -DSTATICLIBS=off -DFTDIPP=on -DPYTHON_BINDINGS=off -DDOCUMENTATION=on -DEXAMPLES=off .

%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT/%{mingw32_libdir}/{libftdi1.a,libftdipp1.a}
rm -f $RPM_BUILD_ROOT/%{mingw64_libdir}/{libftdi1.a,libftdipp1.a}
rm -f $RPM_BUILD_ROOT/%{mingw32_datadir}/doc/libftdi1/example.conf
rm -f $RPM_BUILD_ROOT/%{mingw64_datadir}/doc/libftdi1/example.conf
rm -rf $RPM_BUILD_ROOT/build_win32/doc/html
rm -rf $RPM_BUILD_ROOT/build_win64/doc/html
rm -rf $RPM_BUILD_ROOT/build_win32/examples
rm -rf $RPM_BUILD_ROOT/build_win64/examples


%files -n mingw32-%{name1}
%license COPYING.LIB COPYING.GPL LICENSE
%doc AUTHORS ChangeLog README
%{mingw32_bindir}/ftdi_eeprom.exe      
%{mingw32_bindir}/libftdi1-config
%{mingw32_bindir}/libftdi1.dll
%{mingw32_bindir}/libftdipp1.dll
%{mingw32_includedir}/libftdi1
%{mingw32_libdir}/libftdi1.dll.a
%{mingw32_libdir}/libftdipp1.dll.a
%{mingw32_libdir}/cmake/libftdi1
%{mingw32_libdir}/pkgconfig/libftdi1.pc
%{mingw32_libdir}/pkgconfig/libftdipp1.pc

%files -n mingw64-%{name1}
%license COPYING.LIB COPYING.GPL LICENSE
%doc AUTHORS ChangeLog README
%{mingw64_bindir}/ftdi_eeprom.exe      
%{mingw64_bindir}/libftdi1-config
%{mingw64_bindir}/libftdi1.dll
%{mingw64_bindir}/libftdipp1.dll
%{mingw64_includedir}/libftdi1
%{mingw64_libdir}/libftdi1.dll.a
%{mingw64_libdir}/libftdipp1.dll.a
%{mingw64_libdir}/cmake/libftdi1
%{mingw64_libdir}/pkgconfig/libftdi1.pc
%{mingw64_libdir}/pkgconfig/libftdipp1.pc

%changelog
* Thu Jan 23 2025 Thomas Sailer <fedora@tsailer.ch> - 1.5-1
- update to 1.5

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Thomas Sailer <fedora@tsailer.ch> - 1.4-12
- Fix build

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.4-6
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 02 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.4-1
- update to 1.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.3-8
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 06 2017 Thomas Sailer <thomas.sailer@axsem.com> - 1.3-3
- fix license tag

* Fri Oct 06 2017 Thomas Sailer <thomas.sailer@axsem.com> - 1.3-2
- drop example and documentation
- properly include license files
- modernize spec files, remove obsolete constructs

* Wed Jan 25 2017 Thomas Sailer <thomas.sailer@axsem.com> - 1.3-1
- Initial Specfile
