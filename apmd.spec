Summary: Advanced Power Management (APM) BIOS utilities for laptops
Name: apmd
Version: 3.2.2
Release: 44%{?dist}
Source: ftp://ftp.debian.org/debian/pool/main/a/apmd/%{name}_%{version}.orig.tar.gz
Source2: apmscript
Source3: apmd.conf
Source4: laptopmode
Source5: apmd.modules
Source6: apmd.service
Patch: apmd-3.2-build.patch
Patch1: apmd-3.2-umask.patch
Patch2: apmd-3.2-error.patch
Patch4: apmd-3.2-x.patch
URL: ftp://ftp.debian.org/debian/pool/main/a/apmd
Epoch: 1
License: GPLv2+
BuildRequires: libtool
BuildRequires: systemd
BuildRequires: make
ExclusiveArch: %{ix86}

%{?systemd_requires}
Obsoletes: %{name}-sysvinit < 3.2.2-25

%description
APMD is a set of programs for controlling the Advanced Power
Management daemon and utilities found in most modern laptop
computers. APMD can watch your notebook's battery and warn
users when the battery is low. APMD is also capable of shutting
down the PCMCIA sockets before a suspend.

Install the apmd package if you need to control the APM system
on your laptop.

%prep
%setup -q -n apmd-%{version}.orig
%patch -p1 -b .build
%patch1 -p1 -b .umask
%patch2 -p1 -b .error
%patch4 -p1 -b .x
iconv -f iso-8859-1 -t utf-8 < apmsleep.fr.1 > apmsleep.fr.1_
mv apmsleep.fr.1_ apmsleep.fr.1

%build
%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{modules-load.d,sysconfig/apm-scripts}

%makeinstall APMD_PROXY_DIR=$RPM_BUILD_ROOT/etc

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man{1,8}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/fr/man1
for manpage in apm apmsleep ; do
  install -m 644 $manpage.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
done
install -m 644 apmd.8 $RPM_BUILD_ROOT/%{_mandir}/man8/
install -m 644 apmsleep.fr.1 $RPM_BUILD_ROOT/%{_mandir}/fr/man1/

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/apmd_proxy
rm -rf $RPM_BUILD_ROOT%{_bindir}/on_ac_power
rm -rf $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}

install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/apm-scripts/
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/apmd
install -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/apm-scripts/
install -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/modules-load.d/apmd.conf
install -D -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/apmd.service

%post
%systemd_post apmd.service

%preun
%systemd_preun apmd.service

%postun
%systemd_postun_with_restart apmd.service

