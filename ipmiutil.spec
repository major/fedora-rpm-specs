# spec file for package ipmiutil 
#
# Copyright (c) 2012 Andy Cress
#
Name:      ipmiutil
Version: 3.1.2
Release: 13%{?dist}
Summary:   Easy-to-use IPMI server management utilities
License:   BSD
Source:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:       http://ipmiutil.sourceforge.net
# Suggests: cron or vixie-cron or cronie or similar
%{!?_unitdir: %define _unitdir  /usr/lib/systemd/system}
%define unit_dir  %{_unitdir}
%define init_dir  %{_initrddir}
%define systemd_fls %{_datadir}/%{name}
%define bldreq0   openssl-devel gcc gcc-c++
%define bldreq_extra libtool 
%if 0%{?fedora} >= 15
%define bldreq_extra systemd autoconf automake systemd-units
Requires:  systemd-units
%if 0%{?fedora} == 16
%define unit_dir  /lib/systemd/system
%endif
%if 0%{?fedora} >= 25
%define bldreq_extra systemd autoconf automake systemd-units qrencode-libs
%endif
%endif
%if 0%{?rhel} >= 7
%define bldreq_extra autoconf automake systemd-units
%endif
%if 0%{?sles_version} > 10
%define bldreq0 libopenssl-devel 
%endif
%if 0%{?suse_version} >= 1210
%define bldreq_extra libtool systemd
%define req_systemd 1
%define systemd_fls %{unit_dir}
# Requires: %{?systemd_requires}
%endif
BuildRequires: %{bldreq0} %{bldreq_extra}
BuildRequires: make

%description
The ipmiutil package provides easy-to-use utilities to view the SEL,
perform an IPMI chassis reset, set up the IPMI LAN and Platform Event Filter
entries to allow SNMP alerts, Serial-Over-LAN console, event daemon, and 
other IPMI tasks.
These can be invoked with the metacommand ipmiutil, or via subcommand
shortcuts as well.  IPMIUTIL can also write sensor thresholds, FRU asset tags, 
and has a full IPMI configuration save/restore.
An IPMI driver can be provided by either the OpenIPMI driver (/dev/ipmi0)
or the Intel IPMI driver (/dev/imb), etc.  If used locally and no driver is
detected, ipmiutil will use user-space direct I/Os instead.

%package devel
Summary:  Includes libraries and headers for the ipmiutil package
Requires: ipmiutil

%description devel
The ipmiutil-devel package contains headers and libraries which are
useful for building custom IPMI applications.

%package static
Summary:  Includes static libraries for the ipmiutil package

%description static
The ipmiutil-static package contains static libraries which are
useful for building custom IPMI applications.

%prep
%setup -q

