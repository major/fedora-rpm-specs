Summary: Bluetooth HCI protocol analyser
Name: bluez-hcidump
Version: 2.5
Release: 28%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
URL: http://www.bluez.org/
Requires: glibc >= 2.2.4
Requires: bluez-libs >= 3.14
BuildRequires:  gcc
BuildRequires: glibc-devel >= 2.2.4
BuildRequires: bluez-libs-devel >= 3.14
BuildRequires: pkgconfig
BuildRequires: make
ExcludeArch: s390 s390x

%description
Protocol analyser for Bluetooth traffic.

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%prep

%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README
%{_sbindir}/hcidump
%{_mandir}/man8/hcidump.8.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5-27
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 04 2012 Bastien Nocera <bnocera@redhat.com> 2.5-1
- Update to 2.5

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Bastien Nocera <bnocera@redhat.com> 2.4-1
- Update to 2.4

* Fri Mar 02 2012 Bastien Nocera <bnocera@redhat.com> 2.3-1
- Update to 2.3

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 30 2011 Bastien Nocera <bnocera@redhat.com> 2.2-1
- Update to 2.2

* Mon Jun 20 2011 Bastien Nocera <bnocera@redhat.com> 2.1-1
- Update to 2.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Bastien Nocera <bnocera@redhat.com> 2.0-1
- Update to 2.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 22 2008 - David Woodhouse <David.Woodhouse@intel.com> - 1.42-2
- Rebuild for libbluetooth.so.3

* Tue Jun 17 2008 - Bastien Nocera <bnocera@redhat.com> - 1.42-1
- Update to 1.42

* Tue Mar 04 2008 David Woodhouse <dwmw2@infradead.org> - 1.41-1
- update to bluez-hcidump 1.41

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.40-2
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 David Woodhouse <dwmw2@infradead.org> - 1.40-1
- update to bluez-hcidump 1.40
- update licence

* Sat Jul 21 2007 David Woodhouse <dwmw2@infradead.org> - 1.37-1
- update to bluez-hcidump 1.37

* Tue Jan 30 2007 David Woodhouse <dwmw2@redhat.com> - 1.33-1
- update to bluez-hcidump 1.33

* Sat Sep 30 2006 David Woodhouse <dwmw2@redhat.com> - 1.32-1
- update to bluez-hcidump 1.32
- Fix BNEP IPv6 parsing (#196879)
- Support IPv6 in -n and -s options (#196878)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.31-5.1
- rebuild

* Sun Jun 11 2006 David Woodhouse <dwmw2@redhat.com> 1.31-5
- Upload 1.31 tarball now that the lookaside works again

* Sun Jun 11 2006 David Woodhouse <dwmw2@redhat.com> 1.31-4
- BuildRequire pkgconfig so that the autocrap stuff doesn't break

* Sun Jun 11 2006 David Woodhouse <dwmw2@redhat.com> 1.31-3
- Rebuild now that new bluez-libs is actually in the repo

* Sun Jun 11 2006 David Woodhouse <dwmw2@redhat.com> 1.31-2
- use 1.30 tarball and patch, since lookaside cache seems broken

* Sun Jun 11 2006 David Woodhouse <dwmw2@redhat.com> 1.31-1
- update to bluez-hcidump 1.31

* Thu Feb 23 2006 David Woodhouse <dwmw2@redhat.com> 1.30-1
- Ipdate to bluez-hcidump 1.30

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.27-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.27-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Nov 6 2005 David Woodhouse <dwmw2@redhat.com> 1.27-1
- update to bluez-hcidump 1.27

* Mon Aug 8 2005 David Woodhouse <dwmw2@redhat.com> 1.24-1
- update to bluez-hcidump 1.24
- require bluez-libs 1.18

* Tue Mar 2 2005 David Woodhouse <dwmw2@redhat.com> 1.18-1
- update to bluez-hcidump 1.18

* Tue Jan 12 2005 David Woodhouse <dwmw2@redhat.com> 1.16-1
- update to bluez-hcidump 1.16

* Tue Sep 22 2004 David Woodhouse <dwmw2@redhat.com> 1.11-1
- update to bluez-hcidump 1.11

* Tue Aug 02 2004 David Woodhouse <dwmw2@redhat.com> 1.10-1
- update to bluez-hcidump 1.10

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 12 2004 David Woodhouse <dwmw2@redhat.com>
- update to bluez-hcidump 1.8

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 25 2003 David Woodhosue <dwmw2@redhat.com> 1.5-2
- Fix get_unaligned() -- don't abuse kernel headers.

* Thu Apr 24 2003 David Woodhouse <dwmw2@redhat.com>
- Initial build
