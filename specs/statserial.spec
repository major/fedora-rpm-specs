Summary: A tool which displays the status of serial port modem lines
Name: statserial
Version: 1.1
Release: 72%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: ftp://metalab.unc.edu/pub/Linux/system/serial/
Source: ftp://metalab.unc.edu/pub/Linux/system/serial/statserial-1.1.tar.gz
Patch0: statserial-1.1-config.patch
Patch1: statserial-1.1-dev.patch
Patch2: statserial-1.1--n.patch
Patch3: statserial-1.1-loop-fix.patch
BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel
ExcludeArch: s390 s390x

%description
The statserial utility displays a table of the signals on a standard
9-pin or 25-pin serial port and indicates the status of the
handshaking lines.  Statserial is useful for debugging serial port
and/or modem problems.

%prep
%setup -q
%patch -P0 -p1 -b .config
%patch -P1 -p1 -b .dev
%patch -P2 -p1 -b .-n
%patch -P3 -p1 -b .loop-fix

%build
make LDFLAGS= CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1

install -m 755 statserial ${RPM_BUILD_ROOT}%{_bindir}/statserial
install -m 644 statserial.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/statserial.1

%files
%doc COPYING
%doc phone_log
%{_bindir}/statserial
%{_mandir}/man1/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-71
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1-67
- Fixed unintended looping with some serial ports
  Resolves: rhbz#2214075

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Tim Waugh <twaugh@redhat.com> 1.1-41
- Rebuild for GCC 4.3.

* Wed Aug 29 2007 Tim Waugh <twaugh@redhat.com> 1.1-40
- More specific license tag.

* Fri Feb  9 2007 Tim Waugh <twaugh@redhat.com> 1.1-39
- Added URL tag (bug #226436).
- Removed prefix tag (bug #226436).
- Fixed build root (bug #226436).
- Added dist to release tag (bug #226436).
- Use RPM_OPT_FLAGS (bug #226436).
- Use smp_mflags (bug #226436).
- Fixed summary (bug #226436).
- Fixed license (bug #226436, bug #190125).
- Ship license (bug #226436).
- Ship phone_log script as doc (bug #226436).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1-38.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.1-38.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.1-38.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue May 10 2005 Tim Waugh <twaugh@redhat.com> 1.1-38
- Don't strip the binary.

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 1.1-37
- Rebuild for new GCC.

* Wed Feb  9 2005 Tim Waugh <twaugh@redhat.com> 1.1-36
- Rebuilt.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.1-31
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Apr 22 2002 Tim Waugh <twaugh@redhat.com> 1.1-28
- Don't strip binaries explicitly (bug #62567).

* Tue Feb 26 2002 Tim Waugh <twaugh@redhat.com> 1.1-27
- Rebuild in new environment.

* Sat Feb 16 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- do not specify archaic "-N" anymore for linking

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Nov 16 2001 Tim Waugh <twaugh@redhat.com> 1.1-24
- s/Copyright:/License:/.
- Fix -n (bug #56299).

* Tue Jun 19 2001 Florian La Roche <Florian.LaRoche@redhat.de> 1.1-23
- add ExcludeArch: s390 s390x

* Mon Jun 18 2001 Tim Waugh <twaugh@redhat.com> 1.1-22
- Build requires ncurses-devel.

* Wed May 30 2001 Tim Waugh <twaugh@redhat.com> 1.1-21
- Sync description with specspo.

* Wed Aug 30 2000 Matt Wilson <msw@redhat.com> 1.1-20
- rebuild to cope with glibc locale binary incompatibility, again

* Thu Jul 27 2000 Jeff Johnson <jbj@redhat.com>
- change default device from /dev/cuar to /dev/ttyS1 (#14624).

* Wed Jul 19 2000 Jakub Jelinek <jakub@redhat.com>
- rebuild to cope with glibc locale binary incompatibility

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Jun 14 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man pages.

* Mon Oct 04 1999 Cristian Gafton <gafton@redhat.com>
- rebuilt against new glibc in the sparc tree

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 13)

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root
- include arch sparc

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