%build
%if 0%{?fedora} >= 15
autoconf
%endif
%if 0%{?req_systemd}
%configure --enable-systemd
%else
%configure
%endif
%if 0%{?fedora} >= 15
make %{?_smp_mflags}
%else
make 
%endif

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%dir %{_datadir}/%{name}
%dir %{_var}/lib/%{name}
%{_bindir}/ipmiutil
%{_bindir}/idiscover
%{_bindir}/ievents
%{_sbindir}/iseltime
%{_sbindir}/ipmi_port
%{_sbindir}/ialarms 
%{_sbindir}/iconfig
%{_sbindir}/icmd 
%{_sbindir}/ifru 
%{_sbindir}/igetevent 
%{_sbindir}/ihealth 
%{_sbindir}/ilan 
%{_sbindir}/ireset 
%{_sbindir}/isel 
%{_sbindir}/isensor 
%{_sbindir}/iserial 
%{_sbindir}/isol 
%{_sbindir}/iwdt 
%{_sbindir}/ipicmg 
%{_sbindir}/ifirewall 
%{_sbindir}/ifwum 
%{_sbindir}/ihpm 
%{_sbindir}/iuser 
%{_libdir}/libipmiutil.so.1
%{_datadir}/%{name}/ipmiutil_evt
%{_datadir}/%{name}/ipmiutil_asy
%{_datadir}/%{name}/ipmiutil_wdt
%{_datadir}/%{name}/ipmi_port
%{_datadir}/%{name}/ipmi_info
%{_datadir}/%{name}/checksel
%{systemd_fls}/ipmiutil_evt.service
%{systemd_fls}/ipmiutil_asy.service
%{systemd_fls}/ipmiutil_wdt.service
%{systemd_fls}/ipmi_port.service
%{_datadir}/%{name}/ipmiutil.env
%{_datadir}/%{name}/ipmiutil.pre
%{_datadir}/%{name}/ipmiutil.setup
%{_datadir}/%{name}/ipmi_if.sh
%{_datadir}/%{name}/evt.sh
%{_datadir}/%{name}/ipmi.init.basic
%{_datadir}/%{name}/bmclanpet.mib
%{_mandir}/man8/isel.8*
%{_mandir}/man8/isensor.8*
%{_mandir}/man8/ireset.8*
%{_mandir}/man8/igetevent.8*
%{_mandir}/man8/ihealth.8*
%{_mandir}/man8/iconfig.8*
%{_mandir}/man8/ialarms.8*
%{_mandir}/man8/iwdt.8*
%{_mandir}/man8/ilan.8*
%{_mandir}/man8/iserial.8*
%{_mandir}/man8/ifru.8*
%{_mandir}/man8/icmd.8*
%{_mandir}/man8/isol.8*
%{_mandir}/man8/ipmiutil.8*
%{_mandir}/man8/idiscover.8*
%{_mandir}/man8/ievents.8*
%{_mandir}/man8/ipmi_port.8*
%{_mandir}/man8/ipicmg.8*
%{_mandir}/man8/ifirewall.8*
%{_mandir}/man8/ifwum.8*
%{_mandir}/man8/ihpm.8*
%{_mandir}/man8/isunoem.8*
%{_mandir}/man8/idelloem.8*
%{_mandir}/man8/ismcoem.8*
%{_mandir}/man8/iekanalyzer.8*
%{_mandir}/man8/itsol.8*
%{_mandir}/man8/idcmi.8*
%{_mandir}/man8/iuser.8*
%{_mandir}/man8/iseltime.8*
%doc AUTHORS ChangeLog COPYING NEWS README TODO 
%doc doc/UserGuide

%files devel
# .{_datadir}/.{name} is used by both ipmiutil and ipmiutil-devel
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ipmi_sample.c
%{_datadir}/%{name}/ipmi_sample_evt.c
%{_datadir}/%{name}/isensor.c
%{_datadir}/%{name}/ievents.c
%{_datadir}/%{name}/isensor.h
%{_datadir}/%{name}/ievents.h
%{_datadir}/%{name}/Makefile
%{_libdir}/libipmiutil.so
%{_includedir}/ipmicmd.h

%files static
%{_libdir}/libipmiutil.a

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

%pre
%if 0%{?req_systemd}
%service_add_pre ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service
%endif

%post
/sbin/ldconfig
# POST_INSTALL, $1 = 1 if rpm -i, $1 = 2 if rpm -U
if [ "$1" = "1" ]
then
   # doing rpm -i, first time
   vardir=%{_var}/lib/%{name}
   scr_dir=%{_datadir}/%{name}

%if 0%{?req_systemd}
%service_add_post ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service
%else
   if [ -x /bin/systemctl ] && [ -d %{unit_dir} ]; then
      echo "IINITDIR=%{init_dir}" >>%{_datadir}/%{name}/ipmiutil.env
      cp -f ${scr_dir}/ipmiutil_evt.service %{unit_dir}
      cp -f ${scr_dir}/ipmiutil_asy.service %{unit_dir}
      cp -f ${scr_dir}/ipmiutil_wdt.service %{unit_dir}
      cp -f ${scr_dir}/ipmi_port.service    %{unit_dir}
      # systemctl enable ipmi_port.service >/dev/null 2>&1 || :
   else 
      cp -f ${scr_dir}/ipmiutil_wdt %{init_dir}
      cp -f ${scr_dir}/ipmiutil_asy %{init_dir}
      cp -f ${scr_dir}/ipmiutil_evt %{init_dir}
      cp -f ${scr_dir}/ipmi_port    %{init_dir}
      cp -f ${scr_dir}/ipmi_info    %{init_dir}
   fi
