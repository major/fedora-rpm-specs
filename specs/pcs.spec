Name: pcs
Version: 0.11.8
Release: 2%{?dist}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
# GPL-2.0-only: pcs
# MIT: dacite
License: GPL-2.0-only AND MIT
URL: https://github.com/ClusterLabs/pcs
Group: System Environment/Base
Summary: Pacemaker/Corosync Configuration System
BuildArch: noarch

# When specifying a commit, use its long hash
%global version_or_commit %{version}
# %%global version_or_commit 10069ca47e5c9f4ac1abd8bc4cd99281ead047b7
%global pcs_source_name %{name}-%{version_or_commit}

# ui_commit can be determined by hash, tag or branch
%global ui_commit 0.1.20
%global ui_modules_version 0.1.20
%global ui_src_name pcs-web-ui-%{ui_commit}

%global pyagentx_version  0.4.pcs.2
%global dacite_version 1.8.1

%global required_pacemaker_version 2.1.0

%global pcs_bundled_dir pcs_bundled
%global pcsd_public_dir pcsd/public
%global ui_build_dir_standalone build_standalone
%global ui_build_dir_cockpit build_cockpit
%global ui_cockpit_dest ha-cluster
%global ui_appstream_metainfo org.clusterlabs.cockpit_pcs_web_ui.metainfo.xml

%global pkg_pcs_snmp  pcs-snmp
%global pkg_cockpit_ha_cluster cockpit-ha-cluster

# prepend v for folder in GitHub link when using tagged tarball
%if "%{version}" == "%{version_or_commit}"
  %global v_prefix v
%endif

# part after the last slash is recognized as filename in look-aside cache
Source0: %{url}/archive/%{?v_prefix}%{version_or_commit}/%{pcs_source_name}.tar.gz

Source41: https://github.com/ondrejmular/pyagentx/archive/v%{pyagentx_version}/pyagentx-%{pyagentx_version}.tar.gz
Source42: https://github.com/konradhalas/dacite/archive/v%{dacite_version}/dacite-%{dacite_version}.tar.gz

Source100: https://github.com/ClusterLabs/pcs-web-ui/archive/%{ui_commit}/%{ui_src_name}.tar.gz
Source101: https://github.com/ClusterLabs/pcs-web-ui/releases/download/%{ui_commit}/pcs-web-ui-node-modules-%{ui_modules_version}.tar.xz

# pcs patches: <= 200
# Patch0: name.patch
Patch0: overhaul-fence-agents-mocking.patch

# ui patches: >200
# Patch201: name-web-ui.patch

# git for patches
BuildRequires: git-core
# for building pcs tarballs
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
# printf from coreutils is used in makefile, head is used in spec
BuildRequires: coreutils
# python for pcs
BuildRequires: python3 >= 3.9
BuildRequires: python3-dateutil >= 2.7.0
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pycurl
BuildRequires: python3-pip
BuildRequires: python3-pyparsing
BuildRequires: python3-tornado
BuildRequires: python3-cryptography
BuildRequires: python3-lxml
# for building bundled python packages
BuildRequires: python3-wheel
# ruby and gems for pcsd
BuildRequires: ruby >= 2.5.0
BuildRequires: ruby-devel
BuildRequires: rubygem-backports
BuildRequires: rubygem-childprocess
BuildRequires: rubygem-ethon
BuildRequires: rubygem-ffi
BuildRequires: rubygem-json
BuildRequires: rubygem-mustermann
BuildRequires: rubygem-puma
BuildRequires: rubygem-rack
BuildRequires: rubygem-rack-protection
BuildRequires: rubygem-rack-test
BuildRequires: rubygem-sinatra
BuildRequires: rubygem-tilt
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: rubygem(rexml)
%endif
# ruby libraries for tests
BuildRequires: rubygem-test-unit
# for touching patch files (sanitization function)
BuildRequires: diffstat
# for post, preun and postun macros
BuildRequires: systemd
# pam is used for authentication inside daemon (python ctypes)
# needed for tier0 tests during build
BuildRequires: pam
# for working with qdevice certificates (certutil) - used in configure.ac
BuildRequires: nss-tools

# for building web ui
BuildRequires: nodejs-npm

