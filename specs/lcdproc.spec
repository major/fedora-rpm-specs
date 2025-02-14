%global commit 5c21e8c75fbab53574275c8007f5af746e333144
%global commitdate 20210209
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:        Display real-time system information on a 20x4 back-lit LCD
Name:           lcdproc
Version:        0.5.9
Release:        25.%{commitdate}git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://lcdproc.org
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        lcdproc.service
Source2:        lcdproc.target
Source3:        LCDd.service
Source4:        LCDd-hwdetect.service
Source5:        LCDd-hwdetect.sh
Source6:        90-lcdproc.rules
Source7:        lcdproc.sysusers
Patch1:         0001-server-drivers-g15-Add-support-for-the-LCD-on-Logite.patch
# lcdconf.conf tweaks:
# 1. Enable ProcSize, this is quite useful to have
# 2. Disable TimeDate, its info is duplicate with the MiniClock and it is ugly
# 3. Disable network interface screen by default, since Fedora uses predictable
#    network interface names, having a simple default like Interface0=eth0 does
#    not work
Patch99:        lcdproc-conf.patch

BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
BuildRequires:  doxygen
BuildRequires:  graphviz

BuildRequires:  freetype-devel
%ifnarch s390 s390x
BuildRequires:  libhid-devel
%endif
BuildRequires:  libusb1-devel
BuildRequires:  lirc-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:  xmlto
BuildRequires:  docbook-dtds
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libftdi-devel
BuildRequires:  libg15render-devel
BuildRequires:  mx5000tools-devel
BuildRequires:  libtool autoconf automake
BuildRequires:  gcc make

%{?systemd_requires}



