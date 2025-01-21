Name:           uisp
Version:        20050207
Release:        39%{?dist}
Summary:        Universal In-System Programmer for Atmel AVR and 8051


# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/uisp
Source0:        http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz
Patch0:         uisp_Werror.patch
Patch1:         uisp-20050207-m168-stk500-extendedFuseSupport.patch
Patch2:         uisp-configure-c99.patch


BuildRequires: make
BuildRequires:  gcc-c++
%description
Uisp is utility for downloading/uploading programs to AVR devices. Can also be
used for some Atmel 8051 type devices. In addition, uisp can erase the device,
write lock bits, verify and set the active segment.

For use with the following hardware to program the devices:
  pavr      http://avr.jpk.co.nz/pavr/pavr.html
  stk500    Atmel STK500
  dapa      Direct AVR Parallel Access
  stk200    Parallel Starter Kit STK200, STK300
  abb       Altera ByteBlasterMV Parallel Port Download Cable
  avrisp    Atmel AVR ISP (?)
  bsd       http://www.bsdhome.com/avrprog/ (parallel)
  fbprg     http://ln.com.ua/~real/avreal/adapters.html (parallel)
  dt006     http://www.dontronics.com/dt006.html (parallel)
  dasa      serial (RESET=RTS SCK=DTR MOSI=TXD MISO=CTS)
  dasa2     serial (RESET=!TXD SCK=RTS MOSI=DTR MISO=CTS)


%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1

%build
%configure
make

%install
rm INSTALL
make install DESTDIR=$RPM_BUILD_ROOT DOC_INST_DIR=$RPM_BUILD_ROOT/%{_pkgdocdir}


%files
%doc AUTHORS CHANGES CHANGES.old COPYING ChangeLog* TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 20050207-38
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Florian Weimer <fweimer@redhat.com> - 20050207-33
- Port configure script to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 17 2016 Lucian Langa <lucilanga@gnome.eu.org> - 20050207-19
- cleanup up specfile
- fix build break

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20050207-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050207-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 20050207-16
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050207-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050207-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Lucian Langa <cooly@gnome.eu.org> - 20050207-13
- specify doc install dir, fixes FTBFS

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050207-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050207-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050207-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050207-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050207-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 12 2010 Lucian Langa <cooly@gnome.eu.org> - 20050207-7
- add atmega168 support (upstream #4041)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050207-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20050207-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20050207-4
- fix patch

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 20050207-3
- fix license tag

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20050207-2
- Autorebuild for GCC 4.3

* Mon Mar 12 2007 Trond Danielsen <trond.danielsen@fedoraproject.org> - 20050207-1
- Initial version.
- Summary and description taken from spec file included in uisp.
