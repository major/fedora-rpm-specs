%global tarball xf86-video-qxl
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers

%undefine _hardened_build

# Xspice is x86_64 and ARM only since spice-server is x86_64 / ARM only
%ifarch %{ix86} x86_64 %{arm} aarch64
%define with_xspice (0%{?fedora} || 0%{?rhel} > 6)
%else
%define with_xspice 0
%endif

#global gitdate 20160929
#global gitversion e13d28ee

%if 0%{?gitdate}

%define gver .%{gitdate}git%{gitversion}
%endif

Summary:   Xorg X11 qxl video driver
Name:      xorg-x11-drv-qxl

Version:   0.1.5

Release:   22%{?gver}%{?dist}
URL:       http://www.x.org
Source0:  http://xorg.freedesktop.org/releases/individual/driver/%{tarball}-%{version}.tar.bz2
#Source0:   %{tarball}-%{gitdate}.tar.bz2
Patch1: 0001-worst-hack-of-all-time-to-qxl-driver.patch
Patch2: 0002-Xspice-Use-print-instead-of-print.patch
Patch3: 0003-Xspice-Remove-extra-space-before-assignment.patch
Patch4: 0004-Xspice-Fix-Python3-str-vs-bytes-confusion.patch
# This shebang patch is currently downstream-only
Patch5: 0005-Xspice-Adjust-shebang-to-explicitly-mention-python3.patch
Patch6: 0006-qxl-call-provider-init.patch
# https://gitlab.freedesktop.org/xorg/driver/xf86-video-qxl/-/merge_requests/5
Patch7: 0001-configure-Simplify-fragile-libdrm-detection.patch

License:   MIT

ExcludeArch: s390 s390x

BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: git-core
BuildRequires: xorg-x11-server-devel >= 1.1.0-1
BuildRequires: spice-protocol >= 0.12.1
BuildRequires: libdrm-devel >= 2.4.46-1

%if %{with_xspice}
BuildRequires: spice-server-devel >= 0.8.0
%endif
BuildRequires: glib2-devel
BuildRequires: libtool
BuildRequires: libudev-devel
BuildRequires: libXfont2-devel
BuildRequires: libXext-devel

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description
X.Org X11 qxl video driver.

%if %{with_xspice}
%package -n    xorg-x11-server-Xspice
Summary:       XSpice is an X server that can be accessed by a Spice client
Requires:      Xorg %(xserver-sdk-abi-requires ansic)
Requires:      Xorg %(xserver-sdk-abi-requires videodrv)
Requires:      xorg-x11-server-Xorg

%description -n xorg-x11-server-Xspice
XSpice is both an X and a Spice server.
%endif

%prep
%autosetup -S git_am -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}


%build
autoreconf -ivf
%if %{with_xspice}
%define enable_xspice --enable-xspice
%endif
%configure --disable-static %{?enable_xspice}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%if %{with_xspice}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11
install -p -m 644 examples/spiceqxl.xorg.conf.example \
    $RPM_BUILD_ROOT%{_sysconfdir}/X11/spiceqxl.xorg.conf
# FIXME: upstream installs this file by default, we install it elsewhere.
# upstream should just not install it and let dist package deal with
# doc/examples.
rm -f $RPM_BUILD_ROOT/usr/share/doc/xf86-video-qxl/spiceqxl.xorg.conf.example
%if !%{with_xspice}
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/X11/spiceqxl.xorg.conf
%endif
%endif


%files
%doc COPYING README
%{driverdir}/qxl_drv.so

%if %{with_xspice}
%files -n xorg-x11-server-Xspice
%doc COPYING README.xspice README examples/spiceqxl.xorg.conf.example
%config(noreplace) %{_sysconfdir}/X11/spiceqxl.xorg.conf
%{_bindir}/Xspice
%{driverdir}/spiceqxl_drv.so
%endif


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 10 2021 Adam Jackson <ajax@redhat.com> - 0.1.5-19
- Fix a configure bug that would disable KMS support

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 10:13:02 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 0.1.5-17
- Add BuildRequires for make

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Dave Airlie <airlied@redhat.com> - 0.1.5-14
- Fix missing BR

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Christophe Fergeau <cfergeau@redhat.com> - 0.1.5-9
- Add upstream patches for Python 3 support and small bugfix

