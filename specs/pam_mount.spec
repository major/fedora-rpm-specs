Name:           pam_mount
Version:        2.20
Release:        3%{?dist}
Summary:        A PAM module that can mount volumes for a user session

# The library and binaries are LGPLv2.1+ with these Exceptions:
# "pmvarrun" and "mount.crypt" programs, especially their .c file are under GPLv2+
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://inai.de/projects/pam_mount/
Source0:        https://inai.de/files/pam_mount/%{name}-%{version}.tar.xz
Source1:        https://inai.de/files/pam_mount/%{name}-%{version}.tar.asc
# GPG key from official website: https://inai.de/about/
Source2:        gpgkey-BCA0C5C309CAC569E74A921CF76EFE5D0C223A8F.asc

# AM_PROG_LIBTOOL is obsolete
Patch0:         pam_mount-2.16-LTINIT.patch

# For source verification with gpgv
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cryptsetup-devel
BuildRequires:  gcc
BuildRequires:  gpg
BuildRequires:  libHX-devel >= 3.12.1
BuildRequires:  libmount-devel >= 2.20
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl-interpreter
BuildRequires:  xz

Requires:       libHX%{?_isa} >= 3.12.1
Requires:       hxtools
Requires:       pam%{?_isa}
Requires:       libcryptmount%{?_isa} = %{version}-%{release}


%description
This module is aimed at environments with central file servers that a user
wishes to mount on login and unmount on logout, such as (semi-)diskless
stations where many users can logon and where statically mounting the entire
/home from a server is a security risk, or listing all possible volumes in
/etc/fstab is not feasible.

* Users can define their own list of volumes without having to change
  (possibly non-writable) global config files.
* Single sign-on feature - the user needs to type the password just once (at login)
* Transparent mount process
* No stored passwords
* Volumes are unmounted on logout, freeing system resources and not leaving
  data exposed.

The module also supports mounting local filesystems of any kind the normal
mount utility supports, with extra code to make sure certain volumes are set up
properly because often they need more  than just a mount call, such as
encrypted volumes. This includes SMB/CIFS, FUSE, dm-crypt and LUKS.

If  you  intend  to use pam_mount to protect volumes on your computer using an
encrypted filesystem system, please know that there are many other issues you
need to consider in order to protect your data. For example, you probably want
to disable or encrypt your swap partition (the cryptoswap can help you do
this). Do not assume  a  system  is  secure  without  carefully  considering
potential threats.


%prep
rm -f %{SOURCE2}.gpg ; gpg --dearmor %{SOURCE2}
xzcat %{SOURCE0} | gpgv --quiet --keyring %{SOURCE2}.gpg %{SOURCE1} -
%setup -q
%patch -P0 -p1 -b.LTINIT
./autogen.sh


%build
%configure                     \
  --with-dtd                   \
  --with-slibdir=%{_libdir}    \
  --with-ssbindir=%{_sbindir}
%make_build


%install
%make_install
rm -f %{buildroot}%{_libdir}/libcryptmount.la


%ldconfig_scriptlets


%files
%doc doc/faq.txt doc/options.txt doc/todo.txt
# generated from manpage, no need to package it twice:
#doc/pam_mount.txt
%doc config/pam_mount.conf.xml
%license COPYING LICENSE.GPL2 LICENSE.GPL3 LICENSE.LGPL2 LICENSE.LGPL3
%config(noreplace) %{_sysconfdir}/security/pam_mount.conf.xml
%{_libdir}/security/pam_mount.so
%{_sbindir}/pmvarrun
%{_sbindir}/pmt-ehd
%{_sbindir}/mount.crypt
%{_sbindir}/umount.crypt
%{_sbindir}/mount.crypt_LUKS
%{_sbindir}/umount.crypt_LUKS
%{_sbindir}/mount.crypto_LUKS
%{_sbindir}/umount.crypto_LUKS
%{_mandir}/man5/pam_mount.conf.5*
%{_mandir}/man8/mount.crypt.8*
%{_mandir}/man8/mount.crypt_LUKS.8*
%{_mandir}/man8/mount.crypto_LUKS.8*
%{_mandir}/man8/pam_mount.8*
%{_mandir}/man8/pmt-ehd.8*
%{_mandir}/man8/pmvarrun.8*
%{_mandir}/man8/umount.crypt.8*
%{_mandir}/man8/umount.crypt_LUKS.8*
%{_mandir}/man8/umount.crypto_LUKS.8*
%ghost %{_localstatedir}/run/pam_mount
%dir %{_datadir}/xml/pam_mount/
%dir %{_datadir}/xml/pam_mount/dtd/
%{_datadir}/xml/pam_mount/dtd/pam_mount.conf.xml.dtd