%files
%doc ChangeLog README AUTHORS LSM
%license COPYING apmlib.COPYING
%{_mandir}/man?/*
%lang(fr) %{_mandir}/fr/man?/*
%{_bindir}/*
%{_sbindir}/*
%dir %{_sysconfdir}/sysconfig/apm-scripts
%config(noreplace) %{_sysconfdir}/sysconfig/apmd
%config(noreplace) %{_sysconfdir}/sysconfig/apm-scripts/*
%config(noreplace) %{_sysconfdir}/modules-load.d/apmd.conf
%{_unitdir}/apmd.service

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:3.2.2-37
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 28 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:3.2.2-26
- Use the right macro

* Thu Jul 28 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:3.2.2-25
- Drop -sysinit subpackage (sysvinit scripts are forbidden in Fedora)
- Use normal systemd macros
- Drop lots of old cruft

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 1:3.2.2-22
- Dropped pm-utils requirement
- Removed trailing whitespaces from the description text

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 03 2011 Jiri Skala <jskala@redhat.com> - 1:3.2.2-15
- fixes #744230 - ampd have to put apmd.conf into /etc/modules-load.d

* Wed Jul 20 2011 Jiri Skala <jskala@redhat.com> - 1:3.2.2-14
- fixed epoch in sysvinit subpackage and trigger

* Mon Jul 18 2011 Jiri Skala <jskala@redhat.com> - 1:3.2.2-13
- fixes #716970 - added native unit file
- sysvinitscript moved to subpackage

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Zdenek Prikryl <zprikryl@redhat.com> - 1:3.2.2-10
- minor spec file clean up

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jun 18 2008 Zdenek Prikryl <zprikryl@redhat.com> - 1:3.2.2-8
- cleaned spec file (#225252)

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:3.2.2-7
- Autorebuild for GCC 4.3

* Wed Nov 07 2007 Zdenek Prikryl <zprikryl@redhat.com> - 1:3.2.2-6
- Update apmscript to use pccardctl (#192942)
- Update init script to comply with LSB standard (#237771)
- Fixed starting of anacron after resume (#83770)
- Fixed X_LOCK (#127318)
- Included laptopmode script (#91878)
- Fixed restarting network (#357381)

* Tue Aug 22 2006 Jesse Keating <jkeating@redhat.com> - 1:3.2.2-5
- Fix typos in apmscript (#194024)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:3.2.2-4.1
- rebuild

* Tue Jul 11 2006 Phil Knirsch <pknirsch@redhat.com> - 1:3.2.2-4
- Added missing buildrequires: libtool (#197095)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:3.2.2-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Apr 22 2005 Bill Nottingham <notting@redhat.com> - 1:3.2.2-3
- remove shared/devel libs - nothing uses them (fixes #155724)
- since they're not needed, turn off ppc build
- fix debuginfo generation

* Wed Apr 13 2005 Bill Nottingham <notting@redhat.com> - 1:3.2.2-2
- remove on_ac_power in favor of apm/acpi/etc neutral version
- require pm-utils, where said version lives

* Wed Mar 16 2005 Bill Nottingham <notting@redhat.com> -1:3.2.2-1
- update to 3.2.2 (#115650, #125561)
- fix some ordering issues in apmscript (#92297)
- make /usr/bin/apm return errors sanely (#128405)
- fix obviously wrong sound code (#141463)

* Sat Nov 20 2004 Miloslav Trmac <mitr@redhat.com> - 1:3.0.2-25
- Convert French man page for apmsleep to UTF-8

* Mon Jun 21 2004 Alan Cox <alan@redhat.com>
- avoid xapm build(#108057) 

* Fri Jun 18 2004 Alan Cox <alan@redhat.com>
- gcc34 fix

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 19 2004 David Woodhouse <dwmw2@redhat.com>
- build on ppc too because that emulates APM

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Oct 22 2003 Bill Nottingham <notting@redhat.com> 1:3.0.2-20
- initscript cleanups (#97781)
- add amd to RESTORESERVICES (#102365)

* Mon May 19 2003 Bill Nottingham <notting@redhat.com> 1:3.0.2-19
- add support for laptop_mode in apmscript
- make LOWPOWER_SERVICES not depend on POWER_SERVICES (#74935)
- remove xapm manpage (#77900)
- fix soundmodules bogosity (#90592)
- fix ordering of network & services (#90512, #85436, <dberger@oubliette.org>)
- own /etc/sysconfig/apm-scripts (#74026)
- run anacron with -s (#65689)

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Thu Feb 20 2003 Bill Nottingham <notting@redhat.com> 1:3.0.2-17
- don't remove network modules (#83996)

* Tue Feb 18 2003 Bill Nottingham <notting@redhat.com> 1:3.0.2-16
- pass arguments to apmcontinue-pre (#83398, <aleksey@nogin.org>)
- fix NETDEVICES line (#81153)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan  2 2003 Jeremy Katz <katzj@redhat.com> 1:3.0.2-14
- add CPUFREQ= to /etc/sysconfig/apmd
- if CPUFREQ="yes" and /proc/cpufreq exists, use cpufreq to change between 
  performance and power-save when switching between ac and battery

* Fri Nov 22 2002 Tim Powers <timp@redhat.com>
- remove unpackaged files from the buildroot

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Apr 15 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-10
- Check for Epoch in postuninstall trigger (#62615)

* Fri Apr 12 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-9
- Fix bug in screen locking mechanism (typo: `/sbin/pidof` should
  have been `/sbin/pidof X`)

* Wed Apr  3 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-8
- Fix interoperability with hotplug (#62045)
- Fix build with current kernel headers

* Mon Mar 11 2002 Bill Nottingham <notting@redhat.com> 3.0.2-7
- add epoch so we can upgrade 3.0final

* Tue Feb 26 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-6
- Fix up network device detection (#59447)
- Adapt hwclock calls to current hwclock behavior (#59994)
- Fix net device resume (#59009, #49918)
- Re-add pre-{suspend,resume} hooks (#44603)
- Move LOW_POWER notification file to /var/run/apmd (#56389)
- Determine if X is running before anything else (#20892)
- Run hwclock earlier on resume (#28234)
- Change permissions on /etc/sysconfig/apmd, 0644 is sufficient (#54222)
- Fix stab location (#56718)
- Don't mess up terminal beep on resume (#57955)

* Wed Jan 23 2002 Tim Powers <timp@redhat.com>
- really remove xapm

* Tue Jan 22 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-4
- Remove xapm

* Sat Jan 19 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-2
- Try to work around some more BIOS bugs
- Log which network devices are up when entering suspend mode; the old
  way, only ONBOOT network devices would come back up.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Nov 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-1
- 3.0.2

* Fri Nov 16 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0final-36
- Add yet another workaround for broken BIOSes, #56368
- Don't restart network/netfs unless it was running at suspend time, #54041

* Fri Nov  9 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0final-35
- Add RESTORESERVICES option, fixes #55885

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0final-34
- Add support for kernels with modular apm (RFE #49683)

* Tue Jun 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0final-33
- Add pre-suspend and pre-resume hooks (#44603, #45706)

* Mon Jun 25 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.0final-32
- Add possibility to unload network modules on suspend, required for 3c59x
  (RFE #45706)

* Sat May 12 2001 Than Ngo <than@redhat.com>
- fix problem after a suspend the reinitialization of the network card fails.
- clean up specfile

* Tue Apr 10 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- If we need to lock the screen at suspend and we're running KDE, use a DCOP call
  rather than launching xscreensaver
- Add hooks to stop services when switching to battery power and to restart them when we
  return to line power
- Add hooks to stop services when running short of battery power and to restart them when we
  return to line power
- Add maestro and cs4281 to the default SOUNDMODULES, they're quite common

* Thu Feb 15 2001 Trond Eivind Glomsrd <teg@redhat.com>
- <time.h>-change

* Mon Feb  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- i18nize init script

* Thu Feb  1 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix build with current kernel headers

* Mon Jan  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Don't set umask(0) at startup! (#23133)
- Add support for restarting the network on resume, especially
  useful for DHCP (#22994)
- mark /etc/sysconfig/apmd %%config(noreplace)
- Treat a "standby" event like a "suspend" event (#21115)
- Greatly improve sound handling, based on patch from
  pcfe@redhat.com (#21394)

* Mon Dec 11 2000 Than Ngo <than@redhat.com>
- rebuilt with the fixed fileutils

* Thu Nov  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Remove the obsolete -i and -n options from the man page (Bug #19610)
- Fix build with tar >= 1.13.18

* Tue Oct 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Work around yet another BIOS bug ("Bug" #19674)
- Fix up the check for running anacron

* Mon Oct  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- It's /sbin/cardctl, not /usr/sbin/cardctl (Bug #18021)

* Thu Aug 31 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- change startup order - apmd should be started after netfs to cope with
  an NFS /usr (Not that anyone uses NFS mounted filesystems on notebooks,
  but...) (Bug #16251)

* Wed Aug 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Add NETFS_RESTART feature, fix up LOCK_X to use yes/no like the
  other settings (Bug #17068 and some other stuff)

* Fri Aug 25 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix typo in suspend script, bug #16957

* Thu Aug 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up "status" in init script, bug #16275

* Tue Aug  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- ignore "start" and "stop" events in apmscript instead of claiming
  they're unknown events (Bug #15598)

* Sat Aug 05 2000 Bill Nottingham <notting@redhat.com>
- condrestart fixes

* Thu Aug  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Handle "power" events in apmscript (Bug #15283)

* Tue Aug  1 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix typo in man page (Bug #14778)

* Mon Jul 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Use cardctl to suspend/resume pcmcia cards instead of restarting
  the entire subsystem (Bug #13836)

* Mon Jul 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Don't use obsolete parameters (Bug #13710)
- Add the possibility to lock X displays on suspend, based on patch from
  Hannu Martikka <Hannu.Martikka@nokia.com>
- some other fixes to the apmd scripts

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 27 2000 Preston Brown <pbrown@redhat.com>
- don't prereq, just require initscripts

* Mon Jun 26 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix init script, move to /etc/init.d

* Sun Jun 25 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix resume for users of non-bash shells (Bug #11580)
- Support restoring sound with the commercial OSS drivers (Bug #11580)

* Mon Jun 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- FHSify

* Sat May 27 2000 Bernhard Rosenkrnzer <bero@redhat.com>
- Some more changes to apm-scripts:
  - Fix up HDPARM_AT_RESUME
  - Add ANACRON_ON_BATTERY, and default to turning it off

* Mon May  8 2000 Bernhard Rosenkrnzer <bero@redhat.com>
- Various fixes to the apm-scripts:
  - use modprobe instead of insmod for restoring sound
  - don't try to restore the X display if X isn't running
  - /usr/sbin/anacron, not /usr/bin/anacron
  - misc. cleanups

* Fri Feb  4 2000 Bernhard Rosenkrnzer <bero@redhat.com>
- rebuild to compress man pages

* Mon Jan 17 2000 Bernhard Rosenkrnzer <bero@redhat.com>
- Update to 3.0final

* Mon Jan 17 2000 Bernhard Rosenkrnzer <bero@redhat.com>
- Fixes for UTC clocks (Bug #7939)

* Thu Jan  6 2000 Bernhard Rosenkrnzer <bero@redhat.com>
- If anacron is installed, run it at resume time.

* Sun Nov 21 1999 Bernhard Rosenkrnzer <bero@redhat.com>
- Fix up the broken harddisk fix (needs to be done earlier during suspend,
  also we need to manually wake the drive at resume.)

* Sun Nov 21 1999 Bernhard Rosenkrnzer <bero@redhat.com>
- Updates to the apm-scripts and sysconfig/apmd:
  - Make hwclock --hctosys call optional (CLOCK_SYNC variable)
  - Add possibility to modify hdparm settings on suspend/resume.
    Some broken harddisks (Gericom 3xC) require this for suspend
    to disk to work.

* Wed Nov 10 1999 Bernhard Rosenkrnzer <bero@redhat.com>
- Put in new apm scripts to handle PCMCIA suspend/resume, and give the
  possibility to refresh displays and reload sound modules for some
  broken chipsets
- permit builds on i486, i586 and i686 archs

* Mon Sep 20 1999 Michael K. Johnson <johnsonm@redhat.com>
- accept both "UTC=yes" and "UTC=true"

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- uh-oh, do I own this now?
- update to 3.0beta9

* Thu Jul  1 1999 Bill Nottingham <notting@redhat.com>
- start after, die before network fs...

* Sat Jun 12 1999 Jeff Johnson <jbj@redhat.com>
- add check for /proc/apm (not on SMP) (#3403)

* Mon May 31 1999 Jeff Johnson <jbj@redhat.com>
- shell script tweak (#3176).

* Fri May  7 1999 Bill Nottingham <notting@redhat.com>
- set -u flag for utc

* Sat Apr 17 1999 Matt Wilson <msw@redhat.com>
- prereqs chkconfig

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- exlusive arch i3786, as sparcs and alphas have no apm support...

* Wed Apr 14 1999 <ewt@redhat.com>
- removed X bits; gnome has a much better X interface for apm anyway

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- quoted APMD_OPTIONS variable in the init script

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- whoops, making /etc/rc.d/init.d/apmd a directory was a bad idea. fixed.

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- now owned by Avery Pennarun <apenwarr@debian.org>, upgraded to his latest.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- updated to latest patchlevel from web page.

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced init script

* Thu Apr 2 1998 Erik Troan <ewt@redhat.com>
- moved init script into a separate source file
- added restart and status options to initscript
- made it use a build root
- don't start apm when the package is installed
- don't stop apm when the package is removed

* Mon Dec  8 1997 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Compiled on RH5.0 against libc6.
- Renamed /etc/rc.d/init.d/apmd.init to /etc/rc.d/init.d/apmd
- Make /etc/rc.d/init.d/apmd to be chkconfig-compliant.

* Thu Oct  2 1997 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Fixed buggy /etc/sysconfig/apmd file generation in the spec file.
- Added a patch for apm.c's option handling.
- Both fixes were submitted by Richard D. McRobers <rdm@csn.net>
