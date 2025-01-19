%define __cmake_in_source_build 1

Name:		lizardfs
Summary:	Distributed, fault tolerant file system
Version:	3.12.0
Release:	29%{?dist}
# LizardFS is under GPLv3 while crcutil is under ASL 2.0 and there's one header,
# src/common/coroutine.h, under the Boost license
# Automatically converted from old format: GPLv3 and ASL 2.0 and Boost - review is highly recommended.
License:	GPL-3.0-only AND Apache-2.0 AND BSL-1.0
URL:		http://www.lizardfs.org/
Source:		https://github.com/lizardfs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	pam-lizardfs
Source2:	95-lizardfs.conf

# Use spdlog system library if available
Patch0:		0001-Put-customized-spdlog-in-source-so-we-don-t-download.patch

# Fix for building with GCC 8
# See https://github.com/lizardfs/lizardfs/pull/677
Patch1:		0001-Add-missing-header.patch

# Use python 3 rather than python 2 for cgi server
Patch2:     lizardfs-3.12-cgi-py3.patch

# Fix missing includes
Patch3:     0003-missing-includes.patch

# Starting with Fedora 42, /bin and /sbin are the same directory
Patch4:     0004-bin-sbin-merge.patch

BuildRequires:	asciidoc
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	systemd

BuildRequires:	boost-devel
BuildRequires:	fuse-devel
BuildRequires:	Judy-devel
BuildRequires:	libdb-devel
BuildRequires:	pam-devel
BuildRequires:	systemd-devel
BuildRequires:	zlib-devel

# libcrcutil is basically a copylib with a dead upstream
# https://code.google.com/archive/p/crcutil/
Provides:	bundled(libcrcutil) = 1.0
# spdlog is a copylib that lizardfs changes, so we can't use the system version
Provides:	bundled(spdlib) = 0.14.0

%global	liz_project	mfs
%global	liz_group	%{liz_project}
%global	liz_user	%{liz_project}
%global	liz_datadir	%{_localstatedir}/lib/%{liz_project}
%global	liz_confdir	%{_sysconfdir}/%{liz_project}

%description
LizardFS is an Open Source, easy to deploy and maintain, distributed,
fault tolerant file system for POSIX compliant OSes.
LizardFS is a fork of MooseFS. For more information please visit
http://lizardfs.com


# Packages
############################################################

%package master
Summary:		LizardFS master server
Requires:		pam
%{?systemd_requires}

%description master
LizardFS master (metadata) server together with metadata restore utility.


%package metalogger
Summary:		LizardFS metalogger server
%{?systemd_requires}

%description metalogger
LizardFS metalogger (metadata replication) server.


%package chunkserver
Summary:		LizardFS data server
%{?systemd_requires}

%description chunkserver
LizardFS data server.


%package client
Summary:		LizardFS client
Requires:		fuse

%description client
LizardFS client: mfsmount and lizardfs.


%package cgi
Summary:		LizardFS CGI Monitor
Requires:		python3

%description cgi
LizardFS CGI Monitor.


%package cgiserv
Summary:		Simple CGI-capable HTTP server to run LizardFS CGI Monitor
Requires:		%{name}-cgi = %{version}-%{release}
%{?systemd_requires}

%description cgiserv
Simple CGI-capable HTTP server to run LizardFS CGI Monitor.


%package adm
Summary:		LizardFS administration utility

%description adm
LizardFS command line administration utility.


# Scriptlets - master
############################################################

%pre master
getent group %{liz_group} >/dev/null || groupadd -r %{liz_group}
getent passwd %{liz_user} >/dev/null || \
	useradd -r -g %{liz_group} -d %{liz_datadir} -s /sbin/nologin \
	-c "LizardFS System Account" %{liz_user}
exit 0

%post master
%systemd_post lizardfs-master.service

%preun master
%systemd_preun lizardfs-master.service

%postun master
%systemd_postun_with_restart lizardfs-master.service


# Scriptlets - metalogger
############################################################

