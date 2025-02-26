Name:             freeipmi
Version:          1.6.15
Release:          %autorelease
Summary:          IPMI remote console and system management software
License:          GPL-3.0-or-later
URL:              https://www.gnu.org/software/freeipmi/
Source0:          https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:          bmc-watchdog.service
Source2:          ipmidetectd.service
Source3:          ipmiseld.service
BuildRequires:    libgcrypt-devel texinfo systemd 
%{?systemd_requires}
BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    automake
BuildRequires:    autoconf
BuildRequires:    libtool

# https://lists.gnu.org/archive/html/freeipmi-devel/2025-02/msg00000.html
# https://github.com/chu11/freeipmi-mirror/commit/ececf09d6128cbff65e9048f19d191e87f111059
Patch0:           c23.patch

%description
The FreeIPMI project provides "Remote-Console" (out-of-band) and
"System Management Software" (in-band) based on Intelligent
Platform Management Interface specification.

%package          devel
Summary:          Development package for FreeIPMI
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description      devel
Development package for FreeIPMI. This package includes the FreeIPMI
header files and libraries.

%package          bmc-watchdog
Summary:          IPMI BMC watchdog
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description      bmc-watchdog
Provides a watchdog daemon for OS monitoring and recovery.

%package          ipmidetectd
Summary:          IPMI node detection monitoring daemon
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description      ipmidetectd
Provides a tool and a daemon for IPMI node detection.

%package          ipmiseld
Summary:          IPMI SEL syslog logging daemon
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description      ipmiseld
IPMI SEL syslog logging daemon.

%if %{?_with_debug:1}%{!?_with_debug:0}
  %global _enable_debug --enable-debug --enable-trace --enable-syslog
%endif

%prep
%autosetup -p1
autoreconf -f -v -i

%build
export CFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS"
%configure --program-prefix=%{?_program_prefix:%{_program_prefix}} \
           %{?_enable_debug} --disable-static
%make_build

%install
%make_install
rm -rf %{buildroot}%{_infodir}/dir
# kludge to get around rpmlint complaining about 0 length semephore file
echo freeipmi > %{buildroot}%{_localstatedir}/lib/freeipmi/ipckey

# Remove .la files
find %{buildroot} -name '*.la' -delete -print

# Install systemd units
install -m755 -d %{buildroot}%{_unitdir}
install -pm644 %SOURCE1 %SOURCE2 %SOURCE3 %{buildroot}%{_unitdir}/

# Remove initscripts
rm -frv %{buildroot}%{_initrddir} %{buildroot}%{_sysconfdir}/init.d

%post bmc-watchdog
%systemd_post bmc-watchdog.service

%preun bmc-watchdog
%systemd_preun bmc-watchdog.service

%postun bmc-watchdog
%systemd_postun_with_restart bmc-watchdog.service

%post ipmiseld
%systemd_post ipmiseld.service

%preun ipmiseld
%systemd_preun ipmiseld.service

%postun ipmiseld
%systemd_postun_with_restart ipmiseld.service

%post ipmidetectd
%systemd_post ipmidetectd.service

%preun ipmidetectd
%systemd_preun ipmidetectd.service

%postun ipmidetectd
%systemd_postun_with_restart ipmidetectd.service

%triggerun -- freeipmi-bmc-watchdog < 1.1.1-2
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply httpd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save bmc-watchdog >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del bmc-watchdog >/dev/null 2>&1 || :
/bin/systemctl try-restart bmc-watchdog.service >/dev/null 2>&1 || :

%triggerun -- freeipmi-ipmidetectd < 1.1.1-2
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply httpd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save ipmidetectd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del ipmidetectd >/dev/null 2>&1 || :
/bin/systemctl try-restart ipmidetectd.service >/dev/null 2>&1 || :

