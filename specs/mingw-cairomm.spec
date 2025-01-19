%?mingw_package_header

Name:           mingw-cairomm
Version:        1.12.0
Release:        24%{?dist}
Summary:        MinGW Windows C++ API for the cairo graphics library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.cairographics.org
Source0:        http://www.cairographics.org/releases/cairomm-%{version}.tar.gz
Patch0:         0001-Fix-the-build-with-MinGW-headers.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-libsigc++20
BuildRequires:  mingw64-libsigc++20

%description
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the 
Standard Template Library where it makes sense.


# Win32
%package -n mingw32-cairomm
Summary:        MinGW Windows C++ API for the cairo graphics library

%description -n mingw32-cairomm
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the
Standard Template Library where it makes sense.

%package -n mingw32-cairomm-static
Summary:        Static cross compiled version of the cairomm library
Requires:       mingw32-cairomm = %{version}-%{release}

%description -n mingw32-cairomm-static
Static cross compiled version of the cairomm library.

%package -n mingw64-cairomm
Summary:        MinGW Windows C++ API for the cairo graphics library

%description -n mingw64-cairomm
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the
Standard Template Library where it makes sense.

%package -n mingw64-cairomm-static
Summary:        Static cross compiled version of the cairomm library
Requires:       mingw64-cairomm = %{version}-%{release}

%description -n mingw64-cairomm-static
Static cross compiled version of the cairomm library.


%?mingw_debug_package


%prep
%setup -q -n cairomm-%{version}
%patch -P0 -p1


%build
export lt_cv_deplibs_check_method="pass_all"
%mingw_configure --enable-static --disable-documentation
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/{devhelp,doc}
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/{devhelp,doc}
rm $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm $RPM_BUILD_ROOT%{mingw64_libdir}/*.la


# Win32
%files -n mingw32-cairomm
%license COPYING
%{mingw32_bindir}/libcairomm-1.0-1.dll
%{mingw32_libdir}/libcairomm-1.0.dll.a
%{mingw32_libdir}/pkgconfig/cairomm-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-ft-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-pdf-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-png-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-ps-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-svg-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-win32-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-win32-font-1.0.pc
%{mingw32_includedir}/cairomm-1.0
%{mingw32_libdir}/cairomm-1.0/

%files -n mingw32-cairomm-static
%{mingw32_libdir}/libcairomm-1.0.a

# Win64
%files -n mingw64-cairomm
%license COPYING
%{mingw64_bindir}/libcairomm-1.0-1.dll
%{mingw64_libdir}/libcairomm-1.0.dll.a
%{mingw64_libdir}/pkgconfig/cairomm-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-ft-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-pdf-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-png-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-ps-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-svg-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-win32-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-win32-font-1.0.pc
%{mingw64_includedir}/cairomm-1.0
%{mingw64_libdir}/cairomm-1.0/

%files -n mingw64-cairomm-static
%{mingw64_libdir}/libcairomm-1.0.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.12.0-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.12.0-16
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.12.0-10
- Bump release

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.12.0-9
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 1.12.0-1
- Update to 1.12.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Kalev Lember <kalevlember@gmail.com> - 1.10.0-13
- Rebuild against latest mingw-gcc

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 1.10.0-12
- Use license macro for the COPYING file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.0-9
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr  8 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.0-7
- Added -static subpackage
- Cleaned up unneeded %%global tags

* Thu Mar 15 2012 Kalev Lember <kalevlember@gmail.com> - 1.10.0-6
- Build 64 bit Windows binaries

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.0-5
- Renamed the source package to mingw-cairomm (RHBZ #800848)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10.0-4
- Rebuild against the mingw-w64 toolchain
- Fix filelist (the cairo-ft backend is now enabled)

* Tue Jan 31 2012 Kalev Lember <kalevlember@gmail.com> - 1.10.0-3
- Rebuilt for libpng 1.5
- Remove .la files

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Kalev Lember <kalevlember@gmail.com> - 1.10.0-1
- Update to 1.10.0
- Use automatic mingw dep extraction
- Clean up the spec file for recent rpmbuild

* Sat May 21 2011 Kalev Lember <kalev@smartlink.ee> - 1.9.8-2
- Own _mingw32_libdir/cairomm-1.0/ directory

* Tue Feb 22 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.9.8-1
- update to 1.9.8 to match native

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.9.2-1
- update to 1.9.2 to match native

* Sat Dec  5 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.8.4-1
- update to 1.8.44

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.8.0-3
- add debuginfo packages

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.8.0-2
- replace %%define with %%global

* Wed Mar 25 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.8.0-1
- update to 1.8.0

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.6.2-5
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 1.6.2-4
- Include license.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.6.2-3
- Use _smp_mflags.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.6.2-2
- Initial RPM release.
