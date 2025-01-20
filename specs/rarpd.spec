Summary: The RARP daemon
Name: rarpd
Version: ss981107
Release: 68%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: ftp://ftp.fi.netbsd.org/.m/mirrors1/ftp.inr.ac.ru/ip-routing/dhcp.bootp.rarp/rarpd-%{version}.tar.gz
Source1: rarpd.service
Source2: LICENSE
Patch0: rarpd-%{version}.patch
Patch1: rarpd-fd-leak.patch
Patch2: rarpd-sprintf.patch
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
BuildRequires: make
BuildRequires: systemd-units
BuildRequires: gcc

%description
RARP (Reverse Address Resolution Protocol) is a protocol which allows
individual devices on an IP network to get their own IP addresses from the
RARP server.  Some machines (e.g. SPARC boxes) use this protocol instead
of e.g. DHCP to query their IP addresses during network bootup.
Linux kernels up to 2.2 used to provide a kernel daemon for this service,
but since 2.3 kernels it is served by this userland daemon.

You should install rarpd if you want to set up a RARP server on your
network.

%prep
%setup -q -n rarpd
%patch -P0 -p1 -b .ss981107
%patch -P1 -p1 -b .fd-leak
%patch -P2 -p1 -b .sprintf

%build
%ifarch s390 s390x
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpic"
%endif
export LDFLAGS="-pie -Wl,-z,relro,-z,now"
make CFLAGS="$CFLAGS"

cp %{SOURCE2} .

%install
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8

install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_unitdir}/rarpd.service
install -m 755 rarpd ${RPM_BUILD_ROOT}%{_sbindir}/rarpd
install -m 644 rarpd.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/rarpd.8

%post
%systemd_post rarpd.service

%preun
%systemd_preun rarpd.service

%postun
%systemd_postun_with_restart rarpd.service

%files
%doc README LICENSE
%{_sbindir}/rarpd
%{_mandir}/man8/*
%{_unitdir}/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - ss981107-67
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-57
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Marek Skalický <mskalick@redhat.com> - ss981107-51
- Add missing BuildRequires: gcc/gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - ss981107-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - ss981107-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - ss981107-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - ss981107-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - ss981107-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Honza Horak <hhorak@redhat.com> - ss981107-41
- Fix some packaging issues
- Adding license text since upstream is dead

* Fri May 24 2013 Honza Horak <hhorak@redhat.com> - ss981107-40
- Build the daemon with full relro
- Removing systemd compat calls
- Removing requirement of syslog.target

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - ss981107-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 04 2012 Honza Horak <hhorak@redhat.com> - ss981107-37
- Run %%triggerun regardless of systemd_post variable definition

* Tue Sep 11 2012 Honza Horak <hhorak@redhat.com> - ss981107-36
- Minor spec file changes
- Use new systemd macros (Resolves: #850293)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - ss981107-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - ss981107-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 05 2011 Honza Horak <hhorak@redhat.com> - ss981107-33
- added systemd native unit file, removed patches for a former initscript

* Fri Aug 05 2011 Honza Horak <hhorak@redhat.com> - ss981107-32
- fixed rarpd-ss981107.patch to be apply-able
- fixed some rpmlint errors

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - ss981107-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - ss981107-30
- Convert specfile to UTF-8.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - ss981107-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - ss981107-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - ss981107-27
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - ss981107-26.1
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Jiri Moskovcak <jmoskovc@redhat.com> - ss981107-25.1
- renamed patch file

* Wed Aug 29 2007 Jiri Moskovcak <jmoskovc@redhat.com> - ss981107-25
- Modified init script to allow user to set the rarpd options via /etc/sysconfig/rarpd
- Resolves: #218998

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - ss981107-24
- Rebuild for selinux ppc32 issue.

* Mon Jul 23 2007 Jiri Moskovcak <jmoskovc@redhat.com> - ss981107-23
- Init script rewrite to comply with LSB.
- Resolves: #247042

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - ss981107-22.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - ss981107-22.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - ss981107-22.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Jul 26 2005 Phil Knirsch <pknirsch@redhat.com> ss981107-22
- Fixed and optimized loop with sprintf usage
- Added missing stdlib.h include

* Thu Jul 14 2005 Phil Knirsch <pknirsch@redhat.com> ss981107-21
- Fix for leak socket descriptors (#162000)

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> ss981107-20
- bump release and rebuild with gcc 4

* Fri Feb 18 2005 Phil Knirsch <pknirsch@redhat.com> ss981107-19
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com> ss981107-18
- rebuilt

* Wed May 12 2004 Phil Knirsch <pknirsch@redhat.com> ss981107-17
- Enabled PIE compilation and linking.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> ss981107-13
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Mar 15 2001 Trond Eivind Glomsrød <teg@redhat.com>
- more generic i18n (#26555)

* Mon Feb  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- i18nize init scripts (#26086)

* Thu Aug 17 2000 Jeff Johnson <jbj@redhat.com>
- summaries from specspo.
- typo in init script (#16450).

* Thu Jul 20 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Preston Brown <pbrown@redhat.com>
- move initscript, condrestart magic

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Fri Jun 16 2000 Bill Nottingham <notting@redhat.com>
- don't run by default

* Fri Apr  7 2000 Jakub Jelinek <jakub@redhat.com>
- initial package
