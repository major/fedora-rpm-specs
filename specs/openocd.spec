%global _legacy_common_support 1
#global rcVer 1

Name:       openocd
Version:    0.12.0
Release:    3%{?rcVer:.rc%{rcVer}}%{?dist}.5
Summary:    Debugging, in-system programming and boundary-scan testing for embedded devices

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:    GPL-2.0-only
URL:        https://sourceforge.net/projects/openocd
Source0:    https://downloads.sourceforge.net/project/openocd/openocd/%{version}%{?rcVer:-rc%{rcVer}}/%{name}-%{version}%{?rcVer:-rc%{rcVer}}.tar.bz2
Patch0:     0001-openocd-revert-workarounds-for-expr-syntax-change.patch
Patch1:     0003-jtag-vdebug-fix-endianness-support.patch
Patch2:     0004-openocd-fix-build-with-jimtcl-0.83.patch


BuildRequires: capstone-devel
BuildRequires: chrpath
BuildRequires: gcc
BuildRequires: hidapi-devel
BuildRequires: jimtcl-devel
# Only used for gpio bitbang driver
# BuildRequires: libgpiod-devel
BuildRequires: libjaylink-devel
BuildRequires: libftdi-devel
BuildRequires: libusbx-devel
BuildRequires: make
BuildRequires: sdcc
BuildRequires: texinfo

%description
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system programming 
and boundary-scan testing for embedded devices. Various different boards, 
targets, and interfaces are supported to ease development time.

Install OpenOCD if you are looking for an open source solution for hardware 
debugging.

%prep
%autosetup -n %{name}-%{version}%{?rcVer:-rc%{rcVer}} -p1
rm -rf jimtcl
rm -f src/jtag/drivers/OpenULINK/ulink_firmware.hex
sed -i 's/MODE=.*/TAG+="uaccess"/' contrib/60-openocd.rules

%build
pushd src/jtag/drivers/OpenULINK
make PREFIX=sdcc hex
popd

%configure \
  --disable-werror \
  --enable-static \
  --disable-shared \
  --enable-dummy \
  --enable-ftdi \
  --enable-stlink \
  --enable-ti-icdi \
  --enable-ulink \
  --enable-usb-blaster-2 \
  --enable-ft232r \
  --enable-vsllink \
  --enable-xds110 \
  --enable-cmsis-dap-v2 \
  --enable-osbdm \
  --enable-opendous \
  --enable-aice \
  --enable-usbprog \
  --enable-rlink \
  --enable-armjtagew \
  --enable-cmsis-dap \
  --enable-nulink \
  --enable-kitprog \
  --enable-usb-blaster \
  --enable-presto \
  --enable-openjtag \
  --enable-jlink \
  --enable-parport \
  --enable-jtag_vpi \
  --enable-jtag_dpi \
  --enable-ioutil \
  --enable-amtjtagaccel \
  --enable-ep39xx \
  --enable-at91rm9200 \
  --enable-gw16012 \
  --enable-oocd_trace \
  --enable-buspirate \
  --enable-sysfsgpio \
  --enable-esp-usb-jtag \
  --enable-xlnx-pcie-xvc \
  --enable-remote-bitbang \
  --disable-internal-jimtcl \
  --disable-doxygen-html \
  --with-capstone \
  CROSS=
%make_build

%install
%make_install
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{_libdir}/libopenocd.*
rm -rf %{buildroot}/%{_datadir}/%{name}/contrib
mkdir -p %{buildroot}/%{_prefix}/lib/udev/rules.d/
install -p -m 644 contrib/60-openocd.rules %{buildroot}/%{_prefix}/lib/udev/rules.d/60-openocd.rules
chrpath --delete %{buildroot}/%{_bindir}/openocd

%files
%license COPYING
%doc AUTHORS NEWS* NEWTAPS README TODO
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/OpenULINK/ulink_firmware.hex
%{_bindir}/%{name}
%{_prefix}/lib/udev/rules.d/60-openocd.rules
# doc
%{_infodir}/%{name}.info*.gz
%{_mandir}/man1/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 01 2024 Jiri Kastner <jkastner@fedoraproject.org> - 0.12.0-3.5
- fix build with jimtcl-0.83

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.12.0-3.4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 07 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.0-3
- Disable GPIO bitbanging driver

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 06 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.12.0-2
- Rebuild against jimtcl-0.82

* Fri Feb 17 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-0.rc1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 19 2022 Jiri Kastner <jkastner@fedoraproject.org> - 0.12.0-0.rc1
- release candidate 1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Nils Philippsen <nils@tiptoe.de> - 0.11.0-2
- rebuild against jimtcl-0.81

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 09 2021 Marcus A. Romer <aimylios@gmx.de> - 0.11.0-1
- bump Release version to allow automatic update from rc2

* Sun Mar 07 2021 Jiri Kastner <jkastner@fedoraproject.org> - 0.11.0-0
- release 0.11.0

* Wed Feb 17 2021 Marcus A. Romer <aimylios@gmx.de> - 0.11.0-0.rc2.2
- update build configuration
- fix packaging of license and documentation

* Fri Jan 29 2021 Jiri Kastner <jkastner@fedoraproject.org> - 0.11.0-0.rc2
- release candidate #2
- fixed some rpmlint issues (source, removed patch)
- adjusted dependency for libjaylink-devel in buildrequries

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-0.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Jiri Kastner <jkastner@fedoraproject.org> - 0.11.0-0.rc1
- release candidate #1