# cluster stack packages for pkg-config
# corosync has different package names on distributions but all provide
# corosync-devel
# corosync and pacemaker need versions and it's not working in virtual provides
BuildRequires: corosync-devel >= 3.0
BuildRequires: pacemaker-libs-devel >= %{required_pacemaker_version}
BuildRequires: pkgconfig(booth)
BuildRequires: pkgconfig(corosync-qdevice)
BuildRequires: pkgconfig(sbd)

# for validating cockpit-ha-cluster metainfo
BuildRequires: libappstream-glib


# python and libraries for pcs, setuptools for pcs entrypoint
Requires: python3-cryptography
Requires: python3-dateutil >= 2.7.0
Requires: python3-lxml
Requires: python3-setuptools
Requires: python3-pycurl
Requires: python3-pyparsing
Requires: python3-tornado
# ruby and gems for pcsd
Requires: ruby >= 2.5.0
Requires: rubygem-backports
Requires: rubygem-childprocess
Requires: rubygem-ethon
Requires: rubygem-ffi
Requires: rubygem-json
Requires: rubygem-mustermann
Requires: rubygem-puma
Requires: rubygem-rack
Requires: rubygem-rack-protection
Requires: rubygem-rack-test
Requires: rubygem-sinatra
Requires: rubygem-tilt
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires: rubygem(rexml)
%endif
# for killall
Requires: psmisc
# cluster stack and related packages
Requires: pcmk-cluster-manager >= %{required_pacemaker_version}
Suggests: pacemaker
Requires: (corosync >= 3.0 if pacemaker)
# pcs enables corosync encryption by default so we require libknet1-plugins-all
Requires: (libknet1-plugins-all if corosync)
Requires: pacemaker-cli >= %{required_pacemaker_version}
# for post, preun and postun macros
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# pam is used for authentication inside daemon (python ctypes)
# more details: https://bugzilla.redhat.com/show_bug.cgi?id=1717113
Requires: pam
# needs logrotate for /etc/logrotate.d/pcsd
Requires: logrotate
# for working with qdevice certificates (certutil)
Requires: nss-tools


Provides: bundled(dacite) = %{dacite_version}


# pcs-snmp subpackage definition
%package -n %{pkg_pcs_snmp}
Group: System Environment/Base
Summary: Pacemaker cluster SNMP agent
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
# GPL-2.0-only: pcs
# BSD-2-Clause: pyagentx
License: GPL-2.0-only AND BSD-2-Clause
URL: https://github.com/ClusterLabs/pcs
BuildArch: noarch

# tar for unpacking pyagentx source tarball
BuildRequires: tar

Requires: pcs = %{version}-%{release}
Requires: pacemaker
Requires: net-snmp

Provides: bundled(pyagentx) = %{pyagentx_version}

# cockpit-ha-cluster subpackage definition
%package -n %{pkg_cockpit_ha_cluster}
Group: System Environment/Base
Summary: Cockpit application for managing Pacemaker based clusters
License: GPL-2.0-only AND CC0-1.0
URL: https://github.com/ClusterLabs/pcs-web-ui

BuildRequires: make
BuildRequires: nodejs-npm

Requires: pcs = %{version}-%{release}
Requires: cockpit-bridge


%description
pcs is a corosync and pacemaker configuration tool.  It permits users to
easily view, modify and create pacemaker based clusters.

%description -n %{pkg_pcs_snmp}
SNMP agent that provides information about pacemaker cluster to the master agent
(snmpd).

%description -n %{pkg_cockpit_ha_cluster}
Cockpit application for managing Pacemaker based clusters. Uses
Pacemaker/Corosync Configuration System (pcs) in the background.

%prep

# -- following is inspired by python-simplejon.el5 --
# Update timestamps on the files touched by a patch, to avoid non-equal
# .pyc/.pyo files across the multilib peers within a build

update_times(){
  # update_times <reference_file> <file_to_touch> ...
  # set the access and modification times of each file_to_touch to the times
  # of reference_file

  # put all args to file_list
  file_list=("$@")
  # first argument is reference_file: so take it and remove from file_list
  reference_file=${file_list[0]}
  unset file_list[0]

  for fname in ${file_list[@]}; do
    # some files could be deleted by a patch therefore we test file for
    # existance before touch to avoid exit with error: No such file or
    # directory
    # diffstat cannot create list of files without deleted files
    test -e $fname && touch -r $reference_file $fname
  done
}

