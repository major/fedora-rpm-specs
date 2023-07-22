Name: pcmciautils
Summary: PCMCIA utilities and initialization programs
License: GPLv2
Version: 018
Release: 25%{?dist}
URL: http://www.kernel.org/pub/linux/utils/kernel/pcmcia/pcmcia.html
Source: http://www.kernel.org/pub/linux/utils/kernel/pcmcia/pcmciautils-%{version}.tar.bz2

ExclusiveArch: %{ix86} x86_64 ia64 ppc ppc64 %{arm}
BuildRequires: make
BuildRequires:  gcc
BuildRequires: libsysfs-devel >= 1.3.0
BuildRequires: byacc, flex

%description
The pcmciautils package contains utilities for initializing and
debugging PCMCIA and Cardbus sockets.

%prep
%setup -q

%build
make V=1 OPTIMIZATION="$RPM_OPT_FLAGS" STRIPCMD=: #%{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/lib/udev
cp -p src/yacc_config.c y.tab.c # for -debuginfo


%files
%config(noreplace) %{_sysconfdir}/pcmcia/*.opts
%dir %{_sysconfdir}/pcmcia
%attr(0644,root,root) /lib/udev/rules.d/*
/sbin/pccardctl
%attr(0755,root,root) /sbin/lspcmcia
%attr(0755,root,root) /lib/udev/pcmcia-check-broken-cis
%attr(0755,root,root) /lib/udev/pcmcia-socket-startup
%{_mandir}/man*/lspcmcia*
%{_mandir}/man*/pccardctl*

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 018-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 018-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 018-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 018-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 018-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 018-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 018-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 018-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 018-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 018-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 018-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 018-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 018-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 018-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 018-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 018-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 018-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 018-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Peter Robinson <pbrobinson@fedoraproject.org> 018-7
- Fixup arch macros, cleanup spec, drop ancient obsoletes

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 018-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 018-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 018-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Adam Jackson <ajax@redhat.com>
- Remove some ludicrously old Requires.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 018-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 018-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 23 2011 Harald Hoyer <harald@redhat.com> 018-1
- version 018

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 18 2010 Ville Skyttä <ville.skytta@iki.fi> - 017-2
- Build with $RPM_OPT_FLAGS, fix -debuginfo (#566277).

* Mon Feb 15 2010 Harald Hoyer <harald@redhat.com> 017-1
- version 017
- fix build on rawhide (bug #565133)

* Thu Aug 06 2009 Harald Hoyer <harald@redhat.com> 015-4
- add i686 buildarch

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 12 2009 Harald Hoyer <harald@redhat.com> 015-2
- moved binaries for udev rules to /lib/udev

* Fri Mar 06 2009 Harald Hoyer <harald@redhat.com> 015-1
- version 015
- added buildarch i586

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 014-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 014-12
- Autorebuild for GCC 4.3

* Fri Sep 07 2007 Harald Hoyer <harald@redhat.com> - 014-11
- fixed udev rule

* Wed Aug 22 2007 Harald Hoyer <harald@redhat.com> - 014-10
- changed license tag
- added arm architecture
- removed sh execution in udev rule

* Thu Jun 21 2007 Harald Hoyer <harald@redhat.com> - 014-9
- fixed modprobe udev rule

* Wed Jun  6 2007 Harald Hoyer <harald@redhat.com> - 014-8
- fixed 'pccardctl ident' SEGV
- Resolves: rhbz#242805

* Mon Apr  2 2007 Harald Hoyer <harald@redhat.com> - 014-7
- removed Provides, because it would conflict (#234504)
- Resolves: rhbz#234504

* Fri Mar 23 2007 Harald Hoyer <harald@redhat.com> - 014-6
- specfile cleanup

* Mon Jul 17 2006 Jesse Keating <jkeating@redhat.com> - 014-5
- rebuild
- change br sysfsutils-devel to libsysfs-devel

* Mon Jun 19 2006 Harald Hoyer <harald@redhat.com> - 014-3
- changed MODALIAS to ENV{MODALIAS} in the rules file

* Wed Jun  7 2006 Harald Hoyer <harald@redhat.com> - 014-2
- better buildrequires

* Tue Jun 06 2006 Harald Hoyer <harald@redhat.com> - 014-1
- more build requires (bug #194144)
- version 014

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 011-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 011-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Dec 13 2005  Bill Nottingham <notting@redhat.com> 011-1
- update to 011, now ships with its own udev rules
- remove pcmcia-cs provide

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Jul 24 2005  Bill Nottingham <notting@redhat.com> 007-1
- further udev-related tweaks (#163311)

* Thu Jul 21 2005  Bill Nottingham <notting@redhat.com> 006-2
- udev patch - right idea, awful execution. fix that (#163311)
- add requirement for 2.6.13-rc1, basically

* Wed Jul 20 2005  Bill Nottingham <notting@redhat.com> 006-1
- update to 006
- link libsysfs statically

* Fri Jul 08 2005  Bill Nottingham <notting@redhat.com> 005-1
- initial packaging
