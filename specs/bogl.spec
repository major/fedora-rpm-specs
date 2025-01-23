Summary: A terminal program for displaying Unicode on the console
Name: bogl
Version: 0.1.18
Release: 55%{?dist}
URL: http://packages.debian.org/unstable/source/bogl
Source0: http://update2.intellique.com/repository/archive/pool/main/b/bogl/bogl_0.1.18-1.5.tar.gz
Source1: 14x14cjk.bdf.gz
Patch0: bogl-0.1.18-1.1.sigchld.patch
Patch1: bogl-0.1.18-1.2.reduce-font.patch
Patch2: bogl-0.1.18-1.2.gzip-fonts.patch
Patch3: bogl-0.1.18-1.2.term.patch
Patch4: bogl-0.1.18-1.5.rh.patch
Patch5: bogl-0.1.9-2.6fbdev.patch
Patch6: bogl-0.1.18-noexecstack.patch
Patch7: bogl-0.1.18-format-security.patch
Patch8: bogl-0.1.18-fix-multiple-definition.patch
Patch9: bogl-0.1.18-gcc15-fixes.patch
Epoch: 0
License: GPL-2.0-or-later
BuildRequires: gcc
BuildRequires: gd-devel
BuildRequires: libpng-devel
BuildRequires: ncurses
BuildRequires: make

%description
BOGL stands for Ben's Own Graphics Library.  It is a small graphics
library for Linux kernel frame buffers.  It supports only very simple
graphics.

%package devel
Summary: Development files required to build BOGL applications
Requires: bogl = %{epoch}:%{version}-%{release}

%description devel
The bogl-devel package contains the static libraries and header files
for writing BOGL applications.

%package bterm
Summary: A Unicode capable terminal program for the Linux frame buffer
# Only for /usr/share/terminfo/b
Requires: ncurses-base

%description bterm
The bterm application is a terminal emulator that displays to a Linux
frame buffer.  It is able to display Unicode text on the console.

%prep
%setup -q -n bogl-0.1.18
%patch -P0 -p1 -b .sigchld
%patch -P1 -p1 -b .reduce-font
%patch -P2 -p1 -b .gzip-fonts
%patch -P3 -p1 -b .term
%patch -P4 -p1 -b .rh
%patch -P5 -p1 -b .26fbdev
%patch -P6 -p1 -b .noexecstack
%patch -P7 -p1 -b .format-security
%patch -P8 -p1 -b .fix-multiple-definition
%patch -P9 -p1 -b .gcc15-fixes

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"
gunzip -c %{SOURCE1} > font.bdf
./bdftobogl -b font.bdf > font.bgf

%install
rm -rf $RPM_BUILD_ROOT
make CFLAGS="$RPM_OPT_FLAGS" DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir} install
mkdir -p $RPM_BUILD_ROOT/usr/share/bogl/
cp font.bgf $RPM_BUILD_ROOT/usr/share/bogl/
gzip -9 $RPM_BUILD_ROOT/usr/share/bogl/font.bgf
# remove /usr/share/terminfo/b/bterm - shipped in ncurses-base
rm $RPM_BUILD_ROOT/%{_datadir}/terminfo/b/bterm

%ldconfig_scriptlets

