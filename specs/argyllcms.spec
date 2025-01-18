# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
%undefine _include_frame_pointers

Name: argyllcms
Version: 3.3.0
Release: 2%{?dist}

# Main code - AGPL-3.0-or-later
# spectro, xml - GPL-2.0-or-later
# xicc - GPL-3.0-or-later
# cgats, icc - MIT
# documentation - GFDL-1.3-or-later
License: AGPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later AND MIT AND GFDL-1.3-or-later
Summary: ICC compatible color management system
URL: https://www.argyllcms.com
Source0: %{url}/Argyll_V%{version}_src.zip#/%{name}-%{version}.zip

BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(zlib)

BuildRequires: gcc
BuildRequires: jam

Requires: %{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description
The Argyll color management system supports accurate ICC profile creation for
acquisition devices, CMYK printers, film recorders and calibration and profiling
of displays.

Spectral sample data is supported, allowing a selection of illuminants observer
types, and paper fluorescent whitener additive compensation. Profiles can also
incorporate source specific gamut mappings for perceptual and saturation
intents. Gamut mapping and profile linking uses the CIECAM02 appearance model,
a unique gamut mapping algorithm, and a wide selection of rendering intents. It
also includes code for the fastest portable 8 bit raster color conversion
engine available anywhere, as well as support for fast, fully accurate 16 bit
conversion. Device color gamuts can also be viewed and compared using a VRML
viewer.

%package doc
Summary: Argyll CMS documentation
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description doc
The Argyll color management system supports accurate ICC profile creation for
acquisition devices, CMYK printers, film recorders and calibration and profiling
of displays.

This package contains the Argyll color management system documentation.

%package data
Summary: Argyll CMS assets
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: color-filesystem

%description data
The Argyll color management system supports accurate ICC profile creation for
acquisition devices, CMYK printers, film recorders and calibration and profiling
of displays.

This package contains the Argyll color management system assets.

%prep
%autosetup -p1 -n Argyll_V%{version}

# Exporting correct build flags...
echo "CCFLAGS += \${CFLAGS} -std=gnu89 -fcommon -fPIC -fno-strict-aliasing ;" >> Jamtop
echo "LINKFLAGS += \${LDFLAGS} ;" >> Jamtop

# Unbundling libraries...
rm -rf jpeg png tiff usb zlib

# Removing executable flag from files...
find -type f -name '*.txt' -exec chmod -x '{}' \;
find doc -type f -exec chmod -x '{}' \;
find doc -type f -name '*.htm*' -exec sed -ie 's,\r,,' '{}' \;

%build
%set_build_flags
jam -fJambase %{?_smp_mflags} -sPREFIX=%{_prefix} -sDESTDIR=%{buildroot} -sREFSUBDIR=share/color/argyll/ref all

%install
jam -fJambase -sPREFIX=%{_prefix} -sDESTDIR=%{buildroot} -sREFSUBDIR=share/color/argyll/ref install
rm -f %{buildroot}/%{_bindir}/*.txt

%files
%license License*.txt
%doc log.txt ReadMe.txt
%{_bindir}/applycal
%{_bindir}/average
%{_bindir}/cb2ti3
%{_bindir}/cctiff
%{_bindir}/ccxxmake
%{_bindir}/chartread
%{_bindir}/collink
%{_bindir}/colprof
%{_bindir}/colverify
%{_bindir}/cxf2ti3
%{_bindir}/dispcal
%{_bindir}/dispread
%{_bindir}/dispwin
%{_bindir}/extracticc
%{_bindir}/extractttag
%{_bindir}/fakeCMY
%{_bindir}/fakeread
%{_bindir}/greytiff
%{_bindir}/iccdump
%{_bindir}/iccgamut
%{_bindir}/icclu
%{_bindir}/iccvcgt
%{_bindir}/illumread
%{_bindir}/invprofcheck
%{_bindir}/kodak2ti3
%{_bindir}/ls2ti3
%{_bindir}/mppcheck
%{_bindir}/mpplu
%{_bindir}/mppprof
%{_bindir}/oeminst
%{_bindir}/printcal
%{_bindir}/printtarg
%{_bindir}/profcheck
%{_bindir}/refine
%{_bindir}/revfix
%{_bindir}/scanin
%{_bindir}/spec2cie
%{_bindir}/specplot
%{_bindir}/splitti3
%{_bindir}/spotread
%{_bindir}/synthcal
%{_bindir}/synthread
%{_bindir}/targen
%{_bindir}/tiffgamut
%{_bindir}/timage
%{_bindir}/txt2ti3
%{_bindir}/viewgam
%{_bindir}/xicclu

%files doc
%license doc/DocLicense.txt
%doc doc/*.html doc/*.jpg doc/SG*.txt
%doc doc/ccmxs doc/ccsss

%files data
%{_datadir}/color/argyll/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 27 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.3.0-1
- 3.3.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 18 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.2.0-1
- 3.2.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.1.0-1
- 3.1.0

* Mon Oct 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.2-1
- 3.0.2

* Thu Oct 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.1-1
- 3.0.1

* Tue Sep 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.0-1
- 3.0.0

* Thu Aug 31 2023 Florian Weimer <fweimer@redhat.com> - 2.3.1-6
- Avoid build failure with future toolchain defaults

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 29 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.3.1-4
- Rebuilt without frame pointers to mitigate crashes in dependent packages.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.3.1-1
- Updated to version 2.3.1.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.3.0-1
- Updated to version 2.3.0.

* Thu Sep 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 2.2.1-1
- 2.2.1

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.2.0-2
- Rebuilt with OpenSSL 3.0.0

* Sun Aug 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.0-1
- Updated to version 2.2.0.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.9.2-11
- Added data subpackage. Fixed minor issues with dependencies.

* Sat Oct 17 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.9.2-10
- Resurrected package. Fixed build under Fedora 33+.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 19 2016 Richard Hughes <rhughes@redhat.com> - 1.9.2-1
- Update to 1.9.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Richard Hughes <rhughes@redhat.com> - 1.8.3-1
- Update to 1.8.3

* Mon Sep 07 2015 Richard Hughes <rhughes@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Richard Hughes <rhughes@redhat.com> - 1.7.0-1
- Update to 1.7.0
- Add better cross compatibility with non-Argyll ICC profiles
- Added a dispread & fakeread -Z option to set the number of bits to quantize
- Added a -P prune option to profcheck
- Added dispcal and collink -b black point hack
- Added histogram plot option -h to both profcheck and verify.
- Added IRIDAS .cube 3DLut format support to collink
- Added preset list of display techologies to select from in ccxxmake.
- Add support for DataColor Spyder 5.
- Add support for Klein K10-A colorimeter.
- Add X3D and X3DOM support as an alternative to VRML
- Fix various instrument communications problems for DTP20, DTP92 & DTP94
- Fix very major bug in illumread
- Ignore any patches that have zero values for creating Display profiles
- Improved gamut mapping to reduce unnecessary changes to less saturated colors

* Fri Oct 24 2014 Richard Hughes <rhughes@redhat.com> - 1.6.3-4
- Add experimental ColorHug2 driver, which has already been sent upstream.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 02 2014 Richard Hughes <rhughes@redhat.com> - 1.6.3-1
- Update to 1.6.3
- Added code to minimize ICC rounding error white point accuracy
- Changed colprof to deal with variable grid distribution in a more neuanced way
- Changed colprof to used a power_like function for the grid distribution shape
- Changed i1d3 driver to completely ignore any EEPROM checksum errors
- Fix bug in xicclu -py conversion.
- Fixed bug in dispcal to use the final measurement pass for the calibration
- Fixed bug in spotread, dispcal & dispread for CCSS capable instruments
- Renamed verify to colverify to avoid clash with MSWin program of the same name
- Switch dispread to use NoClamp readings
- Tweaked dispcal to try and improve accuracy of black point calibration

* Tue Nov 26 2013 Richard Hughes <rhughes@redhat.com> - 1.6.2-1
- Update to 1.6.2
- Added "dark region emphasis" -V parameter to targen and colprof
- Changed i1d3 driver to be more forgiving of EEProm checksum calculation
- Fixed "edges don't match" bug in printarg when -iCM -h -s/-S used.
- Fixed bug in -H flag in chartread, dispcal, dispread, illumread & spotread
- Fixed bug in dispcal black point optimization to err on the black side
- Fixed bug introduced into ColorMunki (spectro) reflective measurement
- Fixed major bug in illumread - result was being corrupted.
- Fixed problem with TV encoded output and dispread -E -k/-K

* Mon Aug 19 2013 Richard Hughes <rhughes@redhat.com> - 1.6.0-1
- Update to 1.6.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Richard Hughes <rhughes@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.4.0-8
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.4.0-7
- rebuild against new libjpeg

* Wed Oct 24 2012 Richard Hughes <rhughes@redhat.com> - 1.4.0-6
- Drop 55-Argyll.rules, it's not required and we can rely on colord
  to provide the ENV{COLOR_MEASUREMENT_DEVICE}="1" without the
  plugdev group or invoking a usb-db instance for each USB device
  hotplug.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Jon Ciesla <limburgher@gmail.com> - 1.4.0-3
- Drop udev Requires.

* Mon May 07 2012 Jon Ciesla <limburgher@gmail.com> - 1.4.0-2
- Rebuild for new libtiff.

* Fri Apr 20 2012 Richard Hughes <rhughes@redhat.com> - 1.4.0-1
- Update to latest upstream release
- A colorimeter can now be used as a reference to make ccmx files
- Added dither/screening support for 8 bit output of render
- Added JPEG file support to cctiff, tiffgamut and extracticc
- Fixed double free in icc/icc.c for profiles that have duplicate tags
- Fix bugs in ColorMunki Transmissive measurement mode calibration.

* Mon Mar 19 2012 Richard Hughes <rhughes@redhat.com> - 1.3.7-1
- Update to 1.3.7
- Fix regression in Spyder support - ccmx files were not being handled

* Mon Mar 19 2012 Richard Hughes <rhughes@redhat.com> - 1.3.6-1
- Update to 1.3.6
- Add a -V option to spotread to allow tracking reading consistency.
- Add ColorHug support upstream (so distro patch removed).
- Add Spyder4 support.
- Add support for NEC SpectraSensor Pro version of the i1d3.
- Changed and expanded display selection to be instrument specific.

* Tue Feb 07 2012 Richard Hughes <rhughes@redhat.com> - 1.3.5-7
- Ship a shared library to reduce the installed package size from
  27.7Mb to 3.2Mb by removing 46 instances of static linking.

* Thu Jan 26 2012 Richard Hughes <rhughes@redhat.com> - 1.3.5-6
- Fix the ColorHug patch to not time out with firmware >= 1.1.1 and to
  correctly report negative numbers.
- Re-libtoolize to fix compile failure on rawhide.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
