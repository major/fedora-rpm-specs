%global dbus_version 1.2
%global dbus_glib_version 0.82
%global glib2_version 2.15.0
%global gudev_version 147
%global polkit_version 0.97
%global parted_version 1.8.8
%global udev_version 143
%global mdadm_version 2.6.7
%global device_mapper_version 1.02
%global libatasmart_version 0.14
%global sg3_utils_version 1.27
%global smp_utils_version 0.94
%global systemd_version 185

Summary: Storage Management Service
Name: udisks
Version: 1.0.5
Release: 29%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.freedesktop.org/wiki/Software/udisks
Source0: http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
# https://bugs.freedesktop.org/show_bug.cgi?id=90778
Patch0:  udisks-1.0.5-fix-build-with-glibc-2.20.patch
Patch1:  fix_bash_completion.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1238664
Patch2:  udisks-1.0.5-fix-service-file.patch
Patch3:  udisks-1.0.5-fix-makedev-failure.patch
BuildRequires: make
BuildRequires: pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(dbus-1)  >= %{dbus_version}
BuildRequires: pkgconfig(dbus-glib-1) >= %{dbus_glib_version}
BuildRequires: pkgconfig(polkit-gobject-1) >= %{polkit_version}
BuildRequires: parted-devel >= %{parted_version}
BuildRequires: pkgconfig(devmapper) >= %{device_mapper_version}
BuildRequires: pkgconfig(libudev) >= %{udev_version}
BuildRequires: intltool
BuildRequires: pkgconfig(libatasmart) >= %{libatasmart_version}
BuildRequires: pkgconfig(gudev-1.0) >= %{gudev_version}
%if 0%{?fedora} > 17 || 0%{?rhel} > 6
BuildRequires: pkgconfig(systemd) >= %{systemd_version}
%else
BuildRequires: pkgconfig(libudev) >= %{udev_version}
%endif
BuildRequires: sg3_utils-devel >= %{sg3_utils_version}
BuildRequires: gtk-doc
# Needed for patch 3.
BuildRequires: autoconf automake libtool
BuildRequires: systemd
# needed to pull in the system bus daemon
Requires: dbus >= %{dbus_version}
# needed to pull in the udev daemon
Requires: udev >= %{udev_version}
# we need at least this version for bugfixes / features etc.
Requires: libatasmart >= %{libatasmart_version}
Requires: mdadm >= %{mdadm_version}
# for smp_rep_manufacturer
Requires: smp_utils >= %{smp_utils_version}
# for mount, umount, mkswap
Requires: util-linux
# for mkfs.ext3, mkfs.ext3, e2label
Requires: e2fsprogs
# for mkfs.xfs, xfs_admin
Requires: xfsprogs
# for mkfs.vfat
Requires: dosfstools
# for mlabel
Requires: mtools
# For ejecting removable disks
Requires: eject
# for mkntfs - no ntfsprogs on ppc, though
%ifnarch ppc ppc64
Requires: ntfsprogs
%endif
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# for /proc/self/mountinfo, only available in 2.6.26 or higher
Conflicts: kernel < 2.6.26

# Obsolete and Provide DeviceKit-disks - udisks provides exactly the same
# ABI just with a different name and versioning-scheme
#
Obsoletes: DeviceKit-disks <= 009
Provides: DeviceKit-disks = 010

%description
udisks provides a daemon, D-Bus API and command line tools
for managing disks and storage devices.

%package devel
Summary: D-Bus interface definitions for udisks
Requires: %{name} = %{version}-%{release}

# See comment above
#
Obsoletes: DeviceKit-disks-devel <= 009
Provides: DeviceKit-disks-devel = 010

