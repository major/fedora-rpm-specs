%define _hardened_build 1
Name:             zfs-fuse
Version:          0.7.2.2
Release:          32%{?dist}
Summary:          ZFS ported to Linux FUSE
License:          CDDL-1.0
URL:              https://github.com/gordan-bobic/zfs-fuse
Source00:         http://github.com/gordan-bobic/zfs-fuse/archive/%{name}-%{version}.tar.gz
Source01:         zfs-fuse.service
Source02:         zfs-fuse.scrub
Source03:         zfs-fuse.sysconfig
Source04:         zfs-fuse-helper
Source05:         zfs-fuse-scrub.service
Source06:         zfs-fuse-scrub.timer

Patch0:           zfs-fuse-0.7.2.2-stack.patch
Patch1:           zfs-fuse-0.7.2.2-python3.patch
Patch2:           tirpc.patch
Patch3:           common.patch
Patch4:           gcc.patch
Patch5:           zfs-fuse-c99.patch

BuildRequires:  gcc
BuildRequires:    fuse-devel libaio-devel perl-generators scons gcc-c++
BuildRequires:    zlib-devel openssl-devel libattr-devel lzo-devel bzip2-devel xz-devel
BuildRequires:    libtirpc-devel
%ifnarch aarch64 ppc64le
BuildRequires:    /usr/bin/execstack
%endif
BuildRequires:    systemd
Requires:         fuse >= 2.7.4-1
#Needs initscripts for helper scripts
Requires:         initscripts
# (2010 karsten@redhat.com) zfs-fuse doesn't have s390(x) implementations for atomic instructions
ExcludeArch:      s390 s390x aarch64
# For compatibility for packages expecting slightly other locations
Provides:         /sbin/zfs
Provides:         /sbin/zpool
Provides:         /sbin/zdb
Provides:         /sbin/ztest
Provides:         /sbin/zstreamdump
Provides:         /sbin/mount.zfs

%description
ZFS is an advanced modern general-purpose filesystem from Sun
Microsystems, originally designed for Solaris/OpenSolaris.

This project is a port of ZFS to the FUSE framework for the Linux
operating system.

%prep
%setup -q

%patch -P 0 -p0
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p0
%patch -P 4 -p1
%patch -P 5 -p1

f=LICENSE
mv $f $f.iso88591
iconv -o $f -f iso88591 -t utf8 $f.iso88591
rm -f $f.iso88591

chmod -x contrib/test-datasets
chmod -x contrib/find-binaries
chmod -x contrib/solaris/fixfiles.py
chmod -x contrib/zfsstress.py
cp -f /usr/lib/rpm/redhat/config.{guess,sub} src/lib/libumem/

%build
%define _warning_options '-Wall'
export CCFLAGS="%{optflags}"
pushd src

scons debug=2 optim='%{optflags}'

%install
pushd src
scons debug=1 install install_dir=%{buildroot}%{_sbindir} man_dir=%{buildroot}%{_mandir}/man8/ cfg_dir=%{buildroot}/%{_sysconfdir}/%{name}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -Dp -m 0755 %{SOURCE2} %{buildroot}%{_libexecdir}/%{name}-scrub
install -Dp -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -Dp -m 0755 %{SOURCE4} %{buildroot}%{_sbindir}/zfs-fuse-helper
install -Dp -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}-scrub.service
install -Dp -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}-scrub.timer

%ifnarch aarch64 ppc64le
#set stack not executable, BZ 911150
for i in zdb zfs zfs-fuse zpool ztest; do
       /usr/bin/execstack -c %{buildroot}%{_sbindir}/$i
done
%endif

%post
# Move cache if upgrading
oldcache=/etc/zfs/zpool.cache      # this changed per 0.6.9, only needed when upgrading from earlier versions
newcache=/var/lib/zfs/zpool.cache

if [[ -f $oldcache && ! -e $newcache ]]; then
  echo "Moving existing zpool.cache to new location"
  mkdir -p $(dirname $newcache)
  mv $oldcache $newcache
else
  if [ -e $oldcache ]; then
    echo "Note: old zpool.cache present but no longer used ($oldcache)"
  fi
fi

%systemd_post zfs-fuse.service

%preun
%systemd_preun zfs-fuse.service

%postun
%systemd_postun_with_restart zfs-fuse.service 
if [ $1 -lt 1 ] ; then
echo "Removing files since we removed the last package"
rm -rf /var/run/zfs
rm -rf /var/lock/zfs
fi

