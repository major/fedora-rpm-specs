Name:           ppc64-diag
Version:        2.7.10
Release:        2%{?dist}
Summary:        PowerLinux Platform Diagnostics
URL:            https://github.com/power-ras/%{name}
License:        GPL-2.0-only
ExclusiveArch:  ppc %{power64}
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libservicelog-devel
BuildRequires:  flex
BuildRequires:  perl-interpreter
BuildRequires:  byacc
BuildRequires:  libvpd-devel >= 2.2.9
BuildRequires:  ncurses-devel
BuildRequires:  librtas-devel >= 1.4.0
BuildRequires:  systemd-units
BuildRequires:  systemd-devel
BuildRequires:  libtool
BuildRequires:  bison

Requires:       ppc64-diag-rtas >= 2.7.6
Requires:       servicelog
Requires:       lsvpd
Requires:       powerpc-utils >= 1.3.0

Source0:        https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        add_regex.8
Source2:        convert_dt_node_props.8
Source3:        extract_opal_dump.8
Source4:        extract_platdump.8
Source5:        rtas_errd.8

# fix paths and permissions
Patch0:         ppc64-diag-2.7.9-fedora.patch
# Upstream fixes
# Add Power11 support for diag_nvme
Patch10:        ppc64-diag-2.7.0-diag_vnme-add-power11-support.patch

%description
This package contains various diagnostic tools for PowerLinux.
These tools captures the diagnostic events from Power Systems
platform firmware, SES enclosures and device drivers, and
write events to servicelog database. It also provides automated
responses to urgent events such as environmental conditions and
predictive failures, if appropriate modifies the FRUs fault
indicator(s) and provides event notification to system
administrators or connected service frameworks.

%package        rtas
Summary:        rtas_errd daemon
# PCI hotplug support on PowerKVM guest depends on below powerpc-utils version.
Requires:       powerpc-utils-core >= 1.3.7-5

%description rtas
This package contains only rtas_errd daemon.

%prep
%autosetup -p1