update_times_patch(){
  # update_times_patch <patch_file_name>
  # set the access and modification times of each file in patch to the times
  # of patch_file_name

  patch_file_name=$1

  # diffstat
  # -l lists only the filenames. No histogram is generated.
  # -p override the logic that strips common pathnames,
  #    simulating the patch "-p" option. (Strip the smallest prefix containing
  #    num leading slashes from each file name found in the patch file)
  update_times ${patch_file_name} `diffstat -p1 -l ${patch_file_name}`
}

# documentation for setup/autosetup/autopatch:
#   * http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
#   * https://rpm-software-management.github.io/rpm/manual/autosetup.html
# patch web-ui sources
%autosetup -D -T -b 100 -a 101 -S git -n %{ui_src_name} -N
%autopatch -p1 -m 201
# update_times_patch %%{PATCH201}

# patch pcs sources
%autosetup -S git -n %{pcs_source_name} -N
%autopatch -p1 -M 200
# update_times_patch %%{PATCH0}
update_times_patch %{PATCH0}

# generate .tarball-version if building from an untagged commit, not a released version
# autogen uses git-version-gen which uses .tarball-version for generating version number
%if "%{version}" != "%{version_or_commit}"
  echo "%version+$(echo "%{version_or_commit}" | head -c 8)" > %{_builddir}/%{pcs_source_name}/.tarball-version
%endif

# prepare dirs/files necessary for building python bundles
mkdir -p %{pcs_bundled_dir}/src
cp -f %SOURCE41 rpm/
cp -f %SOURCE42 rpm/


%build
%define debug_package %{nil}

./autogen.sh
%{configure} --enable-local-build --enable-use-local-cache-only \
  --enable-individual-bundling \
  --with-pcsd-default-cipherlist='PROFILE=SYSTEM' \
  --with-pcs-lib-dir="%{_prefix}/lib" PYTHON=%{__python3}
make all

# build pcs-web-ui
export BUILD_USE_CURRENT_NODE_MODULES=true

## standalone
export BUILD_DIR=%{_builddir}/%{ui_src_name}/%{ui_build_dir_standalone}
make -C %{_builddir}/%{ui_src_name} build

## cockpit
export BUILD_DIR=%{_builddir}/%{ui_src_name}/%{ui_build_dir_cockpit}
export BUILD_FOR_COCKPIT=true
make -C %{_builddir}/%{ui_src_name} build


%install
rm -rf $RPM_BUILD_ROOT
pwd


%make_install
# install standalone pcs-web-ui
cp -r %{_builddir}/%{ui_src_name}/%{ui_build_dir_standalone} \
     ${RPM_BUILD_ROOT}%{_prefix}/lib/%{pcsd_public_dir}/ui

# install cockpit pcs-web-ui
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/cockpit/%{ui_cockpit_dest}
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/metainfo
cp -r %{_builddir}/%{ui_src_name}/%{ui_build_dir_cockpit}/* \
     ${RPM_BUILD_ROOT}%{_datadir}/cockpit/%{ui_cockpit_dest}

cp -r %{_builddir}/%{ui_src_name}/packages/app/%{ui_appstream_metainfo} \
     ${RPM_BUILD_ROOT}%{_datadir}/metainfo/

# prepare license files
cp %{pcs_bundled_dir}/src/pyagentx-*/LICENSE.txt pyagentx_LICENSE.txt
cp %{pcs_bundled_dir}/src/pyagentx-*/CONTRIBUTORS.txt pyagentx_CONTRIBUTORS.txt
cp %{pcs_bundled_dir}/src/pyagentx-*/README.md pyagentx_README.md

cp %{pcs_bundled_dir}/src/dacite-*/LICENSE dacite_LICENSE
cp %{pcs_bundled_dir}/src/dacite-*/README.md dacite_README.md


%check
# Run validation of cockpit metainfo
appstream-util validate-relax --nonet ${RPM_BUILD_ROOT}%{_datadir}/metainfo/%{ui_appstream_metainfo}

