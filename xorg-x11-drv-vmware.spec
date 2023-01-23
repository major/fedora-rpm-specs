%global tarball xf86-video-vmware
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers
#global gitdate 20150211
#global gitversion 8f0cf7c

%undefine _hardened_build

%if 0%{?gitdate}
%global gver .%{gitdate}git%{gitversion}
%endif

Summary:    Xorg X11 vmware video driver
Name:	    xorg-x11-drv-vmware
Version:    13.3.0
Release:    2%{?dist}
URL:	    http://www.x.org
License:    MIT

%if 0%{?gitdate}
Source0: %{tarball}-%{gitdate}.tar.bz2
%else
Source0:   https://ftp.x.org/archive/individual/driver/%{tarball}-%{version}.tar.bz2
# upstream compile fixes
Patch12:   0012-vmwgfx-Change-header-inclusion-order-to-avoid-xorg-h.patch
Patch13:   0013-vmwgfx-fix-missing-array-notation.patch
%endif

ExclusiveArch: %{ix86} x86_64 ia64

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-server-devel >= 1.10.99.902
BuildRequires: libdrm-devel pkgconfig(xext) pkgconfig(x11)
BuildRequires: mesa-libxatracker-devel >= 8.0.1-4
BuildRequires: systemd-devel

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires: libxatracker >= 8.0.1-4

%description 
X.Org X11 vmware video driver.

