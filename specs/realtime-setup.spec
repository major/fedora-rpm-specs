Name: realtime-setup
Version: 2.5
Release: 5%{?dist}
License: GPL-2.0-or-later
Summary: Setup RT/low-latency environment details
Source0: https://gitlab.com/rt-linux-tools/%{name}/-/archive/v%{version}/%{name}-%{version}.tar.bz2
URL:  https://gitlab.com/rt-linux-tools/realtime-setup.git

BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: annobin-plugin-gcc
Requires: pam
Requires: tuna
Requires: tuned
Requires: tuned-profiles-realtime
Requires: systemd

# disable generation of debuginfo packages for this package
# the only executable from this package is realtime-entsk and it's not really
# something that requires debugging.
%global debug_package %{nil}

%description
Configure details useful for low-latency environments.

Installation of this package results in:
  - creation of a realtime group
  - adds realtime limits configuration for PAM
  - adds udev specific rules for threaded irqs and /dev/rtc access
  - adds /usr/bin/slub_cpu_partial_off to turn off cpu_partials in SLUB
  - adds net-socket timestamp static key daemon (realtime-entsk)

The slub_cpu_partial_off script is used to turn off the SLUB slab allocator's
use of cpu-partials, which has been known to create latency-spikes.

The realtime-entsk program is a workaround for latency spikes caused when the
network stack enables hardware timestamping and activates a static key. The
realtime-entsk progam is activated by the systemd service included and merely
enables the timestamp static key and pauses, effectively activating the static
key and never exiting, so no deactivation/activation sequences will be seen.

Neither the slub script or realtime-entsk are active by default.


%prep
%setup -q -n %{name}-%{version}


%build
%make_build CFLAGS="%{build_cflags} -D_GNU_SOURCE" all

%install
%make_install DEST=%{buildroot} install

%post
/usr/sbin/groupadd -f -g 71 realtime

%preun
%systemd_preun realtime-setup.service

%files
%config(noreplace) %{_sysconfdir}/security/limits.d/realtime.conf
%config(noreplace) %{_sysconfdir}/udev/rules.d/99-rhel-rt.rules
%config(noreplace) %{_sysconfdir}/sysconfig/realtime-setup
%{_bindir}/slub_cpu_partial_off
%{_bindir}/realtime-entsk
%{_bindir}/kernel-is-rt
%{_unitdir}/realtime-setup.service
%{_bindir}/realtime-setup
%{_unitdir}/realtime-entsk.service

%changelog
* Wed Jan 29 2025 Clark Williams <williams@redhat.com> - 2.5-5
- Move realtime-entsk and kernel-is-rt to /usr/bin

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Clark Williams <williams@redhat.com> - 2.5-3
- remove runtime Require of kexec-tools

* Wed Jul 31 2024 Clark Williams <williams@redhat.com> - 2.5-2
- fix date typo in changelog

* Wed Jul 31 2024 Clark Williams <williams@redhat.com> - 2.5-1
- Add anocheck hardening flags
- version bump

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 05 2023 Clark Williams <williams@redhat.com> - 2.4-1
- Makefile cleanups and added .gitignore
- remove Red Hat Makefile targets and specfile
- ensure all files have valid SPDX license identifiers
- version bump

* Thu Jul 27 2023 Clark Williams <williams@redhat.com> - 2.3.2-1
- Remove rpm specific logic from Makefile
- Remove unused SysVinit script
- version bump

* Wed Jul 05 2023 Clark Williams <williams@redhat.com> - 2.3.1-1
- Fix build require of annobin package
- Update all files with SPDX identifier
- add srpm target in Makefile
- fix versioning in Makefile targets and specfile

* Thu Jul 14 2022 Jiri Kastner<jkastner@fedoraproject.org> - 2.2.3-1
- polish source url

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Clark Williams <williams@redhat.com> - 2.2-3
- pidfile error from renaming. Resolves rhbz##1891048