* Mon Apr 02 2018 Adam Jackson <ajax@redhat.com> - 0.1.5-8
- Rebuild for xserver 1.20

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.5-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Christophe Fergeau <cfergeau@redhat.com> 0.1.5-2
- Build on the same arches as spice-server

* Mon Dec 19 2016 Christophe Fergeau <cfergeau@redhat.com> 0.1.5-1%{?gver}%{?dist}
- Update to latest upstream release. All patches except one have been upstreamed.

* Mon Dec 19 2016 Christophe Fergeau <cfergeau@redhat.com> 0.1.4-11.20160929gite13d28ee
- Fix xspice crashing when used with xserver-1.19 (rhbz#1405939)
  Previous patch was only partially fixing the issue

* Tue Oct  4 2016 Hans de Goede <hdegoede@redhat.com> - 0.1.4-10.20160929gite13d28ee
- Fix qxl driver crashing when used with xserver-1.19 (rhbz#1381045)

* Thu Sep 29 2016 Hans de Goede <hdegoede@redhat.com> - 0.1.4-9.20160929gite13d28ee
- Update to latest git master for use with xserver-1.19
- Rebuild against xserver-1.19
- Really build xspice on ARMv7/aarch64

* Mon Jul 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.4-8
- Spice server is on ARMv7/aarch64

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 16 2015 Dave Airlie <airlied@redhat.com> - 0.1.4-6
- 1.18 ABI rebuild

* Thu Aug 06 2015 Christophe Fergeau <cfergeau@redhat.com> 0.1.4-5
- Drop patches from 0.1.4-4 (one is not upstream, the other one is causing Xorg
  crashes at startup)
- Add upstream patches fixing compilation with Xorg 1.18

* Tue Aug 04 2015 Adam Williamson <awilliam@redhat.com> - 0.1.4-4
- fix build with a couple of patches from upstream list (from davidshea)

* Wed Jul 29 2015 Dave Airlie <airlied@redhat.com>
- 1.15 ABI rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.1.4-2
- fix build on aarch64 - rhbz#1201877

* Thu Apr 02 2015 Christophe Fergeau <cfergeau@redhat.com> 0.1.4-1
- Update to 0.1.4 release

* Tue Mar 03 2015 Dave Airlie <airlied@redhat.com> 0.1.3-3
- remove hardened build

* Wed Feb 11 2015 Hans de Goede <hdegoede@redhat.com> - 0.1.3-2
- xserver 1.17 ABI rebuild

* Fri Oct 31 2014 Christophe Fergeau <cfergeau@redhat.com> 0.1.3-1
- Update to 0.1.3 release

* Fri Oct 10 2014 Christophe Fergeau <cfergeau@redhat.com> 0.1.2-1
- Update to new 0.1.2 upstream release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul  7 2014 Marc-André Lureau <marcandre.lureau@redhat.com> 0.1.1-12
- add fix for invisible cursor after resize (#1116870)

* Mon Jun 16 2014 Hans de Goede <hdegoede@redhat.com> - 0.1.1-11
- xserver 1.15.99.903 ABI rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Hans de Goede <hdegoede@redhat.com> - 0.1.1-9
- Add patches for server managed fd support
- xserver 1.15.99-20140428 git snapshot ABI rebuild

* Tue Jan 14 2014 Dave Airlie <airlied@redhat.com> 0.1.1-8
- grab patches from F20 - fix dates

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> - 0.1.1-7
- 1.15 ABI rebuild

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> - 0.1.1-6
- 1.15RC4 ABI rebuild

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> - 0.1.1-5
- 1.15RC2 ABI rebuild

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> - 0.1.1-4
- 1.15RC1 ABI rebuild

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> - 0.1.1-3
- ABI rebuild

* Thu Oct 24 2013 Adam Jackson <ajax@redhat.com> 0.1.1-2
- Drop qxl rev 1 patches

* Mon Oct 21 2013 Alon Levy <alevy@redhat.com> - 0.1.1-1
- New upstream release
- Fixes to said release to work with suid issues (upstream)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-0.14.20130514git77a1594
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Dave Airlie <airlied@redhat.com> 0.1.1-0.13
- resnapshot upstream to pick up a few patches
- add userspace patch to use new kernel hotspot interface (#974662)

* Wed Jul 03 2013 Dave Airlie <airlied@redhat.com> 0.1.1-0.12
- add support for udev event catching - for dynamic resize from kernel

* Tue Jul 02 2013 Dave Airlie <airlied@redhat.com> 0.1.1-0.11
- helps if you apply the patch (#978612)

* Sat Jun 29 2013 Dave Airlie <airlied@redhat.com> 0.1.1-0.10
- fix another resize issue due (#978612)

* Tue Jun 18 2013 Dave Airlie <airlied@redhat.com> 0.1.1-0.9
- disable composite/a8 surfaces for KMS (#974198)

* Tue May 28 2013 Dave Airlie <airlied@redhat.com> 0.1.1-0.8
- fix 32-bit (#965101)

* Tue May 14 2013 Dave Airlie <airlied@redhat.com> 0.1.1-0.7
- resnapshot - fixes randr under KMS

* Tue May 14 2013 Daniel Mach <dmach@redhat.com> - 0.1.1-0.6
- Fix with_xspice macro definition (airlied - cherrypick)

* Tue May 7 2013 Alon Levy <alevy@redhat.com> 0.1.1-0.5
- Add Xspice fixes and dfps (upstream a474a71..77a1594)

* Tue Mar 19 2013 Adam Jackson <ajax@redhat.com> 0.1.1-0.4
- Less RHEL customization

* Tue Mar 12 2013 Dave Airlie <airlied@redhat.com> 0.1.1-0.3.20130312gita474a71
- add KMS support to userspace driver

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.1.1-0.2.20130306git9d45cc5
- ABI rebuild

* Wed Mar 06 2013 Dave Airlie <airlied@redhat.com> 0.1.1-0.1
- bump to get UMS bo abstraction in - kms coming soon

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.1.0-4
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.1.0-3
- ABI rebuild

* Thu Jan 10 2013 Adam Jackson <ajax@redhat.com> - 0.1.0-2
- ABI rebuild

* Sat Sep 22 2012 Soren Sandmann <ssp@redhat.com> 0.1.0-1
- Upstream 0.1.0

* Wed Aug 29 2012 Adam Jackson <ajax@redhat.com> 0.0.22-6
- Exclude Xspice from RHEL6 builds

* Sun Aug 26 2012 Alon Levy <alevy@redhat.com>
- fix uxa_xorg_enable_disable_fb_access - 0.0.22-5.20120718gitde6620788 (#844463)

* Thu Aug 23 2012 Alon Levy <alevy@redhat.com>
- fix break from introduction of screen privates - 0.0.22-4.20120718gitde6620788 (#844463)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.22-3.20120718gitde6620788
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Dave Airlie <airlied@redhat.com> 0.0.22-2.20120718gitde6620788
- git snapshot for new server API

* Thu Apr 05 2012 Adam Jackson <ajax@redhat.com> - 0.0.22-1
- RHEL arch exclude updates

* Thu Mar 15 2012 Soren Sandmann <ssp@redhat.com> - 0.22.0
- Upstream 0.0.17

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.0.21-16
- ABI rebuild

* Fri Feb 10 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.0.21-15
- ABI rebuild

* Tue Jan 24 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.0.21-14
- ABI rebuild

* Fri Jan 13 2012 Marc-André Lureau <mlureau@redhat.com> 0.0.21-13
- Add 0011-support-_ASYNC-io-calls-and-interrupt-handling-busy-.patch
  to use async calls

* Wed Jan 04 2012 Adam Jackson <ajax@redhat.com> 0.0.21-12
- qxl-0.0.16-ftbfs.patch: Fix some FTBFS.

* Wed Nov 16 2011 Adam Jackson <ajax@redhat.com> 0.0.21-11
- qxl-0.0.16-vgahw.patch: API compat for xserver 1.12 (#753928)

* Mon Nov 14 2011 Adam Jackson <ajax@redhat.com> - 0.0.21-10
- ABI rebuild

* Wed Nov 09 2011 Adam Jackson <ajax@redhat.com> - 0.0.21-9
- ABI rebuild

* Fri Oct 28 2011 Soren Sandmann <ssp@redhat.com> - 0.0.21-8
- Bump release

* Fri Oct 28 2011 Soren Sandmann <ssp@redhat.com> - 0.0.21-7
- Add patch to translate access regions according to drawable offset
  Bug 731245.

* Thu Oct 27 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.21-7
- Rebuilt for glibc bug#747377

* Wed Oct 26 2011 Soren Sandmann <ssp@redhat.com> - 0.0.21-6
- Add patch to confine access regions to the bounds of the drawable.
  Bug 731245.

* Mon Sep 12 2011 Hans de Goede <hdegoede@redhat.com> - 0.0.21-5
- Rebase to latest upstream release
- Enable building of the Xspice X-server and put it in its own
  xorg-x11-server-Xspice package

* Thu Aug 18 2011 Adam Jackson <ajax@redhat.com> - 0.0.21-4
- Rebuild for xserver 1.11 ABI

* Wed Apr 20 2011 Hans de Goede <hdegoede@redhat.com> 0.0.21-3
- Add various bugfixes from upstream git
- Fixes VT-switching (rhbz#696711)
- Add support for old qxl device (from rhel6 branch) (rhbz#642153)

* Mon Mar 07 2011 Dave Airlie <airlied@redhat.com> 0.0.21-2
- Bump to for abi rebuild

* Sat Feb 12 2011 Soren Sandmann <ssp@redhat.com> 0.0.21-1
- New version number to make sure upgrading works

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Soren Sandmann <ssp@redhat.com> 0.0.13-1
- Update to 0.0.13 with surfaces

* Mon Dec 06 2010 Adam Jackson <ajax@redhat.com> 0.0.20.f14b-10
- Rebuild for new server ABI.

* Wed Oct 27 2010 Adam Jackson <ajax@redhat.com> 0.0.20.f14b-8
- Add ABI requires magic (#542742)

* Sun Oct 17 2010 Hans de Goede <hdegoede@redhat.com> 0.0.20.f14b-7
- Fix notification bubbles under gnome not showing (backport from the
  surface-fixes branch)

* Sun Oct 17 2010 Hans de Goede <hdegoede@redhat.com> 0.0.20.f14b-6
- Fix a pointer casting bug which causes the qxl driver to trigger an
  assertion in the qxl device terminating the entire virtual machine

* Mon Oct 11 2010 Hans de Goede <hdegoede@redhat.com> 0.0.20.f14b-5
- Don't access the qxl device when our vt is not focussed, this fixes
  Xorg crashing when switching to a text vc

* Sun Oct 10 2010 Hans de Goede <hdegoede@redhat.com> 0.0.20.f14b-4
- Fix the driver not working on qxl devices with a framebuffer of 8MB

* Sat Oct  9 2010 Hans de Goede <hdegoede@redhat.com> 0.0.20.f14b-3
- Add support for using resolutions > 1024x768 without needing an xorg.conf
- Restore textmode font when switching back to a textmode virtual console

* Fri Oct 08 2010 Jesse Keating <jkeating@redhat.com> - 0.0.20.f14b-2.1
- Rebuild for gcc bug 634757

* Tue Sep 14 2010 Soren Sandmann <ssp@redhat.com> 0.0.20.f14b-2
- Patch to fix it up for the new privates ABI (I had apparently been
  testing with a too old X server).

* Tue Sep 14 2010 Soren Sandmann <ssp@redhat.com> 0.0.20.f14b-1
- Add support for new device

* Sat Mar 13 2010 Dave Airlie <airlied@redhat.com> 0.0.12-2
- fix bug in qxl with asserts

* Sat Mar 13 2010 Dave Airlie <airlied@redhat.com> 0.0.12-1
- rebase to 0.0.12 release - fix some 16-bit bugs

* Mon Jan 11 2010 Dave Airlie <airlied@redhat.com> 0.0.9-0.1
- Initial public release 0.0.9
