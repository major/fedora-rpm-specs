%global svnversion 507
%global gver .trunkREV%{svnversion}

Summary: Library for working with files using the mp4 container format
Name: libmp4v2
Version: 2.1.0
Release: 0.33%{gver}%{?dist}
# Automatically converted from old format: MPLv1.1 - review is highly recommended.
License: LicenseRef-Callaway-MPLv1.1
URL: http://code.google.com/p/mp4v2
# mp4v2-trunk-r507.tar.bz2 made with ./make-svn-snapshot.sh
Source0: http://mp4v2.googlecode.com/files/mp4v2-trunk-r%{svnversion}.tar.bz2
Source1: make-svn-snapshot.sh
# upstreamable patch
# Reference: https://code.google.com/p/mp4v2/issues/detail?id=177
Patch1: 0001-Fix-make-dist.patch
Patch2: 0002-Install-man-man3-BTW-like-in-libmp4v2-1.5.0.1.patch
Patch3: 0003-Fix-out-of-tree-builds-182.patch
Patch4: 0004-Fix-GCC7-build.patch
Patch5: 0005-Fix-clang-compilation.patch
Patch7: 0007-Fix-Out-of-bounds-memory-access-in-MP4v2-2.0.0.patch
Patch8: 0008-Fix-v2-Type-confusion-in-MP4v2-2.0.0.patch
Patch9: 0009-Null-out-pointer-after-free-to-prevent-double-free.patch
Patch10: 0010-Fix-v3-Integer-underflow-overflow-in-MP4v2-2.0.0.patch
Patch50: gcc10.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: autoconf automake gettext-devel libtool texinfo svn
BuildRequires: python%{python3_pkgversion} doxygen help2man
%if 0%{?fedora} > 29 || 0%{?rhel} > 7
BuildRequires: glibc-langpack-en
%endif

%description
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.


%package devel
Summary: Development files for the mp4v2 library
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
Development files and documentation needed to develop and compile programs
using the libmp4v2 library.


%prep
%autosetup -p1 -n mp4v2-trunk

%build
autoreconf --force --install --verbose
%configure --disable-static
%make_build
%if 0%{?fedora} > 29 || 0%{?rhel} > 7
%{__make} txt
%endif
export LANG=en_US.utf8
%{__make} api


%install
%make_install
find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets


%files
%if 0%{?fedora} > 29 || 0%{?rhel} > 7
%doc doc/articles/txt/*txt
%endif
%license COPYING
%{_bindir}/*
%{_libdir}/libmp4v2.so.2*
%{_mandir}/man1/mp4*.1*

%files devel
%doc doc/api/html/
%{_includedir}/mp4v2/
%{_libdir}/libmp4v2.so
%{_mandir}/man3/MP4*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.33.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-0.32.trunkREV507
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.31.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.30.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.29.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.28.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.27.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.26.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.25.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.24.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.23.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.22.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.21.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 2.1.0-0.20.trunkREV507
- Fix narrowing conversion issue caught by gcc-10

* Fri Nov 08 2019 Sérgio Basto <sergio@serjux.com> - 2.1.0-0.19.trunkREV507
- Fix-v3-Integer-underflow-overflow-in-MP4v2-2.0.0

* Sat Nov 02 2019 Sérgio Basto <sergio@serjux.com> - 2.1.0-0.18.trunkREV507
- Fix https://nvd.nist.gov/vuln/detail/CVE-2018-14446
  https://nvd.nist.gov/vuln/detail/CVE-2018-14403
  https://nvd.nist.gov/vuln/detail/CVE-2018-14379
  https://nvd.nist.gov/vuln/detail/CVE-2018-14326
  https://nvd.nist.gov/vuln/detail/CVE-2018-14325
  https://nvd.nist.gov/vuln/detail/CVE-2018-14054
  based on https://github.com/TechSmith/mp4v2/pull/27
  and https://github.com/sergiomb2/libmp4v2/
- Update spec
- Fix build on epel7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.17.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 FeRD (Frank Dana) <ferdnyc AT gmail com> - 2.1.0-0.16.trunkREV507
- Add BuildRequires for help2man, fixes manpage generation

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.15.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.0-0.14.trunkREV507
- Add BR:glibc-langpack-en
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.13.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.12.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.11.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.10.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.9.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Feb 08 2017 Sérgio Basto <sergio@serjux.com> - 2.1.0-0.8.trunkREV507
- Add patch for GCC7
- Add new pactch 0003-Fix-out-of-tree-builds-182.patch
- Rename the others patches

* Mon Feb 06 2017 Sérgio Basto <sergio@serjux.com> - 2.1.0-0.7.trunkREV507
- Fix python3 support in EPEL7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.6.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 04 2015 Sérgio Basto <sergio@serjux.com> - 2.1.0-0.5.trunkREV507
- Tidy a little more.
- Added mp4v2-2.1-fixdoc2.patch : install man/man3/, BTW like in libmp4v2-1.5.0.1
  and fix 30 annoying warnings "target x given more than once in the same rule".
- Make api documentation and add it (doc/api/html/) into -devel package.

* Fri Oct 02 2015 David King <amigadave@amigadave.com> - 2.1.0-0.4.trunkREV507
- Remove obsolete tags
- Use license macro for COPYING
- Tighten requirements on base package
- Update man pages glob in files section
- Tidy spec file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.3.trunkREV507
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Sérgio Basto <sergio@serjux.com> - 2.1.0-0.2.trunkREV507
- Use trunk source, not source generated with make dist

* Wed Apr 22 2015 Sérgio Basto <sergio@serjux.com> - 2.1.0-0.1.trunkREV507
- Update pre release 2.1.0, svn trunk version REV 507 .

* Sat Jan 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-2
- track library soname, so bumps aren't a surprise
- -devel: own %%_includedir/mp4v2/

* Fri Jan 09 2015 Sérgio Basto <sergio@serjux.com> - 2.0.0-1

  Sat Mar 01 2014 Avi Alkalay <avibrazil@gmail.com>
  - included some documentation

  Mon Aug 02 2010 Honore Doktorr <hdfssk@gmail.com>
  - update to upstream 2.0.0

  Mon Aug 02 2010 François Kooman <fkooman@tuxed.net>
  - update to upstream 1.9.1
  - drop redundant patches
  - move README to main package
  - add cli-manuals to main package
  - no longer include the API documentation in devel package
  - move headers to /usr/include/mp4v2/*
  - remove *.la in install phase instead of excluding it while packaging

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Matthias Saou <http://freshrpms.net/> 1.5.0.1-9
- Rebuild to fix runtime problems of the latest builds (#507302).

* Sun Mar 01 2009 Caolán McNamara <caolanm@redhat.com> - 1.5.0.1-8
- constify rets of strchr(const char*)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0.1-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 1.5.0.1-5
- Rebuild for new BuildID feature.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 1.5.0.1-4
- Update License field.

* Fri Dec 15 2006 Matthias Saou <http://freshrpms.net/> 1.5.0.1-3
- Spec file cleanup (habits, mostly) preparing to submit for Extras inclusion.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.5.0.1-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Jul 18 2006 Noa Resare <noa@resare.com> 1.5.0.1-1
- new upstream release

* Sat May 13 2006 Noa Resare <noa@resare.com> 1.4.1-3
- disabled static lib
- use DESTDIR
- disable-dependency-tracking for faster builds
- removed a manpage template file apt.mpt.gz

* Mon May 08 2006 Noa Resare <noa@resare.com> 1.4.1-2
- specfile cleanups

* Fri May 05 2006 Noa Resare <noa@resare.com> 1.4.1-1.lvn5
- initial release