* Thu May 20 2021 Clark Williams <williams@redhat.com> - 2.2-2
- Cgroupv2 fix.  Resolves rhbz#1891048

* Wed May 19 2021 Clark Williams <williams@redhat.com> - 2.2-1
- Fix realtime-entsk.service using wrong image. Resolves rhbz#1891048

* Fri May 14 2021 Clark Williams <williams@redhat.com> - 2.1-4
- Sync RHEL 9 and Fedora versions

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.1-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Mar 27 2019 Clark Williams <williams@redhat.com> 2.1.1
- build for RHEL 8.1.0
- added OSCI gating test framework
Resolves: rhbz#1682427

* Tue Oct 23 2018 Clark Williams <williams@redhat.com> 2.0.10
- rebuild to see if build-id continues to appear in the rpm

* Mon Sep 24 2018 Clark Williams <williams@redhat.com> 2.0.9
- fix annocheck static source analysis errors
Resolves: rhbz#1619407

* Fri Sep 14 2018 Clark Williams <williams@redhat.com> 2.0.8
- fix some coverity complaints about shell scripts
Resolves: rhbz#1619407

* Fri Sep 14 2018 Clark Williams <williams@redhat.com> 2.0.7
- strip rt-entsk executable on installation
Resolves: rhbz#1619407

* Fri Aug 24 2018 Clark Williams <williams@redhat.com> 2.0.6
- check for open failure to make coverity happy
Resolves: rhbz#1619407

* Fri Aug 24 2018 Clark Williams <williams@redhat.com> 2.0.5
- move pidfile write to after daemonize in rt-entsk
Resolves: rhbz#1619407

* Wed Aug 22 2018 Clark Williams <williams@redhat.com> 2.0.4
- add logic to write a pid file in rt-entsk (keep systemd happy)
Resolves: rhbz#1619407

* Wed Aug 22 2018 Clark Williams <williams@redhat.com> 2.0.3
- sync with rhel-7.6 build
Resolves: rhbz#1619407

* Wed Aug 22 2018 Clark Williams <williams@redhat.com> 2.0.2
- fix installation of rt-entsk
Resolves: rhbz#1619407

* Mon Aug 20 2018 Clark Williams <williams@redhat.com> 2.0.1
- build for RHEL 8.0.0
- add rt-entsk program for forcing network timestamps enabled
Resolves: rhbz#1619407

* Wed Aug 08 2018 Clark Williams <williams@redhat.com> 1.59-8
- remove libcgroup requirement
- remove comment about irqbalance

* Fri Jun 01 2018 Luis Claudio R. Goncalves <lgoncalv@redhat.com> 1.59-7
- rt-setup no longer rrequires rtctl (1585198)
Resolves: rhbz#1585198

* Tue Jul 05 2016 John Kacur <jkacur@redhat.com> - 1.59-5
- Rebuild for rhel-7.3
Resolves: rhbz#1341783

* Tue Jun 14 2016 John Kacur <jkacur@redhat.com> - 1.59-3
- Fix some spelling mistakes in the comments in rhel-rt.rules
- Add udev rules to allow the realtime group to access msr and cpuid registers
Resolves: rhbz#1341783

* Fri Jul 10 2015 Clark Williams <williams@redhat.com> - 1.59-2
- removed post-install script that disables irqbalance (1203764)
- fixed typo in requires for tuned-profiles-realtime (1241936)

* Thu Jul  2 2015 Clark Williams <williams@redhat.com> - 1.59-1
- added tuned and tuna dependencies, removed sqlite  (1203764)

* Mon Dec 29 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.58-2
- fixed rt-setup shell script called on startup (1162769)
- removed the unnecessary mrg-rt-firmware logic (1162769)

* Fri Dec 26 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.58-1
- make startup logic work with systemd (1162769)
- product name cleanup (1173312)

* Fri Nov 28 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.57-6
- remove a reference to mrg-rt-release from initscript (1162766)