%package -n libcryptmount
Summary: Library to mount crypto images and handle key files
%description -n libcryptmount
libcryptmount takes care of the many steps involved in making a
crypto image (file) available as a mountable block device, including
supplemental key file decryption, loop device setup and crypto device
setup. It supports pam_mount style plain EHD2/OpenSSL images and LUKS
and transparent use of the OS's crypto layer.
%files -n libcryptmount
%{_libdir}/libcryptmount.so
%{_libdir}/libcryptmount.so.0
%{_libdir}/libcryptmount.so.0.0.0

%package -n libcryptmount-devel
Summary: Development files for libcryptmount
Requires: libcryptmount = %{version}
%description -n libcryptmount-devel
libcryptmount takes care of the many steps involved in making a
crypto image (file) available as a mountable block device, including
supplemental key file decryption, loop device setup and crypto device
setup. It supports pam_mount style plain EHD2/OpenSSL images and LUKS
and transparent use of the OS's crypto layer.
%files -n libcryptmount-devel
%{_includedir}/libcryptmount.h
%{_libdir}/pkgconfig/libcryptmount.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Chen Chen <aflyhorse@hotmail.com> - 2.20-2
- Fix License section

* Wed Sep 04 2024 Chen Chen <aflyhorse@hotmail.com> - 2.20-1
- Update to 2.20

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.19-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Chen Chen <aflyhorse@hotmail.com> - 2.19-1
- Update to 2.19

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 19 2021 Chen Chen <aflyhorse@hotmail.com> - 2.18-3
- The build now uses PCRE2 instead of PCRE1
- Remove libglib dependency

* Fri Dec 17 2021 Chen Chen <aflyhorse@hotmail.com> - 2.18-2
- Switch sources from http to https

* Mon Nov 01 2021 Björn Esser <besser82@fedoraproject.org> - 2.18-1
- Update to 2.18

* Mon Nov 01 2021 Björn Esser <besser82@fedoraproject.org> - 2.16-15
- Fix BuildRequires
- Whitespace cleanup
- Fix explicit Requires
- Modernize spec file
- Sort (Build)Requires by alphabet
- Add patch to replace obsolete use of AM_PROG_LIBTOOL

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.16-14
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Till Maas <opensource@till.name> - 2.16-9
- Actually apply the patch

