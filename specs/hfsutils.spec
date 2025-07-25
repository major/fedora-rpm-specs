Summary: Tools for reading and writing Macintosh HFS volumes
Name: hfsutils
Version: 3.2.6
Release: 54%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: ftp://ftp.mars.org/pub/hfs/%{name}-%{version}.tar.gz
Patch0: hfsutils-3.2.6-errno.patch
Patch1: hfsutils-3.2.6-largefile.patch
Patch2: hfsutils-3.2.6-configure-c99.patch
Patch3: hfsutils-3.2.6-include-c99.patch
URL: http://www.mars.org/home/rob/proj/hfs/
BuildRequires: libXft-devel tcl-devel tk-devel gcc
BuildRequires: make

%package devel
Summary: A C library for reading and writing Macintosh HFS volumes
Provides: %{name}-static = %{version}-%{release}

%package x11
Summary: A Tk-based front end for browsing and copying files

%description
HFS (Hierarchical File System) is the native volume format found on
modern Macintosh computers.  Hfsutils provides utilities for accessing
HFS volumes from Linux and UNIX systems.  Hfsutils contains several
command-line programs which are comparable to mtools.

%description -n hfsutils-devel
The hfsutils-devel package provides a C library for low-level access
to Macintosh volumes. HFS (Hierarchical File System) is the native
volume format found on modern Macintosh computers.  The C library can
be linked with other programs to allow them to manipulate Macintosh
files in their native format.  Other HFS accessing utilities, which
are comparable to mtools, are included in the hfsutils package.

%description -n hfsutils-x11
The hfsutils-x11 package includes a Tk-based front end for browsing
and copying files, and a Tcl package and interface for scriptable access
to volumes.  A C library for low-level access to volumes is included in the
hfsutils-devel package.

%prep
%autosetup -p1

%build
CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -DUSE_INTERP_RESULT -Wno-incompatible-pointer-types -Wno-deprecated-declarations -Wno-deprecated-declarations -Wno-pointer-sign -Wno-unused-but-set-variable -Wno-int-to-pointer-cast"
%{configure} --with-tcl=%{_libdir}  --with-tk=%{_libdir}
make
make hfsck/hfsck

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
make	BINDEST=$RPM_BUILD_ROOT%{_bindir} \
	LIBDEST=$RPM_BUILD_ROOT%{_libdir} \
	INCDEST=$RPM_BUILD_ROOT%{_includedir} \
	MANDEST=$RPM_BUILD_ROOT%{_mandir} \
	INSTALL="install -p" \
	install install_lib
install -p -m 0755 hfsck/hfsck $RPM_BUILD_ROOT/%{_bindir}

%files
%doc CHANGES CREDITS README TODO
%license COPYING COPYRIGHT
%{_bindir}/hattrib
%{_bindir}/hcd
%{_bindir}/hcopy
%{_bindir}/hdel
%{_bindir}/hdir
%{_bindir}/hformat
%{_bindir}/hfs
%{_bindir}/hfssh
%{_bindir}/hls
%{_bindir}/hmkdir
%{_bindir}/hmount
%{_bindir}/hpwd
%{_bindir}/hrename
%{_bindir}/hrmdir
%{_bindir}/humount
%{_bindir}/hvol
%{_bindir}/hfsck
%{_mandir}/man1/hattrib.1.*
%{_mandir}/man1/hcd.1.*
%{_mandir}/man1/hcopy.1.*
%{_mandir}/man1/hdel.1.*
%{_mandir}/man1/hdir.1.*
%{_mandir}/man1/hformat.1.*
%{_mandir}/man1/hfs.1.*
%{_mandir}/man1/hfssh.1.*
%{_mandir}/man1/hfsutils.1.*
%{_mandir}/man1/hls.1.*
%{_mandir}/man1/hmkdir.1.*
%{_mandir}/man1/hmount.1.*
%{_mandir}/man1/hpwd.1.*
%{_mandir}/man1/hrename.1.*
%{_mandir}/man1/hrmdir.1.*
%{_mandir}/man1/humount.1.*
%{_mandir}/man1/hvol.1.*

%files -n hfsutils-x11
%{_bindir}/xhfs
%{_mandir}/man1/xhfs.1.*

