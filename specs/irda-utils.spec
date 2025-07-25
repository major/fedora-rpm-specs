%global _hardened_build 1

Summary:         Utilities for infrared communication between devices
Name:            irda-utils
Version:         0.9.18
Release:         52%{?dist}
Url:             http://irda.sourceforge.net
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:         GPL-2.0-or-later
ExcludeArch:     s390 s390x
Source0: http://downloads.sourceforge.net/irda/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1: irda.init
Source2: irda.service
Source3: irda.sysconfig
Patch1: irda-utils-0.9.17-rootonly.patch
Patch2: irda-utils-0.9.15-rh1.patch
Patch3: irda-utils-0.9.16-io.patch
Patch4: irda-utils-0.9.17-makefile.patch
Patch6: irda-utils-0.9.18-root.patch
Patch7: irda-utils-0.9.18-man.patch
Patch8: irda-utils-0.9.18-PIE.patch
Patch9: irda-utils-0.9.18-no-inline.patch
Patch10: irda-utils-0.9.18-run.patch
Patch11: irda-utils-0.9.18-sbin.patch
BuildRequires: gcc
BuildRequires: glib2-devel, pciutils-devel
BuildRequires: systemd-units
BuildRequires: make

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units


%description
IrDA(TM) (Infrared Data Association) is an industry standard for
wireless, infrared communication between devices. IrDA speeds range
from 9600 bps to 4 Mbps, and IrDA can be used by many modern devices
including laptops, LAN adapters, PDAs, printers, and mobile phones.

The Linux-IrDA project is a GPL'd implementation, written from
scratch, of the IrDA protocols. Supported IrDA protocols include
IrLAP, IrLMP, IrIAP, IrTTP, IrLPT, IrLAN, IrCOMM and IrOBEX.

The irda-utils package contains a collection of programs that enable
the use of IrDA protocols. Most IrDA features are implemented in the
kernel, so IrDA support must be enabled in the kernel before any IrDA
tools or programs can be used. Some configuration outside the kernel
is required, however, and some IrDA features, like IrOBEX, are
actually implemented outside the kernel.


%prep
%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P6 -p1
gunzip man/irnet.4.gz man/irda.7.gz
%patch -P7 -p1
gzip -9 man/irnet.4 man/irda.7
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1


%build
export LDFLAGS="%{?__global_ldflags}"
make all RPM_OPT_FLAGS="$RPM_OPT_FLAGS -std=gnu89" ROOT="$RPM_BUILD_ROOT" \
   LDFLAGS="%{?__global_ldflags}" \
   CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

for dir in %{_bindir} %{_initrddir} %{_sysconfdir}/sysconfig
do
    install -d $RPM_BUILD_ROOT$dir
done

make install  ROOT="$RPM_BUILD_ROOT" MANDIR="$RPM_BUILD_ROOT/%{_mandir}"

#install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT/%{_initrddir}/irda
#chmod -x $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/irda
rm -f $RPM_BUILD_ROOT/%{_initrddir}/irda

install -d $RPM_BUILD_ROOT%{_unitdir}
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/irda.service
install -p -m644 %{SOURCE3} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/irda

rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/network-scripts/ifcfg-irlan0

for i in irattach irdadump irdaping tekram
do
    [ -f $i/README ] && ln $i/README README.$i
done
iconv -f ISO8859-1 -t UTF-8 <README.irdadump >README.irdadump.new && \
	mv -f README.irdadump.new README.irdadump
mv etc/modules.conf.irda etc/modprobe.conf.irda
chmod -x etc/ifcfg-irlan0



%post
%systemd_post irda.service


%preun
%systemd_preun irda.service


%postun
%systemd_postun_with_restart irda.service


