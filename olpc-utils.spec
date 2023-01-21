Name:       olpc-utils
Version:    6.0.6
Release:    10%{?dist}
Summary:    OLPC utilities
URL:        http://wiki.laptop.org/go/Olpc-utils
License:    GPLv2+
Source0:    http://dev.laptop.org/pub/source/%{name}/%{name}-%{version}.tar.bz2
ExclusiveArch: %{ix86} %{arm}

BuildRequires: make
BuildRequires: gcc
BuildRequires: systemd
Requires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# for olpc-dm
BuildRequires: pam-devel
Requires: xorg-x11-xauth

# for olpc-configure
Requires: findutils, hostname, kbd

# for modprobe.d
Requires: kmod

# for SiSUSB2VGA support
Requires: xorg-x11-drv-sisusb

# for pm-utils hook
Requires: filesystem

# for /usr/share/X11/xorg.conf.d
Requires: xorg-x11-server-Xorg

# for /lib/udev
Requires: systemd-udev

# for /usr/share/glib-2.0/schemas and glib-compile-schemas
Requires: glib2

%description
Tools for starting an X session, mapping keys on the OLPC keyboards,
becoming root, and cleaning the datastore.

%prep
%setup -q

%build
make -f Makefile.build %{?_smp_mflags} CFLAGS="%{optflags}"


%install
make -f Makefile.build install DESTDIR=%{buildroot}
%ifarch x86_64 s390x %{power64} sparc64 aarch64
# make _libdir happy
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64

# but revert slightly to please _unitdir
mkdir -p %{buildroot}/usr/lib
mv %{buildroot}/usr/lib64/systemd %{buildroot}/usr/lib
%endif

