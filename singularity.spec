# 
# Copyright (c) 2017-2018, SyLabs, Inc. All rights reserved.
# Copyright (c) 2017, SingularityWare, LLC. All rights reserved.
#
# Copyright (c) 2015-2017, Gregory M. Kurtzer. All rights reserved.
# 
# Copyright (c) 2016, The Regents of the University of California, through
# Lawrence Berkeley National Laboratory (subject to receipt of any required
# approvals from the U.S. Dept. of Energy).  All rights reserved.
# 
# This software is licensed under a customized 3-clause BSD license.  Please
# consult LICENSE file distributed with the sources of this project regarding
# your rights to use or distribute this software.
# 
# NOTICE.  This Software was developed under funding from the U.S. Department of
# Energy and the U.S. Government consequently retains certain rights. As such,
# the U.S. Government has been granted for itself and others acting on its
# behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software
# to reproduce, distribute copies to the public, prepare derivative works, and
# perform publicly and display publicly, and to permit other to do so. 
# 
# 

# Disable debugsource packages; otherwise it ends up with an empty %files
#   file in debugsourcefiles.list on Fedora
%undefine _debugsource_packages

# This can be slightly different than %{version}.
# For example, it has dash instead of tilde for release candidates.
%define package_version 3.8.7

Summary: Application and environment virtualization
Name: singularity
Version: 3.8.7
Release: 3%{?dist}
# https://spdx.org/licenses/BSD-3-Clause-LBNL.html
License: BSD-3-Clause-LBNL
URL: https://singularity.hpcng.org
Source: %{name}-%{package_version}.tar.gz

ExclusiveOS: linux
# RPM_BUILD_ROOT wasn't being set ... for some reason
%if "%{sles_version}" == "11"
BuildRoot: /var/tmp/singularity-%{version}-build
%endif

%if "%{_target_vendor}" == "suse"
%if "%{sles_version}" != "11"
BuildRequires: go
%endif
%else
BuildRequires: golang
%endif
BuildRequires: git
BuildRequires: gcc
BuildRequires: make
%if ! 0%{?el6}
%if "%{sles_version}" != "11"
BuildRequires: libseccomp-devel
%endif
%endif
%if "%{_target_vendor}" == "suse"
Requires: squashfs
%else
Requires: squashfs-tools
%endif
BuildRequires: cryptsetup

# there's no golang for ppc64, just ppc64le
ExcludeArch: ppc64

Provides: %{name}-runtime = %{version}-%{release}
Obsoletes: %{name}-runtime < 3.0

%description
Singularity provides functionality to make portable
containers that can be used across host environments.

%debug_package

%prep
%if "%{?buildroot}"
export RPM_BUILD_ROOT="%{buildroot}"
%endif

if [ -d %{name}-%{version} ]; then
    # Clean up old build root
    # First clean go's modcache because directories are unwritable
    GOPATH=$PWD/%{name}-%{version}/gopath go clean -modcache
    rm -rf %{name}-%{version}
fi

# Create our build root
mkdir %{name}-%{version}

%build
cd %{name}-%{version}

# Setup an empty GOPATH for the build
mkdir -p gopath

export GOPATH=$PWD/gopath
export PATH=$GOPATH/bin:$PATH

# Perform the build outside of GOPATH as we are using go modules
tar -xf "%SOURCE0"
cd %{name}-%{package_version}

%if "%{?SOURCE1}" != ""
GOVERSION="$(echo %SOURCE1|sed 's,.*/,,;s/go//;s/\.src.*//')"
if ! ./mlocal/scripts/check-min-go-version go $GOVERSION; then
	# build the go tool chain, the existing version is too old
	pushd ..
	tar -xf %SOURCE1
	cd go/src
	./make.bash
	cd ../..
	export PATH=$PWD/go/bin:$PATH
	popd
fi
%endif


# Not all of these parameters currently have an effect, but they might be
#  used someday.  They are the same parameters as in the configure macro.
./mconfig -V %{version}-%{release} \
        --prefix=%{_prefix} \
        --exec-prefix=%{_exec_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_localstatedir} \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir}

cd builddir
make old_config=

%install
cd %{name}-%{version}

%if "%{?SOURCE1}" != ""
export PATH=$PWD/go/bin:$PATH
%endif
export GOPATH=$PWD/gopath
export PATH=$GOPATH/bin:$PATH