%files
%doc ChangeLog README debian/copyright
%{_libdir}/*.so.*

%files devel
%{_bindir}/bdftobogl
%{_bindir}/mergebdf
%{_bindir}/pngtobogl
%{_bindir}/reduce-font
%exclude %{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/bogl

%files bterm
%doc README.BOGL-bterm debian/copyright
%{_bindir}/bterm
/usr/share/bogl

%changelog
* Tue Jan 21 2025 Vitezslav Crhonek <vcrhonek@redhat.com> - 0:0.1.18-55
- Fix FTBFS with GCC 15

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Vitezslav Crhonek <vcrhonek@redhat.com> - 0:0.1.18-49
- SPDX migration

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.1.18-43
- Add ncurses to build required packages
  Resoves: #1863281

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-42
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.1.18-40
- Fix source URL
- Fix multiple definiton of variables (FTBFS with GCC 10)
  Resolves: #1799196

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Vitezslav Crhonek <vcrhonek@redhat.com> - 0:0.1.18-35
- Add BuildRequires gcc
- Remove Group tag

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.1.18-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.1.18-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.1.18-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.1.18-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 04 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 0:0.1.18-26
- Fix bogl FTBFS if "-Werror=format-security" flag is used (patch by Dhiru Kholia)
  Resolves: #1037002
- Fix bogus date in %%changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.1.18-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 0:0.1.18-24
- rebuild for new GD 2.1.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.1.18-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.1.18-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.1.18-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0:0.1.18-20
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.1.18-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 0:0.1.18-18
- Remove bterm terminfo entry (it's shipped already in ncurses-base)
  Resolves: #622160
- Fix source URL, add dist tag

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.1.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.1.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:0.1.18-15
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:0.1.18-14
- Autorebuild for GCC 4.3

* Fri Nov 10 2006 Miloslav Trmac <mitr@redhat.com> - 0:0.1.18-13
- Add URL:
- Preserve modification date of header files
- Ship debian/copyright
- Compile all files with $RPM_OPT_FLAGS

* Sun Nov  5 2006 Miloslav Trmac <mitr@redhat.com> - 0:0.1.18-12
- Update to bogl-0.1.18-1.5
- Drop wlite
- Split rh.patch by functionality
- Move the default font to /usr/share/bogl, don't ship it as BDF
- Change to conform to Fedora packaging guidelines

* Tue Oct 17 2006 Miloslav Trmac <mitr@redhat.com> - 0:0.1.18-11.2.1.el5.1
- Rebuild for RHEL 5
- Use sysconf(_SC_PAGE_SIZE) instead <asm/param.h> to fix build on IA-64

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0:0.1.18-11.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0:0.1.18-11.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Sep 22 2005 Miloslav Trmac <mitr@redhat.com> - 0:0.1.18-11
- Update to bogl-0.1.18-1.2

* Tue Sep 20 2005 Miloslav Trmac <mitr@redhat.com> - 0:0.1.18-10
- Simplify overzealous bogl-0.1.18-1.1.sigchld.patch

* Tue Sep 20 2005 Miloslav Trmac <mitr@redhat.com> - 0:0.1.18-9
- Update to bogl-0.1.18-1.1
- Don't ship unused ucs fonts in the SRPM
- Remove obsolete URL: (#168673)

* Sun Sep 18 2005 Miloslav Trmac <mitr@redhat.com> - 0:0.1.18-8
- Ship wlite and Unicode data licenses, and Changelog

* Fri Mar  4 2005 Miloslav Trmac <mitr@redhat.com> - 0:0.1.18-7
- Add missing includes in bogl-0.1.18-rh.patch
- Rebuild with gcc 4

* Thu Feb 17 2005 Miloslav Trmac <mitr@redhat.com> - 0:0.1.18-6
- Don't require executable stack
- Fix build with gcc 4
- Use $RPM_OPT_FLAGS

* Tue Nov 23 2004 Jeremy Katz <katzj@redhat.com> - 0:0.1.18-5
- don't build against dietlibc anymore on x86

* Wed Oct 20 2004 Jeremy Katz <katzj@redhat.com> - 0:0.1.18-4
- rebuild again

* Tue Oct 19 2004 Jeremy Katz <katzj@redhat.com> - 0:0.1.18-3
- rebuild against newer diet with fixed signal handling

* Mon Sep  6 2004 Jeremy Katz <katzj@redhat.com> - 0:0.1.18-2
- fPIC on ppc too (#130719)

* Mon Jul 05 2004 Akira TAGOH <tagoh@redhat.com> 0:0.1.18-1
- New upstream release.
  #113910 has been fixed in this release.
- bogl-0.1.18-rh.patch: updated to be able to apply it for this release.
- bogl-0.1.9-vga16-others.patch: removed. no need this patch anymore.

* Fri Jun 18 2004 Jeremy Katz <katzj@redhat.com> - 0:0.1.9-33
- fix build with gcc 3.4

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 18 2004 Jeremy Katz <katzj@redhat.com> - 0:0.1.9-31
- fix build

* Tue Feb 17 2004 Jeremy Katz <katzj@redhat.com> - 0:0.1.9-30
- fix to work with changed 2.6 fbdev semantics

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Dec 15 2003 Matt Wilson <msw@redhat.com> 0:0.1.9-28
- add BuildRequires: gd-devel, libpng-devel (#111165)

* Mon Aug 25 2003 Jeremy Katz <katzj@redhat.com> 0:0.1.9-27
- add hack to fix #92240

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri May 30 2003 Matt Wilson <msw@redhat.com> 0:0.1.9-25
- rebuild

* Fri May 30 2003 Matt Wilson <msw@redhat.com> 0:0.1.9-24
- enable vga16 support on ia64
- removed workaround for AMD64, kernel should be fixed now

* Tue May 06 2003 Phil Knirsch <pknirsch@redhat.com>  0:0.1.9-23
- Bumped release and rebuilt due to new gd version.

* Wed Apr  2 2003 Matt Wilson <msw@redhat.com> 0:0.1.9-22
- add a workaround for AMD64 that calls iopl(3) in order to gain io
  port access until ioperm() is fixed (#87835).  Workaround for
  (#86321)
- gzip font.bgf

* Wed Mar 19 2003 Jeremy Katz <katzj@redhat.com> 0:0.1.9-21
- include vga16fb support on x86_64 (#86321)

* Thu Feb 13 2003 Adrian Havill <havill@redhat.com> 0:0.1.9-20
- Change the font combo to add zh, change ja to k14 (#81717, #82888)

* Tue Feb 11 2003 Jeremy Katz <katzj@redhat.com> 0:0.1.9-19
- actually do the test correctly
- buildrequire dietlibc on i386

* Tue Feb 11 2003 Jeremy Katz <katzj@redhat.com> 0:0.1.9-18
- only fPIC on needed arches, and do it everywhere

* Mon Feb 10 2003 Matt Wilson <msw@redhat.com> 0:0.1.9-17
- always use wlite for bogl/bterm (for now) (#83980)
  (this makes bterm useless for any non-UTF-8 locale)
- fixed 'bterm' for the normal usage case

* Mon Feb  3 2003 Matt Wilson <msw@redhat.com> 0:0.1.9-16
- add back the Epoch: to support upgrading from betas

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec 30 2002 Jeremy Katz <katzj@redhat.com> 0.1.9-14
- build wlite with -fPIC
- fix deps of subpackages

* Sun Dec 29 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- delete "Epoch: 0" line in spec file

* Mon Dec 16 2002 Adrian Havill <havill@redhat.com> 0.1.9-12
- added bogl.bdf.gz to allow us to reduce-font in loader build

* Mon Dec 16 2002 Adrian Havill <havill@redhat.com> 0.1.9-11
- fixed broken reduce-font to test ENCODING x instead of STARTCHAR x

* Mon Dec 16 2002 Matt Wilson <msw@redhat.com> 0.1.9-10
- made more changes to the rh patch to enable bogl embedding insode loader

* Tue Dec 10 2002 Matt Wilson <msw@redhat.com>
- use all fb drivers on non-i386
- package wlite for use in loader
- use %%{_libdir} to get lib64 right

* Tue Dec 10 2002 Adrian Havill <havill@redhat.com>
- swapped out utf8 code with new and improved wlite

* Tue Nov 26 2002 Adrian Havill <havill@redhat.com>
- re-write font loader so it can load uncompressed or gzipped files
- utf8 lib updated
- fixed bug in bogl_term_new() so struct is inited (s/malloc/calloc/)
- added term bell (screen flash)
- changed background/foreground to pretty pretty blue/white

* Thu Nov 21 2002 Adrian Havill <havill@redhat.com>
- updated utf8 library
- made bogl_term_out reset the state at every call so glibc
  and utf8.c behave consistently
- concatenated two Red Hat diff patches

* Wed Nov 20 2002 Adrian Havill <havill@redhat.com>
- changed behavior of bogl_term_out to queue and save UTF broken between two
  buffers
- utf8 lib improvements

* Thu Nov 14 2002 root <msw@redhat.com>
- integrate havill's utf8 for diet libs
- build and install font

* Tue Jul 23 2002 Matt Wilson <msw@redhat.com>
- Initial build.
