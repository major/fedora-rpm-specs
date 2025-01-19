Summary:    A compact getty program for virtual consoles only
Name:       mingetty
Version:    1.08
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
Release:    39%{?dist}
URL: http://sourceforge.net/projects/mingetty/
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Bug #635412
Patch1:     mingetty-1.08-check_chroot_chdir_nice.patch
Patch2:     mingetty-1.08-openlog_authpriv.patch
# Bug #551754
Patch3:     mingetty-1.08-limit_tty_length.patch
# Bug #647143
Patch4:     mingetty-1.08-Allow-login-name-up-to-LOGIN_NAME_MAX-length.patch
# Bug #691406
Patch5:     mingetty-1.08-Clear-scroll-back-buffer-on-clear-screen.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make

%description
The mingetty program is a lightweight, minimalist getty program for
use only on virtual consoles.  Mingetty is not suitable for serial
lines (you should use the mgetty program in that case).

%prep
%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%global _hardened_build 1
make "CFLAGS=-Wall -D_GNU_SOURCE %{__global_cflags}" "LDFLAGS=%{__global_ldflags}"

%install
install -d $RPM_BUILD_ROOT/{sbin,%{_mandir}/man8}
install -m 0755 mingetty $RPM_BUILD_ROOT/sbin/
install -m 0644 mingetty.8 $RPM_BUILD_ROOT/%{_mandir}/man8/

%files
%license COPYING
/sbin/mingetty
%{_mandir}/man8/mingetty.*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.08-38
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Petr Pisar <ppisar@redhat.com> - 1.08-23
- Modernize spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 Petr Pisar <ppisar@redhat.com> - 1.08-12
- Modernize spec file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 26 2011 Petr Pisar <ppisar@redhat.com> - 1.08-9
- Harden compiler and linker flags per
  <https://fedoraproject.org/wiki/Hardened_Packages#list>

* Fri Jun 10 2011 Petr Pisar <ppisar@redhat.com> - 1.08-8
- Clear scroll-back buffer (bug #691406)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 10 2010 Petr Pisar <ppisar@redhat.com> - 1.08-6
- Allow login name up to LOGIN_NAME_MAX length (bug #647143)

* Tue Oct 26 2010 Petr Pisar <ppisar@redhat.com> - 1.08-5
- Check chroot(), chdir(), and nice() (bug #635412)
- Open syslog with AUTPRIV facility
- Limit TTY name length to prevent buffer overflow (bug #551754)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.08-2
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Florian La Roche <laroche@redhat.com> - 1.08-1
- change Source: tag
- Bernardo Innocenti bernie at codewiz.org: add LDFLAGS to opt patch
  to enable cross building on 64bit host
- release 1.08 with loginpause option from Bernardo Innocenti bernie at codewiz.org

* Tue Jan 08 2008 Florian La Roche <laroche@redhat.com> - 1.07-8
- add sf.net project url
- add dist macro to release

* Sun Jan 06 2008 Florian La Roche <laroche@redhat.com> - 1.07-7
- add rpmlint changes to .spec file from Jon Ciesla limb at jcomserv.net

* Tue Aug 21 2007 Florian La Roche <laroche@redhat.com> - 1.07-6
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.07-5.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.07-5.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.07-5.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 1.07-5
- build with gcc-4

* Wed Feb 09 2005 Karsten Hopp <karsten@redhat.de> 1.07-4
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jan 03 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 1.07

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat May 24 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.06

* Sat Apr 12 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.05

* Sun Mar 30 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.04

* Sat Feb 08 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- small source cleanups

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Mar 04 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- re-release as 1.00

* Thu Jul 05 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild

* Wed Apr 11 2001 Bill Nottingham <notting@redhat.com>
- rebuild (missing ia64 packages)

* Fri Apr 06 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix man-page bug #34991
- fix syslog() call to be more secure #17349

* Thu Jan 11 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- set TERM=dumb for s390 console

* Mon Nov 13 2000 Oliver Paukstadt <oliver.paukstadt@millenux.com>
- fgetc returns int not char

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Matt Wilson <msw@redhat.com>
- use %%{_mandir} for man pages

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 10)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- fixed build problems on intel and alpha for manhattan

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
~- built against glibc
