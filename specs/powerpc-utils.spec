Name:           powerpc-utils
Version:        1.3.13
Release:        2%{?dist}
Summary:        PERL-based scripts for maintaining and servicing PowerPC systems

License:        GPL-2.0-only
URL:            https://github.com/ibm-power-utilities/powerpc-utils
Source0:        https://github.com/ibm-power-utilities/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        nx-gzip.udev
Patch0:         powerpc-utils-1.3.11-manpages.patch

ExclusiveArch:  ppc %{power64}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  zlib-devel
BuildRequires:  librtas-devel >= 1.4.0
BuildRequires:  libservicelog-devel >= 1.0.1-2
BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires:  numactl-devel

# rtas_dump explicit dependency
Requires:       perl(Data::Dumper)
Requires:       %{name}-core = %{version}-%{release}

%description
PERL-based scripts for maintaining and servicing PowerPC systems.


%package core
Summary: Core utilities for maintaining and servicing PowerPC systems
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: kmod
Requires: which
Requires: /usr/bin/awk
Requires: /usr/bin/basename
Requires: /usr/bin/bc
Requires: /usr/bin/cat
Requires: /usr/bin/cut
Requires: /usr/bin/echo
Requires: /usr/bin/find
Requires: /bin/grep
Requires: /usr/bin/head
Requires: /usr/bin/ls
Requires: /usr/bin/sed
Requires: /usr/bin/tr
Requires: /usr/bin/udevadm

# udev rule move
Conflicts: libnxz < 0.63-3

%description core
Core utilities for maintaining and servicing PowerPC systems.


%prep
%autosetup -p1

%build
./autogen.sh
%configure --with-systemd=%{_unitdir} --disable-werror
make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT FILES= RCSCRIPTS=

