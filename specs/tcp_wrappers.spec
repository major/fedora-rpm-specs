Summary: A security tool which acts as a wrapper for TCP daemons
Name: tcp_wrappers
Version: 7.6
Release: 108%{?dist}

%global LIB_MAJOR 0
%global LIB_MINOR 7
%global LIB_REL 6

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Source: ftp://ftp.porcupine.org/pub/security/%{name}_%{version}-ipv6.4.tar.gz
URL: ftp://ftp.porcupine.org/pub/security/index.html
Patch0: tcpw7.2-config.patch
Patch1: tcpw7.2-setenv.patch
Patch2: tcpw7.6-netgroup.patch
Patch3: tcp_wrappers-7.6-bug11881.patch
Patch4: tcp_wrappers-7.6-bug17795.patch
Patch5: tcp_wrappers-7.6-bug17847.patch
Patch6: tcp_wrappers-7.6-fixgethostbyname.patch
Patch7: tcp_wrappers-7.6-docu.patch
Patch8: tcp_wrappers-7.6-man.patch
Patch9: tcp_wrappers.usagi-ipv6.patch
Patch11: tcp_wrappers-7.6-shared.patch
Patch12: tcp_wrappers-7.6-sig.patch
Patch14: tcp_wrappers-7.6-ldflags.patch
Patch15: tcp_wrappers-7.6-fix_sig-bug141110.patch
Patch16: tcp_wrappers-7.6-162412.patch
Patch17: tcp_wrappers-7.6-220015.patch
Patch19: tcp_wrappers-7.6-siglongjmp.patch
Patch20: tcp_wrappers-7.6-sigchld.patch
Patch21: tcp_wrappers-7.6-196326.patch
Patch22: tcp_wrappers_7.6-249430.patch
Patch23: tcp_wrappers-7.6-inetdconf.patch
Patch24: tcp_wrappers-7.6-bug698464.patch
Patch26: tcp_wrappers-7.6-xgets.patch
Patch27: tcp_wrappers-7.6-initgroups.patch
Patch28: tcp_wrappers-7.6-warnings.patch
Patch29: tcp_wrappers-7.6-uchart_fix.patch
Patch30: tcp_wrappers-7.6-altformat.patch
# RFE: rhbz#1181815
Patch31: tcp_wrappers-7.6-aclexec.patch
Patch32: tcp_wrappers-inetcf-c99.patch
# required by sin_scope_id in ipv6 patch
BuildRequires: make
BuildRequires: glibc-devel >= 2.2
BuildRequires: libnsl2-devel
BuildRequires: gcc
Requires: tcp_wrappers-libs%{?_isa} = %{version}-%{release}

%description
The tcp_wrappers package provides small daemon programs which can
monitor and filter incoming requests for systat, finger, FTP, telnet,
rlogin, rsh, exec, tftp, talk and other network services.

Install the tcp_wrappers program if you need a security tool for
filtering incoming network services requests.

This version also supports IPv6.

%package libs
Summary: Libraries for tcp_wrappers
Obsoletes: tcp_wrappers-devel <= 0:7.6-91

%description libs
tcp_wrappers-libs contains the libraries of the tcp_wrappers package.

%prep
%setup -q -n %{name}_%{version}-ipv6.4
%patch -P0 -p1 -b .config
%patch -P1 -p1 -b .setenv
%patch -P2 -p1 -b .netgroup
%patch -P3 -p1 -b .bug11881
%patch -P4 -p1 -b .bug17795
%patch -P5 -p1 -b .bug17847
%patch -P6 -p1 -b .fixgethostbyname
%patch -P7 -p1 -b .docu
%patch -P8 -p1 -b .man
%patch -P9 -p1 -b .usagi-ipv6
%patch -P11 -p1 -b .shared
%patch -P12 -p1 -b .sig
%patch -P14 -p1 -b .ldflags
%patch -P15 -p1 -b .fix_sig
%patch -P16 -p1 -b .162412
%patch -P17 -p1 -b .220015
%patch -P19 -p1 -b .siglongjmp
%patch -P20 -p1 -b .sigchld
%patch -P21 -p1 -b .196326
%patch -P22 -p1 -b .249430
%patch -P23 -p1 -b .inetdconf
%patch -P24 -p1 -b .698464
%patch -P26 -p1 -b .xgets
%patch -P27 -p1 -b .initgroups
%patch -P29 -p1 -b .uchart_fix
%patch -P30 -p1 -b .altformat
%patch -P28 -p1 -b .warnings
%patch -P31 -p1 -b .aclexec
%patch -P32 -p1

