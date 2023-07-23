%global        debug_package %{nil}

Summary:       Realtime IRQ thread system tuning
Name:          rtirq
Version:       20130402
Release:       25%{?dist}
License:       GPLv2+
URL:           http://www.rncbc.org/jack/
Source0:       http://www.rncbc.org/jack/%{name}-%{version}.tar.gz
# sources for udev and power management additions
Source1:       rtirq-udev
Source2:       rtirq-udev-rules
Source3:       rtirq-power
# add configuration option for a minimum priority in rtirq script
Patch0:        rtirq-minprio.patch
# patch to add udev options to rtirq configuration
Patch1:        rtirq-udevprio.patch
BuildArch:     noarch
BuildRequires: perl-interpreter
# For systemd.macros
BuildRequires: systemd
Requires:      systemd

%description
Start-up scripts for tuning the realtime scheduling policy and priority
of relevant IRQ service threads, featured for a realtime-preempt enabled
kernel configuration. 

%prep
%setup -q
%patch1 -p0
# Fix encoding issues
for file in LICENSE; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build

%install
rm -rf %{buildroot}
install -D rtirq.sh   -m 0755 %{buildroot}%{_bindir}/rtirq
install -D rtirq.conf -m 0644 %{buildroot}%{_sysconfdir}/sysconfig/rtirq

# fix order of interrupts, tac was reversing the priority of the soundcards
perl -p -i -e "s/\| tac//g" %{buildroot}%{_bindir}/rtirq

# high priority is 70 instead of 90 (in Fedora 17+)
perl -p -i -e "s|RTIRQ_PRIO_HIGH=90|RTIRQ_PRIO_HIGH=70|g" %{buildroot}%{_sysconfdir}/sysconfig/rtirq
# low priority is 65, 5 above Jack highest priority thread
perl -p -i -e "s|RTIRQ_PRIO_LOW=51|RTIRQ_PRIO_LOW=65|g" %{buildroot}%{_sysconfdir}/sysconfig/rtirq
# priority decrement now 1 instead of 5, no need to leave vacant priorities
perl -p -i -e "s|RTIRQ_PRIO_DECR=5|RTIRQ_PRIO_DECR=1|g" %{buildroot}%{_sysconfdir}/sysconfig/rtirq
# remove usb from list of cards in configuration, this is now handled through udev rules
perl -p -i -e "s|rtc snd usb i8042|rtc snd i8042|g" %{buildroot}%{_sysconfdir}/sysconfig/rtirq
# adjust priority for udev changes, same as highest priority
perl -p -i -e "s|RTIRQ_PRIO_UDEV=85|RTIRQ_PRIO_UDEV=70|g" %{buildroot}%{_sysconfdir}/sysconfig/rtirq
# moved out of init.d/
perl -p -i -e "s|/etc/init.d/|%{_bindir}/|g" rtirq.service

# install udev and power files
install -D %{SOURCE2} -m 0644 %{buildroot}%{_prefix}/lib/udev/rules.d/95-rtirq.rules
install -D %{SOURCE1} -m 0755 %{buildroot}%{_bindir}/rtirq-udev
install -D %{SOURCE3} -m 0755 %{buildroot}%{_sysconfdir}/pm/sleep.d/05-rtirq
install -vD rtirq.service -m 0644 %{buildroot}%{_prefix}/lib/systemd/system/rtirq.service

%post
%systemd_post rtirq.service

%preun
%systemd_preun rtirq.service

%postun
%systemd_postun_with_restart rtirq.service 

%triggerun -- rtirq < 20130402
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply rtirq
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save rtirq >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del rtirq >/dev/null 2>&1 || :
/bin/systemctl try-restart rtirq.service >/dev/null 2>&1 || :

