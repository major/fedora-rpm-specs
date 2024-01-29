Summary: X.Org X11 driver installation package
Name: xorg-x11-drivers
Version: 2022
Release: 6%{?dist}
# SPDX
License: MIT

# relevant hardware

Requires: xorg-x11-drv-dummy
Requires: xorg-x11-drv-evdev
Requires: xorg-x11-drv-libinput
Requires: xorg-x11-drv-modesetting

%if !0%{?rhel}

%ifnarch aarch64 s390x
Requires: xorg-x11-drv-qxl
%endif

# only non-s390x
%ifnarch s390x
Requires: xorg-x11-drv-ati
Requires: xorg-x11-drv-nouveau
Requires: xorg-x11-drv-wacom
%endif

# So far intel is onboard-only.
%ifarch %{ix86} x86_64
Requires: xorg-x11-drv-intel
%endif

# vmware soft drivers.
%ifarch %{ix86} x86_64 ia64
Requires: xorg-x11-drv-vmware
%endif

%ifarch %{ix86} x86_64
Requires: xorg-x11-drv-openchrome
%endif

%endif

%description
The purpose of this package is to require all of the individual X.Org
driver rpms, to allow the OS installation software to install all drivers
all at once, without having to track which individual drivers are present
on each architecture.  By installing this package, it forces all of the
individual driver packages to be installed.

%prep
%build
%install

%files

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 07 2023 José Expósito <jexposit@redhat.com>
- SPDX migration: license is already SPDX compatible

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 01 2022 Adam Jackson <ajax@redhat.com> - 2022-3
- Drop vesa and fbdev for https://fedoraproject.org/wiki/Changes/LegacyXorgDriverRemoval

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 Adam Jackson <ajax@redhat.com> - 2022-1
- Drop v4l

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 2021-1
- Change package version to year + build
- Exclude most drivers from RHEL