%build
make \
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fPIC -DPIC -D_REENTRANT -DHAVE_STRERROR -DACLEXEC" \
LDFLAGS="$RPM_LD_FLAGS" \
MAJOR=%{LIB_MAJOR} MINOR=%{LIB_MINOR} REL=%{LIB_REL} linux %{?_smp_mflags}


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}
mkdir -p ${RPM_BUILD_ROOT}/%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{3,5,8}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}

install -p -m644 hosts_access.3 ${RPM_BUILD_ROOT}%{_mandir}/man3
install -p -m644 hosts_access.5 hosts_options.5 ${RPM_BUILD_ROOT}%{_mandir}/man5
install -p -m644 tcpd.8 tcpdchk.8 tcpdmatch.8 safe_finger.8 try-from.8 ${RPM_BUILD_ROOT}%{_mandir}/man8
ln -sf hosts_access.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/hosts.allow.5
ln -sf hosts_access.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/hosts.deny.5
#cp -a libwrap.a ${RPM_BUILD_ROOT}%{_libdirdir}
cp -a libwrap.so* ${RPM_BUILD_ROOT}/%{_libdir}
#install -p -m644 libwrap.so.0.7.6 ${RPM_BUILD_ROOT}/%{_libdir}
install -p -m644 tcpd.h ${RPM_BUILD_ROOT}%{_includedir}
install -m755 safe_finger ${RPM_BUILD_ROOT}%{_sbindir}
install -m755 tcpd ${RPM_BUILD_ROOT}%{_sbindir}
install -m755 try-from ${RPM_BUILD_ROOT}%{_sbindir}
install -m755 tcpdmatch ${RPM_BUILD_ROOT}%{_sbindir}

# XXX remove utilities that expect /etc/inetd.conf (#16059).
#install -m755 tcpdchk ${RPM_BUILD_ROOT}%{_sbindir}
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man8/tcpdchk.*

