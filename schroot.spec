%undefine __cmake_in_source_build

Name: schroot
Version: 1.6.10
Release: 23%{?dist}
Summary: Execute commands in a chroot environment
License: GPLv3+
Url: https://tracker.debian.org/pkg/schroot
Source0: http://ftp.de.debian.org/debian/pool/main/s/schroot/%{name}_%{version}.orig.tar.xz
Source1: schroot.service
Source2: schroot.default
Patch0: schroot-pam.patch
Patch1: schroot-default-config-path.patch
Patch3: schroot-gcc8-assert-fix.patch
Patch4: schroot-po4a.patch

#Debian patches
Patch10: Add-support-for-more-compression-formats.patch
Patch11: Add-SESSION_SOURCE-and-CHROOT_SESSION_SOURCE.patch
Patch12: 10mount-Move-mount-directory-to-var-run.patch
Patch13: Support-union-mounts-with-overlay-as-in-Linux-4.0.patch
Patch14: GCC5-fixes-on-regexes.patch
Patch15: schroot-mount-make-bind-mounts-private.patch
Patch16: schroot-mount-resolve-mount-destinations-while-chrooted.patch
Patch17: fix-test-suite-with-usrmerge.patch
Patch18: Unmount-everything-that-we-can-instead-of-giving-up.patch
Patch19: fix-killprocs.patch
Patch20: fix-bash-completion.patch
Patch21: fix_typos_in_schroot_manpage.patch
Patch22: update_czech_schroot_translation.patch
Patch23: update_french_schroot_manpage_translation_2018.patch
Patch24: update_german_schroot_manpage_translation_2018.patch
Patch25: zfs-snapshot-support.patch
Patch26: cross.patch
Patch27: binfmt-parent-dir.patch
Patch28: reproducible-build.patch


BuildRequires: gcc-c++
BuildRequires: pam-devel
BuildRequires: boost-devel
BuildRequires: lockdev-devel
BuildRequires: libuuid-devel
BuildRequires: lvm2-devel
BuildRequires: btrfs-progs
BuildRequires: debootstrap
BuildRequires: cppunit-devel
BuildRequires: fakeroot
BuildRequires: groff

# from Debian control
BuildRequires: cmake3
BuildRequires: po4a >= 0.40
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: gtest

%description
schroot allows users to execute commands or interactive shells in
different chroots.  Any number of named chroots may be created, and
access permissions given to each, including root access for normal
users, on a per-user or per-group basis.  Additionally, schroot can
switch to a different user in the chroot, using PAM for
authentication and authorisation.  All operations are logged for
security.

Several different types of chroot are supported, including normal
directories in the filesystem, and also block devices.  Sessions,
persistent chroots created on the fly from files (tar with optional
compression and zip) and LVM snapshots are also supported.

schroot supports kernel personalities, allowing the programs run
inside the chroot to have a different personality.  For example,
running 32-bit chroots on 64-bit systems, or even running binaries
from alternative operating systems such as SVR4 or Xenix.

schroot also integrates with sbuild, to allow building packages with
all supported chroot types, including session-managed chroot types
such as LVM snapshots.

schroot shares most of its options with dchroot, but offers vastly
more functionality.


%prep
%autosetup -p1

%build

# schroot now use cmake
%cmake3 \
    -Ddebug=OFF -Ddchroot=OFF -Ddchroot-dsa=OFF \
    -Dbash_completion_dir=/usr/share/bash-completion/completions \
    -Dlvm-snapshot=ON \
    -Dbtrfs-snapshot=ON \
    -Duuid=ON \
    -DBTRFS_EXECUTABLE=/sbin/btrfs \
    -DLVCREATE_EXECUTABLE=/sbin/lvcreate \
    -DLVREMOVE_EXECUTABLE=/sbin/lvremove

#-DSCHROOT_LIBEXEC_DIR=/$(LIBDIR)/schroot \
%cmake_build
#make doc