%description
LCDproc is a client/server suite including drivers for all
kinds of nifty LCD displays. The server supports several
serial devices: Matrix Orbital, Crystal Fontz, Bayrad, LB216,
LCDM001 (http://kernelconcepts.de), Wirz-SLI and PIC-an-LCD; and some
devices connected to the LPT port: HD44780, STV5730, T6963,
SED1520 and SED1330. Various clients are available that display
things like CPU load, system load, memory usage, up-time, and a lot more.
See also http://lcdproc.omnipotent.net.


%prep
%autosetup -p1 -n %{name}-%{commit}
# Fixup DriverPath
sed -i -e 's|server/drivers|%{_libdir}/lcdproc|' LCDd.conf
touch -r TODO LCDd.conf


%build
# This package has a configure test which uses ASMs, but does not link the
# resultant .o files.  As such the ASM test is always successful in a LTO
# build.  We can force code generation with the -ffat-lto-objects to make
# the test work as expected.
#
# -ffat-lto-objects is the default for F33, but will not be for F34, so we
# make it explicit here.
%define _lto_cflags -flto=auto -ffat-lto-objects

autoreconf -vif
%configure \
  --sysconfdir=%{_sysconfdir}/%{name} \
  --enable-libusb \
  --enable-drivers=all \
  --enable-lcdproc-menus \
  --enable-stat-nfs \
  --enable-stat-smbfs \
  --with-lcdport=13666 \
  --with-pidfile-dir=/run
%make_build


%install
%make_install INSTALL="install -p"
# remove non useful (and not "lcd" prefixed) perl example scripts
rm $RPM_BUILD_ROOT%{_bindir}/fortune.pl
rm $RPM_BUILD_ROOT%{_bindir}/iosock.pl
rm $RPM_BUILD_ROOT%{_bindir}/tail.pl
rm $RPM_BUILD_ROOT%{_bindir}/x11amp.pl

# docs
make install-html-guides DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/*-guide/*.proc
install -pm 0644 CREDITS.md ChangeLog.md README.md \
  $RPM_BUILD_ROOT%{_docdir}/%{name}

# init
install -d $RPM_BUILD_ROOT%{_unitdir}
install -d $RPM_BUILD_ROOT%{_unitdir}/lcdproc.target.wants
install -d $RPM_BUILD_ROOT%{_udevrulesdir}
install -d $RPM_BUILD_ROOT%{_sysusersdir}
install -pm 0644 %{SOURCE1}  $RPM_BUILD_ROOT%{_unitdir}
install -pm 0644 %{SOURCE2}  $RPM_BUILD_ROOT%{_unitdir}
install -pm 0644 %{SOURCE3}  $RPM_BUILD_ROOT%{_unitdir}
install -pm 0644 %{SOURCE4}  $RPM_BUILD_ROOT%{_unitdir}
install -pm 0755 %{SOURCE5}  $RPM_BUILD_ROOT%{_sbindir}/LCDd-hwdetect
install -pm 0644 %{SOURCE6}  $RPM_BUILD_ROOT%{_udevrulesdir}
install -pm 0644 %{SOURCE7}  $RPM_BUILD_ROOT%{_sysusersdir}/lcdproc.conf
for i in lcdproc.service LCDd.service LCDd-hwdetect.service; do
  ln -s ../$i $RPM_BUILD_ROOT%{_unitdir}/lcdproc.target.wants
done

#Disable default configuration
#Thoses are only provided as an example since ncurses isn't a suitable default configuration.
for f in LCDd.conf lcdproc.conf ; do
  mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/${f} \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/${f}.example
done




%post
%systemd_post LCDd.service lcdproc.service


%preun
%systemd_preun LCDd.service lcdproc.service


%postun
%systemd_postun_with_restart LCDd.service lcdproc.service


%files
%doc %{_docdir}/%{name}
%license COPYING
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/lcdproc/
%{_mandir}/man?/*
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*.conf
%config %{_sysconfdir}/%{name}/*.conf.example
%{_unitdir}/*
%{_udevrulesdir}/90-%{name}.rules
%{_sysusersdir}/lcdproc.conf


%changelog
* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.9-25.20210209git5c21e8c
- Drop call to %sysusers_create_compat

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-24.20210209git5c21e8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.9-23.20210209git5c21e8c
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-22.20210209git5c21e8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-21.20210209git5c21e8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-20.20210209git5c21e8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-19.20210209git5c21e8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-18.20210209git5c21e8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-17.20210209git5c21e8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-16.20210209git5c21e8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-15.20210209git5c21e8c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Hans de Goede <hdegoede@redhat.com> - 0.5.9-14.20210209git5c21e8c
- Sync with latest upstream git
- Add support for LCD found on Logitech Z-10 speakers,
  inc. autodetect by udev + automatic LCDd.conf generation by LCDd-hwdetect
- Fix Logitech G15 family devices requiring a manual restart of LCDd
  after a unplug + replug
- Drop ghosting of /etc/lcdproc/*.conf files, these may contain user
  modifications, so they should not be removed on package removal
- This also fixes lcdexec.conf and lcdvc.conf not being packaged

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.9-13.20190625git781b311
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-12.20190625git781b311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 21:06:08 GMT 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.9-11.20190625git781b311
- Build with libusb1

* Thu Aug 20 2020 Jeff Law <law@redhat.com> - 0.5.9-10.20190625git781b311
- Re-enable LTO

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-9.20190625git781b311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jeff Law <law@redhat.com> - 0.5.9-8.20190625git781b311
- Disable LTO

* Fri Mar 20 2020 Hans de Goede <hdegoede@redhat.com> - 0.5.9-7.20190625git781b311
- Drop svgalib support, svgalib is being dropped from the distro (rhbz#1814816)

* Mon Feb 24 2020 Than Ngo <than@redhat.com> - 0.5.9-6.git
- Fixed FTBFS against gcc10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-5.20190625git781b311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct  4 2019 Hans de Goede <hdegoede@redhat.com> - 0.5.9-4.20190625git781b311
- Replace Group=lcdd statement in LCDd.service with Group=nobody, LCDd does not
  need a special group and it breaks starting LCDd (rhbz#1742994)

* Thu Oct  3 2019 Hans de Goede <hdegoede@redhat.com> - 0.5.9-3.20190625git781b311
- The patch adding the keycodes for LCD menu buttons on Logitech keyboards was
  still pending upstream. The final version of the patch has changed the codes,
  update LCDd-hwdetect.sh to use the new codes when writing out LCDd.conf

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-2.20190625git781b311
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Hans de Goede <hdegoede@redhat.com> - 0.5.9-1.20190625git781b311
- Update to upstream 0.5.9 release + latest improvements from git
- Add support for Logitech MX5000, MX5500, G15, G15 V2 and G510 keyboards
- Add LCDd-hwdetect script automatically generating LCDd.conf for
  USB gaming keyboards with LCD panels and LCD2USB devices
- Add udev-rules to call LCDd-hwdetect when there is no existing LCDd.conf
  and to make LCDd and lcdproc hw-activated when using supported USB devices

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.7-11
- Remove unneeded BuildRequires: pth-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.5.7-7
- Remove ControlGroup from services - rhbz#1324015

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 04 2014 Dan Horák <dan[at]danny.cz> - 0.5.7-4
- update BR, libusbx-devel is brought in by libftdi-devel

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.7-1
- Update to 0.5.7
- Build against libusbx and libftdi 1
- Cleanup spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.5.6-5
- Perl 5.18 rebuild

* Sat Apr 27 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.5.6-4
- Enable hardened build rhbz#955453

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Dan Horák <dan[at]danny.cz> - 0.5.6-2
- update BR for s390(x)

* Wed Jan 02 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.5.6-1
- Update to 0.5.6

* Wed Aug 29 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.5-6
- Add systemd macro - rbz#850181

* Sun Jul 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.5-5
- Fix for rhbz#821270

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 13 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.5-3
- Convert to native systemd units

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.5.5-1
- Update to 5.5
- Fix path of functions
- Disable xosd and svga

* Wed Mar 30 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.5.4-1
- Update to 0.5.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 18 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.5.3-5
- Remove Uneeded BR - rhbz#572621
- Rebuild for libftdi update - rhbz#581601

* Thu Sep 10 2009 Jarod Wilson <jarod@redhat.com> - 0.5.3-4
- Add BR: libftdi-devel to build lis driver (#522270)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Jarod Wilson <jarod@redhat.com> - 0.5.3-2
- Fix broken LCDd initscript patch that prevented it from starting

* Mon Jun 22 2009 Jarod Wilson <jarod@redhat.com> - 0.5.3-1
- Update to lcdproc v0.5.3 release
- Drop upstreamed imonlcd and memset_swp patches
- Switch to upstream's rpm initscripts (albeit still patched, need
  to get that bit upstream for the next release)

* Wed May 13 2009 kwizart < kwizart at gmail.com > - 0.5.2-12
- Improve the initscripts patch - Fix #498384

* Tue Apr 14 2009 kwizart < kwizart at gmail.com > - 0.5.2-11
- Disable xmlto validation (Fix FTBFS)
- Disable default configuration (only provided as examples)

* Thu Mar  5 2009 kwizart < kwizart at gmail.com > - 0.5.2-10
- Disable LCDd lcdproc initscript by default.
  (It needs to be configured first).

* Mon Mar  2 2009 kwizart < kwizart at gmail.com > - 0.5.2-9
- re-enable patch0
- Prevent some timestamps changes.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 07 2008 Jarod Wilson <jarod@redhat.com> - 0.5.2-7
- Add SoundGraph iMon and Antec Veris LCD device support
- Replace start_daemon w/daemon in initscripts (#468611)

* Tue Jul  8 2008 kwizart < kwizart at gmail.com > - 0.5.2-6
- Add BR on Fedora > 9 : docbook-dtds

* Tue Jul  8 2008 kwizart < kwizart at gmail.com > - 0.5.2-5
- Fix RETVAL for LSB compliant initscripts - #246971
- Fix Default driver path - #454194

* Sat Feb  9 2008 kwizart < kwizart at gmail.com > - 0.5.2-4
- Rebuild for gcc43

* Sun Aug 26 2007 kwizart < kwizart at gmail.com > - 0.5.2-3
- Rebuild for BuildID

* Sun Aug 12 2007 kwizart < kwizart at gmail.com > 0.5.2-2
- Fix memset swap from djones advice
- License is GPLv2
- Fix #246971

* Sat May 19 2007 kwizart < kwizart at gmail.com > 0.5.2-1
- Update to 0.5.2
- Add BR
- Install docs

* Tue Apr 17 2007 kwizart < kwizart at gmail.com > 0.5.1-1
- Cleaned spec files for Fedora guidelines.

* Fri Sep 26 2003 TC Wan <tcwan@cs.usm.my>
- Fixed spec file for RH 9, made metar dependency optional

* Sun Oct  6 2002 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.4.3-2mdk
- Add docs

* Thu Sep 12 2002 Nicolas Chipaux <chipaux@mandrakesoft.com> 0.4.3-1mdk
- new release

* Fri Oct 26 2001 Rex Dieter <rdieter@unl.edu> 0.4.1-1
- --enable-stat-smbfs
- TODO: make server/client init scripts

* Mon Oct 22 2001 Rex Dieter <rdieter@unl.edu> -0
- first try, 0.4.1 
- --enable-stat-nfs