# Remove the files from -devel subpackage
rm -f ${RPM_BUILD_ROOT}%{_includedir}/*
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.so
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man3/*

%ldconfig_scriptlets libs

%files
%{!?_licensedir:%global license %%doc}
%license DISCLAIMER
%doc BLURB CHANGES README* Banners.Makefile
%{_sbindir}/*
%{_mandir}/man8/*

%files libs
%{!?_licensedir:%global license %%doc}
%license DISCLAIMER
%doc BLURB CHANGES README* Banners.Makefile
%{_libdir}/*.so.*
%{_mandir}/man5/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 7.6-107
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-104
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-103
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Florian Weimer <fweimer@redhat.com> - 7.6-102
- Fix pointer truncation issue and C99 compatibility (#2148869)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-100
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Björn Esser <besser82@fedoraproject.org> - 7.6-99
- Rebuild(libnsl2)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-97
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-96
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-95
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-93
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Jakub Jelen <jjelen@redhat.com> - 7.6-91
- Properly obsolete devel subpackage (#1560757)

* Thu Mar 08 2018 Jakub Jelen <jjelen@redhat.com> - 7.6-90
- Properly inject build flags (#1548669)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-89
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Jakub Jelen <jjelen@redhat.com> - 7.6-88
- Remove the devel subpackage (#1495181)
- Adjust build process for recent changes (nsl separated from glibc-headers)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-87
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Jakub Jelen <jjelen@redhat.com> - 7.6-84
- Fix packaging details (#226482)

* Tue Mar 01 2016 Jakub Jelen <jjelen@redhat.com> 7.6-83
- Fix behaviour for long lines in hosts_option files

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-82
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 23 2015 Jakub Jelen <jjelen@redhat.com> 7.6-80
- add ACLEXEC option (#1181815)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug  6 2014 Tom Callaway <spot@fedoraproject.org> - 7.6-78
- fix license handling

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Petr Lautrbach <plautrba@redhat.com> 7.6-76
- clean warnings and fix compiler inet_ntop issue (#977995)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-75
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Petr Lautrbach <plautrba@redhat.com> 7.6-74
- fix the tcp_wrappers-7.6-altformat.patch (#979009,#981788)

* Fri Feb  8 2013 Viktor Hercinger <vhercing@redhat.com> - 7.6-73
- Add full relro support

* Fri Feb  8 2013 Viktor Hercinger <vhercing@redhat.com> - 7.6-72
- Put binaries and libraries under /usr instead of root

* Mon Jan 28 2013 Viktor Hercinger <vhercing@redhat.com> - 7.6-71
- Updated to version with upstream IPv6 support

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Jan F. Chadima <jchadima@redhat.com> - 7.6-68
- remove most of warnings

* Mon Aug 15 2011 Jan F. Chadima <jchadima@redhat.com> - 7.6-67
- clean (set up correctly) additional groups

* Mon Aug 15 2011 Jan F. Chadima <jchadima@redhat.com> - 7.6-66
- repair possible DOS in xgets

* Wed Aug 10 2011 Jan F. Chadima <jchadima@redhat.com> - 7.6-65
- Add partial relro support for libraries

* Tue May 24 2011 Jan F. Chadima <jchadima@redhat.com> - 7.6-64
- Improve the support for IPv4 /prefix notation (#698464)

* Wed May  4 2011 Jan F. Chadima <jchadima@redhat.com> - 7.6-61
- Add support for IPv4 /prefix notation (#698464)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 16 2010 Jan F. Chadima <jchadima@redhat.com> - 7.6-59
- Add modified tcpdmatch (#604011)

* Fri Feb  5 2010 Jan F. Chadima <jchadima@redhat.com> - 7.6-58
- Add manual pages for safe_finger and try-from (#526190)

* Wed Jan  6 2010 Jan F. Chadima <jchadima@redhat.com> - 7.6-57
- Merge review (#226482)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Jan F. Chadima <jchadima@redhat.com> - 7.6-55
- resolving addr when name == "" (repair of patch #220015)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Jan Safranek <jsafranek@redhat.com> - 7.6-53
- rediff all patches to get rid of patch fuzz

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 7.6-52
- Autorebuild for GCC 4.3

* Tue Oct 16 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-51
- review changes

* Fri Aug 24 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-50
- license tag update (and rebuild for BuildID, etc.)
- include docs in the -libs subpackage, as it is the only one installed on most
  systems (and to comply with the license text)

* Wed Jul 25 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-49
- fix for a.b.c.d/255.255.255.255 - fixes #249430

* Thu Jun 28 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-48
- dropped the hostname resolving patch
- resolve the address given to hosts_ctl to hostname, if hostname not given
- compare localhost and localhost.localdomain as the same
- fixed a few compile warnings

* Wed Jun 06 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-47
- fix the hostname resolving patch for x86_64

* Mon May 28 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-46
- modified the fix for #112975 to fix #156373 as well

* Fri May 25 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-45
- unblock and catch SIGCHLD from spawned shell commands, fixes #112975

* Mon Apr 16 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-44
- added restore_sigalarm and siglongjmp patches from Debian, fixes #205129

* Fri Mar 09 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-43
- resolve hostnames in hosts.{allow,deny}, should fix a bunch of issues with
  IPv4/6

* Thu Mar 08 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-42.1
- moved libwrap.so* to /lib
- removed the static library libwrap.a

* Mon Mar 05 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-42
- added Obsoletes field so that the upgrade goes cleanly
- added dist tag

* Mon Dec  4 2006 Thomas Woerner <twoerner@redhat.com> 7.6-41
- moved devel libraries, headers and man pages into devel sub package (#193188)
- new libs sub package for libraries
- using BuildRequires instead of BuildPreReq

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 7.6-40.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 7.6-40.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 7.6-40.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 24 2006 Thomas Woerner <twoerner@redhat.com> 7.6-40
- fixed uninitialized fp in function inet_cfg (#162412)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri May  6 2005 Thomas Woerner <twoerner@redhat.com> 7.6-39
- fixed sig patch (#141110). Thanks to Nikita Shulga for the patch

* Wed Feb  9 2005 Thomas Woerner <twoerner@redhat.com> 7.6-38
- rebuild

* Thu Oct  7 2004 Thomas Woerner <twoerner@redhat.com> 7.6-37.2
- new URL and spec file cleanup, patch from Robert Scheck

* Mon Oct  4 2004 Thomas Woerner <twoerner@redhat.com> 7.6-37.1
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Mar  5 2004 Thomas Woerner <twoerner@redhat.com> 7.6-36
- pied tcpd

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Feb 16 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- use strerror  #84312

* Tue Feb 11 2003 Harald Hoyer <harald@redhat.de> 7.6-33
- revert Nalins weak version
- link libwrap.so against libnsl, on which it depends

* Mon Feb 10 2003 Nalin Dahyabhai <nalin@redhat.com> 7.6-32
- link libwrap.so against libnsl, on which it depends
- add default (weak) versions of allow_severity and deny_severity to the shared
  library so that configure tests can find it correctly

* Mon Feb 10 2003 Harald Hoyer <harald@redhat.de> 7.6-29
- shared library generated and added #75494
- added security patch tcp_wrappers-7.6-sig.patch
- compile and link with -fPIC -DPIC

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Jeff Johnson <jbj@redhat.com> 7.6-25
- don't include -debuginfo files in package.

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 11 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix #61192
- added Patch8 to fix #17847
- update IPv6 patch

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Mar 11 2001 Pekka Savola <pekkas@netcore.fi>
- Add IPv6 patch from USAGI, enable it.

* Mon Feb  5 2001 Preston Brown <pbrown@redhat.com>
- fix gethostbyname to work better with dot "." notation (#16949)

* Sat Dec 30 2000 Jeff Johnson <jbj@redhat.com>
- permit hosts.{allow,deny} to be assembled from included components (#17795).
- permit '*' and '?' wildcard matches on hostnames (#17847).

* Sun Nov 19 2000 Bill Nottingham <notting@redhat.com>
- ia64 needs -fPIC too

* Mon Aug 14 2000 Jeff Johnson <jbj@redhat.com>
- remove utilities that expect /etc/inetd.conf (#16059).

* Thu Jul 27 2000 Jeff Johnson <jbj@redhat.com>
- security hardening (#11881).

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun  6 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Tue May 16 2000 Chris Evans <chris@ferret.lmh.ox.ac.uk>
- Make tcpd mode -rwx--x--x as a security hardening measure

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man pages.

* Mon Aug 23 1999 Jeff Johnson <jbj@redhat.com>
- add netgroup support (#3940).

* Wed May 26 1999 Jeff Johnson <jbj@redhat.com>
- compile on sparc with -fPIC.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Sat Aug 22 1998 Jeff Johnson <jbj@redhat.com>
- close setenv bug (problem #690)
- spec file cleanup

* Thu Jun 25 1998 Alan Cox <alan@redhat.com>
- Erp where did the Dec 05 patch escape to

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- don't build setenv.o module -- it just breaks things

* Wed Oct 29 1997 Marc Ewing <marc@redhat.com>
- upgrade to 7.6

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Upgraded to version 7.5
- Uses a build root