%endif

   # Test whether an IPMI interface is known to the motherboard
   IPMIret=1
   which dmidecode >/dev/null 2>&1 && IPMIret=0
   if [ $IPMIret -eq 0 ]; then
    IPMIret=1
    %{_sbindir}/dmidecode |grep -q IPMI && IPMIret=0
    if [ $IPMIret -eq 0 ]; then
     # Run some ipmiutil command to see if any IPMI interface works.
     # Some may not have IPMI on the motherboard, so need to check, but
     # some kernels may have IPMI driver partially loaded, which breaks this
     IPMIret=1
     %{_bindir}/ipmiutil sel -v >/dev/null 2>&1 && IPMIret=0
     if [ $IPMIret -eq 0 ]; then
      if [ ! -x %{init_dir}/ipmi ]; then
         cp -f ${scr_dir}/ipmi.init.basic  %{init_dir}/ipmi
      fi
      # If IPMI is enabled, automate managing the IPMI SEL
      if [ -d %{_sysconfdir}/cron.daily ]; then
         cp -f %{_datadir}/%{name}/checksel %{_sysconfdir}/cron.daily
      fi
      # IPMI_IS_ENABLED, so enable services, but only if Red Hat
      if [ -f /etc/redhat-release ]; then
         if [ -x /bin/systemctl ]; then
            touch ${scr_dir}/ipmi_port.service
         elif [ -x /sbin/chkconfig ]; then
            /sbin/chkconfig --add ipmi_port
            /sbin/chkconfig --add ipmi_info
            # /sbin/chkconfig --add ipmiutil_wdt
            # /sbin/chkconfig --add ipmiutil_evt 
         fi
      fi
   
      # Capture a snapshot of IPMI sensor data once now for later reuse.
      sensorout=$vardir/sensor_out.txt
      if [ ! -f $sensorout ]; then
         %{_bindir}/ipmiutil sensor -q >$sensorout || :
         if [ $? -ne 0 ]; then
           # remove file if error, try again in ipmi_port on reboot.
           rm -f $sensorout
         fi
      fi
     fi
    fi
   fi
else
   # postinstall, doing rpm update
   IPMIret=1
   which dmidecode >/dev/null 2>&1 && IPMIret=0
   if [ $IPMIret -eq 0 ]; then
    IPMIret=1
    %{_sbindir}/dmidecode |grep -q IPMI && IPMIret=0
    if [ $IPMIret -eq 0 ]; then
      if [ -d %{_sysconfdir}/cron.daily ]; then
         cp -f %{_datadir}/%{name}/checksel %{_sysconfdir}/cron.daily
      fi
    fi
   fi
fi
%if 0%{?fedora} >= 18
%systemd_post  ipmiutil_evt.service
%systemd_post  ipmiutil_asy.service
%systemd_post  ipmiutil_wdt.service
%systemd_post  ipmi_port.service
%endif

%preun
# before uninstall,  $1 = 1 if rpm -U, $1 = 0 if rpm -e
if [ "$1" = "0" ]
then
%if 0%{?req_systemd}
%service_del_preun ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service
%else
   if [ -x /bin/systemctl ]; then
     if [ -f %{unit_dir}/ipmiutil_evt.service ]; then
%if 0%{?fedora} >= 18
%systemd_preun  ipmiutil_evt.service
%systemd_preun  ipmiutil_asy.service
%systemd_preun  ipmiutil_wdt.service
%systemd_preun  ipmi_port.service
%else
        systemctl disable ipmi_port.service >/dev/null 2>&1 || :
        systemctl disable ipmiutil_evt.service >/dev/null 2>&1 || :
        systemctl disable ipmiutil_asy.service >/dev/null 2>&1 || :
        systemctl disable ipmiutil_wdt.service >/dev/null 2>&1 || :
        systemctl stop ipmiutil_evt.service >/dev/null 2>&1 || :
        systemctl stop ipmiutil_asy.service >/dev/null 2>&1 || :
        systemctl stop ipmiutil_wdt.service >/dev/null 2>&1 || :
        systemctl stop ipmi_port.service    >/dev/null 2>&1 || :