%description devel
D-Bus interface definitions and documentation for udisks.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# https://bugzilla.redhat.com/show_bug.cgi?id=673544#c15
rm -f src/*-glue.h tools/*-glue.h

autoreconf --force --install


%build
%configure --enable-gtk-doc
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# for now, include a compat symlink for the command-line tool
# and man page
ln -s udisks $RPM_BUILD_ROOT%{_bindir}/devkit-disks
ln -s udisks.1 $RPM_BUILD_ROOT%{_datadir}/man/man1/devkit-disks.1

# TODO: should be fixed upstream
chmod 0644 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/udisks-bash-completion.sh
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
mv $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/udisks-bash-completion.sh \
    $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%find_lang %{name}

%post
%systemd_post udisks.service

%preun
%systemd_preun udisks.service

%postun
%systemd_postun_with_restart udisks.service

%files -f %{name}.lang
%doc README AUTHORS NEWS HACKING doc/TODO
%license COPYING
%{_sysconfdir}/avahi/services/udisks.service
%{_sysconfdir}/bash_completion.d/udisks-bash-completion.sh
%{_sysconfdir}/dbus-1/system.d/*.conf
/lib/udev/rules.d/*.rules

/lib/udev/udisks-part-id
/lib/udev/udisks-dm-export
/lib/udev/udisks-probe-ata-smart
/lib/udev/udisks-probe-sas-expander
/sbin/umount.udisks

%{_bindir}/*
%{_libexecdir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man7/%{name}.7*
%{_mandir}/man8/%{name}-daemon.8*
%{_datadir}/polkit-1/actions/*.policy

%{_datadir}/dbus-1/system-services/*.service
%{_unitdir}/udisks.service

%attr(0700,root,root) %dir %{_localstatedir}/lib/udisks

%files devel
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/pkgconfig/udisks.pc
%{_datadir}/gtk-doc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.5-28
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 09 2024 Dan Horák <dan@danny.cz> - 1.0.5-26
- rebuilt for sg3_utils 1.48

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 07 2021 Tomas Bzatek <tbzatek@redhat.com> - 1.0.5-19
- rebuilt for sg3_utils 1.46

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.5-18
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Dan Horák <dan@danny.cz> - 1.0.5-15
- rebuilt for sg3_utils 1.45 (#1809392)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 David King <amigadave@amigadave.com> - 1.0.5-12
- Fix build failure (#1676172)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 13 2016 David King <amigadave@amigadave.com> - 1.0.5-5
- Do not own bash completion directory (#1303443)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 David King <amigadave@amigadave.com> - 1.0.5-3
- Remove needless use of defattr

* Thu Jul 02 2015 David King <amigadave@amigadave.com> - 1.0.5-2
- Fix systemd service file (#1238664)
- Use systemd scriptlet snippets

* Thu Jun 04 2015 David King <amigadave@amigadave.com> - 1.0.5-1
- Update to 1.0.5 (#1075003)
- Use license macro for COPYING
- Use pkgconfig for BuildRequires
- Use SMP flags when building
- Preserve timestamps during install
- Update man page globs in files section

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.0.4-16
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 14 2014 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.0.4-13
- fix CVE-2014-0004

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.0.4-11
- Move bash completion to %%{_sysconfdir}/bash_completion.d (#584569).

* Sun Feb 24 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.0.4-10
- Fix bash completion as per RHBZ 584569

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Adam Jackson <ajax@redhat.com> 1.0.4-7%{?dist}
- Rebuild for new libudev
- Conditional BuildReqs for {libudev,systemd}-devel

* Sat Apr 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.4-6
- Add dependency on eject - fixes RHBZ 810882

* Thu Mar 15 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.4-5
- rebuild (parted)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 David Zeuthen <davidz@redhat.com> - 1.0.4-2%{?dist}
- Add patch to neuter the annoying systemd behavior where stdout/stderr
  is sent to the system logs (#743344)

* Fri Aug 26 2011 David Zeuthen <davidz@redhat.com> - 1.0.4-1%{?dist}
- Update to release 1.0.4 and update BR + files to reflect that lvm2 is no
  longer enabled given recommendations from upstream (lvm2 support in
  udisks never worked well and caused a lot more problems than it solved)
- Remove /etc/tmpfiles.d/udisks.conf hack since this is now created on demand

* Thu Aug 25 2011 David Zeuthen <davidz@redhat.com> - 1.0.3-3%{?dist}
- Use tmpfiles.d for /var/run dir (#733161)

* Mon Jul 18 2011 Dan Horák <dan@danny.cz> - 1.0.3-2%{?dist}
- rebuilt for sg3_utils 1.31

* Mon Jul 11 2011 David Zeuthen <davidz@redhat.com> - 1.0.3-1%{?dist}
- Update to 1.0.3

* Sat Apr  9 2011 Christopher Aillon <caillon@redhat.com> 1.0.2-4%{?dist}
- Bump release to match what's in Fedora 14

* Thu Apr  7 2011 Matthias Clasen <mclasen@redhat.com> 1.0.2-1%{?dist}
- Update to 1.0.2
- Nuke generated D-Bus code to force regeneration and avoid potential
  dbus-glib bug. Credit goes to Tomáš Trnka <tomastrnka@gmx.com> for
  figuring this out (#673544 comment 15)

* Fri Jan 28 2011 Matthias Clasen <mclasen@redhat.com> - 1.0.1-7%{?dist}
- %%ghost /var/run content (#656709)

* Tue Jan 25 2011 Matthias Clasen <mclasen@redhat.com> - 1.0.1-6%{?dist}
- BR gtk-doc

* Mon Aug 23 2010 Matthias Clasen <mclasen@redhat.com> - 1.0.1-5%{?dist}
- Co-own /usr/share/gtk-doc (#604420)
- Some other packaging cleanups

* Wed May 19 2010 David Zeuthen <davidz@redhat.com> - 1.0.1-4%{?dist}
- Actually make udisks work with latest liblvm2app

* Wed May 05 2010 Adam Tkac <atkac redhat com> - 1.0.1-3%{?dist}
- rebuilt against new lvm2 libraries

* Tue Apr 13 2010 Dan HorÃ¡k <dan@danny.cz> - 1.0.1-2%{?dist}
- rebuilt for sg3_utils 1.29

* Fri Apr 09 2010 David Zeuthen <davidz@redhat.com> - 1.0.1-1%{?dist}
- Update to release 1.0.1 (CVE-2010-1149 ,fdo #27494)

* Tue Mar 30 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-2%{?dist}
- Bump release and rebuild so we link to the new libparted.

* Mon Mar 15 2010 David Zeuthen <davidz@redhat.com> - 1.0.0-1%{?dist}
- Update to release 1.0.0

* Tue Feb 23 2010 David Zeuthen <davidz@redhat.com> - 1.0.0-0.git20100223.1%{?dist}
- Update to new git snapshot

* Tue Feb 16 2010 David Zeuthen <davidz@redhat.com> - 1.0.0-0.git20100215.3%{?dist}
- Require lvm2-libs >= 2.02.61 to get the right ABI for liblvm2app

* Tue Feb 16 2010 David Zeuthen <davidz@redhat.com> - 1.0.0-0.git20100215.2%{?dist}
- Update for new liblvm2app library

* Mon Feb 15 2010 David Zeuthen <davidz@redhat.com> - 1.0.0-0.git20100215.1%{?dist}
- Update to git snapshot

* Fri Jan 15 2010 David Zeuthen <davidz@redhat.com> - 1.0.0-0.git20100115.2%{?dist}
- Rebuild

* Fri Jan 15 2010 David Zeuthen <davidz@redhat.com> - 1.0.0-0.git20100115.1%{?dist}
- New git snapshot with LVM support

* Tue Jan 12 2010 David Zeuthen <davidz@redhat.com> - 1.0.0-0.git20091202.3%{?dist}
- Rebuild for new libparted

* Mon Dec 07 2009 David Zeuthen <davidz@redhat.com> - 1.0.0-0.git20091202.2%{?dist}
- Rebuild

* Fri Dec 04 2009 David Zeuthen <davidz@redhat.com> - 1.0.0-0.git20091202.1%{?dist}
- Updated for package review (#543608)

* Wed Dec 02 2009 David Zeuthen <davidz@redhat.com> - 1.0.0-0.git20091202%{?dist}
- Git snapshot for upcoming 1.0.0 release
