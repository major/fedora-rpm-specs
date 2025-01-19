Name:    mtd-utils
Version: 2.2.1
Release: 2%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Summary: Utilities for dealing with MTD (flash) devices
URL:     http://www.linux-mtd.infradead.org/
Source0: ftp://ftp.infradead.org/pub/mtd-utils/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: gcc
BuildRequires: libacl-devel
BuildRequires: libuuid-devel
BuildRequires: libzstd-devel
BuildRequires: lzo-devel
BuildRequires: zlib-devel

%description
The mtd-utils package contains utilities related to handling MTD devices,
and for dealing with FTL, NFTL JFFS2 etc.

%package ubi
Summary: Utilities for dealing with UBI

%description ubi
The mtd-utils-ubi package contains utilities for manipulating UBI on 
MTD (flash) devices.

%package tests
Summary: Test utilities for mtd-utils

%description tests
Various test programs related to mtd-utils

%prep
%autosetup -p1

%build
%configure
%{make_build}

%install
%{make_install}


%files
%license COPYING
%{_sbindir}/doc*
%{_sbindir}/flash*
%{_sbindir}/ftl*
%{_sbindir}/jffs2dump
%{_sbindir}/jffs2reader
%{_sbindir}/lsmtd
%{_sbindir}/mkfs.jffs2
%{_sbindir}/mtd_debug
%{_sbindir}/nand*
%{_sbindir}/nftl*
%{_sbindir}/recv_image
%{_sbindir}/rfd*
%{_sbindir}/serve_image
%{_sbindir}/sumtool
%{_sbindir}/mkfs.ubifs
%{_sbindir}/mtdinfo
%{_sbindir}/mtdpart
%{_sbindir}/fectest
%{_mandir}/*/*


%files ubi
%{_sbindir}/ubi*
%{_sbindir}/mount.ubifs

%files tests
%{_libexecdir}/mtd-utils/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 26 2024 Josh Boyer <jwboyer@fedoraproject.org> - 2.2.1-1
- Update to latest upstream release (RhBug 2133047)

* Wed Sep 25 2024 Josh Boyer <jwboyer@fedoraproject.org> - 2.2.0-1
- Update to latest upstream release (RhBug 2133047)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.6-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 30 2023 Josh Boyer <jwboyer@fedoraproject.org> - 2.1.6-1
- Update to latest upstream release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Josh Boyer <jwboyer@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4 (RhBug 2037579)

* Mon Jul 26 2021 Josh Boyer <jwboyer@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3 (RhBug 1985792)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2 (#1856257)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.1-1
- Update to 2.1.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Josh Boyer <jwboyer@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.1-1
- Update to 2.0.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Josh Boyer <jwboyer@fedoraproject.org> 2.0.0-1
- Update to 2.0.0

* Tue Aug 23 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.2-1
- Update to 1.5.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.1-5
- Append -stdc=gnu89 to CFLAGS (Work-around to c11 compatibility
  issues. Fix F23FTBFS, RHBZ#1239701).
- Append V=1 to make-call to make building verbose.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Update to 1.5.1 (#1087285)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Josh Boyer <jwboyer@redhat.com>
- Update to 1.5.0 (#820903)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Josh Boyer <jwboyer@gmail.com>
- Update to 1.4.9 (#755183)

* Sun Aug 21 2011 Josh Boyer <jwboyer@gmail.com>
- Update to 1.4.6 (#693323)

* Sun Mar 20 2011 Josh Boyer <jwboyer@gmail.com>
- Update to 1.4.3 (#684374)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 01 2010 David Woodhouse <David.Woodhouse@intel.com> - 1.3.1-1
- Update to 1.3.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 02 2008 David Woodhouse <david.woodhouse@intel.com> - 1.2.0-1
- Update to 1.2.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.0-3
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 David Woodhouse <dwmw2@infradead.org> - 1.1.0-2
- Build ubi-utils

* Wed Aug 22 2007 David Woodhouse <dwmw2@infradead.org> - 1.1.0-1
- Update to 1.1.0 + nandtest + multicast utils

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> - 1.0.1-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 David Woodhouse <dwmw2@infradead.org> - 1.0.1-1
- Update to 1.0.1

* Tue May  2 2006 David Woodhouse <dwmw2@infradead.org> - 1.0.0-2
- Fixes from review (include COPYING), BR zlib-devel
- Include device_table.txt

* Sun Apr 30 2006 David Woodhouse <dwmw2@infradead.org> - 1.0.0-1
- Initial build.

