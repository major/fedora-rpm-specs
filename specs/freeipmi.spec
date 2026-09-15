Name:             freeipmi
Version:          1.6.19
Release:          %autorelease
Summary:          IPMI remote console and system management software
License:          GPL-3.0-or-later
URL:              https://www.gnu.org/software/freeipmi/
Source0:          https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:          bmc-watchdog.service
Source2:          ipmidetectd.service
Source3:          ipmiseld.service
Source4:          freeipmi.tmpfiles.conf
Source5:          freeipmi-ipmiseld.tmpfiles.conf
BuildRequires:    libgcrypt-devel texinfo systemd-rpm-macros
BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    automake
BuildRequires:    autoconf
BuildRequires:    libtool

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

# Install tmpfiles configs
install -m0644 -D %{SOURCE4} %{buildroot}%{_tmpfilesdir}/freeipmi.conf
install -m0644 -D %{SOURCE5} %{buildroot}%{_tmpfilesdir}/freeipmi-ipmiseld.conf

# Remove initscripts
rm -frv %{buildroot}%{_initrddir} %{buildroot}%{_sysconfdir}/init.d

# Remove useless generic INSTALL
rm -frv %{buildroot}%{_pkgdocdir}/INSTALL

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



%files
%dir %{_sysconfdir}/freeipmi/
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/freeipmi.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/ipmidetect.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/freeipmi_interpret_sel.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/freeipmi_interpret_sensor.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/libipmiconsole.conf
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/ChangeLog.0
%doc %{_pkgdocdir}/NEWS
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/README.argp
%doc %{_pkgdocdir}/README.build
%doc %{_pkgdocdir}/README.openipmi
%doc %{_pkgdocdir}/TODO
%doc %{_pkgdocdir}/freeipmi-coding.txt
%doc %{_pkgdocdir}/freeipmi-design.txt
%doc %{_pkgdocdir}/freeipmi-hostrange.txt
%doc %{_pkgdocdir}/freeipmi-libraries.txt
%doc %{_pkgdocdir}/freeipmi-bugs-issues-and-workarounds.txt
%doc %{_pkgdocdir}/freeipmi-testing.txt
%doc %{_pkgdocdir}/freeipmi-oem-documentation-requirements.txt
%license %{_pkgdocdir}/COPYING
%license %{_pkgdocdir}/COPYING.ipmiping
%license %{_pkgdocdir}/COPYING.ipmipower
%license %{_pkgdocdir}/COPYING.ipmiconsole
%license %{_pkgdocdir}/COPYING.ipmimonitoring
%license %{_pkgdocdir}/COPYING.pstdout
%license %{_pkgdocdir}/COPYING.ipmidetect
%license %{_pkgdocdir}/COPYING.ipmi-fru
%license %{_pkgdocdir}/COPYING.ipmi-dcmi
%license %{_pkgdocdir}/COPYING.sunbmc
%license %{_pkgdocdir}/COPYING.ZRESEARCH
%license %{_pkgdocdir}/DISCLAIMER.ipmiping
%license %{_pkgdocdir}/DISCLAIMER.ipmipower
%license %{_pkgdocdir}/DISCLAIMER.ipmiconsole
%license %{_pkgdocdir}/DISCLAIMER.ipmimonitoring
%license %{_pkgdocdir}/DISCLAIMER.pstdout
%license %{_pkgdocdir}/DISCLAIMER.ipmidetect
%license %{_pkgdocdir}/DISCLAIMER.ipmi-fru
%license %{_pkgdocdir}/DISCLAIMER.ipmi-dcmi
%license %{_pkgdocdir}/DISCLAIMER.ipmiping.UC
%license %{_pkgdocdir}/DISCLAIMER.ipmipower.UC
%license %{_pkgdocdir}/DISCLAIMER.ipmiconsole.UC
%license %{_pkgdocdir}/DISCLAIMER.ipmimonitoring.UC
%license %{_pkgdocdir}/DISCLAIMER.pstdout.UC
%license %{_pkgdocdir}/DISCLAIMER.ipmidetect.UC
%license %{_pkgdocdir}/DISCLAIMER.ipmi-fru.UC
%{_infodir}/freeipmi-faq.info*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/contrib
%{_pkgdocdir}/contrib/ganglia
%{_pkgdocdir}/contrib/nagios
%{_pkgdocdir}/contrib/pet
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
%{_tmpfilesdir}/freeipmi.conf

%files devel
%{_pkgdocdir}/contrib/libipmimonitoring
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
%license %{_pkgdocdir}/COPYING.bmc-watchdog
%license %{_pkgdocdir}/DISCLAIMER.bmc-watchdog
%license %{_pkgdocdir}/DISCLAIMER.bmc-watchdog.UC
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
%license %{_pkgdocdir}/COPYING.ipmiseld
%license %{_pkgdocdir}/DISCLAIMER.ipmiseld
%{_unitdir}/ipmiseld.service
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/freeipmi/ipmiseld.conf
%{_sbindir}/ipmiseld
%{_mandir}/man5/ipmiseld.conf.5*
%{_mandir}/man8/ipmiseld.8*
%dir %{_localstatedir}/cache/ipmiseld
%{_tmpfilesdir}/freeipmi-ipmiseld.conf

%changelog
%autochangelog