%prep
%autosetup -p1 -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install || exit 1
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%files
%{driverdir}/vmware_drv.so
%{_mandir}/man4/vmware.4*

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Yaakov Selkowitz <yselkowi@redhat.com> - 13.3.0-1
- Update to 13.3.0 (#1579342, #2047133)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 10:25:25 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 13.2.1-14
- Add BuildRequires for make

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Adam Jackson <ajax@redhat.com> - 13.2.1-7
- Rebuild for xserver 1.20

* Mon Mar 05 2018 Adam Jackson <ajax@redhat.com> - 13.2.1-6
- Build fix for xserver 1.20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Hans de Goede <hdegoede@redhat.com> - 13.2.1-1
- New upstream bug-fix release 13.2.1

* Thu Sep 29 2016 Hans de Goede <hdegoede@redhat.com> - 13.0.2-12.20150211git8f0cf7c
- Add patches from upstream for use with xserver-1.19
- Rebuild against xserver-1.19

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.2-11.20150211git8f0cf7c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Peter Hutterer <peter.hutterer@redhat.com>
- s/define/global/

* Wed Jul 29 2015 Dave Airlie <airlied@redhat.com> - 13.0.2-10.20150211git8f0cf7c
- 1.15 ABI rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.2-9.20150211git8f0cf7c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 Dave Airlie <airlied@redhat.com> 13.0.2-8
- removed hardened build

* Wed Feb 11 2015 Hans de Goede <hdegoede@redhat.com> - 13.0.2-7.20150211git8f0cf7c
- xserver 1.17 ABI rebuild
- Update to git snapshot of the day to fix building with xserver 1.17

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.2-6.20140613git82c9b0c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Hans de Goede <hdegoede@redhat.com> - 13.0.2-5.20140613git82c9b0c
- xserver 1.15.99.903 ABI rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 13.0.2-4.20140613git82c9b0c
- Snapshot from git master to fix render accel not working (rhbz#1077453)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Hans de Goede <hdegoede@redhat.com> - 13.0.2-2
- Add server managed fd support

* Mon Apr 28 2014 Hans de Goede <hdegoede@redhat.com> - 13.0.2-1
- vmware 13.0.2

* Mon Apr 28 2014 Hans de Goede <hdegoede@redhat.com> - 13.0.1-10.20131207gita40cbd7b
- xserver 1.15.99-20140428 git snapshot ABI rebuild

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> - 13.0.1-9.20131207gita40cbd7b
- 1.15 ABI rebuild

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> - 13.0.1-8.20131207gita40cbd7b
- 1.15RC4 ABI rebuild

* Sat Dec 07 2013 Dave Airlie <airlied@redhat.com> 13.0.1-7
- snapshot master to build against latest mesa

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> - 13.0.1-6
- 1.15RC2 ABI rebuild

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> - 13.0.1-5
- 1.15RC1 ABI rebuild

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> - 13.0.1-4
- ABI rebuild

* Thu Oct 24 2013 Adam Jackson <ajax@redhat.com> 13.0.1-3
- xserver 1.15 API compat

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Peter Hutterer <peter.hutterer@redhat.com> 13.0.1-1
- vmware 13.0.1

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 12.0.99.901-5.20130109gitadf375f3
- require xorg-x11-server-devel, not -sdk

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 12.0.99.901-4.20130109gitadf375f3
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 12.0.99.901-3.20130109gitadf375f3
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 12.0.99.901-2.20130109gitadf375f3
- ABI rebuild

* Wed Jan 09 2013 Adam Jackson <ajax@redhat.com> 12.0.99.901-1
- vmware 12.0.99.901

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.2-3.20120718gite5ac80d8f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Dave Airlie <airlied@redhat.com> 12.0.2-1.20120718gite5ac80d8f
- snapshot latest git for api changes

* Fri Apr 20 2012 Adam Jackson <ajax@redhat.com> 12.0.2-1
- vmware 12.0.2

* Mon Mar 19 2012 Adam Jackson <ajax@redhat.com> 12.0.1-2
- vmware-12.0.1-vgahw.patch: Fix a different crash at start (#782995)
- vmware-12.0.1-git.patch: Backport a garbage-free fix from git.

* Thu Mar 15 2012 Dave Airlie <airlied@redhat.com> 12.0.1-1
- update to latest upstream release

* Mon Mar 12 2012 Adam Jackson <ajax@redhat.com> 11.0.3-14
- vmware-11.0.3-vgahw.patch: Fix crash at start. (#801546)

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> - 11.0.3-13
- ABI rebuild

* Fri Feb 10 2012 Peter Hutterer <peter.hutterer@redhat.com> - 11.0.3-12
- ABI rebuild

* Tue Jan 24 2012 Peter Hutterer <peter.hutterer@redhat.com> - 11.0.3-11
- ABI rebuild

* Wed Jan 04 2012 Peter Hutterer <peter.hutterer@redhat.com> - 11.0.3-10
- Rebuild for server 1.12

* Fri Dec 16 2011 Adam Jackson <ajax@redhat.com> - 11.0.3-9
- Drop xinf file

* Wed Nov 16 2011 Adam Jackson <ajax@redhat.com> 11.0.3-8
- ABI rebuild
- vmware-11.0.3-abi12.patch: Compensate for videoabi 12.
- vmware-11.0.3-unbreak-xinerama.patch: Unbreak swapped dispatch in the
  fake-xinerama code.

* Wed Nov 09 2011 ajax <ajax@redhat.com> - 11.0.3-7
- ABI rebuild

* Thu Aug 18 2011 Adam Jackson <ajax@redhat.com> - 11.0.3-6
- Rebuild for xserver 1.11 ABI

* Wed May 11 2011 Peter Hutterer <peter.hutterer@redhat.com> - 11.0.3-5
- Rebuild for server 1.11

* Mon Feb 28 2011 Peter Hutterer <peter.hutterer@redhat.com> - 11.0.3-4
- Rebuild for server 1.10

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Peter Hutterer <peter.hutterer@redhat.com> - 11.0.3-2
- Rebuild for server 1.10

* Tue Nov 09 2010 Adam Jackson <ajax@redhat.com> 11.0.3-1
- vmware 11.0.3

* Wed Oct 27 2010 Adam Jackson <ajax@redhat.com> 11.0.1-2
- Add ABI requires magic (#542742)

* Tue Aug 10 2010 Dave Airlie <airlied@redhat.com> 11.0.1-1
- Latest upstream release.

* Mon Jul 05 2010 Peter Hutterer <peter.hutterer@redhat.com> - 10.16.7-4
- rebuild for X Server 1.9

* Thu Jan 21 2010 Peter Hutterer <peter.hutterer@redhat.com> - 10.16.7-3
- Rebuild for server 1.8

* Fri Aug 07 2009 Adam Jackson <ajax@redhat.com> 10.16.7-2
- fix for symbol list removal.

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 10.16.7-1
- vmware 10.16.7 + new abi patch

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.16.0-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 10.16.0-4.1
- ABI bump

* Tue Jun 23 2009 Dave Airlie <airlied@redhat.com> 10.16.0-4
- abi.patch: patch for new server ABI

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 24 2008 Dave Airlie <airlied@redhat.com> 10.16.0-2
- bump build for new server API

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 10.16.0-1
- Latest upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 10.15.2-100.1
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Adam Jackson <ajax@redhat.com> 10.15.2-99.1
- Update to git snapshot for pciaccess conversion. (#428613)

* Thu Oct 11 2007 Adam Jackson <ajax@redhat.com> 10.15.2-1
- xf86-video-vmware 10.15.2

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 10.15.1-1
- xf86-video-vmware 10.15.1

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 10.14.1-3
- Rebuild for build ID

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 10.14.1-2
- Update Requires and BuildRequires.  Disown the module directories.  Add
  Requires: hwdata.

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 10.14.1-1.fc7
- Update to 10.14.1

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 10.13.0-2
- Rebuild for 7.1 ABI fix.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 10.13.0-1
- Update to 10.13.0 from 7.1RC1.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 10.11.1.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 10.11.1.3-1
- Updated xorg-x11-drv-vmware to version 10.11.1.3 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 10.11.1.2-1
- Updated xorg-x11-drv-vmware to version 10.11.1.2 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 10.11.1-1
- Updated xorg-x11-drv-vmware to version 10.11.1 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 10.11.0.1-1
- Updated xorg-x11-drv-vmware to version 10.11.0.1 from X11R7 RC1
- Fix *.la file removal.

* Tue Oct 4 2005 Mike A. Harris <mharris@redhat.com> 10.10.2-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64, ia64

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 10.10.2-0
- Initial spec file for vmware video driver generated automatically
  by my xorg-driverspecgen script.