* Fri Aug 07 2020 Jeff Law <law@redhat.com> - 0.10.0-18
- Enable _legacy_common_support

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.10.0-13
- Remove hardcoded gzip suffix from GNU info pages

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.10.0-12
- Remove obsolete requirements for %%post/%%preun scriptlets

* Thu Feb 21 2019 Jiri Kastner <jkastner@redhat.com> - 0.10.0-11
- fix for CVE-2018-5704 (RHBZ 1534844)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Jiri Kastner <jkastner@redhat.com> - 0.10.0-9
- fix openocd rules (RHBZ 1571599)

* Sat Sep 22 2018 Lubomir Rintel <lkundrak@v3.sk> - 0.10.0-8
- rebuild for jimtcl soname bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 24 2017 Jon Disnard <parasense@fedoraproject.org> - 0.10.0-3
- Update to use recent libjim.so bump

* Mon Mar 13 2017 Jiri Kastner <jkastner@redhat.com> - 0.10.0-2
- removed line with commented macro

* Wed Mar  8 2017 Jiri Kastner <jkastner@redhat.com> - 0.10.0-1
- update to 0.10.0 (RHBZ 1415527)
- added new dependency for libjaylink
- removed patches (RHBZ 1427016)

* Tue Mar  7 2017 Jiri Kastner <jkastner@redhat.com> - 0.9.0-6
- rebuild for jimtcl soname bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 13 2016 Markus Mayer <lotharlutz@gmx.de> - 0.9.0-4
- Fix wrong udev rules bz#1177996

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jiri Kastner <jkastner@redhat.com> - 0.9.0-1
- update to 0.9.0
- added texinfo dependency

* Mon Feb 02 2015 Markus Mayer <lotharlutz@gmx.de> - 0.8.0-6
- rebuild for jimtcl soname bump

* Mon Feb 02 2015 Markus Mayer <lotharlutz@gmx.de> - 0.8.0-5
- rebuild for jimtcl soname bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Markus Mayer <lotharlutz@gmx.de> - 0.8.0-2
- fix build issue with libftdi-1.1

* Tue Apr 29 2014 Markus Mayer <lotharlutz@gmx.de> - 0.8.0-1
- update to 0.8.0
- build ulink_firmware.hex during build
- enable new targets
- add udev rule

* Mon Mar 03 2014 Markus Mayer <lotharlutz@gmx.de> - 0.7.0-5
- rebuild for jimtcl soname bump
- add patch to adapt to new jimtcl API

* Sun Mar 02 2014 Markus Mayer <lotharlutz@gmx.de> - 0.7.0-4
- rebuild for jimtcl soname bump

* Sat Sep 07 2013 Markus Mayer <lotharlutz@gmx.de> - 0.7.0-3
- rebuild for jimtcl soname bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Markus Mayer <lotharlutz@gmx.de> - 0.7.0-1
- update to upstream release 0.7.0

* Thu May 02 2013 Markus Mayer <lotharlutz@gmx.de> - 0.6.1-1
- update to upstream release 0.6.1
- don't bundle jimtcl
- enable additional targets

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 17 2012 Dean Glazeski <dnglaze at gmail.com> - 0.6.0-2
- Enabling the stlink option

* Tue Sep 11 2012 Dean Glazeski <dnglaze at gmail.com> - 0.6.0-1
- RPM build for new release.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 31 2012 Dennis Gilmore <dennis@ausil.us> - 0.5.0-3
- patch in flyswatter2 support

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Dean Glazeski <dnglaze at gmail.com> - 0.5.0-1
- RPM build for new release.

* Sat Feb 13 2010 Dean Glazeski <dnglaze at gmail.com> - 0.4.0-1
- RPM build for new release.

* Fri Nov 13 2009 Dean Glazeski <dnglaze at gmail.com> - 0.3.1-1
- RPM build for bug fix for new release.

* Fri Oct 30 2009 Dean Glazeski <dnglaze at gmail.com> - 0.3.0-1
- RPM build for new release.

* Sat Aug 22 2009 Dean Glazeski <dnglaze at gmail.com> - 0.2.0-4
- Fixed duplicate file warnings for RPM build

* Fri Aug 21 2009 Dean Glazeski <dnglaze at gmail.com> - 0.2.0-3
- Updated spec file to match with suggestions from the review request
  (Bug 502130)
- Changed back to static library but removed the library from the distribution

* Fri Aug 14 2009 Dean Glazeski <dnglaze at gmail.com> - 0.2.0-2
- Switched to a shared object instead of a static library for the installation
  and added ldconfig commands
- Added some interfaces that were added to OpenOCD since 0.1.0

* Sat Aug 08 2009 Dean Glazeski <dnglaze at gmail.com> - 0.2.0-1
- Updated for new OpenOCD release

* Sat Jul 18 2009 Dean Glazeski <dnglaze at gmail.com> - 0.1.0-3
- Fixed the website URL and source0 URL

* Wed Jul 01 2009 Dean Glazeski <dnglaze at gmail.com> - 0.1.0-2
- Added some suggestions from package review (Bug 502130)
- Errors produced by RPM lint can be ignored (Bug 502112)

* Tue Mar 17 2009 Dean Glazeski <dnglaze at gmail.com> - 0.1.0-1
- Created initial package for Fedora