* Tue Oct 27 2020 Adam Jackson <ajax@redhat.com> - 7.7-30
- Don't Require wacom on s390x, that's just silly

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Adam Jackson <ajax@redhat.com> - 7.7-28
- Drop geode, since F31+ no longer supports the associated CPU

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Dan Horák <dan[at]danny.cz> - 7.7-25
- enable on s390x (related #1727029)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Hans de Goede <hdegoede@redhat.com> - 7.7-18
- Drop xorg-x11-drv-vmmouse there is a kernel driver for this which makes the
  device show up as a regular evdev input device now, and which does not need
  iopl

* Mon May 23 2016 Peter Hutterer <peter.hutterer@redhat.com> 7.7-16
- Drop synaptics but install xorg-x11-drv-libinput instead (#1338583)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Peter Hutterer <peter.hutterer@redhat.com>
- Remove unnecessary defattr

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Peter Hutterer <peter.hutterer@redhat.com> 7.7-14
- Drop xorg-x11-drv-void, it outlived its purpose in xorg-x11-server 1.6
  several years ago.

* Thu Apr 23 2015 Peter Robinson <pbrobinson@fedoraproject.org> 7.7-13
- Exclude QXL from aarch64 for the time being

* Tue Oct 28 2014 Hans de Goede <hdegoede@redhat.com> - 7.7-12
- Add xorg-x11-drv-opentegra on arm arches (rhbz#1149362)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Adam Jackson <ajax@redhat.com> 7.7-9
- Drop from F21+: apm cirrus glint i128 i740 mach64 mga neomagic r128
  rendition s3virge savage siliconmotion sis tdfx trident

* Mon May 05 2014 Dennis Gilmore <dennis@ausil.us> 7.7-8
- drop sparc section
- add xorg-x11-drv-freedreno on arm arches

* Tue Apr 22 2014 Peter Hutterer <peter.hutterer@redhat.com> 7.7-7
- Drop mouse and keyboard, use evdev from now on

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Adam Jackson <ajax@redhat.com> 7.7-5
- Drop ast, handled by -modesetting now

* Tue Mar 19 2013 Adam Jackson <ajax@redhat.com> 7.7-4
- Less RHEL conditionals

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Adam Jackson <ajax@redhat.com> 7.7-2
- Drop nv

* Thu Jan 03 2013 Adam Jackson <ajax@redhat.com> 7.7-2
- Hide ast/cirrus/mga in RHEL

* Wed Jan 02 2013 Adam Jackson <ajax@redhat.com> 7.7-1
- Superstition bump to 7.7
- Drop intel from ia64, apparently that was never a thing

* Fri Dec 21 2012 Dennis Gilmore <dennis@ausil.us> - 7.4-11
- arm has omap and armsoc drivers

* Wed Aug 15 2012 Adam Jackson <ajax@redhat.com> 7.4-10
- Only build vesa on arches where xserver builds VBE support

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 7.4-8
- Add options for ARM

* Wed Mar 21 2012 Adam Jackson <ajax@redhat.com> 7.4-7
- More %%rhel conditionals
- Add -modesetting

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Adam Jackson <ajax@redhat.com> 7.4-5
- Reorganize and conditionalize for %%rhel

* Fri Oct 14 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.4-4
- Block penmount and elographics too. Penmount is unmaintained, elographics
  is maintained but may not work with the latest Xorg.

* Tue Sep 27 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.4-3
- Remove aiptek, acecad, fpit, hyperpen, penmount, mutouch. They are not
  maintained upstream anymore.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 04 2010 Adam Jackson <ajax@redhat.com> 7.4-1
- Add qxl

* Tue Mar 09 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.3-14
- Wacom driver is now xorg-x11-drv-wacom.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Kristian Høgsberg <krh@redhat.com> - 7.3-12
- Rename i810 to intel.

* Thu Feb 26 2009 Dave Airlie <airlied@redhat.com> 7.3-11
- remove diamondtouch + wiimote

* Thu Feb 19 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.3-10
- s/synaptics/xorg-x11-drv-synaptics/.
- Remove calcomp, citron, digitaledge, dmc, dynapro, jamstudio, magellan,
  microtouch, palmax, spaceorb, summa, tek4957, ur98. Nobody uses them.

* Mon Aug 11 2008 Adam Jackson <ajax@redhat.com> 7.3-9
- Add r128 and mach64.

* Wed Jul 16 2008 Adam Jackson <ajax@redhat.com> 7.3-8
- Tee hee, imstt isn't packaged yet.

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 7.3-7
- Comment cleanup.
- Add imstt to ppc, just for giggles.

* Tue Jul 15 2008 Warren Togami <wtogami@redhat.com> 7.3-6
- amd was renamed to geode

* Wed Jun 04 2008 Dennis Gilmore <dennis@ausil.us> 7.3-5
- add sparc drivers

* Fri Apr 04 2008 Adam Jackson <ajax@redhat.com> 7.3-4
- Remove -nsc and -cyrix.

* Mon Mar 03 2008 Adam Jackson <ajax@redhat.com> 7.3-3
- Drop magictouch, it can not work and can never have worked.

* Fri Feb 22 2008 Adam Jackson <ajax@redhat.com> 7.3-2
- xorg-x11-drv-diamondtouch.

* Mon Feb 18 2008 Adam Jackson <ajax@redhat.com> 7.3-1
- Superstition bump to 7.3.
- xorg-x11-drv-wiimote.
- Additional commentary about drivers that aren't included here.

* Wed Jan 09 2008 Adam Jackson <ajax@redhat.com> 7.2-11
- Drop avivo for being a dead end.
- Drop ark, chips, s3, and tseng for being unspeakably lame.

* Tue Nov 27 2007 Adam Jackson <ajax@redhat.com> 7.2-10
- :s/via/openchrome/

* Mon Oct 15 2007 Adam Jackson <ajax@redhat.com> 7.2-9
- Archify synaptics, it's not buildable most places.

* Fri Oct 12 2007 Jeremy Katz <katzj@redhat.com> 7.2-8
- Add avivo

* Fri Sep 07 2007 Adam Jackson <ajax@redhat.com> 7.2-7
- Add linuxwacom and synaptics to the default set.

* Fri May 11 2007 Adam Jackson <ajax@redhat.com> 7.2-6
- Add xorg-x11-drv-nouveau.  If this bothers you, uninstall the metapackage.

* Tue Mar 20 2007 Adam Jackson <ajax@redhat.com> 7.2-5
- Un-Require xorg-x11-drv-vga.

* Tue Feb 27 2007 Adam Jackson <ajax@redhat.com> 7.2-4
- Remove elo2300 and joystick for being utterly broken.

* Mon Feb 26 2007 Adam Jackson <ajax@redhat.com> 7.2-3
- Fix the i810 ifarch to include all the relevant arches.

* Mon Feb 19 2007 Adam Jackson <ajax@redhat.com> 7.2-2
- Package review feedback fixes: (#226573)
  - Remove URL, misleading
  - Remove the Obsoletes: xorg-x11
  - Fix License tag

* Sun Feb 18 2007 Adam Jackson <ajax@redhat.com> 7.2-1
- Superstition bump to 7.2
- ExcludeArch of s390{,x}
- Only ExclusiveArch those drivers that really are processor-specific
- Readd forgotten -tek4957

* Thu Oct 12 2006 Jeremy Katz <katzj@redhat.com> - 7.1-4
- mga not on ppc

* Mon Aug 21 2006 Adam Jackson <ajackson@redhat.com> 7.1-3
- Add cirrus to all arches
- Don't bother building this for s390{,x}

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 7.1-2.1
- rebuild

* Thu Jun 29 2006 Mike Harris <mharris@redhat.com> 7.1-2
- Regenerate driver list to match current rawhide X11R7.1 driver set.

* Wed Jun 21 2006 Mike Harris <mharris@redhat.com> 7.1-1
- Regenerate driver list to match current rawhide X11R7.1 driver set.

* Thu Feb 16 2006 Bill Nottingham <notting@redhat.com> 7.0-2
- uncomment (empty) file list so binary RPMs are built

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 7.0-1.1
- bump again for double-long bug on ppc(64)

* Thu Feb 09 2006 Mike Harris <mharris@redhat.com> 7.0-1
- Bumped version to 7.0-1
- Updated the driver list to match current rawhide, X11R7.0

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 0.99.2-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Nov 23 2005 Mike Harris <mharris@redhat.com> 0.99.2-4
- Add ur98 driver back, as it is part of X11R7 RC2

* Tue Nov 15 2005 Jeremy Katz <katzj@redhat.com> 0.99.2-3
- ur98 driver doesn't exist

* Tue Nov 15 2005 Jeremy Katz <katzj@redhat.com> 0.99.2-2
- add an obsoletes on xorg-x11 to get pulled in on upgrades

* Tue Nov 15 2005 Mike Harris <mharris@redhat.com> 0.99.2-1
- Initial build.
