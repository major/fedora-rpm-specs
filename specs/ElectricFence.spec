# Regarding the following rpmlint citation:
#
#   library package calls exit() or _exit() [...]
#
# Electric fence is a debugger, not a library.  The fact that it comes
# in the form factor of a library is just because that's how you
# override malloc-related calls from libc.  Calling _exit is the
# ultimate outcome of detecting a class of memory errors (double free,
# free of wild pointer, etc.)  Overflows (or underflows) are detected
# by the operating system and lead to process termination as well.
#
#   devel-file-in-non-devel-package /usr/lib64/libefence.a
#
# Electric fence is itself a development package.

Summary: A debugger which detects memory allocation violations
Name: ElectricFence
Version: 2.2.2
Release: 66%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://perens.com/FreeSoftware/ElectricFence/

# ftp://ftp.perens.com/pub/ElectricFence/beta/ used to be here, but
# the site is inaccessible as of lately.  I looked through the web but
# didn't find anything.  Debian has a link to a site that hosts an
# obsolete version.  I don't think there's any proper upstream for
# this.
Source: %{name}-%{version}.tar.gz
Patch1: ElectricFence-2.0.5-longjmp.patch
Patch2: ElectricFence-2.1-vaarg.patch
Patch3: ElectricFence-2.2.2-pthread.patch
Patch4: ElectricFence-2.2.2-madvise.patch
Patch5: ElectricFence-mmap-size.patch
Patch6: ElectricFence-2.2.2-banner.patch
Patch7: ElectricFence-2.2.2-ef.patch
Patch8: ElectricFence-2.2.2-builtins.patch
Patch9: ElectricFence-2.2.2-sse.patch
Patch10: ElectricFence-2.2.2-posix_memalign.patch
Patch11: ElectricFence-2.2.2-malloc_usable_size.patch
Patch12: ElectricFence-2.2.2-man-ef.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1105913
Patch13: ElectricFence-2.2.2-sys_errlist.patch

Patch14: ElectricFence-2.2.2-lto.patch

Patch15: ElectricFence-strerror.patch

BuildRequires:  gcc
BuildRequires: make
%description
ElectricFence is a utility for C programming and
debugging. ElectricFence uses the virtual memory hardware of your
system to detect when software overruns malloc() buffer boundaries,
and/or to detect any accesses of memory released by
free(). ElectricFence will then stop the program on the first
instruction that caused a bounds violation and you can use your
favorite debugger to display the offending statement.

Install ElectricFence if you need a debugger to find malloc()
violations.

%prep
%autosetup -p1

%build
make CFLAGS='${RPM_OPT_FLAGS} -DUSE_SEMAPHORE -fpic'

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}{%{_bindir},%{_libdir},%{_mandir}/man{1,3}}

make	BIN_INSTALL_DIR=%{buildroot}%{_bindir} \
	LIB_INSTALL_DIR=%{buildroot}%{_libdir} \
	MAN_INSTALL_DIR=%{buildroot}%{_mandir} \
	install

echo ".so man3/efence.3" > %{buildroot}%{_mandir}/man3/libefence.3

%ldconfig_scriptlets


