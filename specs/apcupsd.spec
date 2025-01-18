# A change in RPM 4.15 causes the make_build macro to misbuild this package.
# See https://github.com/rpm-software-management/rpm/issues/798
%global _make_verbose %nil

Name:       apcupsd
Version:    3.14.14
Release:    34%{?dist}
Summary:    APC UPS Power Control Daemon

License:    GPL-2.0-only
URL:        http://www.apcupsd.com
Source0:    https://downloads.sourceforge.net/apcupsd/apcupsd-%version.tar.gz
Source1:    apcupsd.service
Source2:    apcupsd_shutdown
Source3:    apcupsd-httpd.conf
Source4:    apcupsd.logrotate
Source5:    apcupsd64x64.png

# fix crash in gui, rhbz#578276
Patch0:       apcupsd-3.14.9-fixgui.patch
# Halt without powering off, rhbz#1442577
Patch1:       apcupsd-3.14.4-shutdown.patch
# Fix format-security error so we can enable the checks
Patch2:       patch-format-security
Patch3:       disable_nologin.patch


BuildRequires: gcc-c++
BuildRequires: glibc-devel, gd-devel
%if %{defined fedora}
BuildRequires: libusb-compat-0.1-devel
%endif
%if (%{defined rhel} && 0%{?rhel} <= 9)
BuildRequires: libusb-devel
%endif
BuildRequires: net-snmp-devel, 
BuildRequires: gtk2-devel, GConf2-devel, desktop-file-utils
# /sbin/shutdown is required to be present when building
# Somehow in F36 systemd is installed in mock but not in koji
BuildRequires: systemd
# This is part of util-linux in Fedora, but on EL7 it's in sysvinit-tools.
BuildRequires: /usr/bin/wall
BuildRequires: make
Requires:      /bin/mail /usr/bin/wall
%{?systemd_requires}

%description
Apcupsd can be used for controlling most APC UPSes. During a
power failure, apcupsd will inform the users about the power
failure and that a shutdown may occur.  If power is not restored,
a system shutdown will follow when the battery is exausted, a
timeout (seconds) expires, or the battery runtime expires based
on internal APC calculations determined by power consumption
rates.  If the power is restored before one of the above shutdown
conditions is met, apcupsd will inform users about this fact.
Some features depend on what UPS model you have (simple or smart).


%package cgi
Summary:      Web interface for apcupsd
Requires:     apcupsd = %version-%release
Requires:     httpd

%description cgi
A CGI interface to the APC UPS monitoring daemon.


%package gui
Summary:      GUI interface for apcupsd
Requires:     apcupsd = %version-%release

%description gui
A GUI interface to the APC UPS monitoring daemon.


%prep
%autosetup -p1

# Override the provided platform makefile
printf 'install:\n\techo skipped\n' > platforms/redhat/Makefile

%build
%configure \
        --sysconfdir="/etc/apcupsd" \
        --with-cgi-bin="/var/www/apcupsd" \
        --sbindir=/sbin \
        --enable-cgi \
        --enable-pthreads \
        --enable-net \
        --enable-apcsmart \
        --enable-dumb \
        --enable-net-snmp \
        --enable-snmp \
        --enable-usb \
        --enable-modbus-usb \
        --enable-gapcmon \
        --enable-pcnet \
        --with-serial-dev= \
        --with-upstype=usb \
        --with-upscable=usb \
        --with-lock-dir=/var/lock \
        APCUPSD_MAIL=/bin/mail
%make_build

%install
mkdir -p %buildroot/var/www/apcupsd
%make_install
install -m744 platforms/apccontrol \
              %buildroot/etc/apcupsd/apccontrol

install -p -D -m0644 %SOURCE1 %buildroot/lib/systemd/system/apcupsd.service
install -p -D -m0755 %SOURCE2 %buildroot/lib/systemd/system-shutdown/apcupsd_shutdown
install -p -D -m0644 %SOURCE3 %buildroot/etc/httpd/conf.d/apcupsd.conf
install -p -D -m0644 %SOURCE4 %buildroot/etc/logrotate.d/apcupsd
install -p -D -m0644 %SOURCE5 %buildroot/usr/share/pixmaps/apcupsd64x64.png

desktop-file-install \
        --vendor="fedora" \
        --dir=%buildroot/usr/share/applications \
        --set-icon=apcupsd64x64 \
        --delete-original \
        %buildroot/usr/share/applications/gapcmon.desktop