# In the building environment LC_CTYPE is set to C which causes tests to fail
# due to python prints a warning about it to stderr. The following environment
# variable disables the warning.
# On the live system either UTF8 locale is set or the warning is emmited
# which breaks pcs. That is the correct behavior since with wrong locales it
# would be probably broken anyway.
# The main concern here is to make the tests pass.
# See https://fedoraproject.org/wiki/Changes/python3_c.utf-8_locale for details.
export PYTHONCOERCECLOCALE=0

run_all_tests(){
  #run pcs tests

  # disabled tests:
  #
  %{__python3} pcs_test/suite --tier0 -v --vanilla --all-but \
  pcs_test.tier0.daemon.app.test_app_remote.SyncConfigMutualExclusive.test_get_not_locked \
  pcs_test.tier0.daemon.app.test_app_remote.SyncConfigMutualExclusive.test_post_not_locked \

  test_result_python=$?

  #run pcsd tests and remove them
  ruby \
    -I$RPM_BUILD_ROOT%{_prefix}/lib/pcsd \
    -Ipcsd/test \
    pcsd/test/test_all_suite.rb
  test_result_ruby=$?

  if [ $test_result_python -ne 0 ]; then
    return $test_result_python
  fi
  return $test_result_ruby
}

run_all_tests

%posttrans
# Make sure the new version of the daemon is running.
# Also, make sure to start pcsd-ruby if it hasn't been started or even
# installed before. This is done by restarting pcsd.service.
%{_bindir}/systemctl daemon-reload
%{_bindir}/systemctl try-restart pcsd.service


%post
%systemd_post pcsd.service
%systemd_post pcsd-ruby.service

%post -n %{pkg_pcs_snmp}
%systemd_post pcs_snmp_agent.service

%preun
%systemd_preun pcsd.service
%systemd_preun pcsd-ruby.service

%preun -n %{pkg_pcs_snmp}
%systemd_preun pcs_snmp_agent.service

%postun
%systemd_postun_with_restart pcsd.service
%systemd_postun_with_restart pcsd-ruby.service

%postun -n %{pkg_pcs_snmp}
%systemd_postun_with_restart pcs_snmp_agent.service

