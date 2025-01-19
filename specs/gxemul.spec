Name:		gxemul
Version:	0.7.0
Release:	11%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
Summary:	Instruction-level machine emulator
URL:		http://gavare.se/gxemul/
Source0:	http://gavare.se/gxemul/src/%{name}-%{version}.tar.gz
Patch0:		gxemul-0.6.0.1-Makefile-cleanup.patch
Patch1:		gxemul-0.6.0.1-gcc47.patch
# https://sourceforge.net/p/gxemul/mailman/message/37270384/
Patch2:		gxemul-0.7.0-linux-fix.patch
Patch3:		gxemul-0.7.0-no-rpath.patch
BuildRequires:	libX11-devel, xorg-x11-proto-devel
BuildRequires:	gcc
BuildRequires:	make

%description
GXemul is an experimental instruction-level machine emulator. It can be
used to run binary code for (among others) MIPS-based machines, regardless
of host platform. Several emulation modes are available. For some modes,
processors and surrounding hardware components are emulated well enough to
let unmodified operating systems (e.g. NetBSD) run as if they were running
on a real machine.

%prep
%setup -q
%patch -P0 -p1 -b .cleanup
%patch -P1 -p1
%patch -P2 -p1 -b .linux-fix
%patch -P3 -p1 -b .no-rpath

%build
CFLAGS="$RPM_OPT_FLAGS" PREFIX="%{_prefix}" ./configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc LICENSE HISTORY README demos/
%doc %{_datadir}/doc/gxemul/
%{_bindir}/gxemul
%{_mandir}/man1/gxemul.*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.0-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Tom Callaway <spot@fedoraproject.org> - 0.7.0-1
- update to 0.7.0

* Thu Feb 25 2021 Tom Callaway <spot@fedoraproject.org> - 0.6.3.1-1
- update to 0.6.3.1

* Tue Feb 16 2021 Tom Callaway <spot@fedoraproject.org> - 0.6.3-1
- update to 0.6.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Tom Callaway <spot@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Tom Callaway <spot@fedoraproject.org> - 0.6.0.2-1
- update to 0.6.0.2

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 0.6.0.1-11
- add BuildRequires: gcc, gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.0.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Aug 20 2014 Tom Callaway <spot@fedoraproject.org> - 0.6.0.1-1
- update to 0.6.0.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for c++ ABI breakage

* Sun Jan 22 2012 Tom Callaway <spot@fedoraproject.org> - 0.6.0-4
- fix compile with gcc 4.7 (may have been an issue with 4.6 too)
- do not run the test suite at make install

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.0-1
- update to 0.6.0

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.7.2-3
- fix urls

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.7.2-1
- update to 0.4.7.2

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 18 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.4.6.6-1
- update to 0.4.6.6

* Fri Sep 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.6.5-1
- update to 0.4.6.5

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.6.2-2
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.4.6.2-1
- bump to 0.4.6.2

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.4.6-3.1
- drop patch

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.4.6-3
- rebuild for ppc32

* Thu Jul  5 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.4.6-1
- bump to 0.4.6

* Wed Jan 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.4.3-1
- bump to 0.4.3

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.4.2-1
- bump to 0.4.2

* Tue Jul 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.4.0.1-3
- add demos/ to doc

* Fri Jul  7 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.4.0.1-2
- fix FC-4 BuildRequires

* Thu Jul  6 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.4.0.1-1
- bump to 0.4.0.1

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.8-1
- bump to 0.3.8

* Mon Jan  9 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.7-1
- bump to 0.3.7
- enable all the cpu types by default (MIPS, ARM, PPC are primary)

* Thu Jul 28 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.4-1
- initial package for Fedora Extras