# Enter the source builddir for the install
cd %{name}-%{package_version}/builddir

make DESTDIR=$RPM_BUILD_ROOT install

%if "%{suse_version}" == "11"
%clean
/bin/rm -rf %{buildroot}
%endif

%files
%attr(4755, root, root) %{_libexecdir}/singularity/bin/starter-suid
%{_bindir}/singularity
%{_bindir}/run-singularity
%dir %{_libexecdir}/singularity
%{_libexecdir}/singularity/bin/starter
%{_libexecdir}/singularity/cni/*
%dir %{_sysconfdir}/singularity
%config(noreplace) %{_sysconfdir}/singularity/*.conf
%config(noreplace) %{_sysconfdir}/singularity/*.toml
%config(noreplace) %{_sysconfdir}/singularity/*.json
%config(noreplace) %{_sysconfdir}/singularity/*.yaml
%config(noreplace) %{_sysconfdir}/singularity/global-pgp-public
%config(noreplace) %{_sysconfdir}/singularity/cgroups/*
%config(noreplace) %{_sysconfdir}/singularity/network/*
%config(noreplace) %{_sysconfdir}/singularity/seccomp-profiles/*
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/*
%dir %{_localstatedir}/singularity
%dir %{_localstatedir}/singularity/mnt
%dir %{_localstatedir}/singularity/mnt/session
%{_mandir}/man1/singularity*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 3.8.7-2
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Mar 17 2022 Dave Dykstra <dwd@fedoraproject.org> - 3.8.7-1
- Upgrade to upstream 3.8.7

* Wed Feb  9 2022 Dave Dykstra <dwd@fedoraproject.org> - 3.8.6-1
- Upgrade to upstream 3.8.6

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.8.5-2
- Rebuild using golang-1.16.12

* Mon Nov 29 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.8.5-1
- Upgrade to upstream 3.8.5

* Tue Nov  9 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.8.4-1
- Upgrade to upstream 3.8.4

* Wed Sep  8 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.8.3-1
- Upgrade to upstream 3.8.3

* Wed Sep  1 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.8.2-1
- Upgrade to upstream 3.8.2

* Mon Aug 16 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.8.1-1
- Upgrade to upstream 3.8.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.8.0-1
- Upgrade to upstream 3.8.0

* Wed May 26 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.7.4-1
- Upgrade to upstream security release 3.7.4

* Wed Apr  7 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.7.3-1
- Upgrade to upstream security release 3.7.3

* Thu Mar 11 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.7.2-1
- Upgrade to upstream 3.7.2.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Dave Dykstra <dwd@fedoraproject.org> - 3.7.1-1
- Upgrade to upstream 3.7.1.

* Tue Nov 24 2020 Dave Dykstra <dwd@fedoraproject.org> - 3.7.0-1
- Upgrade to upstream 3.7.0.

* Tue Oct 13 2020 Dave Dykstra <dwd@fedoraproject.org> - 3.6.4-1
- Upgrade to upstream 3.6.4.

* Tue Sep 15 2020 Dave Dykstra <dwd@fedoraproject.org> - 3.6.3-1
- Upgrade to upstream 3.6.3.

* Wed Aug 26 2020 Dave Dykstra <dwd@fedoraproject.org> - 3.6.2-1
- Upgrade to upstream 3.6.2.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Dave Dykstra <dwd@fedoraproject.org> - 3.6.1-1
- Upgrade to upstream 3.6.1.

* Tue Jul 14 2020 Dave Dykstra <dwd@fedoraproject.org> - 3.6.0-1
- Upgrade to upstream 3.6.0.  Remove patch #4679 for el8, since
  golang-12 is now available for that build machine.

* Tue Feb 18 2020 Dave Dykstra <dwd@fedoraproject.org> - 3.5.3-1.1
- Upgrade to upstream 3.5.3, keeping only patch #4769 on el8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Dave Dykstra <dwd@fedoraproject.org> - 3.5.2-1.2
- Add patch for PR #4974.  Only the src rpm is being used, for
  building a --without-suid installation, so this won't be released
  to EPEL or Fedora other than rawhide..

* Tue Dec 17 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.5.2-1.1
- Upgrade to upstream 3.5.2, keeping #4769 patch only on el8

* Thu Dec 05 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.5.1-1.1
- Upgrade to upstream 3.5.1, keeping #4769 patch only on el8

* Wed Nov 20 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.5.0-1.1
- Apply patch from PR #4769 to build with golang-1.11 on el8 only

* Wed Nov 13 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.5.0-1
- Upgrade to upstream 3.5.0

* Thu Nov 07 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.5.0~rc.2-1
- Upgrade to upstream 3.5.0~rc.2.

* Wed Oct 30 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.5.0~rc.1-1
- Upgrade to upstream 3.5.0~rc.1.  Drop PR #4522 patch.

* Mon Oct 21 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.4.2-1.1
- Upgrade to upstream 3.4.2.  Remove PR #4522, no longer needed.
  Still contains config fakeroot cli PR #4346.

* Thu Sep 26 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.4.1-1.2
- Add PR #4522 to fix sandbox rootless builds

* Mon Sep 23 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.4.1-1.1
- Update to upstream 3.4.0-1, keeping only config fakeroot cli PR #4346

* Thu Sep 05 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.4.0-1.2
- Add fix for bug that always enabled --pid (PR #4380)

* Tue Sep 03 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.4.0-1.1
- Update to upstream 3.4.0-1
- Fix compiles on non-64 bit architectures (PR #4370)
- Add config fakeroot CLI which was inadvertently left out of the upstream
  release (PR #4346)

* Tue Jul 30 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.3.0-1
- Update to upstream 3.3.0-1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.2.1-1.1
- Add patch for PR #3456 to make --home work with 'mount home = no'
- Add patch for PR #3803 to make bind mounts from read-only filesystems
  work unprivileged

* Wed May 29 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.2.1-1
- Update to upstream 3.2.1-1

* Mon May 20 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.2.0-1.1
- Add PR #3419

* Mon May 20 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.2.0-1
- Update to upstream 3.2.0-1

* Tue May 14 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.1.1-1.1
- Add patch for CVE-2019-11328

* Tue Apr 02 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.1.1-1
- Update to upstream 3.1.1-1

* Mon Feb 25 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.1.0-1
- Update to upstream 3.1.0-1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.0.3-1
- Update to upstream 3.0.3-1 release.

* Fri Jan 18 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.0.3-rc2
- Update to upstream 3.0.3-rc2

* Wed Jan 16 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.0.3-rc1
- Update to upstream 3.0.3-rc1

* Wed Jan 09 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.0.2-1.2
- Add patch for PR 2531

* Mon Jan 07 2019 Dave Dykstra <dwd@fedoraproject.org> - 3.0.2-1.1
- Update to upstream 3.0.2
- Added patches for PRs 2472, 2478, 2481

* Tue Dec 11 2018 Dave Dykstra <dwd@fedoraproject.org> - 2.6.1-1.1
- Update to released upstream 2.6.1

* Tue Aug 07 2018 Dave Dykstra <dwd@fnal.gov> - 2.6.0-1.1
- Update to released upstream 2.6.0
- Rename PR 1638 to 1817
- Rename PR 1762 to 1818
- Note that PR 1324 was also renamed, to 1819

* Tue Jul 24 2018 Dave Dykstra <dwd@fnal.gov> - 2.5.999-1.4
- Move the Requires /usr/bin/python3 to be under %package runtime instead
  of under its %description.

* Tue Jul 24 2018 Dave Dykstra <dwd@fnal.gov> - 2.5.999-1.3
- Move the BuildRequires /usr/bin/python3 back to the primary package,
  because otherwise it doesn't get installed at build time.  Leave
  the Requires on the runtime subpackage.
- Add singularity.abignore to avoid warnings from abipkgdiff.

* Tue Jul 24 2018 Dave Dykstra <dwd@fnal.gov> - 2.5.999-1.2
- Add PR #1324 which makes the docker:// and shub:// URLs work with only
  the runtime subpackage.  All the changes are to this file so it does
  not add a patch.  Moves python files to the runtime subpackage, so the
  BuildRequires & Requires /usr/bin/python3 go back there as well.
- Improve the underlay option comment in singularity.conf as found in
  the current version of PR #1638.

* Tue Jul 24 2018 Dave Dykstra <dwd@fnal.gov> - 2.5.999-1.1
- Update to upstream 2.5.999, which is tagged as 2.6.0-rc2.
- Disable the underlay feature by default
- Move the BuildRequires: /usr/bin/python3 back to the singularity package
  because there is no python in singularity-runtime.
- Add an additional Requires: /usr/bin/python3 for install time.

* Mon Jul 16 2018 Dave Dykstra <dwd@fnal.gov> - 2.5.99-1.1
- Update to upstream 2.5.99, which is tagged as 2.6.0-rc1.
- Switch to using internally defined require_python3, which is true unless
  %{osg} is defined, to decide whether or not to require python3.
- Get python3 patch from PR #1762 instead of custom defined.
- Move /usr/bin/python3 BuildRequires to singularity-runtime subpackage.
- Apply PR #1638, which adds the underlay feature.

- Only require python3 if %{py3_dist} macro defined

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Dave Dykstra <dwd@fnal.gov> - 2.5.2-1
- Update to upstream high severity security release 2.5.2.   See
  https://github.com/singularityware/singularity/releases/tag/2.5.2
  and CVE #2018-12021.
- Only require python3 if %{py3_dist} macro defined

* Fri May 04 2018 Dave Dykstra <dwd@fnal.gov> - 2.5.1-1
- Update to upstream version 2.5.1

* Fri Apr 27 2018 Dave Dykstra <dwd@fnal.gov> - 2.5.0-1
- Update to upstream version 2.5.0

* Mon Apr 16 2018 Dave Dykstra <dwd@fnal.gov> - 2.4.6-1
- Update to upstream version 2.4.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Dave Love <loveshack@fedoraproject.org> - 2.2.1-3
- Drop patch 13, broken in the merged version
- Fix remaining arch restriction
- Fix configured container_dir

* Thu May 18 2017 Dave Love <loveshack@fedoraproject.org> - 2.2.1-2
- Fix sexec/sexec-suid confusion
- Use _sharedstatedir, not _localstatedir, and make the mnt directories

* Tue May 16 2017 Dave Love <loveshack@fedoraproject.org> - 2.2.1-1
- New version
- Various spec adjustments for the new version
- Replace the patches with a load more
- Remove RHEL5 rpm-isms

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 13 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-10
- Modify COPYING to avoid default licensing
- Patches for race warning and return values

* Fri Jul  1 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-9
- Require pyliblzma and debootstrap
- Patch for mounting kernel file systems
- Fix License tag
- Patch for bootstrap

* Tue Jun 21 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-8
- Revert part of -yum patch

* Fri Jun 17 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-7
- Actually apply patch5

* Thu Jun 16 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-6
- Patches for yum/dnf usage, Fedora example, installing rpm release package,
  creating directories
- Change URL

* Sat Jun 11 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-5
- Modify snapshot bits per review instructions

* Wed Jun  8 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-5
- Patch for rpmlint warnings

* Tue Jun  7 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-4
- Revert last change; configure limits arch, and ftrace to be used again

* Tue Jun  7 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-3
- Don't build ftrace, ftype and remove the arch restriction

* Mon Jun  6 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-2
- Ship LICENSE, examples

* Thu Jun  2 2016 Dave Love <loveshack@fedoraproject.org> - 2.0-1
- New version
- Replace spec features for el5
- Exclude ftrace, ftype

* Fri Apr 29 2016 Dave Love <loveshack@fedoraproject.org> - 1.0-6.e7409ff5
- Updated snapshot

* Thu Apr 21 2016 Dave Love <loveshack@fedoraproject.org> - 1.0-5.20160420
- Don't require which

* Thu Apr 21 2016 Dave Love <loveshack@fedoraproject.org> - 1.0-5.20160420
- Snapshot version
- Remove resolver patch
- Add hardening ldflags

* Wed Apr 20 2016 Dave Love <loveshack@fedoraproject.org> - 1.0-4
- Take description from readme

* Mon Apr 18 2016 Dave Love <loveshack@fedoraproject.org> - 1.0-3
- Patch for missing utils for debug on el6
- More resolver changes

* Sat Apr 16 2016 Dave Love <loveshack@fedoraproject.org> - 1.0-2
- Fix running text resolvers
- Don't configure twice

* Fri Apr 15 2016 Dave Love <loveshack@fedoraproject.org> - 1.0-1
- New version
- BR automake, libtool and run autogen