%files
%doc CHANGELOG.md
%doc README.md
%doc dacite_README.md
%license dacite_LICENSE
%license COPYING
%{python3_sitelib}/*
%{_sbindir}/pcs
%{_sbindir}/pcsd
%{_prefix}/lib/pcs/*
%{_prefix}/lib/pcsd/*
%{_unitdir}/pcsd.service
%{_unitdir}/pcsd-ruby.service
%{_datadir}/bash-completion/completions/pcs
%{_sharedstatedir}/pcsd
%config(noreplace) %{_sysconfdir}/pam.d/pcsd
%dir %{_var}/log/pcsd
%config(noreplace) %{_sysconfdir}/logrotate.d/pcsd
%config(noreplace) %{_sysconfdir}/sysconfig/pcsd
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/cfgsync_ctl
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/known-hosts
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/pcsd.cookiesecret
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/pcsd.crt
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/pcsd.key
%ghost %config(noreplace) %attr(0644,root,root) %{_sharedstatedir}/pcsd/pcs_settings.conf
%ghost %config(noreplace) %attr(0644,root,root) %{_sharedstatedir}/pcsd/pcs_users.conf
%{_mandir}/man8/pcs.*
%{_mandir}/man8/pcsd.*
%exclude %{_prefix}/lib/pcs/pcs_snmp_agent
%exclude %{_prefix}/lib/pcs/%{pcs_bundled_dir}/packages/pyagentx*
%exclude %{_datadir}/cockpit
%exclude %{_datadir}/metainfo/%{ui_appstream_metainfo}

%files -n %{pkg_pcs_snmp}
%{_prefix}/lib/pcs/pcs_snmp_agent
%{_prefix}/lib/pcs/%{pcs_bundled_dir}/packages/pyagentx*
%{_unitdir}/pcs_snmp_agent.service
%{_datadir}/snmp/mibs/PCMK-PCS*-MIB.txt
%{_mandir}/man8/pcs_snmp_agent.*
%config(noreplace) %{_sysconfdir}/sysconfig/pcs_snmp_agent
%doc CHANGELOG.md
%doc pyagentx_CONTRIBUTORS.txt
%doc pyagentx_README.md
%license COPYING
%license pyagentx_LICENSE.txt

%files -n %{pkg_cockpit_ha_cluster}
%{_datadir}/cockpit/%{ui_cockpit_dest}
%{_datadir}/metainfo/%{ui_appstream_metainfo}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 6 2024 Michal Pospíšil <mpospisi@redhat.com> - 0.11.8-1
- Rebased to the latest sources (see CHANGELOG.md)
- Updated pcs-web-ui to 0.1.20

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.11.7-4
- Rebuilt for Python 3.13

* Mon Feb 5 2024 Michal Pospisil <mpospisi@redhat.com> - 0.11.7-3
- Fixed a bug preventing the Cockpit Application from being installed from Cockpit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 8 2024 Michal Pospisil <mpospisi@redhat.com> - 0.11.7-1
- Rebased to the latest upstream sources (see CHANGELOG.md)
- Updated pcs-web-ui to 0.1.18
- TLS cipher setting in pcsd now follows system-wide crypto policies by default
- Added cockpit-ha-cluster subpackage that adds pcs-web-ui as a Cockpit application

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 0.11.6-2
- Rebuilt for Python 3.12

* Wed Jun 21 2023 Michal Pospisil <mpospisi@redhat.com> - 0.11.6-1
- Rebased to the latest upstream sources (see CHANGELOG.md)
- Updated pcs-web-ui
- Removed dependency fedora-logos - favicon is now correctly provided by pcs-web-ui
- Resolves: rhbz#2109852 rhbz#2170648

* Wed Apr 12 2023 Michal Pospisil <mpospisi@redhat.com> - 0.11.5-2
- Fix displaying differences between configuration checkpoints in “pcs config checkpoint diff” command
- Fix “pcs stonith update-scsi-devices” command which was broken since Pacemaker-2.1.5-rc1
- Fixed loading of cluster status in the web interface when fencing levels are configured
- Fixed a vulnerability in pcs-web-ui-node-modules
- Swapped BuildRequires: npm for BuildRequires: nodejs-npm in Fedora 37 because of NodeJS packaging change
- Removed BuildRequires: rubygem-io-console
- Removed dependency rubygem-eventmachine

* Thu Feb 16 2023 Michal Pospisil <mpospisi@redhat.com> - 0.11.5-1
- Rebased to the latest upstream sources (see CHANGELOG.md)
- Fixed broken filtering in create resource/fence device wizards in the web interface
- Converted package to noarch
- Added creation of .tarball-version file needed by autotools when building from untagged commits and fixed Source0 link to the tarball on GitHub
- Modified build options of pcs for booth authfile fix for all Fedora versions
- Added BuildRequires: pam for tier0 tests during build
- Added BuildRequires: nodejs-npm for NodeJS packaging change since Fedora 38
- Removed bundled rubygem thin and its associated BuildRequires: rubygems, rubygem-bundler, rubygem-daemons, gcc, gcc-c++
- Added dependency rubygem-puma - replacement for rubygem thin
- Added dependency nss-tools - for working with qdevice certificates
- Added dependency fedora-logos - for the web interface favicon
- Removed dependencies: rubygem-daemons, rubygem(webrick)
- Resolves: rhbz#2166266

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.11.4-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2
- Workaround for dnf dependency resolution confusion between nodejs16 vs nodejs
- Workaround for find-debuginfo.sh failure wrt ruby3.2 gem install change

* Mon Dec 12 2022 Michal Pospisil <mpospisi@redhat.com> - 0.11.4-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Updated pcs-web-ui
- Added dependency rubygem-childprocess
- Removed dependency rubygem-open4

* Mon Dec 12 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.11.3-5
- Backport upstream patch for rubygem-json 2.6.3 error message format change

* Wed Sep 07 2022 Miroslav Lisik <mlisik@redhat.com> - 0.11.3-4
- Fixed ruby socket permissions
- Resolves: rhbz#2123389

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11.3-2
- Rebuilt for pyparsing-3.0.9

* Tue Jun 28 2022 Miroslav Lisik <mlisik@redhat.com> - 0.11.3-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Updated pcs-web-ui
- Resolves: rhbz#2068452

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.11.2-3
- Rebuilt for Python 3.11

* Thu Jun 09 2022 Miroslav Lisik <mlisik@redhat.com> - 0.11.2-2
- Python 3.11 related fixes
- Resolves: rhbz#bz2093935

* Fri Feb 04 2022 Miroslav Lisik <mlisik@redhat.com> - 0.11.2-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Updated pcs-web-ui
- Removed old web gui

* Thu Jan 27 2022 Vít Ondruch <vondruch@redhat.com> - 0.10.11-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Miroslav Lisik <mlisik@redhat.com> - 0.10.11-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Updated pcs-web-ui
- Stop bundling rubygems daemons eventmachine mustermann rack rack-protection ruby2_keywords sinatra tilt

* Mon Aug 16 2021 Miroslav Lisik <mlisik@redhat.com> - 0.10.9-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Updated pcs-web-ui
- Bundle rubygem-sinatra, rubygem-thin and their dependencies because they were orphaned
- Resolves: rhbz#1983359

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10.8-3
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.8-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Feb 04 2021 Miroslav Lisik <mlisik@redhat.com> - 0.10.8-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Updated pcs-web-ui
- Updated bundled python dependency: dacite
- Changed BuildRequires from git to git-core
- Added conditional (Build)Requires: rubygem(rexml)
- Added conditional Requires: rubygem(webrick)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Vít Ondruch <vondruch@redhat.com> - 0.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Thu Nov 26 2020 Ondrej Mular <omular@redhat.com> - 0.10.7-2
- Python 3.10 related fix

* Wed Sep 30 2020 Miroslav Lisik <mlisik@redhat.com> - 0.10.7-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Added dependency on python packages pyparsing and dateutil
- Fixed virtual bundle provides for ember, handelbars, jquery and jquery-ui
- Removed dependency on python3-clufter

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Miroslav Lisik <mlisik@redhat.com> - 0.10.6-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Updated pcs-web-ui
- Stopped bundling tornado (use distribution package instead)
- Stopped bundling rubygem-tilt (use distribution package instead)
- Removed rubygem bundling
- Removed unneeded BuildRequires: execstack, gcc, gcc-c++
- Excluded some tests for tornado daemon

* Tue Jul 21 2020 Tom Stellard <tstellar@redhat.com> - 0.10.5-8
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jul 15 2020 Ondrej Mular <omular@redhat.com> - 0.10.5-7
- Use fixed upstream version of dacite with Python 3.9 support
- Split upstream tests in gating into tiers

* Fri Jul 03 2020 Ondrej Mular <omular@redhat.com> - 0.10.5-6
- Use patched version of dacite compatible with Python 3.9
- Resolves: rhbz#1838327

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.5-5
- Rebuilt for Python 3.9

* Thu May 07 2020 Ondrej Mular <omular@redhat.com> - 0.10.5-4
- Rebased to latest upstream sources (see CHANGELOG.md)
- Run only tier0 tests in check section

* Fri Apr 03 2020 Ondrej Mular <omular@redhat.com> - 0.10.5-3
- Enable gating

* Fri Mar 27 2020 Ondrej Mular <omular@redhat.com> - 0.10.5-2
- Remove usage of deprecated module xml.etree.cElementTree
- Resolves: rhbz#1817695

* Wed Mar 18 2020 Miroslav Lisik <mlisik@redhat.com> - 0.10.5-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Miroslav Lisik <mlisik@redhat.com> - 0.10.4-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.3-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Ondrej Mular <omular@redhat.com> - 0.10.3-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Ondrej Mular <omular@redhat.com> - 0.10.2-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Added pam as required package
- An alternative webUI rebased to latest upstream sources
- Improved configuration files permissions in rpm

* Tue Mar 19 2019 Tomas Jelinek <tojeline@redhat.com> - 0.10.1-4
- Removed unused dependency rubygem-multi_json
- Removed files needed only for building rubygems from the package

* Mon Feb 04 2019 Ivan Devát <idevat@redhat.com> - 0.10.1-3
- Corrected gem install flags

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Ivan Devát <idevat@redhat.com> - 0.10.1-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Tue Oct 09 2018 Ondrej Mular <omular@redhat.com> - 0.10.0.alpha.6-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Resolves: rhbz#1618911

* Fri Aug 31 2018 Ivan Devát <idevat@redhat.com> - 0.10.0.alpha.2-3
- Started bundling rubygem-tilt (rubygem-tilt is orphaned in fedora due to rubygem-prawn dependency)
- Enabled passing tests

* Sat Aug 25 2018 Ivan Devát <idevat@redhat.com> - 0.10.0.alpha.2-2
- Fixed error with missing rubygem location during pcsd start
- Resolves: rhbz#1618911

* Thu Aug 02 2018 Ivan Devát <idevat@redhat.com> - 0.10.0.alpha.2-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Wed Jul 25 2018 Ivan Devát <idevat@redhat.com> - 0.9.164-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.164-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.164-2
- Rebuilt for Python 3.7

* Mon Apr 09 2018 Ondrej Mular <omular@redhat.com> - 0.9.164-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Fixed: CVE-2018-1086, CVE-2018-1079

* Mon Feb 26 2018 Ivan Devát <idevat@redhat.com> - 0.9.163-2
- Fixed crash when adding a node to a cluster

* Tue Feb 20 2018 Ivan Devát <idevat@redhat.com> - 0.9.163-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Adapted for Rack 2 and Sinatra 2

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.160-5
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.160-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.160-3
- Rebuilt for switch to libxcrypt

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.160-2
- F-28: rebuild for ruby25
- Workaround for gem install option

* Wed Oct 18 2017 Ondrej Mular <omular@redhat.com> - 0.9.160-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- All pcs tests are temporarily disabled because of issues in pacemaker.

* Thu Sep 14 2017 Ondrej Mular <omular@redhat.com> - 0.9.159-4
- Bundle rubygem-rack-protection which is being updated to 2.0.0 in Fedora.
- Removed setuptools patch.
- Disabled debuginfo subpackage.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.159-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.159-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Ondrej Mular <omular@redhat.com> - 0.9.159-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Tue May 23 2017 Tomas Jelinek <tojeline@redhat.com> - 0.9.156-3
- Fixed python locales issue preventing build-time tests to pass
- Bundle rubygem-tilt which is being retired from Fedora

* Thu Mar 23 2017 Tomas Jelinek <tojeline@redhat.com> - 0.9.156-2
- Fixed Cross-site scripting (XSS) vulnerability in web UI CVE-2017-2661
- Re-added support for clufter as it is now available for Python 3

* Wed Feb 22 2017 Tomas Jelinek <tojeline@redhat.com> - 0.9.156-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.155-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Vít Ondruch <vondruch@redhat.com> - 0.9.155-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Wed Jan 04 2017 Adam Williamson <awilliam@redhat.com> - 0.9.155-1
- Latest release 0.9.155
- Fix tests with Python 3.6 and lxml 3.7
- Package the license as license, not doc
- Use -f param for rm when wiping test directories as they are nested now

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Oct 18 2016 Tomas Jelinek <tojeline@redhat.com> - 0.9.154-2
- Fixed upgrading from pcs-0.9.150

* Thu Sep 22 2016 Tomas Jelinek <tojeline@redhat.com> - 0.9.154-1
- Re-synced to upstream sources
- Spec file cleanup and fixes

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.150-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 11 2016 Tomas Jelinek <tojeline@redhat.com> - 0.9.150-1
- Re-synced to upstream sources
- Make pcs depend on python3
- Spec file cleanup

* Tue Feb 23 2016 Tomas Jelinek <tojeline@redhat.com> - 0.9.149-2
- Fixed rubygems issues which prevented pcsd from starting
- Added missing python-lxml dependency

* Thu Feb 18 2016 Tomas Jelinek <tojeline@redhat.com> - 0.9.149-1
- Re-synced to upstream sources
- Security fix for CVE-2016-0720, CVE-2016-0721
- Fixed rubygems issues which prevented pcsd from starting
- Rubygems built with RELRO
- Spec file cleanup
- Fixed multilib .pyc/.pyo issue

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.144-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 0.9.144-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Fri Sep 18 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.144-1
- Re-synced to upstream sources

* Tue Jun 23 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.141-2
- Added requirement for psmisc for killall

* Tue Jun 23 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.141-1
- Re-synced to upstream sources

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.140-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.140-1
- Re-synced to upstream sources

* Fri May 22 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-4
- Fix for CVE-2015-1848, CVE-2015-3983 (sessions not signed)

* Thu Mar 26 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-3
- Add BuildRequires: systemd (rhbz#1206253)

* Fri Feb 27 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-2
- Reflect clufter inclusion (rhbz#1180723)

* Thu Feb 19 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-1
- Re-synced to upstream sources

* Sat Jan 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.115-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.115-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.115-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.115-2
- Rebuild to fix ruby dependencies

* Mon Apr 21 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-1
- Re-synced to upstream sources

* Fri Dec 13 2013 Chris Feist <cfeist@redhat.com> - 0.9.102-1
- Re-synced to upstream sources

* Wed Jun 19 2013 Chris Feist <cfeist@redhat.com> - 0.9.48-1
- Rebuild with upstream sources

* Thu Jun 13 2013 Chris Feist <cfeist@redhat.com> - 0.9.44-5
- Added fixes for building rpam with ruby-2.0.0

* Mon Jun 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.44-4
- Rebuild with upstream sources

* Tue May 07 2013 Chris Feist <cfeist@redhat.com> - 0.9.41-2
- Resynced to upstream sources

* Fri Apr 19 2013 Chris Feist <cfeist@redhat.com> - 0.9.39-1
- Fixed gem building
- Re-synced to upstream sources

* Mon Mar 25 2013 Chris Feist <cfeist@rehdat.com> - 0.9.36-4
- Don't try to build gems at all

* Mon Mar 25 2013 Chris Feist <cfeist@rehdat.com> - 0.9.36-3
- Removed all gems from build, will need to find pam package in the future

* Mon Mar 25 2013 Chris Feist <cfeist@redhat.com> - 0.9.36-2
- Removed duplicate libraries already present in fedora

* Mon Mar 18 2013 Chris Feist <cfeist@redhat.com> - 0.9.36-1
- Resynced to latest upstream

* Mon Mar 11 2013 Chris Feist <cfeist@redhat.com> - 0.9.33-1
- Resynched to latest upstream
- pcsd has been moved to /usr/lib to fix /usr/local packaging issues

* Thu Feb 21 2013 Chris Feist <cfeist@redhat.com> - 0.9.32-1
- Resynced to latest version of pcs/pcsd

* Mon Nov 05 2012 Chris Feist <cfeist@redhat.com> - 0.9.27-3
- Build on all archs

* Thu Oct 25 2012 Chris Feist <cfeist@redhat.com> - 0.9.27-2
- Resync to latest version of pcs
- Added pcsd daemon

* Mon Oct 08 2012 Chris Feist <cfeist@redhat.cmo> - 0.9.26-1
- Resync to latest version of pcs

* Thu Sep 20 2012 Chris Feist <cfeist@redhat.cmo> - 0.9.24-1
- Resync to latest version of pcs

* Thu Sep 20 2012 Chris Feist <cfeist@redhat.cmo> - 0.9.23-1
- Resync to latest version of pcs

* Wed Sep 12 2012 Chris Feist <cfeist@redhat.cmo> - 0.9.22-1
- Resync to latest version of pcs

* Thu Sep 06 2012 Chris Feist <cfeist@redhat.cmo> - 0.9.19-1
- Resync to latest version of pcs

* Tue Aug 07 2012 Chris Feist <cfeist@redhat.com> - 0.9.12-1
- Resync to latest version of pcs

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Chris Feist <cfeist@redhat.com> - 0.9.4-1
- Resync to latest version of pcs
- Move cluster creation options to cluster sub command.

* Mon May 07 2012 Chris Feist <cfeist@redhat.com> - 0.9.3.1-1
- Resync to latest version of pcs which includes fixes to work with F17.

* Mon Mar 19 2012 Chris Feist <cfeist@redhat.com> - 0.9.2.4-1
- Resynced to latest version of pcs

* Mon Jan 23 2012 Chris Feist <cfeist@redhat.com> - 0.9.1-1
- Updated BuildRequires and %%doc section for fedora

* Fri Jan 20 2012 Chris Feist <cfeist@redhat.com> - 0.9.0-2
- Updated spec file for fedora specific changes

* Mon Jan 16 2012 Chris Feist <cfeist@redhat.com> - 0.9.0-1
- Initial Build
