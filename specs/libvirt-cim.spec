# -*- rpm-spec -*-

Summary: A CIM provider for libvirt
Name: libvirt-cim
Version: 0.6.3
Release: 26%{?dist}%{?extra_release}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Source: libvirt-cim-%{version}.tar.gz

# Update configure for aarch64 (bz #925923)
Patch1: libvirt-cim-aarch64.patch
URL: http://libvirt.org/CIM/
Requires: libxml2 >= 2.6.0
Requires: libvirt >= 0.9.0
Requires: unzip
# either tog-pegasus or sblim-sfcb should provide cim-server
Requires: cim-server
BuildRequires: make
BuildRequires:  gcc
BuildRequires: libcmpiutil >= 0.5.4
BuildRequires: tog-pegasus-devel
BuildRequires: libvirt-devel >= 0.9.0

# In RHEL5 uuid-devel is provided by e2fsprogs
%if 0%{?el5}
BuildRequires: e2fsprogs-devel
%else
BuildRequires: libuuid-devel
BuildRequires: libconfig-devel
%endif

BuildRequires: libxml2-devel
BuildRequires: libcmpiutil-devel
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
BuildRequires: systemd-units
%endif
BuildConflicts: sblim-cmpi-devel

%description
Libvirt-cim is a CMPI CIM provider that implements the DMTF SVPC
virtualization model. The goal is to support most of the features
exported by libvirt itself, enabling management of multiple
platforms with a single provider.

%prep
%setup -q

# Update configure for aarch64 (bz #925923)
%patch -P1 -p1

%build
%configure --disable-werror
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/cmpi/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/cmpi/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libxkutil.so
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libvirt-cim-%{version}
mkdir -p $RPM_BUILD_ROOT/etc/ld.so.conf.d
echo %{_libdir}/cmpi > $RPM_BUILD_ROOT/etc/ld.so.conf.d/libvirt-cim.%{_arch}.conf
mkdir -p $RPM_BUILD_ROOT/etc/libvirt/cim

