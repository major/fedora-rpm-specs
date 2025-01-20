%global _hardened_build 1
%define download_dir 3310

Name:           pmount
Version:        0.9.23
Release:        33%{?dist}
Summary:        Enable normal user mount

# realpath.c is GPLv2+. Others are GPL+;
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pmount.alioth.debian.org/
# BEWARE: The number in the url determines the content, ahs to be updated each time.
Source0:        http://alioth.debian.org/frs/download.php/%{download_dir}/%{name}-%{version}.tar.bz2
# don't set the setuid bits during make install
Patch0:         pmount-0.9.17-nosetuid.patch
# Add exfat support
# https://bugs.launchpad.net/ubuntu/+source/pmount/+bug/1524523
Patch1:         pmount.exfat.patch
Patch2:         pmount-c99.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  e2fsprogs-devel
BuildRequires:  libblkid-devel

# ntfs-3g may be used too, it is considered optional, will be used if installed.
Requires:       cryptsetup
Requires:       /bin/mount

%description
pmount  ("policy mount") is a wrapper around the standard mount program
which permits normal users to mount removable devices without a  
matching /etc/fstab entry.

Be warned that pmount is installed setuid root.

%prep
%autosetup -p 1

%build
# mount, umount, cryptsetup and ntfs-3g paths are right and don't use rpm 
# macros, so the corresponding configure options are not used. /media/ is
# also rightly used.
%configure \
  --enable-hal=no \
  --with-lock-dir=%{_localstatedir}/lock/pmount \
  --with-whitelist=%{_sysconfdir}/pmount.allow

%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.devel COPYING ChangeLog
%config(noreplace) %{_sysconfdir}/pmount.allow
%attr(4755,root,root) %{_bindir}/pmount
%attr(4755,root,root) %{_bindir}/pumount
%{_mandir}/man1/p*mount*.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.9.23-32
- Remove quiet and nonempty exfat mount options

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.23-31
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Florian Weimer <fweimer@redhat.com> - 0.9.23-25
- Port to C99 (#2152707)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.9.23-22
- Add exfat support

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.9.23-20
- replace cryptsetup-liks runtime requirement with cryptsetup
- modernize specfile

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Richard Shaw <hobbes1069@gmail.com> - 0.9.23-2
- Fix cflags to meet packaging guidelines for packages that contain suid
  binaries. Fixes BZ# 965459.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Richard Shaw <hobbes1069@gmail.com> - 0.9.23-1
- Update to latest upstream release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 21 2011 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 0.9.22-3
- Drop HAL support (Fedora 15 Features/HalRemoval)
- Remove TODO with obsolete information in favor of README.devel

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 28 2010 Jan Zeleny <jzeleny@redhat.com> - 0.9.22-1
- rebased to 0.9.22 (fixed #577614, calling luksClose correctly)

* Wed Sep 23 2009 Stepan Kasal <skasal@redhat.com> - 0.9.20-1
- new upstream version
- adjust BuildRequires

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 25 2008 Patrice Dumas <pertusus@free.fr> 0.9.17-3
- rediff nosetuid patch

* Sat Mar  1 2008 Patrice Dumas <pertusus@free.fr> 0.9.17-2
- update to 0.9.17
- remove pmount-0.9.13-keeppublic.patch now that dbus connection is private

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.13-2
- Autorebuild for GCC 4.3

* Sun Sep 24 2006 Patrice Dumas <pertusus@free.fr> 0.9.13-1
- initial packaging