%files -n hfsutils-devel
%{_libdir}/libhfs.a
%{_libdir}/librsrc.a
%{_includedir}/hfs.h
%{_includedir}/rsrc.h

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 12 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2.6-52
- Rebuilt for the bin-sbin merge (2nd attempt)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.6-51
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Zbigniew Jedrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2.6-49
- Drop /usr/bin/fsck.hfs to avoid conflict with /usr/sbin/fsck.hfs provided by
  hfsplus-tools when https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin
  is implemented

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Peter Fordham <peter.fordham@gmail.com> - 3.2.6-45
- Port configure script to C99 and add missing include.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Filipe Rosset <rosset.filipe@gmail.com> - 3.2.6-37
- Rebuilt to fix FTBFS rhbz#1604324 rhbz#1675101 and rhbz#1665687 + spec cleanup

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 13 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.6-27
- Append -DUSE_INTERP_RESULT to CFLAGS to work-around Tcl/Tk-8.6
  incompatibilities (FTBFS RHBZ #1106760).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.2.6-25
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 25 2009 Peter Lemenkov <lemenkov@gmail.com> - 3.2.6-19
- Added provides hfsutils-static (bz #225886)
- Use INSTALL="install -p" (bz #225886)

* Fri Sep 25 2009 Peter Lemenkov <lemenkov@gmail.com> - 3.2.6-18
- Fixed issues from the Merge Review (bz #225886)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 11 2009 Debarshi Ray <rishi@fedoraproject.org> - 3.2.6-15
- Updated large file patch. Closes Red Hat Bugzilla bug #465060.
- Added 'BuildRequires: libXft-devel'.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.2.6-14
- Autorebuild for GCC 4.3

* Fri Jan 25 2008 Jesse Keating <jkeating@redhat.com> - 3.2.6-13
- Exclude hfssh, nobody really uses it and it drags in tcl to the base
  requires.
- Drop the artificial tcl requirement, rpm will do it's job on reqs.

* Thu Jan 03 2008 David Woodhouse <dwmw2@infradead.org> 3.2.6-12
- Rebuild for tcl 8.5

* Wed Aug 22 2007 David Woodhouse <dwmw2@infradead.org> 3.2.6-11
- Update licence

* Wed Aug 22 2007 David Woodhouse <dwmw2@infradead.org> 3.2.6-10
- Rebuild

* Fri Feb 09 2007 David Cantrell <dcantrell@redhat.com> 3.2.6-9
- Rebuild for tcl

* Fri Jan 26 2007 Jesse Keating <jkeating@redhat.com> 3.2.6-8
- rebuild for new tcl

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 3.2.6-7.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 3.2.6-7.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 3.2.6-7.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 2 2005 David Woodhouse <dwmw2@redhat.com> 3.2.6-7
- Rebuild with gcc 4

* Sun Feb 20 2005 David Woodhouse <dwmw2@redhat.com> 3.2.6-6
- Handle files larger than 2GiB
- Include hfsck

* Mon Feb 14 2005 David Woodhouse <dwmw2@redhat.com> 3.2.6-5
- s/Copyright:/License:/ (sic)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com> 3.2.6-4
- rebuilt

* Mon Apr 19 2004 David Woodhouse  <dwmw2@redhat.com> 3.2.6-3
- BuildRequires tk-devel

* Sun Apr 11 2004 David Woodhouse  <dwmw2@redhat.com> 3.2.6-2.1
- Adjust configure invocation to find tcl in %%{_libdir}

* Sun Apr 11 2004 David Woodhouse  <dwmw2@redhat.com> 3.2.6-2
- Require tcl

* Fri Apr 09 2004 David Woodhouse  <dwmw2@redhat.com> 3.2.6-1
- Fix BuildRequires, include errno.h in tclhfs.c, use %%{configure}

* Wed Oct 02 2002 Dan Burcaw <dburcaw@terrasoftsolutions.com>
- Anubis rebuild

* Fri Mar 30 2001 Dan Burcaw <dburcaw@terrasoftsolutions.com>
- split xhfs into its own package

* Fri Feb 11 2000 Tim Powers <timp@redhat.com>
- gzip manpages, strip binaries

* Thu Jul 15 1999 Tim Powers <timp@redhat.com>
- added %%defattr
- rebuilt for 6.1

* Thu Apr 15 1999 Michael Maher <mike@redhat.com>
- built package for 6.0
- updated source

* Thu Aug 20 1998 Michael Maher <mike@redhat.com>
- built package

