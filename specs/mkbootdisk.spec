Summary: Creates a boot floppy disk for booting a system
Name: mkbootdisk
Version:  1.5.5
Release: 37%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: mkbootdisk-%{version}.tar.xz
Patch0: mkbootdisk-1.5.5-fix-long-volid.patch
Patch1: mkbootdisk-1.5.5-man-dracut.patch
Patch2: mkbootdisk-1.5.5-syslinux-5-fix.patch
BuildArch: noarch
ExclusiveOs: Linux
ExclusiveArch: %{ix86} sparc sparc64 x86_64
BuildRequires: make
Requires: genisoimage
%ifnarch sparc sparc64
Requires: syslinux
%else
Requires: silo genromfs
%endif

%description
The mkbootdisk program creates a standalone boot floppy disk for
booting the running system.  The created boot disk will look for the
root filesystem on the device mentioned in /etc/fstab and includes an
initial ramdisk image which will load any necessary SCSI modules for
the system.

%prep
%setup -q
%patch -P0 -p1 -b .fix-long-volid
%patch -P1 -p1 -b .man-dracut
%patch -P2 -p1 -b .syslinux-5-fix

%install
rm -rf $RPM_BUILD_ROOT
make BUILDROOT=$RPM_BUILD_ROOT mandir=%{_mandir} install

%files
%doc COPYING
%attr(755,root,root) /sbin/mkbootdisk
%attr(644,root,root) %{_mandir}/man8/mkbootdisk.8*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 30 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.5-36
- Made package noarch
  Resolves: rhbz#2300971

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.5-35
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov  5 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.5-15
- Added support for syslinux-5+
  Resolves: rhbz#1141496
- Fixed same bogus dates in the changelog (best effort guessing :)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 17 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.5-9
- Fixed man page to point to dracut instead of mkinitrd
  Resolves: rhbz#829183

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar  1 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.5-7
- Fixed summary

* Mon Feb 13 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.5-6
- Added explicit requires for genisoimage
  Resolves: rhbz#790049

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.5-4
- Fixed volume ID to be max 32 chars

* Wed Aug 03 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.5-3
- Added license file into package
- Fixed rpmlint warning
- Added sparc64 to ExclusiveArch
  Resolves: rhbz#226145

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 15 2010 Stepan Kasal <skasal@redhat.com> - 1.5.5-1
- do not require dosfstools nor mkinitrd; tey are not needed for --iso
- Resolves: 549098, #549099
- various cosmetic changes
- drop obsolete conflicts tag
- better buildroot