chmod -x %{buildroot}/%{_datadir}/olpc-utils/xorg.conf.d/*.conf
chmod -x %{buildroot}/usr/lib/systemd/system/*.service
rm %{buildroot}/%{_datadir}/glib-2.0/schemas/olpc.gschema.override
rm %{buildroot}/%{_bindir}/olpc-test-devkey %{buildroot}/%{_bindir}/olpc-audit %{buildroot}/%{_bindir}/olpc-fsp-fwread

%post
rm -f /.olpc-configured # force re-configuration on upgrade
%systemd_post olpc-dm.service
%systemd_post olpc-configure.service
%systemd_post olpc-boot-finish.service
%systemd_post plymouth-shutdown-wait.service


%preun
%systemd_preun olpc-dm.service
%systemd_preun olpc-configure.service
%systemd_preun olpc-boot-finish.service
%systemd_preun plymouth-shutdown-wait.service


%postun
%systemd_postun olpc-dm.service
%systemd_postun olpc-configure.service
%systemd_postun olpc-boot-finish.service
%systemd_postun plymouth-shutdown-wait.service

%files
%license COPYING
%{_sbindir}/*
%{_bindir}/olpc-logbat
%{_bindir}/olpc-session
%{_bindir}/olpc-pwr-log
%{_bindir}/olpc-solar-log
%{_bindir}/olpc-hwinfo
%{_bindir}/olpc-batcap
%{_bindir}/olpc-fsp-regs
%{_bindir}/olpc-panelpwr-log
%{_unitdir}/*
%{_datadir}/olpc-utils
# %{_datadir}/glib-2.0/schemas/*
%{_datadir}/X11/xorg.conf.d/*
%{_libdir}/pm-utils/sleep.d/00xo
/usr/lib/systemd/system-sleep/*
/lib/udev/device-tree-val
/lib/udev/hwdb.d/96-olpc-keyboard.hwdb
/lib/udev/olpc*
/lib/udev/rules.d/*
%{_sysconfdir}/profile.d/zzz_olpc.sh
%config(noreplace) %{_sysconfdir}/motd.olpc
%config(noreplace) %{_sysconfdir}/skel/.xsession-example
%config(noreplace) %{_sysconfdir}/skel/.config/autostart/imsettings-start.desktop
%config(noreplace) %{_sysconfdir}/pam.d/olpc-login

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Peter Robinson <pbrobinson@fedoraproject.org> 6.0.6-3
- Drop components that are not currently relevent

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Peter Robinson <pbrobinson@fedoraproject.org> 6.0.6-1
- Update to 6.0.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 5.0.0-9
- Add ExclusiveArch, cleanups

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 5.0.0-7
- Add aarch64 to list of /usr/lib64 ones
- Fixed dates in changelog

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Sep 07 2014 Karsten Hopp <karsten@redhat.com> 5.0.0-5
- fix libdir on ppc64p7 and ppc64le

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Daniel Drake <dsd@laptop.org> - 5.0.0-1
- Drop library support (Sugar handles it), fix X launching in rawhide

* Thu May 23 2013 Daniel Drake <dsd@laptop.org> - 4.0.4-1
- Add systemd suspend hook

* Mon May 13 2013 Daniel Drake <dsd@laptop.org> - 4.0.3-3
- Fix galcore access on XO-4

* Wed Apr 24 2013 Daniel Drake <dsd@laptop.org> - 4.0.2-2
- ion/vmeta support for XO-4

* Mon Apr  1 2013 Daniel Drake <dsd@laptop.org> - 4.0.1-1
- Fix setting environment from PAM

* Thu Mar 21 2013 Daniel Drake <dsd@laptop.org> - 4.0.0-1
- Latest version with cleaner olpc-configure, now safe for non-XO hardware.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 30 2013 Daniel Drake <dsd@laptop.org> - 3.0.7-1
- Enable accelerated graphics on XO-4

* Sun Nov 18 2012 Daniel Drake <dsd@laptop.org> - 3.0.6-1
- Update olpc-dev-kernel for new zip file names

* Tue Oct 30 2012 Daniel Drake <dsd@laptop.org> - 3.0.5-1
- Update for systemd-195

* Tue Oct  9 2012 Daniel Drake <dsd@laptop.org> - 3.0.4-1
- Restore GNOME desktop, activate on-screen keyboard

* Wed Sep 12 2012 Daniel Drake <dsd@laptop.org> - 3.0.3-1
- /bootpart behaviour change, support overriding language/keyboard defaults

* Mon Sep 10 2012 Daniel Drake <dsd@laptop.org> - 3.0.2-2
- Add missing Requires on hostname

* Mon Sep 10 2012 Daniel Drake <dsd@laptop.org> - 3.0.2-1
- Add olpc-dev-kernel utility

* Mon Sep 10 2012 Daniel Drake <dsd@laptop.org> - 3.0.1-1
- New version, includes various fixes for F18, XO4 and keyboards

* Mon Aug 20 2012 Daniel Drake <dsd@laptop.org> - 3.0.0-1
- Update for DisplayManagerRework

* Sat Aug 18 2012 Martin Langhoff <martin@.laptop.org> - 2.0.19-1
- Add initial XO-4 support, future proof XO-1.75 board detection

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Martin Langhoff <martin@laptop.org> - 2.0.18-1
- Fix detection of XO-1.5 motherboards (dlo#12003)

* Fri Jun 29 2012 Daniel Drake <dsd@laptop.org> - 2.0.17-1
- Another networking naming fix

* Thu Jun 28 2012 Daniel Drake <dsd@laptop.org> - 2.0.16-1
- Fix network naming rules being executed twice

* Mon Jun 18 2012 Daniel Drake <dsd@laptop.org> - 2.0.15-1
- Enable 3rd mouse button emulation in GNOME

* Thu Jun 14 2012 Daniel Drake <dsd@laptop.org> - 2.0.14-1
- Set vmeta device permissions on XO-1.75

* Fri Jun  1 2012 Daniel Drake <dsd@laptop.org> - 2.0.13-1
- Enable RenderAccel on XO-1.75

* Thu May 31 2012 Daniel Drake <dsd@laptop.org> - 2.0.12-1
- Fix for sisusb configuration
- Allow access to butia robot devices
- Delay shutdown after showing splash to give the user time to see it

* Wed May 16 2012 Daniel Drake <dsd@laptop.org> - 2.0.11-1
- Fixes for X and suond configuration and upgrade path from pre-F17

* Mon May  7 2012 Daniel Drake <dsd@laptop.org> - 2.0.10-1
- Fix mounting of boot partition
- Fix DisplayLink USB VGA support

* Fri Apr 27 2012 Daniel Drake <dsd@laptop.org> - 2.0.9-1
- Fix udev configuration for Lego devices
- Disable media keys in GNOME
- Fix USB VGA

* Wed Apr 18 2012 Daniel Drake <dsd@laptop.org> - 2.0.8-1
- Add log rotation utility
- Wait for network device before reading MAC address

* Tue Apr 10 2012 Daniel Drake <dsd@laptop.org> - 2.0.7-1
- Various font configuration fixes
- Fix XO-1.75 keyboard mapping

* Tue Apr  3 2012 Daniel Drake <dsd@laptop.org> - 2.0.6-1
- XO-1 boot partition mounting fix.
- Grow SD card root filesystem during first boot.

* Mon Mar 26 2012 Daniel Drake <dsd@laptop.org> - 2.0.5-1
- Various bug fixes for mouse, network, XO-1.75 video, etc.

* Mon Mar 19 2012 Daniel Drake <dsd@laptop.org> - 2.0.4-1
- Bug fixes, and interaction with OLPC's plymouth boot animation

* Wed Mar 14 2012 Daniel Drake <dsd@laptop.org> - 2.0.3-1
- olpc-dm: Use PAM instead of ConsoleKit, fixes session management

* Mon Mar  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.2-1
- 2.0.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 23 2011 Karsten Hopp <karsten@redhat.com> 2.0.1-3
- move files from lib to lib64 on all 64bit archs

* Mon Nov 21 2011 Daniel Drake <dsd@laptop.org> - 2.0.1-2
- Add missing dependency on ConsoleKit-x11

* Sat Nov 12 2011 Daniel Drake <dsd@laptop.org> - 2.0.1-1
- Improved mouse setup

* Sat Oct  1 2011 Daniel Drake <dsd@laptop.org> - 2.0.0-1
- Remove outdated bits
- Update for Fedora 16
- Add GNOME 3 gsettings overrides for OLPC

* Fri Sep 30 2011 Daniel Drake <dsd@laptop.org> - 1.3.5-1
- Enable XO-1.75 hardware cursor and screen rotation
- Fix permissions on screen/lockdev runtime directories

* Sun Sep 25 2011 Daniel Drake <dsd@laptop.org> - 1.3.4-1
- Disable XO-1.75 renderaccel to avoid hangs
- Disable tap-to-click and pad scrolling on sentelic driver
- Create runtime directories for screen and lockdev

* Thu Sep 22 2011 Daniel Drake <dsd@laptop.org> - 1.3.3-1
- Latest version, includes various fixes and OLPC XO-1.75 support

* Thu May  5 2011 Daniel Drake <dsd@laptop.org> - 1.2.11-1
- Fix hostname configuration

* Fri Apr 29 2011 Daniel Drake <dsd@laptop.org> - 1.2.10-1
- New version with updated XO-1.5 X config and olpc-configure tweaks

* Wed Apr  6 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.9-2
- Add bitfrost dep for olpc-test-devkey - fixes # 688510

* Thu Mar 17 2011 Daniel Drake <dsd@laptop.org> - 1.2.9-1
- force-disable DPMS to workaround bug in chrome driver
- olpc-dm: disable X TCP port
- another keyboard detection fix

* Sun Mar 13 2011 Daniel Drake <dsd@laptop.org> - 1.2.8-2
- port to systemd

* Tue Mar 08 2011 Daniel Drake <dsd@laptop.org> - 1.2.8-1
- update keyboard detection code
- use symlink for X config
- force-enable XO-1.5 audio capture mixer
- drop MigrationHeuristic workaround for XO-1.5 video

* Tue Feb 22 2011 Daniel Drake <dsd@laptop.org> - 1.2.7-1
- Switch XO-1.5 to chrome video driver

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Daniel Drake <dsd@laptop.org> - 1.2.6-1
- fix stale activity groups file, and fix screen resolution on XO-1.5

* Wed Dec 22 2010 Daniel Drake <dsd@laptop.org> - 1.2.5-1
- Drop Xephyr from sisusb setup, protect ~/Activities in GNOME, create
  default GNOME keyring, sound mixer default tweaks, check and repair bad
  GNOME config, enable xrandr-1.2 rotation

* Wed Dec  1 2010 Daniel Drake <dsd@laptop.org> - 1.2.4-1
- Add upower hook, remove batterymon handling

* Thu Nov 25 2010 Daniel Drake <dsd@laptop.org> - 1.2.3-1
- Fix naming of network devices

* Mon Nov 22 2010 Daniel Drake <dsd@laptop.org> - 1.2.2-1
- Mount boot partition on XO-1, and update to use xorg.conf.d

* Wed Sep 29 2010 jkeating - 1.2.1-2
- Rebuilt for gcc bug 634757

* Mon Sep 13 2010 Daniel Drake <dsd@laptop.org> - 1.2.0-1
- update for systemd
- remove stale X MigrationHeuristic rendering bug workaround

* Thu Aug 26 2010 Daniel Drake <dsd@laptop.org> - 1.0.29-1
- olpc-session: set SUGAR_SCALING for Sugar 0.90

* Thu Aug 19 2010 Daniel Drake <dsd@laptop.org> - 1.0.28-1
- fix olpc-pwr-log on XO-1

* Mon Aug  9 2010 Daniel Drake <dsd@laptop.org> - 1.0.27-1
- new version

* Mon Jul  5 2010 Daniel Drake <dsd@laptop.org> - 1.0.25-2
- fix build

* Mon Jul  5 2010 Daniel Drake <dsd@laptop.org> - 1.0.25-1
- Update to v1.0.25
- Adds support for lego wedo, and fixes mouse configuration for XO-1

* Wed Jun 23 2010 Bernie Innocenti <bernie@codewiz.org> - 1.0.24-1
- Update to 1.0.24

* Sat May 15 2010 Bernie Innocenti <bernie@codewiz.org> - 1.0.23-1
- Update to 1.0.23

* Thu May  6 2010 Daniel Drake <dsd@laptop.org> - 1.0.22-3
- spec fix

* Thu May  6 2010 Daniel Drake <dsd@laptop.org> - 1.0.22-2
- upstart 0.6 patch no longer needed

* Thu May  6 2010 Daniel Drake <dsd@laptop.org> - 1.0.22-1
- update to v1.0.22 for tap-to-click control

* Thu Mar 25 2010 Bernie Innocenti <bernie@codewiz.org> - 1.0.20-1
- Update to 1.0.20
- Remove obsolete olpc-pwr-prof.cron
- Add /etc/udev/rules.d/20-olpc-rfkill.rules

* Thu Jan 28 2010 Bernie Innocenti <bernie@codewiz.org> - 1.0.18-1
- Update to 1.0.18

* Thu Dec 31 2009 Sayamindu Dasgupta <sayamindu@laptop.org> - 1.0.16-1
- Bump to v1.0.16 for disabling imsettings-daemon

* Sun Dec 27 2009 Daniel Drake <dsd@laptop.org> - 1.0.15-1
- Bump to v1.0.15 to enable python optimizations

* Fri Dec 11 2009 Daniel Drake <dsd@laptop.org> - 1.0.14-1
- Bump to v1.0.14 for DDC config

* Wed Dec  9 2009 Bill Nottingham <notting@redhat.com> -  1.0.13-2
- adjust for upstart 0.6

* Fri Dec  4 2009 Daniel Drake <dsd@laptop.org> - 1.0.13-1
- Bump to v1.0.13

* Tue Dec  1 2009 Daniel Drake <dsd@laptop.org> - 1.0.12-1
- Bump to v1.0.12

* Thu Nov 26 2009 Daniel Drake <dsd@laptop.org> - 1.0.11-1
- Bump to v1.0.11

* Thu Nov 19 2009 Daniel Drake <dsd@laptop.org> - 1.0.10-1
- Bump to v1.0.10

* Wed Nov 18 2009 Daniel Drake <dsd@laptop.org> - 1.0.9-1
- Bump to v1.0.9

* Mon Nov 16 2009 Daniel Drake <dsd@laptop.org> - 1.0.8-1
- Bump to v1.0.8

* Thu Nov 12 2009 Daniel Drake <dsd@laptop.org> - 1.0.7-1
- Bump to v1.0.7

* Tue Nov 10 2009 Daniel Drake <dsd@laptop.org> - 1.0.6-1
- Bump to v1.0.6

* Mon Nov  9 2009 Daniel Drake <dsd@laptop.org> - 1.0.5-1
- Bump to v1.0.5

* Thu Nov  5 2009 Daniel Drake <dsd@laptop.org> - 1.0.4-1
- Bump to v1.0.4

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul  6 2009 Daniel Drake <dsd@laptop.org> 1.0.3-1
- Bug fix release

* Mon Jun 29 2009 Daniel Drake <dsd@laptop.org> 1.0.2-1
- Update to latest version, including XO-1.5 support

* Sun Apr 19 2009 Ville Skyttä <ville.skytta at iki.fi> - 0.89-11
- Build with %%{optflags}.

* Thu Feb 26 2009 Adam Jackson <ajax@redhat.com> 0.89-10
- Remove x11-input.fdi, this should all be automatically right already in
  F11 and later, and it breaks synaptics.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.89-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan  2 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.89-8
- Add patch to fix spurious python2.5 Requires (#478661)

* Mon Dec 15 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.89-7
- Fix deps and rebuild

* Fri Dec  5 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.89-6
- Rebuild for Python 2.6 and merge from branch

* Wed Oct  1 2008 Marco Pesenti Gritti <mpg@redhat.com> 0.89-4
- Marco Pesenti Gritti (1):
    Fix typo in the dbus session patch.

* Wed Oct  1 2008 Marco Pesenti Gritti <mpg@redhat.com> 0.89-3
- Marco Pesenti Gritti (1):
    Add missing quotes in the dbus session patch.

* Wed Oct  1 2008 Marco Pesenti Gritti <mpg@redhat.com> 0.89-2
- Marco Pesenti Gritti (1):
    Make olpc-session launch a dbus-session before running sugar.

* Mon Sep 29 2008 Michael Stone <michael@laptop.org> 0.89-1
- Chris Ball (2):
    Require 20 MB of free-space, not 600 MB.
    Properly skip cleanup logic when space is available.

* Mon Sep 29 2008 Michael Stone <michael@laptop.org> 0.88-1
- Chris Ball (1):
    dlo#7932: Fix failsafe script in the presence of pretty-boot.

* Tue Sep 23 2008 Michael Stone <michael@laptop.org> 0.87-1
- Chris Ball (1):
    dlo#7932: Set up utf8 environment, and display a UTF-8 string.

* Tue Sep 02 2008 Michael Stone <michael@laptop.org> 0.86-1
- Guillaume Desmottes (1):
    xsession-example: open Telepathy log files in append mode instead of trunc (#8142)

* Tue Sep 02 2008 Michael Stone <michael@laptop.org> 0.85-1
- Michael Stone (1):
    dlo#7690: Remove the msh0-renaming rule since dlo#5746 was fixed upstream.

* Fri Aug 15 2008 Sayamindu Dasgupta <sayamindu@laptop.org> 0.84-1
- Sayamindu Dasgupta (1):
    dlo#7818: Load the XIM GTK Input Module conditionally.
- Chris Ball (1):
    dlo#7932, dlo#7125: Install disk-space failsafe script.

* Tue Aug 05 2008 Michael Stone <michael@laptop.org> 0.83-1
- C. Scott Ananian (1):
    Trac #5705: fix dbus at_console policy rule.
- Richard Smith (1):
    Update power logging scripts.

* Sat Aug 02 2008 Michael Stone <michael@laptop.org> 0.82-1
- C. Scott Ananian (2):
    dlo#5705: allow specification of the tty used for X on the command line.
    Delint olpc-dm.
- Martin Dengler (1):
    dlo#7442 start olpc-dm on tty3 and no other

* Thu Jul 24 2008 Michael Stone <michael@laptop.org> 0.81-1
- cscott: dlo#317: Set appropriate ICEAUTHORITY, XAUTHORITY, and XSERVERAUTH
  variables to move these to a tmpfs.

* Wed Jul 23 2008 Michael Stone <michael@laptop.org> 0.80-1
- sayamindu: dlo#7474: Choose the XIM method by default.
- pgf: dlo#7537: Be more precise when assigning permissions to /home/olpc.

* Tue Jul 22 2008 Michael Stone <michael@laptop.org> 0.79-1
- cscott: dlo#7495: Trigger activity update on base OS upgrade.

* Tue Jul 08 2008 Michael Stone <michael@laptop.org> 0.78-1
- dsd: dlo#7211: Increase mouse sensitivity.

* Mon Jul 07 2008 Michael Stone <michael@laptop.org> 0.77-1
- Bump revision number.

* Thu Jul 03 2008 C. Scott Ananian <cscott@laptop.org> 0.76-1
- dlo#6432: local installation of RPMs on first boot.
- dlo#7171: move network testing tools to olpc-netutils
- add olpc-test-devkey script to verify a developer key.

* Tue Jun 24 2008 Michael Stone <michael@laptop.org> 0.75-1
- mstone:
    Merge Fedora's divergence.
    Replace autotools with GNUmake.
- erikg: Reduce mouse acceleration.
    dlo#7211: Touchpad is super-sensitive in olpc3 builds.
- dsd/marco: Properly initialize a ConsoleKit session.
    dlo#7266: Can't restart/shutdown system from sugar with olpc3.
    dlo#7289: No USB automount with olpc3.
- ausil:
    include x11-input.fdi
    update xorg-dcon.conf
    (temporarily?) drop our custom sudo implementation.

* Tue May 27 2008 Sayamindu Dasgupta <sayamindu@gmail.com> 0.74-1
- dlo#6945: Added workaround for typo in mfg-data for Ethiopian machines.

* Fri May 16 2008 Michael Stone <michael@laptop.org> - 0.73-1
- dlo#6767: Run make_index.py with a reasonable value of LANG.

* Fri May 16 2008 Sayamindu Dasgupta <sayamindu@gmail.com> - 0.72-1
- dlo#6945: Export GTK_IM_MODULE so that other modules such as Amharic does not get picked up.

* Fri Mar 21 2008 Michael Stone <michael@laptop.org> - 0.71-1
- dlo#5746: Use a more precise udev ignore-me rule for msh* interfaces.

* Sun Mar 02 2008 Michael Stone <michael@laptop.org> - 0.70-1
- Substitute $olpc_usb_version for $olpc_home_version to fix a stupid mistake.

* Sun Mar 02 2008 Michael Stone <michael@laptop.org> - 0.69-1
- Teach olpc-configure about usb customization keys.

* Tue Feb 12 2008 Michael Stone <michael@laptop.org> - 0.68-1
- Import olpc-audit from Marcus
- Import sudo from cscott
- Drop become_root

* Sat Jan 19 2008 Giannis Forgot-to-bump-the-version Galanis <bernie@codewiz.org> - 0.67-1
- Import olpc-netstatus 0.4 from Yanni

* Sat Jan 19 2008 Bernardo Innocenti <bernie@codewiz.org> - 0.66-1
- dlo#5746: Do not try to rename msh0.

* Sat Jan 19 2008 Giannis Galanis <bernie@codewiz.org> - 0.66-1
- dlo#5153: Fix sysfs path to rtap

* Fri Jan 18 2008 Bernardo Innocenti <bernie@codewiz.org> - 0.65-1
- Use GPLv2+ license tag as nothing in this package is GPLv2-only.
- Make preview cleaner robust in the case of a missing datastore
- Do not bother running journal cleaner on fresh installations (saves time on first boot)
- Add a silly TODO list
- Bump revision to 0.65

* Thu Jan 17 2008 Giannis Galanis <bernie@codewiz.org> - 0.65-1
- Import olpc-netlog-0.3 and olpc-netstatus-0.3

* Thu Jan 17 2008 Phil Bordelon <bernie@codewiz.org> - 0.65-1
- Add 'clean-previews' and incorporate it into olpc-configure.

* Mon Jan 14 2008 Michael Stone <michael@laptop.org> - 0.64-1
- 'become_root' script merged upstream.
- Update License field to GPLv2 in order to match the COPYING file.

* Sat Jan 12 2008 Michael Stone <michael@laptop.org> - 0.63-2
- Install a simple 'become_root' script to ease dlo#5537.

* Sat Jan 05 2008 Bernardo Innocenti <bernie@codewiz.org> - 0.63-1
- Rename RPMDIST to DISTVER and DISTVAR to DIST
- dlo#5626: Fix permissions in /home/bernie.

* Thu Jan 03 2008 Bernardo Innocenti <bernie@codewiz.org> - 0.62-1
- Insert extra spacing at the top for cosmetic reasons
- Spacing fixes
- Add missing cron job for olpc-pwr-prof

* Thu Jan 03 2008 Richard Smith <bernie@codewiz.org> - 0.62-1
- Power profile scripts

* Thu Jan 03 2008 Michael Stone <bernie@codewiz.org> - 0.61-1
- Construct Rainbow's spool dir if it doesn't exist - #5033
- Ensure /security has reasonable permissions.

* Wed Jan 02 2008 Bernardo Innocenti <bernie@codewiz.org> - 0.60-1
- Depend on /usr/bin/find
- Remove files in $OLPC_HOME before creating them.
- Add missing dependencies.
- Use /ofw/openprom/model instead of olpc-bios-sig
- Add more missing dependencies
- Remove stray reference to olpc-bios-sig.c.
- Pass absolute paths to rpmbuild
- Add back sbin dirs to unprivileged users PATH
- Invoke rainbow-replay-spool

* Thu Dec 20 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.59-1
- Remove stupid 'exit 0' in zzz_olpc.sh that makes bash *exit* rather than skip the scriptlet
- Depend on tcpdump for olpc-netcapture.

* Sun Dec 16 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.58-1
- Fix version replacement in spec file

* Sun Dec 16 2007 Giannis Galanis <bernie@codewiz.org> - 0.57-1
- Merge olpc-netstatus 0.2
- Merge olpc-netlog 0.2

* Fri Dec 14 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.56-1
- Really bump revision

* Fri Dec 14 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.55-1
- Add a couple of new languages
- Add missing files
- Ensure correct keyboard is loaded even on first boot
- Don't create /root/.i18n as it makes us loose the boot time optimization
- Add code to help us improve boot time

* Fri Dec 07 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.54-1
- Add VMware configuration.
- Fix http://dev.laptop.org/ticket/5320
- Display motd in profile, not through /bin/login

* Mon Dec 03 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.53-1
- Simplyfy setxkb invocation
- Add ASCII art for motd (need more translations)
- More languages for the motd
- Replace fake input driver hack with proper config option.

* Mon Dec 03 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.52-1
- Fix http://dev.laptop.org/ticket/5114
- Simplify test for Geode
- Reindent with TABs to match other init scripts
- Remove check for A-test boards (the following code is harmelss)
- Be a little more verbose on progress.
- Fix https://dev.laptop.org/ticket/5217: Update library index
- Only run checks on start
- Use $OLPC_HOME consistently
- Only run hardware configuration on startup.
- Fix numeric test on empty flag file.
- Bump revision

* Fri Nov 30 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.51-2
- Add olpc-netcapture to %%files

* Fri Nov 30 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.51-1
- Fix olpc#5195: Console font too small when using pretty boot.
- Bump revision

* Fri Nov 30 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.50-1
- Add autoconf check for PAM
- Update spec file
- Merge branch 'master' of ssh://bernie@dev.laptop.org/git/projects/olpc-utils
- Automatically push to origin on bumprev
- Fix bumprev rule
- Bump revision

* Wed Nov 28 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.49-1
- Reorganize variables
- Fix http://dev.laptop.org/ticket/4928
- Fix permissions on /home/olpc
- Bump revision

* Mon Nov 26 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.48-1
- Pacify automake's portability warnings
- Update spec file
- Even more aggressive packaging automation
- Add script to import srpms in Fedora.
- Merge commit 'cscott/master'
- Explicitly strip NUL from mfg tags
- Add cvs-import.sh to EXTRADIST
- Fix https://dev.laptop.org/ticket/4762
- Bump revision

* Mon Nov 26 2007 C. Scott Ananian <bernie@codewiz.org> - 0.47-1
- Separate out configuration done to /home and /.
- Create /home/devkey.html, which can be used to request a developer key.

* Wed Nov 21 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.46-1
- Automate the release process a bit more.
- Approximate XOs DPI on emulators.
- ReTAB.
- Automate specfile generation some more
- Ignore a few more generated files.
- Set i18n settings from the new manufacturing data tags
- Go back to starting sugar with /usr/bin/sugar.
- Bump revision

* Sat Nov 17 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.45-1
- Add bumprev rule
- Merge branch 'master' of ssh://bernie@dev.laptop.org/git/projects/olpc-utils
- Add rule to generate RPM changelog.
- Add support for X 1.3
- Bump revision

* Wed Nov 14 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.44-1
- Don't specify the (olpc) XKB variant esplicitly when not needed
- Fix http://dev.laptop.org/ticket/470
- Bump revision

* Tue Nov 13 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.43-2
- Typo: /etc/skel/.xession-example -> /etc/skel/.xsession-example
- Add "ulimit -c unlimited" example in .xsession-example

* Tue Nov 06 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.43-1
- Reverse check for A-test (bad monkey no bananas)
- Restore i18n, integrate /usr/bin/sugar.
- Disable .tar.gz and bump revision
- Fix check for sugar debug for new scheme.

* Tue Nov 06 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.41-3
- Be more specific in instructions on how to generate tarball
- Install .xession-example in /etc/skel
- REALLY drop obsolete olpc-register

* Mon Nov 05 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.41-2
- Drop obsolete olpc-register

* Mon Nov 05 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.41-1
- Source custom user session last, so they can override everything we did

* Mon Nov 05 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.40-1
- Bump revision to 0.40
- Rename user session to .xsession so it sounds familiar
- Make .i18n owned by user olpc and simplify script
- Fix X config file on qemu (untested)
- Improve override mechanism and make XKB_VARIANT optional
- Simplify by using extended XKB syntax instead of a separate XKB_VARIANT
- Remove now useless nvram code for DCON detection
- Add support for /etc/sysconfig/keyboard

* Sat Nov 03 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.33-1
- Bump revision
- Rename custom user session to ~/.olpcinit to avoid sourcing stale .xinitrc file on updates.
- Delete stray xorg.conf left by old versions of pilgrim.
- Make olpc-configure executable

* Fri Nov 02 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.32-1
- Bump revision to 0.32
- Juggle keyboard and language configuration stuff between olpc-configure
  and olpc-session

* Thu Nov 01 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.31-1
- Bump revision to 0.31
- Make olpc-configure pkgconfig compliant

* Wed Oct 31 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.30-1
- Bump revision to 0.30
- Whitespace cleanup
- Fix compiler warnings
- Add xorg.conf files
- Add olpc-netlog and olpc-netstatus
- Add olpc-session (replaces .xinitrc)
- Add olpc-logbat from Richard Smith
- Add olpc-configure

* Mon Oct 15 2007 Bernardo Innocenti <bernie@codewiz.org> - 0.20-1
- Add olpc-dm
- Switch to automake
- Drop olpc-evdev
- Temporarily disable olpc-register because nobody seems to know what it was for

* Tue Jul 31 2007 Dan Williams <dcbw@redhat.com> - 0.15-1.1
- Add registration utility

* Sat Jun 23 2007 Rahul Sundaram <sundaram@redhat.com> 0.15
- Upstream pull, more spec file cleanup
* Thu Jun 21 2007 Rahul Sundaram <sundaram@redhat.com> 0.11-2
- Spec file cleanup as per review
* Wed Jun 20 2007 Rahul Sundaram <sundaram@redhat.com 0.11-1
- Newer source from J5 which fixes a permission issue. Fix build root cleanup.
* Wed Jun 20 2007 Rahul Sundaram <sundaram@redhat.com 0.10-1
- Newer source and spec cleanups from J5
* Wed Jun 20 2007 Rahul Sundaram <sundaram@redhat.com 0.1-3
- Split off dbench. Added a description for bios signature tool.
* Wed Jun 20 2007 Rahul Sundaram <sundaram@redhat.com> - 0.1-2
- Submit for review in Fedora
* Fri Nov 10 2006 John (J5) Palmieri <johnp@redhat.com> - 0.1-1
- initial package