* Mon Nov 24 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.57-5
- move kernel-is-rt from /sbin to /usr/sbin (1151563)

* Tue Nov 18 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.57-4
- remove the database used by mrg-rt-release (1162766)

* Tue Nov 11 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.57-3
- remove mrg-rt-release (1162766)

* Tue Nov 04 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.57-2
- remove the old dracut rules from RHEL6 (1160440)

* Wed Oct 29 2014 Clark Williams <williams@redhat.com> - 1.57-1
- added mrg-2.5.8 release to mrg-rt-release database

* Tue Sep 30 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.56-2
- added mrg-2.5.7 release to mrg-rt-release database

* Wed Aug 20 2014 Clark Williams <williams@redhat.com> - 1.56-1
- added mrg-2.5.6 release to mrg-rt-release database
- removed dracut rule that caused problems when adding firmware to initramfs

* Fri Jul 25 2014 Clark Williams <williams@redhat.com> - 1.55-8
- added mrg-2.5.2 and mrg-2.5.4 releases to mrg-rt-release database

* Tue Jun 10 2014 John Kacur <jkacur@redhat.com> - 1.55-7
- udev: Add udev rule to give group realtime write access to cpu_dma_latency

* Mon Apr 28 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.55-6
- Added mrg-2.5 GA data to the mrg-rt-release database

* Wed Apr 09 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.55-5
- Added mrg-2.4.6 data to the mrg-rt-release database

* Fri Mar 28 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.55-4
- Trim the kernel version when read from uname -rt

* Tue Feb 18 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.55-3
- Added mrg-2.4.5 data to the mrg-rt-release database

* Wed Jan 22 2014 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.55-2
- Added mrg-2.4.3 data to the mrg-rt-release database

* Tue Dec 10 2013 Clark Williams <williams@redhat.com> - 1.55-1
- First common build for RHEL7 and RHEL6

* Thu Nov 28 2013 Luis Claudio R. Goncalves <lgoncalv@redhat.com> 1.54-2
- Enhanced update-mrg-rt-release

* Thu Nov 28 2013 Luis Claudio R. Goncalves <lgoncalv@redhat.com> 1.54-1
- Update mrg-rt-release on every boot [848433]

* Thu Aug 29 2013 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.53-4
- add /lib/firmware/$(uname -r) to dracut firmware search path (998920)
- ensure rt-firmware files are on udev firmware search path (998920)

* Thu Aug 22 2013 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.53-3
- removed the dracut config file

* Tue Aug 20 2013 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.53-2
- added configuration file for dracut (998920)
- fixed macro usage on the specfile

* Thu Apr  25 2013 Clark Williams <williams@redhat.com> - 1.53-1
- turn off cgroup mounting logic
- added Requires for libcgroup

* Tue Apr   2 2013 Clark Williams <williams@redhat.com> - 1.52-1
- added script slub_cpu_partial_off
- added cgroups to /etc/sysconfig/rt-setup

* Wed Mar  27 2013 Clark Williams <williams@redhat.com> - 1.51-1
- added code to turn off SLUB cpu_partial at startup

* Mon Nov  12 2012 Luis Claudio R. Goncalves  <lgoncalv@redhat.com> - 1.50-1
- rt-setup-kdump: use mrg-2.x as the kdump kernel [868446] [868442] [868329]
- rt-setup-kdump: simplified the script and added --rhel option

