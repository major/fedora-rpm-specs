Summary: A high quality TV viewer
Name: tvtime
Version: 1.0.10
Release: 24%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://tvtime.sourceforge.net
Source0: http://linuxtv.org/downloads/%{name}/%{name}-%{version}.tar.gz
Patch0:  tvtime-1.0.10-honor-cflags.patch
Patch1:  tvtime-1.0.10-fix-v-crash.patch
Patch2:  tvtime-1.0.10-rdtsc-x86_64.patch 
Patch3:  tvtime-1.0.10-fix-crash-on-no-v4ldevs.patch
Patch4:  0001-xvoutput-print-an-error-if-create_shm-fails.patch
Patch5:  0002-xvtvoutput-make-it-work-fine-under-remote-access-ssh.patch
Patch6:  0003-Fix-bitwise-comparison-always-evaluates-to-false-com.patch
Patch7:  0004-Fix-warning-implicit-declaration-of-function-minor-m.patch
BuildRequires: make
BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: freetype-devel >= 2.0
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: SDL-devel
BuildRequires: libxml2-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXinerama-devel
BuildRequires: libXtst-devel
BuildRequires: libXv-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXt-devel
BuildRequires: libXi-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libtool gettext-devel
BuildRequires: desktop-file-utils libappstream-glib
Requires: hicolor-icon-theme
ExcludeArch: s390 s390x

%description
tvtime is a high quality television application for use with video
capture cards.  tvtime processes the input from a capture card and
displays it on a computer monitor or projector.  Unlike other television
applications, tvtime focuses on high visual quality making it ideal for
videophiles.


%prep
%autosetup -p1
autoreconf -ifv


%build
%configure --disable-dependency-tracking --disable-rpath
make %{?_smp_mflags} V=1


