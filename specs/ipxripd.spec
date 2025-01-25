Summary: IPX RIP/SAP daemon - routing for IPX networks
Name: ipxripd
Version: 0.8
Release: 42%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: ftp://ftp.ibiblio.org/pub/Linux/system/filesystems/ncpfs/
Source0: ftp://ftp.ibiblio.org/pub/Linux/system/filesystems/ncpfs/ipxripd-%{version}.tar.gz
Source1: ipxripd.init
Source2: ipxripd.service
Patch0: ipxripd-0.8-glibc2.1.patch
Patch1: ipxripd-0.7-gcc3.patch
Patch2: ipxripd-0.7-kernel2.6.patch
Patch3: ipxripd-0.8-printf.patch
Patch4: ipxripd-0.8-stdint.patch
Patch5: ipxripd-0.8-signal.patch
BuildRequires: gcc
BuildRequires: systemd-units
BuildRequires: make

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units


%description
%{name} is an implementation of Novell's RIP and SAP protocols.
It automagically builds and updates IPX routing table in the Linux kernel.
%{name} can be useful to get a Linux box to act as an IPX router.


%prep
%setup -q
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
install -m755 ipxd $RPM_BUILD_ROOT%{_sbindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man8
install -d $RPM_BUILD_ROOT%{_mandir}/man5
install -p ipxd.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p ipx_ticks.5 $RPM_BUILD_ROOT%{_mandir}/man5

#install -d $RPM_BUILD_ROOT%{_initrddir}
#install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/ipxd

install -d $RPM_BUILD_ROOT%{_unitdir}
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/ipxd.service


%post
%systemd_post ipxd.service


%preun
%systemd_preun ipxd.service


%postun
%systemd_postun_with_restart ipxd.service




%files
%doc COPYING README ipx_ticks ipxripd-*.lsm
%{_sbindir}/*
#%{_initrddir}/*
%{_unitdir}/*
%{_mandir}/*/*


%changelog
* Thu Jan 23 2025 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.8-42
- Fix signal handler prototype for compiling with C23 standard (#2340660)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8-40
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8-31
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 18 2016 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.8-20
- Fix for 64-bit platforms (#1367852)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec  3 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.8-15
- fix format-security issue (#1037134)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.8-12
- new sustemd-rpm macros (#850169)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.8-9
- Migration from SysV to Systemd init system (#662724)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.8-5
- change initscript to comply with the LSB standarts (#246956)

* Fri Aug 17 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- change License tag to GPLv2+

* Fri Sep  1 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.8-4
- rebuild for FC6

* Wed Feb 15 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.8-3
- rebuild for FC5

* Tue Dec 13 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.8-2
- spec file cleanups
- accepted for Fedora Extra (review by John Mahowald <jpmahowald@gmail.com>)

* Thu Oct 13 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.8-1
- upgrade to 0.8
- cleanups of initrd script

* Thu Mar 10 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.7-1
- add patch for kernel >= 2.6

* Tue Aug  3 2004 Dmitry Butskoy <Dmitry@Butskoy.name>
- replace old patches by new one from PLD distribution (common "glibc2.1.patch")
- add gcc3 compilation patch to build on Fedora Core 1

* Tue Dec 14 1999 Joerg Dorchain <joerg@dorchain.net>
- added init script

* Wed Jul  8 1998 Andrzej K. Brandt <andy@mnich.ml.org>
- First version of the RPM package
- Added a quick and dirty hack to this thing to compile under glibc
  I tested it and it works fine