* Thu Oct  1 2009 Stepan Kasal <skasal@redhat.com> - 1.5.4-1
- syslinux image changed (#506181)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5.3-4
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.3-3.1
- Autorebuild for GCC 4.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.5.3-2.1
- rebuild

* Thu Apr 06 2006 Peter Vrabec <pvrabec@redhat.com> 1.5.3-2
- change noarch back to ExclusiveArch

* Wed Apr 05 2006 Peter Vrabec <pvrabec@redhat.com> 1.5.3-1
- fix tail command usage (#187876)

* Tue Mar 07 2006 Peter Vrabec <pvrabec@redhat.com> 1.5.2-6
- build  as noarch

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.5.2-5.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Mar 17 2005 Peter Vrabec <pvrabec@redhat.com> 1.5.2-5
- rebuild

* Mon Nov 01 2004 Peter Vrabec <pvrabec@redhat.com>
- fix slight man page error (#85470)

* Mon Oct 25 2004 Peter Vrabec <pvrabec@redhat.com>
- fix problem with hangup (#112752)

* Thu Oct 21 2004 Peter Vrabec <pvrabec@redhat.com>
- fix clear /tmp (#136599)

* Tue Aug  3 2004 Jeremy Katz <katzj@redhat.com> - 1.5.2-1
- fix name of system to boot (#114878)

* Wed Feb 19 2003 Jeremy Katz <katzj@redhat.com> 1.5.1-1
- apply mikem's patch so that we handle loop devices better (#84351)
- switch to making a loopback img and then dd'ing that to the floppy (#84351)
- man page updates (#77262)

* Wed Feb 19 2003 Jeremy Katz <katzj@redhat.com> 1.5.0-1
- use copy instead of mkinitrd to get the initrd
- don't get default kernel args if grubby can't figure out the default kernel
- exit with an exit status of 1 if things fail

* Mon Dec 23 2002 Matt Wilson <msw@redhat.com>
- rebuild in new collection

* Thu Aug 08 2002 Michael Fulbright <msf@redhat.com>
- fix creation of boot iso image

* Thu Aug 08 2002 Michael Fulbright <msf@redhat.com>
- fix small bug with temp files

* Thu Aug 08 2002 Michael Fulbright <msf@redhat.com>
- add option when we make dos fs to save more space

* Mon Jun 03 2002 Erik Troan <ewt@redhat.com>
- only run grubby if /boot/grub/grub.conf exists

* Mon Jun 03 2002 Erik Troan <ewt@redhat.com>
- if --kernelargs isn't specified and grubby is available use it to get
  the arguments to use; this only works with mkinitrd (grubby) >= 3.4.3
  (8591)
- fixed some typos in man page (11297)
- use cp -p rather then cp -a (as we want to follow symlinks) (13480)
- create image files if appropriate (53818)
- compact option removed (syslinux doesn't use it anyway) (58989)

* Tue Mar 26 2002 Jeremy Katz <katzj@redhat.com>
- add --kernelargs command line option

* Sun Jan 06 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- do not require syslinux for sparc

* Mon Nov 05 2001 Erik Troan <ewt@redhat.com>
- fixed minor typo in man page

* Wed Aug 15 2001 Matt Wilson <msw@redhat.com>
- changed Summary:, it's no longer a bad copy and paste job from the
  mkinitrd spec file (MF #50193)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Feb 08 2001 Michael Fulbright <msf@redhat.com>
- return error code when we cant format the floppy. Helps anaconda out.

* Tue Jan 23 2001 Erik Troan <ewt@redhat.com>
- switched to use syslinux rather then lilo
- requires dosfstools
- put version in only one place, mkbootdisk

* Thu Jul 06 2000 Erik Troan <ewt@redhat.com>
- wasn't including ethernet devices properly

* Thu Jun  1 2000 Bill Nottingham <notting@redhat.com>
- conf.modules -> modules.conf, fhs stuff

* Mon May 01 2000 Erik Troan <ewt@redhat.com>
- patched to work with disk labels

* Thu Feb  3 2000 Matt Wilson <msw@redhat.com>
- gzip manpage

* Mon Jan 10 2000 Erik Troan <ewt@redhat.com>
- removed rescue stuff

* Mon Nov  8 1999 Matt Wilson <msw@redhat.com>
- removed 'prompt' from silo.conf

* Mon Oct 25 1999 Jakub Jelinek <jakub@redhat.com>
- fix sparc ramdisk making for new modutils and kernel
  file layout.

* Sat Sep 25 1999 Michael K. Johnson <johnsonm@redhat.com>
- ignore commented lines in fstab, generally more robust
  fstab parsing

* Sat Aug 21 1999 Bill Nottingham <notting@redhat.com>
- ditto

* Thu Aug 12 1999 Bill Nottingham <notting@redhat.com>
- add fix

* Tue May 25 1999 Matt Wilson <msw@redhat.com>
- added -P to the cp lines for devices to pick up parent directories
  for ida/ and rd/

* Wed Apr  7 1999 Matt Wilson <msw@redhat.com>
- pass load_ramdisk=2 as alan had to port his ramdisk hack from 2.0.x 

* Mon Apr  5 1999 Matt Wilson <msw@redhat.com>
- pass load_ramdisk=1 for rescue image, as 2.2 kernels get this right

* Thu Mar 18 1999 Matt Wilson <msw@redhat.com>
- fixed misspelling in man page

* Thu Feb 25 1999 Matt Wilson <msw@redhat.com>
- updated the description

* Thu Nov  5 1998 Jeff Johnson <jbj@redhat.com>
- import from ultrapenguin 1.1.

* Fri Oct 30 1998 Jakub Jelinek <jj@ultra.linux.cz>
- support for SPARC

* Sat Aug 29 1998 Erik Troan <ewt@redhat.com>
- wasn't including nfs, isofs, or fat modules properly
- mkinitrd args weren't passed right due to a typo