# Cleanup for later %%doc processing
chmod -x examples/*.c
rm examples/*.in

%files
%license COPYING
%doc ChangeLog examples ReleaseNotes
%dir /etc/apcupsd
/lib/systemd/system/apcupsd.service
/lib/systemd/system-shutdown/apcupsd_shutdown
%config(noreplace) /etc/apcupsd/apcupsd.conf
%attr(0755,root,root) /etc/apcupsd/apccontrol
%config(noreplace) /etc/apcupsd/changeme
%config(noreplace) /etc/apcupsd/commfailure
%config(noreplace) /etc/apcupsd/commok
%config(noreplace) /etc/apcupsd/offbattery
%config(noreplace) /etc/apcupsd/onbattery
%config(noreplace) /etc/logrotate.d/apcupsd
/usr/share/hal/fdi/policy/20thirdparty/80-apcupsd-ups-policy.fdi
%attr(0755,root,root) /sbin/*
%{_mandir}/*/*

%files cgi
%config(noreplace) /etc/apcupsd/apcupsd.css
%config(noreplace) /etc/httpd/conf.d/apcupsd.conf
%config(noreplace) /etc/apcupsd/hosts.conf
%config(noreplace) /etc/apcupsd/multimon.conf
/var/www/apcupsd/

%files gui
/usr/bin/gapcmon
/usr/share/applications/*gapcmon.desktop
/usr/share/pixmaps/apcupsd.png
/usr/share/pixmaps/apcupsd64x64.png
/usr/share/pixmaps/charging.png
/usr/share/pixmaps/gapc_prefs.png
/usr/share/pixmaps/onbatt.png
/usr/share/pixmaps/online.png
/usr/share/pixmaps/unplugged.png


%post
%systemd_post apcupsd.service

%preun
%systemd_preun apcupsd.service

%postun
%systemd_postun_with_restart apcupsd.service


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 08 2024 Germano Massullo <germano.massullo@gmail.com> - 3.14.14-33
- Adds distinction between Fedora and EL <= 9 for BuildRequires: libusb

* Fri Nov 08 2024 Germano Massullo <germano.massullo@gmail.com> - 3.14.14-32
- release bump

* Fri Nov 08 2024 Germano Massullo <germano.massullo@gmail.com> - 3.14.14-31
- Adds disable_nologin.patch

* Sun Jan 07 2024 Germano Massullo <germano.massullo@gmail.com> - 3.14.14-30
- disables apcupsd-3.14.4-shutdown.patch

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 Jason L Tibbitts III <j@tib.bs> - 3.14.14-27
- Depend on libusb-compat-0.1-devel to avoid build breakage.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jan 25 2022 Jason L Tibbitts III <j@tib.bs> - 3.14.14-25
- Explicitly require systemd at build time to ensure that /sbin/shutdown is
  present.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jan 30 2021 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.14.14-22
- Fix build on F33+.
- Allow build with format-security checking enabled.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Germano Massullo <germano.massullo@gmail.com> - 3.14.14-18
- Replaced BuildRequires: gnome-vfs2 with BuildRequires: GConf2-devel More infos at https://bugzilla.redhat.com/show_bug.cgi?id=1745727#c5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.14.14-16
- Workaround change in RPM 4.15 which breaks the build.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.14.14-13
- Fix broken zero-size icon.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.14.14-11
- Add KillMode=process to the systemd unit.

* Mon Mar 26 2018 Till Maas <opensource@till.name> - 3.14.14-10
- rebuilt to drop tcp_wrappers dependency
  https://bugzilla.redhat.com/show_bug.cgi?id=1518751
- remove tcp_wrappers support

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.14.14-8
- Use proper systemd dependencies.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.14.14-5
- Reinstate patch to call shutdown with -H to halt instead of powering down.

* Fri Mar 24 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.14.14-4
- Depend on /usr/bin/wall to accommodate EL7.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 22 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.14.14-2
- Clean up the spec a bit.
- Stop adding the unit file and shutdown script in a patch and just included
  them as sources instead.
- Have the unit go after network-online.target instead of network.target.
- Remove apcupsd-3.14.4-shutdown.patch.  Both the old and the new commands to
  exactly the same thing for me (halt but not power down) on my test machines.

* Thu Jun 02 2016 Michal Hlavinka <mhlavink@redhat.com> - 3.14.14-1
- updated to 3.14.14

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Michal Hlavinka <mhlavink@redhat.com> - 3.14.13-4
- fix apcaccess crash if apcupsd is not running (#1236367,#1197383)
- enabled modbus-usb (#1195071)
- add bigger icon (#1157532)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.14.13-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 03 2015 Michal Hlavinka <mhlavink@redhat.com> - 3.14.13-1
- apcupsd updated to 3.14.13

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Michal Hlavinka <mhlavink@redhat.com> - 3.14.12-1
- apcupsd updated to 3.14.12
- force lock dir to /var/lock (#1064099)

* Mon Feb 17 2014 Michal Hlavinka <mhlavink@redhat.com> - 3.14.11-1
- apcupsd updated to 3.14.11

* Tue Jan 21 2014 Michal Hlavinka <mhlavink@redhat.com> - 3.14.10-14
- reduce amount of debug messages (#1053324)

* Wed Aug 14 2013 Michal Hlavinka <mhlavink@redhat.com> - 3.14.10-13
- fix aarch64 support (#925007)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 3.14.10-11
- rebuild for new GD 2.1.0

* Fri May 17 2013 Michal Hlavinka <mhlavink@redhat.com> - 3.14.10-10
- make executables hardened (#955341)

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.14.10-9
- Remove --vendor flag to desktop-file-install on F19+

* Tue Feb 05 2013 Michal Hlavinka <mhlavink@redhat.com> - 3.14.10-8
- remove obsolete documentation

* Tue Oct 30 2012 Michal Hlavinka <mhlavink@redhat.com> - 3.14.10-7
- fix configuration for httpd 2.4 (#871361)

* Fri Aug 24 2012 Michal Hlavinka <mhlavink@redhat.com> - 3.14.10-6
- scriptlets replaced with new systemd macros (#851227)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 13 2012 Michal Hlavinka <mhlavink@redhat.com> - 3.14.10-4
- start after network is up (#789191)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Michal Hlavinka <mhlavink@redhat.com> - 3.14.10-2
- remove powerfail flag on boot (#768684)

* Mon Dec 12 2011 Michal Hlavinka <mhlavink@redhat.com> - 3.14.10-1
- apcupsd updated to 3.14.10
- fix MODEL vs. APCMODEL confusion. Remove APCMODEL and rename old MODEL
  aka 'mode' to DRIVER.

* Thu Oct 20 2011 Michal Hlavinka <mhlavink@redhat.com> - 3.14.9-2
- fix crash in gui (#578276), patch by Michal Sekletar

* Mon Jul 25 2011 Michal Hlavinka <mhlavink@redhat.com> - 3.14.9-1
- apcupsd updated to 3.14.9

* Fri Jul 08 2011 Michal Hlavinka <mhlavink@redhat.com> - 3.14.8-9
- rebuilt for net-snmp update

* Thu Jun 16 2011 Michal Hlavinka <mhlavink@redhat.com> - 3.14.8-8
- move from SysV init script to systemd service file

* Wed Feb 09 2011 Michal Hlavinka <mhlavink@redhat.com> - 3.14.9-7
- add readme file to doc explaining needed configuration of halt script

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Michal Hlavinka <mhlavink@redhat.com> - 3.14.8-5
- do not attempt to invoke directory as a script (#659219)

* Fri Nov 05 2010 Michal Hlavinka <mhlavink@redhat.com> - 3.14.8-4
- rebuilt for library update

* Wed Sep 29 2010 jkeating - 3.14.8-3
- Rebuilt for gcc bug 634757

* Wed Sep 22 2010 Michal Hlavinka <mhlavink@redhat.com> - 3.14.8-2
- fix c++ code linking (FTBFS) (#631288)

* Mon Jan 18 2010 Michal Hlavinka <mhlavink@redhat.com> - 3.14.8-1
- updated to 3.14.8

* Fri Sep 18 2009 Michal Hlavinka <mhlavink@redhat.com> - 3.14.7-3
- fix building with new net-snmp version

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.14.7-2
- rebuilt with new openssl

* Mon Aug 03 2009 Michal Hlavinka <mhlavink@redhat.com> - 3.14.7-1
- updated to 3.14.7

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Michal Hlavinka <mhlavink@redhat.com> - 3.14.6-1
- update to 3.14.6

* Tue Feb 24 2009 Michal Hlavinka <mhlavink@redhat.com> - 3.14.5-3
- fix build with gcc 4.4

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Michal Hlavinka <mhlavink@redhat.com> - 3.14.5-1
- update to 3.14.5

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 3.14.4-3
- rebuild with new openssl

* Fri Jun 06 2008 Tomas Smetana <tsmetana@redhat.com> - 3.14.4-2
- drop useless build requirements
- fix #448637 - hosts.conf and multimon.conf should be in apcupsd-cgi
- move binaries to /sbin (related #346271)

* Wed May 28 2008 Tomas Smetana <tsmetana@redhat.com> - 3.14.4-1
- new upstream version

* Tue Feb 12 2008 Tomas Smetana <tsmetana@redhat.com> - 3.14.3-2.1
- rebuild (gcc-4.3)

* Wed Jan 30 2008 Tomas Smetana <tsmetana@redhat.com> - 3.14.3-2
- fix #348701 - apcupsd control script does not invoke shutdown properly

* Wed Jan 23 2008 Tomas Smetana <tsmetana@redhat.com> - 3.14.3-1
- Update to 3.14.3

* Wed Oct 10 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.14.2-1
- Update to 3.14.2, remove upstreamed patches

* Wed Aug  1 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.14.1-3
- Add patch to close open file descriptors (bug #247162)
- Stop/restart service as needed on removal/upgrade

* Mon Jun 04 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.14.1-2
- Add patch for linux USB UPS detection (bug #245864)

* Tue May 29 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.14.1-1
- Update to 3.14.1

* Mon Apr 23 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.14.0-2
- Fix init script for LSB compliance (bug #237532)

* Mon Feb 12 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.14.0-1
- Update to 3.14.0

* Fri Jan  5 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.13.9-2
- Mark everything in /etc/apcupsd noreplace
- Change BR to tcp_wrappers-devel

* Thu Nov 30 2006 - Orion Poplawski <orion@cora.nwra.com> - 3.13.9-1
- Update to 3.13.9, add gui package

* Mon Oct  9 2006 - Orion Poplawski <orion@cora.nwra.com> - 3.12.4-3
- Fix /etc/httpd/conf.d/apcupsd.conf so DirectoryIndex works (bug #209952).
  Patch from Clive Messer (clive@vacuumtube.org.uk)

* Tue Aug 29 2006 - Orion Poplawski <orion@cora.nwra.com> - 3.12.4-2
- Rebuild for FC6

* Mon Aug 21 2006 - Orion Poplawski <orion@cora.nwra.com> - 3.12.4-1
- Update to 3.12.4

* Tue Jan 10 2006 - Orion Poplawski <orion@cora.nwra.com> - 3.12.2-1
- Update to 3.12.2
- Don't strip binaries

* Tue Jan 10 2006 - Orion Poplawski <orion@cora.nwra.com> - 3.12.1-1
- Update to 3.12.1

* Wed Jan  4 2006 - Orion Poplawski <orion@cora.nwra.com> - 3.12.0-1
- Update to 3.12.0

* Tue Jan  3 2006 - Orion Poplawski <orion@cora.nwra.com> - 3.10.18-7
- Rebuild

* Wed Dec 21 2005 - Orion Poplawski <orion@cora.nwra.com> - 3.10.18-6
- Rebuild

* Wed Nov 16 2005 - Orion Poplawski <orion@cora.nwra.com> - 3.10.18-5
- Bump for new openssl

* Fri Nov  4 2005 - Orion Poplawski <orion@cora.nwra.com> - 3.10.18-4
- Add logrotate script for /var/log/apcupsd.events
- Add apache configuration script and change cgi directory to
  /var/www/apcupsd
- Compile in snmp, net-snmp, powerflute, nls, add tcp_wrappers support

* Mon Oct 17 2005 - Orion Poplawski <orion@cora.nwra.com> - 3.10.18-3
- Removed %%{_smp_mflags} from make, broke builds
- Patch init file to not start automatically and add reload
- Mark css file config
- Require /sbin/chkconfig

* Mon Oct 17 2005 - Orion Poplawski <orion@cora.nwra.com> - 3.10.18-2
- Add %%defattr to -cgi package

* Wed Aug 17 2005 - Orion Poplawski <orion@cora.nwra.com> - 3.10.18-1
- Initial Fedora Version