%files
%doc README CHANGES COPYING
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so*
%{_mandir}/*/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.2-65
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 23 2020 Jeff Law  <law@redhat.com> - 2.2.2-53
- Use strerror, not sys_errlist on linux platforms
- Use autosetup

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 2.2.2-51
- Make global variable volatile in test to defeat LTO optimization

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Petr Machata <pmachata@redhat.com> - 2.2.2-40
- Fix hiding of default declaration of sys_nerr, sys_errlist
  (ElectricFence-2.2.2-sys_errlist.patch)

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Petr Machata <pmachata@redhat.com> - 2.2.2-35
- Add a man page for "ef" script
- Resolves: #225722

* Mon Mar 12 2012 Petr Machata <pmachata@redhat.com> - 2.2.2-34
- Add a patch that implements malloc_usable_size
- Resolves: #772306

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar 11 2011 Petr Machata <pmachata@redhat.com> - 2.2.2-32
- Add a patch that implements posix_memalign
- Resolves: #684019

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Petr Machata <pmachata@redhat.com> - 2.2.2-30
- Use the same formula as glibc uses to align memory
- Resolves: #662085

* Fri Sep 10 2010 Petr Machata <pmachata@redhat.com> - 2.2.2-29
- Tell GCC not to recognize builtins when compiling efence.c.
- Resolves: #631316
- Related: #632312

* Thu Sep  9 2010 Petr Machata <pmachata@redhat.com> - 2.2.2-28
- GCC optimizes out write to internalUse in call from
  allocateMoreSlots to malloc.  Rename malloc to __efence__malloc to
  pacify the trigger.  Later sneak the malloc symbol in with an alias.
- Resolves: #631316

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Petr Machata <pmachata@redhat.com> - 2.2.2-25
- Fix ef.sh argument passing
- Resolves: #432286

* Thu Aug 16 2007 Petr Machata <pmachata@redhat.com> - 2.2.2-24
- Fix licesing tag.

* Wed Mar 28 2007 Petr Machata <pmachata@redhat.com> - 2.2.2-23
- Detect for EF_DISABLE_BANNER env. var before printing out the
  banner.  (Patch adapted from Debian repositories.)
- Resolves: #233702

* Fri Mar 16 2007 Petr Machata <pmachata@redhat.com> - 2.2.2-22
- Remove bad cast in ElectricFence mmap (George Beshers)
- Resolves: #232695

* Wed Feb  7 2007 Petr Machata <pmachata@redhat.com> - 2.2.2-21
- Tidy up the specfile per rpmlint comments

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.2.2-20.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.2.2-20.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.2.2-20.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Mar  5 2005 Jakub Jelinek <jakub@redhat.com> 2.2.2-20
- rebuilt with GCC 4

* Sat Oct 16 2004 Jakub Jelinek <jakub@redhat.com> 2.2.2-19
- when EF_PROTECT_FREE=1, instead of munmaping mprotect PROT_NONE
  and madvise MADV_DONTNEED (#107506)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb  3 2003 Jakub Jelinek <jakub@redhat.com>
- never call semaphore routines in between
  __libc_malloc_pthread_startup(true) and
  __libc_malloc_pthread_startup(false) (#83111)
- only use semaphore locking if application or its dependencies
  are linked against -lpthread, don't link libefence.so against
  -lpthread
- run tests as part of the build process

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Jeff Johnson <jbj@redhat.com> 2.2.2-13
- don't include -debuginfo files in package.

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 2.2.2-12
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Nov 16 2000 Tim Powers <timp@redhat.com>
- use -fPIC, not -fpic, also -DUSE_SEMAPHORE to make it thread safe,
  as per bug #20935

* Tue Sep 19 2000 Bill Nottingham <notting@redhat.com>
- use -fpic

* Fri Aug 18 2000 Tim Waugh <twaugh@redhat.com>
- fix efence.3/libefence.3 confusion (#16412).

* Tue Aug 1 2000 Tim Powers <timp@redhat.com>
- added ldconfig stuff to ;post and postun
- added Requires /sbin/ldconfig
* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Jul 05 2000 Preston Brown <pbrown@redhat.com>
- back in main distro
- 2.2.2 version - claimed beta, but no releases in over a year.
- FHS macros

* Fri May 26 2000 Tim Powers <timp@redhat.com>
- moved to Powertools
- fix map page location to be in /usr/share/man

* Tue May 16 2000 Jakub Jelinek <jakub@redhat.com>
- fix build on ia64

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description
- man pages are compressed

* Tue Jan  4 2000 Jeff Johnson <jbj@redhat.com>
- remove ExcludeArch: alpha (#6683).

* Sat Apr 10 1999 Matt Wilson <msw@redhat.com>
- version 2.1

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 13)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- create efence.3 (problem #830)

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- need to use sigsetjmp() and siglongjmp() for proper testing

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use ExcludeArch instead of Exclude

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
