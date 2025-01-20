Summary: A tool for gathering and displaying system information
Name: procinfo
Version: 18
Release: 58%{dist}
License: GPL-1.0-or-later
Source: ftp://ftp.cistron.nl/pub/people/00-OLD/svm/%{name}-%{version}.tar.gz
Patch0: procinfo-14-misc.patch
Patch3: procinfo-17-mandir.patch
Patch5: procinfo-17-uptime.patch
Patch6: procinfo-17-lsdev.patch
Patch7: procinfo-18-acct.patch
Patch8: procinfo-18-mharris-use-sysconf.patch
Patch9: procinfo-18-maxdev.patch
Patch10: procinfo-18-ranges.patch
Patch11: procinfo-18-cpu-steal.patch
Patch12: procinfo-18-intr.patch
Patch13: procinfo-18-intrprint.patch
Patch14: procinfo-18-version.patch
Patch15: procinfo-18-man-comment.patch
Patch16: procinfo-18-socklist.patch
Patch17: procinfo-18-idle-overflow.patch
Patch18: procinfo-strsignal.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: ncurses-devel

%description
The procinfo command gets system data from the /proc directory (the
kernel filesystem), formats it and displays it on standard output.
You can use procinfo to acquire information about your system from the
kernel as it is running.

Install procinfo if you'd like to use it to gather and display system
data.

%prep
%setup -q
%patch -P0 -p1 -b .misc
%patch -P3 -p1 -b .mandir
%patch -P5 -p1 -b .uptime
%patch -P6 -p1 -b .lsdev
%patch -P7 -p1 -b .acct
%patch -P8 -p1 -b .mharris-use-sysconf
%patch -P9 -p1 -b .maxdev
%patch -P10 -p1 -b .ranges
%patch -P11 -p1 -b .steal
%patch -P12 -p1 -b .intr
%patch -P13 -p1 -b .intrprint
%patch -P14 -p1 -b .version
%patch -P15 -p1 -b .mancomment
%patch -P16 -p0 -b .socklist
%patch -P17 -p1 -b .idle
%patch -P18 -p1 -b .strsignal

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses" LDFLAGS= LDLIBS=-lncurses

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
make install prefix=$RPM_BUILD_ROOT/usr mandir=$RPM_BUILD_ROOT/%{_mandir}