* Tue Jan 14 2020 Till Maas <opensource@till.name> - 2.16-8
- Support LUKS2 volumes (https://bugzilla.redhat.com/show_bug.cgi?id=1773362)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Till Maas <opensource@till.name> - 2.16-3
- Remove unneeded dependency on readlink

* Wed Nov 08 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.16-2
- Rebuild for cryptsetup-2.0.0

* Tue Oct 31 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.16-1
- Update to 2.16 (OpenSSL 1.1 compatibility)
- Use /usr/bin instead of /bin in Requires

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 01 2014 Till Maas <opensource@till.name> - 2.15-1
- Update to latest release with upstreamed patches and an additional bugfix
  (#1122250)
- Add automatic GPG key verification
- Harden build
- Update %%description
- Install to %%{_libdir}

* Fri Nov 28 2014 Till Maas <opensource@till.name> - 2.14-4
- Remove usage of deprecated -p0 mount option (#1167684)
- Support utab (#1161601)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 05 2013 Till Maas <opensource@till.name> - 2.14-1
- Update to new release
- Update BRs
- doc/changelog.txt was renamed to doc/news.txt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-5.20130707git966c6bea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 07 2013 Till Maas <opensource@till.name> - 2.13-4.20130707git966c6bea
- Update to GIT snapshot due to missing releases
- Remove lz compression handling from SPEC
- fix bogus dates (wrong day of week) in earlier changelog entries

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Till Maas <opensource@till.name> - 2.13-1
- Update to new release
- Update dependencies
- Remove obsoleted patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 30 2011 Till Maas <opensource@till.name> - 2.5-2
- %%ghost /var/run/pam_mount (RH #656656)
- rebuild because of new libcryptsetup

* Mon Aug 16 2010 Till Maas <opensource@till.name> - 2.5-1
- Update to lastest release
- Update libHX dependency
- remove upstreamed patches
- do not package pam_mount.txt (RH #615714)

* Sat Jul 03 2010 Till Maas <opensource@till.name> - 2.4-2
- Add cryptsetup-luks-libs Requires
- list all manpages explicitly

* Fri Jul 02 2010 Till Maas <opensource@till.name> - 2.4-1
- Update to new release
- add patch to keep cmtab at /etc
- add patch to use mount -t crypt instead of mount.crypt for crypto volumes
- BR cryptsetup-luks-devel >= 1.1.2
- add man-db BR for Fedora >= 14 for pam_mount.8 to pam_mount.txt conversion
- add Patch to remove man-db BR for Fedora < 14

* Wed May 19 2010 Till Maas <opensource@till.name> - 2.3-1
- Update to new release

* Sun May 16 2010 Till Maas <opensource@till.name> - 2.2-1
- Update to new release

* Sun May 16 2010 Till Maas <opensource@till.name> - 2.1-1
- Update to new release
- Add BuildRequires: cryptsetup-luks-devel
- Cleanup BRs
- Add Requires: /bin/readlink
- Update libHX dependency

* Mon Jan 04 2010 Till Maas <opensource@till.name> - 1.32-2
- Do not package compatibility symlinks anymore

* Thu Sep 24 2009 Till Maas <opensource@till.name> - 1.32-1
- Update to new release
- Update libHX dependency

* Fri Aug 28 2009 Till Maas <opensource@till.name> - 1.30-2
- rebuilt with new openssl

* Thu Aug 27 2009 Till Maas <opensource@till.name> - 1.30-1
- Update to new release

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.27-4
- rebuilt with new openssl

* Fri Aug 07 2009 Till Maas <opensource@till.name> - 1.27-3
- Use %%global instead of %%define
- BR: lzip only if the tarball might be packaged with lzip / has a .lz suffix

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 02 2009 Till Maas <opensource@till.name> - 1.27-1
- Update to new release

* Mon Apr 13 2009 Till Maas <opensource@till.name> - 1.22-1
- Update to new release
- Support remount (Red Hat Bugzilla: #492347)
- Show more correct mount options in /etc/mtab
- backport fix against uninitialized value

* Tue Mar 03 2009 Till Maas <opensource@till.name> - 1.20-1
- Update to new release
- Update libHX dependency

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Till Maas <opensource@till.name> - 1.18-1
- Update to new release

* Wed Jan 28 2009 Till Maas <opensource@till.name> - 1.17-1
- Update to new release

* Wed Jan 28 2009 Till Maas <opensource@till.name> - 1.9-1
- Update to new release

* Tue Jan 20 2009 Till Maas <opensource@till.name> - 1.8-1
- Update to new release

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.4-2
- rebuild with new openssl

* Thu Nov 27 2008 Till Maas <opensource@till.name> - 1.4-1
- Update to new release
- Add patch to support fsck mount option

* Sun Oct 26 2008 Till Maas <opensource@till.name> - 1.2-2
- Add patch to mount luks volumes without -o cipher

* Sat Oct 25 2008 Till Maas <opensource@till.name> - 1.2-1
- Update to new release
- remove config conversion script
- add crypt_LUKS symlinks
- remove psmisc dependency, lsof is no longer used

* Wed Oct 08 2008 Till Maas <opensource@till.name> - 0.49-1
- Update to new release

* Sat Sep 13 2008 Till Maas <opensource@till.name> - 0.48-2
- Update libHX dependencies
- remove lsof dependency
- Add patch to fix convert_pam_mount_conf.pl by Stephen P. Schaefer
  (Red Hat Bug 462155)

* Thu Sep 11 2008 Till Maas <opensource@till.name> - 0.48-1
- Update to new version

* Fri Sep 05 2008 Till Maas <opensource@till.name> - 0.47-1
- Update to new version that includes a security fix:
  https://sourceforge.net/project/shownotes.php?release_id=624240
- Add lzma BR and unpack source manually
- Update libHX requirements
- add new binary

* Mon Jun 23 2008 Till Maas <opensource@till.name> - 0.41-2
- Add patch to fix <or> handling in config file, reference:
  Red Hat Bugzilla #448485 comment 9
  http://sourceforge.net/tracker/index.php?func=detail&aid=1974442&group_id=41452&atid=430593
  comment from 2008-06-19 10:29

* Tue Jun 17 2008 Till Maas <opensource till name> - 0.41-1
- Update to new version

* Wed Jun 11 2008 Till Maas <opensource till name> - 0.40-1
- Update to new version
- set make variable V for full compiler commandline

* Mon May 05 2008 Till Maas <opensource till name> - 0.35-1
- Update to new version
- Use $RPM_BUILD_ROOT instead of %%{buildroot}
- Update description
- create and own %%{_localstatedir}/run/pam_mount

* Sun Feb 24 2008 Till Maas <opensource till name> - 0.33-1
- update to new version

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.32-3
- Autorebuild for GCC 4.3

* Mon Jan 07 2008 Till Maas <opensource till name> - 0.32-2
- fix config conversion scriptlet

* Mon Jan 07 2008 Till Maas <opensource till name> - 0.32-1
- update to new version
- add default/example config to %%doc

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 0.29-2
 - Rebuild for deps

* Wed Oct 10 2007 Till Maas <opensource till name> - 0.29-1
- bump to new version
- remove uneeded patches
- add config file conversion script and convert config in %%post

* Thu Aug 23 2007 Till Maas <opensource till name> - 0.18-2
- add README.Fedora
- add patch to wait for applications that do not process pam properly
- update license tag

* Sun Dec 10 2006 Till Maas <opensource till name> - 0.18-1
- Version bump
- removed Patch0
- adding LICENSE.GPL2 to %%doc with LICENSE.*
- removed ChangeLog (is empty)
- removed NEWS (nothing interesting)
- removed INSTALL
- removed BR: zlib-devel, already in openssl-devel
- added -p to install to preserve timestamp

* Thu Sep 07 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.17-5
- Upstream update
- Build on x86_64

* Sun Aug 27 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.13.0-9
- Rebuild for FC6

* Wed Jul 05 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.13.0-8
- don't add a local loop.h for rawhide

* Wed Jul 05 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.13.0-4
- added patch for bz #188284
- spec tidy, removed unused buildreq on kernel-devel

* Wed Apr 05 2006 W. Michael Petullo <mike[@]flyn.org> - 0.13.0-3
   - Ship LICENSE.LGPL2.

* Sun Apr 02 2006 W. Michael Petullo <mike[@]flyn.org> - 0.13.0-2
   - Don't use --owner=root or --group=root on install.

* Sun Apr 02 2006 W. Michael Petullo <mike[@]flyn.org> - 0.13.0-1
   - Updated to pam_mount 0.13.0.
   - Added patch to allow to build with local loop.h (see RH BZ 174190.)
   - Ensure module installed in RPM_BUILD_ROOT when building package.

* Sun Jan 01 2006 W. Michael Petullo <mike[@]flyn.org> - 0.11.0-1
   - Updated to pam_mount 0.11.0.
   - Mike Petullo is no longer the up-stream maintainer.
   - Change URL.
   - Change Source.

* Thu Jun 09 2005 W. Michael Petullo <mike[@]flyn.org> - 0.9.25-4
   - Bump release for devel.

* Thu Jun 09 2005 W. Michael Petullo <mike[@]flyn.org> - 0.9.25-3
   - Bump release for FC-4.

* Thu Jun 09 2005 W. Michael Petullo <mike[@]flyn.org> - 0.9.25-2
   - Bump release for FC-3.

* Thu Jun 09 2005 W. Michael Petullo <mike[@]flyn.org> - 0.9.25-1
   - Updated to pam_mount 0.9.25.

* Thu Jun 09 2005 W. Michael Petullo <mike[@]flyn.org> - 0.9.25-1
   - Updated to pam_mount 0.9.25.

* Sat May 14 2005 W. Michael Petullo <mike[@]flyn.org> - 0.9.24-1
   - Updated to pam_mount 0.9.24.

* Wed May 04 2005 W. Michael Petullo <mike[@]flyn.org> - 0.9.23-1
   - Updated to pam_mount 0.9.23.

   - Remove fdr from version.

   - Get rid of rel variable.

   - %%{PACKAGE_VERSION} to %%{name}-%%{version}.

* Thu Feb 10 2005 W. Michael Petullo <mike[@]flyn.org> - 0.9.22-0.fdr.1
   - Updated to pam_mount 0.9.22.

   - Should now build properly on x86-64.

* Sun Dec 12 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.21-0.fdr.1
   - Updated to pam_mount 0.9.21.

* Fri Jul 23 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.20-0.fdr.1
   - Updated to pam_mount 0.9.20.

* Sun Jun 27 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.19-0.fdr.1
   - Updated to pam_mount 0.9.19.

   - Moved policy sources to /etc/selinux.

* Sun Apr 25 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.18-0.fdr.1
   - Updated to pam_mount 0.9.18.

   - Added mount.crypt and umount/crypt.

   - Added pmvarrun.

* Wed Apr 21 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.17-0.fdr.1
   - Updated to pam_mount 0.9.17.

   - Added pam_mount_macros.te.

* Tue Mar 23 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.16-0.fdr.1
   - Updated to pam_mount 0.9.16.

   - Ensure pam_mount.conf etc. has safe permissions (install vs. cp).

   - Don't compress documentation files.

   - Don't set distribution in .spec.

   - Remove uneeded prefix definition.

   - Fix buildroot.

* Wed Mar 10 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.15-0.fdr.1
   - Updated to pam_mount 0.9.15.

   - Added zlib-devel to BuildRequires.

* Tue Feb 10 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.14-0.fdr.1
   - Updated to pam_mount 0.9.14.

   - Added pam_mount_auth.so and pam_mount_session.so to package.

* Sun Jan 25 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.13-0.fdr.1
   - Updated to pam_mount 0.9.13.

* Sat Jan 24 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.12-0.fdr.2
   - RPM specification work.

* Fri Jan 23 2004 W. Michael Petullo <mike[@]flyn.org> - 0.9.12-0.fdr.1
   - Updated to pam_mount 0.9.12.
