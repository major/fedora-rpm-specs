Summary:        A program for recovering corrupt partition tables
Name:           gpart
Version:        0.3
Release:        23%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/baruch/%{name}/
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/baruch/gpart/pull/16
Patch0:         fsf_address.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

%description
Gpart is a small tool which tries to guess what partitions are on a PC
type harddisk in case the primary partition table was damaged.


%prep
%autosetup
autoreconf -f -i


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING
%if 0%{?el7}
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/*
%else
%dir %{_pkgdocdir}
%{_pkgdocdir}/*
%endif
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 14 2024 David Cantrell <dcantrell@redhat.com> - 0.3-21
- Correct license to GPL-2.0-or-later

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 Jonathan Wright <jonathan@almalinux.org> - 0.3-16
- Update spec to use more macros
- Update source to proper GitHub format
- Update license to SPDX format
- Add doc dir to files
- Remove excluded arches (build on all arches)
- Remove unnecessary buildrequires glibc-kernheaders
- Initial build for EPEL7, EPEL8, and EPEL9

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 01 2015 David Cantrell <dcantrell@redhat.com> - 0.3-1
- Upgrade to gpart-0.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.1-2
- Update Exclude/Exclusive arch
- Modernise spec

* Mon Oct 13 2014 David Cantrell <dcantrell@redhat.com> - 0.2.1-1
- Upgrade to newly discovered upstream fork on github (#1151790)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1h-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1h-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 David Cantrell <dcantrell@redhat.com> - 0.1h-20
- Build gpart with RPM_OPT_FLAGS and fix O_CREAT usage in
  make_mbr_backup() function in gpart.c (#977147)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1h-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 David Cantrell <dcantrell@redhat.com> - 0.1h-18
- Add x86_64 to the ExclusiveArch listing
- Patch gm_ntfs.h so it works on x86_64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1h-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1h-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1h-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1h-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 21 2010 David Cantrell <dcantrell@redhat.com> - 0.1h-13
- Spec file cleanups to comply with current packaging policies

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1h-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 manuel "lonely wolf" wolfshant <wolfy@fedoraproject.org> - 0.1h-11
- replacing %%exclusive arch i386 with %%{ix86}

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1h-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 David Cantrell <dcantrell@redhat.com> - 0.1h-9
- Rebuild for gcc-4.3

* Sat Dec 01 2007 David Cantrell <dcantrell@redhat.com> - 0.1h-8
- Merge review (#225853)

* Tue Aug 21 2007 David Cantrell <dcantrell@redhat.com> - 0.1h-7
- Rebuild

* Thu Aug 02 2007 David Cantrell <dcantrell@redhat.com> - 0.1h-6
- License field updated to GPLv2+

* Sat Feb 03 2007 David Cantrell <dcantrell@redhat.com> - 0.1h-5
- Fix spec file problems with merge review (#225853)

* Sun Oct 22 2006 David Cantrell <dcantrell@redhat.com> - 0.1h-4
- Compile with large file support (#211746)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.1h-3.1
- rebuild

* Tue Jun 06 2006 Chris Lumens <clumens@redhat.com> 0.1h-3
- Fix building on i386 by using the right syscall stuff.

* Tue Jun 06 2006 Jesse Keating <jkeating@redhat.com> - 0.1h-2
- Added missing BR glibc-kernheaders

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.1h-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Jun 10 2005 Chris Lumens <clumens@redhat.com> 0.1h-1
- Initial build.