%files
%{_bindir}/*
%{_mandir}/*/*
%{_unitdir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/irda
%doc README* etc/ifcfg-irlan0 etc/modprobe.conf.irda


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 23 2025 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.18-51
- Use /usr/bin instead of /usr/sbin (#2340661)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.18-49
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.18-40
- move /var/run to /run and fix systemd service file (#1960900)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.18-39
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.18-29
- add no-inline patch for new compilers
- require pciutils-devel for smcinit

* Sun Feb 12 2017 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.18-25
- enable smcinit (#1421387)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.18-18
- build with PIE flags (#955165)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.18-16
- new systemd-rpm macros (#850171)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.18-13
- migrate from SysV to Systemd init system (#694940)

* Fri Jul 15 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.18-12
- spec file cleanup
- add own init script instead of huge patched original one
  (and fix #242468)
- disable smcinit manuals in smcdisable patch as well
- fix typos in man pages (#668122, #675677)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 20 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9.18-10
- Add patch to fix installing of initscript into buildroot

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.9.18-9
- Convert specfile to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Karsten Hopp <karsten@redhat.com> 0.9.18-6
- use macros, fix Source0

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.18-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.18-4
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Karsten Hopp <karsten@redhat.com> 0.9.18-3
- rebuild for buildid

* Wed Feb 21 2007 Karsten Hopp <karsten@redhat.com> 0.9.18-2
- review cleanups

* Tue Jan 23 2007 Karsten Hopp <karsten@redhat.com> 0.9.18-1
- update to 0.9.18

* Tue Aug 01 2006 Karsten Hopp <karsten@redhat.de> 0.9.17-2
- initscript fix from Paul Bolle (#168325)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.9.17-1.1
- rebuild

* Mon Jun 19 2006 Karsten Hopp <karsten@redhat.de> 0.9.17-1
- update to 0.9.17
- makefile fixes
- disable smcinit
- use manpages from 0.9.17-pre3 as those from 0.9.17 are corrupted

* Mon Apr 03 2006 Karsten Hopp <karsten@redhat.de> 0.9.16-8
- don't use asm/io.h directly (Bastien Nocera #186875)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9.16-7.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9.16-7.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 0.9.16-7
- build with gcc-4

* Tue Feb 15 2005 Karsten Hopp <karsten@redhat.de> 0.9.16-6
- use RPM_OPT_FLAGS as CFLAGS

* Tue Feb 15 2005 Karsten Hopp <karsten@redhat.de> 0.9.16-5 
- load irtty-sir module (#148750)

* Wed Feb 02 2005 Karsten Hopp <karsten@redhat.de> 0.9.16-4 
- use glib2 instead of glib (#136223)

* Mon Oct 04 2004 Karsten Hopp <karsten@redhat.de> 0.9.16-3
- load irda modules to make it work with udev (#134322)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 02 2004 Karsten Hopp <karsten@redhat.de> 0.9.16-1 
- update

* Wed Feb 18 2004 Karsten Hopp <karsten@redhat.de> 0.9.15-5 
- add manpages (#115972)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jan 24 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- do not use *.spec as filename for a patch

* Mon Nov 24 2003 Karsten Hopp <karsten@redhat.de> 0.9.15-2
- fix array usage (#110791)

* Sun Oct 19 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add a %%clean specfile target

* Thu Jul 03 2003 Karsten Hopp <karsten@redhat.de> 0.9.15-1.1
- rebuilt

* Wed Jul 02 2003 Karsten Hopp <karsten@redhat.de> 0.9.15-1
- update
- removed libtool patch, it's obsolete now
- new root patch

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec 16 2002 Dan Walsh <dwalsh@redhat.com> 0.9.14-8
- Fixed service script description

* Mon Dec 09 2002 Phil Knirsch <pknirsch@redhat.com> 0.9.14-7
- Fixed problem with %%doc entries.

* Tue Jul 09 2002 Phil Knirsch <pknirsch@redhat.com> 0.9.14-6
- Removed the ifcfg-irlan0 file. It shouldn't be installed by default. Moved it
  to the docs dir.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.9.14-5
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com> 0.9.14-4
- automated rebuild

* Thu Apr  4 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.9.14-3
- Stop irda service earlier (#61777)

* Mon Jul 16 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.9.14-2
- Fix libtool detection (#49093)

* Tue Apr 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.9.14-1
- 0.9.14-1

* Thu Feb  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Make init scripts more i18n friendly (use $0, $prog)
  Bugs #26527 and #26550
- Exclude S/390 (they don't have the needed hardware)

* Mon Feb  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- i18nize init scripts (#26077)

* Wed Jan 10 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- chmod -x /etc/sysconfig/irda (#22837)

* Sat Jan  6 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up the init script

* Mon Dec 25 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Get rid of the /etc/modules.conf hack; the entries are in the
  latest modutils by default. (Bug #22799)
- Require modutils >= 2.3.21-4 to make sure the modules.conf hack
  isn't needed

* Wed Dec  6 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Require modutils >= 2.3.11-5 rather than /etc/modules.conf

* Tue Dec  5 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.9.13

* Tue Oct 31 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Add necessary entries to /etc/modules.conf in %%post (Bug #19960)
- Update source URL
- Fix build with current kernel 2.4 header files

* Mon Oct  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- make irdadump exit with an error message rather than a segfault when
  run as non-root
- Update URL

* Wed Aug  2 2000 Bill Nottingham <notting@redhat.com>
- fix start priority (345 isn't right...)
- fix condrestart

* Sun Jul 23 2000 Trond Eivind Glomsrød <teg@redhat.com>
- source files from /etc/rc.d/init.d

* Sun Jul 23 2000 Trond Eivind Glomsrød <teg@redhat.com>
- don't prereq /etc/init.d anymore
- rename "rh-status"
- use %%{_tmppath}

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 27 2000 Preston Brown <pbrown@redhat.com>
- don't prereq, only require initscripts

* Mon Jun 26 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up initscripts
- chkconfigize

* Sun Jun 18 2000 Matt Wilson <msw@redhat.com>
- rebuilt for next release

* Fri Feb  4 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.9.10
- add docs

* Fri Feb  4 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- strip libraries

* Mon Jan 31 2000 Bill Nottingham <notting@redhat.com>
- fix typo in initscript

* Mon Oct 11 1999 Cristian Gafton <gafton@redhat.com>
- remove some of the network config files (and hope that the package will
  still work :-)

* Sun Oct 10 1999 Bernhard Rosenkraenzer <bero@redhat.de>
- Add the /etc/irda directory. It's needed.
- Add the /etc/rc.d/init.d/irda script to start the irda daemon
- chkconfig'ize /etc/rc.d/init.d/irda

* Fri Sep 17 1999 Cristian Gafton <gafton@redhat.com>
- build for RH 6.1
- add patch to make the damn package compile without any IrDA installed.
