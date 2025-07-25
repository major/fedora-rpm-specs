# pywbem is not included in RHEL
%bcond smis %{undefined rhel}
# disabled by default
%bcond test 0

Name:           libstoragemgmt
Version:        1.10.2
Release:        5%{?dist}
Summary:        Storage array management library
License:        LGPL-2.1-or-later
URL:            https://github.com/libstorage/libstoragemgmt
Source0:        https://github.com/libstorage/libstoragemgmt/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch1:         0001_systemd_ug.patch
Patch2:         0002_include_integration_script.patch
Requires:       python3-%{name}%{_isa}
Requires:       ledmon-libs

# Packages that have been removed
Obsoletes:      %{name}-netapp-plugin <= 1.6.2-10
Provides:       %{name}-netapp-plugin <= 1.6.2-10
Obsoletes:      %{name}-nstor-plugin <= 1.9.0-1
Provides:       %{name}-nstor-plugin <= 1.9.0-1

BuildRequires:  gcc gcc-c++
BuildRequires:  autoconf automake libtool check-devel perl-interpreter
BuildRequires:  glib2-devel
BuildRequires:  systemd
BuildRequires:  bash-completion
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  libconfig-devel
BuildRequires:  systemd-devel
BuildRequires:  procps
BuildRequires:  sqlite-devel
BuildRequires:  python3-six
BuildRequires:  python3-devel
BuildRequires:  ledmon-devel

%{?systemd_requires}
BuildRequires:  systemd systemd-devel

BuildRequires:  chrpath
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
The libStorageMgmt library will provide a vendor agnostic open source storage
application programming interface (API) that will allow management of storage
arrays.  The library includes a command line interface for interactive use and
scripting (command lsmcli).  The library also has a daemon that is used for
executing plug-ins in a separate process (lsmd).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n python3-%{name}
Summary:        Python 3 client libraries and plug-in support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-six

# If obsoleted packages are installed, we need to meet it's requirement
# of having the correct version of this package functionality installed too as
# the update occurs first, before the obsolete removes the obsoleted package.
Provides:       python2-%{name}-clibs <= 1.9.0-1
Obsoletes:      python2-%{name}-clibs <= 1.9.0-1

Provides:       python3-%{name}-clibs <= 1.9.0-1
Obsoletes:      python3-%{name}-clibs <= 1.9.0-1

%{?python_provide:%python_provide python3-%{name}}

%description    -n python3-%{name}
This contains python 3 client libraries as well as python framework
support and open source plug-ins written in python 3.

%if %{with smis}
%package        smis-plugin
Summary:        Files for SMI-S generic array support for %{name}
BuildRequires:  python3-pywbem
BuildRequires: make
Requires:       python3-pywbem
BuildArch:      noarch
Provides:       %{name}-ibm-v7k-plugin <= 2:1.9.3-4
Obsoletes:      %{name}-ibm-v7k-plugin <= 2:0.1.0-3
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}


%description    smis-plugin
The %{name}-smis-plugin package contains plug-in for generic SMI-S array
support.
%endif

%package        targetd-plugin
Summary:        Files for targetd array support for %{name}
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    targetd-plugin
The %{name}-targetd-plugin package contains plug-in for targetd array
support.

%package        udev
Summary:        Udev files for %{name}

%description    udev
The %{name}-udev package contains udev rules and helper utilities for
uevents generated by the kernel.

%package        megaraid-plugin
Summary:        Files for LSI MegaRAID support for %{name}
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    megaraid-plugin
The %{name}-megaraid-plugin package contains the plugin for LSI
MegaRAID storage management via storcli.

%package        hpsa-plugin
Summary:        Files for HP SmartArray support for %{name}
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    hpsa-plugin
The %{name}-hpsa-plugin package contains the plugin for HP
SmartArray storage management via hpssacli.

