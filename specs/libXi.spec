%global tarball libXi
#global gitdate 20130524
%global gitversion 661c45ca1

Summary: X.Org X11 libXi runtime library
Name: libXi
Version: 1.8.2
Release: 3%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT-open-group AND SMLNJ AND MIT
URL: http://www.x.org

%if 0%{?gitdate}
Source0:    %{tarball}-%{gitdate}.tar.bz2
Source1:    make-git-snapshot.sh
%else
Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
%endif

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel
BuildRequires: pkgconfig(inputproto) >= 2.3.99.1
BuildRequires: libX11-devel >= 1.5.99.902
BuildRequires: libXext-devel libXfixes-devel
BuildRequires: xmlto asciidoc >= 8.4.5

Requires: libX11 >= 1.5.99.902

%description
X.Org X11 libXi runtime library

%package devel
Summary: X.Org X11 libXi development package
Requires: %{name} = %{version}-%{release}
# required by xi.pc
Requires: xorg-x11-proto-devel
Requires: pkgconfig

%description devel
X.Org X11 libXi development package

%prep
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install || exit 1
%configure --disable-specs \
	   --disable-static

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING
%{_libdir}/libXi.so.6
%{_libdir}/libXi.so.6.1.0

%files devel
%{_includedir}/X11/extensions/XInput.h
%{_includedir}/X11/extensions/XInput2.h
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
%{_mandir}/man3/*.3*

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 05 2024 Peter Hutterer <peter.hutterer@redhat.com> - 1.8.2-1
- libXi 1.8.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 06 2023 Benjamin Tissoires <benjamin.tissoires@redhat.com> - 1.8.1-3
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 04 2023 Peter Hutterer <peter.hutterer@redhat.com> - 1.8.1-1
- libXi 1.8.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 16 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.8-1
- libXi 1.8

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 11:25:48 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.10-5
- Add BuildRequires for make

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Adam Jackson <ajax@redhat.com> - 1.7.10-1
- libXi 1.7.10

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 1.7.9-7
- Use ldconfig scriptlet macros

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.9-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Peter Hutterer <peter.hutterer@redhat.com> 1.7.9-1
- libXi 1.7.9

* Tue Oct 25 2016 Peter Hutterer <peter.hutterer@redhat.com> 1.7.8-2
- libXi 1.7.8

* Thu Oct 13 2016 Peter Hutterer <peter.hutterer@redhat.com> 1.7.7-2
- Fix crash when calling XListInputDevices on devices without classes

* Wed Oct 05 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.7.7-1
- libXi 1.7.7
- fixes CVE-2016-7945, CVE-2016-7946

* Fri Mar 25 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com>
- Fix release string: %%{dist} -> %%{?dist}

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Peter Hutterer <peter.hutterer@redhat.com>
- Remove unnecessary defattr

* Tue Jan 05 2016 Peter Hutterer <peter.hutterer@redhat.com>
- Drop the optional disable-static, it's been disabled for years now.

* Tue Dec 22 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.7.6-1
- libXi 1.7.6
- drop unused mandir creation

* Thu Sep 10 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.7.5-1
- libXi 1.7.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.7.4-1
- libXi 1.7.4

* Thu Jul 10 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.7.3-1
- libXi 1.7.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.7.2-1
- libXi 1.7.2

* Thu Jun 27 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.7.1.901-1
- libXi 1.7.1.901

* Mon May 27 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.7.1-5.20130524git661c45ca1
- Require libX11 1.6RC2 for _XEatDataWords

* Fri May 24 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.7.1-4.20130524git661c45ca1
- Udpate to git snapshot to fix CVEs listed below
- CVE-2013-1984
- CVE-2013-1995
- CVE-2013-1998

* Tue May 21 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.7.1-3
- fix sequence number copy - the cookie already had (a potentially
  different) sequence number copied (#965347)

* Fri May 17 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.7.1-2
- copy the sequence number into XI2 events

* Fri Apr 05 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.7.1-1
- libXi 1.7.1

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.7-1
- libXi 1.7

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Adam Jackson <ajax@redhat.com> 1.6.99.1-1
- libXi 1.6.99.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.6.1-1
- libXi 1.6.1

* Thu Mar 08 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.6.0-1
- libXi 1.6

* Wed Feb 15 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.5.99.3-1
- libXi 1.5.99.3

* Mon Feb 06 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.5.99.2-4
- Add requires for libX11 to avoid mismatches when updating

* Fri Jan 27 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.5.99.2-3
- Bump libX11-devel requirement up to what configure actually wants

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.99.2-2.20111222gitae0187c87
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.5.99.2-1.20111222.gitae0187c87
- 1.5.99.2 from git

* Wed Dec 21 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-1
- libXi 1.5.0

* Wed Nov 09 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.4.99.1-1
- Update to 1.4.99.1 (with XI 2.1 support)

* Tue Oct 11 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.4.3-3
- Fix 0001-Handle-unknown-device-classes.patch: missing prototype change for
  copy_classes in XIQueryDevice caused parameter corruption (#744960)

* Wed Aug 17 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.4.3-2
- 0001-Handle-unknown-device-classes.patch: don't corrupt memory when a
  server sends unknown device classes.

* Tue Jun 07 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.4.3-1
- libXi 1.4.3

* Mon Mar 21 2011 Adam Jackson <ajax@redhat.com> 1.4.2-1
- libXi 1.4.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.4.1-1
- libXi 1.4.1

* Wed Nov 03 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.4.0-1
- libXi 1.4
- disable spec building, don't think they're of much of much use to our
  users.

* Wed Aug 04 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.3.2-1
- libXi 1.3.2
  libXi 1.3.1 had a bug in the configure script.

* Mon Aug 02 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.3.1-1
- libXi 1.3.1

* Tue Feb 02 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.3-2
- Remove unnecessary libXau-devel BuildRequires.

* Tue Oct 06 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.3-1
- libXi 1.3

* Tue Aug 25 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-11.20090825
- Update to today's git master, requires inputproto 1.9.99.902

* Wed Aug 05 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-10.20090805
- Update to today's git master
- Re-enable parallel builds, the man page makefile is fixed now.

* Tue Aug 04 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-9.20090804
- Update to today's git master

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.99-8.20090723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.2.99-7.20090723
- Un-require xorg-x11-filesystem

* Thu Jul 23 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-6.20090723
- Update to today's git master

* Thu Jul 16 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-5.20090716
- Update to today's git master

* Mon Jul 13 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-4.20090713
- Update to today's git master
- Add commitid file.

* Sun Jul 12 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-3.20090712
- Update to today's git master

* Fri Jun 19 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-2.20090619
- Add missing make-git-snapshot.sh

* Fri Jun 19 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-1.20090619
- Update to today's git master

* Thu Feb 26 2009 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.1-1
- libXi 1.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 03 2008 Adam Jackson <ajax@redhat.com> 1.2.0-1
- libXi 1.2.0

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.3-4
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.1.3-3
- Fix pkconfig type on -devel.

* Fri Jan 11 2008 parag <paragn@fedoraproject.org> 1.1.3-2
- Merge-review #226076
- Removed BR:pkgconfig
- Removed XFree86-libs, xorg-x11-libs XFree86-devel, xorg-x11-devel as Obsoletes
- Removed zero-length AUTHORS README file

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 1.1.3-1
- libXi 1.1.3

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.1.1-2
- Rebuild for build id

* Wed Jul 11 2007 Adam Jackson <ajax@redhat.com> 1.1.1-1
- libXi 1.1.1

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 1.0.4-2
- Don't install INSTALL

* Wed Apr 11 2007 Adam Jackson <ajax@redhat.com> 1.0.4-1
- libXi 1.0.4

* Mon Nov 20 2006 Adam Jackson <ajax@redhat.com> 1.0.2-1
- Update to 1.0.2

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-3.1
- rebuild

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-3
- Added "Requires: xorg-x11-proto-devel" to devel package for xi.pc
- Remove package ownership of mandir/libdir/etc.

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-2
- Replace "makeinstall" with "make install DESTDIR=..." for (#192721)
- Remove package ownership of mandir/libdir/etc.

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1.0.1-1
- Update to 1.0.1

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 23 2006 Mike A. Harris <mharris@redhat.com> 1.0.0-2
- Bumped and rebuilt

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated libXi to version 1.0.0 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Updated libXi to version 0.99.2 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Tue Nov 15 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-3
- Added "BuildRequires: libXau-devel", as build fails without it, but does
  not check for it with ./configure.  Bug (fdo#5065)

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'

* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated libXi to version 0.99.1 from X11R7 RC1
- Updated file manifest to find manpages in "man3x"

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.
