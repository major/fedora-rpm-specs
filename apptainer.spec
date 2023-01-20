#
# Copyright (c) Contributors to the Apptainer project, established as
#   Apptainer a Series of LF Projects LLC.
#   For website terms of use, trademark policy, privacy policy and other
#   project policies see https://lfprojects.org/policies
# Copyright (c) 2017-2022, SyLabs, Inc. All rights reserved.
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

# Disable debugsource packages; otherwise it ends up with an empty %%files
#   file in debugsourcefiles.list on Fedora
%undefine _debugsource_packages

# This can be slightly different than %%{version}.
# For example, it has dash instead of tilde for release candidates.
%global package_version 1.1.5

# Uncomment this to include a multithreaded version of squashfuse_ll
%global squashfuse_version 0.1.105

# The last singularity version number in EPEL/Fedora
%global last_singularity_version 3.8.7-3

Summary: Application and environment virtualization formerly known as Singularity
Name: apptainer
Version: 1.1.5
Release: 2%{?dist}
# See LICENSE.md for first party code (BSD-3-Clause and LBNL BSD)
# See LICENSE_THIRD_PARTY.md for incorporated code (ASL 2.0)
# See LICENSE_DEPENDENCIES.md for dependencies
# License identifiers taken from: https://fedoraproject.org/wiki/Licensing
License: BSD and LBNL BSD and ASL 2.0
URL: https://apptainer.org
Source: https://github.com/%{name}/%{name}/releases/download/v%{package_version}/%{name}-%{package_version}.tar.gz

%if "%{?squashfuse_version}" != ""
Source10: https://github.com/vasi/squashfuse/archive/%{squashfuse_version}/squashfuse-%{squashfuse_version}.tar.gz
Patch10: https://github.com/vasi/squashfuse/pull/70.patch
Patch11: https://github.com/vasi/squashfuse/pull/77.patch
Patch12: https://github.com/vasi/squashfuse/pull/81.patch
%endif

# This Conflicts is in case someone tries to install the main apptainer
# package when an old singularity package is installed.  An Obsoletes is on
# the apptainer-suid subpackage below.  If an Obsoletes were here too, it
# would get different behavior with yum and dnf: a "yum install apptainer"
# on EL7 would install only apptainer but a "dnf install apptainer" on EL8
# or greater would install both apptainer and apptainer-suid.  With this
# Conflicts, both yum and dnf consistently install both apptainer and
# apptainer-suid when apptainer is requested while singularity is installed.
Conflicts: singularity <= %{last_singularity_version}

# In the singularity 2.x series there was a singularity-runtime package
#  that could have been installed independently, but starting in 3.x
#  there was only one package
Obsoletes: singularity-runtime < 3.0

# Multiple packages contain /usr/bin/singularity and /usr/bin/run-singularity,
# which are necessary to run SIF images.  Use a pivot provides/conflicts to
# avoid them all needing to conflict with each other.
Provides: sif-runtime
Conflicts: sif-runtime

%if "%{_target_vendor}" == "suse"
BuildRequires: binutils-gold
%endif
BuildRequires: golang
BuildRequires: git
BuildRequires: gcc
BuildRequires: make
BuildRequires: libseccomp-devel
%if "%{_target_vendor}" == "suse"
Requires: squashfs
%else
Requires: squashfs-tools
%endif
BuildRequires: cryptsetup
%if "%{?squashfuse_version}" != ""
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: fuse3-devel
BuildRequires: zlib-devel
%endif
Requires: squashfuse
Requires: fakeroot
Requires: fuse-overlayfs
Requires: e2fsprogs
# Uncomment this for the epel build, but we don't want it for the Apptainer
#  release build because there the same rpm is shared across OS versions
%if 0%{?el7}
Requires: fuse2fs
%endif

%description
Apptainer provides functionality to make portable
containers that can be used across host environments.

%package suid
Summary: Setuid component of Apptainer
Requires: %{name} = %{version}-%{release}
# The singularity package was renamed to apptainer.  The Obsoletes is
# on this subpackage for greater compatibility after an update from the
# old singularity.
Obsoletes: singularity <= %{last_singularity_version}

%description suid
Provides the optional setuid-root portion of Apptainer.

%prep
%if "%{?squashfuse_version}" != ""
# the default directory for other steps is where the %%prep section ends
# so do main package last
%setup -b 10 -n squashfuse-%{squashfuse_version}
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%setup -n %{name}-%{package_version}
%else
%autosetup -n %{name}-%{package_version}
%endif

%build
%if "%{?squashfuse_version}" != ""
pushd ../squashfuse-%{squashfuse_version}
./autogen.sh
FLAGS=-std=c99 ./configure --enable-multithreading
%make_build squashfuse_ll
popd
%endif

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
./mconfig %{?mconfig_opts} -V %{version}-%{release} --with-suid \
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

%make_build -C builddir V= old_config=

%install
%if "%{?SOURCE1}" != ""
export PATH=$PWD/go/bin:$PATH
%endif

%make_install -C builddir V=
%if "%{?squashfuse_version}" != ""
install -m 755 ../squashfuse-%{squashfuse_version}/squashfuse_ll %{buildroot}%{_libexecdir}/%{name}/bin/squashfuse_ll
%endif

%if 0%{?el7}
# Check for fuse2fs only as a pre-install so that an rpm built on el7 can
# be used on el8 & el9.  Only el7 has a fuse2fs package, the others have 
# the fuse2fs program in the e2fsprogs package.
%pre
if [ ! -f /usr/bin/fuse2fs ] && [ ! -f /usr/sbin/fuse2fs ]; then
	echo "fuse2fs not found, please yum install /usr/*bin/fuse2fs from epel" >&2
	exit 1