%package        arcconf-plugin
Summary:        Files for Microsemi Adaptec and Smart Family support for %{name}
Requires:       python3-%{name} = %{version}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    arcconf-plugin
The %{name}-arcconf-plugin package contains the plugin for Microsemi
Adaptec RAID and Smart Family Controller storage management.

%package        nfs-plugin
Summary:        Files for NFS local filesystem support for %{name}
Requires:       python3-%{name} = %{version}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nfs-utils
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}

%description    nfs-plugin
The nfs-plugin package contains plug-in for local NFS exports support.

%package        local-plugin
Summary:        Files for local pseudo plugin of %{name}
Requires:       python3-%{name} = %{version}
Requires:       %{name}-arcconf-plugin = %{version}-%{release}
Requires:       %{name}-hpsa-plugin = %{version}-%{release}
Requires(post): python3-%{name} = %{version}
Requires(postun): python3-%{name} = %{version}
BuildArch:      noarch

%description    local-plugin
The %{name}-local-plugin is a plugin that provides auto
plugin selection for locally managed storage.

%prep
%autosetup -p1

%build
./autogen.sh

%configure \
    --with-python3 \
%ifnarch %{valgrind_arches}
    --without-mem-leak-test \
%endif
    --disable-static %{!?with_smis:--without-smispy}
%make_build

%install
rm -rf %{buildroot}

%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

#Files for udev handling
mkdir -p %{buildroot}/%{_udevrulesdir}
install -m 644 tools/udev/90-scsi-ua.rules \
    %{buildroot}/%{_udevrulesdir}/90-scsi-ua.rules
install -m 755 tools/udev/scan-scsi-target \
    %{buildroot}/%{_udevrulesdir}/../scan-scsi-target

%if 0%{with test}
%check
if ! make check
then
  cat test-suite.log || true
  exit 1
fi

%endif

%pre

%post
/sbin/ldconfig
# Create tmp socket folders.
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
/sbin/ldconfig
%systemd_postun %{name}.service

%if %{with smis}
# Need to restart lsmd if plugin is new installed or removed.
%post smis-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%postun smis-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi
%endif

# Need to restart lsmd if plugin is new installed or removed.
%post targetd-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%postun targetd-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

# Need to restart lsmd if plugin is new installed or removed.
%post megaraid-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi
%postun megaraid-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

# Need to restart lsmd if plugin is new installed or removed.
%post hpsa-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi
%postun hpsa-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

# Need to restart lsmd if plugin is new installed or removed.
%post arcconf-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi
%postun arcconf-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

# Need to restart lsmd if plugin is new installed or removed.
%post nfs-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi
%postun nfs-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