%endif
     fi
   else 
     if [ -x /sbin/service ]; then
        /sbin/service ipmi_port stop       >/dev/null 2>&1 || :
        /sbin/service ipmiutil_wdt stop    >/dev/null 2>&1 || :
        /sbin/service ipmiutil_asy stop    >/dev/null 2>&1 || :
        /sbin/service ipmiutil_evt stop    >/dev/null 2>&1 || :
     fi
     if [ -x /sbin/chkconfig ]; then
        /sbin/chkconfig --del ipmi_port    >/dev/null 2>&1 || :
        /sbin/chkconfig --del ipmiutil_wdt >/dev/null 2>&1 || :
        /sbin/chkconfig --del ipmiutil_asy >/dev/null 2>&1 || :
        /sbin/chkconfig --del ipmiutil_evt >/dev/null 2>&1 || :
     fi
   fi
%endif
   if [ -f %{_sysconfdir}/cron.daily/checksel ]; then
        rm -f %{_sysconfdir}/cron.daily/checksel
   fi
fi

%postun
# after uninstall,  $1 = 1 if update, $1 = 0 if rpm -e
/sbin/ldconfig
%if 0%{?req_systemd}
%service_del_postun ipmi_port.service ipmiutil_evt.service ipmiutil_asy.service ipmiutil_wdt.service
%else
if [ -x /bin/systemctl ]; then
%if 0%{?fedora} >= 18
%systemd_postun_with_restart  ipmi_port.service
%else
   systemctl daemon-reload  || :
   if [ $1 -ge 1 ] ; then
      # Package upgrade, not uninstall
      systemctl try-restart ipmi_port.service  || :
   fi
%endif
   if [ -f %{unit_dir}/ipmiutil_evt.service ]; then
      rm -f %{unit_dir}/ipmiutil_evt.service  2>/dev/null || :
      rm -f %{unit_dir}/ipmiutil_asy.service  2>/dev/null || :
      rm -f %{unit_dir}/ipmiutil_wdt.service  2>/dev/null || :
      rm -f %{unit_dir}/ipmi_port.service     2>/dev/null || :
   fi
else
   if [ -f %{init_dir}/ipmiutil_evt.service ]; then
      rm -f %{init_dir}/ipmiutil_wdt 2>/dev/null || :
      rm -f %{init_dir}/ipmiutil_asy 2>/dev/null || :
      rm -f %{init_dir}/ipmiutil_evt 2>/dev/null || :
      rm -f %{init_dir}/ipmi_port    2>/dev/null || :
   fi
fi
%endif

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.1.2-11
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Andrew Cress <arcress at users.sourceforge.net> 3.1.2-2
- added iseltime.8, reworked util/Makefile.am for race condition
* Fri Jul 20 2018 Andrew Cress <arcress at users.sourceforge.net> 3.1.2-1
- resolve doubly-defined Group for Fedora
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Andrew Cress <arcress at users.sourceforge.net> 3.1.1-3
- remove BuildRoot, %clean, %defattr per fedeng, RHBZ# 1599923
* Wed Jul 11 2018 Andrew Cress <arcress at users.sourceforge.net> 3.1.1-2
- fix spec comments 
* Thu May 31 2018 Andrew Cress <arcress at users.sourceforge.net> 3.1.1-1
- update to upstream 3.1.1, RHBZ# 1560767, 1555891
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Andrew Cress <arcress at users.sourceforge.net> 3.0.8-1
- update from upstream 3.0.8, RHBZ#1423055
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Wed Jun 14 2017 Andrew Cress <arcress at users.sourceforge.net> 3.0.5-1
- added iuser, iuser.8
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Andrew Cress <arcress at users.sourceforge.net> 3.0.1-1
- refine detection if IPMI is present (IPMIret)
* Thu Jun 09 2016 Andrew Cress <arcress at users.sourceforge.net> 2.9.9-3
- put libipmiutil.so.1 in base, *.so in devel, add ldconfig
* Tue May 17 2016 Andrew Cress <arcress at users.sourceforge.net> 2.9.9-2
- move libipmiutil.so* from devel to binary package RH#1177213
* Fri May 13 2016 Andrew Cress <arcress at users.sourceforge.net> 2.9.9-1
- if _unitdir not defined, give default value
* Mon Nov 03 2014 Andrew Cress <arcress at users.sourceforge.net> 2.9.5-1
- separate libipmiutil.a into ipmiutil-static package

