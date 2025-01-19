%{?mingw_package_header}

%global vday 02
%global vmonth 12
%global vyear 2004
%global name1 zfstream

Name:           mingw-%{name1}
Version:        %{vyear}%{vmonth}%{vday}
Release:        45%{?dist}
Summary:        MinGW Windows abstraction API for reading and writing compressed files

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.wanderinghorse.net/computing/%{name1}/
Source0:        http://www.wanderinghorse.net/computing/%{name1}/libs11n_%{name1}-%{vyear}.%{vmonth}.%{vday}.tar.gz
# I tried half a day to get the rather peculiar original build system working,
# but I failed, so I decided to simply replace it by autotools.
# This has the further advantage that it knows how to cross-compile.
Source1:        %{name1}-autotools.tar.gz
# The patch has been sent via private mail to the author. The author responded
# that the patch had been integrated into his personal tree, but apparently
# he has not gotten around to release a new version.
Patch1:         %{name1}-zip.patch
# Fix build against minizip-3.0.7
Patch2:         %{name1}-minizip.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
BuildRequires:  mingw32-minizip
BuildRequires:  mingw64-minizip
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw64-pkg-config

%description
MinGW zfstream C++ compressed I/O abstraction library

#Mingw32
%package -n mingw32-%{name1}
Summary:        MinGW Windows abstraction API for reading and writing compressed files

%description -n mingw32-%{name1}
MinGW zfstream C++ compressed I/O abstraction library

#Mingw64
%package -n mingw64-%{name1}
Summary:        MinGW Windows abstraction API for reading and writing compressed files

%description -n mingw64-%{name1}
MinGW zfstream C++ compressed I/O abstraction library

%{?mingw_debug_package}

%prep
%setup -q -n libs11n_%{name1}-%{vyear}.%{vmonth}.%{vday} -a 1
%patch -P1 -p0 -b .zip
%patch -P2 -p1
touch NEWS README AUTHORS
aclocal
autoconf
autoheader
libtoolize -f
automake -a -c

%build
%{mingw_configure} --disable-static
%{mingw_make} %{?_smp_mflags}


%install
%{mingw_make} install DESTDIR=$RPM_BUILD_ROOT

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


%files -n mingw32-%{name1}
%doc LICENSE
%{mingw32_bindir}/libzfstream-0.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libzfstream.dll.a
%{mingw32_libdir}/pkgconfig/zfstream.pc

%files -n mingw64-%{name1}
%doc LICENSE
%{mingw64_bindir}/libzfstream-0.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libzfstream.dll.a
%{mingw64_libdir}/pkgconfig/zfstream.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 20041202-44
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Sandro Mani <manisandro@gmail.com> - 20041202-38
- Rebuild (mingw-minizip)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 20041202-36
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 10 2021 Sandro Mani <manisandro@gmail.com> - 20041202-33
- Rebuild (minizip)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 23:14:28 CET 2020 Sandro Mani <manisandro@gmail.com> - 20041202-31
- Rebuild (minizip)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 20041202-28
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-26
- add missing library to pkgconf file
- use pkgconf for zlib and bzip2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20041202-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 20041202-16
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Mon Aug 13 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-15
- enable mingw64 build

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 20041202-13
- Dropped .la files

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 20041202-12
- Renamed the source package to mingw-zfstream (#801040)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 20041202-11
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 20041202-9
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20041202-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-6
- add debuginfo packages

* Fri May 15 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-5
- add missing BR

* Fri May  1 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-4
- incorporate changes from native review

* Mon Mar 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-3
- unfiy main and devel subpackages

* Mon Mar 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20041202-2
- copy from native package