# Need to restart lsmd if plugin is new installed or removed.
%post local-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi
%postun local-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%files
%doc README COPYING.LIB NEWS
%{_mandir}/man1/lsmcli.1*
%{_mandir}/man1/lsmd.1*
%{_mandir}/man5/lsmd.conf.5*
%{_libdir}/*.so.*
%{_bindir}/lsmcli
%{_datadir}/bash-completion/completions/lsmcli
%{_bindir}/lsmd
%{_bindir}/simc_lsmplugin
%dir %{_sysconfdir}/lsm
%dir %{_sysconfdir}/lsm/pluginconf.d
%config(noreplace) %{_sysconfdir}/lsm/lsmd.conf
%{_mandir}/man1/simc_lsmplugin.1*

%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf

%ghost %dir %attr(0775, root, libstoragemgmt) /run/lsm/
%ghost %dir %attr(0775, root, libstoragemgmt) /run/lsm/ipc

%attr(0644, root, root) %{_tmpfilesdir}/%{name}.conf

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/lsm_*
%{_mandir}/man3/libstoragemgmt*

%files -n python3-%{name}
%dir %{python3_sitearch}/lsm
%{python3_sitearch}/lsm/__init__.*
%{python3_sitearch}/lsm/_client.*
%{python3_sitearch}/lsm/_common.*
%{python3_sitearch}/lsm/_local_disk.*
%{python3_sitearch}/lsm/_data.*
%{python3_sitearch}/lsm/_iplugin.*
%{python3_sitearch}/lsm/_pluginrunner.*
%{python3_sitearch}/lsm/_transport.*
%{python3_sitearch}/lsm/__pycache__/
%{python3_sitearch}/lsm/version.*
%dir %{python3_sitearch}/lsm/lsmcli
%{python3_sitearch}/lsm/lsmcli/__init__.*
%{python3_sitearch}/lsm/lsmcli/__pycache__/
%{python3_sitearch}/lsm/lsmcli/data_display.*
%{python3_sitearch}/lsm/lsmcli/cmdline.*
%{python3_sitearch}/lsm/_clib.*

%dir %{python3_sitearch}/sim_plugin
%{python3_sitearch}/sim_plugin/__pycache__/
%{python3_sitearch}/sim_plugin/__init__.*
%{python3_sitearch}/sim_plugin/simulator.*
%{python3_sitearch}/sim_plugin/simarray.*

%{_bindir}/sim_lsmplugin
%dir %{_libexecdir}/lsm.d
%{_libexecdir}/lsm.d/find_unused_lun.py*
%{_libexecdir}/lsm.d/local_check.py*
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/sim.conf
%{_mandir}/man1/sim_lsmplugin.1*

%if %{with smis}
%files smis-plugin
%dir %{python3_sitelib}/smispy_plugin
%dir %{python3_sitelib}/smispy_plugin/__pycache__
%{python3_sitelib}/smispy_plugin/__pycache__/*
%{python3_sitelib}/smispy_plugin/__init__.*
%{python3_sitelib}/smispy_plugin/smis.*
%{python3_sitelib}/smispy_plugin/dmtf.*
%{python3_sitelib}/smispy_plugin/utils.*
%{python3_sitelib}/smispy_plugin/smis_common.*
%{python3_sitelib}/smispy_plugin/smis_cap.*
%{python3_sitelib}/smispy_plugin/smis_sys.*
%{python3_sitelib}/smispy_plugin/smis_pool.*
%{python3_sitelib}/smispy_plugin/smis_disk.*
%{python3_sitelib}/smispy_plugin/smis_vol.*
%{python3_sitelib}/smispy_plugin/smis_ag.*
%{_bindir}/smispy_lsmplugin
%{_mandir}/man1/smispy_lsmplugin.1*
%endif

%files targetd-plugin
%dir %{python3_sitelib}/targetd_plugin
%dir %{python3_sitelib}/targetd_plugin/__pycache__
%{python3_sitelib}/targetd_plugin/__pycache__/*
%{python3_sitelib}/targetd_plugin/__init__.*
%{python3_sitelib}/targetd_plugin/targetd.*
%{_bindir}/targetd_lsmplugin
%{_mandir}/man1/targetd_lsmplugin.1*

%files udev
%{_udevrulesdir}/../scan-scsi-target
%{_udevrulesdir}/90-scsi-ua.rules

%files megaraid-plugin
%dir %{python3_sitelib}/megaraid_plugin
%dir %{python3_sitelib}/megaraid_plugin/__pycache__
%{python3_sitelib}/megaraid_plugin/__pycache__/*
%{python3_sitelib}/megaraid_plugin/__init__.*
%{python3_sitelib}/megaraid_plugin/megaraid.*
%{python3_sitelib}/megaraid_plugin/utils.*
%{_bindir}/megaraid_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/megaraid.conf
%{_mandir}/man1/megaraid_lsmplugin.1*

%files hpsa-plugin
%dir %{python3_sitelib}/hpsa_plugin
%dir %{python3_sitelib}/hpsa_plugin/__pycache__
%{python3_sitelib}/hpsa_plugin/__pycache__/*
%{python3_sitelib}/hpsa_plugin/__init__.*
%{python3_sitelib}/hpsa_plugin/hpsa.*
%{python3_sitelib}/hpsa_plugin/utils.*
%{_bindir}/hpsa_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/hpsa.conf
%{_mandir}/man1/hpsa_lsmplugin.1*

%files nfs-plugin
%dir %{python3_sitearch}/nfs_plugin
%dir %{python3_sitearch}/nfs_plugin/__pycache__
%{python3_sitearch}/nfs_plugin/__pycache__/*
%{python3_sitearch}/nfs_plugin/__init__.*
%{python3_sitearch}/nfs_plugin/nfs.*
%{python3_sitearch}/nfs_plugin/nfs_clib.*
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/nfs.conf
%{_bindir}/nfs_lsmplugin
%{_mandir}/man1/nfs_lsmplugin.1*

%files arcconf-plugin
%dir %{python3_sitelib}/arcconf_plugin
%dir %{python3_sitelib}/arcconf_plugin/__pycache__
%{python3_sitelib}/arcconf_plugin/__pycache__/*
%{python3_sitelib}/arcconf_plugin/__init__.*
%{python3_sitelib}/arcconf_plugin/arcconf.*
%{python3_sitelib}/arcconf_plugin/utils.*
%{_bindir}/arcconf_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/arcconf.conf
%{_mandir}/man1/arcconf_lsmplugin.1*

%files local-plugin
%dir %{python3_sitelib}/local_plugin
%dir %{python3_sitelib}/local_plugin/__pycache__
%{python3_sitelib}/local_plugin/__pycache__/*
%{python3_sitelib}/local_plugin/__init__.*
%{python3_sitelib}/local_plugin/local.*
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/local.conf
%{_bindir}/local_lsmplugin
%{_mandir}/man1/local_lsmplugin.1*

%changelog
* Thu Jul 24 2025 Tony Asleson <tasleson@redhat.com> - 1.10.2-5
- Convert to tmt testing

* Wed Jun 11 2025 Tony Asleson <tasleson@redhat.com> - 1.10.2-4
- Fix for https://bugzilla.redhat.com/show_bug.cgi?id=2371736

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.10.2-3
- Rebuilt for Python 3.14

* Wed Mar 05 2025 David Abdurachmanov <davidlt@rivosinc.com> - 1.10.2-2
- Properly check valgrind arches

* Thu Jan 23 2025 Tony Asleson <tasleson@redhat.com> - 1.10.2-1
- Upgrade to 1.10.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.10.1-3
- Disable smis-plugin subpackage on RHEL

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Tony Asleson <tasleson@redhat.com> - 1.10.1-1
- Upgrade to 1.10.1

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.10.0-3
- Rebuilt for Python 3.13

* Mon May 13 2024 Tony Asleson <tasleson@redhat.com> - 1.10.0-2
- Exclude i686 build

* Mon May 13 2024 Tony Asleson <tasleson@redhat.com> - 1.10.0-1
- Upgrade to 1.10.0

* Wed Apr 3 2024 Tony Asleson <tasleson@redhat.com> - 1.9.8-7
- Fix for https://bugzilla.redhat.com/show_bug.cgi?id=1457164

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Tony Asleson <tasleson@redhat.com> - 1.9.8-4
- migrated to SPDX license

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.9.8-2
- Rebuilt for Python 3.12

* Mon Apr 17 2023 Tony Asleson <tasleson@redhat.com> - 1.9.8-1
- Upgrade to 1.9.8

* Mon Feb 20 2023 Tony Asleson <tasleson@redhat.com> - 1.9.7-1
- Upgrade to 1.9.7

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 11 2022 Tony Asleson <tasleson@redhat.com> - 1.9.6-2
- Rebuild

* Thu Nov 10 2022 Tony Asleson <tasleson@redhat.com> - 1.9.6-1
- Upgrade to 1.9.6

* Mon Oct 17 2022 Tony Asleson <tasleson@redhat.com> - 1.9.5-1
- Upgrade to 1.9.5

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Tony Asleson <tasleson@redhat.com> - 1.9.4-4
- Use systemd-sysusers

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.9.4-3
- Rebuilt for Python 3.11

* Thu Apr 7 2022 Tony Asleson <tasleson@redhat.com> - 1.9.4-2
- Fix failure to build on i386

* Thu Apr 7 2022 Tony Asleson <tasleson@redhat.com> - 1.9.4-1
- Upgrade to 1.9.4

* Wed Jan 26 2022 Tony Asleson <tasleson@redhat.com> - 1.9.3-3
- Remove -Werror for build due to bug, see: https://gcc.gnu.org/PR104213

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 17 2021 Tony Asleson <tasleson@redhat.com> - 1.9.3-1
- Upgrade to 1.9.3
- Add requirements for local plugin

* Mon Aug 9 2021 Tony Asleson <tasleson@redhat.com> - 1.9.2-4
- Add missing requirement for python six library

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.2-2
- Rebuilt for Python 3.10

* Mon May 17 2021 Tony Asleson <tasleson@redhat.com> - 1.9.2-1
- Upgrade to 1.9.2

* Tue Apr 20 2021 Tony Asleson <tasleson@redhat.com> - 1.9.1-1
- Upgrade to 1.9.1

* Thu Mar 25 2021 Tony Asleson <tasleson@redhat.com> - 1.9.0-1
- Upgrade to 1.9.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Tony Asleson <tasleson@redhat.com> - 1.8.8-2
- Disable test

* Tue Dec 15 2020 Tony Asleson <tasleson@redhat.com> - 1.8.8-1
- Upgrade to 1.8.8 which removes a couple of plugins and reorg.
  the plugin install directories.

* Thu Dec 3 2020 Tony Asleson <tasleson@redhat.com> - 1.8.7-1
- Upgrade to 1.8.7

* Mon Nov 2 2020 Tony Asleson <tasleson@redhat.com> - 1.8.6-1
- Upgrade to 1.8.6

* Thu Oct 1 2020 Tony Asleson <tasleson@redhat.com> - 1.8.5-3
- Remove pywbem version check as its not needed and breaks
  now that epoch is used in it.

* Fri Sep 4 2020 Tony Asleson <tasleson@redhat.com> - 1.8.5-2
- Fix test compile error for i386

* Tue Aug 11 2020 Tony Asleson <tasleson@redhat.com> - 1.8.5-1
- Upgrade to 1.8.5
- Fixes: https://bugzilla.redhat.com/show_bug.cgi?id=1864052

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 1.8.4-3
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.4-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Tony Asleson <tasleson@redhat.com> - 1.8.4-1
- Upgrade to 1.8.4

* Wed Feb 12 2020 Tony Asleson <tasleson@redhat.com> - 1.8.3-1
- Upgrade to 1.8.3

* Mon Feb 10 2020 Tony Asleson <tasleson@redhat.com> - 1.8.2-3
- Correct python clib packages to include ISA for correct dependencies

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Tony Asleson <tasleson@redhat.com> - 1.8.2-1
- Upgrade to 1.8.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Tony Asleson <tasleson@redhat.com> - 1.8.0-1
- Upgrade to 1.8.0

* Mon Feb 18 2019 Tony Asleson <tasleson@redhat.com> - 1.7.3-1
- Upgrade to 1.7.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Tony Asleson <tasleson@redhat.com> - 1.7.2-1
- Upgrade to 1.7.2

* Tue Nov 6 2018 Tony Asleson <tasleson@redhat.com> - 1.7.1-1
- Upgrade to 1.7.1

* Wed Oct 31 2018 Tony Asleson <tasleson@redhat.com> - 1.7.0-1
- Upgrade to 1.7.0

* Tue Sep 18 2018 Gris Ge <fge@redhat.com> - 1.6.2-10
- Add explicit package version requirement to libstoragemgmt-nfs-plugin-clibs.

* Mon Sep 17 2018 Gris Ge <fge@redhat.com> - 1.6.2-9
- Fix the `rpm -V` failures. (RHBZ #1629735, the same issue also in Fedora)

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 1.6.2-8
- Rebuild for new libconfig

* Tue Jul 24 2018 Gris Ge <fge@redhat.com> - 1.6.2-7
- Add missing gcc gcc-c++ build requirements.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Gris Ge <fge@redhat.com> - 1.6.2-5
- Fix lscmli on python 3.7.

* Tue Jun 26 2018 Gris Ge <fge@redhat.com> - 1.6.2-4
- Rebuild again with --target=f29-python.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.2-3
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Gris Ge <fge@redhat.com> - 1.6.2-2
- Removed the requirement of initscripts. (RHBZ 1592363)

* Fri May 18 2018 Gris Ge <fge@redhat.com> - 1.6.2-1
- Upgrade to 1.6.2.

* Fri Mar 23 2018 Gris Ge <fge@redhat.com> - 1.6.1-7
- Fix incorect memset size.

* Fri Mar 23 2018 Gris Ge <fge@redhat.com> - 1.6.1-6
- Add ./autogen.sh back to fix the version diff on autotools.

* Fri Mar 23 2018 Gris Ge <fge@redhat.com> - 1.6.1-5
- Add missing rpm script for arcconf, nfs, local plugins.

* Thu Mar 22 2018 Gris Ge <fge@redhat.com> - 1.6.1-4
- Fix build on GCC 8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Lumír Balhar <lbalhar@redhat.com> - 1.6.1-2
- Fix directory ownership in python subpackages

* Tue Oct 31 2017 Gris Ge <fge@redhat.com> - 1.6.1-1
- Upgrade to 1.6.1

* Thu Oct 19 2017 Gris Ge <fge@redhat.com> - 1.6.0-1
- Upgrade to 1.6.0

* Sun Oct 15 2017 Gris Ge <fge@redhat.com> - 1.5.0-3
- Specify Python version in SPEC Requires.

* Wed Oct 11 2017 Gris Ge <fge@redhat.com> - 1.5.0-2
- Fix multilib confliction of nfs-plugin by move binrary file to
  another subpackage libstoragemgmt-nfs-plugin-clibs

* Tue Oct 10 2017 Gris Ge <fge@redhat.com> - 1.5.0-0
- New upstream release 1.5.0:
    * New sub-package libstoragemgmt-nfs-plugin, libstoragemgmt-arcconf-plugin,
      and libstoragemgmt-local-plugin.
    * C API manpages for libstoragemgmt-devel package.

* Tue Oct 3 2017 Tony Asleson <tasleson@redhat.com> - 1.4.0-5
- Remove m2crypto requirement

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.0-4
- Python 2 binary packages renamed to python2-libstoragemgmt and python2-libstoragemgmt-clibs
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3
- %%python_provide added for all four python subpackages

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild


* Tue Feb 21 2017 Gris Ge <fge@redhat.com> 1.4.0-1
- Add Python3 support.
- New sub rpm package python3-libstoragemgmt.
- Add support of lmiwbem(this rpm use pywbem instead).
- Allow plugin test to be run concurrently.
- Bug fixes:
    * Fix megaraid plugin for dell PERC.
    * Fix local disk rotation speed query on NVMe disk.
    * Fix lsmcli incorrect try-expect on local disk query.
    * Fix all the gcc compile warnings.
    * Fix the obsolete usage of AC_OUTPUT in configure.ac.
- Library adds:
    * Query serial of local disk:
        lsm_local_disk_serial_num_get()/lsm.LocalDisk.serial_num_get()
    * Query LED status of local disk:
        lsm_local_disk_led_status_get()/lsm.LocalDisk.led_status_get()
    * Query link speed of local disk:
        lsm_local_disk_link_speed_get()/lsm.LocalDisk.link_speed_get()

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Gris Ge <fge@redhat.com> 1.3.5-1
- New upstream release 1.3.5

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 18 2016 Tony Asleson <tasleson@redhat.com> 1.3.2-1
- New upstream release 1.3.2

* Fri May 13 2016 Tony Asleson <tasleson@redhat.com> 1.3.1-2
- Disable make check as we are hitting a valgrind memleak in ld.so
  on arm arch.

* Fri May 13 2016 Tony Asleson <tasleson@redhat.com> 1.3.1-1
- New upstream release 1.3.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 24 2015 Gris Ge <fge@redhat.com> 1.2.3-1
- New upstream release 1.2.3:
    * Bug fixes:
        * lsmcli bash completion: Fix syntax error.
        * lsmcli bash completion: Fix volume-delete.
        * lsmcli bash completion: Add missing completions.
        * Fix: selinux dac_override
        * Manpage: Update hpsa and megaraid plugin manpages.
        * HP Smart Array Plugin: Fix pool querying on P410i.
        * MegaRAID Plugin: Fix bug when no volume configured.

* Fri Jun 19 2015 Gris Ge <fge@redhat.com> - 1.2.1-1
- New upstream release 1.2.1.
- Changed upstream URL and source URL to github.
- New sub-pacakges:
    * libstoragemgmt-megaraid-plugin
        New plugin in 1.2.0 release.
    * libstoragemgmt-hpsa-plugin
        New plugin in 1.2.0 release.
- Add bash-completion script for lsmcli.
- New rpmbuild switch: 
    * '--without test'
        Use to skip 'make check' test to save debug time.
    * '--without megaraid'
        Don't compile megaraid plugin.
    * '--without hpsa'
        Don't compile hpsa plugin.
- Remove PyYAML BuildRequires.
- Add NEWS(changelog) to document folder.
- Replace the hardcoded udev path with <percent>{_udevrulesdir}.
- Fix rpmlint error 'dir-or-file-in-var-run'.
- Mark /run/lsm and /run/lsm/ipc as <percent>ghost folder.
- Fix rpmlint warnning 'W: non-standard-uid /run/lsm libstoragemgmt'.
- Add 'Requires(post)' and 'Requires(postun)' to plugins in order
  to make sure plugin is installed after libstoragemgmt and removed before
  libstoragemgmt.
- Fix the incorrect use of <percent>bcond_with and <percent>bcond_without.
- Removed autogen.sh which is not required for release version any more.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Fri Jan 16 2015 Tony Asleson <tasleson@redhat.com> 1.1.0-2
- Make updates work correctly for removed sub package
  libstoragemgmt-ibm-v7k-plugin

* Thu Dec 4 2014 Tony Asleson <tasleson@redhat.com> 1.1.0-1
- New upstream release
- Fix udev files directory
- Move command line files to python package

* Wed Oct 8 2014 Tony Asleson <tasleson@redhat.com> - 1.0.0-3
- Specify udev files to /usr/lib dir instead of /lib
- Move command line python files to python package

* Wed Oct 1 2014 Tony Asleson <tasleson@redhat.com> - 1.0.0-2
- BZ 850185, Use new systemd rpm macros
- BZ 1122117, Use correct tmpfiles.d dir

* Sun Sep 7 2014 Tony Asleson <tasleson@redhat.com> - 1.0.0-1
- New upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 3 2014 Tony Asleson <tasleson@redhat.com> - 0.1.0-1
- New upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 30 2014 Tony Asleson <tasleson@redhat.com> 0.0.24-1
- New upstream release

* Wed Nov 27 2013 Tony Asleson <tasleson@redhat.com> 0.0.23-1
- New upstream release

* Mon Aug 12 2013 Tony Asleson <tasleson@redhat.com> 0.0.22-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Tony Asleson <tasleson@redhat.com> 0.0.21-1
- New upstream release
- Put plug-ins in separate sub packages
- Don't include IBM plug-in on RHEL > 6, missing paramiko

* Tue May 28 2013 Tony Asleson <tasleson@redhat.com> - 0.0.20-1
- New upstream release
- Separate package for python libraries
- Make timestamps match on version.py in library
- Add python-paramiko requirement for IBM plug-in

* Mon Apr 22 2013 Tony Asleson <tasleson@redhat.com> - 0.0.19-1
- New upstream release

* Fri Mar 8 2013 Tony Asleson <tasleson@redhat.com> - 0.0.18-1
- New upstream release

* Thu Jan 31 2013 Tony Asleson <tasleson@redhat.com> - 0.0.17-1
- New upstream release

* Wed Jan 2 2013 Tony Asleson <tasleson@redhat.com> - 0.0.16-1
- New upstream release

* Tue Nov 27 2012 Tony Asleson <tasleson@redhat.com> - 0.0.15-1
- New upstream release

* Wed Oct 3 2012 Tony Asleson <tasleson@redhat.com> - 0.0.13-1
- New upstream release

* Tue Sep 18 2012 Tony Asleson <tasleson@redhat.com> - 0.0.12-1
- New upstream release

* Mon Aug 13 2012 Tony Asleson <tasleson@redhat.com> 0.0.11-1
- New upstream release

* Fri Jul 27 2012 Dan Horák <dan[at]danny.cz> - 0.0.9-3
- detect also non-x86 arches in Pegasus check

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Tony Asleson <tasleson@redhat.com> 0.0.9-1
- Initial checkin of lio plug-in
- System filtering via URI (smispy)
- Error code mapping (ontap)
- Fixed build so same build tarball is used for all binaries

* Mon Jun 4 2012 Tony Asleson <tasleson@redhat.com> 0.0.8-1
- Make building of SMI-S CPP plugin optional
- Add pkg-config file
- SMIS: Fix exception while retrieving Volumes
- SMIS: Fix exception while retrieving Volumes
- lsm: Add package imports
- Make Smis class available in lsm python package
- Add option to disable building C unit test
- Make simulator classes available in lsm python package
- Make ontap class available in lsm python package
- Changes to support building on Fedora 17 (v2)
- Spec. file updates from feedback from T. Callaway (spot)
- F17 linker symbol visibility correction
- Remove unneeded build dependencies and cleaned up some warnings
- C Updates, client C library feature parity with python

* Fri May 11 2012 Tony Asleson <tasleson@redhat.com> 0.0.7-1
- Bug fix for smi-s constants
- Display formatting improvements
- Added header option for lsmcli
- Improved version handling for builds
- Made terminology consistent
- Ability to list visibility for access groups and volumes
- Simulator plug-in fully supports all block operations
- Added support for multiple systems with a single plug-in instance

* Fri Apr 20 2012 Tony Asleson <tasleson@redhat.com> 0.0.6-1
- Documentation improvements (man & source code)
- Support for access groups
- Unified spec files Fedora/RHEL
- Package version auto generate
- Rpm target added to make
- Bug fix for missing optional property on volume retrieval (smispy plug-in)

* Fri Apr 6 2012 Tony Asleson <tasleson@redhat.com> 0.0.5-1
- Spec file clean-up improvements
- Async. operation added to lsmcli and ability to check on job status
- Sub volume replication support
- Ability to check for child dependencies on VOLUMES, FS and files
- SMI-S Bug fixes and improvements

* Mon Mar 26 2012 Tony Asleson <tasleson@redhat.com> 0.0.4-1
- Restore from snapshot
- Job identifiers string instead of integer
- Updated license address

* Wed Mar 14 2012 Tony Asleson <tasleson@redhat.com> 0.0.3-1
- Changes to installer, daemon uid, gid, /var/run/lsm/*
- NFS improvements and bug fixes
- Python library clean up (rpmlint errors)

* Sun Mar 11 2012 Tony Asleson <tasleson@redhat.com> 0.0.2-1
- Added NetApp native plugin

* Mon Feb 6 2012 Tony Asleson <tasleson@redhat.com>  0.0.1alpha-1
- Initial version of package

