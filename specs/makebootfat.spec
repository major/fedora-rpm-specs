%define new_ldlinux	0

Summary: Utility for creation bootable FAT disk
Name: makebootfat
Version: 1.4
Release: 42%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://advancemame.sourceforge.net/doc-makebootfat.html
Source0: http://downloads.sourceforge.net/advancemame/%{name}-%{version}.tar.gz
Source1: makebootfat-README.usbboot
Patch0:  makebootfat-1.4-newioctl.patch
Patch1: makebootfat-configure-c99.patch

BuildRequires: make
BuildRequires: gcc

%if %{new_ldlinux}
#  Get syslinux-VERSION.tar.bz2 from
#	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/
#  or
#	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/Old/
#  Then
#	bunzip2 -cd syslinux-VERSION.tar.bz2 | tar -xvf -
#	cp syslinux-VERSION/ldlinux.bss ldlinux.bss-VERSION
#	cp syslinux-VERSION/ldlinux.sys ldlinux.sys-VERSION
#	rm -rf syslinux-VERSION
#
Source2: ldlinux.bss-3.36
Source3: ldlinux.sys-3.36
%endif



%description
This utility creates a bootable FAT filesystem and populates it
with files and boot tools.

It was mainly designed to create bootable USB and Fixed disk
for the AdvanceCD project (http://advancemame.sourceforge.net), but
can be successfully used separately for any purposes.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

install -p -m644 %{SOURCE1} README.usbboot


%build

%configure
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/x86
install -p -m644 mbrfat.bin $RPM_BUILD_ROOT%{_datadir}/%{name}/x86
%if %{new_ldlinux}
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/x86/ldlinux.bss
install -p -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}/x86/ldlinux.sys
%else
install -p -m644 test/ldlinux.bss $RPM_BUILD_ROOT%{_datadir}/%{name}/x86
install -p -m644 test/ldlinux.sys $RPM_BUILD_ROOT%{_datadir}/%{name}/x86
%endif



%files
%doc AUTHORS COPYING HISTORY README README.usbboot
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/*/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4-41
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Florian Weimer <fweimer@redhat.com> - 1.4-36
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-15
- fix Source0 url (#847799)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-11
- Fix '-o usb' option on new kernels (#653796,
  patch from Dennis Czeremin <fedora@czeremin.de>)

* Fri Jun 18 2010 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-10
- Compile without strict aliasing (#605549)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4-7
- Autorebuild for GCC 4.3

* Thu Sep 27 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-6
- always distribute own ldlinux.sys as well as ldlinux.bss
- add conditional macro %%{new_ldlinux} (default off) to build the package
  with ldlinux.bss and ldlinux.sys taken from some syslinux source directly.
- Update README.usbboot .

* Fri Aug 17 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to GPLv2+

* Fri Sep  1 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-5
- rebuild for FC6

* Tue Aug  1 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-4
- avoid world-writable docs (#200829)

* Wed Feb 15 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-3
- rebuild for FC5

* Mon Dec 26 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-2
- place mbrfat.bin and ldlinux.bss under %%{_datadir}/%%{name}/x86

* Mon Dec 24 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-1
- accepted for Fedora Extra (review by John Mahowald <jpmahowald@gmail.com>)

* Mon Oct  3 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.4-1
- initial release
- install mbrfat.bin and ldlinux.bss binary files, they are
  actually needed to create something useful here.
- add README.usbboot -- instruction how to make diskboot.img more helpful
  (written by me).

