%global tools_version 2.11.1
%global linux_version 2.11.1

Name:           dahdi-tools
Version:        %{tools_version}
Release:        34%{?dist}
Summary:        Userspace tools to configure the DAHDI kernel modules

# Automatically converted from old format: GPLv2 and LGPLv2 - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2
URL:            http://www.asterisk.org/

Source0:        http://downloads.asterisk.org/pub/telephony/dahdi-tools/releases/dahdi-tools-%{tools_version}.tar.gz
Source1:        http://downloads.asterisk.org/pub/telephony/dahdi-tools/releases/dahdi-tools-%{tools_version}.tar.gz.asc
Source2:        http://downloads.asterisk.org/pub/telephony/dahdi-linux/releases/dahdi-linux-%{linux_version}.tar.gz
Source3:        http://downloads.asterisk.org/pub/telephony/dahdi-linux/releases/dahdi-linux-%{linux_version}.tar.gz.asc
# Add SystemD service file
Source4:        dahdi.service

# Add wcopenpci to initial blacklist
Patch0:         dahdi-tools-blacklist-wcopenpci.patch
# Fix gcc warning (upgraded to error) for what was almost certainly
# an incorrect use of the logical negation operator
#Patch1:         mpptalk-oper-fix.patch
# Fix GCC warning for unused variables, bug #1306634,
# fixed in upstream after 2.11.0
#Patch2:         dahdi-tools-2.10.0-Remove-unused-rcsid.patch
# Fix for GCC 10
Patch3:		https://issues.asterisk.org/jira/secure/attachment/58976/dahdi-tools-3.1.0-fno-common.patch
Patch4:		gcc-lto.patch
# Fixes building PIE executables
Patch5:         dahdi-tools-2.11.1-Respect-CFLAGS.patch
# Fix Makefile.legacy so that it adds compiler and linker flags
Patch6:         dahdi-tools_fix-legacy-make.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  newt-devel
BuildRequires:  patch
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  perl-generators
BuildRequires:  udev
%{?systemd_requires}

Requires:        dahdi-tools-libs%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:        systemd-udev
%endif
Requires(pre):   %{_sbindir}/useradd
Requires(pre):   %{_sbindir}/groupadd

Conflicts:       zaptel-utils

%description
DAHDI stands for Digium Asterisk Hardware Device Interface. This
package contains the userspace tools to configure the DAHDI kernel
modules.  DAHDI is the replacement for Zaptel, which must be renamed
due to trademark issues.

%package        libs
Summary:        Library files for DAHDI
Conflicts:      zaptel-lib

%description    libs
The dahdi-tools-libs package contains libraries for accessing DAHDI hardware.

%package        devel
Summary:        Development files for DAHDI
Requires:       dahdi-tools-libs%{?_isa} = %{version}-%{release}
BuildRequires:  chrpath
BuildRequires: make

%description    devel
The dahdi-devel package contains libraries and header files for
developing applications that use DAHDI hardware.

%prep
%setup0 -q -n dahdi-tools-%{tools_version} -a 2
ln -s dahdi-linux-%{linux_version}/include include

%patch -P0 -p1 -b .blacklist
# Fix for GCC 10
%patch -P3 -p1 -b .gcc10
%patch -P4 -p1 -b .gcc-lto
%patch -P5 -p1 -b .cflags
%patch -P6 -p1 -b .legacy-fix

# Copy SystemD service file
cp -pa %{SOURCE4} dahdi.service