%install
%make_install INSTALL="install -p"
%find_lang %{name}
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files -f %{name}.lang
%doc AUTHORS ChangeLog  NEWS README* docs/html
%license COPYING COPYING.LGPL data/COPYING*
%dir %{_sysconfdir}/tvtime/
%config(noreplace) %{_sysconfdir}/tvtime/tvtime.xml
%{_bindir}/tvtime
%{_bindir}/tvtime-command
%{_bindir}/tvtime-configure
%{_bindir}/tvtime-scanner
%{_datadir}/appdata/tvtime.appdata.xml
%{_datadir}/applications/tvtime.desktop
%{_datadir}/icons/hicolor/*/apps/tvtime.png
%{_datadir}/tvtime/
%{_mandir}/man?/*
%lang(de) %{_mandir}/de/man?/*
%lang(es) %{_mandir}/es/man?/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.10-23
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Hans de Goede <hdegoede@redhat.com> - 1.0.10-10
- Fix FTBFS (rhbz#1606593)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.10-7
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 26 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.10-3
- Fix crash when started on system with no v4ldevs

* Wed Mar  9 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.10-2
- Honor CFLAGS (no -03 no -fomit-framepointer) when building
- Fix crash when running "tvtime -v" on x86_64 (rhbz1315619)

* Sat Feb 27 2016 Mauro Carvalho Chehab <mchehab@osg.samsung.com> - 1.0.10-1
- Update language translations and merge Hans patches upstream

* Sun Feb 14 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.8-4
- Add a bunch of patches from upstream:
 - Add support for glamor Xv output
 - Digital audio loopback fixes + autodetect capture devices
 - Save / restore matte setting on quit / startup
 - Add appdata
 - Add Catalan translation (rhbz#1306596)
- Modernize spec a bit

* Thu Feb 11 2016 Tomas Smetana <tsmetana@redhat.com> - 1.0.8-3
- Prevent gcc from using the C++11 preprocessor features: this "fixes" the
  build failures onn F24 and newer.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 18 2015 Mauro Carvalho Chehab <mchehab@osg.samsung.com> - 1.0.8-1
- Update language translations and fixes some bugs

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan  7 2015 Mauro Carvalho Chehab <mchehab@osg.samsung.com> - 1.0.6-1
- Update to version 1.0.6, fixing default ALSA mixer

* Tue Dec 23 2014 Mauro Carvalho Chehab <mchehab@osg.samsung.com> - 1.0.5-1
- Update to version 1.0.5, with several fixes

* Mon Sep 08 2014 Tomas Smetana <tsmetana@redhat.com> - 1.0.2-29
- Fix tvtime-scanner crash with home unset (#1000210)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Tomas Smetana <tsmetana@redhat.com> - 1.0.2-27
- Fix build error with -Werror=format-security (#1037367, #1107467)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Tomas Smetana <tsmetana@redhat.com> - 1.0.2-24
- fix #926664 call autoreconf -ivf during build to add support for aarch64

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 06 2012 Tomas Smetana <tsmetana@redhat.com> - 1.0.2-22
- fix #829901: errors in setting of the _NET_WM_ICON property

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar  5 2012 Tom Callaway <spot@fedoraproject.org> - 1.0.2-20
- fix code to build properly against libpng 1.5

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.2-18
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Tomas Smetana <tsmetana@redhat.com> 1.0.2-16
- fix #655038 - tvtime does not work with UVC webcams

* Mon Nov 08 2010 Tomas Smetana <tsmetana@redhat.com> 1.0.2-15
- fix #571339 use a saner way to disable screensaver, thanks to Debian folks
  for the patch, namely Resul Cetin

* Fri Nov 05 2010 Tomas Smetana <tsmetana@redhat.com> 1.0.2-14
- rebuild with new libxml

* Mon Jan 04 2010 Tomas Smetana <tsmetana@redhat.com> 1.0.2-13
- finish merge review (#226508)
- revert the font-related patch; continue shipping tvtime's specific fonts

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Tomas Smetana <tsmetana@redhat.com> 1.0.2-11
- fix a typo in the default config file

* Sun Jun 28 2009 Tomas Smetana <tsmetana@redhat.com> 1.0.2-10
- fix BuildRequires (XInput.h has moved...)

* Sun Jun 28 2009 Tomas Smetana <tsmetana@redhat.com> 1.0.2-9
- try to document the new ALSA mixer settings, make ALSA mixer
  the default one

* Mon Jun 01 2009 Tomas Smetana <tsmetana@redhat.com> 1.0.2-8
- merge review round two; thanks to Jussi Lehtola

* Sun May 31 2009 Tomas Smetana <tsmetana@redhat.com> 1.0.2-7
- fix conflicting types for locale_t
- fix build requires for rawhide

* Sun May 31 2009 Tomas Smetana <tsmetana@redhat.com> 1.0.2-6
- fix #498167 - patch by Philipp Hahn adding ALSA mixer support
- merge review changes

* Tue Mar 03 2009 Tomas Smetana <tsmetana@redhat.com> 1.0.2-5
- fix font requirements

* Mon Mar 02 2009 Tomas Smetana <tsmetana@redhat.com> 1.0.2-4
- fix #477473 - drop fonts, depend on liberation-fonts

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 03 2008 Tomas Smetana <tsmetana@redhat.com> 1.0.2-2
- compile with $RPM_OPT_FLAGS

* Mon Mar 10 2008 Tomas Smetana <tsmetana@redhat.com> 1.0.2-1
- update to 1.0.2

* Thu Mar 06 2008 Tomas Smetana <tsmetana@redhat.com> 1.0.1-8
- fix #235622 - X error when toggling fullscreen

* Tue Feb 12 2008 Tomas Smetana <tsmetana@redhat.com> 1.0.1-7
- fix license tag and summary
- rebuild (gcc-4.3)

* Thu Jul 13 2006 Than Ngo <than@redhat.com> 1.0.1-6
- fix build problem

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-5.1
- rebuild

* Tue May 16 2006 Than Ngo <than@redhat.com> 1.0.1-5 
- add BR on libXt-devel

* Mon Feb 27 2006 Than Ngo <than@redhat.com> 1.0.1-4
- fix post install script error #182895

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 23 2005 Than Ngo <than@redhat.com> 1.0.1-3
- fix build problem with gcc4.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov 15 2005 Than Ngo <than@redhat.com> 1.0.1-2 
- fix for modular X

* Mon Sep 12 2005 Than Ngo <than@redhat.com> 1.0.1-1
- update to 1.0.1

* Wed Aug 17 2005 Than Ngo <than@redhat.com> 0.99-2
- rebuilt

* Tue Jul 19 2005 Than Ngo <than@redhat.com> 0.99-1
- update to 0.99
- fix gcc4 build problem

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 0.9.15-7
- silence %%post

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 0.9.15-5
- Update the GTK+ theme icon cache on (un)install

* Sat Mar 05 2005 Than Ngo <than@redhat.com> 0.9.15-4
- rebuilt

* Mon Nov 22 2004 Miloslav Trmac <mitr@redhat.com> - 0.9.15-3
- Convert German man pages to UTF-8

* Tue Nov 16 2004 Than Ngo <than@redhat.com> 0.9.15-2
- remove suid root

* Sun Oct 31 2004 Than Ngo <than@redhat.com> 0.9.15-1
- update to 0.9.15

* Fri Oct 29 2004 Than Ngo <than@redhat.com> 0.9.14-2
- fix build problem on x86_64

* Fri Oct 29 2004 Than Ngo <than@redhat.com> 0.9.14-1
- update to 0.9.14

* Wed Sep 29 2004 Than Ngo <than@redhat.com> 0.9.13-1
- update to 0.9.13

* Mon Jun 21 2004 Than Ngo <than@redhat.com> 0.9.12-10
- fix gcc-3.4 build problem, thank to Jakub

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 24 2004 Than Ngo <than@redhat.com> 0.9.12-8
- add another patch to enable PIE build of tvtime binary

* Mon May 17 2004 Than Ngo <than@redhat.com> 0.9.12-7
- add patch to enable PIE build

* Mon Apr 19 2004 Than Ngo <than@redhat.com> 0.9.12-6
- add BuildRequires: libxml2-devel, bug #121237

* Tue Mar 16 2004 Mike A. Harris <mharris@redhat.com 0.9.12-5
- BuildRequires: s/XFree86-libs/XFree86-devel/

* Thu Mar 11 2004 Than Ngo <than@redhat.com> 0.9.12-4
- fixed gcc-3.4 build problem

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Dec 04 2003 Than Ngo <than@redhat.com> 0.9.12-2
- get rid of unused vsync.c code, which is broken on ppc/ppc64.

* Wed Dec 03 2003 Than Ngo <than@redhat.com> 0.9.12-1
- 0.9.12 release

* Mon Nov 10 2003 Than Ngo <than@redhat.com> 0.9.10-2
- built into new Fedora tree

* Mon Oct 13 2003 Than Ngo <than@redhat.com> 0.9.10-1
- 0.9.10
