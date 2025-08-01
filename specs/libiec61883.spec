Summary:        Streaming library for IEEE1394
Name:           libiec61883
Version:        1.2.0
Release:        38%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
Source:         http://www.kernel.org/pub/linux/libs/ieee1394/%{name}-%{version}.tar.gz
# Fedora specific patches.

Patch0:         libiec61883-1.2.0-installtests.patch
Patch1:         libiec61883-channel-allocation-without-local-node-rw.patch
URL:            http://ieee1394.wiki.kernel.org/index.php/Libraries#libiec61883
ExcludeArch:    s390 s390x

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
# Works only with newer libraw1394 versions
BuildRequires:  libraw1394-devel
BuildRequires:  libtool
BuildRequires:  make

%description
The libiec61883 library provides an higher level API for streaming DV,
MPEG-2 and audio over IEEE1394.  Based on the libraw1394 isochronous
functionality, this library acts as a filter that accepts DV-frames,
MPEG-2 frames or audio samples from the application and breaks these
down to isochronous packets, which are transmitted using libraw1394.

%package devel
Summary:        Development files for libiec61883
Requires:       %{name} = %{version}-%{release}

%description devel
Development files needed to build applications against libiec61883

%package utils
Summary:        Utilities for use with libiec61883
Requires:       %{name} = %{version}-%{release}

%description utils
Utilities that make use of iec61883

%prep
%autosetup -p1

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/libiec61883.so.*

%files devel
%{_libdir}/libiec61883.so
%dir %{_includedir}/libiec61883
%{_includedir}/libiec61883/*.h
%{_libdir}/pkgconfig/libiec61883.pc

%files utils
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-36
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Simone Caronni <negativo17@gmail.com> - 1.2.0-29
- Rebuild autotools scripts to avoid running sed.
- Drop ldconfig scriptlets.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Nils Philippsen <nils@tiptoe.de> - 1.2.0-25
- Indent consistently
- Use %%autosetup

* Tue Jan 05 2021 Tom Stellard <tstellar@redhat.com> - 1.2.0-25
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.0-19
- require gcc for building

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 24 2010 Parag Nemade <paragn AT fedoraproject.org> 1.2.0-5
- Merge-review cleanup (#226030)

* Fri Jan 8 2010 Jay Fenlason <fenlason@redhat.com> 1.2.0-4
- Update the Source and URL fields to point to correct locations.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Jarod Wilson <jarod@redhat.com> 1.2.0-1
- Update to libiec61883 v1.2.0 release
- Rework installtests patch to not require autoreconf
- Make iso channel allocation work w/o local fw node r/w

* Tue Jul 22 2008 Jarod Wilson <jwilson@redhat.com> 1.1.0-5
- Bump and rebuild for libraw1394 v2.0.0

* Thu Feb 14 2008 Jarod Wilson <jwilson@redhat.com> 1.1.0-4
- Bump and rebuild with gcc 4.3

* Wed Dec 19 2007 Jarod Wilson <jwilson@redhat.com> 1.1.0-3
- Fix license and group tags (#411201)
- Clean up spacing and macro/var inconsistency

* Mon Mar 26 2007 Jarod Wilson <jwilson@redhat.com> 1.1.0-2
- Own created directories (#233865)

* Wed Oct 25 2006 Jarod Wilson <jwilson@redhat.com> 1.1.0-1
- Update to 1.1.0 release

* Wed Oct 11 2006 Jarod Wilson <jwilson@redhat.com> 1.0.0-11
- Use %%dist tag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.0.0-10.fc5.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.0-10.fc5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.0-10.fc5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 30 2005 Jarod Wilson <jarod@wilsonet.com> 1.0.0-10
- Add missing autoconf, automake and libtool
  BuildRequires

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Warren Togami <wtogami@redhat.com> 1.0.0-9
- incorporate some spec improvements from Matthias (#172105)

* Mon Sep 19 2005 Warren Togami <wtogami@redhat.com> 1.0.0-8
- split -devel for pkgconfig chain
- remove .a and .la
- exclude s390 and s390x

* Tue Apr  5 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Fixes for building properly on x86_64.

* Mon Mar 28 2005 Jarod Wilson <jarod@wilsonet.com>
- Fixed utils so they build properly

* Sat Feb 26 2005 Jarod Wilson <jarod@wilsonet.com>
- Rolled in utils

* Wed Feb 23 2005 Jarod Wilson <jarod@wilsonet.com>
- Initial build