%files
%doc LICENSE
%config(noreplace) %{_sysconfdir}/sysconfig/rtirq
# udev and power management
%{_prefix}/lib/udev/rules.d/95-rtirq.rules
%{_sysconfdir}/pm/sleep.d/05-rtirq
%{_bindir}/rtirq-udev
%{_bindir}/rtirq
%{_prefix}/lib/systemd/system/rtirq.service

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 20130402-20
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Orcan Ogetbil <oget [dot] fedora [at] gmail [dot] com> - 20130402-11
- Added BR: perl

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20130402-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130402-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130402-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 11 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 20130402-6
- Add BR: systemd for systemd.macros (RHBZ #1018052).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130402-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Brendan Jones <brendan.jones.it@gmail.com> 20130402-4
- Correct macro error

* Fri Jun 14 2013 Brendan Jones <brendan.jones.it@gmail.com> 20130402-3?dist}
- Correct changelog

* Wed Jun 12 2013 Brendan Jones <brendan.jones.it@gmail.com> 20130402-2
- Remove sysvinit scripts

* Fri May 24 2013 Brendan Jones <brendan.jones.it@gmail.com> 20130402-1
- Upstream release, add systemd

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120505-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Brendan Jones <brendan.jones.it@gmail.com> 20120505-5
- Add LICENSE file

* Tue Jul 24 2012 Brendan Jones <brendan.jones.it@gmail.com> 20120505-4
- Update udev lib macro

* Tue Jul 24 2012 Brendan Jones <brendan.jones.it@gmail.com> 20120505-3
- Move udev rules to /usr/lib/udev

* Thu Jul 12 2012 Brendan Jones <brendan.jones.it@gmail.com> 20120505-2
- initial SPEC changes for use in Fedora

* Tue May 29 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20120505-1
- udpate to 20120505
- add rtirq patch for minimum priority (nando@ccrma)
- tweak priorities for new Fedora allowed rt priorities (max priority for
  jack users is 70 in fc17+, jackd priority is 60)
- add udev rule, power management rule, udev script and patch to add udev
  and default priorities to rtirq configuration file (nando@ccrma)
- tweak udev priority to be the max priority

* Fri May  4 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20120504-2
- update to 20120504, proper handling of pci soundcards on 3.2.x
- add patch to fix handling of soundcards on 3.2

* Fri Oct  7 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20111007-1
- update to 20111007, has better logic for shared interrupts

* Tue May 31 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20090920-1
- changed schedutils requirement to /usr/bin/chrt, fc15 no longer has it

* Mon Oct 26 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20090920-1
- updated to latest version that works with 2.6.31.* rt kernels

* Thu Jan 11 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20070101-1
- updated to 20070101, works with latest versions of the realtime
  preempt patch
- fix order of interrupts (was reversing the priority of the soundcards)

* Tue Aug 29 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20060819-1
- updated to 20060819 (fixes errors on PREEMPT_DESKTOP kernels)

* Wed Apr  5 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20060218-1
- updated to 20060218

* Mon Jun 20 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20050620-1
- updated to 20050620

* Thu Apr 14 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20050414-1
- Rui added support for unthreading rtc and snd interrupts

* Fri Apr  8 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20050408-1
- small fixes from Rui, new tarball

* Wed Apr  6 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20050407-1
- new tarball from Rui with dup irqs fix incorporated

* Wed Apr  6 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20050406-1
- updated to new tarball
- added patch to avoid irq's used by several devices to end up lower
  in priority, helps maintain the soundcard at the proper irq priority
- changed default high priority
- with both changes the soundcard priority should be 70...63

* Mon Mar 21 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20041118-2
- start rtirq after alsasound, add post script to check priority
  and readd rtirq if needed

* Thu Dec 23 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 20041118-1
- initial Planet CCRMA build
- do not rearrange interrupts on package install, seems safer to me,
  of course if there are problems this merely delays them till the 
  next reboot or when the user executes the script :-)

* Fri Nov 12 2004 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Bumped to 20041112 version.

* Mon Nov 8 2004 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Update for the new 20041108 version.

* Thu Nov 4 2004 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Created initial rtirq.spec