#define pkgdocdir {_datadir}/doc/{name}-{version}
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# move doc files
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}
install $RPM_BUILD_ROOT/usr/share/doc/packages/powerpc-utils/* -t $RPM_BUILD_ROOT%{_pkgdocdir}
rm -rf $RPM_BUILD_ROOT/usr/share/doc/packages/powerpc-utils
rm -f $RPM_BUILD_ROOT%{_pkgdocdir}/COPYING

# install udev rule for the nx-gzip accelerator
install -pDm 644  %{SOURCE1}  %{buildroot}%{_udevrulesdir}/90-nx-gzip.rules

# remove init script and perl script. They are deprecated
rm -rf $RPM_BUILD_ROOT/etc/init.d/ibmvscsis.sh $RPM_BUILD_ROOT/usr/sbin/vscsisadmin

# symlink uspchrp
ln -s serv_config %{buildroot}%{_sbindir}/uspchrp
ln -s serv_config.8 %{buildroot}%{_mandir}/man8/uspchrp.8

# deprecated, use sosreport instead
rm -f $RPM_BUILD_ROOT%{_sbindir}/snap $RPM_BUILD_ROOT%{_mandir}/man8/snap.8*

# drop needless stuffs
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/powerpc-utils

# keep service name
mv $RPM_BUILD_ROOT%{_unitdir}/hcn-init-NetworkManager.service $RPM_BUILD_ROOT%{_unitdir}/hcn-init.service

%post core
%systemd_post hcn-init.service
# update the smt.state file with current SMT
/usr/sbin/smtstate --save >/dev/null 2>&1 || :

%preun core
%systemd_preun smtstate.service
%systemd_preun hcn-init.service

%postun core
%systemd_postun_with_restart smtstate.service
%systemd_postun_with_restart hcn-init.service 

%posttrans core
systemctl enable hcn-init.service >/dev/null 2>&1 || :

%files
# PERL-based scripts for maintaining and servicing PowerPC systems
%doc README Changelog
%license COPYING
%{_sbindir}/hvcsadmin
%{_sbindir}/rtas_dump
%{_mandir}/man8/hvcsadmin.8*
%{_mandir}/man8/rtas_dump.8*

%files core
%doc README Changelog
%license COPYING
%dir %{_localstatedir}/lib/powerpc-utils
%config(noreplace) %{_localstatedir}/lib/powerpc-utils/smt.state
%{_unitdir}/smtstate.service
%{_unitdir}/smt_off.service
%{_unitdir}/hcn-init.service
%if 0%{?wicked}
%{_unitdir}/hcn-init-wicked.service
%else
%exclude %{_unitdir}/hcn-init-wicked.service
%endif
%{_bindir}/amsstat
%{_sbindir}/activate_firmware
%{_sbindir}/bootlist
%{_sbindir}/errinjct
%{_sbindir}/lparstat
%{_sbindir}/lsdevinfo
%{_sbindir}/lsprop
%{_sbindir}/lsslot
%{_sbindir}/ls-vdev
%{_sbindir}/ls-veth
%{_sbindir}/ls-vscsi
%{_sbindir}/nvsetenv
%{_sbindir}/ppc64_cpu
%{_sbindir}/rtas_dbg
%{_sbindir}/rtas_event_decode
%{_sbindir}/rtas_ibm_get_vpd
%{_sbindir}/serv_config
%{_sbindir}/set_poweron_time
%{_sbindir}/sys_ident
%{_sbindir}/uesensor
%{_sbindir}/update_flash
%{_sbindir}/update_flash_nv
%{_sbindir}/uspchrp
%{_sbindir}/hcncfgdrc
%{_sbindir}/hcnmgr
%{_sbindir}/hcnqrydev
%{_sbindir}/hcnrmdev
%{_sbindir}/hcnrmhcn
%{_sbindir}/hcnversion
%{_sbindir}/vcpustat
%{_sbindir}/smtstate
%{_sbindir}/nvram
%{_sbindir}/ofpathname
%{_sbindir}/pseries_platform
%{_sbindir}/drmgr
%{_sbindir}/lparnumascore
%{_udevrulesdir}/90-nx-gzip.rules
%{_mandir}/man1/amsstat.1*
%{_mandir}/man5/lparcfg.5*
%{_mandir}/man8/activate_firmware.8*
%{_mandir}/man8/bootlist.8*
%{_mandir}/man8/errinjct.8*
%{_mandir}/man8/lparstat.8*
%{_mandir}/man8/lsdevinfo.8*
%{_mandir}/man8/lsprop.8*
%{_mandir}/man8/lsslot.8*
%{_mandir}/man8/ls-vdev.8*
%{_mandir}/man8/ls-veth.8*
%{_mandir}/man8/ls-vscsi.8*
%{_mandir}/man8/nvsetenv.8*
%{_mandir}/man8/ppc64_cpu.8*
%{_mandir}/man8/rtas_dbg.8*
%{_mandir}/man8/rtas_event_decode.8*
%{_mandir}/man8/rtas_ibm_get_vpd.8*
%{_mandir}/man8/serv_config.8*
%{_mandir}/man8/set_poweron_time.8*
%{_mandir}/man8/sys_ident.8*
%{_mandir}/man8/uesensor.8*
%{_mandir}/man8/update_flash.8*
%{_mandir}/man8/pseries_platform.8*
%{_mandir}/man8/update_flash_nv.8*
%{_mandir}/man8/uspchrp.8*
%{_mandir}/man8/vcpustat.8.gz
%{_mandir}/man8/smtstate.8.gz
%{_mandir}/man8/hcnmgr.8*
%{_mandir}/man8/nvram.8*
%{_mandir}/man8/ofpathname.8*
%{_mandir}/man8/drmgr.8*
%{_mandir}/man8/drmgr-hooks.8*
%{_mandir}/man8/lparnumascore.8*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 20 2024 Than Ngo <than@redhat.com> - 1.3.13-1
- Update to 1.3.13

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 07 2024 Than Ngo <than@redhat.com> - 1.3.12-2
- conditionally hcn-init-wicked.service

* Fri Apr 05 2024 Than Ngo <than@redhat.com> - 1.3.12-1
- update to 1.3.12

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 01 2023 Than Ngo <than@redhat.com> - 1.3.11-4
- Fix negative values seen while running lpar
- Fix lparstat error with mixed SMT state
- Fix negative values seen while running lparstat with -E option

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 16 2023 Than Ngo <than@redhat.com> - 1.3.11-2
- migrated to SPDX license

* Tue Jan 24 2023 Than Ngo <than@redhat.com> - 1.3.11-1
- update to 1.3.11

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 02 2022 Than Ngo <than@redhat.com> - 1.3.10-5
- Fix lsslot -c mem output when using 4GB LMB size
- Add NVMf-FC boot support for Power

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Jakub Čajka <jcajka@redhat.com> - 1.3.10-3
- Add udev rule for the nx-gzip in to the core subpackage

* Wed Jun 08 2022 Than Ngo <than@redhat.com> - 1.3.10-2
- install smt.state as config file
- drop nvsetenv which is included in upstream

* Fri Jun 03 2022 Than Ngo <than@redhat.com> - 1.3.10-1
- update to 1.3.10

* Thu May 12 2022 Than Ngo <than@redhat.com> - 1.3.9-6
- fix smtstate test failure, add default SMT_VALUE=1 in smt.state

* Tue Feb 08 2022 Than Ngo <than@redhat.com> - 1.3.9-5
- santize devspec output of a newline if one is present
- fixed invalid hex number (multipath)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Than Ngo <than@redhat.com> - 1.3.9-3
- enable support vnic as backend for HNV interface
- fixed hexdump format
- switch to systemd macros in scriptlets
- marked smt.state as %%ghost

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Than Ngo <than@redhat.com> - 1.3.9-1
- Rebase to 1.3.9

* Mon May 31 2021 Than Ngo <than@redhat.com> - 1.3.8-9
- Resolves: #1935658, New lparstat -x option to report the security flavor
- Resolves: #1938420, rebase patch fix_boot-time_bonding_interface_cleanup_and_avoid_use_ifcfg
- Resolves: #1940358, ppc64_cpu --help does not list --version as an option
- Resolves: #1951068, take care of NUMA topology when removing memory (DLPAR)

* Mon May 03 2021 Than Ngo <than@redhat.com> - 1.3.8-8
- Use od instead xxd

* Mon Feb 08 2021 Than Ngo <than@redhat.com> - 1.3.8-7
- updated hcnmgr manpage

* Mon Feb 08 2021 Than Ngo <than@redhat.com> - 1.3.8-6
- Fix boot-time bonding interface cleanup and avoid use ifcfg

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Than Ngo <than@redhat.com> - 1.3.8-4
- additional patches to support Linux Hybrid Network Virtualization
- move commands that dont depend on perl to core subpackage
- update hcnmgr patch
- sys_ident: Skip length field from search
- ofpathname: Use NVMe controller physical nsid

* Thu Oct 01 2020 Than Ngo <than@redhat.com> - 1.3.8-3
- add hcnmgr man page

* Thu Oct 01 2020 Than Ngo <than@redhat.com> - 1.3.8-2
- clean up systemd service 

* Fri Sep 04 2020 Than Ngo <than@redhat.com> - 1.3.8-1
- update to 1.3.8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Than Ngo <than@redhat.com> - 1.3.7-6
- Track and expose idle PURR and SPURR ticks
- ofpathname: speed up l2of_scsi()
- ofpathname: failed to boot
- update lparstat man page with -E option
- enable support for ibm,drc-info property

* Sat Mar 28 2020 Than Ngo <than@redhat.com> - 1.3.7-5
- move drmgr in core to avoid pulling in Perl

* Mon Mar 09 2020 Than Ngo <than@redhat.com> - 1.3.7-4
- update_flash_nv: fixup null byte command substitution warning
- drmgr: Fix segfault when running 'drmgr -c pmig -h'

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Than Ngo <than@redhat.com> - 1.3.7-2
- add systemd service to set default system SMT mode

* Wed Dec 18 2019 Than Ngo <than@redhat.com> - 1.3.7-1
- update to 1.3.7 

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Than Ngo <than@redhat.com> - 1.3.6-1
- update to 1.3.6

* Fri Nov 30 2018 Than Ngo <than@redhat.com> - 1.3.5-4
- install missing pseries_platform and update_flash_nv man pages

* Thu Nov 29 2018 Than Ngo <than@redhat.com> - 1.3.5-3
- added pseries_platform and update_flash_nv man pages

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Dan Horák <dan[at]danny.cz> - 1.3.5-1
- Rebased to 1.3.5

* Tue Apr 17 2018 Dan Horák <dan[at]danny.cz> - 1.3.4-4
- fix deps for perl-based tools
- spec cleanup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Stephen Gallagher <sgallagh@redhat.com> - 1.3.4-2
- Fix grep dependency

* Tue Oct 10 2017 Dan Horák <dan[at]danny.cz> - 1.3.4-1
- Rebased to 1.3.4

* Tue Oct 10 2017 Stephen Gallagher <sgallagh@redhat.com> - 1.3.3-4
- Split critical components into powerpc-utils-core (#1463749)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.3.3-1
- Update to latest upstream 1.3.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.1-1
- Update to latest upstream 1.3.1
- Use %%license
- Drop requires on optional powerpc-utils-python so as not to pull in X stack
- Package cleanups
- Obsolete/Provide powerpc-utils-papr

* Sat Apr  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.0-2
- Rebuild for librtas soname bump

* Thu Feb 18 2016 Rafael Fonseca <rdossant@redhat.com> - 1.3.0-1
- Update to latest upstream 1.3.0
- Update upstream URL.
- Change license to GPL.
- Remove deprecated patch.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.27-2
- Fix build warnings

* Mon Nov 16 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.27
- Update to latest upstream 1.2.27

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 06 2015 Jakub Čajka <jcajka@redhat.com> - 1.2.24-1
- Update to latest upstream 1.2.24
- ppc64le fix
- removed snap, sosreport from sos should be used instead

* Mon Nov 03 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.23
- Update to latest upstream 1.2.23

* Mon Sep 22 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.22-2
- Fix makefile issue

* Mon Sep 22 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.22
- Update to latest upstream 1.2.22

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Jakub Čajka <jcajka@redhat.com> - 1.2.20-2
- Spec file clean up

* Mon Apr 14 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.20
- Update to latest upstream 1.2.20

* Wed Mar 05 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.19
- Update to latest upstream 1.2.19

* Thu Oct 10 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.18-2
- Add ppc64le architecture

* Thu Oct 10 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.18
- Update to latest upstream 1.2.18

* Sun Sep 15 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.17-2
- Fix docdir (#998579)

* Tue Aug 20 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.17
- Update to latest upstream 1.2.17

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Tony Breeds <tony@bakeyournoodle.com> - 1.2.16-2
- drmgr: Check for rpadlpar_io module
- resolves: #972606

* Tue May 21 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.2.16
- Update to latest upstream 1.2.16

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Karsten Hopp <karsten@redhat.com> 1.2.15-1
- update to 1.2.15
- usysident/usysattn got moved to ppc64-diag package
- multipath ofpathname patch removed as it is upstream now

* Tue Dec 18 2012 Filip Kocina <fkocina@redhat.com> 1.2.14-1
- Resolves: #859222 - updated to latest upstream 1.2.14

* Thu Dec 13 2012 Karsten Hopp <karsten@redhat.com> 1.2.12-4
- Add multipath support to ofpathname for bug #884826

* Tue Sep 04 2012 Karsten Hopp <karsten@redhat.com> 1.2.12-3
- require powerpc-utils-python (#852326 comment 7)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Jiri Skala <jskala@redhat.com> - 1.2.12-1
- updated to latest upstream 1.2.12

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 03 2011 Jiri Skala <jskala@redhat.com> - 1.2.11-2
- updated dependecy

* Mon Oct 31 2011 Jiri Skala <jskala@redhat.com> - 1.2.11-1
- updated to latest upstream 1.2.11
-fixes #749892 - powerpc-utils spec file missing dependency

* Fri Aug 05 2011 Jiri Skala <jskala@redhat.com> - 1.2.10-1
- updated to latest upstream 1.2.10

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Jiri Skala <jskala@redhat.com> - 1.2.6-1
- updated to latest upstream 1.2.6
- removed amsvis man page (amsvis moved to powerpc-utils-python)
- added lparcfg man page - doc to /proc/ppc64/lparcfg

* Thu Jun 24 2010 Roman Rakus <rrakus@redhat.com> - 1.2.2-14
- Compile with -fno-strict-aliasing CFLAG
- linked nvsetenv man page to nvram man page
- Updated man page of ofpathname
- Updated amsstat script

* Tue Jun 15 2010 Roman Rakus <rrakus@redhat.com> - 1.2.2-11
- Correct the parameter handling of ppc64_cpu when setting the run-mode

* Wed Jun 09 2010 Roman Rakus <rrakus@redhat.com> - 1.2.2-10
- Added some upstream patches
- also bump release

* Wed Jun 02 2010 Roman Rakus <rrakus@redhat.com> - 1.2.2-4
- correct the parameter checking when attempting to set the run mode
- also bump release

* Fri Mar 05 2010 Roman Rakus <rrakus@redhat.com> - 1.2.2-2
- Removed deprecated init script and perl script

* Thu Oct 29 2009 Stepan Kasal <skasal@redhat.com> - 1.2.2-1
- new upstream version
- amsvis removed, this package has no longer anything with python
- change the manual pages in the file list so that it does not depend on
  particular compression used
- add patch for configure.ac on platforms with autoconf < 2.63
- use standard %%configure/make in %%build

* Mon Aug 17 2009 Roman Rakus <rrakus@redhat.com> - 1.2.0-1
- Bump tu version 1.2.0 - powerpc-utils and powerpc-utils-papr get merged

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 06 2009 Roman Rakus <rrakus@redhat.com> - 1.1.3-1
- new upstream version 1.1.3

* Tue Mar 03 2009 Roman Rakus <rrakus@redhat.com> - 1.1.2-1
- new upstream version 1.1.2

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Roman Rakus <rrakus@redhat.com> - 1.1.1-1
- new upstream version 1.1.1

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.6-3
- Autorebuild for GCC 4.3

* Mon Dec  3 2007 David Woodhouse <dwmw2@redhat.com> 1.0.6-2
- Add --version to nvsetenv, for ybin compatibility

* Fri Nov 23 2007 David Woodhouse <dwmw2@redhat.com> 1.0.6-1
- New package, split from ppc64-utils
