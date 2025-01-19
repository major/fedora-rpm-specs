Name:           macchanger
Version:        1.7.0
Release:        28%{?dist}
Summary:        An utility for viewing/manipulating the MAC address of network interfaces
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later

URL:            https://github.com/alobbs/macchanger
#               http://www.alobbs.com/macchanger

#Source0:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
#Source1:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig

Source0:        https://github.com/alobbs/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

# no OUI update at the moment
#Patch0:         macchanger-1.X.0-OUI-list-update.diff

# prefer /dev/urandom as source of seed for random
Patch1:         macchanger-1.7.0-seed-source.diff
# fix compile time warnings to make package build with -Werror
Patch2:         macchanger-1.7.0-werror.diff

# texinfo is only needed when .info rebuild is required
#BuildRequires:    texinfo
BuildRequires: make
BuildRequires:  gcc


%description
Features:
  * set specific MAC address of a network interface
  * set the MAC randomly
  * set a MAC of another vendor
  * set another MAC of the same vendor
  * reset MAC address to its original permanent hardware value
  * display a vendor MAC list (more than 18000 items)


%prep
%setup -q
%patch -P1 -p1 -b .seedsource
%patch -P2 -p1 -b .werror


%build
CFLAGS="$RPM_OPT_FLAGS -Werror"
%configure
make %{?_smp_mflags} V=1


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_infodir}/*.info.*
%{_mandir}/man1/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.0-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.7.0-14
- Remove hardcoded gzip suffix from GNU info pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Tomas Hoger <thoger@fedoraproject.org> - 1.7.0-11
- Add BuildRequires: gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul  4 2014 Tomas Hoger <thoger@fedoraproject.org> - 1.7.0-3
- Format string fix to actually build with -Werror

* Fri Jul  4 2014 Tomas Hoger <thoger@fedoraproject.org> - 1.7.0-2
- Build package with -Werror

* Fri Jul  4 2014 Tomas Hoger <thoger@fedoraproject.org> - 1.7.0-1
- Update to upstream 1.7.0
- Licence change from GPLv2+ to GPLv3+
  https://github.com/alobbs/macchanger/issues/3#issuecomment-31526964
- Upstream sources are now on github, no more signatures :-(
- Dropped patches - fixes applied upstream:
  1.6.0-dynamic-lists.diff
  1.6.0-dev-name-overflow.diff
  1.6.0-endding.diff
  1.6.0-doc-cleanup.diff
  1.6.0-bia-fix.diff
  1.6.0-show-default.diff
- New patche for 1.7.0:
  1.7.0-seed-source.diff - keep preferring /dev/urandom as seed source

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  1 2013 Tomas Hoger <thoger@fedoraproject.org> - 1.6.0-1
- Update to upstream 1.6.0 (RHBZ#928256)
- Dropped patches - fixes applied upstream:
  1.5.0-OUI-list-update.diff
  1.5.0-man-update.diff
  1.5.0-random-seed.diff
  1.5.0-exit-code.diff
  1.5.0-formatstr-warning.diff
  1.5.0-permanent-mac.diff
- Patches updated for 1.6.0:
  1.6.0-dynamic-lists.diff
  1.6.0-dev-name-overflow.diff
  1.6.0-endding.diff
- New patches for 1.6.0:
  1.6.0-bia-fix.diff - fix regression from new --bia option
    https://github.com/alobbs/macchanger/issues/1
  1.6.0-show-default.diff - change default action to --show
    https://github.com/alobbs/macchanger/issues/4
  1.6.0-doc-cleanup.diff - documentation cleanup
- Add GPLv2 text, no longer included in 1.6.0 upstream sources.
- texinfo BuildRequires is no longer temporary, as upstream tarball does not
  include .info any more and it needs to be built at compile time.
- Use verbose build output (make V=1).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Tomas Hoger <thoger@fedoraproject.org> - 1.5.0-11
- Fix build warning caused by bad format string (size_t).
- Fix command line argument typo: endding -> ending, see Debian bug
  http://bugs.debian.org/621698
- Add option to reset MAC address to hardware permanent address.
  Patch by Anders Sundman, taken from the Debian macchanger package.
- Add texinfo BuildRequires to rebuild .info from updated .texi.
- Minor correction of the man-update patch.
- Update OUI list from IEEE, now more than 15000 items listed

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Tomas Hoger <thoger@fedoraproject.org> - 1.5.0-9
- Fix buffer overflow when excessively long device name is specified as
  command line argument (caught by FORTIFY_SOURCE, RHBZ#641704)
- Add Debian patch fixing exit code for certain error conditions, see
  Debian bug http://bugs.debian.org/547596
- Update OUI list from IEEE, now more than 14000 items listed

* Wed Sep  2 2009 Tomas Hoger <thoger@fedoraproject.org> - 1.5.0-8
- Fix pseudo random number generator seeding (RHBZ#520268)
- Update OUI list from IEEE, now more than 12000 items listed
- Update man page to list -s / --show
- Fix handling of internal mac lists where static array was still assumed,
  while dynamically allocated array was used

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5.0-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-4
- Autorebuild for GCC 4.3

* Sat Mar 24 2007 Damien Durand <splinux@fedoraproject.org> - 1.5.0-3
- Fix doc section

* Sat Mar 24 2007 Damien Durand <splinux@fedoraproject.org> - 1.5.0-2
- Remove info directory in the install section

* Thu Mar 22 2007 Damien Durand <splinux@fedoraproject.org> - 1.5.0-1
- Initial RPM release
