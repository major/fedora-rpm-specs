Summary: A utility for adjusting kernel time variables
Name: adjtimex
Version: 1.29
Release: 33%{?dist}
License: GPL-2.0-or-later
Source: http://ftp.debian.org/debian/pool/main/a/adjtimex/%{name}_%{version}.orig.tar.gz
Patch1: adjtimex-manopts.patch
Patch2: adjtimex-decl.patch
BuildRequires: gcc
BuildRequires: make

%description
Adjtimex provides raw access to kernel time variables. On standalone
or intermittently connected machines, root can use adjtimex to correct
for systematic drift. If your machine is connected to the Internet or
is equipped with a precision oscillator or radio clock, you should
instead manage the system clock with the xntpd program. Users can use
adjtimex to view kernel time variables.

%prep
%setup -q
%patch -P1 -p1 -b .manopts
%patch -P2 -p1 -b .decl

%build
%configure
make %{?_smp_mflags} VERSION=%{version}

%install
mkdir -p ${RPM_BUILD_ROOT}{%{_sbindir},%{_mandir}/man8}
install -m755 adjtimex ${RPM_BUILD_ROOT}%{_sbindir}/adjtimex
install -m644 adjtimex.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/adjtimex.8

%files
%license COPYING
%doc README COPYRIGHT ChangeLog
%{_sbindir}/adjtimex
%{_mandir}/man8/adjtimex.8*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Miroslav Lichvar <mlichvar@redhat.com> 1.29-32
- fix build with new gcc (#2336031)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Miroslav Lichvar <mlichvar@redhat.com> 1.29-16
- add gcc to build requirements
- use license macro

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.29-6
- fix options in man page (#856521)
- move binary to /usr
- remove obsolete macros

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 19 2010 Miroslav Lichvar <mlichvar@redhat.com> 1.29-1
- update to 1.29

* Tue Dec 01 2009 Miroslav Lichvar <mlichvar@redhat.com> 1.28-1
- update to 1.28

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Miroslav Lichvar <mlichvar@redhat.com> 1.27.1-1
- update to 1.27.1

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 25 2008 Miroslav Lichvar <mlichvar@redhat.com> 1.26-1
- update to 1.26

* Wed May 21 2008 Miroslav Lichvar <mlichvar@redhat.com> 1.24-1
- update to 1.24

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.21-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Miroslav Lichvar <mlichvar@redhat.com> 1.21-3
- update license tag

* Mon Feb 05 2007 Miroslav Lichvar <mlichvar@redhat.com> 1.21-2
- spec cleanup (#225239)

* Mon Oct 16 2006 Miroslav Lichvar <mlichvar@redhat.com> 1.21-1
- update to 1.21

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.20-2.1
- rebuild

* Mon May 22 2006 Miroslav Lichvar <mlichvar@redhat.com> 1.20-2
- fix segfault when parsing -s option

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.20-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.20-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 16 2005 Jindrich Novy <jnovy@redhat.com> 1.20-1
- update to 1.20
- update .glibc patch
- drop .getopt, .fixman, .gcc3 patches

* Fri Mar  4 2005 Jindrich Novy <jnovy@redhat.com> 1.13-16
- rebuilt with gcc4

* Thu Feb 10 2005 Jindrich Novy <jnovy@redhat.com> 1.13-15
- remove -D_FORTIFY_SOURCE=2 from CFLAGS, present in RPM_OPT_FLAGS

* Wed Feb  9 2005 Jindrich Novy <jnovy@redhat.com> 1.13-14
- add -D_FORTIFY_SOURCE=2 to CFLAGS
- spec cleanup

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 19 2004 Than Ngo <than@redhat.com> 1.13-12 
- add fix for new glibc
- add COPYRIGHT file

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 16 2003 Than Ngo <than@redhat.com> 1.13-10
- rebuild

* Fri Jun 06 2003 Than Ngo <than@redhat.com> 1.13-9
- fix s390/s390x build

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Than Ngo <than@redhat.com> 1.13-7
- fix build woth gcc 3.3

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.13-5
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 18 2002 Than Ngo <than@redhat.com> 1.13-3
- don't forcibly strip binaries

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Harald Hoyer <harald@redhat.de>
- 1.13

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 1.12-2
- rebuild in new enviroment

* Tue Feb 19 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.12-1
- 1.12

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Mon Jan 29 2001 Preston Brown <pbrown@redhat.com>
- fix man page for '-t' usage on alpha (#9674)

* Mon Nov 20 2000 Bill Nottingham <notting@redhat.com>
- fix ia64 build

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Jun 14 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Fri Mar 03 2000 Cristian Gafton <gafton@redhat.com>
- fix bug #9674

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description
- man pages are compressed

* Fri Jan  7 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.9.

* Wed Jan  5 2000 Jeff Johnson <jbj@redhat.com>
- burn y2k wartlet (#8172)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 09 1997 Erik Troan <ewt@redhat.com>
- builds on all architectures