%files
%dir %{_sysconfdir}/freeipmi/
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/freeipmi.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/ipmidetect.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/freeipmi_interpret_sel.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/freeipmi_interpret_sensor.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/libipmiconsole.conf
%doc %{_datadir}/doc/%{name}/AUTHORS
%doc %{_datadir}/doc/%{name}/COPYING
%doc %{_datadir}/doc/%{name}/ChangeLog
%doc %{_datadir}/doc/%{name}/ChangeLog.0
%doc %{_datadir}/doc/%{name}/INSTALL
%doc %{_datadir}/doc/%{name}/NEWS
%doc %{_datadir}/doc/%{name}/README
%doc %{_datadir}/doc/%{name}/README.argp
%doc %{_datadir}/doc/%{name}/README.build
%doc %{_datadir}/doc/%{name}/README.openipmi
%doc %{_datadir}/doc/%{name}/TODO
%doc %{_infodir}/*
%doc %{_datadir}/doc/%{name}/COPYING.ipmiping
%doc %{_datadir}/doc/%{name}/COPYING.ipmipower
%doc %{_datadir}/doc/%{name}/COPYING.ipmiconsole
%doc %{_datadir}/doc/%{name}/COPYING.ipmimonitoring
%doc %{_datadir}/doc/%{name}/COPYING.pstdout
%doc %{_datadir}/doc/%{name}/COPYING.ipmidetect
%doc %{_datadir}/doc/%{name}/COPYING.ipmi-fru
%doc %{_datadir}/doc/%{name}/COPYING.ipmi-dcmi
%doc %{_datadir}/doc/%{name}/COPYING.sunbmc
%doc %{_datadir}/doc/%{name}/COPYING.ZRESEARCH
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmiping
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmipower
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmiconsole
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmimonitoring
%doc %{_datadir}/doc/%{name}/DISCLAIMER.pstdout
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmidetect
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmi-fru
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmi-dcmi
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmiping.UC
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmipower.UC
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmiconsole.UC
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmimonitoring.UC
%doc %{_datadir}/doc/%{name}/DISCLAIMER.pstdout.UC
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmidetect.UC
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmi-fru.UC
%doc %{_datadir}/doc/%{name}/freeipmi-coding.txt
%doc %{_datadir}/doc/%{name}/freeipmi-design.txt
%doc %{_datadir}/doc/%{name}/freeipmi-hostrange.txt
%doc %{_datadir}/doc/%{name}/freeipmi-libraries.txt
%doc %{_datadir}/doc/%{name}/freeipmi-bugs-issues-and-workarounds.txt
%doc %{_datadir}/doc/%{name}/freeipmi-testing.txt
%doc %{_datadir}/doc/%{name}/freeipmi-oem-documentation-requirements.txt
%dir %{_datadir}/doc/%{name}
%dir %{_datadir}/doc/%{name}/contrib
%dir %{_datadir}/doc/%{name}/contrib/ganglia
%doc %{_datadir}/doc/%{name}/contrib/ganglia/*
%dir %{_datadir}/doc/%{name}/contrib/nagios
%doc %{_datadir}/doc/%{name}/contrib/nagios/*
%dir %{_datadir}/doc/%{name}/contrib/pet
%doc %{_datadir}/doc/%{name}/contrib/pet/*
%{_libdir}/libipmiconsole*so.*
%{_libdir}/libfreeipmi*so.*
%{_libdir}/libipmidetect*so.*
%{_libdir}/libipmimonitoring.so.*
%{_localstatedir}/lib/*
%{_sbindir}/bmc-config
%{_sbindir}/bmc-info
%{_sbindir}/bmc-device
%{_sbindir}/ipmi-config
%{_sbindir}/ipmi-fru
%{_sbindir}/ipmi-locate
%{_sbindir}/ipmi-oem
%{_sbindir}/ipmi-pef-config
%{_sbindir}/pef-config
%{_sbindir}/ipmi-raw
%{_sbindir}/ipmi-sel
%{_sbindir}/ipmi-sensors
%{_sbindir}/ipmi-sensors-config
%{_sbindir}/ipmiping
%{_sbindir}/ipmi-ping
%{_sbindir}/ipmipower
%{_sbindir}/ipmi-power
%{_sbindir}/rmcpping
%{_sbindir}/rmcp-ping
%{_sbindir}/ipmiconsole
%{_sbindir}/ipmi-console
%{_sbindir}/ipmimonitoring
%{_sbindir}/ipmi-chassis
%{_sbindir}/ipmi-chassis-config
%{_sbindir}/ipmi-dcmi
%{_sbindir}/ipmi-pet
%{_sbindir}/ipmidetect
%{_sbindir}/ipmi-detect
%{_mandir}/man8/bmc-config.8*
%{_mandir}/man5/bmc-config.conf.5*
%{_mandir}/man8/bmc-info.8*
%{_mandir}/man8/bmc-device.8*
%{_mandir}/man8/ipmi-config.8*
%{_mandir}/man5/ipmi-config.conf.5*
%{_mandir}/man8/ipmi-fru.8*
%{_mandir}/man8/ipmi-locate.8*
%{_mandir}/man8/ipmi-oem.8*
%{_mandir}/man8/ipmi-pef-config.8*
%{_mandir}/man8/pef-config.8*
%{_mandir}/man8/ipmi-raw.8*
%{_mandir}/man8/ipmi-sel.8*
%{_mandir}/man8/ipmi-sensors.8*
%{_mandir}/man8/ipmi-sensors-config.8*
%{_mandir}/man8/ipmiping.8*
%{_mandir}/man8/ipmi-ping.8*
%{_mandir}/man8/ipmipower.8*
%{_mandir}/man8/ipmi-power.8*
%{_mandir}/man5/ipmipower.conf.5*
%{_mandir}/man8/rmcpping.8*
%{_mandir}/man8/rmcp-ping.8*
%{_mandir}/man8/ipmiconsole.8*
%{_mandir}/man8/ipmi-console.8*
%{_mandir}/man5/ipmiconsole.conf.5*
%{_mandir}/man8/ipmimonitoring.8*
%{_mandir}/man5/ipmi_monitoring_sensors.conf.5*
%{_mandir}/man5/ipmimonitoring_sensors.conf.5*
%{_mandir}/man5/ipmimonitoring.conf.5*
%{_mandir}/man5/freeipmi_interpret_sel.conf.5*
%{_mandir}/man5/freeipmi_interpret_sensor.conf.5*
%{_mandir}/man5/libipmimonitoring.conf.5*
%{_mandir}/man8/ipmi-chassis.8*
%{_mandir}/man8/ipmi-chassis-config.8*
%{_mandir}/man8/ipmi-dcmi.8*
%{_mandir}/man8/ipmi-pet.8*
%{_mandir}/man8/ipmidetect.8*
%{_mandir}/man8/ipmi-detect.8*
%{_mandir}/man5/freeipmi.conf.5*
%{_mandir}/man5/ipmidetect.conf.5*
%{_mandir}/man5/libipmiconsole.conf.5*
%{_mandir}/man7/freeipmi.7*
%dir %{_localstatedir}/cache/ipmimonitoringsdrcache

%files devel
%dir %{_datadir}/doc/%{name}/contrib/libipmimonitoring
%doc %{_datadir}/doc/%{name}/contrib/libipmimonitoring/*
%{_libdir}/libipmiconsole.so
%{_libdir}/libfreeipmi.so
%{_libdir}/libipmidetect.so
%{_libdir}/libipmimonitoring.so
%dir %{_includedir}/freeipmi
%dir %{_includedir}/freeipmi/api
%dir %{_includedir}/freeipmi/cmds
%dir %{_includedir}/freeipmi/debug
%dir %{_includedir}/freeipmi/driver
%dir %{_includedir}/freeipmi/fiid
%dir %{_includedir}/freeipmi/fru
%dir %{_includedir}/freeipmi/interface
%dir %{_includedir}/freeipmi/interpret
%dir %{_includedir}/freeipmi/locate
%dir %{_includedir}/freeipmi/payload
%dir %{_includedir}/freeipmi/record-format
%dir %{_includedir}/freeipmi/record-format/oem
%dir %{_includedir}/freeipmi/sdr
%dir %{_includedir}/freeipmi/sdr/oem
%dir %{_includedir}/freeipmi/sel
%dir %{_includedir}/freeipmi/sensor-read
%dir %{_includedir}/freeipmi/spec
%dir %{_includedir}/freeipmi/spec/oem
%dir %{_includedir}/freeipmi/templates
%dir %{_includedir}/freeipmi/templates/oem
%dir %{_includedir}/freeipmi/util
%{_includedir}/ipmiconsole.h
%{_includedir}/ipmidetect.h
%{_includedir}/ipmi_monitoring*.h
%{_includedir}/freeipmi/*.h
%{_includedir}/freeipmi/api/*.h
%{_includedir}/freeipmi/cmds/*.h
%{_includedir}/freeipmi/debug/*.h
%{_includedir}/freeipmi/driver/*.h
%{_includedir}/freeipmi/fiid/*.h
%{_includedir}/freeipmi/fru/*.h
%{_includedir}/freeipmi/interface/*.h
%{_includedir}/freeipmi/interpret/*.h
%{_includedir}/freeipmi/locate/*.h
%{_includedir}/freeipmi/payload/*.h
%{_includedir}/freeipmi/record-format/*.h
%{_includedir}/freeipmi/record-format/oem/*.h
%{_includedir}/freeipmi/sdr/*.h
%{_includedir}/freeipmi/sdr/oem/*.h
%{_includedir}/freeipmi/sel/*.h
%{_includedir}/freeipmi/sensor-read/*.h
%{_includedir}/freeipmi/spec/*.h
%{_includedir}/freeipmi/spec/oem/*.h
%{_includedir}/freeipmi/templates/*.h
%{_includedir}/freeipmi/templates/oem/*.h
%{_includedir}/freeipmi/util/*.h
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*

%files bmc-watchdog
%doc %{_datadir}/doc/%{name}/COPYING.bmc-watchdog
%doc %{_datadir}/doc/%{name}/DISCLAIMER.bmc-watchdog
%doc %{_datadir}/doc/%{name}/DISCLAIMER.bmc-watchdog.UC
%config(noreplace) %{_sysconfdir}/sysconfig/bmc-watchdog
%{_sbindir}/bmc-watchdog
%{_mandir}/man8/bmc-watchdog.8*
%{_unitdir}/bmc-watchdog.service

%files ipmidetectd
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/ipmidetectd.conf
%{_sbindir}/ipmidetectd
%{_mandir}/man5/ipmidetectd.conf.5*
%{_mandir}/man8/ipmidetectd.8*
%{_unitdir}/ipmidetectd.service

%files ipmiseld
%doc %{_datadir}/doc/%{name}/COPYING.ipmiseld
%doc %{_datadir}/doc/%{name}/DISCLAIMER.ipmiseld
%{_unitdir}/ipmiseld.service
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/ipmiseld.conf
%{_sbindir}/ipmiseld
%{_mandir}/man5/ipmiseld.conf.5*
%{_mandir}/man8/ipmiseld.8*
%dir %{_localstatedir}/cache/ipmiseld

%changelog
%autochangelog
