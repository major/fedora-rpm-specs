%global tarball libXrender
#global gitdate 20130524
%global gitversion 786f78fd8

Summary: X.Org X11 libXrender runtime library
Name: libXrender
Version: 0.9.12
Release: 3%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: HPND-sell-variant
URL: http://www.x.org

%if 0%{?gitdate}
Source0:    %{tarball}-%{gitdate}.tar.bz2
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
%endif

Requires: libX11 >= 1.5.99.902

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig
BuildRequires: libX11-devel >= 1.5.99.902

%description
X.Org X11 libXrender runtime library

%package devel
Summary: X.Org X11 libXrender development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXrender development package

%prep
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
# undo this, we'll add it ourselves in %%doc
rm $RPM_BUILD_ROOT/%{_docdir}/*/libXrender.txt

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING
%{_libdir}/libXrender.so.1
%{_libdir}/libXrender.so.1.3.0

%files devel
%doc doc/libXrender.txt
%{_includedir}/X11/extensions/Xrender.h
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 José Expósito <jexposit@redhat.com> - 0.9.12-1
- libXrender 0.9.12

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 06 2023 Benjamin Tissoires <benjamin.tissoires@redhat.com> - 0.9.11-4
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 04 2022 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.9.11-1
- libXrender 0.9.11-1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 12:26:07 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 0.9.10-13
- Add BuildRequires for make

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Adam Jackson <ajax@redhat.com> - 0.9.10-7
- Drop useless %%defattr

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 0.9.10-6
- Use ldconfig scriptlet macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 05 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.9.10-1
- libXrender 0.9.10
- fixes CVE-2016-7949, CVE-2016-7950

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Adam Jackson <ajax@redhat.com> 0.9.9-1
- libXrender 0.9.9

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.9.8-1
- libXrender 0.9.8

* Mon May 27 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.9.7-6.20130524git786f78fd8
- Require libX11 1.6RC2 for _XEatDataWords

* Fri May 24 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.9.7-5.20130524git786f78fd8
- Update to git snapshot to fix CVEs listed below:
- CVE-2013-1987

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.9.7-4
- autoreconf for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 08 2012 Adam Jackson <ajax@redhat.com> 0.9.7-1
- libXrender 0.9.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 09 2010 Peter Hutterer <peter.hutterer@redhat.com> 0.9.6-1
- libXrender 0.9.6

* Tue Oct 06 2009 Adam Jackson <ajax@redhat.com> 0.9.5-1
- libXrender 0.9.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 0.9.4-6
- Un-require xorg-x11-filesystem
- Remove useless %%dir

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 03 2008 Caolán McNamara <caolanm@redhat.com> - 0.9.4-4
- rebuild to get provides pkgconfig(xrender)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.4-3
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 parag <paragn@fedoraproject.org> 0.9.4-2
- Merge-Review #226084
- Removed BR:pkgconfig 
- Removed XFree86-libs, xorg-x11-libs XFree86-devel, xorg-x11-devel as Obsoletes
- Removed zero-length README file

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 0.9.4-1
- libXrender 0.9.4

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> 0.9.3-1
- libXrender 0.9.3

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 0.9.2-2
- Don't install INSTALL

* Mon Nov 20 2006 Adam Jackson <ajax@redhat.com> 0.9.2-1
- Update to 0.9.2

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 0.9.1-3.1
- rebuild

* Fri Jun 09 2006 Mike A. Harris <mharris@redhat.com> 0.9.1-3
- Added "Requires: libX11-devel" to devel package for xrender.pc

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 0.9.1-2
- Added "BuildRequires: pkgconfig" for (#193429)
- Replace "makeinstall" with "make install DESTDIR=..."
- Remove package ownership of mandir/libdir/etc.

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 0.9.1-1
- Update to 0.9.1

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9.0.2-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9.0.2-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 23 2006 Mike A. Harris <mharris@redhat.com> 0.9.0.2-3
- Bump and rebuild

* Mon Jan 16 2006 Mike A. Harris <mharris@redhat.com> 0.9.0.2-2
- Added "Requires: xorg-x11-proto-devel" to resolve bug (#176742)

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 0.9.0.2-1
- Updated libXrender to version 0.9.0.2 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.9.0.1-1
- Updated libXrender to version 0.9.0.1 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.9.0-5
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'

* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 0.9.0-4
- Updated libXrender to version 0.9.0 from X11R7 RC1

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.9.0-3
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 0.9.0-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.9.0-1
- Initial build.