%build
./autogen.sh
CXXFLAGS="-std=gnu++14 %{build_cflags}" %configure
LDFLAGS="%{build_ldflags}" CFLAGS="%{build_cflags}" CXXFLAGS="-std=gnu++14 %{build_cflags}" make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT
chmod 644 COPYING
rm -f $RPM_BUILD_ROOT%{_docdir}/ppc64-diag/*
mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/ses_pages
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/log/dump
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/log/opal-elog
ln -sfv %{_sbindir}/usysattn $RPM_BUILD_ROOT/%{_sbindir}/usysfault
install -m 644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} $RPM_BUILD_ROOT/%{_mandir}/man8/

%files
%license COPYING
%doc README.md
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/ses_pages
%dir %{_localstatedir}/log/%{name}/diag_disk
%dir %{_localstatedir}/log/dump
%dir %{_localstatedir}/log/opal-elog
%{_mandir}/man8/*
%{_sbindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/message_catalog/
%{_libexecdir}/%{name}/ppc64_diag_migrate
%{_libexecdir}/%{name}/ppc64_diag_mkrsrc
%{_libexecdir}/%{name}/ppc64_diag_notify
%{_libexecdir}/%{name}/ppc64_diag_setup
%{_libexecdir}/%{name}/lp_diag_setup
%{_libexecdir}/%{name}/lp_diag_notify
%{_libexecdir}/%{name}/servevent_parse.pl
%{_datadir}/%{name}/message_catalog/*
%{_unitdir}/opal_errd.service
%{_sysconfdir}/cron.daily/run_diag_encl
%{_sysconfdir}/cron.daily/run_diag_nvme

# get rid of obsolete initscripts for rhel >=7
%exclude %{_libexecdir}/%{name}/rtas_errd
%exclude %{_libexecdir}/%{name}/opal_errd

# exclude stuffs which are moved to rtas
%exclude %{_mandir}/man8/convert_dt_node_props*
%exclude %{_mandir}/man8/extract_platdump*
%exclude %{_mandir}/man8/rtas_errd*
%exclude %{_sbindir}/convert_dt_node_props
%exclude %{_sbindir}/extract_platdump
%exclude %{_sbindir}/rtas_errd

%files rtas
%license COPYING
%dir %{_sysconfdir}/%{name}
%{_mandir}/man8/convert_dt_node_props*
%{_mandir}/man8/extract_platdump*
%{_mandir}/man8/rtas_errd*
%config(noreplace) %{_sysconfdir}/%{name}/ppc64-diag.config
%config(noreplace) %{_sysconfdir}/%{name}/diag_nvme.config
%{_sbindir}/convert_dt_node_props
%{_sbindir}/extract_platdump
%{_sbindir}/rtas_errd
%{_sysconfdir}/rc.powerfail
%{_unitdir}/rtas_errd.service

%post
# Post-install script --------------------------------------------------
%{_libexecdir}/%{name}/lp_diag_setup --register >/dev/null 2>&1
%{_libexecdir}/%{name}/ppc64_diag_setup --register >/dev/null 2>&1
if [ "$1" = "1" ]; then # first install
    systemctl -q enable opal_errd.service >/dev/null
    systemctl start opal_errd.service >/dev/null
elif [ "$1" = "2" ]; then # upgrade
    systemctl restart opal_errd.service >/dev/null
    systemctl daemon-reload > /dev/null 2>&1
fi

%preun
# Pre-uninstall script -------------------------------------------------
if [ "$1" = "0" ]; then # last uninstall
    systemctl stop opal_errd.service >/dev/null
    systemctl -q disable opal_errd.service
    %{_libexecdir}/%{name}/ppc64_diag_setup --unregister >/dev/null
    %{_libexecdir}/%{name}/lp_diag_setup --unregister >/dev/null
    systemctl daemon-reload > /dev/null 2>&1
fi

%triggerin -- librtas
# trigger on librtas upgrades ------------------------------------------
if [ "$2" = "2" ]; then
    systemctl restart opal_errd.service >/dev/null
    systemctl restart rtas_errd.service >/dev/null
fi

 
%post rtas
if [ "$1" = "1" ]; then # first install
    systemctl -q enable rtas_errd.service >/dev/null
    systemctl start rtas_errd.service >/dev/null
elif [ "$1" = "2" ]; then # upgrade
    systemctl restart rtas_errd.service >/dev/null
    systemctl daemon-reload > /dev/null 2>&1
fi

%preun rtas
if [ "$1" = "0" ]; then # last uninstall
    systemctl stop rtas_errd.service >/dev/null
    systemctl -q disable rtas_errd.service
    systemctl daemon-reload > /dev/null 2>&1
fi

%changelog
* Thu Jan 02 2025 Than Ngo <than@redhat.com> - 2.7.10-2
- Add Power11 support for diag_nvme

* Sun Oct 27 2024 Than Ngo <than@redhat.com> - 2.7.10-1
- Update to 2.7.10
  * Aadd support for multiple platform dumps
  * Add support for light path diagnostics for rtas events
  * Enable correct display of model and system-id for IPS Power systems
  * Fix call home feature for nvmf devices
  * Fix crash in rtas_errd due to invalid -f option values
  * Fix build warnings with GCC-15

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 16 2023 Than Ngo <than@redhat.com> - 2.7.9-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 18 2022 Than Ngo <than@redhat.com> - 2.7.9-1
- update to 2.7.9
- added BR on libvpd >= 2.2.9

* Thu Jul 28 2022 Than Ngo <than@redhat.com> - 2.7.8-4
- Fixed FTBFS, error: format not a string literal

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 14 2022 Than Ngo <than@redhat.com> - 2.7.8-2
- opal-dump-parse -h should return 0

* Thu Apr 07 2022 Dan Horák <dan[at]danny.cz> - 2.7.8-1
- rebase to 2.7.8

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Than Ngo <than@redhat.com> - 2.7.6-10
- Standard output type syslog is obsolete

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Jeff Law <law@redhat.com> - 2.7.6-8
- Force C++14 for configure step too

* Tue Oct 27 2020 Jeff Law <law@redhat.com> - 2.7.6-7
- Force C++14 mode as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Than Ngo <than@redhat.com> - 2.7.6-5
- add requirement on powerpc-utils in main package

* Sat Mar 28 2020 Than Ngo <than@redhat.com> - 2.7.6-4
- create rtas subpackage to avoid the perl dependency

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Than Ngo <than@redhat.com> - 2.7.6-2
- Update Url and Source

* Wed Nov 27 2019 Than Ngo <than@redhat.com> - 2.7.6-1
- rebase to 2.7.6
- update Url

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.7.5-1
- Update to latest upstream 2.7.5

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Dan Horák <dan[at]danny.cz> - 2.7.4-2
- fix condition for rtas_errd service (#1575638)

* Fri Mar 09 2018 Than Ngo <than@redhat.com> - 2.7.4-1
- update to latest upstream 2.7.4

* Wed Mar 07 2018 Than Ngo <than@redhat.com> - 2.7.1-6
- fixed bz#1552653 - ppc64-diag: Missing Fedora build flags injection

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 9 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.7.1-1
- Update to latest upstream 2.7.1

* Sat Apr  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.7.0-2
- Rebuild for librtas soname bump
- Use %%license

* Mon Mar 21 2016 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.7.0-1
- Update to latest upstream 2.7.0
- Change license to GPLv2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.10
- Update to latest upstream 2.6.10

* Tue Aug  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.6.7-4
- Make the build verbase as per packaging standards

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 25 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.7-2
- Update dependency list

* Thu Sep 25 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.7
- Update to latest upstream 2.6.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.6
- Update to latest upstream 2.6.6

* Wed Apr 02 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.5
- Update to latest upstream 2.6.5

* Fri Mar 21 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.4
- Update to latest upstream 2.6.4

* Fri Mar 07 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.3
- Update to latest upstream 2.6.3

* Thu Oct 10 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.2-3
- Add ppc64le architecture

* Sun Sep 15 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.2-2
- Fix minor build issue.
- Fix PRRN hotplug script location issue

* Wed Aug 21 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.2
- Update to latest upstream 2.6.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.1-2
- Add ncurses-devel as build dependency
- Fix script location issue

* Mon May 20 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.6.1
- Update to latest upstream 2.6.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Karsten Hopp <karsten@redhat.com> 2.4.3-6
- revert permissions fix, filter requirement instead

* Mon Sep 24 2012 karsten Hopp <karsten@redhat.com> 2.4.3-4
- fix permissions of servevent_parse.pl

* Fri Jul 27 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 2.4.3-3
- rename .service file
- auto start rtas_errd (#843471)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 Karsten Hopp <karsten@redhat.com> 2.4.3-1
- update to 2.4.3

* Wed Feb 15 2012 Karsten Hopp <karsten@redhat.com> 2.4.2-5
- don't strip binaries
- fix some build issues

* Thu Sep 22 2011 Karsten Hopp <karsten@redhat.com> 2.4.2-4
- fix preun and post install scriptlets

* Fri Sep 09 2011 Karsten Hopp <karsten@redhat.com> 2.4.2-3
- add buildrequirement systemd-units for _unitdir rpm macro
- move helper scripts to libexecdir/ppc64-diag

* Wed Sep 07 2011 Karsten Hopp <karsten@redhat.com> 2.4.2-2       
- additional fixes for Fedora package review (bugzilla #736062)

* Wed Aug 17 2011 Karsten Hopp <karsten@redhat.com> 2.4.2-1
- initial Fedora version, based on IBM spec file with rpmlint cleanups
  - move scripts to /usr/share/ppc-diag
  - don't start service automatically after install