%files
%doc README CHANGES
%{_bindir}/procinfo
%{_bindir}/lsdev
%{_bindir}/socklist
%{_mandir}/man8/procinfo.8*
%{_mandir}/man8/lsdev.8*
%{_mandir}/man8/socklist.8*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 18-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 18-56
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jeff Law <law@redhat.com> - 18-46
- Use strsignal not sys_siglist

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 18-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 14 2011 Jan Görig <jgorig@redhat.com> 18-29
- fixed overflow in hms calculations (#676651) - thanks to ychavan@redhat.com

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 12 2010 Jan Görig <jgorig@redhat.com> 18-27
- added IPv6 support to socklist (patch from Ubuntu - bug #513837)

* Tue Oct 12 2010 Jan Görig <jgorig@redhat.com> 18-26
- fixed parsing gcc version string
- fixed view on terminal with 80 characters line
- fixed comment tag in manpage
- spec fixes

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Tomas Smetana <tsmetana@redhat.com> 18-23
- rebuild (gcc-4.3)

* Wed Oct 10 2007 Tomas Smetana <tsmetana@redhat.com> 18-22
- fix #323121 - segfault caused by interrupts counting
- fix division by zero in fullscreen

* Thu Aug 23 2007 Tomas Smetana <tsmetana@redhat.com> 18-21
- update license tag
- rebuild (buildID)

* Thu Jan 11 2007 Karel Zak <kzak@redhat.com> 18-20
- bye bye libtermcap

* Wed Jul 19 2006 Karel Zak <kzak@redhat.com> - 18-19
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 18-18.3.1
- rebuild

* Fri Apr 21 2006 Karel Zak <kzak@redhat.com> - 18-18.2.3
- fix #185300 - cpu steal time support

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 18-18.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 18-18.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Oct 12 2005 Karel Zak <kzak@redhat.com> 18-18
- improve procinfo-18-ranges.patch

* Wed Oct 12 2005 Karel Zak <kzak@redhat.com> 18-17
- fix #170424 - procinfo crashing on X86_64

* Tue May 10 2005 Karel Zak <kzak@redhat.com> 18-16
- fixed debuginfo

* Sat Mar  5 2005 Karel Zak <kzak@redhat.com> 18-15
- rebuilt

* Fri Dec 17 2004 Karel Zak <kzak@redhat.com> 18-14
- fixed limit of devices (#89176)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jan 17 2004 Mike A. Harris <mharris@redhat.com> 18-11
- Added procinfo-18-mharris-use-sysconf.patch to use sysconf for determining
  the number of processors online, as this is more portable between different
  CPU architectures than relying on particular /proc file entry contents and
  formatting.  We ship on 7 architectures (x86, ia64, AMD64, ppc, ppc64, s390,
  s390x), and the current code only handled x86, alpha, sparc.  sysconf will
  work on all processors.  Better fix for (#9497)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Oct  7 2002 Mike A. Harris <mharris@redhat.com> 18-7
- Removed TODO from doc list as the file isn't present any longer
- Checked upstream URL, still no package version update.

* Mon Oct  7 2002 Mike A. Harris <mharris@redhat.com> 18-6
- All-arch rebuild
- Updated to use {_bindir} et al.
- Fixed Buildroot: line in specfile to be sensible

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Jul 21 2001 Bernhard Rosenkraenzer <bero@redhat.com> 18-2
- Add BuildRequires (#49561)
- s/Copyright/License/

* Wed Apr 25 2001 Bernhard Rosenkraenzer <bero@redhat.com> 18-1
- 18

* Mon Dec 11 2000 Erik Troan <ewt@redhat.com>
- built on all archs

* Thu Nov 16 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- fix up lsdev (Bug #10295 and a couple of unreported bugs) 
- fix up calculation of uptime milliseconds (introduced by gcc acting
  differently from previous releases, t/100*100 != t*100/100)
  (Bug #20741)

* Mon Oct 16 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix uptime calculation (Bug #18673)
  This problem was introduced by gcc acting differently from previous
  releases (t * 100 / HZ --> overflow; t / HZ * 100 ok).

* Mon Oct  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix CPU stats after very long uptimes (Bug #17391)

* Tue Aug  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix reported number of CPUs on sparc (Bug #9597)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Matt Wilson <msw@redhat.com>
- FHS man paths (patch3)
- buildable as non-root (patch3)

* Fri Feb 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up the CPU detection patch (Bug #9497)

* Sat Feb  5 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- handle compressed man pages

* Mon Oct 04 1999 Michael K. Johnson <johnsonm@redhat.com>
- fix cpu detection on sparc and alpha

* Fri Aug 27 1999 Preston Brown <pbrown@redhat.com>
- upgraded to r17, which incorporates several of our patches + smp fixes
- fix bug #1959

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- patched to work with kernels with LOTS of IRQs. (bug 1616)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Fri Mar 12 1999 Michael Maher <mike@redhat.com>
- updated to version 16
- closed bug 1349

* Fri Nov 20 1998 Michael K. Johnson <johnsonm@redhat.com>
- updated to version 15 to fix bugzilla 70.

* Fri Oct  2 1998 Jeff Johnson <jbj@redhat.com>
- calculate time per-cent on non-{alpha,i386} correctly.

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 14
- fixed the spec file 

* Thu Apr 30 1998 Donnie Barnes <djb@redhat.com>
- updated from 0.11 to 13
- added socklist program

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- updated to version 0.11

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