%pre
%define REGISTRATION %{_datadir}/%{name}/*.registration
%define SCHEMA %{_datadir}/%{name}/*.mof

%define INTEROP_REG %{_datadir}/%{name}/{RegisteredProfile,ElementConformsToProfile,ReferencedProfile}.registration
%define INTEROP_MOF %{_datadir}/%{name}/{ComputerSystem,HostSystem,RegisteredProfile,DiskPool,MemoryPool,NetPool,ProcessorPool,VSMigrationService,ElementConformsToProfile,ReferencedProfile,AllocationCapabilities}.mof

%define PGINTEROP_REG %{_datadir}/%{name}/{RegisteredProfile,ElementConformsToProfile,ReferencedProfile}.registration
%define PGINTEROP_MOF %{_datadir}/%{name}/{RegisteredProfile,ElementConformsToProfile,ReferencedProfile}.mof

%define CIMV2_REG %{_datadir}/%{name}/{HostedResourcePool,ElementCapabilities,HostedService,HostedDependency,ElementConformsToProfile,HostedAccessPoint}.registration
%define CIMV2_MOF %{_datadir}/%{name}/{HostedResourcePool,ElementCapabilities,HostedService,HostedDependency,RegisteredProfile,ComputerSystem,ElementConformsToProfile,HostedAccessPoint}.mof

# _If_ there is already a version of this installed, we must deregister
# the classes we plan to install in post, otherwise we may corrupt
# the pegasus repository.  This is convention in other provider packages
%{_datadir}/%{name}/provider-register.sh -d -t pegasus \
	-n root/virt \
	-r %{REGISTRATION} -m %{SCHEMA} >/dev/null 2>&1 || true

%post
/sbin/ldconfig

%{_datadir}/%{name}/install_base_schema.sh %{_datadir}/%{name}

%if 0%{?Fedora} >= 17 || 0%{?rhel} >= 7
    if [ "`systemctl is-active tog-pegasus.service`" = "active" ]
    then
        systemctl restart tog-pegasus.service
    fi

    if [ "`systemctl is-active sblim-sfcb.service`" = "active" ]
    then
        systemctl restart sblim-sfcb.service
    fi
%else
    /etc/init.d/tog-pegasus condrestart
%endif

if [ -x /usr/sbin/cimserver ]
then
%{_datadir}/%{name}/provider-register.sh -t pegasus \
	-n root/virt \
	-r %{REGISTRATION} -m %{SCHEMA} >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -t pegasus \
        -n root/virt \
        -r %{REGISTRATION} -m %{SCHEMA} >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -t pegasus \
        -n root/interop \
        -r %{INTEROP_REG} -m %{INTEROP_MOF} -v >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -t pegasus \
        -n root/PG_InterOp \
        -r %{PGINTEROP_REG} -m %{PGINTEROP_MOF} -v >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -t pegasus \
        -n root/cimv2\
        -r %{CIMV2_REG} -m %{CIMV2_MOF} -v >/dev/null 2>&1 || true
fi
if [ -x /usr/sbin/sfcbd ]
then
%{_datadir}/%{name}/provider-register.sh -t sfcb \
	-n root/virt \
	-r %{REGISTRATION} -m %{SCHEMA} >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -t sfcb \
        -n root/virt \
        -r %{REGISTRATION} -m %{SCHEMA} >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -t sfcb \
        -n root/interop \
        -r %{INTEROP_REG} -m %{INTEROP_MOF} -v >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -t sfcb \
        -n root/PG_InterOp \
        -r %{PGINTEROP_REG} -m %{PGINTEROP_MOF} -v >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -t sfcb \
        -n root/cimv2\
        -r %{CIMV2_REG} -m %{CIMV2_MOF} -v >/dev/null 2>&1 || true
fi

%preun
if [ -x /usr/sbin/cimserver ]
then
%{_datadir}/%{name}/provider-register.sh -d -t pegasus \
	-n root/virt \
	-r %{REGISTRATION} -m %{SCHEMA} >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -d -t pegasus \
	-n root/interop \
	-r %{INTEROP_REG} -m %{INTEROP_MOF} >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -d -t pegasus \
	-n root/PG_InterOp \
	-r %{PGINTEROP_REG} -m %{PGINTEROP_MOF} >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -d -t pegasus \
	-n root/cimv2 \
	-r %{CIMV2_REG} -m %{CIMV2_MOF} >/dev/null 2>&1 || true
fi
if [ -x /usr/sbin/sfcbd ]
then
%{_datadir}/%{name}/provider-register.sh -d -t sfcb \
	-n root/virt \
	-r %{REGISTRATION} -m %{SCHEMA} >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -d -t sfcb \
	-n root/interop \
	-r %{INTEROP_REG} -m %{INTEROP_MOF} >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -d -t sfcb \
	-n root/PG_InterOp \
	-r %{PGINTEROP_REG} -m %{PGINTEROP_MOF} >/dev/null 2>&1 || true
%{_datadir}/%{name}/provider-register.sh -d -t sfcb \
	-n root/cimv2 \
	-r %{CIMV2_REG} -m %{CIMV2_MOF} >/dev/null 2>&1 || true
fi

%postun -p /sbin/ldconfig

%files
%{_sysconfdir}/libvirt/cim

%doc README COPYING doc/CodingStyle doc/SubmittingPatches
%doc base_schema/README.DMTF
%doc doc/*.html
%{_libdir}/lib*.so*
%{_libdir}/cmpi/lib*.so*
%{_datadir}/libvirt-cim
%{_datadir}/libvirt-cim/*.sh
%{_datadir}/libvirt-cim/*.mof
%{_datadir}/libvirt-cim/cimv*-interop_mof
%{_datadir}/libvirt-cim/cimv*-cimv2_mof
%{_datadir}/libvirt-cim/*.registration
%{_datadir}/libvirt-cim/cim_schema_*-MOFs.zip
%{_sysconfdir}/ld.so.conf.d/libvirt-cim.%{_arch}.conf
%config(noreplace) %{_sysconfdir}/libvirt-cim.conf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.3-25
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 0.6.3-11
- Rebuild for new libconfig

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jul 25 2013 Daniel Veillard <veillard@redhat.com> 0.6.3-1
- update to 0.6.3 release

* Fri Jun 28 2013 Cole Robinson <crobinso@redhat.com> - 0.6.2-2
- Update configure for aarch64 (bz #925923)

* Mon Apr 15 2013 Daniel Veillard <veillard@redhat.com> 0.6.2-1
- update to 0.6.2 release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 12 2012 Daniel Veillard <veillard@redhat.com> - 0.6.1-2
- fix build in the presence of sblim-sfcb
- add schemas (de)registration with sfcb if found

* Mon Mar  5 2012 Daniel Veillard <veillard@redhat.com> - 0.6.1-1
- update to upstream release 0.6.1
- allow to use tog-pegasus or sblimfscb
- switch for systemctl for conditional restart of the server

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Daniel Veillard <veillard@redhat.com> - 0.5.14-1
- update to upstream release 0.5.14

* Wed Jul  6 2011 Daniel Veillard <veillard@redhat.com> - 0.5.13-1
- update to upstream release 0.5.13

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 07 2009 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.8-2
- Add missing namespace unreg bits for root/interop, root/cimv2 
- Remove additional reg call of root/virt from postinstall 
- Do not use /etc directly.  Use sysconfigdir instead
- Remove additional DESTDIR definition
- Fix Xen migration URI to not include 'system'
- Change net->name to net->source

* Wed Dec 02 2009 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.8-1
- Updated to latest upstream source

* Mon Oct 05 2009 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.7-1
- Updated to latest upstream source

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.6-1
- Updated to latest upstream source

* Tue Apr 21 2009 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.5-1
- Updated to latest upstream source

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.4-1
- Updated to latest upstream source

* Thu Jan 15 2009 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.3-1
- Updated to latest upstream source

* Mon Oct 06 2008 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.2-1
- Updated to latest upstream source

* Tue Sep 23 2008 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.1-5
- Added vsmigser_schema patch to remove dup method name from VSMigrationService
- Added mem_parse patch to set proper mem max_size and mem values
- Added mig_prof_ver patch to report the proper Migration Profile version
- Added hyp_conn_fail patch to fix when not connecting to hyp returns a failure
- Added rm_def_virtdev patch to remove default DiskRADSD virtual device
- Added rm_eafp_err patch to remove error status when EAFP no pool link exists
- Added sdc_unsup patch to make SDC not return unsup for RASD to AC case

* Wed Aug 27 2008 Kaitlin Rupert <kaitlin@us.ibm.com> - 0.5.1-4
- Added nostate patch to consider XenFV no state guests as running guests
- Added createsnap_override patch to add vendor defined values to CreateSnapshot
- Added add_shutdown_rsc patch to add support for shutdown operation
- Added vsmc_add_remove patch to expose Add/Remove resources via VSMC
- Added override_refconf patch to fix dup devs where ID matches refconf dev ID

* Thu Aug 07 2008 Dan Smith <danms@us.ibm.com> - 0.5.1-3
- Added infostore_trunc patch to fix infostore corruption
- Added vsss_paramname patch to fix VSSS parameter name
- Added vsss_logic patch to fix terminal memory snapshot logic
- Added /etc/libvirt/cim directory for infostore

* Thu Jul 31 2008 Dan Smith <danms@us.ibm.com> - 0.5.1-1
- Updated to latest upstream source

* Tue Jun 03 2008 Dan Smith <danms@us.ibm.com> - 0.5-1
- Updated to latest upstream source

* Fri May 30 2008 Dan Smith <danms@us.ibm.com> - 0.4-2
- Fixed schema registration to pick up ECTP in root/virt properly
- Fixed schema registration to include ReferencedProfile in interop
- Added RASD namespace fix

* Wed May 21 2008 Dan Smith <danms@us.ibm.com> - 0.4-1
- Updated to latest upstream source
- Added default disk pool configuration patch

* Fri Mar 14 2008 Dan Smith <danms@us.ibm.com> - 0.3-4
- Fixed loader config for 64-bit systems
- Added missing root/interop schema install
- Added RegisteredProfile.registration to install

* Fri Mar 07 2008 Dan Smith <danms@us.ibm.com> - 0.3-2
- Added KVM method enablement patch

* Mon Mar 03 2008 Dan Smith <danms@us.ibm.com> - 0.3-1
- Updated to latest upstream source

* Wed Feb 13 2008 Dan Smith <danms@us.ibm.com> - 0.2-1
- Updated to latest upstream source

* Thu Jan 17 2008 Dan Smith <danms@us.ibm.com> - 0.1-8
- Add ld.so.conf.d configuration

* Mon Jan 14 2008 Dan Smith <danms@us.ibm.com> - 0.1-7
- Update to offical upstream release
- Patch source to fix parallel make issue until fixed upstream

* Mon Jan 07 2008 Dan Smith <danms@us.ibm.com> - 0.1-3
- Remove RPATH on provider modules

* Mon Jan 07 2008 Dan Smith <danms@us.ibm.com> - 0.1-2
- Cleaned up Release
- Removed unnecessary Requires
- After install, condrestart pegasus
- Updated to latest source snapshot

* Fri Oct 26 2007 Daniel Veillard <veillard@redhat.com> - 0.1-1
- created