* Tue Mar   6 2012 Clark Williams <williams@redhat.com> - 1.11-1
- removed %%post logic that disables bandwidth limiting [BZ# 791371]
- changed rtprio from 100 to 99 in realtime.conf

* Thu Oct  13 2011 Clark Williams <williams@redhat.com> - 1.10-1
- fixed thinko by removing firmware download logic

* Tue Oct  11 2011 Clark Williams <williams@redhat.com> - 1.9-1
- added sysconfig and init script for handling cgroup mounting
- changed script kernel-is-rt to use /sys/kernel/realtime

* Wed May 11 2011 Clark Williams <williams@redhat.com> - 1.8-1
- simplified mrg-rt-firmware.rules to fix boot time hang on
  large core machines (BZ# 698481)

* Fri Feb 11 2011 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.7-4
- Normalized the RHEL6 firmware path search (due to uname -r changes)

* Thu May 27 2010 John Kacur <jkacur@redhat.com> - 1.7-2
- set kernel.hung_task_panic=0 (off) by default
- set kernel.hung_task_timeout_secs=600 by default
- used sysctl to set sched_rt_runtime_us at install time, not just boot time

* Tue May 18 2010 Clark Williams <williams@redhat.com> - 1.7-1
- removed requirement for kernel-rt (circular dependency)
- cleaned up mrg-rt-firmware.rules (added commas between all key/value pairs)

* Wed Nov 25 2009 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.6-3
- rt-setup-kdump: configure kdump on all MRG kernel flavors
- rt-setup-kdump: fix a log entry that was too verbose

* Wed Nov 25 2009 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.6-2
- rt-setup-kdump treats MRG v1 and v2 kernels accordingly (BZ# 517529)

* Mon Nov  2 2009 Clark Williams <williams@redhat.com> - 1.6-1
- removed "@16" specifier from rt-setup-kdump script (BZ# 517529)

* Tue Sep  1 2009 Clark Williams <williams@redhat.com> - 1.5-2
- fixed path mismatches reported by Vernon Maury

* Wed Aug 26 2009 Clark Williams <williams@redhat.com> - 1.5-1
- add udev rules and scripts for handling driver firmware download

* Thu Jul  9 2009 Clark Williams <williams@redhat.com> - 1.4-1
- blow away rtctl udev rule (compatibility problem with RHEL
  version of udev)
- update /dev/rtc udev rule to use PROGRAM rather than SYMLINK

* Tue Jul  7 2009 Clark Williams <williams@redhat.com> - 1.3-1
- added udev rules file to address:
 - BZ 510121 hwclock & /dev/rtc broken in rt-kernel
 - BZ 466929 udev rule for hotplug rtctl

* Thu May 21 2009 Clark Williams <williams@redhat.com> - 1.2-1
- added post section to edit /etc/sysctl.conf and add the
  kernel.sched_rt_runtime_us parameter = -1 line to disable
  the RT scheduler bandwith limiter

* Tue Jul 15 2008 Clark Williams <williams@redhat.com> - 1.1-6
- fixed rt-setup-kdump to handle incorrect arguments (BZ 455536)
- added help argument to rt-setup-kdump

* Fri Jun 13 2008 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.1-5
- rt-setup-kdump now touches /etc/grub.conf only when requested

* Tue Jun 03 2008 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.1-4
- /usr/bin/rt-setup-kdump had wrong permissions
- changed rt-setup-kdump: added a few tests for reserved memory and for the
  absence of /etc/sysconfig/kdump
- now rt-setup requires kexec-tools

* Mon May 12 2008 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.1-3
- disables irqbalance as it may hurt determinism in RT
- installs rt-setup-kdump in /usr/bin

* Tue Apr 22 2008 Clark Williams <williams@redhat.com> - 1.1-2
- removed sed script to edit kdump config file (using updated
  kexec-tools instead)

* Mon Apr 21 2008 Clark Williams <williams@redhat.com> - 1.1-1
- removed --args-linux from /etc/sysconfig/kdump (BZ# 432378)
- changed BuildArch to noarch

* Thu Feb 07 2008 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.0-3
- BZ:399591 - Fixed spec issues pointed by Jeremy Katz
- BZ:399591 - @realtime has gid=71.
- FIXES: BZ399591

* Thu Aug 02 2007 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.0-2
- Fixed package description

* Mon Jul 30 2007 Luis Claudio R. Goncalves <lgoncalv@redhat.com> - 1.0-1
- Initial packaging
- Requires all the basic packages for RT
- Requires support for limits.d and no realtime.conf present in PAM package