%files
%license LICENSE
%doc BUGS CHANGES contrib HACKING README
%doc README.NFS STATUS TESTING TODO
%{_sbindir}/zdb
%{_sbindir}/zfs
%{_sbindir}/zfs-fuse
%{_sbindir}/zfs-fuse-helper
%{_sbindir}/zpool
%{_sbindir}/zstreamdump
%{_sbindir}/ztest
%{_sbindir}/mount.zfs
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-scrub.service
%{_unitdir}/%{name}-scrub.timer
%{_libexecdir}/%{name}-scrub
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sysconfdir}/%{name}/
%{_mandir}/man8/zfs-fuse.8.gz
%{_mandir}/man8/zdb.8.gz
%{_mandir}/man8/zfs.8.gz
%{_mandir}/man8/zpool.8.gz
%{_mandir}/man8/zstreamdump.8.gz

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.7.2.2-28
- Fix postun logic.

* Mon Jun 12 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.7.2.2-27
- Require initscripts

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.7.2.2-26
- migrated to SPDX license

* Tue Feb 14 2023 Arjun Shankar <arjun@redhat.com> - 0.7.2.2-25
- Port to C99

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.7.2.2-21
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.2.2-19
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.7.2.2-17
- Move from cron.weekly to systemd timer unit.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.7.2.2-14
- Fix FTBFS.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.7.2.2-11
- port to libtirpc

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Karsten Hopp <karsten@redhat.com> - 0.7.2.2-7
- fix syntax for python3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Neal Gompa <ngompa13@gmail.com> - 0.7.2.2-4
- Move binaries to /usr/sbin for compatibility with other zfs implementations

