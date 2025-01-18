%define _legacy_common_support 1
Name:           fatsort
Version:        1.6.3.622
Release:        11%{?dist}
Summary:        FAT sorter for FAT16 and FAT32 filesystems

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://fatsort.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires: make
# FIXME: Cannot run tests, because bbe is not available


%description
Fatsort is a utility written in C to sort FAT16 and FAT32 filesystems. It is
needed to sort files on cheap mp3 players that display files not sorted by
their name but by the order they appear in the file allocation table (FAT).


%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"


%install
%make_install SBINDIR=%{_sbindir} MANDIR=%{_mandir}/man1


%files
%license LICENSE.txt
%doc CHANGES.md README
%{_mandir}/man1/fatsort.1*
%{_sbindir}/fatsort


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3.622-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.3.622-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3.622-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3.622-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3.622-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3.622-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3.622-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3.622-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3.622-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3.622-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 11 2021 Till Maas <opensource@till.name> - 1.6.3.622-1
- New version

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2.605-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Jeff Law <law@redhat.com> - 1.6.2.605-4
- Enable legacy_common_support

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2.605-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2.605-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 01 2020 Till Maas <opensource@till.name> - 1.6.2.605-1
- Update to latest release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2.439-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2.439-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2.439-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2.439-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2.439-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 30 2017 Till Maas <opensource@till.name> - 1.4.2.439-1
- Update to new release
- Cleanup specfile

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.365-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.365-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.365-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.365-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.365-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 31 2014 Till Maas <opensource@till.name> - 1.3.365-1
- Update to latest release
- Cleanup spec

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.355-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.355-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 04 2014 Till Maas <opensource@till.name> - 1.2.355-3
- Add help2man BR

* Sat Jan 04 2014 Till Maas <opensource@till.name> - 1.2.355-2
- Harden build

* Sat Jan 04 2014 Till Maas <opensource@till.name> - 1.2.355-1
- Update to new release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.331-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 Till Maas <opensource@till.name> - 1.1.331-1
- Update to new release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17.269-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17.269-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Till Maas <opensource@till.name> - 0.9.17.269-1
- Update to new release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16.254-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Till Maas <opensource@till.name> - 0.9.16.254-1
- Update to new release

* Sun Oct 30 2011 Till Maas <opensource@till.name> - 0.9.15.247-1
- Update to new release
- Adjust to new upstream location

* Sat Aug 27 2011 Till Maas <opensource@till.name> - 0.9.14-1
- Update to new release
- Add manpage

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 08 2010 Till Maas <opensource@till.name> - 0.9.10-4
- Use %%global instead of %%define

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Till Maas <opensource@till.name> - 0.9.10-1
- Update to new release

* Tue Dec 02 2008 Till Maas <opensource@till.name> - 0.9.9.1-2
- Fix typo in %%description

* Tue Dec 02 2008 Till Maas <opensource@till.name> - 0.9.9.1-1
- Update to new release, that really contains the upstreamed patches

* Tue Dec 02 2008 Till Maas <opensource@till.name> - 0.9.9-1
- Update to new release
- Remove upstreamed patches

* Sat Nov 22 2008 Till Maas <opensource@till.name> - 0.9.8.3-2
- Update summary and description

* Tue Jul 15 2008 Till Maas <opensource@till.name> - 0.9.8.3-1
- Update to new version
- Fix Makefile install target

* Mon Jul 07 2008 Till Maas <opensource@till.name> - 0.9.8.2-2
- Fix CFLAGS handling in the Makefile (Red Hat Bug #454212)

* Wed Jun 11 2008 Till Maas <opensource till name> - 0.9.8.2-1
- New upstream release

* Wed Jun 11 2008 Till Maas <opensource till name> - 0.9.8.1-1
- New upstream release

* Mon Jun 09 2008 Till Maas <opensource till name> - 0.9.8-1
- New upstream release
- move install to Makefile/patch
- ChangeLog is now CHANGES
- Disable stripping in Makefile

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.7.1-3
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Till Maas <opensource till name> - 0.9.7.1-2
- bump version for rebuild
- update License Tag

* Sun May 06 2007 Till Maas <opensource till name> - 0.9.7.1-1
- new version (fatsort supports >4GB filesystems now)

* Thu Feb 01 2007 Till Maas <opensource till name> - 0.9.7-1
- version bump
- added some linebreaks in changelog
- changed e-mail address obfuscation
- corrected time of changelog entries

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.9.6.1-8
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Till Maas <opensource till name> - 0.9.6.1-7
- Fixed typos in changelog

* Sat Sep 02 2006 Till Maas <opensource till name> - 0.9.6.1-6
- Bumped release to build again because of yum failure on ppc

* Sat Sep 02 2006 Till Maas <opensource till name> - 0.9.6.1-5
- Bumped release to make "make tag" work

* Sat Sep 02 2006 Till Maas <opensource till name> - 0.9.6.1-4
- Bumped release for mass rebuild

* Fri Jul 28 2006 Till Maas <opensource till name> - 0.9.6.1-3
- Use $RPM_OPT_FLAGS instead of %%{optflags}

* Tue Jul 04 2006 Till Maas <opensource till name> - 0.9.6.1-2
- made Source0 to valid URL

* Sat Jul 01 2006 Till Maas <opensource till name> - 0.9.6.1-1
- new version 

* Fri Jun 30 2006 Till Maas <opensource till name> - 0.9.6-1
- Created from scratch for fedora extras