%pre metalogger
getent group %{liz_group} >/dev/null || groupadd -r %{liz_group}
getent passwd %{liz_user} >/dev/null || \
	useradd -r -g %{liz_group} -d %{liz_datadir} -s /sbin/nologin \
	-c "LizardFS System Account" %{liz_user}
exit 0

%post metalogger
%systemd_post lizardfs-metalogger.service

%preun metalogger
%systemd_preun lizardfs-metalogger.service

%postun metalogger
%systemd_postun_with_restart lizardfs-metalogger.service


# Scriptlets - chunkserver
############################################################

%pre chunkserver
getent group %{liz_group} >/dev/null || groupadd -r %{liz_group}
getent passwd %{liz_user} >/dev/null || \
	useradd -r -g %{liz_group} -d %{liz_datadir} -s /sbin/nologin \
	-c "LizardFS System Account" %{liz_user}
exit 0

%post chunkserver
%systemd_post lizardfs-chunkserver.service

%preun chunkserver
%systemd_preun lizardfs-chunkserver.service

%postun chunkserver
%systemd_postun_with_restart lizardfs-chunkserver.service


# Scriptlets - CGI server
############################################################

%post cgiserv
%systemd_post lizardfs-cgiserv.service

%preun cgiserv
%systemd_preun lizardfs-cgiserv.service

%postun cgiserv
%systemd_postun_with_restart lizardfs-cgiserv.service


# Prep, build, install, files...
############################################################

%prep
%autosetup -p1

# Remove /usr/bin/env from bash scripts
for i in src/tools/mfstools.sh src/master/mfsrestoremaster.in \
	 src/common/serialization_macros_generate.sh src/data/postinst.in \
	 utils/coverage.sh utils/cpp-interpreter.sh utils/wireshark/plugins/lizardfs/generate.sh; do
	sed -i 's@#!/usr/bin/env bash@#!/bin/bash@' $i
done
# Remove /usr/bin/env from python3 scripts
for i in src/cgi/cgiserv.py.in src/cgi/chart.cgi.in src/cgi/lizardfs-cgiserver.py.in src/cgi/mfs.cgi.in utils/wireshark/plugins/lizardfs/make_dissector.py; do
	sed -i 's@#!/usr/bin/env python3@#!/usr/bin/python3@' $i
done


%build
# Build code taken almost completely ./configure, but with some changes to use
# Fedora's build flags
rm -rf build-pack
mkdir -p build-pack
cd build-pack

# Shared libraries need to be off because we call some functions that
# are hidden which aren't accessible in DSOs
%cmake .. \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DCMAKE_BUILD_TYPE=Release \
	-DENABLE_TESTS=NO \
	-DCMAKE_INSTALL_PREFIX=/ \
	-DENABLE_DEBIAN_PATHS=YES \
	-DENABLE_DOCS=YES
cat >../Makefile <<END
all:
	make -C build-pack all

clean:
	make -C build-pack clean

install:
	make -C build-pack install

distclean:
	rm -rf build-pack
	rm -rf external/gtest*
	rm -f Makefile