fi
%endif

%post
# $1 in %%posttrans cannot distinguish between fresh installs and upgrades,
# so check it here and create a file to pass the knowledge to that step
if [ "$1" -eq 1 ] && [ -d %{_sysconfdir}/singularity ]; then
	touch %{_sysconfdir}/%{name}/.singularityupgrade
fi

%posttrans
# clean out empty directories under /etc/singularity
rmdir %{_sysconfdir}/singularity/* %{_sysconfdir}/singularity 2>/dev/null || true
if [ -f %{_sysconfdir}/%{name}/.singularityupgrade ]; then
	pushd %{_sysconfdir}/%{name} >/dev/null
	rm .singularityupgrade
	# This is the first install of apptainer after removal of singularity.
	# Import any singularity configurations that remain, which were left
	# because they were non-default.
	find %{_sysconfdir}/singularity ! -type d 2>/dev/null|while read F; do
		B="$(echo $F|sed 's,%{_sysconfdir}/singularity/,,;s/\.rpmsave//')"
		if [ "$B" == singularity.conf ]; then
			echo "info: renaming $PWD/%{name}.conf to $PWD/%{name}.conf.rpmorig" >&2
			mv %{name}.conf %{name}.conf.rpmorig
			echo "info: converting configuration from $F into $PWD/%{name}.conf" >&2
			%{_bindir}/%{name} confgen $F %{name}.conf
		elif [ "$B" == remote.yaml ]; then
			echo "info: renaming $PWD/$B to $PWD/$B.rpmorig" >&2
			mv $B $B.rpmorig
			echo "info: merging $F into $PWD/$B" >&2
			(
			sed -n '1p' $F
			sed -n '2,$p' $B.rpmorig
			sed -n '3,$p' $F
			) >$B
		else
			if [ -f "$B" ]; then
				echo "info: renaming $PWD/$B to $PWD/$B.rpmorig" >&2
				mv $B $B.rpmorig
			fi
			echo "info: copying $F into $PWD/$B" >&2
			cp $F $B
		fi
	done
	popd >/dev/null
fi

# Define `%%license` tag if not already defined.
# This is needed for EL 7 compatibility.
%{!?_licensedir:%global license %doc}

%files
%{_bindir}/%{name}
%{_bindir}/singularity
%{_bindir}/run-singularity
%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/bin
%{_libexecdir}/%{name}/bin/starter
%if "%{?squashfuse_version}" != ""
%{_libexecdir}/%{name}/bin/squashfuse_ll
%endif
%{_libexecdir}/%{name}/cni
%{_libexecdir}/%{name}/lib
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_datadir}/bash-completion/completions/*
%dir %{_localstatedir}/%{name}
%dir %{_localstatedir}/%{name}/mnt
%dir %{_localstatedir}/%{name}/mnt/session
%{_mandir}/man1/%{name}*
%{_mandir}/man1/singularity*
%license LICENSE.md
%license LICENSE_THIRD_PARTY.md
%license LICENSE_DEPENDENCIES.md
%doc README.md
%doc CHANGELOG.md

%files suid
%attr(4755, root, root) %{_libexecdir}/%{name}/bin/starter-suid

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Dave Dykstra <dwd@fnal.gov> - 1.1.5-1
- Update to upstream 1.1.5, including changing the obsoletes on the main
  apptainer package to conflicts.

* Wed Jan  4 2023 Dave Dykstra <dwd@fnal.gov> - 1.1.4-3
- Restore the singularity obsoletes on the apptainer main package, so
  that now it is on both the main package and suid subpackage.

* Wed Dec 14 2022 Carl George <carl@george.computer> - 1.1.4-2
- Add pivot provides/conflict of sif-runtime
- Reduce singularity obsoletes upper bound
- Remove singularity provides due to incompatibilities introduced in apptainer
- Add the word singularity to the summary so it shows up in dnf search results
- Move obsoletes to suid subpackage

* Tue Dec 13 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.4
- Update to upstream 1.1.4.

* Wed Dec  7 2022 Florian Weimer <fweimer@redhat.com> - 1.1.3-2
- Port squashfuse configure script to C99

* Tue Oct 25 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.3
- Update to upstream 1.1.3.

* Thu Oct 06 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.2
- Update to upstream 1.1.2.

* Tue Sep 27 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0
- Update to upstream 1.1.0.  Uncomment the requiring of fuse2fs on el7.

* Tue Sep 06 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0-rc.3
- Update to upstream 1.1.0~rc.3.  Uncomment setting squashfuse_version and
  the requiring of fuse2fs on el7.

* Thu Sep 01 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0-rc.2+37-g1f91ff3
- Test build

* Wed Aug 17 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0~rc.2
- Update to upstream 1.1.0~rc.2.  Remove customizations put into
  1.1.0-rc.1 packaging except for f35 inclusion of golang source.

* Tue Aug  2 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0~rc.1-2
- Add patch for 32-bit compilation

* Tue Aug  2 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.1.0~rc.1
- Update to upstream 1.1.0~rc.1
- Require fuse2fs package on el7
- Require fuse-overlayfs everywhere for cases that kernel overlayfs
  does not support 

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul  6 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.0.3
- Update to upstream 1.0.3

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-2
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Tue May 10 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.0.2
- Update to upstream 1.0.2

* Wed Mar 16 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.0.1
- Update to upstream 1.0.1
- Remove patch from pr 299, not needed anymore

* Thu Mar 03 2022 Dave Dykstra <dwd@fedoraproject.org> - 1.0.0
- Initial release from upstream 1.0.0