* Thu Aug 28 2014 Andrew Cress <arcress at users.sourceforge.net> 2.9.4-1
- Updated to ipmiutil-2.9.4

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 09 2013 Andrew Cress <arcress at users.sourceforge.net> 2.9.0-1
  Merged with upstream ipmiutil-2.9.0, fix for Fedora bug #925593
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 21 2012 Andrew Cress <arcress at users.sourceforge.net> 2.8.5-2
  Added F18 systemd macros for RH bug #850163
* Fri May 04 2012 Andrew Cress <arcress at users.sourceforge.net> 2.8.4-1
  Fixups for devel rpm (RH bug #818910)
* Tue Apr 24 2012 Andrew Cress <arcress at users.sourceforge.net> 2.8.3-1
  Use service_* macros if req_systemd is set
* Thu Mar 08 2012 Andrew Cress <arcress at users.sourceforge.net> 2.8.2-1
  reworked systemd logic/macros, moved ipmiutil from sbindir to bindir
* Mon Dec 12 2011 Andrew Cress <arcress at users.sourceforge.net> 2.8.0-1
  added devel package files
* Fri Nov 11 2011 Andrew Cress <arcress at users.sourceforge.net> 2.7.9-3
  fix RH bug #752319 to not copy checksel to cron.daily if IPMI not enabled
* Tue Sep 13 2011 Andrew Cress <arcress at users.sourceforge.net> 2.7.8-1
  added systemd scripts, added idelloem.8
* Mon Jun 06 2011 Andrew Cress <arcress at users.sourceforge.net> 2.7.7-1
  add gcc,gcc-c++ to BuildRequires to detect broken build systems
* Mon May 09 2011 Andrew Cress <arcress at users.sourceforge.net> 2.7.6-1
  updated ipmiutil
* Fri Nov 12 2010 Andrew Cress <arcress at users.sourceforge.net> 2.7.3-1
  updated package description
* Fri Oct 15 2010 Andrew Cress <arcress at users.sourceforge.net> 2.7.1-1
  skip chkconfig --add if not Red Hat
* Mon Sep 27 2010 Andrew Cress <arcress at users.sourceforge.net> 2.7.0-1
  added fwum, hpm, sunoem, ekanalyzer man pages
* Mon Jul 19 2010 Andrew Cress <arcress at users.sourceforge.net> 2.6.8-1
  cleaned up two more rpmlint issues 
* Mon Jul 12 2010 Andrew Cress <arcress at users.sourceforge.net> 2.6.7-1
  cleaned up some rpmlint issues, include ipmiutil_evt in chkconfig's
* Thu Apr 29 2010 Andrew Cress <arcress at users.sourceforge.net> 2.6.4-1
  cleaned up some style issues
* Fri Mar  5 2010 Andrew Cress <arcress at users.sourceforge.net> 2.6.1-1
  cleaned up some style issues
* Tue Feb 16 2010 Andrew Cress <arcress at users.sourceforge.net> 2.6.0-1
  cleaned up some script clutter, changed naming scheme for sub-commands
* Tue Jan 26 2010 Andrew Cress <arcress at users.sourceforge.net> 2.5.3-1
  cleaned up some rpmlint issues, removed bmclanaol.mib
* Mon Nov  9 2009 Andrew Cress <arcress at users.sourceforge.net> 2.5.1-1
  do not gzip man files, clean up scripts, move distro specifics to configure
* Tue Jun 23 2009 Andrew Cress <arcress at users.sourceforge.net> 2.4.0-1
  moved all progs to sbin, install init/cron scripts via files not post
* Wed Dec 10 2008 Andrew Cress <arcress at users.sourceforge.net> 2.3.2-1
  changes for Fedora with ipmiutil-2.3.2