END
make VERBOSE=1 %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{_unitdir}
for f in rpm/service-files/*.service ; do
	install -m644 "$f" %{buildroot}%{_unitdir}/$(basename "$f")
done
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/lizardfs
mkdir -p %{buildroot}%{_sysconfdir}/security/limits.d
install -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/security/limits.d/95-lizardfs.conf


%files master
%doc NEWS README.md UPGRADE
%license COPYING
%{_sbindir}/mfsmaster
%{_sbindir}/mfsrestoremaster
%{_sbindir}/mfsmetadump
%{_sbindir}/mfsmetarestore
%{_mandir}/man5/mfsexports.cfg.5*
%{_mandir}/man5/mfstopology.cfg.5*
%{_mandir}/man5/mfsgoals.cfg.5*
%{_mandir}/man5/mfsmaster.cfg.5*
%{_mandir}/man5/globaliolimits.cfg.5*
%{_mandir}/man7/mfs.7*
%{_mandir}/man7/moosefs.7*
%{_mandir}/man7/lizardfs.7*
%{_mandir}/man8/mfsmaster.8*
%{_mandir}/man8/mfsmetadump.8*
%{_mandir}/man8/mfsmetarestore.8*
%{_mandir}/man8/mfsrestoremaster.8*
%{_unitdir}/lizardfs-master.service
%attr(-,%{liz_user},%{liz_group}) %dir %{liz_datadir}
%attr(-,%{liz_user},%{liz_group}) %{liz_datadir}/metadata.mfs.empty
# Upstream documentation expects default config files to be stored in /etc/mfs
%dir %{liz_confdir}
%config %{liz_confdir}/mfsexports.cfg.dist
%config %{liz_confdir}/mfstopology.cfg.dist
%config %{liz_confdir}/mfsgoals.cfg.dist
%config %{liz_confdir}/mfsmaster.cfg.dist
%config %{liz_confdir}/globaliolimits.cfg.dist
%config(noreplace) %{_sysconfdir}/pam.d/lizardfs
%config(noreplace) %{_sysconfdir}/security/limits.d/95-lizardfs.conf


%files metalogger
%doc NEWS README.md UPGRADE
%license COPYING
%{_sbindir}/mfsmetalogger
%{_mandir}/man5/mfsmetalogger.cfg.5*
%{_mandir}/man8/mfsmetalogger.8*
%{_unitdir}/lizardfs-metalogger.service
%attr(-,%{liz_user},%{liz_group}) %dir %{liz_datadir}
%dir %{liz_confdir}
%config %{liz_confdir}/mfsmetalogger.cfg.dist


%files chunkserver
%doc NEWS README.md UPGRADE
%license COPYING
%{_sbindir}/mfschunkserver
%{_mandir}/man5/mfschunkserver.cfg.5*
%{_mandir}/man5/mfshdd.cfg.5*
%{_mandir}/man8/mfschunkserver.8*
%{_unitdir}/lizardfs-chunkserver.service
%attr(-,%{liz_user},%{liz_group}) %dir %{liz_datadir}
%dir %{liz_confdir}
%config %{liz_confdir}/mfschunkserver.cfg.dist
%config %{liz_confdir}/mfshdd.cfg.dist
%config(noreplace) %{_sysconfdir}/pam.d/lizardfs
%config(noreplace) %{_sysconfdir}/security/limits.d/95-lizardfs.conf


%files client
%doc NEWS README.md UPGRADE
%license COPYING
%{_bindir}/lizardfs
%{_bindir}/mfstools.sh
%{_bindir}/mfsmount
%{_bindir}/mfsappendchunks
%{_bindir}/mfscheckfile
%{_bindir}/mfsdeleattr
%{_bindir}/mfsdirinfo
%{_bindir}/mfsfileinfo
%{_bindir}/mfsfilerepair
%{_bindir}/mfsgeteattr
%{_bindir}/mfsgetgoal
%{_bindir}/mfsgettrashtime
%{_bindir}/mfsmakesnapshot
%{_bindir}/mfsrepquota
%{_bindir}/mfsrgetgoal
%{_bindir}/mfsrgettrashtime
%{_bindir}/mfsrsetgoal
%{_bindir}/mfsrsettrashtime
%{_bindir}/mfsseteattr
%{_bindir}/mfssetgoal
%{_bindir}/mfssetquota
%{_bindir}/mfssettrashtime
%{_mandir}/man1/lizardfs-appendchunks.1*
%{_mandir}/man1/lizardfs-checkfile.1*
%{_mandir}/man1/lizardfs-deleattr.1*
%{_mandir}/man1/lizardfs-dirinfo.1*
%{_mandir}/man1/lizardfs-fileinfo.1*
%{_mandir}/man1/lizardfs-filerepair.1*
%{_mandir}/man1/lizardfs-geteattr.1*
%{_mandir}/man1/lizardfs-getgoal.1*
%{_mandir}/man1/lizardfs-gettrashtime.1*
%{_mandir}/man1/lizardfs-makesnapshot.1*
%{_mandir}/man1/lizardfs-repquota.1*
%{_mandir}/man1/lizardfs-rgetgoal.1*
%{_mandir}/man1/lizardfs-rgettrashtime.1*
%{_mandir}/man1/lizardfs-rremove.1*
%{_mandir}/man1/lizardfs-rsetgoal.1*
%{_mandir}/man1/lizardfs-rsettrashtime.1*
%{_mandir}/man1/lizardfs-seteattr.1*
%{_mandir}/man1/lizardfs-setgoal.1*
%{_mandir}/man1/lizardfs-setquota.1*
%{_mandir}/man1/lizardfs-settrashtime.1*
%{_mandir}/man1/lizardfs.1*
%{_mandir}/man5/iolimits.cfg.5*
%{_mandir}/man5/mfsmount.cfg.5*
%{_mandir}/man7/mfs.7*
%{_mandir}/man7/moosefs.7*
%{_mandir}/man7/lizardfs.7*
%{_mandir}/man1/mfsmount.1*
%{_sysconfdir}/bash_completion.d/lizardfs
%dir %{liz_confdir}
%config %{liz_confdir}/mfsmount.cfg.dist
%config %{liz_confdir}/iolimits.cfg.dist


%files cgi
%doc NEWS README.md UPGRADE
%license COPYING
%dir %{_datadir}/mfscgi
%{_datadir}/mfscgi/err.gif
%{_datadir}/mfscgi/favicon.ico
%{_datadir}/mfscgi/index.html
%{_datadir}/mfscgi/logomini.png
%{_datadir}/mfscgi/mfs.css
%{_datadir}/mfscgi/mfs.cgi
%{_datadir}/mfscgi/chart.cgi


%files cgiserv
%doc NEWS README.md UPGRADE
%license COPYING
%{_sbindir}/lizardfs-cgiserver
%{_sbindir}/mfscgiserv
%{_mandir}/man8/lizardfs-cgiserver.8*
%{_mandir}/man8/mfscgiserv.8*
%{_unitdir}/lizardfs-cgiserv.service


%files adm
%doc NEWS README.md UPGRADE
%license COPYING
%{_bindir}/lizardfs-admin
%{_mandir}/man8/lizardfs-admin.8*
%{_bindir}/lizardfs-probe
%{_mandir}/man8/lizardfs-probe.8*


%changelog
* Fri Jan 17 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.12.0-29
- Fix FTBFS

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 3.12.0-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 09 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.12.0-22
- Add a patch to fix build failures with GCC13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.12.0-17
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 09 2020 Jonathan Dieter <jdieter@gmail.com> - 3.12.0-15
- Fix build issues

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 24 2019 Jonathan Dieter <jdieter@gmail.com> - 3.12.0-11
- Use python 3 for cgi server and web interface

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Jonathan Dieter <jdieter@gmail.com> - 3.12.0-7
- Fix building for GCC 8

* Wed Mar 07 2018 Jonathan Dieter <jdieter@gmail.com> - 3.12.0-6
- Add BuildRequires: gcc and BuildRequires: gcc-c++

* Thu Feb 08 2018 Jonathan Dieter <jdieter@gmail.com> - 3.12.0-5
- Remove obsolete Group tag

* Thu Feb 08 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.12.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Jonathan Dieter <jdieter@gmail.com> - 3.12.0-2
- Fix systemd Requires and BuildRequires

* Tue Dec 26 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.12.0-1
- Update to 3.12.0

* Sat Aug 26 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.11.3-1
- Update to 3.11.3, removing upstreamed patches

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul  5 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.11.2-1
- Update to 3.11.2, removing upstreamed patches and adding in some new ones to
  fix some small caching bugs

* Sun May 28 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.11.0-3
- Add more upstream bug-fixes, the most important of which fixes a rare crash
  in master

* Sat May 20 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.11.0-2
- Update to 3.11.0 which fixes bug where goals are all empty
- Remove upstreamed patches
- Add new upstream patches that fix bugs in 3.11.0

* Tue Apr 25 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.10.6-7
- Switch to upstream patch for building with GCC 7

* Mon Apr 24 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.10.6-6
- Add patch to fix building in Rawhide

* Thu Apr 20 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.10.6-5
- Fix BuildRequires for Judy-devel
- Add BR: pam-devel

* Wed Apr 19 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.10.6-4
- Take ownership of /etc/mfs
- Explain why libcrcutil is bundled
- Change %%define to %%global
- Use hardcoded paths when removing /usr/bin/env from scripts so we don't have
  to BR: python?-devel
- Remove unnecessary rm -rf %%{buildroot}
- Update license information

* Tue Apr 18 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.10.6-3
- Use __python2 and __python3 macros instead of hardcoded paths when removing
  /usr/bin/env from scripts

* Sun Apr  9 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.10.6-2
- Cleanup spec file
- Use Fedora build flags
- Remove /usr/bin/env from scripts

* Thu Jan 26 2017 Jonathan Dieter <jdieter@lesbg.com> - 3.10.6-1
- Update to 3.10.6
- (master) judy library fixes
- (master) ARM compilation fixes

* Mon Oct 31 2016 Jonathan Dieter <jdieter@lesbg.com> - 3.10.4-1
- Update to 3.10.4
- Rename tools

* Tue Aug 16 2016 Jonathan Dieter <jdieter@lesbg.com> - 3.10.0-1
- Update to 3.10.0

* Thu May 19 2016 Jonathan Dieter <jdieter@lesbg.com> - 3.9.4-1
- Fix -l option in mfsmakesnapshot

* Wed Dec 2 2015 Piotr Sarna <contact@lizardfs.org> - 3.9.4
- (master) Removed master server overload on restarting chunkservers
- (master) Improved global file locks engine
- (chunkserver) Fixed leaking descriptors problem
- (chunkserver) Improved mechanism of moving chunks to new directory layout
- (chunkserver) Fixed issues related to scanning directories with new chunk format present
- (mount) Removed hang in mount when chunkserver reported no valid copies of a file
- (master) Changed handling of legacy (pre-3.9.2) chunkservers in new installations
- (cgi) Added XOR replication to statistics
- (all) Removed default linking to tcmalloc library due to performance drop

* Fri Oct 23 2015 Piotr Sarna <contact@lizardfs.org> - 3.9.2
- (all) Introduced XOR goal types
- (all) Added file locks (flock & fcntl)
- (all) Increased max number of files from 500 million to over 4 billion
- (all) Introduced managing open file limits by PAM
- (master) Improved consistency of applying changelogs by shadow masters
- (master) Redesigned snapshot execution in master
- (master) Redesigned chunk loop logic
- (master) Added option to limit chunk loop's CPU usage
- (master) Removed hard coded connection limit
- (chunkserver) Added new network threads responsible for handling requests
  sent by chunkserver's clients
- (chunkserver) Introduced new more efficient directory layout
- (chunkserver) Added option to choose if fsync should be performed after each write
  for increased safety
- (chunkserver) Removed hard coded connection limit
- (chunkserver) Added replication network bandwidth limiting
- (mount) Improved symlink cache and added configurable timeout value
- (all) Minor bug fixes and improvements

* Mon Feb 09 2015 Adam Ochmanski <contact@lizardfs.org> - 2.6.0
- (all) Added comments in all config files
- (all) Improve messages printed by daemons when starting
- (cgi) A new chunkserver's chart: number of chunk tests
- (cgi) Fixed paths to static content
- (cgi) New implementation of the CGI server; mfscgiserv is now deprecated.
- (cgi) New table: 'Metadata Servers' in the 'Servers' tab
- (chunkserver) Allowed starts with damaged disks
- (chunkserver) A new option: HDD_ADVISE_NO_CACHE
- (chunkserver) Improved handling of disk read errors
- (chunkserver) Removed 'testing chunk: xxxxxx' log messages
- (master) A new feature: disabling atime updates (globally)
- (master) Fixed rotating changelogs and downloading files in shadow mode
- (probe) New commands
- (probe) Renamed to lizardfs-admin
- (all) Minor bug fixes and improvements

* Fri Nov 07 2014 Alek Lewandowski <contact@lizardfs.org> - 2.5.4
- (all) Boost is no longer required to build the source code of LizardFS
  or use the binary version
- (all) Added tiering (aka 'custom goal') feature, which allows
  users to label chunkservers and to request chunks to be stored
  on specific groups of servers
- (cgi) "Exports" tabs renamed to "Config", now it also shows goal
  definitions
- (cgi) Added new tab "Chunks"
- (probe) New command "chunks-health" makes it possible to get number of
  missing or endangered chunks
- (master) Fixed reporting memory usage in CGI
- (mount) Fixed caching contents of open directories
- (mount) Add a .lizardfs_tweaks file
- (all) Other minor fixes and improvements

* Mon Sep 15 2014 Alek Lewandowski <contact@lizardfs.org> - 2.5.2
- (master, shadow) Metadata checksum mechanism, allowing to
  find and fix possible metadata inconsistencies between master
  and shadow
- (mount, master) ACL cache in mount, reducing the load of
  the master server
- (packaging) Support packaging for RedHat based systems
- (master) Improved chunkserver deregistration mechanism in
  order to avoid temporary master unresponsiveness
- (polonaise) Add filesystem API for developers allowing to
  use the filesystem without FUSE (and thus working also on
  Windows)
- (all) Minor fixes and improvements

* Tue Jul 15 2014 Marcin Sulikowski <sulik@lizardfs.org> - 2.5.0
- (master) High availability provided by shadow master servers
- (mount, chunkserver) CRC algorithm replaced with a 3 times faster
  implementation
- (mount, master) Support for quotas (for users and groups)
- (mount, master) Support for posix access contol lists (requires
  additional OS support)
- (mount, master) Support for global I/O limiting (bandwidth limiting)
- (mount) Support for per-mountpoint I/O limiting (bandwidth limiting)
- (adm) New package lizardfs-adm with a lizardfs-probe command-line
  tool which can be used to query the installation for variuos
  parameteres
- (master) New mechanism of storing metadata backup files which
  improves performance of the hourly metadata dumps
- (all) A comprehensive test suite added
- (all) Multiple bugfixes


* Wed Oct 16 2013 Peter aNeutrino <contact@lizardfs.org> - 1.6.28-1
- (all) compile with g++ by default
- (deb) fix init scripts for debian packages
- (all) fix build on Mac OS X
- (cgi) introducing LizardFS logo

* Thu Feb 16 2012 Jakub Bogusz <contact@moosefs.com> - 1.6.27-1
- adjusted to keep configuration files in /etc/mfs
- require just mfsexports.cfg (master) and mfshdd.cfg (chunkserver) in RH-like
  init scripts; for other files defaults are just fine to run services
- moved mfscgiserv to -cgiserv subpackage (-cgi alone can be used with any
  external CGI-capable HTTP server), added mfscgiserv init script

* Fri Nov 19 2010 Jakub Bogusz <contact@moosefs.com> - 1.6.19-1
- separated mfs-metalogger subpackage (following Debian packaging)

* Fri Oct  8 2010 Jakub Bogusz <contact@moosefs.com> - 1.6.17-1
- added init scripts based on work of Steve Huff (Dag Apt Repository)
  (included in RPMs when building with --define "distro rh")

* Mon Jul 19 2010 Jakub Kruszona-Zawadzki <contact@moosefs.com> - 1.6.16-1
- added mfscgiserv man page

* Fri Jun 11 2010 Jakub Bogusz <contact@moosefs.com> - 1.6.15-1
- initial spec file, based on Debian packaging;
  partially inspired by spec file by Kirby Zhou