%install
%cmake_install

install -d -m 755 %{buildroot}%{_unitdir}
install -pm644 %{SOURCE1} %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_sysconfdir}/default
install -pm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/default/schroot

# get rid of uneeded include and library files
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm $RPM_BUILD_ROOT%{_libdir}/pkgconfig/sbuild.pc
#rm -f $RPM_BUILD_ROOT%{_libdir}/libsbuild.la
#rm -f $RPM_BUILD_ROOT%{_libdir}/libsbuild.so*
rm $RPM_BUILD_ROOT%{_libdir}/libsbuild.a

%find_lang %{name}

%check
# cmake3 on epel don't have ctest
%if 0%{?rhel} == 7
fakeroot %cmake test V=1 || :
%else
fakeroot %ctest || :
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS README THANKS TODO
%attr (4755, root, root ) %{_bindir}/schroot
%{_sysconfdir}/default/schroot
%dir %{_sysconfdir}/schroot
%dir %{_sysconfdir}/schroot/chroot.d
%config(noreplace) %{_sysconfdir}/schroot/schroot.conf
%config(noreplace) %{_sysconfdir}/schroot/sbuild
%config(noreplace) %{_sysconfdir}/schroot/buildd
%config(noreplace) %{_sysconfdir}/pam.d/schroot
%config(noreplace) %{_sysconfdir}/schroot/default/copyfiles
%config(noreplace) %{_sysconfdir}/schroot/default/fstab
%config(noreplace) %{_sysconfdir}/schroot/default/nssdatabases
%config(noreplace) %{_sysconfdir}/schroot/desktop/copyfiles
%config(noreplace) %{_sysconfdir}/schroot/desktop/fstab
%config(noreplace) %{_sysconfdir}/schroot/desktop/nssdatabases
%config(noreplace) %{_sysconfdir}/schroot/minimal/copyfiles
%config(noreplace) %{_sysconfdir}/schroot/minimal/fstab
%config(noreplace) %{_sysconfdir}/schroot/minimal/nssdatabases
%dir %{_sysconfdir}/schroot/setup.d
%config(noreplace) %{_sysconfdir}/schroot/setup.d/00check
%config(noreplace) %{_sysconfdir}/schroot/setup.d/05btrfs
%config(noreplace) %{_sysconfdir}/schroot/setup.d/05file
%config(noreplace) %{_sysconfdir}/schroot/setup.d/05lvm
%config(noreplace) %{_sysconfdir}/schroot/setup.d/05union
%config(noreplace) %{_sysconfdir}/schroot/setup.d/05zfs
%config(noreplace) %{_sysconfdir}/schroot/setup.d/10mount
%config(noreplace) %{_sysconfdir}/schroot/setup.d/15killprocs
%config(noreplace) %{_sysconfdir}/schroot/setup.d/15binfmt
%config(noreplace) %{_sysconfdir}/schroot/setup.d/20copyfiles
%config(noreplace) %{_sysconfdir}/schroot/setup.d/20nssdatabases
%config(noreplace) %{_sysconfdir}/schroot/setup.d/50chrootname
%config(noreplace) %{_sysconfdir}/schroot/setup.d/70services
%config(noreplace) %{_sysconfdir}/schroot/setup.d/99check
%dir %{_libexecdir}/schroot
%{_libexecdir}/schroot/schroot-listmounts
%{_libexecdir}/schroot/schroot-mount
#{_libexecdir}/schroot/schroot-releaselock
%dir %{_localstatedir}/lib/schroot
%{_localstatedir}/lib/schroot/session
#{_localstatedir}/lib/schroot/mount
%{_datadir}/bash-completion/completions/schroot
%{_datadir}/%{name}/setup/common-config
%{_datadir}/%{name}/setup/common-data
%{_datadir}/%{name}/setup/common-functions
%{_mandir}/man1/schroot.1.gz
%{_mandir}/man5/schroot-script-config.5.gz
%{_mandir}/man5/schroot-setup.5.gz
%{_mandir}/man5/schroot.conf.5.gz
%{_mandir}/man7/schroot-faq.7.gz
%{_mandir}/*/man1/schroot.1.gz
%{_mandir}/*/man5/schroot-script-config.5.gz
%{_mandir}/*/man5/schroot-setup.5.gz
%{_mandir}/*/man5/schroot.conf.5.gz
%{_mandir}/*/man7/schroot-faq.7.gz
%{_unitdir}/schroot.service

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.6.10-22
- Rebuilt for Boost 1.78

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.6.10-20
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 07 2021 Sérgio Basto <sergio@serjux.com> - 1.6.10-18
- Add more 2 patches from debian
- Clean old files

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.6.10-16
- Rebuilt for Boost 1.75

* Wed Aug 05 2020 Sérgio Basto <sergio@serjux.com> - 1.6.10-15
- Add latest patches from Debian
- Add patch to fix build with newest po4a

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Fix cmake build

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.6.10-12
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.6.10-8
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Sérgio Basto <sergio@serjux.com> - 1.6.10-7
- po4a is now available on ppc64 and we can build schroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Sérgio Basto <sergio@serjux.com> - 1.6.10-5
- Fix rpmlint W: install-file-in-docs /usr/share/doc/schroot/INSTALL

* Thu Jun 14 2018 Sérgio Basto <sergio@serjux.com> - 1.6.10-4
- Add config(noreplace) in all files of /etc (#1585406)

* Fri May 11 2018 Sérgio Basto <sergio@serjux.com> - 1.6.10-3
- Make compatible with epel 7

* Wed May 09 2018 Sérgio Basto <sergio@serjux.com> - 1.6.10-2
- Add patch to fix STL assets with gcc 8

* Wed May 02 2018 Sérgio Basto <sergio@serjux.com> - 1.6.10-1
- Update to 1.6.10
- Add from Debian package, BRs, patches and config files
- Switch to cmake
- Modernize spec file

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.5-23
- Escape macros in %%changelog

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.6.5-22
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.6.5-19
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 1.6.5-18
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 1.6.5-15
- Rebuilt for Boost 1.60

* Mon Sep 07 2015 Jonathan Wakely <jwakely@redhat.com> - 1.6.5-14
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.6.5-12
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.5-10
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 1.6.5-9
- Bump for rebuild.

* Fri Jan 30 2015 Zach Carter <os@zachcarter.com> - 1.6.5-8
- Make sure schroot is suid (BZ1045006,BZ1175351)

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.6.5-7
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.6.5-4
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.6.5-2
- Rebuild for boost 1.54.0

* Wed Jul 3 2013 Zach Carter <z.carter@f5.com> - 1.6.5-1
- Upstream bump to 1.6.5
- Fix for 'make check' issue regarding missing test/run.parts.ex2 directory.

* Tue May 21 2013 Zach Carter <z.carter@f5.com> - 1.4.25-13
- Enable hardened build flags (BZ #965512 and #965485)

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.4.25-12
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.4.25-11
- Rebuild for Boost-1.53.0

* Tue Aug 14 2012 Zach Carter <z.carter@f5.com> - 1.4.25-10
- Rebuild for new boost

* Tue Jul 24 2012 Zach Carter <z.carter@f5.com> - 1.4.25-9
- Bump release to be equal to f17 package
- Add groff to BR

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Zach Carter <z.carter@f5.com> - 1.4.25-7
- Add lvm2-devel to BR, enables lvm-snapshot support

* Thu Apr 12 2012 Zach Carter <z.carter@f5.com> - 1.4.25-1
- New upstream version (removes need for gcc47-patch)
- Add BR to enable unit tests, lvm snapshot, btrfs snapshot support (BZ 811856)
- Add schroot-test-sbuild-util-path.patch

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.23-5
- Rebuilt for c++ ABI breakage

* Tue Jan 17 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4.23-4
- Add schroot-1.4.23-gcc47.patch (Fix mass rebuild FTBFS).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Thomas Spura <tomspur@fedoraproject.org> - 1.4.23-2
- rebuild for https://fedoraproject.org/wiki/Features/F17Boost148

* Thu Jul 21 2011 Zach Carter <z.carter@f5.com> - 1.4.23-1
- rebuild for boost 1.47.0
- fix incorrect %%dir tag for binary in %%files section
- update to new upstream 1.4.23 version

* Wed Apr 20 2011 Zach Carter <z.carter@f5.com> - 1.4.21-2
- rebuild for boost 1.46.1

* Mon Mar 14 2011 Zach Carter <z.carter@f5.com> - 1.4.21-1
- rebuild for boost 1.46.1
- update to 1.4.21

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Zach Carter <z.carter@f5.com> - 1.4.19-1
- rebuild for new boost
- fix boost 1.46 build issue: leaf() function renamed to filename()
- update to 1.4.19

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 1.4.10-2
- rebuild for new boost

* Mon Aug 16 2010 Zach Carter <z.carter@f5.com> - 1.4.10-1
- update to 1.4.10

* Fri Jul 30 2010 Zach Carter <z.carter@f5.com> - 1.4.2-6
- rebuild for boost 1.44 update

* Mon Jul 19 2010 Zach Carter <z.carter@f5.com> - 1.4.2-5
- fix configure and configure.ac to correct boost function call

* Fri Jul 16 2010 Zach Carter <z.carter@f5.com> - 1.4.2-4
- cat config.log on failure.

* Fri Jul 16 2010 Zach Carter <z.carter@f5.com> - 1.4.2-3
- Add some LIBS="-l<lib>" statements to fix build break.

* Wed Jul  7 2010 Zach Carter <z.carter@f5.com> - 1.4.2-2
- Licensing Guidelines Update - add license to dchroot subpackage.

* Thu May 27 2010 Zach Carter <z.carter@f5.com> - 1.4.2-1
- update to 1.4.2
- require libuuid-devel
- add /sbin directories to path in /etc/schroot/default/config BZ588200

* Sat Feb 13 2010 Zach Carter <z.carter@f5.com> - 1.2.3-5
- Specifically call out -lboost_system BZ564770

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.2.3-4
- Rebuild for Boost soname bump
- Fix more than one changelog

* Mon Aug  3 2009 Zach Carter <z.carter@f5.com> - 1.2.3-3
- re-add /etc/schroot/chroot.d directory

* Tue Jul 14 2009 Zach Carter <z.carter@f5.com> - 1.2.3-2
- fix "file listed twice" warnings

* Tue Jul 14 2009 Zach Carter <z.carter@f5.com> - 1.2.3-1
- new upstream version
- compile with --enable-static --disable-shared
- improve dchroot description
- define directory ownership
- add + to GPLv3 license definition

* Tue May  5 2009 Zach Carter <z.carter@f5.com> - 1.2.2-2
- schroot-bind-shm patch to fix DOS issue 

* Sat Apr 25 2009 Zach Carter <z.carter@f5.com> - 1.2.2-1
- update to 1.2.2

* Wed Nov  5 2008 Zach Carter <z.carter@f5.com> - 1.2.1-2
- move libsbuild subpackage into main package
- remove duplicate doc entries
- disable rpath
- defattr for dchroot files

* Mon Sep 15 2008 Zach Carter <z.carter@f5.com> - 1.2.1-1
- bump version to 1.2.1

* Tue May 20 2008 Zach Carter <z.carter@f5.com> - 1.2.0-1
- move dchroot.1.gz to correct subpackage
- removed superfluous Requires: statements
- moved i18n files into libsbuild subpackage
- removed tmpfs patch

* Mon May 12 2008 Zach Carter <z.carter@f5.com> - 1.2.0-1
- Initial version