* Tue Mar 14 2017 Jon Ciesla <limburgher@gmail.com> - 0.7.2.2-3
- Systemd cleanup

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Jon Ciesla <limburgher@gmail.com> - 0.7.2.2-1
- Update to new upstream, 0.7.2.2, adds ARM build and pool v28.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 04 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-22
- Use new execstack (#1247795)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 08 2014 Karsten Hopp <karsten@redhat.com> 0.7.0-20
- only use execstack on archs with prelink
- fix ppc64le detection as littleendian
- use up2date config.{guess,sub} with ppc64le support

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.0-18
- Cleanup and modernise spec
- Update systemd scriptlets to the latest standard
- Update exclude arch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Jon Ciesla <limburgher@gmail.com> - 0.7.0-16
- Fix format-security FTBFS, BZ 1037411.

* Tue Aug 13 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-15
- ExcludeArch ARM, BZ 993168.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-13
- Fixed date, systemd-units BR.

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.7.0-12
- Perl 5.18 rebuild

* Fri May 24 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-11
- Fix unit file typo, BZ 966850.

* Fri Feb 15 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-10
- Patch to add stack-protector and FORTIFY_SOURCE, BZ 911150.

* Thu Feb 14 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-9
- Set stack not executable on some binaries, BZ 911150.

* Tue Jan 29 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-8
- Correct OOM immunization.
- Drop PrivateTmp to fix mount issue, BZ 904643.

* Tue Jan 15 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-7
- Fix directory ownership, BZ 894517.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 12 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.0-5
- Add hardened build.

* Wed Mar 14 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.0-4
- Migrate to systemd.

* Tue Feb 28 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.0-3
- Partially decrufted spec.

* Tue Feb 28 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.0-2
- Fixed sysconfig permissions, BZ 757488.

* Mon Feb 27 2012 Jon Ciesla <limburgher@gmail.com> - 0.7.0-1
- New upstream, fix FTBFS BZ 716087.
- Patch out bad umem declaration.
- Stop starting automatically in post. BZ 755464.
- Marked sysconfig file noreplace, BZ 772403.
- Setting weekly scrub to off by default in sysconfig to silence crob job if service disabled, BZ 757488 et. al.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-9.20100709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-8.20100709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 01 2010 Uwe Kubosch <uwe@kubosch.no> - 0.6.9-7.20100709git
- Moved to fedpkg and git
- Fixed missing dependency to libaio

* Fri Jul 09 2010 Uwe Kubosch <uwe@kubosch.no> - 0.6.9-6.20100709git
- Updated to upstream maintenance snapshot.
- Fixes build problems on EL5
- Added zfs-fuse man page
- Removed package patching of linked libraries

* Mon Jul 05 2010 Uwe Kubosch <uwe@kubosch.no> - 0.6.9-5
- Cleanup of RPM spec and init script

* Sun Jul 04 2010 Uwe Kubosch <uwe@kubosch.no> - 0.6.9-4
- Patched SConstruct to define NDEBUG instead of DEBUG to avoid debug code while still generating debug symbols
- Added moving of zfs.cache when updating from pre 0.6.9 version

* Sat Jul 03 2010 Uwe Kubosch <uwe@kubosch.no> - 0.6.9-2
- Updated to upstream stable release 0.6.9
- Patched default debug level from 0 to 1
- Fixed missing compiler flags and debug flag in build: BUG 595442

* Sat May 22 2010 Uwe Kubosch <uwe@kubosch.no> - 0.6.9_beta3-6
- Updated to upstream version 0.6.9_beta3
- Add more build requires to build on F13 BUG 565076
- Add patches for missing libraries and includes to build on F13 BUG 565076
- Added packages for ppc and ppc64
- Build on F13 BUG 565076
- Fixes BUG 558172
- Added man files
- Added zfs_pool_alert
- Added zstreamdump
- Fixed bug in automatic scrub script BUG 559518

* Mon Jan 04 2010 Uwe Kubosch <uwe@kubosch.no> - 0.6.0-6
- Added option for automatic weekly scrubbing.
  Set ZFS_WEEKLY_SCRUB=yes in /etc/sysconfig/zfs-fuse to enable
- Changed ZFS_AUTOMOUNT option value from "1" to "yes" for better readability.
  ZFS_AUTOMOUNT=1 deprecated and will be removed in version 0.7.0.
- Added option for killing processes with unknown working directory at zfs-fuse startup.
  This would be the case if zfs-fuse crashed.  Use with care.  It may kill unrelated processes.
  Set ZFS_KILL_ORPHANS=yes_really in /etc/sysconfig/zfs-fuse to enable.
- Relaxed dependency on fuse from 2.8.0 to 2.7.4 to allow installation on RHEL/Centos 5

* Sat Dec 26 2009 Uwe Kubosch <uwe@kubosch.no> - 0.6.0-5
- Removed chckconfig on and service start commands from install script
  See https://fedoraproject.org/wiki/Packaging:SysVInitScript#Why_don.27t_we

* Sat Dec 26 2009 Uwe Kubosch <uwe@kubosch.no> - 0.6.0-4
- Updated to upstream version 0.6.0 STABLE

* Mon Nov 30 2009 Uwe Kubosch <uwe@kubosch.no> - 0.6.0-3
- Updated the home page URL to http://zfs-fuse.net/

* Sat Nov 28 2009 Uwe Kubosch <uwe@kubosch.no> - 0.6.0-2
- Corrected some KOJI build errors.

* Fri Nov 27 2009 Uwe Kubosch <uwe@kubosch.no> - 0.6.0-1
- Updated to upstream version 0.6.0 BETA
- Updated dependency to Fuse 2.8.0
- Minor change in spec: Source0 to Source00 for consistency

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-9.20081221.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Karsten Hopp <karsten@redhat.com> 0.5.0-8.20081221.1
- excludearch s390, s390x as there is no implementation for atomic instructions

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8.20081221
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Uwe Kubosch <uwe@kubosch.no> - 0.5.0-7.20081221
- Updated etc/init.d/zfs-fuse init script after feedback from Rudd-O
  Removed limits for the fuse process which could lead to a hung system
  or use lots of memory.

* Sun Dec 28 2008 Uwe Kubosch <uwe@kubosch.no> - 0.5.0-6.20081221
- Updated etc/init.d/zfs-fuse init script after feedback from Rudd-O at
  http://groups.google.com/group/zfs-fuse/browse_thread/thread/da94aa803bceef52
- Adds better wait at startup before mounting filesystems.
- Add OOM kill protection.
- Adds syncing of disks at shutdown.
- Adds pool status when asking for service status.
- Changed to start zfs-fuse at boot as default.
- Changed to start zfs-fuse right after installation.
- Cleanup of /var/run/zfs and /var/lock/zfs after uninstall.

* Wed Dec 24 2008 Uwe Kubosch <uwe@kubosch.no> - 0.5.0-5.20081221
- Development tag.

* Sun Dec 21 2008 Uwe Kubosch <uwe@kubosch.no> - 0.5.0-4.20081221
- Updated to upstream trunk of 2008-12-21
- Added config file in /etc/sysconfig/zfs
- Added config option ZFS_AUTOMOUNT=0|1 to mount filesystems at boot

* Tue Nov 11 2008 Uwe Kubosch <uwe@kubosch.no> - 0.5.0-3.20081009
- Rebuild after import into Fedora build system.

* Thu Oct 09 2008 Uwe Kubosch <uwe@kubosch.no> - 0.5.0-2.20081009
- Updated to upstream trunk of 2008-10-09
- Adds changes to make zfs-fuse build out-of-the-box on Fedora 9,
  and removes the need for patches.

* Sat Oct  4 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.5.0-1 
- initial build