# Fix incorrect FSF addresses
sed -i -e \
   's/675 Mass Ave, Cambridge, MA 02139/51 Franklin St, Boston, MA 02110/' \
   xpp/*.c xpp/*.h xpp/xtalk/*.c xpp/xtalk/*.h xpp/xtalk/include/xtalk/*.h \
   xpp/waitfor_xpds xpp/xpp_fxloader

sed -i -e \
   's/59 Temple Place, Suite 330, Boston, MA  02111-1307/51 Franklin St, Boston, MA 02110/' \
   LICENSE


%build
autoreconf -fi
%configure --with-dahdi=`pwd` --enable-shared --with-pic --with-perllib=%{perl_vendorlib}

# allow overrding the variable in Makefile
#sed -i s/UDEVRULES_DIR:=/UDEVRULES_DIR=/ Makefile

%{make_build}


%install
%make_install config PERLLIBDIR=%{perl_vendorlib} perllibdir=%{perl_vendorlib} UDEVRULES_DIR=%{_udevrulesdir} udevrulesdir=%{_udevrulesdir}
install -D -p -m 0644 include/dahdi/user.h %{buildroot}%{_includedir}/dahdi/user.h
install -D -p -m 0644 include/dahdi/user.h %{buildroot}%{_includedir}/dahdi/dahdi_config.h
find %{buildroot} -name '*.a' -delete
rm -f %{buildroot}%{_sbindir}/sethdlc
rm -f %{buildroot}%{_libdir}/libtonezone.la
chrpath --delete %{buildroot}%{_sbindir}/dahdi_cfg
mkdir -p %{buildroot}%{_unitdir}
install -D -p -m 0644 dahdi.service %{buildroot}%{_unitdir}/dahdi.service

%pre
%{_sbindir}/groupadd -r dahdi &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d /usr/share/dahdi -M \
                               -c 'DAHDI User' -g dahdi dahdi &>/dev/null || :

%post
%systemd_post dahdi.service

%preun
%systemd_preun dahdi.service

%postun
%systemd_postun_with_restart dahdi.service

%files
%license LICENSE LICENSE.LGPL
%doc README
%dir %{_sysconfdir}/dahdi
%config(noreplace) %{_sysconfdir}/bash_completion.d/dahdi
%config(noreplace) %{_sysconfdir}/dahdi/assigned-spans.conf.sample
%config(noreplace) %{_sysconfdir}/dahdi/modules.sample
%config(noreplace) %{_sysconfdir}/dahdi/span-types.conf.sample
%config(noreplace) %{_sysconfdir}/dahdi/system.conf.sample
%{_udevrulesdir}/dahdi.rules
%{_udevrulesdir}/xpp.rules
%{_sbindir}/astribank_allow
%{_sbindir}/astribank_hexload
%{_sbindir}/astribank_is_starting
%{_sbindir}/astribank_tool
%{_sbindir}/dahdi_cfg
%{_sbindir}/dahdi_genconf
%{_sbindir}/dahdi_hardware
%{_sbindir}/dahdi_maint
%{_sbindir}/dahdi_monitor
%{_sbindir}/dahdi_registration
%{_sbindir}/dahdi_scan
%{_sbindir}/dahdi_span_assignments
%{_sbindir}/dahdi_span_types
%{_sbindir}/dahdi_speed
%{_sbindir}/dahdi_test
%{_sbindir}/dahdi_tool
%{_sbindir}/dahdi_waitfor_span_assignments
%{_sbindir}/fxotune
%{_sbindir}/lsdahdi
%{_sbindir}/twinstar
%{_sbindir}/xpp_blink
%{_sbindir}/xpp_sync
%dir %{_datadir}/dahdi
%{_datadir}/dahdi/astribank_hook
%{_datadir}/dahdi/xpp_fxloader
%{_datadir}/dahdi/waitfor_xpds
%{_datadir}/dahdi/dahdi_auto_assign_compat
%{_datadir}/dahdi/dahdi_handle_device
%{_datadir}/dahdi/dahdi_span_config
%dir %{_datadir}/dahdi/handle_device.d
%{_datadir}/dahdi/handle_device.d/10-span-types
%{_datadir}/dahdi/handle_device.d/20-span-assignments
%dir %{_datadir}/dahdi/span_config.d
%{_datadir}/dahdi/span_config.d/10-dahdi-cfg
%{_datadir}/dahdi/span_config.d/20-fxotune
%{_datadir}/dahdi/span_config.d/50-asterisk
%{_mandir}/man8/astribank_allow.8.gz
%{_mandir}/man8/astribank_hexload.8.gz
%{_mandir}/man8/astribank_is_starting.8.gz
%{_mandir}/man8/astribank_tool.8.gz
%{_mandir}/man8/dahdi_cfg.8.gz
%{_mandir}/man8/dahdi_genconf.8.gz
%{_mandir}/man8/dahdi_hardware.8.gz
%{_mandir}/man8/dahdi_maint.8.gz
%{_mandir}/man8/dahdi_monitor.8.gz
%{_mandir}/man8/dahdi_registration.8.gz
%{_mandir}/man8/dahdi_scan.8.gz
%{_mandir}/man8/dahdi_span_assignments.8.gz
%{_mandir}/man8/dahdi_span_types.8.gz
%{_mandir}/man8/dahdi_test.8.gz
%{_mandir}/man8/dahdi_tool.8.gz
%{_mandir}/man8/dahdi_waitfor_span_assignments.8.gz
%{_mandir}/man8/fxotune.8.gz
%{_mandir}/man8/lsdahdi.8.gz
%{_mandir}/man8/twinstar.8.gz
%{_mandir}/man8/xpp_blink.8.gz
%{_mandir}/man8/xpp_sync.8.gz
%{perl_vendorlib}/Dahdi.pm
%{perl_vendorlib}/Dahdi
%{_sbindir}/xtalk_send
%{_mandir}/man8/xtalk_send.8.gz
%{_unitdir}/dahdi.service

%files libs
%license LICENSE LICENSE.LGPL
%{_libdir}/*.so.*

%files devel
%license LICENSE LICENSE.LGPL
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.11.1-33
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Petr Pisar <ppisar@redhat.com> - 2.11.1-26
- Rename a dependency on libusb-devel (bug #2066607)
- Move configure to build section because of linker package notes (bug #2045296)
- Respect distribution CFLAGS
- Set Perl libdir with a configure option

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.11.1-25
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.11.1-22
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.11.1-21
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.11.1-18
- Perl 5.32 rebuild

* Tue May 26 2020 Jeff Law <law@redhat.com> - 2.11.1-17
- Fix inline vs static inline exposed by LTO.

* Mon May 04 2020 Jared K. Smith <jsmith@fedoraproject.org> - 2.11.1-16
- Add patch to fix XPP compilation with GCC 10
- Fix dependency on systemd-udev for EPEL 7

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.11.1-13
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 2.11.1-10
- Perl 5.28 rebuild

* Thu Mar 08 2018 jsmith <jsmith.fedora@gmail.com> - 2.11.1-9
- Remove call to ldconfig_scriptlets macro, as it conflicts with %%post

* Wed Feb 14 2018 Jared Smith <jsmith@fedoraproject.org> - 2.11.1-8
- Replace post and postun scriptlets with ldconfig_scriptlets macro invocation

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Jared Smith <jsmith@fedoraproject.org> - 2.11.1-4
- Bump revision for new version of Perl

* Wed May 24 2017 Jared Smith <jsmith@fedoraproject.org> - 2.11.1-3
- Add missing Requires and BuildRequires

* Wed May 24 2017 Jared Smith <jsmith@fedoraproject.org> - 2.11.1-2
- Fix dependencies
- Replace defines with globals
- Fix incorrect FSF addresses with a little sed magic

* Wed Mar 30 2016 Jared Smith <jsmith@fedoraproject.org> - 2.11.1-1
- Update to upstream 2.11.1 release
- Add systemd support

* Wed Mar 30 2016 Petr Pisar <ppisar@redhat.com> - 2.10.0-8
- Fix GCC warning for unused variables (bug #1306634)
- Modernize spec file

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.10.0-6
- Move rules file to %%{_udevrulesdir} (#1229955)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Bruno Wolff III - 2.10.0-4
- Fix FTBFS from gcc error due to bad use of logical negation operator
- This should also take care of the rebuild needed for perl

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.0-3
- Perl 5.22 rebuild

* Fri Nov 07 2014 Petr Pisar <ppisar@redhat.com> - 2.10.0-2
- Build-require perl-podlators for pod2man tool (bug #1161158)

* Fri Oct 24 2014 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.10.0-1
- Update to 2.10.0

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.0-6
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 17 2013 Bruno Wolff III <bruno@wolff.to> - 2.7.0-3
- blacklist wcopenpci so that it doesn't get loaded until the right time

* Sat Aug 17 2013 Bruno Wolff III <bruno@wolff.to> - 2.7.0-2
- Include user.h as dahdi_config.h to avoid issue noted in bug 783890

* Sat Aug 17 2013 Bruno Wolff III <bruno@wolff.to> - 2.7.0-1
- Move to current upstream release
- Changlog is available at http://git.asterisk.org/gitweb/?p=dahdi/tools.git;a=shortlog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.4.1-8
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.4.1-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.4.1-3
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.4.1-2
- Perl 5.14 mass rebuild

* Fri Mar  4 2011  <jeff@ocjtech.us> - 2.4.1-1
- The Asterisk Development Team is pleased to announce the release of
- DAHDI-Linux and DAHDI-Tools version 2.4.1.
-
- DAHDI-Linux 2.4.1, DAHDI-Tools 2.4.1, and DAHDI-Linux-Complete 2.4.1+2.4.1 are
- available for immediate download at:
- http://downloads.asterisk.org/pub/telephony/dahdi-linux
- http://downloads.asterisk.org/pub/telephony/dahdi-tools
- http://downloads.asterisk.org/pub/telephony/dahdi-linux-complete
-
- 2.4.1 is a maintenance release of the DAHDI drivers and tools packages. Some of
- the more notable changes are:
-
- * Support for compilation against kernel versions from 2.6.9 up to and including
-  2.6.38-rc6.
-
- * wct4xxp: PCI-express cards go through an extended reset at start by default.
-
- * wcte12xp, wctdm24xxp: Disable read-line multiple PCI command, which increases
-  compatibility in some systems.
-
- * xpp: Fixes init error for PRI devices with < 4 ports.
-
- * tonezone: Add Macao, China to tone zone data.
-
- * dahdi_genconf: Don't generate configurations that use channel 16 on E1 CAS.
-
- For a full list of changes in these releases, please see the ChangeLogs at
- http://svn.asterisk.org/svn/dahdi/linux/tags/2.4.1/ChangeLog and
- http://svn.asterisk.org/svn/dahdi/tools/tags/2.4.1/ChangeLog
-
- Issues found in these release candidates can be reported in the DAHDI-linux or
- DAHDI-tools project at https://issues.asterisk.org

* Wed Feb  9 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.4.0-2
- Make library requirements architecture specific.

* Wed Feb  9 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.4.0-1
-
- In addition to several bug fixes, the most significant changes from the
- 2.3.0 release are:
-
- General DAHDI Changes:
-
- * Added DAHDI_MAINT_ALARM_SIM maintenance mode for drivers that
-  support alarm simulation (wct4xxp).  This is only used by
-  dahdi_maint and doesn't change the ABI.
-
- * Span callbacks are moved out of the dahdi_span structure potentially
-  saving memory when a single driver implements multiple spans.
-
- Changes to dahdi-tools:
-
- * dahdi_maint: Added support for simulating alarm conditions.
-
- * dahdi_scan: Report more detailed alarm information.
-
- * xpp_fxloader:
-  - Load firmware in the background
-  - Support 1163 twinstar devices
-  - A delay loop for older kernels (e.g. 2.6.18)
-
- * astribank_is_starting does not depend on libusb.
-
- * Allow using CONNECTOR/LABEL in genconf_parameters for pri_termtype
-
- For a full list of changes in these releases, please see the ChangeLogs at
- http://svn.asterisk.org/svn/dahdi/linux/tags/2.4.0/ChangeLog and
- http://svn.asterisk.org/svn/dahdi/tools/tags/2.4.0/ChangeLog

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug  7 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.3.0-1
- Update to 2.3.0

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.1.0.2-10
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.1.0.2-9
- rebuild against perl 5.10.1

* Wed Aug 19 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.1.0.2-8
- fix bz 495453 (/etc/modprobe.d/dahdi.blacklist and /etc/modprobe.d/dahdi doesn't end with.conf)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1.0.2-6
- Let dahdi-tools conflict with zaptel-utils (#472357).

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan  4 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.1.0.2-4
- Update to latest.

* Thu Nov 20 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.0-4
- Fix zaptel-lib(s) conflicts

* Sat Oct 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.0-3
- Add conflicts/requires to help make sure that we get dahdi-tools-libs and not zaptel-libs

* Fri Oct 10 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.0-2
- Don't package sethdlc even if it gets built.

* Thu Oct  9 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.0-1
- Cleanups suggested by reviewers

* Fri Oct  3 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.0-0.4
- Update to final release.

* Wed Sep 10 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.0-0.3.rc2
- Install dahdi/user.h header

* Mon Sep  8 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.0-0.2.rc2
- Update dahdi-linux to 2.0.0rc4

* Fri Sep  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.0.0-0.1.rc2
- First version for Fedora
